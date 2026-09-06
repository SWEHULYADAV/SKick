# GitHub Copilot Adapter - VERIFIED

GitHub Copilot supports Agent Skills and installable plugins in Copilot CLI/cloud-agent workflows. Copilot CLI can install a single Skill directly or a plugin; declaring the Agent Plugins v1 schema in root `plugin.json` opts into the portable open-plugin semantics.

## Recommended v1.1 distribution
- One Skill: project `.github/skills/` or `.agents/skills/`, or a documented personal Skill root.
- Portable bundle: generated Agent Plugin v1 package.
- Use Copilot-specific agents/hooks/LSP/MCP only in a host wrapper when needed; do not add them to the canonical research core.

Verify `/skills list` / plugin component discovery in the actual CLI before claiming runtime success.

## Superpowers
Superpowers upstream documents GitHub Copilot CLI support. If installed, use it as an optional engineering workflow layer; do not duplicate planning/TDD/debugging/review instructions.

## MCP stack
Use `core/mcp-stack.md`; prefer native capability first and enable only task-matched, trusted servers.


<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `github-copilot`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `no`
- **Native activation equivalent:** /skick
- **Surfaces covered:** GitHub cloud agent, code review, Copilot CLI, Copilot app, VS Code agent mode, JetBrains agent mode
- **Availability / gating:** Agent Skill availability varies by Copilot surface and plan. For example, Copilot code-review Skills are currently generally available to Copilot Pro, Pro+, Business, and Enterprise users; other Copilot agent surfaces have their own eligibility/limits.
- **Preferred install:** Prefer project .github/skills/skick or .agents/skills/skick; use ~/.copilot/skills/skick or ~/.agents/skills/skick for personal scope. GitHub CLI 2.90+ can preview/install/update Skills with gh skill.
- **Project/local destinations:** `.github/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`
- **User/personal destinations:** `~/.copilot/skills/skick/`, `~/.agents/skills/skick/`
- **Prebuilt distribution when applicable:** `shared-agent-skill.zip`

### GitHub source fast path

- gh skill preview SWEHULYADAV/SKick skick
- gh skill install SWEHULYADAV/SKick skick
- gh skill update skick

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

1. Confirm SKick is discovered by the active Copilot surface.
2. For Copilot CLI, reload skills when needed and verify the discovered list.

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

https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

<!-- SKICK-AI-INSTALL-END -->
