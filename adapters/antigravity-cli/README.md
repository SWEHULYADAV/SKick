# Antigravity CLI Adapter — VERIFIED DISTINCT RUNTIME

Antigravity CLI (`agy`) is not the same installation surface as the Antigravity visual Agent/IDE. Keep their Skill paths and packaging assumptions separate.

## Documented locations

- Workspace Skill root: `.agents/skills/`
- Global CLI Skill root: `~/.gemini/antigravity-cli/skills/`

The current CLI documentation demonstrates local Skills as Markdown files inside those roots and exposes them as slash commands. Because SKick is a multi-file Skill with supporting resources, do **not** assume a directory copy is equivalent unless the installed CLI version explicitly documents that capability.

## Safe SKick setup

1. Prefer the generic SKick prompt adapter (`../generic/PROMPT.md`) as a flattened CLI Skill when directory-form resources are not documented by the installed CLI.
2. If the target CLI version explicitly supports directory-form `SKILL.md` packages, follow that version's first-party instructions rather than this fallback.
3. Use `/skills` to confirm discovery before relying on SKick.
4. Do not generate or install an Antigravity plugin manifest from an undocumented schema. Plugin packaging must follow the current CLI plugin specification.

## Antigravity Agent/IDE

For the visual Agent/IDE, use `../antigravity/README.md`; that runtime documents directory-form Agent Skills at `.agents/skills/<skill-folder>/` and `~/.gemini/config/skills/<skill-folder>/`.

## Primary references

- https://antigravity.google/docs/cli/plugins/
- https://antigravity.google/docs/cli/gcli-migration/

## Warning

Do not silently run installer shell commands from documentation or third-party packages. Review the source and user intent before changing the host environment.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `antigravity-cli`
- **Support status:** `VERIFIED_DISTINCT_RUNTIME`
- **Surfaces covered:** terminal TUI
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Antigravity CLI uses workspace .agents/skills/ and global ~/.gemini/antigravity-cli/skills/ for CLI skills, but its documented local Skill examples are flat .md files. Use the adapter guidance and a deliberately flattened prompt for SKick unless the installed CLI version documents full directory-form Agent Skills; plugin packaging must follow the current Antigravity CLI plugin specification rather than guessed manifests.
- **Project/local destinations:** `.agents/skills/`
- **User/personal destinations:** `~/.gemini/antigravity-cli/skills/`
- **Prebuilt distribution when applicable:** `generic-prompt.md`

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

1. Run /skills and confirm the installed/flattened SKick command is visible before relying on it.

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

https://antigravity.google/docs/cli/plugins/

<!-- SKICK-AI-INSTALL-END -->
