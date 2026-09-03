# Gemini CLI Adapter — VERIFIED

## Native options
- Project Skill: `.gemini/skills/skick/` or `.agents/skills/skick/`.
- User Skill: `~/.gemini/skills/skick/` or `~/.agents/skills/skick/`.
- Extension: root `gemini-extension.json` plus `skills/skick/`.

Install/link with current `gemini skills` or `gemini extensions` commands, then verify with `/skills list` or `/extensions list`.

## Serena
Gemini CLI is a documented Serena MCP client. Prefer Serena automatically when connected.

## Superpowers
Superpowers upstream documents a Gemini CLI extension path. If installed, use it for matching engineering workflows while SKick owns research/evidence/tool routing.

## MCP stack
Use `core/mcp-stack.md`; prefer native capability first and enable only task-matched, trusted servers.


## v1.0 design/motion/3D
Use the canonical cross-platform design orchestration. Claude-oriented upstream design skills are optional reference material only; do not fabricate Claude marketplace commands for this host. Resolve current project libraries and official APIs, preserve reduced-motion/performance budgets, and use the host's strongest rendered/browser validation path.

## v1.0 preferred web profile
For ordinary new websites/web tools without a stronger existing-project constraint, preserve the canonical Python + vanilla profile: Python backend in `backend/`, semantic HTML/CSS/vanilla JS in `frontend/`, and a minimal root launcher such as `app.py`. Do not let host defaults auto-scaffold React/Next/Vite or a Node backend without a task-specific reason.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `gemini-cli`
- **Support status:** `VERIFIED`
- **Surfaces covered:** CLI/TUI, terminal integrations
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Prefer `gemini skills install <source> --scope workspace|user` or the documented .gemini/skills / .agents/skills discovery roots; use /skills reload after local changes when needed.
- **Project/local destinations:** `.agents/skills/skick/`, `.gemini/skills/skick/`
- **User/personal destinations:** `~/.agents/skills/skick/`, `~/.gemini/skills/skick/`
- **Prebuilt distribution when applicable:** `shared-agent-skill.zip`

### GitHub source fast path

- gemini skills install <GITHUB_REPO_URL> --scope workspace
- /skills reload
- /skills list

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

1. Use /skills list or gemini skills list --all.
2. Reload/refresh skills after changes and confirm SKick is enabled.

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

https://geminicli.com/docs/cli/skills/

<!-- SKICK-AI-INSTALL-END -->
