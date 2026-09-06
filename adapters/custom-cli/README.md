# Custom CLI / API Orchestrator — GENERIC FALLBACK

Use `../generic/PROMPT.md` as the system/project instruction and expose the canonical `core/` files through the orchestrator's file/context mechanism.

Map runtime tools to the abstract capabilities in `core/runtime-and-capabilities.md`. If MCP/semantic tooling is supported, expose the capabilities and let SKick route to the best observed provider by fit.

Do not encode model-specific logic unless the runtime requires it.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `custom-cli`
- **Support status:** `GENERIC_PROMPT_FALLBACK`
- **Verification status:** `GENERIC_PROMPT_FALLBACK`
- **Runtime tier:** `prompt_fallback`
- **Native Skill support:** `unknown`
- **Literal `@SKick`:** `unknown`
- **Native activation equivalent:** Attach or paste the SKick prompt/context in the active host.
- **Surfaces covered:** custom CLI/harness
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** If the host supports Agent Skills, map SKick to its verified skill root. Otherwise inject the generic prompt adapter and preserve canonical files as reference resources.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `generic-prompt.md`

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

1. Document the host contract and test discovery before calling it supported.

### Availability and limitations

- No native persistent Skill mechanism is claimed for this generic route.

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

https://agentskills.io/

<!-- SKICK-AI-INSTALL-END -->
