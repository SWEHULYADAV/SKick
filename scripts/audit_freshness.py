#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

DATE_RE = re.compile(r"(?:Verification date|Verified|INSPECTED):\s*\*\*?(\d{4}-\d{2}-\d{2})", re.I)
URL_RE = re.compile(r"https?://[^\s)\]>]+")


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def days_old(value: str, as_of: date | None = None) -> int:
    return ((as_of or date.today()) - parse_date(value)).days


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--max-age-days", type=int, default=90)
    ap.add_argument("--as-of", help="deterministic ISO date for CI/tests")
    ap.add_argument("--fail-stale", action="store_true", help="return 1 when dated evidence exceeds the age budget")
    ap.add_argument("--network", action="store_true", help="also probe unique HTTP URLs; never enabled implicitly")
    ap.add_argument("--max-urls", type=int, default=40)
    args = ap.parse_args()
    root = args.root.resolve()
    as_of = parse_date(args.as_of) if args.as_of else date.today()
    stale_docs: list[tuple[str, str, int]] = []
    stale_routes: list[tuple[str, str, int]] = []
    urls: list[str] = []

    for p in sorted(root.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in DATE_RE.finditer(text):
            age = days_old(m.group(1), as_of)
            if age > args.max_age_days:
                stale_docs.append((p.relative_to(root).as_posix(), m.group(1), age))
        if args.network:
            urls.extend(URL_RE.findall(text))

    manifest_path = root / "INSTALLATION_MANIFEST.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"INVALID INSTALLATION_MANIFEST.json: {exc}")
            return 1
        for pid, entry in sorted((manifest.get("platforms") or {}).items()):
            value = entry.get("last_verified") if isinstance(entry, dict) else None
            try:
                age = days_old(value, as_of)
            except Exception:
                print(f"STALE_ROUTE {pid}: invalid last_verified {value!r}")
                stale_routes.append((pid, str(value), 10**9))
                continue
            if age > args.max_age_days:
                stale_routes.append((pid, value, age))
            if args.network and isinstance(entry, dict):
                for ev in entry.get("official_evidence") or []:
                    if isinstance(ev, dict) and isinstance(ev.get("url"), str):
                        urls.append(ev["url"])

    print(f"Freshness dates older than {args.max_age_days} days: {len(stale_docs)}")
    for rel, value, age in stale_docs:
        print(f"REVERIFY {rel}: {value} ({age} days)")
    print(f"Platform routes older than {args.max_age_days} days: {len(stale_routes)}")
    for pid, value, age in stale_routes:
        print(f"STALE_ROUTE {pid}: {value} ({age} days)")

    network_failures = 0
    if args.network:
        seen: list[str] = []
        for u in urls:
            u = u.rstrip(".,;:'\"")
            if u and u not in seen:
                seen.append(u)
        for u in seen[: args.max_urls]:
            req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "SKick-Freshness-Audit/2"})
            try:
                with urllib.request.urlopen(req, timeout=10) as r:
                    print(f"FRESH {r.status} {u}")
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
                network_failures += 1
                print(f"CHECK {u}: {exc}")

    if network_failures:
        return 2
    if args.fail_stale and (stale_docs or stale_routes):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
