#!/usr/bin/env python3
"""Build the unzip-and-commit SKick GitHub bundle.

The bundle contains canonical repository source under SKick/ plus generated
release artifacts under SKick/release-artifacts/. The repository .gitignore
excludes release-artifacts/ so a normal `git add .` commits canonical source
without accidentally versioning generated ZIPs.
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

SKIP_PARTS = {".git", "dist", "releases", "release-artifacts", "__pycache__"}
SKIP_NAMES = {".DS_Store"}


def copy_source(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for p in sorted(source.rglob("*")):
        rel = p.relative_to(source)
        if any(part in SKIP_PARTS for part in rel.parts) or p.name in SKIP_NAMES:
            continue
        if not p.is_file():
            continue
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def zip_tree(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(root.parent).as_posix())


def main() -> int:
    ap = argparse.ArgumentParser(description="Build SKick GitHub-ready source + release-artifact bundle")
    ap.add_argument("source_root", type=Path)
    ap.add_argument("skill_zip", type=Path)
    ap.add_argument("dist_dir", type=Path)
    ap.add_argument("output_zip", type=Path)
    args = ap.parse_args()

    source = args.source_root.resolve()
    skill_zip = args.skill_zip.resolve()
    dist = args.dist_dir.resolve()
    output = args.output_zip.resolve()

    for required in [source / "SKILL.md", source / "README.md", source / ".github/workflows/validate.yml"]:
        if not required.is_file():
            raise SystemExit(f"Missing canonical source file: {required}")
    if not skill_zip.is_file():
        raise SystemExit(f"Missing skill.zip: {skill_zip}")
    if not dist.is_dir():
        raise SystemExit(f"Missing distribution directory: {dist}")

    with tempfile.TemporaryDirectory(prefix="skick-github-bundle-") as td:
        stage_parent = Path(td)
        stage = stage_parent / "SKick"
        copy_source(source, stage)

        artifacts = stage / "release-artifacts"
        artifacts.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_zip, artifacts / "skill.zip")
        for p in sorted(dist.iterdir()):
            if p.is_file():
                shutil.copy2(p, artifacts / p.name)

        artifact_files = [p for p in sorted(artifacts.iterdir()) if p.is_file()]
        checksum_lines = [f"{sha256(p)}  {p.name}\n" for p in artifact_files]
        (artifacts / "SHA256SUMS.txt").write_text("".join(checksum_lines), encoding="utf-8")
        (artifacts / "README.md").write_text(
            "# Generated release artifacts\n\n"
            "These files are generated from the canonical SKick source in the parent repository. "
            "They are included in the downloadable GitHub-ready bundle for convenience, but "
            "`release-artifacts/` is git-ignored so generated ZIPs do not become maintenance source.\n\n"
            "- `skill.zip` — canonical Skill upload artifact.\n"
            "- `runtime-skill.zip` — one top-level `skick/` directory.\n"
            "- other archives — runtime-specific wrappers built by `scripts/build_distributions.py`.\n"
            "- `SHA256SUMS.txt` — checksums for the generated artifacts in this directory.\n",
            encoding="utf-8",
        )
        zip_tree(stage, output)

    print(f"Built GitHub-ready bundle: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
