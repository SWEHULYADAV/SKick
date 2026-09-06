#!/usr/bin/env python3
"""Conservatively normalize SKick's canonical compatibility registry.

This script never upgrades a route to DOC_VERIFIED or LIVE_TESTED. Evidence
upgrades are editorial/research actions and must be made in
INSTALLATION_MANIFEST.json with sources. The script only fills missing truth
fields using conservative defaults and validates cross-field invariants.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

STATUSES = {
    "LIVE_TESTED", "DOC_VERIFIED", "COMMUNITY_VERIFIED", "HOST_DEPENDENT",
    "GENERIC_PROMPT_FALLBACK", "BROKEN_UNSUPPORTED", "UNKNOWN",
}
OFFICIAL_SOURCE_TYPES = {
    "first_party_docs", "first_party_release_notes", "official_repository", "official_support",
}


def conservative_status(entry: dict) -> str:
    if entry.get("kind") == "model_provider_only":
        return "HOST_DEPENDENT"
    if entry.get("kind") == "generic":
        return "GENERIC_PROMPT_FALLBACK"
    return "UNKNOWN"


def normalize(data: dict, today: str | None = None) -> tuple[dict, list[str]]:
    today = today or date.today().isoformat()
    errors: list[str] = []
    platforms = data.get("platforms", {})
    if not isinstance(platforms, dict):
        return data, ["platforms must be an object"]
    for pid, entry in platforms.items():
        if not isinstance(entry, dict):
            errors.append(f"{pid}: entry must be an object")
            continue
        status = entry.setdefault("verification_status", conservative_status(entry))
        entry["status"] = status
        entry.setdefault("legacy_status", "UNSPECIFIED")
        if status not in STATUSES:
            errors.append(f"{pid}: invalid verification_status {status!r}")
        if entry.get("kind") == "model_provider_only":
            entry.setdefault("entity_type", "model_provider")
            entry.setdefault("native_skill_support", "host_dependent")
            entry.setdefault("runtime_tier", "prompt_fallback")
        else:
            entry.setdefault("entity_type", "unknown")
            entry.setdefault("native_skill_support", "unknown")
            entry.setdefault("runtime_tier", "unknown")
        entry.setdefault("capabilities", [])
        entry.setdefault("activation", {
            "explicit": "unknown",
            "literal_at_skick": "unknown",
            "native_equivalent": "Use the host's documented Skill mechanism.",
            "automatic": "unknown",
        })
        entry.setdefault("last_verified", today)
        entry.setdefault("official_evidence", [])
        entry.setdefault("live_test", None)
        entry.setdefault("limitations", [])

        if status == "DOC_VERIFIED":
            evidence = entry.get("official_evidence") or []
            if not evidence:
                errors.append(f"{pid}: DOC_VERIFIED requires official_evidence")
            elif not any(
                item.get("source_type") in OFFICIAL_SOURCE_TYPES
                and item.get("checked_on") == entry.get("last_verified")
                for item in evidence
                if isinstance(item, dict)
            ):
                errors.append(
                    f"{pid}: DOC_VERIFIED requires current first-party documentation, support, "
                    "release-note, or official-repository evidence"
                )
        if status == "LIVE_TESTED":
            live = entry.get("live_test")
            required = {"skick_version", "host_version", "tested_on", "activation", "result"}
            if not isinstance(live, dict) or required - set(live) or live.get("result") != "passed":
                errors.append(f"{pid}: LIVE_TESTED requires reproducible passing live_test metadata")
        if entry.get("entity_type") == "model_provider" and entry.get("activation", {}).get("literal_at_skick") == "yes":
            errors.append(f"{pid}: model provider cannot claim literal @SKick without a native host contract")
    return data, errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    path = args.root.resolve() / "INSTALLATION_MANIFEST.json"
    original = json.loads(path.read_text(encoding="utf-8"))
    normalized, errors = normalize(json.loads(json.dumps(original)))
    changed = normalized != original
    for error in errors:
        print(f"ERROR {error}")
    if args.write and not errors:
        path.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"normalized {len(normalized.get('platforms', {}))} routes")
    elif changed:
        print("registry is not normalized; run with --write")
    else:
        print(f"registry normalized: {len(normalized.get('platforms', {}))} routes")
    return 1 if errors or (args.check and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
