#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXCLUDE = {"ARTIFACT_MANIFEST.json", "SHA256SUMS.txt"}
SKIP_PARTS = {".git", "__pycache__", "dist", "release-artifacts", "releases"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_paths(root: Path) -> set[str]:
    result: set[str] = set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_PARTS for part in rel.parts) or rel.as_posix() in EXCLUDE:
            continue
        result.add(rel.as_posix())
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    manifest_path = root / "ARTIFACT_MANIFEST.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    items = data.get("artifacts", [])
    listed: set[str] = set()
    for item in items:
        rel = item.get("path")
        if not isinstance(rel, str):
            errors.append("artifact entry missing path")
            continue
        listed.add(rel)
        p = root / rel
        if not p.is_file():
            errors.append(f"missing: {rel}")
            continue
        actual = digest(p)
        if actual != item.get("sha256"):
            errors.append(f"digest mismatch: {rel}")
        if p.stat().st_size != item.get("size"):
            errors.append(f"size mismatch: {rel}")
    actual_paths = canonical_paths(root)
    for rel in sorted(actual_paths - listed):
        errors.append(f"unlisted canonical file: {rel}")
    for rel in sorted(listed - actual_paths):
        errors.append(f"manifest lists non-canonical/absent file: {rel}")
    if errors:
        print("PROVENANCE VERIFY: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"PROVENANCE VERIFY: PASS ({len(items)} files, complete coverage)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
