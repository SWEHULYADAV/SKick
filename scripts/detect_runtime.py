#!/usr/bin/env python3
"""Detect likely AI coding-agent runtimes without pretending certainty.

Outputs candidates from project markers and installed executables. This is a
hinting tool only; installation must still use INSTALLATION_MANIFEST.json and
runtime-specific verification.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.capabilities import discover_capabilities, load_declared_capabilities


MARKERS = {
    "claude-code": [".claude"],
    "cursor": [".cursor"],
    "opencode": [".opencode"],
    "browsercode": [".bcode"],
    "qwen": [".qwen"],
    "kimi": [".kimi-code"],
    "mimo": [".mimocode"],
    "cline": [".cline"],
    "roo-code": [".roo"],
    "windsurf": [".windsurf"],
    "trae": [".trae"],
    "continue": [".continue"],
    "goose": [".goose"],
    "kiro-cli": [".kiro"],
    "junie": [".junie"],
    "openhands": [".openhands"],
    "devin": [".devin"],
    "augment": [".augment"],
    "kilo-code": [".kilocode"],
    "qoder": [".qoder"],
    "pi": [".pi"],
    "mux": [".mux"],
    "iflow-cli": [".iflow"],
    "mcpjam": [".mcpjam"],
    "zencoder": [".zencoder"],
    "mistral": [".vibe"],
    "grok": [".grok"],
    "deepcode": [".deepcode"],
    "zcode": [".zcode"],
    "gemini-cli": [".gemini"],
    "factory-droid": [".factory"],
    "crush": [".crush"],
}

EXECUTABLES = {
    "codex": ["codex"],
    "claude-code": ["claude"],
    "gemini-cli": ["gemini"],
    "opencode": ["opencode"],
    "browsercode": ["bcode"],
    "qwen": ["qwen", "qwen-code"],
    "kimi": ["kimi", "kimi-code"],
    "cline": ["cline"],
    "roo-code": ["roo"],
    "goose": ["goose"],
    "mistral": ["vibe"],
    "devin": ["devin"],
    "warp": ["warp"],
    "factory-droid": ["droid"],
    "crush": ["crush"],
}


def detect(project: Path) -> dict[str, list[str]]:
    evidence: dict[str, list[str]] = {}
    for runtime, markers in MARKERS.items():
        for marker in markers:
            if (project / marker).exists():
                evidence.setdefault(runtime, []).append(f"project marker {marker}")
    for runtime, commands in EXECUTABLES.items():
        for command in commands:
            path = shutil.which(command)
            if path:
                evidence.setdefault(runtime, []).append(f"executable {command} -> {path}")
                break
    return evidence


def main() -> int:
    ap = argparse.ArgumentParser(description="Detect likely SKick host runtimes from local evidence")
    ap.add_argument("--project", type=Path, default=Path.cwd())
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--capabilities", action="store_true", help="include a conservative structured capability snapshot")
    ap.add_argument("--capabilities-file", type=Path, help="trusted host capability declaration JSON")
    ap.add_argument("--probe-network", action="store_true", help="opt in to a small active network probe")
    args = ap.parse_args()
    project = args.project.resolve()
    evidence = detect(project)
    payload = {"project": str(project), "candidates": evidence}
    if args.capabilities:
        declared = load_declared_capabilities(args.capabilities_file) if args.capabilities_file else None
        payload["capability_snapshot"] = discover_capabilities(
            project,
            declared=declared,
            active_network_probe=args.probe_network,
            runtime_candidates=evidence,
        ).to_dict()
    if args.json:
        print(json.dumps(payload, indent=2))
    elif args.capabilities:
        print(json.dumps(payload["capability_snapshot"], indent=2))
    elif not evidence:
        print("No runtime could be inferred safely. Use the actual host name explicitly or the shared Agent Skills fallback only when supported.")
    else:
        for runtime, reasons in sorted(evidence.items()):
            print(f"{runtime}: " + "; ".join(reasons))
        if len(evidence) > 1:
            print("Multiple candidates found; do not auto-install until the active host is known.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
