# Qwen Code Adapter - VERIFIED; Qwen Web FALLBACK

## Qwen Code
Qwen Code supports Agent Skills under `.qwen/skills/` / `~/.qwen/skills/` and extension-provided skills. It also natively loads **Agent Plugins v1** packages with a root `plugin.json`, direct-child `skills/*/SKILL.md`, and supported MCP entries without rewriting the portable files.

Prefer the generated Agent Plugin v1 bundle when distributing v1.0 as a plugin. Use the plain Agent Skill when only the research methodology is needed.

## Qwen web/model-only surfaces
A model name is not a Skill runtime contract. If Qwen runs inside another host (Cursor, OpenCode, etc.), use that host adapter; otherwise use the generic prompt fallback.

## v1.0 preferred web profile
For ordinary new websites/web tools without a stronger existing-project constraint, preserve the canonical Python + vanilla profile: Python backend in `backend/`, semantic HTML/CSS/vanilla JS in `frontend/`, and a minimal root launcher such as `app.py`. Do not let host defaults auto-scaffold React/Next/Vite or a Node backend without a task-specific reason.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `qwen`
- **Support status:** `VERIFIED_HOST_SPLIT`
- **Surfaces covered:** Qwen Code CLI, Qwen Code editor integrations, Qwen model/web fallback
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use .qwen/skills/skick for project scope or ~/.qwen/skills/skick for personal scope; invoke explicitly with /skick when desired.
- **Project/local destinations:** `.qwen/skills/skick/`
- **User/personal destinations:** `~/.qwen/skills/skick/`
- **Prebuilt distribution when applicable:** `shared-agent-skill.zip`

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

1. Use the Qwen Code skills UI/command and test automatic activation; debug with the current runtime if discovery fails.

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

https://qwenlm.github.io/qwen-code-docs/en/users/features/skills

<!-- SKICK-AI-INSTALL-END -->
