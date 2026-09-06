# Google Antigravity Agent/IDE Adapter — VERIFIED

This adapter covers the Antigravity visual Agent/IDE Skill system. Antigravity CLI is a distinct surface; use `../antigravity-cli/README.md` for CLI setup.

## Native Agent Skill locations

- Workspace: `.agents/skills/skick/`
- Global: `~/.gemini/config/skills/skick/`
- Backward-compatible workspace root documented by Antigravity: `.agent/skills/`

SKick uses the directory form with `SKILL.md` plus supporting resources.

## Install

Copy the complete SKick Skill folder into one documented root. Prefer workspace scope unless the user asks for a global install.

```bash
python3 scripts/install_skick.py --target antigravity --scope project --project /path/to/project --dry-run
```

Remove `--dry-run` only after reviewing the destination.

## Verify

Start/reload Antigravity and confirm SKick appears in the Skill inventory or is selected for an explicit low-risk prompt such as `Use SKick to review this project plan.`

## Optional integrations

MCP servers, browser tools, GitHub access, Serena, cloud tooling, and other integrations are separate. Never install or authenticate them silently while installing SKick.

## Primary reference

https://antigravity.google/docs/skills/

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `antigravity`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `no`
- **Native activation equivalent:** /skick
- **Surfaces covered:** Antigravity visual agent/IDE
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use <workspace>/.agents/skills/skick for workspace scope or ~/.gemini/config/skills/skick for global scope. Do not use a fabricated plugin manifest.
- **Project/local destinations:** `.agents/skills/skick/`
- **User/personal destinations:** `~/.gemini/config/skills/skick/`
- **Prebuilt distribution when applicable:** `shared-agent-skill.zip`

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

1. Confirm SKick appears in the Antigravity skill inventory or is selected automatically for a matching low-risk prompt.

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

https://antigravity.google/docs/skills/

<!-- SKICK-AI-INSTALL-END -->
