# Claude Code / IDE Adapter — VERIFIED

## Native options
- Standalone project Skill: `.claude/skills/skick/SKILL.md`.
- Reusable plugin: `.claude-plugin/plugin.json` plus `skills/skick/SKILL.md`.
- Local plugin testing: `claude --plugin-dir <plugin-directory-or-zip>` on supported versions.

The VS Code/JetBrains Claude Code integration uses the Claude Code runtime; use the same plugin/Skill package.

## Engineering orchestration
Superpowers is available through Claude Code's official plugin marketplace. When installed, use its narrower engineering workflows for design/planning/TDD/debugging/subagent/review phases and keep SKick responsible for research/evidence/versioning/safety/provenance.

## Serena
Claude Code is a documented Serena MCP client. Follow Serena's official Quick Start, prefer the `claude-code` Serena context, and use project-aware startup such as `--project-from-cwd` when appropriate. Serena's host context intentionally removes duplicate basic file/shell tools so semantic tools complement rather than replace Claude Code's native capabilities.

## MCP stack
Use task-matched MCPs: Context7 for current external docs; Playwright for browser automation; Chrome DevTools for deep network/console/performance diagnosis; GitHub/Sentry only when their project context is present. Treat authenticated browser/production/forge data as sensitive and use least privilege.

## v1.0 specialist/harness routing
Claude Code can compose SKick with installed Hugging Face, AWS/Vercel/security/review skills or other narrow specialists. Keep one workflow owner per phase; do not run Superpowers plus another full engineering methodology simultaneously. External evaluation/harness backends remain separate task environments rather than hidden nested control planes.

Qualify downloaded skills and unfamiliar MCPs before activation. Unknown stdio server commands require source/config review and sandboxed Inspector qualification; do not trust marketplace/catalog presence alone.

## v1.0 design-skill interoperability
`freshtechbro/claudedesignskills` may be used as an optional narrow Claude design specialist when its current marketplace/plugin path is verified. Do not make it a dependency of SKick. Preserve SKick's research-first stack selection, current official API checks, anti-slop QA, accessibility/performance budgets, and rendered verification.

## v1.0 preferred web profile
For ordinary new websites/web tools without a stronger existing-project constraint, preserve the canonical Python + vanilla profile: Python backend in `backend/`, semantic HTML/CSS/vanilla JS in `frontend/`, and a minimal root launcher such as `app.py`. Do not let host defaults auto-scaffold React/Next/Vite or a Node backend without a task-specific reason.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `claude-code`
- **Support status:** `VERIFIED`
- **Surfaces covered:** CLI, VS Code, JetBrains, Claude Code Desktop/local sessions
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use .claude/skills/skick for project scope, ~/.claude/skills/skick for personal scope, or the generated Claude Code plugin for shared/plugin distribution.
- **Project/local destinations:** `.claude/skills/skick/`
- **User/personal destinations:** `~/.claude/skills/skick/`
- **Prebuilt distribution when applicable:** `claude-code-plugin.zip`

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

1. Confirm the skill is visible/invocable in the active Claude Code session.
2. For plugin testing, use the runtime-supported local plugin load flow and reload plugins after changes.

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

https://code.claude.com/docs/en/slash-commands

<!-- SKICK-AI-INSTALL-END -->
