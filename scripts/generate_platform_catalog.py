#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def q(values: list[str]) -> str:
    return ", ".join(f"`{v}`" for v in values) if values else "None asserted."


def esc(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def official_source_for(p: dict) -> str:
    ev = p.get("official_evidence") or []
    if ev and isinstance(ev[0], dict) and ev[0].get("url"):
        return ev[0]["url"]
    return ""


def source_for(p: dict) -> str:
    return official_source_for(p) or p.get("source") or ((p.get("sources") or [""])[0])


def build_catalog(data: dict) -> str:
    counts = Counter(p.get("verification_status", "UNKNOWN") for p in data["platforms"].values())
    lines = [
        "# SKick Platform Installation Catalog", "",
        "Generated from `INSTALLATION_MANIFEST.json`. Route count is not a quality target; proof status is.", "",
        "## Proof summary", "",
        " | ".join([]),
    ]
    lines.pop()
    lines += ["| Verification status | Routes |", "|---|---:|"]
    for key in ("LIVE_TESTED", "DOC_VERIFIED", "COMMUNITY_VERIFIED", "HOST_DEPENDENT", "GENERIC_PROMPT_FALLBACK", "BROKEN_UNSUPPORTED", "UNKNOWN"):
        lines.append(f"| `{key}` | {counts.get(key, 0)} |")
    lines += ["", "## Routes", "", "| Route | Entity | Proof | Runtime tier | Native Skill | Adapter |", "|---|---|---|---|---|---|"]
    for pid, p in data["platforms"].items():
        lines.append(f"| `{pid}` | {esc(p.get('entity_type'))} | `{p.get('verification_status')}` | `{p.get('runtime_tier')}` | `{p.get('native_skill_support')}` | [`{p['adapter']}`](../{p['adapter']}) |")
    lines += ["", "## Detailed routing", ""]
    for pid, p in data["platforms"].items():
        lines += [
            f"### `{pid}`", "",
            f"- **Entity type:** `{p.get('entity_type')}`",
            f"- **Verification:** `{p.get('verification_status')}` (checked `{p.get('last_verified')}`)",
            f"- **Runtime tier:** `{p.get('runtime_tier')}`",
            f"- **Native Skill support:** `{p.get('native_skill_support')}`",
            f"- **Explicit activation:** `{p.get('activation',{}).get('explicit')}` — {p.get('activation',{}).get('native_equivalent','')}",
            f"- **Literal `@SKick`:** `{p.get('activation',{}).get('literal_at_skick')}`",
            f"- **Automatic activation:** `{p.get('activation',{}).get('automatic')}`",
            f"- **Project paths:** {q(p.get('project_paths', []))}",
            f"- **User paths:** {q(p.get('user_paths', []))}",
            f"- **Evidence:** {source_for(p) or 'No current first-party evidence asserted.'}",
            f"- **Adapter:** [`{p['adapter']}`](../{p['adapter']})",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def build_audit(data: dict) -> str:
    lines = [
        "# SKick Compatibility Evidence Audit", "",
        "Generated from the canonical `INSTALLATION_MANIFEST.json`. `DOC_VERIFIED` is not `LIVE_TESTED`; no route is promoted to live proof without a reproducible live-test record.", "",
        "| Platform | Entity type | Native Skill | Install method | Project install | Global install | Discovery | Explicit activation | Literal `@SKick` | Native equivalent | Automatic | Runtime tier | Relevant capabilities | Required plan/tier if known | Limitations | Verification | Last verified | Official evidence | Live test | Notes |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for pid, p in data["platforms"].items():
        activation = p.get("activation", {})
        evidence = official_source_for(p) or "—"
        live = p.get("live_test")
        live_text = "—" if not live else f"{live.get('host_version','?')} / {live.get('tested_on','?')} / {live.get('result','?')}"
        discovery = "skill discovery" if "skill_discovery" in p.get("capabilities", []) else ("host-dependent" if p.get("verification_status") == "HOST_DEPENDENT" else "unknown")
        limitations = "; ".join(p.get("limitations", [])) or "—"
        lines.append("| " + " | ".join([
            f"`{pid}`", esc(p.get("entity_type")), f"`{p.get('native_skill_support')}`",
            esc(p.get("preferred_install", "")), "yes" if p.get("project_paths") else "no/managed",
            "yes" if p.get("user_paths") else "no/managed", discovery,
            f"`{activation.get('explicit')}`", f"`{activation.get('literal_at_skick')}`", esc(activation.get("native_equivalent")),
            f"`{activation.get('automatic')}`", f"`{p.get('runtime_tier')}`", esc(", ".join(p.get("capabilities", [])) or "—"),
            esc(p.get("availability") or "—"), esc(limitations), f"`{p.get('verification_status')}`", f"`{p.get('last_verified')}`", esc(evidence), esc(live_text),
            esc(p.get("notes") or (f"Legacy status: {p.get('legacy_status')}" if p.get("legacy_status") else "—"))
        ]) + " |")
    return "\n".join(lines).rstrip() + "\n"


def build_activation(data: dict) -> str:
    lines = [
        "# SKick Activation Matrix", "",
        "`@SKick` is a transport-specific syntax, not the universal protocol. Unknown means unproven, not unsupported.", "",
        "| Platform | Explicit | Literal `@SKick` | Native equivalent | Automatic | Proof |",
        "|---|---|---|---|---|---|",
    ]
    for pid, p in data["platforms"].items():
        a = p.get("activation", {})
        lines.append(f"| `{pid}` | `{a.get('explicit')}` | `{a.get('literal_at_skick')}` | {esc(a.get('native_equivalent'))} | `{a.get('automatic')}` | `{p.get('verification_status')}` |")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    root = args.root.resolve()
    data = json.loads((root / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
    outputs = {
        root / "docs/PLATFORM_CATALOG.md": build_catalog(data),
        root / "docs/PLATFORM_AUDIT.md": build_audit(data),
        root / "docs/ACTIVATION_MATRIX.md": build_activation(data),
    }
    stale = []
    for path, content in outputs.items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(root).as_posix())
        else:
            path.write_text(content, encoding="utf-8")
            print(f"Generated {path.relative_to(root)}")
    if stale:
        print("Generated platform docs are stale: " + ", ".join(stale))
        return 1
    if args.check:
        print("Generated platform docs are synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
