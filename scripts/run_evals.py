#!/usr/bin/env python3
"""Portable repeated-evaluation harness with separated execution and scoring.

Executor protocol (``--runner ...``): receives one JSON object on stdin::

  {"case": <eval case>, "run_index": <int>, "suite": <path>}

It returns candidate JSON on stdout. A candidate ``passed`` field is preserved as
raw metadata but is *not* scoring authority.

Scoring order:

TASK -> EXECUTOR -> RAW CANDIDATE -> DETERMINISTIC CHECKS -> OPTIONAL JUDGE -> AGGREGATE

Deterministic checks are defined in each case's ``checks`` array. Supported types:
``field_equals``, ``exact``, ``contains``, ``not_contains``, ``regex``,
``file_exists`` and ``file_contains``. Filesystem checks require ``--workspace``
and cannot escape that root.

Optional semantic judge protocol (``--judge-command 'cmd ...'``): receives the case,
raw candidate result and deterministic check results, then returns JSON containing
``passed: bool``. Candidate and judge outputs remain separate for re-scoring.
"""
from __future__ import annotations

import argparse
import json
import re
import shlex
import statistics
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def split_command(command: str, *, platform: str | None = None) -> list[str]:
    platform = platform or __import__("os").name
    return shlex.split(command, posix=(platform != "nt"))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_cases(path: Path) -> list[dict]:
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
            normalized.setdefault("checks", [])
            cases.append(normalized)
    out = []
    for i, case in enumerate(cases):
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            label = mode[:-1] if mode.endswith("s") else mode
            raise ValueError(f"{path}: {label} #{i} needs id and prompt")
        normalized = dict(case)
        raw_checks = normalized.get("checks", [])
        if raw_checks is None:
            raw_checks = []
        if not isinstance(raw_checks, list):
            raise ValueError(f"{path}: case {case['id']} checks must be an array")
        normalized["checks"] = raw_checks
        out.append(normalized)
    return out




_SCORING_ONLY_KEYS = {
    "checks", "expected", "expect", "expected_answer", "reference_answer",
    "oracle", "rubric", "judge_rubric",
}

def candidate_case_view(case: dict[str, Any]) -> dict[str, Any]:
    """Return the task payload visible to the candidate executor.

    Scoring rules and answer-oracle fields stay in the harness. This does not
    prevent a privileged local runner from independently reading the suite file,
    so production benchmarks should also isolate candidate filesystem access.
    """
    return {
        key: value
        for key, value in case.items()
        if key not in _SCORING_ONLY_KEYS
        and not key.startswith("expect_")
        and not key.startswith("expected_")
    }

def numeric_usage(result: dict, key: str):
    usage = result.get("usage")
    if isinstance(usage, dict):
        value = usage.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
    return None


def get_field(data: Any, field: str) -> Any:
    value = data
    for part in field.split("."):
        if isinstance(value, dict) and part in value:
            value = value[part]
        else:
            return None
    return value


def safe_workspace_path(workspace: Path | None, raw: str) -> Path:
    if workspace is None:
        raise ValueError("filesystem check requires --workspace")
    root = workspace.resolve()
    path = (root / raw).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"filesystem check escapes workspace: {raw}") from exc
    return path


def evaluate_check(check: dict[str, Any], candidate: dict[str, Any], workspace: Path | None) -> dict[str, Any]:
    kind = str(check.get("type", ""))
    field = str(check.get("field", "response"))
    expected = check.get("value")
    result: dict[str, Any] = {"type": kind, "field": field, "passed": False}
    try:
        if kind in {"field_equals", "exact"}:
            actual = get_field(candidate, field)
            result.update({"actual": actual, "expected": expected, "passed": actual == expected})
        elif kind == "contains":
            actual = get_field(candidate, field)
            passed = str(expected) in (actual if isinstance(actual, str) else json.dumps(actual, sort_keys=True))
            result.update({"expected": expected, "passed": passed})
        elif kind == "not_contains":
            actual = get_field(candidate, field)
            passed = str(expected) not in (actual if isinstance(actual, str) else json.dumps(actual, sort_keys=True))
            result.update({"expected": expected, "passed": passed})
        elif kind == "regex":
            actual = get_field(candidate, field)
            passed = bool(re.search(str(expected), actual if isinstance(actual, str) else json.dumps(actual, sort_keys=True)))
            result.update({"expected": expected, "passed": passed})
        elif kind == "file_exists":
            path = safe_workspace_path(workspace, str(check.get("path", "")))
            result.update({"path": str(path), "passed": path.is_file()})
        elif kind == "file_contains":
            path = safe_workspace_path(workspace, str(check.get("path", "")))
            needle = str(expected)
            passed = path.is_file() and needle in path.read_text(encoding="utf-8")
            result.update({"path": str(path), "expected": expected, "passed": passed})
        else:
            raise ValueError(f"unsupported deterministic check type: {kind}")
    except Exception as exc:
        result["error"] = f"{exc.__class__.__name__}: {exc}"
        result["passed"] = False
    return result


