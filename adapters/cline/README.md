# Cline Adapter — VERIFIED

Cline supports Agent Skills as on-demand folders containing `SKILL.md` and optional resources. Skills may be created from the Skills UI or installed manually. Some Cline releases expose Skills behind a feature toggle, so confirm the feature is enabled before diagnosing discovery failures.

## Install SKick

Project/workspace scope:

```text
.cline/skills/skick/SKILL.md
```

Global/user scope:

```text
~/.cline/skills/skick/SKILL.md
```

Copy the **complete SKick directory**, not only `SKILL.md`, because SKick references supporting `core/`, `docs/`, `adapters/`, `scripts/`, and other resources.

## Call SKick

Cline can auto-select a skill from its description. Explicit invocation is also supported through slash commands when the skill is enabled. Use `/skick` where the active Cline release exposes the skill command, or say `Use SKick to ...`.

## Verify

1. Open Cline's Skills menu and confirm `skick` is discovered and enabled.
2. Ask a low-risk matching task such as `Use SKick to review this repository structure.`
3. Confirm Cline actually activates the skill before claiming installation succeeded.

## Update / remove

Inspect local changes before replacing the complete `skick` directory. Remove the directory or use the current Skills UI to disable/delete it.

## Source

- https://docs.cline.bot/customization/skills
- https://github.com/cline/skills

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `cline`
- **Support status:** `VERIFIED`
- **Surfaces covered:** VS Code extension, Cline agent surfaces
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Enable Skills in Cline when required, then install project-local at .cline/skills/skick or global at ~/.cline/skills/skick. Cline also supports explicit slash-command invocation for enabled skills.
- **Project/local destinations:** `.cline/skills/skick/`
- **User/personal destinations:** `~/.cline/skills/skick/`
- **Prebuilt distribution when applicable:** `runtime-skill.zip`

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

1. Confirm SKick appears in the Cline Skills menu and is enabled.
2. Invoke `/skick` or a matching low-risk prompt and confirm use_skill loads it.

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

https://docs.cline.bot/customization/skills

<!-- SKICK-AI-INSTALL-END -->
