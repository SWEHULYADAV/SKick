# BrowserCode Adapter — VERIFIED VIA OPEN-CODE INHERITANCE

BrowserCode is a browser-native coding agent built as a fork of OpenCode. Its repository contains `.opencode/skills/*/SKILL.md`, and its README identifies OpenCode as the upstream coding-agent core. This supports an OpenCode-compatible SKick installation path for current BrowserCode builds, but runtime discovery must still be tested after installation because BrowserCode can diverge from upstream.

## Install SKick

Project scope:

```text
.opencode/skills/skick/
```

Shared project scope when supported by the installed build:

```text
.agents/skills/skick/
```

User scope inherited from OpenCode:

```text
~/.config/opencode/skills/skick/
~/.agents/skills/skick/
```

Copy the complete SKick directory.

## Browser-aware usage

BrowserCode adds a persistent browser/CDP primitive. When SKick is active and the task involves a web application, combine the normal SKick research/build/debug flow with `core/webapp-validation.md`; browser access is a capability, not a replacement for the skill workflow.

## Call SKick

Use `Use SKick to ...` or a request matching the SKick description.

## Verify

1. Start BrowserCode (`bcode`) or the active BrowserCode surface.
2. Confirm SKick is available to the agent.
3. Run a low-risk task and verify that SKick instructions are loaded.
4. For browser work, verify BrowserCode's browser primitive independently from skill discovery.

## Sources

- https://github.com/browser-use/browsercode
- https://opencode.ai/docs/skills

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `browsercode`
- **Support status:** `VERIFIED_INHERITED_OPENCODE`
- **Surfaces covered:** BrowserCode CLI/TUI, headless BrowserCode runs, browser-native coding-agent sessions
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** BrowserCode is a fork of OpenCode and its repository contains .opencode/skills/*/SKILL.md. Install SKick using the OpenCode-compatible skill roots, then verify discovery in the installed BrowserCode build.
- **Project/local destinations:** `.opencode/skills/skick/`, `.agents/skills/skick/`
- **User/personal destinations:** `~/.config/opencode/skills/skick/`, `~/.agents/skills/skick/`
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

1. Start BrowserCode (`bcode`) and verify SKick is visible/usable as a skill.
2. Run a low-risk browser-aware task and confirm SKick instructions are loaded before claiming successful installation.

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

https://github.com/browser-use/browsercode

<!-- SKICK-AI-INSTALL-END -->
