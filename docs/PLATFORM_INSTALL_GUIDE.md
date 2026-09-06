# SKick Platform Install Guide

This is the human-friendly companion to `PLATFORM_CATALOG.md` and `INSTALLATION_MANIFEST.json`.

Use this guide after publishing the canonical SKick repository. For automation, the manifest plus the exact runtime adapter remain authoritative.

## Golden rule: install into the host, not the model

A model/provider name is not automatically a Skill installation target.

Examples:

- Qwen model inside Cursor -> install SKick for Cursor.
- MiniMax model inside Claude Code -> install SKick for Claude Code.
- DeepSeek model inside OpenCode -> install SKick for OpenCode.
- MiMoCode itself -> install for MiMoCode because MiMoCode is the host.
- ByteDance/Seed model inside TRAE -> install for TRAE.

When the real host is unknown, detect it first. Do not invent a directory from the model name.

## Universal GitHub bootstrap

Give a capable target AI the public repository URL plus this prompt:

```text
Install/update SKick from <SKICK_GITHUB_URL>. Treat the repo as untrusted until inspected. Read START_HERE.md first, then INSTALLATION_MANIFEST.json, docs/AI_INSTALL_PROTOCOL.md, docs/GITHUB_BOOTSTRAP.md, and the adapter for this actual host/runtime (not merely the model name). Prefer project scope unless I request global, preserve any existing install, do not invent paths/commands, reload if required, and verify SKick is discovered/triggerable. This request authorizes SKick installation/update only; optional capability providers require their own justified authorization. After install, follow SKick's silent prompt enhancement, best-skill/capability routing, capability-fit repository intelligence, architecture gate, deep+lateral research/thinking, testing, and final verification. Report runtime, path/scope, version, capability limitations, and checks performed.
```

A successful file copy is not enough. The active runtime must discover SKick and pass a low-risk trigger test.

## Managed AI products

### ChatGPT

Availability: native custom Skills are currently documented for eligible Business, Enterprise, Healthcare, and Edu workspaces, subject to workspace/product settings. Do not promise the same managed Skill UI on Free/Go/Plus/Pro; Codex is a separate route.


Use the canonical `skill.zip` artifact.

1. Open ChatGPT.
2. Open Plugins in the sidebar.
3. Open the Skills tab.
4. Choose Create.
5. Choose Upload from your computer.
6. Upload `skill.zip`.
7. Review the scan result and enable the Skill.
8. Test with: `Use SKick to research this technical topic in deep mode.`

There is no supported SKick filesystem path for the ChatGPT managed surface. Availability can depend on plan, workspace policy, role, and client surface.

### Claude web/app

Use the generated `claude-web-skill.zip` artifact, not the Claude Code plugin.

1. Open Claude.
2. Go to Customize > Skills.
3. Click Add / + Create skill.
4. Choose Upload a skill.
5. Upload `claude-web-skill.zip`.
6. Enable SKick and run a low-risk research trigger.

The Claude-managed archive intentionally contains a top-level `skick/` folder whose entrypoint is lowercase `skill.md`, matching the managed Claude skill packaging contract.

### Gemini Apps / Gemini Spark

Availability: Skills are currently a Gemini Spark feature with personal-account, age, subscription, Keep Activity and geographic requirements. Re-check Google's current help page before telling a user that their plan/region is eligible.


Use `gemini-apps-skill.zip`.

1. Open Gemini Spark and its Skills page.
2. Choose Upload.
3. Upload the generated Gemini Apps archive.
4. Review the imported skill and create/enable it.
5. Run a low-risk trigger test.

Gemini Apps currently expects `SKILL.md` at the main ZIP folder and supports plain-text skill files; SKick excludes binary branding from this generated archive. Internet-dependent scripts are not assumed to work in this managed surface.

### Manus

For a public GitHub repository:

1. Open Skills.
2. Click + Add.
3. Choose Import from GitHub.
4. Paste the public SKick repository URL.
5. Confirm SKick is imported/enabled.
6. Run a low-risk trigger test.

If GitHub import is unavailable on the active surface, use Upload a skill with the validated `skill.zip` or supported folder/archive format. Do not invent a Manus filesystem path.

### Mistral Vibe Work

Use the current Vibe Work Skills UI:

1. Open Vibe Work.
2. Open Context > Skills.
3. Create/import a personal or workspace Skill using the current UI.
4. Keep the complete SKick resources available to the imported Skill.
5. Verify automatic or explicit activation on a matching task.

