#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

EXCLUDE = {"ARTIFACT_MANIFEST.json", "SHA256SUMS.txt"}
SKIP_PARTS = {".git", "__pycache__", "dist", "release-artifacts", "releases"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--release", default=None)
    args = ap.parse_args()
    root = args.root.resolve()
    release = args.release or ((root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").is_file() else "unknown")

    artifacts = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or any(part in SKIP_PARTS for part in p.parts) or p.name in EXCLUDE:
            continue
        rel = p.relative_to(root).as_posix()
        artifacts.append({"path": rel, "sha256": digest(p), "size": p.stat().st_size})

    manifest = {
        "schema_version": 1,
        "release": release,
        "generated_at": utc_now(),
        "builder": {"tool": "scripts/build_provenance.py", "python": platform.python_version(), "platform": platform.platform()},
        "inputs": [],
        "artifacts": artifacts,
    }
    (root / "ARTIFACT_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (root / "SHA256SUMS.txt").write_text("".join(f"{a['sha256']}  {a['path']}\n" for a in artifacts), encoding="utf-8")
    print(f"Wrote provenance for {len(artifacts)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
