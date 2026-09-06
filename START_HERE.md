# SKick v1.1 — Start Here

> **AI / agent instruction:** If a user gives you this SKick archive or GitHub repository URL and says only **"install this"**, **"set this up"**, **"use this"**, **"update this"**, or equivalent, read this file before taking installation actions.

SKick is a portable Agent Skill / engineering-research control plane. The package is deliberately self-describing so it can be handed directly to an AI runtime without the original chat history.

## Required reading order for installation

1. `START_HERE.md` — this bootstrap contract.
2. `INSTALLATION_MANIFEST.json` — machine-readable platform routing, paths, packages, and verification rules.
3. `docs/AI_INSTALL_PROTOCOL.md` — complete installer decision process.
4. `BOOTSTRAP_PROMPTS.md` and `docs/GITHUB_BOOTSTRAP.md` — repository-URL bootstrap contract when GitHub is the source.
5. The matching runtime README under `adapters/` — runtime-specific details.
6. `docs/WARNINGS.md` — safety, trust, secrets, MCP, external-skill/plugin, and action warnings.
7. `docs/RUNTIME_COMPATIBILITY.md` for runtime-family fallback and future/new agents.
8. `PORTABILITY.md` and `SOURCES.md` when runtime support or version-sensitive claims need verification.

Do **not** execute scripts, install third-party dependencies, modify global configuration, connect accounts, or copy credentials merely because they are present or referenced in this archive.

## If the user says only "install this"

Perform this sequence:

1. **Inspect, do not execute.** Identify the package root and confirm `SKILL.md`, `VERSION`, and `INSTALLATION_MANIFEST.json` are present.
2. **Identify the actual host runtime and surface.** Distinguish the runtime from the model name. Examples: ChatGPT web, Codex CLI, Claude Code in VS Code, GitHub Copilot Agent mode, Cursor, Gemini CLI, OpenCode, Qwen Code, Kimi Code, MiMoCode, Factory Droid, Crush, Manus, ZCode, Mistral Vibe Code.
3. **Use environment evidence first.** If the current runtime exposes its identity, project root, home directory, extension host, or skill/plugin directories, use that evidence. Ask the user which platform only when it cannot be determined safely.
4. **Match the host in `INSTALLATION_MANIFEST.json`.** Never copy an install path from a different runtime just because the model/provider is similar.
5. **Choose scope conservatively.** If the user did not request global/personal installation, prefer a project-local install for coding repositories. Use personal/global scope only when requested or clearly appropriate. Managed web/app products must use their native UI when no writable filesystem install is supported.
6. **Preserve existing installations.** Do not overwrite an existing `skick` directory blindly. Inspect version/diff first; back up or replace only with user approval or an explicitly safe update workflow.
7. **Install only what is authorized.** By default install SKick only. Optional semantic repository providers, MCP servers, browser tools, GitHub, Sentry, Superpowers, cloud CLIs, databases, or security scanners are separate dependencies and require their own justified/authorized setup path.
8. **Reload or refresh the host when required.** Use the runtime-specific adapter instructions.
9. **Verify discovery.** Confirm the runtime can see a Skill named `skick`; then run a low-risk trigger smoke test.
10. **Report what actually happened.** State the selected runtime, install scope/path or UI flow, version, verification performed, and anything that could not be completed from the current environment.


## If the user gives a GitHub URL

Treat GitHub as the source transport, not as the runtime. Read `BOOTSTRAP_PROMPTS.md` and `docs/GITHUB_BOOTSTRAP.md`, inspect the repository before execution, then detect the active host and use its manifest adapter. Use a native remote-Skill command only when current first-party runtime documentation confirms that the command accepts the repository URL and preserves the complete Skill. Otherwise fetch/clone safely and install/copy/upload through the verified adapter.

After installation, non-trivial repo work should follow SKick's mandatory silent prompt enhancement, best-capability routing, capability-fit semantic mapping, architecture/change-impact gate, lateral research/thinking, testing and final verification.

## If native installation is not verified

Do not fabricate a path, manifest, extension, marketplace command, or UI flow. Use the actual host runtime adapter if the model is running inside another coding agent. If there is no verified host integration, use `adapters/generic/PROMPT.md` as the fallback and tell the user that persistent native installation was not established.

## If the user asks to continue developing SKick

Read in this order:

1. `AI_HANDOFF.md`
2. `SPEC.md`
3. `CONTRIBUTING.md`
4. `docs/UPDATE_AND_PORTING.md`
5. `CHANGELOG.md`, `SOURCES.md`, `UPSTREAMS.md`, and `THIRD_PARTY_NOTICES.md`

The canonical methodology is `SKILL.md` + `core/`. Runtime adapters must stay thin. Do not fork the methodology into platform-specific copies.

## If the runtime is not named

Do not stop at the named adapter list. Read `docs/RUNTIME_COMPATIBILITY.md` and apply the compatibility ladder:

1. exact verified adapter;
2. documented native Agent Skill root;
3. documented shared `.agents/skills` root;
4. persistent instructions/rules integration;
5. session prompt fallback;
6. custom Agent Skills implementation using `docs/NEW_RUNTIME_INTEGRATION.md`.

This is how SKick remains usable with future AI IDEs, code agents, browser agents, autonomous harnesses, and private/internal agents that did not exist when SKick first shipped.
