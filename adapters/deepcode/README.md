# Deep Code Adapter — VERIFIED WITH PROVIDER WARNING

Deep Code is a third-party coding-agent integration documented by DeepSeek. Treat Deep Code runtime support separately from the DeepSeek model/API itself.

## Install locations

- Project: `.deepcode/skills/skick/`
- Personal/shared Agent Skill: `~/.agents/skills/skick/`

Copy the complete SKick directory so `SKILL.md` can resolve its `core/`, `docs/`, scripts, and references. The SKick installer helper supports this runtime as `--target deepcode`.

## Verify

1. Reload/restart the actual Deep Code host if required by its version.
2. Confirm SKick is discovered by the host.
3. Run a low-risk explicit call such as `Use SKick to review this repository structure.`
4. Do not treat selecting a DeepSeek model as proof that the host loaded SKick.

## Update/remove

Inspect `VERSION` and local modifications before replacing an existing install. Replace the complete Skill directory rather than mixing files from releases.

## Primary reference

https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode

## Warning

DeepSeek's integration page identifies Deep Code as a third-party tool. Re-check the installed Deep Code version and its own documentation before automating installation or write actions.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `deepcode`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `no`
- **Native activation equivalent:** /skick
- **Surfaces covered:** Deep Code CLI, Deep Code VS Code extension
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use project .deepcode/skills/skick or the documented shared personal Agent Skill path. DeepSeek documentation identifies Deep Code as a third-party integration, so verify the installed Deep Code version before automation.
- **Project/local destinations:** `.deepcode/skills/skick/`
- **User/personal destinations:** `~/.agents/skills/skick/`
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

1. Confirm SKick is discovered by the actual Deep Code host; do not treat selecting a DeepSeek model as proof of Skill support.

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

https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode

<!-- SKICK-AI-INSTALL-END -->
