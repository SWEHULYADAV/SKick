# Devin Adapter — VERIFIED_REPO

SKick uses the current first-party/evidence-backed Skill contract for **Devin**. Preserve the complete SKick directory and verify discovery in the active runtime; file presence alone is not a runtime test.

## Preferred scope

Project/repository paths:
- `.agents/skills/skick/`
- `.github/skills/skick/`
- `.claude/skills/skick/`
- `.cursor/skills/skick/`
- `.codex/skills/skick/`
- `.cognition/skills/skick/`
- `.windsurf/skills/skick/`

User/personal paths:
- No filesystem user path is asserted for this surface.

## Runtime notes

Commit the complete Skill at .agents/skills/skick in the repository. Devin also scans several compatible repository Skill roots, but .agents/skills is the recommended portable path.
- Current Devin Skills are repository-scoped; do not invent a global ~/.devin/skills route.
- Devin currently activates one Skill at a time; a new Skill replaces the active Skill.

## Source

- https://docs.devin.ai/product-guides/skills

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `devin`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `unknown`
- **Native activation equivalent:** Use the host skill picker or documented native Skill mechanism.
- **Surfaces covered:** Devin
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Commit the complete Skill at .agents/skills/skick in the repository. Devin also scans several compatible repository Skill roots, but .agents/skills is the recommended portable path.
- **Project/local destinations:** `.agents/skills/skick/`, `.github/skills/skick/`, `.claude/skills/skick/`, `.cursor/skills/skick/`, `.codex/skills/skick/`, `.cognition/skills/skick/`, `.windsurf/skills/skick/`
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `runtime-skill.zip`

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

1. Confirm Devin discovers the repository Skill after indexing/cloning or a branch rescan.
2. Invoke with a matching request or @skills:skick and verify only the intended Skill is active.

### Availability and limitations

- Current Devin Skills are repository-scoped; do not invent a global ~/.devin/skills route.
- Devin currently activates one Skill at a time; a new Skill replaces the active Skill.

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

https://docs.devin.ai/product-guides/skills

<!-- SKICK-AI-INSTALL-END -->
