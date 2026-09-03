# Continue Adapter — ECOSYSTEM-VERIFIED, RECHECK FIRST-PARTY DOCS

SKick is compatible with the Agent Skills ecosystem path(s) below for this runtime according to current cross-agent installer/compatibility data. Because this adapter is not marked first-party-verified, **re-check the installed runtime's own documentation before automating a global install or claiming permanent support**.

## Project paths

- `.continue/skills/skick/`

## User/global paths

- `~/.continue/skills/skick/`

## Safe install

1. Read `../../START_HERE.md` and `../../docs/WARNINGS.md`.
2. Confirm the active runtime really is **Continue**.
3. Prefer project scope unless the user explicitly wants a global install.
4. Copy the complete SKick directory into the selected skill root.
5. Reload/refresh the runtime when needed.
6. Verify that the runtime discovers `skick`; file presence alone is not enough.

## Fallback

If the installed release no longer recognizes these paths, do not invent a replacement. Check current first-party docs. If the runtime supports `.agents/skills/`, use that documented shared path. Otherwise use `../generic/PROMPT.md` for a session-level integration.

## Compatibility source

- https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html
- https://agentskills.io/home

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `continue`
- **Support status:** `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY`
- **Surfaces covered:** Continue
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use the Continue Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback.
- **Project/local destinations:** `.continue/skills/skick/`
- **User/personal destinations:** `~/.continue/skills/skick/`
- **Prebuilt distribution when applicable:** `runtime-skill.zip`

### GitHub source fast path

- No runtime-specific remote command is asserted. Fetch/inspect the GitHub source, then use the verified path/UI for this adapter.

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

1. Verify the active runtime discovers SKick after installation.
2. Re-check current first-party documentation before scripting installation for a release-sensitive environment.

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

https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html

<!-- SKICK-AI-INSTALL-END -->
