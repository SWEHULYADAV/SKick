# MiniMax Adapter — HOST-RUNTIME VERIFIED

MiniMax publishes an official Skills repository whose documented installation targets are host agents such as Claude Code, Cursor, Codex, and OpenCode. This is evidence that the portable unit is an Agent Skill consumed by the host runtime, not a MiniMax-model-specific Skill path.

Use the adapter for the host where the MiniMax model is running. For MiniMax web/chat without a verified custom Skill importer, use the generic prompt fallback.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `minimax`
- **Support status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces covered:** MiniMax models in host agents, web/model fallback
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** For MiniMax models inside another coding agent, install SKick into that actual host. MiniMax also has an evolving Code/Skills ecosystem; use a dedicated host route only after current first-party documentation establishes its exact discovery/install contract.
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
5. Do not silently install Serena, MCP servers, plugins, extensions, browser tooling, cloud CLIs, credentials, or other optional dependencies. The universal prompt in `../../BOOTSTRAP_PROMPTS.md` is an explicit exception only for canonical Serena setup; it does not authorize unrelated dependencies.
6. Reload/refresh/restart only as required by this runtime's documented behavior.
7. Verify discovery in the actual active surface, not only by checking that files exist.
8. Report the selected runtime, scope/path or UI flow, SKick version, verification performed, and any step that required user/admin/UI/authentication action.

### Verification

1. Verify the host runtime Skill installation; do not claim a MiniMax-specific path unless first-party docs establish one.

### Availability and limitations

- Do not invent .minimax/skills or another filesystem path solely from the provider/model name.

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

https://github.com/MiniMax-AI/skills

<!-- SKICK-AI-INSTALL-END -->
