#!/usr/bin/env python3
"""Build SKick runtime-specific distributions from canonical source.

Generated distributions are release artifacts, not maintenance source. The
builder intentionally excludes repository-only files and large README artwork
from runtime wrappers. Gemini Apps receives a text-only archive because its
Skills upload surface does not accept binary/rich-media files.
"""
from __future__ import annotations

import argparse
import json
import shutil
import zipfile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from runtime.versioning import normalize_semver, read_package_version

NAME = "skick"

REPO_ONLY_DIRS = {".git", ".github", "dist", "release-artifacts", "__pycache__"}
REPO_ONLY_FILES = {".DS_Store"}
RUNTIME_EXCLUDE_PREFIXES = {"assets/readme/"}
TEXT_ONLY_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".csv",
    ".toml", ".xml", ".html", ".css", ".js", ".ts", ".ini", ".cfg",
}
TEXT_ONLY_NAMES = {"VERSION", "Dockerfile", "Makefile"}


def is_repo_only(rel: Path) -> bool:
    if any(part in REPO_ONLY_DIRS for part in rel.parts):
        return True
    if rel.name in REPO_ONLY_FILES:
        return True
    return False


def is_runtime_file(rel: Path) -> bool:
    if is_repo_only(rel):
        return False
    text = rel.as_posix()
    return not any(text.startswith(prefix) for prefix in RUNTIME_EXCLUDE_PREFIXES)


def is_text_only(rel: Path) -> bool:
    if not is_runtime_file(rel):
        return False
    if rel.name in TEXT_ONLY_NAMES:
        return True
    return rel.suffix.lower() in TEXT_ONLY_SUFFIXES


