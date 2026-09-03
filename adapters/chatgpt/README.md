# ChatGPT Adapter — VERIFIED

## Native format
Use the package root as an Agent Skill: `SKILL.md` plus the canonical `core/` resources.

## Install
1. Package the Skill as `skill.zip` with the official Skill validator/packager.
2. In ChatGPT, open Plugins → Skills → Create → Upload from your computer.
3. Keep the archive structure intact so progressive `core/` references resolve.
4. Workspace/admin availability can vary by plan and policy; do not assume every account exposes Skill upload.

## Serena
If the current ChatGPT/Codex environment exposes Serena through MCP or another supported connection, prefer Serena automatically for semantic repository operations. Otherwise fall back without blocking the workflow.

## Test
Use a current-version technical research prompt, then a repository prompt that asks for symbols/references and verify Serena is preferred when connected.


## v1.0 design/motion/3D
Use the canonical cross-platform design orchestration. Claude-oriented upstream design skills are optional reference material only; do not fabricate Claude marketplace commands for this host. Resolve current project libraries and official APIs, preserve reduced-motion/performance budgets, and use the host's strongest rendered/browser validation path.

## v1.0 preferred web profile
For ordinary new websites/web tools without a stronger existing-project constraint, preserve the canonical Python + vanilla profile: Python backend in `backend/`, semantic HTML/CSS/vanilla JS in `frontend/`, and a minimal root launcher such as `app.py`. Do not let host defaults auto-scaffold React/Next/Vite or a Node backend without a task-specific reason.

<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `chatgpt`
- **Support status:** `VERIFIED`
- **Surfaces covered:** web, desktop, mobile/web-mobile
- **Availability / gating:** Native custom Skill creation/upload is currently documented for eligible ChatGPT Business, Enterprise, Healthcare, and Edu workspaces, subject to workspace settings and product availability. Do not assume Plus/Pro/Free expose the same managed Skill UI.
- **Preferred install:** Upload canonical skill.zip through Plugins > Skills > Create > Upload from your computer.
- **Project/local destinations:** No filesystem project path is asserted for this surface.
- **User/personal destinations:** No filesystem personal path is asserted for this surface.
- **Prebuilt distribution when applicable:** `skill.zip`

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

1. Confirm SKick appears in Skills as installed/enabled.
2. Run a low-risk prompt that clearly matches the SKick description.

### Availability and limitations

- Managed ChatGPT Skill availability is plan/workspace/surface dependent.
- Codex has separate Skill support and plan availability; do not infer Codex eligibility from the ChatGPT managed-Skill gate.

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

https://help.openai.com/en/articles/20001066

<!-- SKICK-AI-INSTALL-END -->
