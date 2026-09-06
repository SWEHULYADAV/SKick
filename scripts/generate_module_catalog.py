#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def title_for(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def estimate(path: Path) -> int:
    return max(1, round(path.stat().st_size / 4))


def generate(root: Path) -> dict:
    policy_path = root / "runtime" / "module_policies.json"
    policies = json.loads(policy_path.read_text(encoding="utf-8"))
    overrides = policies.get("overrides", {})
    paths = sorted(list((root / "core").glob("*.md")) + list((root / "extensions").glob("*.md")))
    modules = []
    errors = []
    for path in paths:
        rel = path.relative_to(root).as_posix()
        override = overrides.get(rel, {})
        entry = {
            "id": path.stem,
            "path": rel,
            "title": title_for(path),
            "priority": int(override.get("priority", 20)),
            "mandatory": bool(override.get("mandatory", False)),
            "always_for_activated": bool(override.get("always_for_activated", False)),
            "modes": list(override.get("modes", [])),
            "depths": list(override.get("depths", ["quick", "standard", "deep", "exhaustive"])),
            "task_patterns": list(override.get("task_patterns", [])),
            "domains": list(override.get("domains", [])),
            "required_capabilities": list(override.get("required_capabilities", [])),
            "optional_capabilities": list(override.get("optional_capabilities", [])),
            "required_provider": override.get("required_provider"),
            "project_policy": override.get("project_policy"),
            "estimated_context_tokens": estimate(path),
            "estimate_method": "utf8_bytes_div_4"
        }
        for pattern in entry["task_patterns"]:
            try:
                re.compile(pattern)
            except re.error as exc:
                errors.append(f"{rel}: invalid task pattern {pattern!r}: {exc}")
        modules.append(entry)
    unknown_overrides = sorted(set(overrides) - {m["path"] for m in modules})
    errors.extend(f"module policy references missing path: {p}" for p in unknown_overrides)
    if errors:
        raise ValueError("\n".join(errors))
    return {"schema_version": 1, "generated_by": "scripts/generate_module_catalog.py", "modules": modules}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", type=Path, default=ROOT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = args.root.resolve()
    target = root / "runtime" / "module_catalog.json"
    data = generate(root)
    text = json.dumps(data, indent=2) + "\n"
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != text:
            print("module catalog is stale")
            return 1
        print(f"module catalog in sync ({len(data['modules'])} modules)")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"generated {target.relative_to(root)} ({len(data['modules'])} modules)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
