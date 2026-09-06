# Crush Adapter — VERIFIED

Crush supports the Agent Skills format and discovers project/global Skill roots documented by the current Charmbracelet runtime. Prefer a project-local Skill root for repository work and preserve the complete SKick directory.

Use the native Skill discovery/invocation behavior to verify the install. Serena is separate; configure it only when explicitly authorized and when the active Crush tooling can expose the required semantic/MCP capability.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `crush`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `unknown`
- **Native activation equivalent:** Use the host skill picker or documented native Skill mechanism.
- **Surfaces covered:** CLI/TUI coding agent
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Prefer .crush/skills/skick or .agents/skills/skick for project scope; use current documented global Skill roots only for personal scope.
- **Project/local destinations:** `.crush/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`, `.cursor/skills/skick/`
- **User/personal destinations:** `~/.config/crush/skills/skick/`, `~/.agents/skills/skick/`, `~/.claude/skills/skick/`
- **Prebuilt distribution when applicable:** `shared-agent-skill.zip`

### GitHub source fast path

- Fetch/inspect the repository, then copy the complete Skill to the selected verified Crush/shared project root.

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

1. Confirm SKick appears in Crush native Skill discovery/invocation.
2. Run a low-risk explicit SKick trigger.

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

https://github.com/charmbracelet/crush

<!-- SKICK-AI-INSTALL-END -->
