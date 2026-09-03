#!/usr/bin/env python3
"""Conservative filesystem installer for SKick Agent Skills.

The installer is manifest-driven and future-friendly. It installs only into
filesystem paths that the release manifest explicitly declares. Managed web
products remain UI-driven. Unknown runtimes can use --target agents when the
host documents the shared .agents/skills convention, or --destination for an
explicit user-approved skill root.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO_EXCLUDES = {".git", ".github", "dist", "releases", "release-artifacts", "__pycache__"}
FILE_EXCLUDES = {".DS_Store"}


def load_manifest(source: Path) -> dict:
    p = source / "INSTALLATION_MANIFEST.json"
    if not (source / "SKILL.md").is_file() or not p.is_file():
        raise SystemExit(f"Invalid SKick source: {source}")
    return json.loads(p.read_text(encoding="utf-8"))


def filesystem_targets(manifest: dict) -> dict[str, dict]:
    result = {}
    for pid, item in manifest.get("platforms", {}).items():
        if item.get("project_paths") or item.get("user_paths"):
            result[pid] = item
    result["agents"] = {
        "status": "SHARED_STANDARD_WHEN_SUPPORTED",
        "project_paths": [".agents/skills/skick/"],
        "user_paths": ["~/.agents/skills/skick/"],
        "preferred_install": "Shared Agent Skills root; use only when the active host documents/scans it.",
    }
    return result


def expand_path(raw: str, project: Path, scope: str) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(raw))
    p = Path(expanded)
    if scope == "project" and not p.is_absolute():
        return (project / p).resolve()
    return p.resolve()


def detect_candidates(project: Path) -> list[str]:
    # Keep auto-detection intentionally conservative; .github alone is not a Copilot signal.
    markers = {
        "claude-code": [".claude"], "cursor": [".cursor"], "opencode": [".opencode"],
        "browsercode": [".bcode"], "qwen": [".qwen"], "kimi": [".kimi-code"],
        "mimo": [".mimocode"], "cline": [".cline"], "roo-code": [".roo"],
        "windsurf": [".windsurf"], "trae": [".trae"], "continue": [".continue"],
        "goose": [".goose"], "kiro-cli": [".kiro"], "junie": [".junie"],
        "openhands": [".openhands"], "augment": [".augment"],
        "kilo-code": [".kilo"], "qoder": [".qoder"], "pi": [".pi"],
        "mux": [".mux"], "iflow-cli": [".iflow"], "mcpjam": [".mcpjam"],
        "zencoder": [".zencoder"], "mistral": [".vibe"], "grok": [".grok"],
        "deepcode": [".deepcode"], "zcode": [".zcode"], "gemini-cli": [".gemini"],
        "factory-droid": [".factory"], "crush": [".crush"],
    }
    commands = {
        "codex": ["codex"], "claude-code": ["claude"], "gemini-cli": ["gemini"],
        "opencode": ["opencode"], "browsercode": ["bcode"], "qwen": ["qwen", "qwen-code"],
        "kimi": ["kimi", "kimi-code"], "mimo": ["mimo"], "goose": ["goose"],
        "mistral": ["vibe"], "warp": ["warp"], "factory-droid": ["droid"],
        "crush": ["crush"],
    }
    found = {k for k, ms in markers.items() if any((project / m).exists() for m in ms)}
    for runtime, executables in commands.items():
        if any(shutil.which(command) for command in executables):
            found.add(runtime)
    return sorted(found)


def ignore(_directory: str, names: list[str]) -> set[str]:
    ignored = {n for n in names if n in REPO_EXCLUDES or n in FILE_EXCLUDES}
    # GitHub README artwork is repository-only and should not be duplicated into runtime installs.
    if Path(_directory).name == "assets" and "readme" in names:
        ignored.add("readme")
    return ignored


def main() -> int:
    ap = argparse.ArgumentParser(description="Safely install SKick into a filesystem Agent Skill root")
    ap.add_argument("--target", default="auto", help="Runtime id from INSTALLATION_MANIFEST.json, 'agents', or 'auto'")
    ap.add_argument("--scope", choices=["project", "user"], default="project")
    ap.add_argument("--project", type=Path, default=Path.cwd())
    ap.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--destination", type=Path, help="Explicit user-approved destination; overrides manifest path selection")
    ap.add_argument("--path-index", type=int, default=0, help="Choose an alternate declared path when a runtime has more than one")
    ap.add_argument("--force", action="store_true", help="Replace an existing destination after explicit selection; existing install is backed up by default")
    ap.add_argument("--no-backup", action="store_true", help="With --force, delete the existing destination instead of creating a sibling backup")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-targets", action="store_true")
    args = ap.parse_args()

    source = args.source.resolve()
    project = args.project.resolve()
    manifest = load_manifest(source)
    targets = filesystem_targets(manifest)

    if args.list_targets:
        for pid, item in sorted(targets.items()):
            print(f"{pid:20} {item.get('status','')} project={item.get('project_paths',[])} user={item.get('user_paths',[])}")
        return 0

    target = args.target
    if target == "auto":
        matches = [m for m in detect_candidates(project) if m in targets]
        if not matches:
            raise SystemExit("Could not safely infer an active filesystem runtime. Pass --target explicitly, or use --target agents only when the host supports .agents/skills.")
        if len(matches) != 1:
            raise SystemExit("Runtime detection is ambiguous: " + ", ".join(matches) + ". Pass --target explicitly.")
        target = matches[0]
    if target not in targets:
        raise SystemExit(f"Target {target!r} has no declared filesystem Skill path. Use the managed UI adapter or generic fallback instead.")

    item = targets[target]
    status = item.get("status", "")
    declared = item.get("project_paths" if args.scope == "project" else "user_paths", [])
    if args.destination:
        destination = args.destination.expanduser().resolve()
    else:
        if not declared:
            raise SystemExit(f"Target {target!r} has no declared {args.scope} path in this release.")
        if args.path_index < 0 or args.path_index >= len(declared):
            raise SystemExit(f"--path-index out of range; available {args.scope} paths: {declared}")
        destination = expand_path(declared[args.path_index], project, args.scope)

    # Refuse obviously dangerous or recursive destinations before any destructive operation.
    protected = {Path("/").resolve(), Path.home().resolve(), project.resolve(), source.resolve()}
    if destination in protected:
        raise SystemExit(f"Refusing unsafe destination: {destination}")
    try:
        destination.relative_to(source)
    except ValueError:
        pass
    else:
        raise SystemExit("Refusing to install SKick inside its own source tree.")

    print(f"SKick source: {source}")
    print(f"Target runtime: {target}")
    print(f"Support status: {status}")
    print(f"Install scope: {args.scope}")
    print(f"Destination: {destination}")
    if status.startswith("ECOSYSTEM_"):
        print("WARNING: this path is ecosystem-verified; re-check the installed runtime's first-party documentation before automating global deployment.")
    if target == "agents":
        print("WARNING: .agents/skills is a shared convention. The active host must actually scan it.")

    if args.dry_run:
        print("Dry run only; no files changed.")
        return 0

    if destination.exists() or destination.is_symlink():
        version_file = destination / "VERSION"
        version = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else "unknown"
        if not args.force:
            raise SystemExit(f"Destination already exists (version {version}): {destination}. Inspect local changes first, then rerun with --force only if replacement is intended.")
        if args.no_backup:
            if destination.is_symlink() or destination.is_file():
                destination.unlink()
            else:
                shutil.rmtree(destination)
            print("Existing installation removed because --no-backup was explicitly supplied.")
        else:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup = destination.with_name(destination.name + f".backup-{stamp}")
            if backup.exists():
                raise SystemExit(f"Backup destination unexpectedly exists: {backup}")
            shutil.move(str(destination), str(backup))
            print(f"Existing installation backed up to: {backup}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=ignore)
    print(f"Installed SKick files at: {destination}")
    print("Runtime discovery is NOT proven by the copy. Reload/refresh the host as documented and verify that a Skill named 'skick' is actually discovered and activated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
