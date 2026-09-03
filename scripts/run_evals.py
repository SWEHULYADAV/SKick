#!/usr/bin/env python3
"""Portable repeated-eval harness.

Runner protocol: the command after --runner receives one JSON object on stdin:
  {"case": <eval case>, "run_index": <int>, "suite": <path>}
It should return JSON on stdout. Recommended fields:
  response: str
  passed: bool
  checks: object|array
  usage: {input_tokens, output_tokens, cost, ...}
  metadata: object

The harness intentionally does not invent a semantic judge. Target-runtime adapters can
provide a runner/judge while this script handles repetition, timing, failures and logs.
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_cases(path: Path) -> list[dict]:
    """Load prompt eval cases or normalize declarative portability checks.

    Prompt suites use a top-level ``cases`` array with ``id`` and ``prompt``.
    Portability suites use a top-level ``checks`` array with ``id``, ``path`` and
    ``expect``. The latter are normalized into runner-compatible cases so the
    same harness can list them and, when a dedicated runner is supplied, execute
    structural checks without pretending they are model prompts.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = data.get("cases")
    mode = "cases"
    if not isinstance(cases, list):
        checks = data.get("checks")
        if not isinstance(checks, list):
            raise ValueError(f"{path}: expected top-level cases or checks array")
        mode = "checks"
        cases = []
        for i, check in enumerate(checks):
            if not isinstance(check, dict) or not check.get("id") or not check.get("path") or not check.get("expect"):
                raise ValueError(f"{path}: check #{i} needs id, path and expect")
            normalized = dict(check)
            normalized["prompt"] = f"Portability check for {check['path']}: {check['expect']}"
            normalized["suite_kind"] = "portability_check"
            cases.append(normalized)
    out = []
    for i, case in enumerate(cases):
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            raise ValueError(f"{path}: {mode[:-1] if mode.endswith('s') else mode} #{i} needs id and prompt")
        out.append(case)
    return out


def numeric_usage(result: dict, key: str):
    usage = result.get("usage")
    if isinstance(usage, dict):
        value = usage.get(key)
        if isinstance(value, (int, float)):
            return value
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("suite", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--repetitions", type=int, default=1)
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--list", action="store_true", dest="list_only")
    ap.add_argument("--runner", nargs=argparse.REMAINDER,
                    help="Executable argv; receives JSON on stdin and returns JSON on stdout")
    args = ap.parse_args()

    if args.repetitions < 1:
        ap.error("--repetitions must be >= 1")

    cases = load_cases(args.suite.resolve())
    if args.list_only:
        for case in cases:
            print(f"{case['id']}: {case['prompt']}")
        return 0
    if not args.runner:
        ap.error("--runner is required unless --list is used")

    results = []
    for case in cases:
        for run_index in range(args.repetitions):
            payload = {"case": case, "run_index": run_index, "suite": str(args.suite)}
            started = time.perf_counter()
            record = {
                "case_id": case["id"],
                "run_index": run_index,
                "started_at": utc_now(),
                "runner": args.runner,
            }
            try:
                proc = subprocess.run(
                    args.runner,
                    input=json.dumps(payload),
                    text=True,
                    capture_output=True,
                    timeout=args.timeout,
                    check=False,
                )
                record["duration_seconds"] = time.perf_counter() - started
                record["exit_code"] = proc.returncode
                record["stderr"] = proc.stderr[-8000:]
                if proc.returncode == 0:
                    try:
                        parsed = json.loads(proc.stdout)
                        if not isinstance(parsed, dict):
                            raise ValueError("runner JSON must be an object")
                        record["result"] = parsed
                        record["runner_protocol_ok"] = True
                    except Exception as exc:
                        record["runner_protocol_ok"] = False
                        record["protocol_error"] = str(exc)
                        record["stdout"] = proc.stdout[-16000:]
                else:
                    record["runner_protocol_ok"] = False
                    record["stdout"] = proc.stdout[-16000:]
            except subprocess.TimeoutExpired as exc:
                record["duration_seconds"] = time.perf_counter() - started
                record["exit_code"] = None
                record["runner_protocol_ok"] = False
                record["timeout"] = True
                record["stdout"] = (exc.stdout or "")[-16000:] if isinstance(exc.stdout, str) else ""
                record["stderr"] = (exc.stderr or "")[-8000:] if isinstance(exc.stderr, str) else ""
            results.append(record)
            print(f"{case['id']} run={run_index} protocol_ok={record.get('runner_protocol_ok')}")

    passed = []
    durations = []
    in_tokens = []
    out_tokens = []
    costs = []
    for r in results:
        if isinstance(r.get("duration_seconds"), (int, float)):
            durations.append(r["duration_seconds"])
        res = r.get("result")
        if isinstance(res, dict):
            if isinstance(res.get("passed"), bool):
                passed.append(res["passed"])
            for key, bucket in [("input_tokens", in_tokens), ("output_tokens", out_tokens), ("cost", costs)]:
                value = numeric_usage(res, key)
                if value is not None:
                    bucket.append(value)

    summary = {
        "runs": len(results),
        "protocol_failures": sum(not bool(r.get("runner_protocol_ok")) for r in results),
        "pass_rate": (sum(passed) / len(passed)) if passed else None,
        "duration_mean_seconds": statistics.fmean(durations) if durations else None,
        "input_tokens_mean": statistics.fmean(in_tokens) if in_tokens else None,
        "output_tokens_mean": statistics.fmean(out_tokens) if out_tokens else None,
        "cost_mean": statistics.fmean(costs) if costs else None,
    }
    output = {
        "schema_version": 1,
        "created_at": utc_now(),
        "suite": str(args.suite.resolve()),
        "repetitions": args.repetitions,
        "runner": args.runner,
        "summary": summary,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if summary["protocol_failures"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
