#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

DATE_RE = re.compile(r"(?:Verification date|Verified|INSPECTED):\s*\*\*?(\d{4}-\d{2}-\d{2})", re.I)
URL_RE = re.compile(r"https?://[^\s)\]>]+")


def days_old(value: str) -> int:
    d = datetime.strptime(value, "%Y-%m-%d").date()
    return (date.today() - d).days


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--max-age-days", type=int, default=90)
    ap.add_argument("--network", action="store_true", help="also probe unique HTTP URLs")
    ap.add_argument("--max-urls", type=int, default=40)
    args = ap.parse_args()
    root = args.root.resolve()
    stale = []
    urls = []
    for p in sorted(root.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in DATE_RE.finditer(text):
            age = days_old(m.group(1))
            if age > args.max_age_days:
                stale.append((p.relative_to(root).as_posix(), m.group(1), age))
        if args.network:
            urls.extend(URL_RE.findall(text))
    print(f"Freshness dates older than {args.max_age_days} days: {len(stale)}")
    for rel, value, age in stale:
        print(f"REVERIFY {rel}: {value} ({age} days)")

    failures = 0
    if args.network:
        seen = []
        for u in urls:
            u = u.rstrip(".,;:'\"")
            if u not in seen:
                seen.append(u)
        for u in seen[: args.max_urls]:
            req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "SKick-Freshness-Audit/1"})
            try:
                with urllib.request.urlopen(req, timeout=10) as r:
                    print(f"FRESH {r.status} {u}")
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
                failures += 1
                print(f"CHECK {u}: {exc}")
    return 2 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
