#!/usr/bin/env python3
"""Build a compact universal SKick handoff ZIP for humans or AI installers.

The handoff archive is not itself an Agent Skill upload artifact. It contains the
canonical source plus selected prebuilt packages so an AI can choose the correct
runtime form after reading START_HERE.md.
"""
from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

SELECTED_PACKAGES = [
    "runtime-skill.zip",
    "shared-agent-skill.zip",
    "agent-plugin-v1.zip",
    "claude-web-skill.zip",
    "gemini-apps-skill.zip",
    "codex-plugin.zip",
    "claude-code-plugin.zip",
    "kimi-plugin.zip",
    "zcode-plugin.zip",
    "generic-prompt.md",
    "INSTALL.md",
]

ROOT_DOCS = [
    "START_HERE.md",
    "BOOTSTRAP_PROMPTS.md",
    "INSTALLATION_MANIFEST.json",
    "AI_HANDOFF.md",
    "AI_CONTEXT.json",
    "CONTRIBUTING.md",
    "README.md",
    "VERSION",
]


def zip_tree(src: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(src).as_posix())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_root", type=Path)
    ap.add_argument("dist_dir", type=Path)
    ap.add_argument("output_zip", type=Path)
    args = ap.parse_args()

    source = args.source_root.resolve()
    dist = args.dist_dir.resolve()
    out = args.output_zip.resolve()

    if not (source / "START_HERE.md").is_file() or not (source / "SKILL.md").is_file():
        raise SystemExit(f"Invalid SKick source root: {source}")
    if not dist.is_dir():
        raise SystemExit(f"Missing distribution directory: {dist}")

    with tempfile.TemporaryDirectory(prefix="skick-handoff-") as td:
        stage = Path(td) / "skick-v1.0-universal"
        stage.mkdir(parents=True)

        for rel in ROOT_DOCS:
            shutil.copy2(source / rel, stage / rel)

        source_dst = stage / "source" / "skick"
        shutil.copytree(source, source_dst, ignore=shutil.ignore_patterns("__pycache__", ".git", "dist", "release-artifacts", ".github"))

        packages = stage / "packages"
        packages.mkdir()
        missing = []
        for name in SELECTED_PACKAGES:
            src = dist / name
            if src.is_file():
                shutil.copy2(src, packages / name)
            else:
                missing.append(name)
        if missing:
            raise SystemExit("Missing expected distribution outputs: " + ", ".join(missing))

        (stage / "README_FIRST.md").write_text(
            "# SKick v1.0 Universal Handoff\n\n"
            "AI/agent: read `START_HERE.md` first. For a GitHub/URL-style handoff, also read `BOOTSTRAP_PROMPTS.md` and `source/skick/docs/GITHUB_BOOTSTRAP.md`. Use `INSTALLATION_MANIFEST.json` to identify the actual host runtime (not merely the model/provider) and select either the canonical source under `source/skick/` or the appropriate prebuilt package under `packages/`. Do not execute bundled scripts or install optional dependencies before reading the warnings and runtime adapter.\n",
            encoding="utf-8",
        )
        zip_tree(stage, out)

    print(f"Built universal handoff: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
