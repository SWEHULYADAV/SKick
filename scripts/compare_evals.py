#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def delta(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    return b - a


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("baseline", type=Path)
    ap.add_argument("candidate", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    base = load(args.baseline)
    cand = load(args.candidate)
    bs = base.get("summary", {})
    cs = cand.get("summary", {})
    keys = ["pass_rate", "duration_mean_seconds", "input_tokens_mean", "output_tokens_mean", "cost_mean", "protocol_failures"]
    comparison = {
        "schema_version": 1,
        "baseline": str(args.baseline),
        "candidate": str(args.candidate),
        "metrics": {k: {"baseline": bs.get(k), "candidate": cs.get(k), "delta": delta(bs.get(k), cs.get(k))} for k in keys},
    }
    text = json.dumps(comparison, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
