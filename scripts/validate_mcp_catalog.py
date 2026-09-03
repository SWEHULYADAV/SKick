#!/usr/bin/env python3
"""Validate MCP catalog references, safety metadata, and profile semantics."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("catalog", nargs="?", default="mcp/catalog.json")
    args = ap.parse_args()
    path = Path(args.catalog)
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    if data.get("release") != "v1.0":
        errors.append("release must be v1.0")

    servers = data.get("servers") if isinstance(data.get("servers"), list) else []
    profiles = data.get("profiles") if isinstance(data.get("profiles"), list) else []
    validators = data.get("validators") if isinstance(data.get("validators"), list) else []

    def unique_ids(items: list[dict], kind: str) -> set[str]:
        seen: set[str] = set()
        for item in items:
            ident = item.get("id") if isinstance(item, dict) else None
            if not isinstance(ident, str) or not ID_RE.fullmatch(ident):
                errors.append(f"invalid {kind} id: {ident!r}")
                continue
            if ident in seen:
                errors.append(f"duplicate {kind} id: {ident}")
            seen.add(ident)
        return seen

    server_ids = unique_ids(servers, "server")
    profile_ids = unique_ids(profiles, "profile")
    unique_ids(validators, "validator")

    for server in servers:
        if not isinstance(server, dict):
            continue
        ident = server.get("id", "?")
        upstream = server.get("upstream")
        if not isinstance(upstream, str) or not (upstream.startswith("https://") or upstream.startswith("local:")):
            errors.append(f"invalid upstream for {ident}")
        if not isinstance(server.get("role"), list) or not server.get("role"):
            errors.append(f"missing role list for {ident}")
        if not isinstance(server.get("write_capable"), bool) or not isinstance(server.get("external_data"), bool):
            errors.append(f"boolean trust metadata missing for {ident}")
        for profile in server.get("profiles", []):
            if profile not in profile_ids:
                errors.append(f"server {ident} references unknown profile {profile}")

    for profile in profiles:
        if not isinstance(profile, dict):
            continue
        ident = profile.get("id", "?")
        mode = profile.get("mode")
        providers = profile.get("providers")
        if mode not in {"all", "one_of"}:
            errors.append(f"profile {ident} has invalid mode")
        if not isinstance(providers, list) or not providers:
            errors.append(f"profile {ident} has no providers")
            continue
        if len(set(providers)) != len(providers):
            errors.append(f"profile {ident} repeats provider ids")
        for provider in providers:
            if provider not in server_ids:
                errors.append(f"profile {ident} references unknown provider {provider}")
        if mode == "one_of" and len(providers) < 2:
            errors.append(f"one_of profile {ident} should expose alternatives")

    raw = json.dumps(data).lower()
    for marker in ["ghp_", "sk-proj-", "sk_live_", "sk_test_", "bearer actual", "actual_token"]:
        if marker in raw:
            errors.append(f"credential-like value found: {marker}")

    if errors:
        print("MCP CATALOG VALIDATION: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    print("MCP CATALOG VALIDATION: PASS")
    print(f"servers={len(servers)} profiles={len(profiles)} validators={len(validators)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
