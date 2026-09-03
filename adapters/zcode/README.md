# ZCode Adapter - VERIFIED

## Native Skill
ZCode Agent user skills live at `~/.zcode/skills/<skill-name>/SKILL.md`. ZCode can also import skills from supported external agent installations through Settings -> Skills.

## Native plugin
For reusable bundles, ZCode recommends `.zcode-plugin/plugin.json`; plugins may bundle `skills/<name>/SKILL.md`, commands, subagents, hooks, MCP servers, and LSP configuration. ZCode plugin management is currently documented as Beta, so re-check the manifest docs before publishing a marketplace package.

Use the generated ZCode wrapper only for distribution. Keep all research methodology in the canonical Skill.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `zcode`
- **Support status:** `VERIFIED`
- **Surfaces covered:** ZCode Agent, remote/SSH/WSL workspaces
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use ~/.zcode/skills/skick for user scope or ZCode Settings > Skills import/copy/symlink flows for supported external/project installs; use the generated plugin for distributable bundles when appropriate.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** `~/.zcode/skills/skick/`
- **Prebuilt distribution when applicable:** `zcode-plugin.zip`

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

1. Open Settings > Skills, Refresh, and confirm SKick is enabled under the expected source.
2. For remote workspaces, verify the skill exists on the remote host or use the supported sync flow.

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

https://zcode-ai.github.io/zcode-docs/

<!-- SKICK-AI-INSTALL-END -->
