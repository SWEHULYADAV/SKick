# Roo Code Adapter — VERIFIED

Roo Code supports Agent Skills with progressive loading, Roo-specific skill roots, the shared `.agents/skills` convention, and optional mode-specific skill directories. SKick should normally stay in the generic skill root so all relevant modes can use it.

## Install SKick

Preferred project path:

```text
.roo/skills/skick/
```

Cross-agent project path:

```text
.agents/skills/skick/
```

Preferred global path:

```text
~/.roo/skills/skick/
```

Cross-agent global path:

```text
~/.agents/skills/skick/
```

Copy the complete SKick directory. A project skill overrides a global skill with the same name.

## Call SKick

Use natural language such as `Use SKick to debug this issue` or a request that clearly matches its description. Roo can auto-load relevant skills.

## Verify

Run a matching low-risk prompt and confirm Roo loads SKick. Do not treat file presence alone as proof of runtime discovery.

## Source

- https://roocodeinc.github.io/Roo-Code/features/skills/

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `roo-code`
- **Support status:** `VERIFIED`
- **Surfaces covered:** VS Code extension, Roo modes
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use .roo/skills/skick for project scope or ~/.roo/skills/skick for global scope; .agents/skills is also supported for cross-agent sharing.
- **Project/local destinations:** `.roo/skills/skick/`, `.agents/skills/skick/`
- **User/personal destinations:** `~/.roo/skills/skick/`, `~/.agents/skills/skick/`
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

1. Ask Roo for a task matching SKick and confirm the skill loads.
2. If using mode-specific skills, keep SKick in the generic skills root unless a deliberate mode override is desired.

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

https://roocodeinc.github.io/Roo-Code/features/skills/

<!-- SKICK-AI-INSTALL-END -->