def run_json_command(command: list[str], payload: dict[str, Any], timeout: float) -> tuple[bool, dict[str, Any] | None, dict[str, Any]]:
    started = time.perf_counter()
    meta: dict[str, Any] = {"command": command}
    try:
        proc = subprocess.run(
            command,
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        meta["duration_seconds"] = time.perf_counter() - started
        meta["exit_code"] = proc.returncode
        meta["stderr"] = proc.stderr[-8000:]
        if proc.returncode != 0:
            meta["stdout"] = proc.stdout[-16000:]
            return False, None, meta
        try:
            parsed = json.loads(proc.stdout)
            if not isinstance(parsed, dict):
                raise ValueError("JSON output must be an object")
            return True, parsed, meta
        except Exception as exc:
            meta["protocol_error"] = str(exc)
            meta["stdout"] = proc.stdout[-16000:]
            return False, None, meta
    except subprocess.TimeoutExpired as exc:
        meta["duration_seconds"] = time.perf_counter() - started
        meta["exit_code"] = None
        meta["timeout"] = True
        meta["stdout"] = (exc.stdout or "")[-16000:] if isinstance(exc.stdout, str) else ""
        meta["stderr"] = (exc.stderr or "")[-8000:] if isinstance(exc.stderr, str) else ""
        return False, None, meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("suite", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--repetitions", type=int, default=1)
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--list", action="store_true", dest="list_only")
    ap.add_argument("--workspace", type=Path, help="trusted sandbox root for file_exists/file_contains checks")
    ap.add_argument("--judge-command", help="optional separate semantic judge command string")
    ap.add_argument("--runner", nargs=argparse.REMAINDER,
                    help="executor argv; receives JSON on stdin and returns candidate JSON on stdout")
    args = ap.parse_args()

    if args.repetitions < 1:
        ap.error("--repetitions must be >= 1")

    suite = args.suite.resolve()
    cases = load_cases(suite)
    if args.list_only:
        for case in cases:
            print(f"{case['id']}: {case['prompt']}")
        return 0
    if not args.runner:
        ap.error("--runner is required unless --list is used")

    judge_command = split_command(args.judge_command) if args.judge_command else None
    results: list[dict[str, Any]] = []
    for case in cases:
        for run_index in range(args.repetitions):
            payload = {
                "case": candidate_case_view(case),
                "run_index": run_index,
                "suite_id": suite.name,
            }
            ok, candidate, meta = run_json_command(args.runner, payload, args.timeout)
            record: dict[str, Any] = {
                "case_id": case["id"],
                "run_index": run_index,
                "started_at": utc_now(),
                "runner": args.runner,
                "runner_protocol_ok": ok,
                "duration_seconds": meta.get("duration_seconds"),
                "exit_code": meta.get("exit_code"),
                "stderr": meta.get("stderr", ""),
                "case_tags": case.get("tags", []),
                "critical": bool(case.get("critical", False)),
                "scored_passed": None,
                "score_source": "unscored",
            }
            for key in ("timeout", "protocol_error", "stdout"):
                if key in meta:
                    record[key] = meta[key]
            if ok and candidate is not None:
                record["candidate_result"] = candidate
                record["result"] = candidate  # v1 reader compatibility; never used as scoring authority here.
                record["candidate_reported_passed"] = candidate.get("passed") if isinstance(candidate.get("passed"), bool) else None
                check_results = [evaluate_check(check, candidate, args.workspace) for check in case.get("checks", [])]
                record["deterministic_checks"] = check_results
                check_errors = [item for item in check_results if item.get("error")]
                deterministic_passed = all(bool(item.get("passed")) for item in check_results) if check_results else None
                record["deterministic_passed"] = deterministic_passed
                record["check_error_count"] = len(check_errors)

                judge_passed = None
                if judge_command:
                    judge_payload = {
                        "case": case,
                        "run_index": run_index,
                        "suite": str(suite),
                        "candidate_result": candidate,
                        "deterministic_checks": check_results,
                    }
                    judge_ok, judge_result, judge_meta = run_json_command(judge_command, judge_payload, args.timeout)
                    record["judge_protocol_ok"] = judge_ok
                    record["judge_command"] = judge_command
                    record["judge_metadata"] = judge_meta
                    if judge_ok and judge_result is not None:
                        record["judge_result"] = judge_result
                        judge_passed = judge_result.get("passed") if isinstance(judge_result.get("passed"), bool) else None
                        if judge_passed is None:
                            record["judge_protocol_ok"] = False
                            record["judge_metadata"]["protocol_error"] = "judge JSON must contain passed: bool"
                    if not record.get("judge_protocol_ok"):
                        record["scored_passed"] = None
                        record["score_source"] = "judge_protocol_failure"
                    elif deterministic_passed is None:
                        record["scored_passed"] = judge_passed
                        record["score_source"] = "judge"
                    else:
                        record["scored_passed"] = bool(deterministic_passed and judge_passed)
                        record["score_source"] = "deterministic+judge"
                elif deterministic_passed is not None:
                    record["scored_passed"] = deterministic_passed
                    record["score_source"] = "deterministic"
            results.append(record)
            print(f"{case['id']} run={run_index} protocol_ok={record.get('runner_protocol_ok')} score={record.get('scored_passed')} source={record.get('score_source')}")

    scored = [r["scored_passed"] for r in results if isinstance(r.get("scored_passed"), bool)]
    candidate_reported = [r["candidate_reported_passed"] for r in results if isinstance(r.get("candidate_reported_passed"), bool)]
    durations = [r["duration_seconds"] for r in results if isinstance(r.get("duration_seconds"), (int, float))]
    in_tokens: list[float] = []
    out_tokens: list[float] = []
    costs: list[float] = []
    for r in results:
        candidate = r.get("candidate_result")
        if isinstance(candidate, dict):
            for key, bucket in (("input_tokens", in_tokens), ("output_tokens", out_tokens), ("cost", costs)):
                value = numeric_usage(candidate, key)
                if value is not None:
                    bucket.append(float(value))

    summary = {
        "runs": len(results),
        "scored_runs": len(scored),
        "unscored_runs": len(results) - len(scored),
        "protocol_failures": sum(not bool(r.get("runner_protocol_ok")) for r in results),
        "judge_protocol_failures": sum(r.get("judge_protocol_ok") is False for r in results),
        "deterministic_check_errors": sum(int(r.get("check_error_count", 0)) for r in results),
        "pass_rate": (sum(scored) / len(scored)) if scored else None,
        "candidate_reported_pass_rate": (sum(candidate_reported) / len(candidate_reported)) if candidate_reported else None,
        "duration_mean_seconds": statistics.fmean(durations) if durations else None,
        "input_tokens_mean": statistics.fmean(in_tokens) if in_tokens else None,
        "output_tokens_mean": statistics.fmean(out_tokens) if out_tokens else None,
        "cost_mean": statistics.fmean(costs) if costs else None,
    }
    output = {
        "schema_version": 2,
        "created_at": utc_now(),
        "suite": str(suite),
        "repetitions": args.repetitions,
        "runner": args.runner,
        "judge_command": judge_command,
        "workspace": str(args.workspace.resolve()) if args.workspace else None,
        "summary": summary,
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    harness_failures = summary["protocol_failures"] + summary["judge_protocol_failures"] + summary["deterministic_check_errors"]
    return 0 if harness_failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
