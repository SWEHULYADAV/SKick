# Claude Web/App Adapter — VERIFIED

Claude supports custom Skill uploads.

## Upload shape
The ZIP must contain the skill folder as the top level, and that folder must contain lowercase `skill.md` plus resources. The generated Claude-web distribution converts only the entrypoint filename; canonical core content is unchanged.

## Install
Claude → Customize → Skills → + Create skill → Upload a skill → select the Claude-web ZIP.

## Serena
Do not assume the web surface exposes Serena/MCP. If it does, prefer Serena automatically; otherwise use Claude's available tools/files.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `claude-app`
- **Support status:** `VERIFIED`
- **Surfaces covered:** web, desktop/mobile app where custom Skills are available
- **Availability / gating:** Custom Skills are currently documented for Claude Free, Pro, Max, Team, and Enterprise users. Code execution must be enabled; some creation/recording surfaces have narrower plan/device availability.
- **Preferred install:** Upload claude-web-skill.zip through Customize > Skills > + Create skill > Upload a skill. The archive contains a top-level skick folder with lowercase skill.md.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `claude-web-skill.zip`

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

1. Confirm SKick is present/enabled in Claude Skills.
2. Invoke it on a low-risk research task.

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

https://support.claude.com/en/articles/12512180-use-skills-in-claude

<!-- SKICK-AI-INSTALL-END -->
