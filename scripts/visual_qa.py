#!/usr/bin/env python3
"""Static anti-slop preflight for web source. Not a rendered visual judge."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PATTERNS = {
    "gradients": re.compile(r"(?:linear|radial|conic)-gradient\s*\(", re.I),
    "backdrop_blur": re.compile(r"backdrop-filter\s*:\s*[^;]*blur|backdrop-blur", re.I),
    "large_radius": re.compile(r"border-radius\s*:\s*(?:1\.5|2|2\.5|3|4|5|6|[3-9]\d)\s*(?:rem|px)|rounded-(?:2xl|3xl|full)", re.I),
    "box_shadow": re.compile(r"box-shadow\s*:|shadow-(?:xl|2xl)", re.I),
    "purple_blue": re.compile(r"(?:purple|violet|indigo|fuchsia).{0,80}(?:blue|cyan)|(?:blue|cyan).{0,80}(?:purple|violet|indigo|fuchsia)", re.I | re.S),
    "center_everything": re.compile(r"text-align\s*:\s*center|text-center", re.I),
    "generic_copy": re.compile(r"transform your|revolutioni[sz]e|unlock (?:the )?power|supercharge|seamless(?:ly)?|next[- ]generation", re.I),
}

TEXT_EXT = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = args.path.resolve()
    files = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_EXT]
    counts = {k: 0 for k in PATTERNS}
    scanned = 0
    for p in files:
        if p.suffix.lower() not in TEXT_EXT:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        scanned += 1
        for name, rx in PATTERNS.items():
            counts[name] += len(rx.findall(text))
    signals = sum(1 for v in counts.values() if v > 0)
    intensity = sum(min(v, 12) for v in counts.values())
    risk = "LOW" if signals <= 2 and intensity < 10 else "MEDIUM" if signals <= 4 and intensity < 30 else "HIGH"
    result = {
        "files_scanned": scanned,
        "signals": counts,
        "static_slop_risk": risk,
        "note": "Heuristic source preflight only; rendered screenshot/interaction review is required for a strong design conclusion."
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Static slop risk: {risk}")
        for k, v in counts.items():
            print(f"- {k}: {v}")
        print(result["note"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
