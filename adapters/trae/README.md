# TRAE Adapter — VERIFIED PRODUCT/ECOSYSTEM PATHS

TRAE exposes Skills as `SKILL.md` instruction packages and supports project-level skill folders. Current TRAE editions/surfaces can differ in global-path and UI behavior, so distinguish TRAE international, TRAE CN, standalone IDE, and plugin surfaces before a global installation.

## Install SKick

Project scope:

```text
.trae/skills/skick/
```

Common global roots:

```text
~/.trae/skills/skick/
~/.trae-cn/skills/skick/   # TRAE CN where documented by the installed edition
```

Some releases also expose `Settings -> Skills & Commands -> Create/Import`; prefer the live product UI when the filesystem surface is not writable or when account/workspace policy controls Skills.

## Call SKick

Use natural language such as `Use SKick to review this project` or a task matching the SKick description. TRAE may also auto-load relevant Skills.

## Verify

Reload/refresh skill discovery when required, then confirm SKick is actually invoked on a low-risk task.

## ByteDance / model note

Do not treat a ByteDance/Doubao/Seed model name as an install surface. If that model is running in TRAE, use this adapter. If it runs in another host, use that host's adapter.

## Sources

- https://www.trae.ai/
- https://forum.trae.cn/t/topic/67755

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `trae`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `unknown`
- **Native activation equivalent:** Use the host skill picker or documented native Skill mechanism.
- **Surfaces covered:** TRAE IDE, TRAE SOLO, TRAE VS Code/plugin-style surfaces where Skills are exposed
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Prefer the current TRAE Skills UI or the cross-agent project root `.agents/skills/skick/`, which current first-party release notes explicitly support. Treat product-specific global filesystem roots as version-sensitive unless the installed TRAE release documents them.
- **Project/local destinations:** `.agents/skills/skick/`
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

1. Refresh/reload TRAE skill discovery or use the Skills/Commands UI.
2. Invoke SKick by name or run a matching task and confirm the runtime loads the skill rather than only copying files.

### Availability and limitations

- Current first-party evidence supports Agent Skills and `.agents/skills` project loading, but this audit did not establish a stable product-specific global filesystem path.

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

https://www.trae.ai/changelog

<!-- SKICK-AI-INSTALL-END -->
