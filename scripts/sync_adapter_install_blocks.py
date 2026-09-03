#!/usr/bin/env python3
"""Synchronize adapter install-contract blocks from INSTALLATION_MANIFEST.json."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BEGIN = "<!-- SKICK-AI-INSTALL-BEGIN -->"
END = "<!-- SKICK-AI-INSTALL-END -->"
BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)


def fmt_paths(values: list[str] | None, none_text: str) -> str:
    if not values:
        return none_text
    return ", ".join(f"`{v}`" for v in values)


def build_block(platform_id: str, entry: dict) -> str:
    surfaces = ", ".join(entry.get("surfaces") or ["unspecified"])
    distribution = entry.get("distribution") or "No dedicated generated archive; follow the native/manual adapter path."
    verification = entry.get("verification") or ["Confirm SKick is discovered by the actual target runtime."]
    verify_lines = "\n".join(f"{i}. {line}" for i, line in enumerate(verification, 1))
    source = entry.get("source", "")
    availability = entry.get("availability") or "Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface."
    limitations = entry.get("limitations") or []
    limitation_lines = "\n".join(f"- {x}" for x in limitations) if limitations else "- No additional platform-specific limitation is asserted beyond the normal runtime and security warnings."
    github_commands = entry.get("github_commands") or []
    github_lines = "\n".join(f"- {line}" for line in github_commands) if github_commands else "- No runtime-specific remote command is asserted. Fetch/inspect the GitHub source, then use the verified path/UI for this adapter."
    return f"""{BEGIN}
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **\"install this\"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `{platform_id}`
- **Support status:** `{entry.get('status', 'UNSPECIFIED')}`
- **Surfaces covered:** {surfaces}
- **Availability / gating:** {availability}
- **Preferred install:** {entry.get('preferred_install', 'Follow current first-party runtime documentation.')}
- **Project/local destinations:** {fmt_paths(entry.get('project_paths'), 'No filesystem project path is asserted for this surface.')}
- **User/personal destinations:** {fmt_paths(entry.get('user_paths'), 'No filesystem personal path is asserted for this surface.')}
- **Prebuilt distribution when applicable:** `{distribution}`

### GitHub source fast path

{github_lines}

Always read `../../docs/GITHUB_BOOTSTRAP.md` before treating a repository URL as installable. Native remote-install commands are allowed only when the current runtime documents them.

### Safe setup sequence

1. Read `../../START_HERE.md`, `../../INSTALLATION_MANIFEST.json`, and `../../docs/WARNINGS.md` first.
2. Inspect the target runtime and existing SKick installation before writing or uploading anything.
3. Prefer project scope when the user did not request a global/personal install and the runtime supports project Skills.
4. Preserve the complete SKick directory for directory-form Agent Skills; do not copy only `SKILL.md` when it references supporting files.
5. Do not silently install Serena, MCP servers, plugins, extensions, browser tooling, cloud CLIs, credentials, or other optional dependencies. The universal prompt in `../../BOOTSTRAP_PROMPTS.md` is an explicit exception only for canonical Serena setup; it does not authorize unrelated dependencies.
6. Reload/refresh/restart only as required by this runtime's documented behavior.
7. Verify discovery in the actual active surface, not only by checking that files exist.
8. Report the selected runtime, scope/path or UI flow, SKick version, verification performed, and any step that required user/admin/UI/authentication action.

### Verification

{verify_lines}

### Availability and limitations

{limitation_lines}

### Update and removal

- For filesystem installs, inspect `VERSION` and local modifications before replacement. Replace the complete Skill directory rather than mixing files from releases.
- For managed web/app/plugin installs, use the product's current update/remove controls.
- For forks, change canonical source first and rebuild generated distributions; never maintain an extracted wrapper as the source of truth.

### Runtime-specific warnings

- Do not infer paths, commands, manifest schemas, or UI controls from another platform.
- Treat downloaded Skills/plugins and bundled scripts as untrusted until reviewed.
- Never put credentials, tokens, cookies, private keys, or secrets into SKick files.
- Structural ZIP validation is not proof of successful execution in an external runtime.
- Re-check current first-party documentation before automating version-sensitive install commands.

### Primary support reference

{source}

{END}"""


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    manifest = json.loads((root / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    updated = 0
    platforms = manifest.get("platforms", {})
    adapter_counts: dict[str, int] = {}
    for entry in platforms.values():
        adapter = entry.get("adapter") if isinstance(entry, dict) else None
        if isinstance(adapter, str):
            adapter_counts[adapter] = adapter_counts.get(adapter, 0) + 1
    for platform_id, entry in platforms.items():
        adapter = entry.get("adapter")
        if not isinstance(adapter, str):
            errors.append(f"{platform_id}: missing adapter path")
            continue
        path = root / adapter
        if not path.is_file():
            errors.append(f"{platform_id}: adapter not found: {adapter}")
            continue
        if adapter_counts.get(adapter, 0) > 1:
            # Shared/provider adapters describe several model routes and should not be
            # overwritten repeatedly with one platform-specific install block.
            continue
        text = path.read_text(encoding="utf-8")
        block = build_block(platform_id, entry)
        if BLOCK_RE.search(text):
            new = BLOCK_RE.sub(block, text, count=1)
        else:
            new = text.rstrip() + "\n\n" + block + "\n"
        path.write_text(new, encoding="utf-8")
        updated += 1
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print(f"Synchronized {updated} adapter install blocks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
