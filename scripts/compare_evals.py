#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def delta(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool) or not isinstance(b, (int, float)) or isinstance(b, bool):
        return None
    return b - a


def scored_pass(record: dict[str, Any]) -> tuple[bool | None, str]:
    value = record.get("scored_passed")
    if isinstance(value, bool):
        return value, "scored_passed"
    legacy = record.get("result")
    if isinstance(legacy, dict) and isinstance(legacy.get("passed"), bool):
        # v1 candidate self-reports are retained as historical raw data only.
        # They are never promoted into v1.1 scoring authority.
        return None, "legacy_candidate_report_ignored"
    return None, "unscored"


def wilson_interval(successes: int, n: int, z: float = 1.96) -> list[float] | None:
    if n < 20:
        return None
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt((p * (1 - p) / n) + (z * z / (4 * n * n))) / denom
    return [max(0.0, centre - half), min(1.0, centre + half)]


def task_summary(data: dict) -> dict[str, dict[str, Any]]:
    grouped: dict[str, list[tuple[bool, str]]] = defaultdict(list)
    for record in data.get("results", []):
        if not isinstance(record, dict) or not record.get("case_id"):
            continue
        value, source = scored_pass(record)
        if isinstance(value, bool):
            grouped[str(record["case_id"])].append((value, source))
    out: dict[str, dict[str, Any]] = {}
    for case_id, values in sorted(grouped.items()):
        passes = sum(value for value, _ in values)
        sources = sorted(set(source for _, source in values))
        out[case_id] = {
            "scored_runs": len(values),
            "passes": passes,
            "pass_rate": passes / len(values),
            "score_sources": sources,
            "pass_rate_ci95": wilson_interval(passes, len(values)),
        }
    return out


def overall_metric(data: dict, key: str):
    summary = data.get("summary", {})
    value = summary.get(key)
    if value is not None:
        return value
    if key == "pass_rate":
        scored = [scored_pass(r)[0] for r in data.get("results", []) if isinstance(r, dict)]
        scored = [v for v in scored if isinstance(v, bool)]
        return sum(scored) / len(scored) if scored else None
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline", type=Path)
    ap.add_argument("candidate", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    base = load(args.baseline)
    cand = load(args.candidate)
    keys = ["pass_rate", "duration_mean_seconds", "input_tokens_mean", "output_tokens_mean", "cost_mean", "protocol_failures"]
    metrics = {
        key: {
            "baseline": overall_metric(base, key),
            "candidate": overall_metric(cand, key),
            "delta": delta(overall_metric(base, key), overall_metric(cand, key)),
        }
        for key in keys
    }

    base_tasks = task_summary(base)
    cand_tasks = task_summary(cand)
    task_ids = sorted(set(base_tasks) | set(cand_tasks))
    tasks: dict[str, Any] = {}
    regressions: list[str] = []
    improvements: list[str] = []
    for case_id in task_ids:
        b = base_tasks.get(case_id)
        c = cand_tasks.get(case_id)
        b_rate = b.get("pass_rate") if b else None
        c_rate = c.get("pass_rate") if c else None
        d = delta(b_rate, c_rate)
        tasks[case_id] = {"baseline": b, "candidate": c, "pass_rate_delta": d}
        if isinstance(d, (int, float)):
            if d < 0:
                regressions.append(case_id)
            elif d > 0:
                improvements.append(case_id)

    base_by_pair = {}
    for record in base.get("results", []):
        if isinstance(record, dict):
            value, _ = scored_pass(record)
            if isinstance(value, bool):
                base_by_pair[(record.get("case_id"), record.get("run_index"))] = value
    cand_by_pair = {}
    for record in cand.get("results", []):
        if isinstance(record, dict):
            value, _ = scored_pass(record)
            if isinstance(value, bool):
                cand_by_pair[(record.get("case_id"), record.get("run_index"))] = value
    pairs = sorted(set(base_by_pair) & set(cand_by_pair), key=lambda x: (str(x[0]), int(x[1] or 0)))
    wins = losses = ties = 0
    differences: list[int] = []
    for pair in pairs:
        b = base_by_pair[pair]
        c = cand_by_pair[pair]
        diff = int(c) - int(b)
        differences.append(diff)
        if diff > 0:
            wins += 1
        elif diff < 0:
            losses += 1
        else:
            ties += 1
    success_delta = statistics.fmean(differences) if differences else None
    ci = None
    if len(differences) >= 20:
        if len(differences) == 1:
            ci = [success_delta, success_delta]
        else:
            sd = statistics.stdev(differences)
            half = 1.96 * sd / math.sqrt(len(differences))
            ci = [max(-1.0, success_delta - half), min(1.0, success_delta + half)]

    comparison = {
        "schema_version": 2,
        "baseline": str(args.baseline),
        "candidate": str(args.candidate),
        "metrics": metrics,
        "tasks": tasks,
        "paired": {
            "pairs": len(pairs),
            "wins": wins,
            "losses": losses,
            "ties": ties,
            "success_delta": success_delta,
            "success_delta_ci95": ci,
            "ci_method": "normal approximation on paired success differences; emitted only for n>=20" if ci is not None else None,
        },
        "regressions": regressions,
        "improvements": improvements,
    }
    text = json.dumps(comparison, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
