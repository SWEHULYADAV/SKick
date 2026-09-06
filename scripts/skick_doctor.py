#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.capabilities import discover_capabilities
from runtime.versioning import read_package_version
from scripts.detect_runtime import detect


def expand(raw: str, project: Path) -> Path:
    value = os.path.expandvars(os.path.expanduser(raw))
    path = Path(value)
    return (project / path).resolve() if not path.is_absolute() else path.resolve()


def _frontmatter_valid(path: Path) -> tuple[bool, str | None]:
    if not path.is_file():
        return False, "SKILL.md missing"
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return False, "SKILL.md frontmatter delimiter missing"
    end = text.find("\n---\n", 4)
    if end < 0:
        return False, "SKILL.md closing frontmatter delimiter missing"
    frontmatter = text[4:end]
    name = re.search(r"(?m)^name:\s*(\S+)\s*$", frontmatter)
    description = re.search(r"(?m)^description:\s*(.+?)\s*$", frontmatter)
    if not name or not description:
        return False, "SKILL.md frontmatter requires name and description"
    if name.group(1).strip() != name.group(1).strip().lower():
        return False, "SKILL.md name must be lowercase"
    return True, None


def _inspect_install(path: Path, package_version: str) -> dict:
    skill_path = path / "SKILL.md"
    version_path = path / "VERSION"
    version = version_path.read_text(encoding="utf-8").strip() if version_path.is_file() else None
    frontmatter_valid, frontmatter_problem = _frontmatter_valid(skill_path)
    return {
        "path": str(path),
        "entrypoint_exists": skill_path.is_file(),
        "frontmatter_valid": frontmatter_valid,
        "frontmatter_problem": frontmatter_problem,
        "installed_version": version,
        "package_version": package_version,
        "version_matches_package": version == package_version if version is not None else False,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Diagnose a SKick filesystem/runtime installation without overstating proof")
    ap.add_argument("--project", type=Path, default=Path.cwd())
    ap.add_argument("--target", default="auto")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    project = args.project.resolve()
    manifest = json.loads((ROOT / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
    package_version = read_package_version(ROOT)
    candidates = detect(project)
    target = args.target
    if target == "auto":
        target = candidates[0] if len(candidates) == 1 else "unknown"
    entry = manifest.get("platforms", {}).get(target) if target != "unknown" else None

    detected: list[str] = []
    inferred: list[str] = []
    unverified: list[str] = []
    problems: list[str] = []
    existing_installs: list[dict] = []

    if candidates:
        detected.append("runtime candidate evidence: " + ", ".join(candidates))
    else:
        unverified.append("active host identity could not be observed from local markers/executables")

    install_path = None
    if isinstance(entry, dict):
        paths = entry.get("project_paths") or []
        if paths:
            resolved_paths: list[Path] = []
            for raw in paths:
                path = expand(raw, project)
                if path not in resolved_paths:
                    resolved_paths.append(path)
            install_path = resolved_paths[0]
            inferred.append(f"preferred project install path from manifest: {install_path}")
            for path in resolved_paths:
                if path.exists() or path.is_symlink():
                    inspected = _inspect_install(path, package_version)
                    existing_installs.append(inspected)
                    detected.append(f"SKick installation candidate exists at {path}")
                    if not inspected["frontmatter_valid"]:
                        problems.append(f"Malformed SKILL.md frontmatter at {path}: {inspected['frontmatter_problem']}")
                    if inspected["installed_version"] is None:
                        problems.append(f"VERSION missing from installation at {path}")
                    elif not inspected["version_matches_package"]:
                        problems.append(
                            f"Version mismatch at {path}: installed {inspected['installed_version']} vs package {package_version}"
                        )
            if not existing_installs:
                detected.append(f"SKick entrypoint not present at declared project paths for target {target}")
            if len(existing_installs) > 1:
                problems.append(
                    "Duplicate SKick installations detected for this target: "
                    + ", ".join(item["path"] for item in existing_installs)
                )
        else:
            inferred.append("target has no filesystem project path; managed/fallback adapter may be required")
    else:
        unverified.append("target could not be resolved to a canonical manifest route")

    snapshot = discover_capabilities(project, runtime_candidates={name: ["local candidate"] for name in candidates})
    unverified.extend([
        "runtime Skill discovery is unverified unless the host's own inventory was observed",
        "explicit invocation is unverified unless the host accepted the native activation mechanism",
        "live task execution is unverified unless a real task completed under the host",
    ])
    payload = {
        "schema_version": 2,
        "target": target,
        "project": str(project),
        "package_version": package_version,
        "install_path": str(install_path) if install_path else None,
        "existing_installs": existing_installs,
        "problems": problems,
        "detected": detected,
        "inferred": inferred,
        "unverified": unverified,
        "capabilities": snapshot.to_dict()["capabilities"],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Target: {target}")
        print(f"Package version: {package_version}")
        for label in ("detected", "inferred", "unverified", "problems"):
            print(label.upper() + ":")
            for item in payload[label]:
                print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
