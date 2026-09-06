#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))
from runtime.versioning import normalize_semver

NAME = "skick"
EXPECTED = {
    "runtime-skill.zip": [f"{NAME}/SKILL.md", f"{NAME}/core/research-core.md", f"{NAME}/START_HERE.md"],
    "agent-plugin-v1.zip": ["plugin.json", f"skills/{NAME}/SKILL.md", f"skills/{NAME}/core/research-core.md"],
    "codex-plugin.zip": [".codex-plugin/plugin.json", f"skills/{NAME}/SKILL.md", f"skills/{NAME}/core/research-core.md"],
    "claude-code-plugin.zip": [".claude-plugin/plugin.json", f"skills/{NAME}/SKILL.md", f"skills/{NAME}/core/research-core.md"],
    "claude-web-skill.zip": [f"{NAME}/skill.md", f"{NAME}/core/research-core.md", f"{NAME}/START_HERE.md"],
    "gemini-apps-skill.zip": ["SKILL.md", "START_HERE.md", "core/research-core.md", "adapters/gemini-apps/README.md"],
    "kimi-plugin.zip": ["kimi.plugin.json", f"skills/{NAME}/SKILL.md", f"skills/{NAME}/core/research-core.md"],
    "zcode-plugin.zip": [".zcode-plugin/plugin.json", f"skills/{NAME}/SKILL.md", f"skills/{NAME}/core/research-core.md"],
    "shared-agent-skill.zip": [f".agents/skills/{NAME}/SKILL.md", f".agents/skills/{NAME}/core/research-core.md"],
}
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip", ".docx", ".pptx", ".xlsx"}


def read_json_from_zip(path: Path, member: str):
    with zipfile.ZipFile(path) as zf:
        return json.loads(zf.read(member).decode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate generated SKick distributions")
    ap.add_argument("output_dir", type=Path)
    args = ap.parse_args()
    root = args.output_dir.resolve()
    errors: list[str] = []
    package_version = None
    runtime_zip = root / "runtime-skill.zip"
    if runtime_zip.is_file():
        try:
            with zipfile.ZipFile(runtime_zip) as zf:
                package_version = zf.read(f"{NAME}/VERSION").decode("utf-8").strip()
        except Exception as exc:
            errors.append(f"could not derive package version from runtime-skill.zip: {exc}")
    expected_plugin_version = normalize_semver(package_version) if package_version else None

    for filename, required in EXPECTED.items():
        p = root / filename
        if not p.is_file():
            errors.append(f"missing distribution: {filename}")
            continue
        try:
            with zipfile.ZipFile(p) as zf:
                bad = zf.testzip()
                names = set(zf.namelist())
                if bad:
                    errors.append(f"corrupt member in {filename}: {bad}")
                for member in required:
                    if member not in names:
                        errors.append(f"{filename} missing {member}")
                for member in names:
                    if member.startswith(".git/") or "/.git/" in member or "assets/readme/" in member:
                        errors.append(f"{filename} contains repo-only/runtime-bloat member: {member}")
        except zipfile.BadZipFile:
            errors.append(f"bad zip: {filename}")

    p = root / "agent-plugin-v1.zip"
    if p.is_file():
        m = read_json_from_zip(p, "plugin.json")
        allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
        if m.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("Agent Plugin v1 schema identifier mismatch")
        if m.get("name") != NAME or m.get("version") != expected_plugin_version:
            errors.append("Agent Plugin identity/version mismatch")
        unknown = set(m) - allowed
        if unknown:
            errors.append(f"Agent Plugin v1 has non-standard top-level fields: {sorted(unknown)}")

    p = root / "codex-plugin.zip"
    if p.is_file():
        m = read_json_from_zip(p, ".codex-plugin/plugin.json")
        if m.get("skills") != "./skills/" or m.get("version") != expected_plugin_version:
            errors.append("Codex plugin skills/version mismatch")

    p = root / "kimi-plugin.zip"
    if p.is_file():
        m = read_json_from_zip(p, "kimi.plugin.json")
        if m.get("skills") != "./skills/" or m.get("version") != expected_plugin_version:
            errors.append("Kimi plugin skills/version mismatch")

    p = root / "claude-web-skill.zip"
    if p.is_file():
        with zipfile.ZipFile(p) as zf:
            names = set(zf.namelist())
            if f"{NAME}/SKILL.md" in names:
                errors.append("Claude web archive must use lowercase skill.md, not SKILL.md")
            if not all(name.startswith(f"{NAME}/") for name in names if name):
                errors.append("Claude web archive must contain one top-level skill folder")

    p = root / "gemini-apps-skill.zip"
    if p.is_file():
        with zipfile.ZipFile(p) as zf:
            names = set(zf.namelist())
            if "SKILL.md" not in names:
                errors.append("Gemini Apps archive must place SKILL.md at ZIP root")
            binary = sorted(name for name in names if Path(name).suffix.lower() in BINARY_SUFFIXES)
            if binary:
                errors.append(f"Gemini Apps archive contains unsupported binary/rich files: {binary[:8]}")
            if any(name.startswith("skick/") for name in names):
                errors.append("Gemini Apps archive must not wrap SKILL.md inside a skick/ directory")

    forbidden_outputs = ["antigravity-plugin.zip"]
    for name in forbidden_outputs:
        if (root / name).exists():
            errors.append(f"unverified distribution should not be generated: {name}")

    if not (root / "generic-prompt.md").is_file():
        errors.append("missing generic-prompt.md")
    if not (root / "INSTALL.md").is_file():
        errors.append("missing INSTALL.md")

    if errors:
        print("DISTRIBUTION VALIDATION: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1
    print("DISTRIBUTION VALIDATION: PASS")
    for filename in sorted(EXPECTED):
        p = root / filename
        print(f"- {filename}: {p.stat().st_size:,} bytes")
    print(f"- generic-prompt.md: {(root / 'generic-prompt.md').stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
