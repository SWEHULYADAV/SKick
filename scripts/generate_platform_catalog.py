#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def q(values: list[str]) -> str:
    return ", ".join(f"`{v}`" for v in values) if values else "Managed/UI or host-dependent; no filesystem path asserted."


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
    lines = [
        "# SKick Platform Installation Catalog",
        "",
        "This catalog is generated from `INSTALLATION_MANIFEST.json`. Use the matching adapter for detailed setup, verification, update/removal, and warnings. Re-check current first-party documentation before automating version-sensitive commands.",
        "",
        "## How to use this catalog",
        "",
        "1. Identify the actual host runtime, not only the model/provider name.",
        "2. Match the runtime/alias below.",
        "3. Open the linked adapter.",
        "4. Prefer project scope when the user did not request global scope and the host supports project Skills.",
        "5. Verify discovery in the active runtime surface after copying/uploading.",
        "",
        "## Summary",
        "",
        "| Runtime | Status | Availability / gating | Surfaces | Preferred form | Adapter |",
        "|---|---|---|---|---|---|",
    ]
    for pid, p in data["platforms"].items():
        surfaces = ", ".join(p.get("surfaces", []))
        pref = p.get("preferred_install", "").replace("|", "\\|")
        availability = p.get("availability", "Host/plan/version dependent; see adapter.").replace("|", "\\|")
        lines.append(f"| `{pid}` | {p.get('status','')} | {availability} | {surfaces} | {pref} | [`{p['adapter']}`](../{p['adapter']}) |")
    lines += ["", "## Detailed routing", ""]
    for pid, p in data["platforms"].items():
        lines += [
            f"### {pid}",
            "",
            f"- **Aliases:** {', '.join(p.get('aliases', []))}",
            f"- **Status:** `{p.get('status','')}`",
            f"- **Surfaces:** {', '.join(p.get('surfaces', []))}",
            f"- **Availability / gating:** {p.get('availability','Host/plan/version dependent; see current first-party documentation and adapter.')}",
            f"- **Preferred install:** {p.get('preferred_install','')}",
            f"- **Project/local paths:** {q(p.get('project_paths', []))}",
            f"- **User/personal paths:** {q(p.get('user_paths', []))}",
            f"- **Generated distribution:** `{p['distribution']}`" if p.get("distribution") else "- **Generated distribution:** none dedicated",
            f"- **Adapter:** [`{p['adapter']}`](../{p['adapter']})",
            f"- **Primary source:** {p.get('source') or (p.get('sources') or ['No standalone native source asserted; use host/fallback rules.'])[0]}",
            "- **Verification:**",
        ]
        for v in p.get("verification", []):
            lines.append(f"  - {v}")
        limitations = p.get('limitations', [])
        if limitations:
            lines.append('- **Limitations / caveats:**')
            for item in limitations:
                lines.append(f'  - {item}')
        availability_source = p.get('availability_source')
        if availability_source:
            lines.append(f'- **Availability source:** {availability_source}')
        extra_sources = p.get('sources', [])
        if extra_sources:
            lines.append('- **Sources:**')
            for src in extra_sources:
                lines.append(f'  - {src}')
        lines.append("")
    (root / "docs" / "PLATFORM_CATALOG.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
    print("Generated docs/PLATFORM_CATALOG.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
