#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    manifest_path = root / "ARTIFACT_MANIFEST.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []
    for item in data.get("artifacts", []):
        p = root / item["path"]
        if not p.is_file():
            errors.append(f"missing: {item['path']}")
            continue
        actual = digest(p)
        if actual != item.get("sha256"):
            errors.append(f"digest mismatch: {item['path']}")
        if p.stat().st_size != item.get("size"):
            errors.append(f"size mismatch: {item['path']}")
    if errors:
        print("PROVENANCE VERIFY: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"PROVENANCE VERIFY: PASS ({len(data.get('artifacts', []))} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