def copy_filtered(src: Path, dst: Path, predicate=is_runtime_file) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)
    for p in sorted(src.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(src)
        if not predicate(rel):
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def zip_dir(src: Path, out: Path, include_root: bool = False) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                arc = p.relative_to(src.parent if include_root else src)
                zf.write(p, arc.as_posix())


def build(root: Path, out: Path) -> None:
    package_version = read_package_version(root)
    label = f"v{package_version}"
    plugin_version = normalize_semver(package_version)
    desc = f"SKick v{package_version}: universal engineering, evidence-driven research, verification, and delivery workflows."
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    stage = out / "_stage"
    stage.mkdir()

    # Portable runtime Skill folder. The archive has a single top-level skick/ directory.
    runtime_skill = stage / "runtime-skill"
    copy_filtered(root, runtime_skill / NAME)
    zip_dir(runtime_skill, out / "runtime-skill.zip")

    # Shared Agent Skills layout used by runtimes that explicitly support .agents/skills.
    shared_root = stage / "shared-agent-skill"
    copy_filtered(root, shared_root / ".agents" / "skills" / NAME)
    zip_dir(shared_root, out / "shared-agent-skill.zip")

    # Agent Plugins v1 portable wrapper. Skills use the standard fixed skills/<name>/ path.
    agent_plugin = stage / "agent-plugin-v1"
    copy_filtered(root, agent_plugin / "skills" / NAME)
    write_json(agent_plugin / "plugin.json", {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": NAME,
        "version": plugin_version,
        "description": desc,
        "repository": "https://github.com/SWEHULYADAV/SKick",
        "keywords": ["engineering", "research", "security", "agent-skills"],
    })
    zip_dir(agent_plugin, out / "agent-plugin-v1.zip")

    # OpenAI Codex plugin wrapper.
    codex = stage / "codex-plugin"
    copy_filtered(root, codex / "skills" / NAME)
    write_json(codex / ".codex-plugin" / "plugin.json", {
        "name": NAME,
        "version": plugin_version,
        "description": desc,
        "repository": "https://github.com/SWEHULYADAV/SKick",
        "keywords": ["engineering", "research", "security"],
        "skills": "./skills/",
    })
    zip_dir(codex, out / "codex-plugin.zip")

    # Claude Code plugin wrapper.
    claude = stage / "claude-code-plugin"
    copy_filtered(root, claude / "skills" / NAME)
    write_json(claude / ".claude-plugin" / "plugin.json", {
        "name": NAME,
        "version": plugin_version,
        "description": desc,
    })
    zip_dir(claude, out / "claude-code-plugin.zip")

    # Kimi Code plugin wrapper.
    kimi = stage / "kimi-plugin"
    copy_filtered(root, kimi / "skills" / NAME)
    write_json(kimi / "kimi.plugin.json", {
        "name": NAME,
        "version": plugin_version,
        "description": desc,
        "skills": "./skills/",
    })
    zip_dir(kimi, out / "kimi-plugin.zip")

    # ZCode plugin wrapper.
    zcode = stage / "zcode-plugin"
    copy_filtered(root, zcode / "skills" / NAME)
    write_json(zcode / ".zcode-plugin" / "plugin.json", {
        "name": NAME,
        "version": plugin_version,
        "description": desc,
    })
    zip_dir(zcode, out / "zcode-plugin.zip")

    # Claude web/app custom Skills: top-level skill folder and lowercase skill.md.
    claude_web = stage / "claude-web"
    claude_skill = claude_web / NAME
    copy_filtered(root, claude_skill)
    skill_upper = claude_skill / "SKILL.md"
    if not skill_upper.is_file():
        raise RuntimeError("Canonical SKILL.md missing while building Claude web package")
    skill_upper.rename(claude_skill / "skill.md")
    zip_dir(claude_web, out / "claude-web-skill.zip")

    # Gemini Apps: SKILL.md at archive root and text-only supporting files.
    gemini = stage / "gemini-apps"
    copy_filtered(root, gemini, predicate=is_text_only)
    # README contains image references that are intentionally excluded; use a compact runtime README instead.
    (gemini / "README.md").write_text(
        "# SKick for Gemini Apps\n\n"
        "This generated distribution is text-only for Gemini Apps compatibility. "
        "The canonical GitHub repository contains PNG branding and README artwork; those binary files are intentionally excluded here. "
        "Start with `SKILL.md`, `START_HERE.md`, and `adapters/gemini-apps/README.md`.\n",
        encoding="utf-8",
    )
    zip_dir(gemini, out / "gemini-apps-skill.zip")

    # Generic fallback for model-only or unsupported host surfaces.
    shutil.copy2(root / "adapters" / "generic" / "PROMPT.md", out / "generic-prompt.md")

    install = f"""# SKick {label} portable distributions

These files are generated from canonical source. Do not hand-edit generated ZIPs.

- `skill.zip` is produced separately by the official Skill packager/release builder.
- `runtime-skill.zip` - portable archive containing one top-level `{NAME}/` Skill directory.
- `shared-agent-skill.zip` - `.agents/skills/{NAME}/` layout for hosts that explicitly support Agent Skills.
- `agent-plugin-v1.zip` - portable Agent Plugins v1 package.
- `codex-plugin.zip` - OpenAI Codex `.codex-plugin` wrapper.
- `claude-code-plugin.zip` - Claude Code `.claude-plugin` wrapper.
- `claude-web-skill.zip` - Claude web/app upload shape with top-level `{NAME}/skill.md`.
- `gemini-apps-skill.zip` - Gemini Apps text-only shape with `SKILL.md` at archive root.
- `kimi-plugin.zip` - Kimi Code plugin wrapper.
- `zcode-plugin.zip` - ZCode plugin wrapper.
- `generic-prompt.md` - fallback when no verified native Skill importer exists.

Antigravity is intentionally not given a fabricated plugin manifest. For Antigravity Agent/IDE use the documented Agent Skill paths (or `shared-agent-skill.zip`); Antigravity CLI has a distinct flat-file Skill model and should use the adapter instructions/fallback rather than this full directory package unless the runtime documents compatible directory Skills.

Structural validation proves package shape and archive integrity only. It does not prove live installation in every external product.
"""
    (out / "INSTALL.md").write_text(install, encoding="utf-8")
    shutil.rmtree(stage)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build SKick portable runtime distributions")
    ap.add_argument("skill_root", type=Path)
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()
    build(args.skill_root.resolve(), args.output_dir.resolve())
    print(f"Built distributions in {args.output_dir.resolve()}")
