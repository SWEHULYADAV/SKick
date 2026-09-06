# AI Installation Protocol

This document defines how another AI/agent should install SKick when it receives the ZIP, unpacked source, or GitHub repository URL with little or no prior context.

## Objective

Turn a vague request such as **"install this ZIP"** into a safe, reproducible, platform-specific installation without guessing runtime contracts.

## Inputs

The installer may receive any of the following:

- canonical `skill.zip` / unpacked `skick/` directory;
- a generated platform distribution from `scripts/build_distributions.py`;
- a repository checkout/fork containing SKick;
- a public/private GitHub repository URL that the active environment is authorized to read;
- a ZIP attached inside a web/app AI surface with no direct filesystem install capability.

## GitHub repository source mode

When the input is a GitHub repository URL, read `../BOOTSTRAP_PROMPTS.md` and `GITHUB_BOOTSTRAP.md` before installation. Treat GitHub as source transport, not as the runtime. Inspect the repository identity/structure before executing anything, then detect the actual host and route through its manifest adapter.

Use a native remote-Skill command only when current first-party documentation for the active host confirms that repository-URL workflow. Otherwise fetch/clone to a reviewed location and use the verified filesystem or managed-import path.

The universal GitHub prompt authorizes SKick installation/update only. Optional semantic repository providers, plugins, MCPs, CLIs, credentials, and external Skills require a separate capability-fit and authorization decision.

## Phase 1 — Preflight

1. Inspect the archive tree without executing bundled code.
2. Locate the canonical package root. It must contain `SKILL.md`, `VERSION`, and `INSTALLATION_MANIFEST.json`.
3. Read `VERSION` and `INSTALLATION_MANIFEST.json`.
4. Read `docs/WARNINGS.md` before any write, plugin, MCP, credential, network, or executable action.
5. If the archive lacks the expected root files, stop and treat it as an unknown package rather than guessing that it is SKick.

## Phase 2 — Runtime detection

Identify the **runtime**, **surface**, **scope**, and **capabilities** separately.

### Runtime

Examples: ChatGPT, Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, OpenCode, Qwen Code, Kimi Code, ZCode, Mistral Vibe Code.

A model/provider name such as GLM, DeepSeek, MiniMax, LongCat, MiMo, Qwen, Kimi, or Claude does not by itself establish an installation path. The model may be running inside another host.

### Surface

Examples:

- web;
- desktop app;
- mobile app;
- CLI/TUI;
- VS Code extension;
- JetBrains extension;
- standalone IDE/editor;
- remote/SSH/container environment;
- managed enterprise/workspace environment.

### Scope

Prefer in this order unless the user requests otherwise:

1. project/repository-local;
2. user/personal;
3. organization/workspace/admin-managed;
4. system/global machine scope.

Project scope is preferred for coding repos because the installation is reviewable, version-controlled, and isolated.

### Capabilities

Determine whether the current agent can:

- read/write the target filesystem;
- access the project root;
- use the runtime's Skill/plugin manager;
- invoke an installation UI;
- restart/reload the runtime;
- run verification commands;
- access current first-party documentation.

Never claim an installation completed if the current environment cannot perform the required action.

## Phase 3 — Route through the manifest

Open `INSTALLATION_MANIFEST.json` and match the runtime using its canonical ID or aliases. Then open the referenced runtime README under `adapters/`.

Routing rules:

1. Explicit user runtime wins if it is internally consistent.
2. Runtime evidence from the environment wins over model/provider branding.
3. If several hosts are plausible, ask only for the missing discriminator.
4. If no native contract is verified, select `generic` rather than inventing an installation method.

## Phase 4 — Select install form

Use the least host-specific form that preserves correct behavior:

1. canonical Agent Skill directory when the host supports it;
2. shared `.agents/skills/` path when explicitly supported;
3. native host Skill path;
4. generated Agent Plugin v1 package when the host explicitly supports that standard;
5. generated host plugin wrapper when richer host packaging is required;
6. managed web/app upload/import UI;
7. generic prompt fallback only when no native contract is verified.

Do not install a plugin wrapper merely because one exists if a plain Skill is sufficient.

## Phase 5 — Safe write/update behavior

Before copying files:

1. Resolve the exact destination.
2. Check whether a `skick` installation already exists.
3. If none exists, create the parent Skill directory and copy the complete package.
4. If one exists, inspect its `VERSION`, git state if relevant, and local modifications.
5. Never merge two releases file-by-file. Replace the complete Skill only after preserving any intentional local fork changes.
6. For a fork, preserve fork-specific changes in source control and rebuild from the fork rather than hand-editing generated distributions.

Do not silently modify unrelated runtime configuration. If a runtime needs an enable switch, permission, plugin registration, or user consent, perform only what the environment safely supports and explain the rest.

## Phase 6 — Optional integrations

SKick can route to optional capabilities, but installation of SKick does not imply installation of those dependencies. The only packaged bootstrap exception is the explicit Serena authorization in `../BOOTSTRAP_PROMPTS.md`; outside that prompt, Serena remains opt-in like every other external dependency.

Examples include Serena, Context7, Playwright, Chrome DevTools, GitHub, Sentry, Superpowers, cloud/database tooling, research providers, security scanners, evaluation harnesses, and MCP servers.

For every optional dependency:

- confirm it is needed for the user's task;
- use current first-party installation documentation;
- inspect permissions and executable/network behavior;
- never place secrets in the SKick package;
- never run an unknown stdio command merely to learn what it does;
- verify the dependency independently after configuration.

## Phase 7 — Verification

A successful copy is not enough. Verify the runtime actually discovers SKick.

Minimum verification:

1. confirm `SKILL.md` exists at the intended target;
2. use the runtime's current Skill list/settings UI or discovery command when available;
3. confirm a Skill named `skick` is visible/enabled;
4. trigger a low-risk prompt such as `Use SKick to inspect this repository and explain the architecture before proposing changes.`;
5. confirm the runtime follows prompt-enhancement, best-capability routing, and research-before-plan-before-code where material;
6. for GitHub bootstrap, report whether canonical Serena was already available, configured, unsupported, or replaced by the semantic-code fallback;
7. record any reload/restart that was required.

For IDE extensions, verify in the extension's agent session, not only on disk.

## Phase 8 — Completion report

Tell the user:

- detected runtime and surface;
- installed SKick version;
- scope and destination or UI flow;
- whether an existing install was replaced/updated;
- verification performed and result;
- optional integrations that were intentionally not installed;
- any step that requires the user's UI/admin/authentication action.

## Failure behavior

If installation cannot be completed:

- do not fake success;
- preserve the archive and existing installation;
- explain the exact missing capability, permission, path, or runtime ambiguity;
- provide the smallest safe manual step required to continue.

## Security reminder

A Skill archive can contain instructions, scripts, and assets. Treat the archive itself as untrusted until inspected. SKick's own rules do not supersede the active runtime's system policies, user intent, organization policy, filesystem permissions, or safety controls.
