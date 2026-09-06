# OpenAI Codex Plugin Adapter — VERIFIED

Codex plugins use `.codex-plugin/plugin.json` and may bundle Agent Skills under `skills/`. This is the distributable/shared form for Codex; direct `.agents/skills/` remains useful for repo-local skills.

## Package shape
- `.codex-plugin/plugin.json`
- `skills/skick/SKILL.md`
- `skills/skick/core/`

Keep the plugin thin: all research methodology stays in the Skill/core.


## Superpowers
Codex can also use the official Superpowers plugin. When both are installed, let Superpowers own matching engineering-method phases while SKick owns research/evidence/versioning/MCP routing.

## MCP stack
Use `core/mcp-stack.md`; prefer native capability first and enable only task-matched, trusted servers.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `openai-plugin`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `partial_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `unknown`
- **Native activation equivalent:** Install the plugin in a host that supports Agent Plugins v1, then use that host activation mechanism.
- **Surfaces covered:** Codex plugin/workspace
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use the Codex plugin wrapper when you intentionally distribute SKick as a Codex plugin; otherwise prefer a plain Agent Skill.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `codex-plugin.zip`

### GitHub source fast path

- No runtime-specific remote command is asserted. Fetch/inspect the GitHub source, then use the verified path/UI for this adapter.

Always read `../../docs/GITHUB_BOOTSTRAP.md` before treating a repository URL as installable. Native remote-install commands are allowed only when the current runtime documents them.

### Safe setup sequence

1. Read `../../START_HERE.md`, `../../INSTALLATION_MANIFEST.json`, and `../../docs/WARNINGS.md` first.
2. Inspect the target runtime and existing SKick installation before writing or uploading anything.
3. Prefer project scope when the user did not request a global/personal install and the runtime supports project Skills.
4. Preserve the complete SKick directory for directory-form Agent Skills; do not copy only `SKILL.md` when it references supporting files.
5. Do not silently install semantic repository providers, MCP servers, plugins, extensions, browser tooling, cloud CLIs, credentials, or other optional dependencies. Optional capability setup requires a separate justified and authorized path.
6. Reload/refresh/restart only as required by this runtime's documented behavior.
7. Verify discovery in the actual active surface, not only by checking that files exist.
8. Report the selected runtime, scope/path or UI flow, SKick version, verification performed, and any step that required user/admin/UI/authentication action.

### Verification

1. Confirm the plugin lists the SKick skill.
2. Verify any required apps separately; SKick itself does not grant app access.

### Availability and limitations

- No additional platform-specific limitation is asserted beyond the normal runtime and security warnings.

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

https://developers.openai.com/plugins/build/plugins

<!-- SKICK-AI-INSTALL-END -->