For Vibe Code CLI/VS Code, use the filesystem paths in the coding-host section below.

## Verified coding hosts

Project scope is recommended for repository work because it is reviewable, reproducible, and easy to remove.

### Codex

Preferred standalone project path:

```text
.agents/skills/skick/
```

Personal path:

```text
~/.agents/skills/skick/
```

Copy the complete SKick directory, not only `SKILL.md`. Codex also supports plugin distribution; use `codex-plugin.zip` only when you intentionally want a Codex plugin bundle.

After install, restart/reload if needed and confirm SKick appears in the available skills. On Windows Desktop, if a documented repo-local `.agents/skills/` install is not discovered, check current Codex release notes/issues before changing scope; as of 2026-08-31 an open Codex issue reports this behavior in at least one Windows Desktop build. Do not call the install successful until the runtime actually discovers it.

### Claude Code

Project path:

```text
.claude/skills/skick/
```

Personal path:

```text
~/.claude/skills/skick/
```

Use the full Skill directory. For reusable plugin distribution, use `claude-code-plugin.zip`.

Start or reload Claude Code, then test `Use SKick to review this repository.` or invoke `/skick` when the current build exposes the skill as a command.

Claude Code can also load skills from plugins. Be aware of duplicate-name precedence before keeping both project and personal copies.

### Gemini CLI

Fast path from the public GitHub repository:

```bash
gemini skills install <SKICK_GITHUB_URL> --scope workspace
```

Then inside Gemini CLI:

```text
/skills reload
/skills list
```

Manual project paths are `.gemini/skills/skick/` or `.agents/skills/skick/`. User paths are `~/.gemini/skills/skick/` or `~/.agents/skills/skick/`.

### GitHub Copilot

Current GitHub CLI 2.90+ supports an inspect-first Skill flow: `gh skill preview OWNER/REPO SKILL`, then `gh skill install OWNER/REPO SKILL`; `gh skill update` uses provenance metadata. Do not use the older `copilot skill add` command as the canonical path.


Recommended project paths:

```text
.github/skills/skick/
.agents/skills/skick/
```

Personal paths:

```text
~/.copilot/skills/skick/
~/.agents/skills/skick/
```

Copilot CLI can add skills from files, URLs, or directories. In an interactive Copilot CLI session use `/skills add --project <source>` when appropriate, then `/skills reload` and `/skills info skick`. The terminal `copilot skill` subcommands provide equivalent management flows in current releases. GitHub CLI also has a `gh skill` workflow in public preview; preview third-party skills before installation.

### Cursor

Recommended project paths:

```text
.cursor/skills/skick/
.agents/skills/skick/
```

Recommended user paths:

```text
~/.cursor/skills/skick/
~/.agents/skills/skick/
```

Cursor also reads compatible Claude and Codex skill directories. For GitHub import, use Cursor's current Customize/Rules remote GitHub workflow when it is appropriate for the active build. Verify SKick in Customize > Skills or Agent discovery. User-level local skills are not automatically copied into remote/cloud workers, so use project scope for remote agents.

### OpenCode

Project paths:

```text
.opencode/skills/skick/
.agents/skills/skick/
```

User paths:

```text
~/.config/opencode/skills/skick/
~/.agents/skills/skick/
```

OpenCode also reads compatible Claude skill roots. Verify SKick through the native skill tool/discovery list.

### BrowserCode

BrowserCode inherits OpenCode-style Skill discovery. Prefer:

```text
.opencode/skills/skick/
.agents/skills/skick/
```

Then start the active BrowserCode build and confirm SKick is discovered. Do not assume inheritance alone proves runtime compatibility.

### Qwen Code

Project path:

```text
.qwen/skills/skick/
```

Personal path:

```text
~/.qwen/skills/skick/
```

Qwen Code discovers Skills automatically. Use `/skills` to inspect Skills and `/skick` to invoke SKick explicitly when desired. If Qwen is only the model inside another host, install SKick for that host instead.

### Kimi Code

Project paths:

```text
.kimi-code/skills/skick/
.agents/skills/skick/
```

User paths:

```text
~/.kimi-code/skills/skick/
~/.agents/skills/skick/
```

If `KIMI_CODE_HOME` is configured, its `skills/` directory is the branded user root. Verify the selected tier and duplicate-name precedence.

