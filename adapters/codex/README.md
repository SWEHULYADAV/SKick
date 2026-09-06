# Codex Adapter — VERIFIED

## Native options
- Shared/distributable: Codex plugin with `.codex-plugin/plugin.json` and bundled `skills/`.
- Project/user Agent Skill: place `skick/` under a documented `.agents/skills/` location.
- `AGENTS.md` is only a thin project bridge; never duplicate the core there.

## Engineering orchestration
If the official Superpowers plugin is installed, let relevant Superpowers skills own brainstorming/planning/TDD/debugging/subagent/review phases while SKick supplies research, evidence, versions, safety, MCP routing and final verification. Do not duplicate both methodologies at full detail.


## MCP stack
For optional MCPs, select by capability and task fit: a semantic repository provider for code intelligence, a current-doc provider when needed, and the smallest capable browser tool for browser work. Add GitHub/Sentry only when project/auth context requires them. Verify the installed Codex build before adding remote HTTP MCPs because transport/config support has changed across releases. Use `/mcp`/`codex mcp list` or the current equivalent to verify connectivity.

## Test
Restart/reload after installation, verify skill/plugin + relevant MCPs are discovered, then run a repository bug investigation and a targeted test-backed edit.

## v1.1 specialist/harness routing
When installed and task-matched, Codex may use official/provider specialists such as Hugging Face Skills, AWS Agent Toolkit plugins, Codex Security, CodeRabbit or other narrow skills while SKick remains the control plane. External mini-SWE/Open SWE/Pydantic/Symphony harnesses are optional references/runtimes, not nested automatically inside a normal Codex run. For benchmark work, Inspect/Harbor adapters must preserve model/runtime/tool-policy and task/scorer/container versions.

Qualify downloaded skills and unfamiliar MCPs before activation; prefer the bundled local static preflight and isolated MCP Inspector flow. Do not execute an unknown stdio config simply to discover its tools.



<!-- SKICK-AI-INSTALL-BEGIN -->
## Direct ZIP / AI installer contract

When an AI receives the SKick ZIP and the user says **"install this"**, use this adapter only after identifying the actual runtime/surface from environment evidence or the user's explicit target.

- **Manifest platform ID:** `codex`
- **Support status:** `DOC_VERIFIED`
- **Verification status:** `DOC_VERIFIED`
- **Runtime tier:** `full_runtime`
- **Native Skill support:** `yes`
- **Literal `@SKick`:** `no`
- **Native activation equivalent:** $skick
- **Surfaces covered:** CLI, app, IDE extension
- **Availability / gating:** Codex is currently included across ChatGPT Free, Go, Plus, Pro, Business, Edu, and Enterprise plans; limits vary by plan. This is separate from native Skill upload availability in ChatGPT chat.
- **Preferred install:** Prefer repository/user Agent Skill scope for a standalone SKick install; use codex-plugin.zip only for Codex plugin distribution.
- **Project/local destinations:** `.agents/skills/skick/`
- **User/personal destinations:** `~/.agents/skills/skick/`
- **Prebuilt distribution when applicable:** `codex-plugin.zip`

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

1. Confirm SKick appears in the Codex skill selector/list.
2. If a change is not detected, restart/reload Codex and re-check.

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

https://learn.chatgpt.com/docs/build-skills

<!-- SKICK-AI-INSTALL-END -->
