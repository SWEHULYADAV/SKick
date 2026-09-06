#!/usr/bin/env python3
"""Generate/check the exact canonical SKick package file list.

This replaces the manually maintained tests/package-manifest.txt workflow that
allowed files to enter source after the manifest was generated.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {'.git', '__pycache__'}
MANIFEST = 'tests/package-manifest.txt'


def canonical_paths(root: Path) -> list[str]:
    paths: list[str] = []
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        name = rel.as_posix()
        if name == MANIFEST:
            continue
        paths.append(name)
    return sorted(paths)


def render(root: Path) -> str:
    return ''.join(f'{path}\n' for path in canonical_paths(root))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    root = args.root.resolve()
    target = root / MANIFEST
    expected = render(root)
    if args.check:
        if not target.is_file() or target.read_text(encoding='utf-8') != expected:
            print('package manifest is stale')
            return 1
        print(f'package manifest in sync ({len(canonical_paths(root))} files)')
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(expected, encoding='utf-8')
    print(f'generated {MANIFEST} ({len(canonical_paths(root))} files)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