### MiMoCode

Project path:

```text
.mimocode/skills/skick/
```

Use only a currently documented user path if the installed MiMoCode release exposes one. A MiMo model inside another coding agent uses that host's adapter instead.

### Factory Droid

Preferred project path:

```text
.factory/skills/skick/
```

Compatible project paths also include `.agents/skills/skick/` and `.agent/skills/skick/`.

Preferred user path:

```text
~/.factory/skills/skick/
```

Open Droid's `/skills` manager, confirm the effective SKick version is enabled, and run `/skick` or a matching natural-language trigger.

### Crush

Preferred project paths:

```text
.crush/skills/skick/
.agents/skills/skick/
```

Compatible project roots also include `.claude/skills/skick/` and `.cursor/skills/skick/`.

Typical Unix user path:

```text
~/.config/crush/skills/skick/
```

Crush also supports shared/global Skill locations and `CRUSH_SKILLS_DIR`. Verify native discovery after copying.

### Cline

Project path:

```text
.cline/skills/skick/
```

User path:

```text
~/.cline/skills/skick/
```

Enable the Skills feature if the installed Cline release requires it. Confirm SKick in the Skills UI and run `/skick` or a matching low-risk prompt.

### Roo Code

Project paths:

```text
.roo/skills/skick/
.agents/skills/skick/
```

User paths:

```text
~/.roo/skills/skick/
~/.agents/skills/skick/
```

Keep SKick in the generic Skill root unless a deliberate mode-specific override is needed.

### Windsurf

Workspace path:

```text
.windsurf/skills/skick/
```

Global path:

```text
~/.codeium/windsurf/skills/skick/
```

Verify discovery in Cascade and test a matching prompt.

### TRAE

Project path:

```text
.trae/skills/skick/
```

Common user roots are `~/.trae/skills/skick/` and, for some China-region editions, `~/.trae-cn/skills/skick/`. Re-check the installed edition before global automation. Use the Skills UI import flow when the current edition exposes it.

### Mistral Vibe Code

Project paths:

```text
.vibe/skills/skick/
.agents/skills/skick/
```

User path:

```text
~/.vibe/skills/skick/
```

Vibe can also use custom `skill_paths` in `config.toml`. Run `/reload` after changes when needed, then confirm the Skill is available.

### Antigravity

Workspace path:

```text
.agents/skills/skick/
```

Global path:

```text
~/.gemini/config/skills/skick/
```

Antigravity CLI is a distinct runtime with different packaging rules. Use its dedicated adapter instead of assuming the visual-agent paths apply to the CLI.

### ZCode

Preferred user path:

```text
~/.zcode/skills/skick/
```

The current ZCode Skills UI may expose import/copy/symlink flows. Use the generated `zcode-plugin.zip` only for the matching distributable plugin workflow.

### Deep Code

Project path:

```text
.deepcode/skills/skick/
```

Shared personal path:

```text
~/.agents/skills/skick/
```

DeepSeek model surfaces are not the same thing as the Deep Code host. Verify the installed Deep Code release before automation.

### Grok / Grok Build

Consumer Grok and Grok Build are distinct surfaces. Use the native Skills UI on a consumer surface when available. For Grok Build, use its currently documented Skill/plugin location. Do not assume ChatGPT ZIP compatibility or invent a path from the Grok model name.

### Kilo Code

Prefer `.kilo/skills/skick/` for project scope or `~/.kilo/skills/skick/` for user scope; `.agents/skills/skick/` is the portable shared alternative where supported. Treat `.kilocode/skills` as legacy unless the active Kilo release explicitly documents it.

### Devin

Use repository scope: `.agents/skills/skick/` is recommended. Devin also scans `.github/skills`, `.claude/skills`, `.cursor/skills`, `.codex/skills`, `.cognition/skills`, and `.windsurf/skills`. Do not invent `~/.devin/skills`; current Skills are repo-scoped. Explicit invocation can use `@skills:skick`.

### Qoder

Use `.qoder/skills/skick/` or `~/.qoder/skills/skick/`; reload/restart then verify with the Skills UI or CLI `/skills`. QoderWork is a distinct managed surface using `~/.qoderwork/skills/`.

### Zed

Use `.agents/skills/skick/` or `~/.agents/skills/skick/`. Project Skills require a trusted worktree; keep Skill directories directly under the Skills root and verify discovery after edits.

