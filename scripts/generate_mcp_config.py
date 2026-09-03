#!/usr/bin/env python3
"""Generate example local MCP configuration without installing or mutating the host.

Only profiles with stable local stdio shapes are emitted. Project/cloud/database/
remote/keyed providers stay in the catalog so the active host can configure them
from current first-party documentation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PROFILES = {
    "core-code": ["serena", "context7"],
    "browser-fast": ["agent-browser"],
    "browser-e2e": ["playwright"],
    "browser-diagnostics": ["chrome-devtools"],
    "engineering": ["serena", "context7", "agent-browser"],
    "engineering-debug": ["serena", "context7", "chrome-devtools"],
}

STDIO = {
    "serena": {"command": "serena", "args": ["start-mcp-server", "--project-from-cwd"]},
    "context7": {"command": "npx", "args": ["-y", "@upstash/context7-mcp@latest"]},
    "agent-browser": {"command": "agent-browser", "args": ["mcp", "--tools", "core"]},
    "playwright": {"command": "npx", "args": ["-y", "@playwright/mcp@latest"]},
    "chrome-devtools": {"command": "npx", "args": ["-y", "chrome-devtools-mcp@latest", "--isolated=true", "--redact-network-headers=true"]},
}

HEADER = "# Example only. Resolve current first-party docs, inspect/pin package versions for persistent use, and run MCP qualification before trust."


def selected(profile: str) -> list[str]:
    return PROFILES[profile]


def config_for(name: str, host: str) -> dict:
    cfg = {"command": STDIO[name]["command"], "args": list(STDIO[name]["args"])}
    if name == "serena":
        cfg["args"] += ["--context", "codex" if host == "codex" else "claude-code" if host == "claude-code" else "ide-assistant"]
    return cfg


def codex(profile: str) -> str:
    out = [HEADER]
    for name in selected(profile):
        cfg = config_for(name, "codex")
        key = name.replace("-", "_")
        out += [f"\n[mcp_servers.{key}]", f'command = {json.dumps(cfg["command"])}', f'args = {json.dumps(cfg["args"])}']
    return "\n".join(out) + "\n"


def claude(profile: str) -> str:
    servers = {name: config_for(name, "claude-code") for name in selected(profile)}
    return json.dumps({"_note": HEADER, "mcpServers": servers}, indent=2) + "\n"


def generic(profile: str) -> str:
    servers = {name: config_for(name, "generic") for name in selected(profile)}
    return json.dumps({"_note": HEADER, "mcpServers": servers}, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--host", choices=["codex", "claude-code", "generic"])
    ap.add_argument("--profile", choices=sorted(PROFILES), default="core-code")
    ap.add_argument("--output")
    ap.add_argument("--list-profiles", action="store_true")
    args = ap.parse_args()
    if args.list_profiles:
        for profile, providers in sorted(PROFILES.items()):
            print(f"{profile}: {', '.join(providers)}")
        return 0
    if not args.host:
        ap.error("--host is required unless --list-profiles is used")
    text = {"codex": codex, "claude-code": claude, "generic": generic}[args.host](args.profile)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
