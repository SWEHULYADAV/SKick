# Manus Adapter — VERIFIED MANAGED IMPORT

Manus exposes portable Skills through its managed Skill workflow. Do not invent a local filesystem path for Manus. Use the product's current import/share/upload controls and the distribution named by `INSTALLATION_MANIFEST.json`.

If the active Manus surface cannot fetch a GitHub repository directly, use the validated generated Skill archive through the UI. Runtime verification means the imported Skill is enabled/discoverable and can pass a low-risk trigger test.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `manus`
- **Support status:** `VERIFIED_MANAGED_IMPORT`
- **Surfaces covered:** managed Manus Skill surfaces
- **Availability / gating:** Availability, plan, region, and admin policy can vary; re-check current first-party documentation for this surface.
- **Preferred install:** Use Skills > + Add > Import from GitHub for a public SKick repository URL, or Upload a skill for the validated archive/folder. Do not assert a filesystem path.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `skill.zip`

### GitHub source fast path

- Open Skills > + Add > Import from GitHub.
- Paste <GITHUB_REPO_URL>.
- Confirm SKick is imported/enabled and run a low-risk trigger test.

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

1. Confirm SKick is imported/enabled in the Manus Skills surface.
2. Run a low-risk trigger test and distinguish UI import success from external tool availability.

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

https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus

<!-- SKICK-AI-INSTALL-END -->