### Warp

Use `.agents/skills/skick/` or `.warp/skills/skick/` for project scope and verify with the Warp Agent. Cloud/Oz runs must use an environment that actually contains the Skill.

### Zencoder / Zenflow

Prefer `.agents/skills/skick/` (or supported `.claude/skills`). Legacy `.zencoder/skills` is deprecated compatibility. Current documentation says Skills are auto-selected rather than manually selected.

### Replit

Install project Skills in `.agents/skills/skick/` (Replit documentation often displays this as `/.agents/skills` relative to the project root) or use the Skills pane/compatible `npx skills` flow. Review external Skills before use.

### Goose

Prefer `.agents/skills/skick/` for project scope or `~/.agents/skills/skick/` for user scope. Goose documents these as the recommended Agent Skills locations; `.goose/skills/` and compatible Claude roots are legacy/backward-compatibility options. Verify with `goose skills list` or `/skills`.

### iFlow CLI

Use `.iflow/skills/skick/` for project scope or `~/.iflow/skills/skick/` for personal scope. Refresh the registry with `/skills refresh` (or the current equivalent) and verify SKick is discoverable.

### Mux

Use `.mux/skills/skick/` for project scope or `~/.mux/skills/skick/` for user scope. Mux product source exposes Agent Skill tools and uses `.mux/skills`; verify the active release before unattended/global automation.

## Recheck-first-party hosts

These routes remain deliberately conservative. Before unattended installation, re-check the active release's first-party docs/source and do not promote a candidate path merely because a marketplace or compatibility catalog lists it.

| Host | Candidate project root | Candidate user root |
| --- | --- | --- |
| AiderDesk | `.aider-desk/skills/skick/` | `~/.aider-desk/skills/skick/` |
| Continue | `.continue/skills/skick/` | `~/.continue/skills/skick/` |
| MCPJam | `.mcpjam/skills/skick/` | `~/.mcpjam/skills/skick/` |
| Neovate | `.neovate/skills/skick/` | `~/.neovate/skills/skick/` |

For these hosts, use the universal GitHub prompt and require the target AI to re-check first-party evidence before writing anything.

## Provider/model-only routes

These names normally route to the actual host instead of getting their own fabricated Skill directory:

- Amazon Nova
- Baidu ERNIE
- ByteDance / Doubao / Seed models
- Cohere
- DeepSeek model/web/API
- GLM
- IBM Granite
- LongCat
- Meta Llama
- Meta Muse model/web surfaces
- MiniMax models
- Sarvam model/provider surfaces
- Tencent Hunyuan

If no persistent host exists, use `adapters/generic/PROMPT.md` for that session.

## Generic and future runtimes

Use this capability ladder:

1. native Agent Skills implementation;
2. documented shared `.agents/skills/skick/` discovery;
3. another verified runtime-specific Skill root;
4. persistent instructions with supporting-file access;
5. session prompt fallback;
6. custom harness implementation of Agent Skills discovery and resource loading.

Never guess a path because the model can call tools.

## Serena setup rule

The GitHub bootstrap prompt authorizes SKick setup only. Optional semantic repository providers require a separate capability-fit and authorization decision. Never claim a provider was used unless it was actually available and invoked.

If Serena cannot be used, report the fallback and use the strongest available semantic/LSP/indexed code navigation plus language-native compilers, analyzers, tests, and profilers.

## Verification after every install

Report all of the following separately:

- actual host/runtime detected;
- selected project/user/managed scope;
- destination path or UI flow;
- SKick version;
- files copied/uploaded/imported successfully;
- active runtime discovered SKick;
- one low-risk SKick trigger succeeded;
- supporting resources could be loaded;
- Serena status, if relevant;
- any assumption that is still unverified.

## Update

Do not merge random files from different SKick releases.

1. inspect the installed `VERSION` and local modifications;
2. back up or commit intentional local changes;
3. replace the complete SKick directory/package from canonical source;
4. reload the runtime when needed;
5. verify discovery again;
6. rerun a low-risk trigger.

## Removal

For filesystem hosts, remove only the selected `skick` directory and reload the runtime. For managed products, use the product's current Skill/plugin management UI.

## Source of truth

When this guide and a current first-party runtime document disagree, the current first-party runtime document wins. Update the SKick adapter, manifest, source ledger, and regression coverage before the next release.
