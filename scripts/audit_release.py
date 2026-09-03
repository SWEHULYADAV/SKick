#!/usr/bin/env python3
"""Release-grade structural audit for the SKick repository.

This audit intentionally separates structural checks from live runtime tests.
It verifies repository consistency, packaging hygiene, adapters, links, branding,
JSON, Python syntax, and stale branding. It does not claim external products
actually executed SKick.
"""
from __future__ import annotations

import json
import py_compile
import re
import sys
import struct
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STALE_PATTERNS = [r"\b" + "Sp" + "ecs" + r"\b", r"\b" + "Side" + "kick" + r"\b", "Universal Engineering " + "Research Agent", r"\b" + "U" + "RA" + r"\b"]
SKIP_DIRS = {".git", "dist", "releases", "release-artifacts", "__pycache__"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def text_files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        if p.suffix.lower() in {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".toml", ".sh"} or p.name in {"VERSION"}:
            yield p


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # Identity and stale-brand checks.
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = FRONT_RE.match(skill)
    if not m:
        fail(errors, "SKILL.md frontmatter missing")
    else:
        front = m.group(1)
        if not re.search(r"(?m)^name:\s*skick\s*$", front):
            fail(errors, "SKILL.md name must be skick")
        dm = re.search(r"(?m)^description:\s*(.+)$", front)
        if not dm or not dm.group(1).strip():
            fail(errors, "SKILL.md description missing")
        elif len(dm.group(1).strip()) > 1024:
            fail(errors, "SKILL.md description exceeds 1024 characters")
    if len(skill.splitlines()) > 500:
        fail(errors, f"SKILL.md has {len(skill.splitlines())} lines; keep under 500")

    for p in text_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(ROOT).as_posix()
        for pat in STALE_PATTERNS:
            if re.search(pat, text):
                fail(errors, f"stale branding/reference in {rel}: /{pat}/")

    # README images and local links.
    readme = ROOT / "README.md"
    if not readme.is_file():
        fail(errors, "README.md missing")
    else:
        rt = readme.read_text(encoding="utf-8")
        for expected in [
            "assets/readme/hero-banner.webp", "assets/readme/capabilities-banner.webp",
            "assets/readme/usage-guide.webp", "assets/readme/platforms-banner.webp",
        ]:
            if expected not in rt:
                fail(errors, f"README missing image reference: {expected}")
            if not (ROOT / expected).is_file():
                fail(errors, f"README image missing on disk: {expected}")
        if "https://github.com/SWEHULYADAV/SKick" not in rt:
            fail(errors, "README missing canonical GitHub repository URL")

    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (p.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"link escapes repository: {p.relative_to(ROOT)} -> {raw}")
                continue
            if not resolved.exists():
                fail(errors, f"broken local link: {p.relative_to(ROOT)} -> {raw}")

    # Branding dimensions. Parse the PNG IHDR directly so release validation
    # has no third-party Python dependency or network-install step.
    def png_dimensions(path: Path) -> tuple[int, int]:
        data = path.read_bytes()[:24]
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            raise ValueError("not a valid PNG with IHDR")
        return struct.unpack(">II", data[16:24])

    expected_dims = {
        "assets/icon.png": (512, 512),
        "assets/favicon.png": (64, 64),
        "assets/favicon-32.png": (32, 32),
    }
    for rel, dims in expected_dims.items():
        p = ROOT / rel
        if not p.is_file():
            fail(errors, f"missing branding asset {rel}")
            continue
        try:
            actual = png_dimensions(p)
        except Exception as exc:
            fail(errors, f"invalid PNG {rel}: {exc}")
            continue
        if actual != dims:
            fail(errors, f"{rel} must be {dims}, got {actual}")
    logo = ROOT / "assets/logo.png"
    if not logo.is_file():
        fail(errors, "assets/logo.png missing")
    else:
        try:
            width, height = png_dimensions(logo)
            if width < 512 or height < 256:
                fail(errors, f"assets/logo.png unexpectedly small: {(width, height)}")
        except Exception as exc:
            fail(errors, f"invalid PNG assets/logo.png: {exc}")

    # JSON syntax.
    for p in ROOT.rglob("*.json"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(errors, f"invalid JSON {p.relative_to(ROOT)}: {exc}")

    # Python syntax.
    for p in ROOT.rglob("*.py"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        try:
            compile(p.read_text(encoding="utf-8"), str(p), "exec")
        except Exception as exc:
            fail(errors, f"python syntax failure {p.relative_to(ROOT)}: {exc}")

    # Installation manifest consistency.
    manifest = json.loads((ROOT / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("package", {}).get("name") != "skick":
        fail(errors, "manifest package name must be skick")
    platforms = manifest.get("platforms", {})
    if len(platforms) < 40:
        fail(errors, f"platform manifest unexpectedly narrow: {len(platforms)} entries")
    required_platforms = {
        "chatgpt", "codex", "claude-code", "gemini-cli", "cursor", "github-copilot",
        "opencode", "browsercode", "qwen", "kimi", "mimo", "minimax", "longcat",
        "cline", "roo-code", "windsurf", "trae", "bytedance-models", "continue", "goose", "kiro-cli",
        "junie", "openhands", "replit", "warp", "devin", "amp", "augment", "kilo-code",
    }
    missing = sorted(required_platforms - set(platforms))
    if missing:
        fail(errors, f"required platform routes missing: {missing}")
    for pid, item in platforms.items():
        adapter = item.get("adapter")
        if not adapter or not (ROOT / adapter).is_file():
            fail(errors, f"platform {pid} adapter missing: {adapter}")
        if not item.get("verification"):
            fail(errors, f"platform {pid} has no verification steps")
        if item.get("kind") != "model_provider_only" and not item.get("source") and not item.get("sources"):
            warnings.append(f"platform {pid} has no source URL")

    # Direct-ZIP bootstrap requirements.
    start = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
    for marker in ["INSTALLATION_MANIFEST.json", "RUNTIME_COMPATIBILITY.md", "NEW_RUNTIME_INTEGRATION.md", "install this"]:
        if marker.lower() not in start.lower():
            fail(errors, f"START_HERE.md missing bootstrap marker: {marker}")

    # Repository hygiene.
    for forbidden in [ROOT / "dist", ROOT / "releases", ROOT / "release-artifacts"]:
        if forbidden.exists():
            fail(errors, f"generated artifact directory must not live in canonical source during audit: {forbidden.name}/")
    if not (ROOT / ".github/workflows/validate.yml").is_file():
        fail(errors, "GitHub Actions validation workflow missing")
    if not (ROOT / "SECURITY.md").is_file():
        fail(errors, "SECURITY.md missing")
    if not (ROOT / "LICENSE").is_file():
        fail(errors, "LICENSE missing")
    for required in [
        "docs/INVOCATION_AND_MODES.md", "docs/RUNTIME_COMPATIBILITY.md",
        "docs/NEW_RUNTIME_INTEGRATION.md", "BOOTSTRAP_PROMPTS.md", "docs/GITHUB_BOOTSTRAP.md", "scripts/detect_runtime.py",
        "scripts/install_skick.py", "scripts/build_distributions.py", "scripts/build_github_bundle.py",
    ]:
        if not (ROOT / required).is_file():
            fail(errors, f"required release file missing: {required}")
    reviewed = manifest.get("last_reviewed")
    try:
        reviewed_date = date.fromisoformat(reviewed)
        age = (date.today() - reviewed_date).days
        if age < -1:
            warnings.append(f"installation manifest last_reviewed is unexpectedly in the future: {reviewed}")
        elif age > 45:
            warnings.append(f"installation manifest review is {age} days old: {reviewed}")
    except Exception:
        warnings.append(f"installation manifest last_reviewed is not a valid ISO date: {reviewed!r}")
    known_distributions = {
        "skill.zip", "runtime-skill.zip", "shared-agent-skill.zip", "agent-plugin-v1.zip",
        "codex-plugin.zip", "claude-code-plugin.zip", "claude-web-skill.zip",
        "gemini-apps-skill.zip", "kimi-plugin.zip", "zcode-plugin.zip", "generic-prompt.md",
    }
    for pid, item in platforms.items():
        dist = item.get("distribution")
        if dist and dist not in known_distributions:
            fail(errors, f"platform {pid} references unknown distribution: {dist}")

    # The portability suite must stay synchronized with generated release artifacts.
    portability = json.loads((ROOT / "evals/portability-evals.json").read_text(encoding="utf-8"))
    portability_paths = {c.get("path") for c in portability.get("checks", []) if isinstance(c, dict)}
    expected_portable = {
        "skill.zip", "runtime-skill.zip", "shared-agent-skill.zip", "agent-plugin-v1.zip",
        "codex-plugin.zip", "claude-code-plugin.zip", "claude-web-skill.zip",
        "gemini-apps-skill.zip", "kimi-plugin.zip", "zcode-plugin.zip",
    }
    missing_portability = sorted(expected_portable - portability_paths)
    if missing_portability:
        fail(errors, f"portability suite missing generated artifacts: {missing_portability}")
    if "antigravity-plugin.zip" in portability_paths:
        fail(errors, "portability suite must not expect the intentionally unverified antigravity-plugin.zip")

    print(f"SKICK RELEASE AUDIT: errors={len(errors)} warnings={len(warnings)} platforms={len(platforms)}")
    for w in warnings:
        print(f"- WARNING {w}")
    for e in errors:
        print(f"- ERROR {e}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
