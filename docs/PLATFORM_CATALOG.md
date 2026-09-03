# SKick Platform Installation Catalog

This catalog is generated from `INSTALLATION_MANIFEST.json`. Use the matching adapter for detailed setup, verification, update/removal, and warnings. Re-check current first-party documentation before automating version-sensitive commands.

## How to use this catalog

1. Identify the actual host runtime, not only the model/provider name.
2. Match the runtime/alias below.
3. Open the linked adapter.
4. Prefer project scope when the user did not request global scope and the host supports project Skills.
5. Verify discovery in the active runtime surface after copying/uploading.

## Summary

| Runtime | Status | Availability / gating | Surfaces | Preferred form | Adapter |
|---|---|---|---|---|---|
| `aider-desk` | ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY | Host/plan/version dependent; see adapter. | AiderDesk | Use the AiderDesk Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback. | [`adapters/aider-desk/README.md`](../adapters/aider-desk/README.md) |
| `amazon-nova` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | Amazon Nova | Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `amp` | VERIFIED | Skill discovery is an Amp host capability; model/provider billing and account limits are separate from the Skill format. | Amp | Use .agents/skills/skick for project scope. For user/machine scope use ~/.config/agents/skills/skick or another path explicitly documented by the active Amp release. Amp can also add Skills from supported sources through its native skill commands. | [`adapters/amp/README.md`](../adapters/amp/README.md) |
| `antigravity` | VERIFIED | Host/plan/version dependent; see adapter. | Antigravity visual agent/IDE | Use <workspace>/.agents/skills/skick for workspace scope or ~/.gemini/config/skills/skick for global scope. Do not use a fabricated plugin manifest. | [`adapters/antigravity/README.md`](../adapters/antigravity/README.md) |
| `antigravity-cli` | VERIFIED_DISTINCT_RUNTIME | Host/plan/version dependent; see adapter. | terminal TUI | Antigravity CLI uses workspace .agents/skills/ and global ~/.gemini/antigravity-cli/skills/ for CLI skills, but its documented local Skill examples are flat .md files. Use the adapter guidance and a deliberately flattened prompt for SKick unless the installed CLI version documents full directory-form Agent Skills; plugin packaging must follow the current Antigravity CLI plugin specification rather than guessed manifests. | [`adapters/antigravity-cli/README.md`](../adapters/antigravity-cli/README.md) |
| `augment` | VERIFIED | Skill support is a host capability; Augment plan/usage limits and model-provider billing are separate from Skill discovery. | Augment | Use .augment/skills/skick for Augment-specific project scope or .agents/skills/skick for a portable project install; Augment also discovers compatible Claude Skill roots. Use the corresponding documented user roots for personal scope. | [`adapters/augment/README.md`](../adapters/augment/README.md) |
| `baidu-ernie` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | Baidu ERNIE | Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `browsercode` | VERIFIED_INHERITED_OPENCODE | Host/plan/version dependent; see adapter. | BrowserCode CLI/TUI, headless BrowserCode runs, browser-native coding-agent sessions | BrowserCode is a fork of OpenCode and its repository contains .opencode/skills/*/SKILL.md. Install SKick using the OpenCode-compatible skill roots, then verify discovery in the installed BrowserCode build. | [`adapters/browsercode/README.md`](../adapters/browsercode/README.md) |
| `bytedance-models` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | ByteDance / Doubao / Seed models | Do not install SKick on the model name. Install it in Trae or the actual host coding agent; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `chatgpt` | VERIFIED | Native custom Skill creation/upload is currently documented for eligible ChatGPT Business, Enterprise, Healthcare, and Edu workspaces, subject to workspace settings and product availability. Do not assume Plus/Pro/Free expose the same managed Skill UI. | web, desktop, mobile/web-mobile | Upload canonical skill.zip through Plugins > Skills > Create > Upload from your computer. | [`adapters/chatgpt/README.md`](../adapters/chatgpt/README.md) |
| `claude-app` | VERIFIED | Custom Skills are currently documented for Claude Free, Pro, Max, Team, and Enterprise users. Code execution must be enabled; some creation/recording surfaces have narrower plan/device availability. | web, desktop/mobile app where custom Skills are available | Upload claude-web-skill.zip through Customize > Skills > + Create skill > Upload a skill. The archive contains a top-level skick folder with lowercase skill.md. | [`adapters/claude-app/README.md`](../adapters/claude-app/README.md) |
| `claude-code` | VERIFIED | Host/plan/version dependent; see adapter. | CLI, VS Code, JetBrains, Claude Code Desktop/local sessions | Use .claude/skills/skick for project scope, ~/.claude/skills/skick for personal scope, or the generated Claude Code plugin for shared/plugin distribution. | [`adapters/claude-code/README.md`](../adapters/claude-code/README.md) |
| `cline` | VERIFIED | Host/plan/version dependent; see adapter. | VS Code extension, Cline agent surfaces | Enable Skills in Cline when required, then install project-local at .cline/skills/skick or global at ~/.cline/skills/skick. Cline also supports explicit slash-command invocation for enabled skills. | [`adapters/cline/README.md`](../adapters/cline/README.md) |
| `codex` | VERIFIED | Codex is currently included across ChatGPT Free, Go, Plus, Pro, Business, Edu, and Enterprise plans; limits vary by plan. This is separate from native Skill upload availability in ChatGPT chat. | CLI, app, IDE extension | Prefer repository/user Agent Skill scope for a standalone SKick install; use codex-plugin.zip only for Codex plugin distribution. | [`adapters/codex/README.md`](../adapters/codex/README.md) |
| `cohere` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | Cohere | Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `continue` | ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY | Host/plan/version dependent; see adapter. | Continue | Use the Continue Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback. | [`adapters/continue/README.md`](../adapters/continue/README.md) |
| `crush` | VERIFIED | Host/plan/version dependent; see adapter. | CLI/TUI coding agent | Prefer .crush/skills/skick or .agents/skills/skick for project scope; use current documented global Skill roots only for personal scope. | [`adapters/crush/README.md`](../adapters/crush/README.md) |
| `cursor` | VERIFIED | Host/plan/version dependent; see adapter. | desktop IDE, agent chat | Prefer .cursor/skills/skick for project scope and ~/.cursor/skills/skick for user scope; Cursor also documents the shared .agents/skills paths. | [`adapters/cursor/README.md`](../adapters/cursor/README.md) |
| `custom-cli` | GENERIC_CAPABILITY_BASED | Host/plan/version dependent; see adapter. | custom CLI/harness | If the host supports Agent Skills, map SKick to its verified skill root. Otherwise inject the generic prompt adapter and preserve canonical files as reference resources. | [`adapters/custom-cli/README.md`](../adapters/custom-cli/README.md) |
| `deepcode` | VERIFIED_WITH_PROVIDER_WARNING | Host/plan/version dependent; see adapter. | Deep Code CLI, Deep Code VS Code extension | Use project .deepcode/skills/skick or the documented shared personal Agent Skill path. DeepSeek documentation identifies Deep Code as a third-party integration, so verify the installed Deep Code version before automation. | [`adapters/deepcode/README.md`](../adapters/deepcode/README.md) |
| `deepseek` | HOST_RUNTIME_OR_FALLBACK | Host/plan/version dependent; see adapter. | DeepSeek model/web/API, Deep Code or external coding hosts | For a DeepSeek model inside another coding agent, install SKick into that host. For Deep Code specifically, use the separate deepcode entry; do not invent a model-only DeepSeek Skill path. | [`adapters/deepseek/README.md`](../adapters/deepseek/README.md) |
| `devin` | VERIFIED_REPO | Host/plan/version dependent; see adapter. | Devin | Commit the complete Skill at .agents/skills/skick in the repository. Devin also scans several compatible repository Skill roots, but .agents/skills is the recommended portable path. | [`adapters/devin/README.md`](../adapters/devin/README.md) |
| `factory-droid` | VERIFIED | Host/plan/version dependent; see adapter. | CLI/IDE engineering agent | Prefer .factory/skills/skick for project scope; Factory also documents compatible .agents/skills and .agent/skills roots. | [`adapters/factory-droid/README.md`](../adapters/factory-droid/README.md) |
| `future-agent` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | future/unknown runtimes | Detect capability: Agent Skill if explicitly supported, then Agent Plugin v1 if explicitly supported, otherwise a thin verified wrapper or generic prompt. | [`adapters/future-agent/README.md`](../adapters/future-agent/README.md) |
| `gemini-apps` | VERIFIED | Gemini Apps Skills are currently limited to Gemini Spark. Requirements include age 18+, a personal Google Account, Keep Activity on, and a qualifying Google AI subscription; work/school accounts are not supported. Geographic and subscription rules vary and can change. | Gemini Apps web/app surfaces that expose Skills | Upload gemini-apps-skill.zip. This generated archive keeps SKILL.md at ZIP root and intentionally excludes PNG/binary assets because Gemini Apps Skills support plain-text skill files only. | [`adapters/gemini-apps/README.md`](../adapters/gemini-apps/README.md) |
| `gemini-cli` | VERIFIED | Host/plan/version dependent; see adapter. | CLI/TUI, terminal integrations | Prefer `gemini skills install <source> --scope workspace\|user` or the documented .gemini/skills / .agents/skills discovery roots; use /skills reload after local changes when needed. | [`adapters/gemini-cli/README.md`](../adapters/gemini-cli/README.md) |
| `github-copilot` | VERIFIED | Agent Skill availability varies by Copilot surface and plan. For example, Copilot code-review Skills are currently generally available to Copilot Pro, Pro+, Business, and Enterprise users; other Copilot agent surfaces have their own eligibility/limits. | GitHub cloud agent, code review, Copilot CLI, Copilot app, VS Code agent mode, JetBrains agent mode | Prefer project .github/skills/skick or .agents/skills/skick; use ~/.copilot/skills/skick or ~/.agents/skills/skick for personal scope. GitHub CLI 2.90+ can preview/install/update Skills with gh skill. | [`adapters/github-copilot/README.md`](../adapters/github-copilot/README.md) |
| `glm` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | GLM models/providers inside coding hosts | Install SKick for the actual host (Claude Code, OpenCode, Cursor, Cline, etc.) and configure GLM separately as the model/provider. | [`adapters/glm/README.md`](../adapters/glm/README.md) |
| `goose` | VERIFIED | Goose Agent Skills are provided by the built-in Skills platform support; model/provider access and billing are separate. | Goose | Use the open Agent Skills standard path: project .agents/skills/skick or user ~/.agents/skills/skick. Goose documents these as the recommended locations; legacy .goose/skills and compatible Claude roots are fallback compatibility only. | [`adapters/goose/README.md`](../adapters/goose/README.md) |
| `grok` | VERIFIED_SPLIT_RUNTIME | Host/plan/version dependent; see adapter. | Grok web/iOS/Android, Grok Build | Use Grok native Skills UI for consumer surfaces; for Grok Build use its documented skill/plugin paths. Do not assume ChatGPT-style ZIP compatibility for consumer Grok. | [`adapters/grok/README.md`](../adapters/grok/README.md) |
| `ibm-granite` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | IBM Granite | Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `iflow-cli` | VERIFIED | Skill support is an iFlow CLI host capability; account/model/provider availability is separate. | iFlow CLI | Use .iflow/skills/skick for project scope or ~/.iflow/skills/skick for personal scope, then refresh/list Skills in iFlow CLI. | [`adapters/iflow-cli/README.md`](../adapters/iflow-cli/README.md) |
| `junie` | VERIFIED | Junie Skill support is documented in Junie surfaces; JetBrains AI entitlement/usage rules remain separate and may change. | JetBrains Junie | Use .junie/skills/skick for project scope or .agents/skills/skick for a portable project install. Use ~/.junie/skills/skick or ~/.agents/skills/skick for documented user scope. | [`adapters/junie/README.md`](../adapters/junie/README.md) |
| `kilo-code` | VERIFIED | Skill discovery is a Kilo Code host capability; model/provider billing or Kilo plan limits remain separate from the Skill directory format. | Kilo Code | Use .kilo/skills/skick for project scope or ~/.kilo/skills/skick for user scope; shared .agents/skills is also supported where documented. Treat older .kilocode/skills references as legacy unless the installed release explicitly documents them. | [`adapters/kilo-code/README.md`](../adapters/kilo-code/README.md) |
| `kimi` | VERIFIED_HOST_SPLIT | Host/plan/version dependent; see adapter. | Kimi Code CLI, Kimi model/web fallback | For Kimi Code use .kimi-code/skills/skick or .agents/skills/skick for project scope; use ~/.kimi-code/skills/skick or ~/.agents/skills/skick for user scope (or the equivalent $KIMI_CODE_HOME/skills/skick when KIMI_CODE_HOME is explicitly configured). | [`adapters/kimi/README.md`](../adapters/kimi/README.md) |
| `kiro-cli` | VERIFIED | Host/plan/version dependent; see adapter. | Kiro CLI | Use .kiro/skills/skick for workspace scope or ~/.kiro/skills/skick for global scope. Skills work across current Kiro IDE/CLI/Web/Mobile surfaces with scope differences; GitHub import requires a Skill subdirectory or SKILL.md URL rather than an arbitrary repository root. | [`adapters/kiro-cli/README.md`](../adapters/kiro-cli/README.md) |
| `longcat` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | LongCat models in agent harnesses, web fallback | Install SKick into the actual host harness; use generic fallback where no persistent Skill mechanism is verified. | [`adapters/longcat/README.md`](../adapters/longcat/README.md) |
| `manus` | VERIFIED_MANAGED_IMPORT | Host/plan/version dependent; see adapter. | managed Manus Skill surfaces | Use Skills > + Add > Import from GitHub for a public SKick repository URL, or Upload a skill for the validated archive/folder. Do not assert a filesystem path. | [`adapters/manus/README.md`](../adapters/manus/README.md) |
| `mcpjam` | ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY | Host/plan/version dependent; see adapter. | MCPJam | Use the MCPJam Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback. | [`adapters/mcpjam/README.md`](../adapters/mcpjam/README.md) |
| `meta-llama` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | Meta Llama | Do not install SKick on the model name. Install it in the actual host coding agent or custom harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `meta-muse` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | Meta AI web, Meta Model API, external hosts | Use generic prompt fallback on model-only surfaces; when Muse runs through a coding host, install SKick for that host. | [`adapters/meta-muse/README.md`](../adapters/meta-muse/README.md) |
| `mimo` | VERIFIED_HOST_SPLIT | Host/plan/version dependent; see adapter. | MiMoCode, MiMo models in other hosts | For MiMoCode use its documented .mimocode skill path; for MiMo models in another agent install SKick in that host instead. | [`adapters/mimo/README.md`](../adapters/mimo/README.md) |
| `minimax` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | MiniMax models in host agents, web/model fallback | For MiniMax models inside another coding agent, install SKick into that actual host. MiniMax also has an evolving Code/Skills ecosystem; use a dedicated host route only after current first-party documentation establishes its exact discovery/install contract. | [`adapters/minimax/README.md`](../adapters/minimax/README.md) |
| `mistral` | VERIFIED | Host/plan/version dependent; see adapter. | Vibe Code CLI, Vibe Code VS Code extension, Vibe Work web | For Vibe Code use .vibe/skills/skick or .agents/skills/skick project scope, ~/.vibe/skills/skick user scope, or configured skill_paths. Use the current Vibe Work UI for web/workspace Skills. | [`adapters/mistral/README.md`](../adapters/mistral/README.md) |
| `mux` | VERIFIED_PRODUCT_SOURCE | Mux Skill support is evidenced by the product source tree/tool surface; re-check the active Mux release before scripted global rollout. | Mux | Use .mux/skills/skick for project scope or ~/.mux/skills/skick for user scope. Mux source exposes Agent Skill list/read/write tools and uses .mux/skills in its own repository; verify the active release before unattended automation. | [`adapters/mux/README.md`](../adapters/mux/README.md) |
| `neovate` | ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY | Host/plan/version dependent; see adapter. | Neovate | Use the Neovate Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback. | [`adapters/neovate/README.md`](../adapters/neovate/README.md) |
| `openai-plugin` | VERIFIED | Host/plan/version dependent; see adapter. | Codex plugin/workspace | Use the Codex plugin wrapper when you intentionally distribute SKick as a Codex plugin; otherwise prefer a plain Agent Skill. | [`adapters/openai-plugin/README.md`](../adapters/openai-plugin/README.md) |
| `opencode` | VERIFIED | Host/plan/version dependent; see adapter. | CLI/TUI, web, IDE integrations that use OpenCode runtime | Use .opencode/skills/skick or .agents/skills/skick for project scope; use a documented global path for personal scope. | [`adapters/opencode/README.md`](../adapters/opencode/README.md) |
| `openhands` | VERIFIED_REPO | Host/plan/version dependent; see adapter. | OpenHands | For repository-scoped OpenHands use .openhands/skills/skick or the shared .agents/skills/skick route supported by the active release; verify scope behavior before assuming organization/user-level persistence. | [`adapters/openhands/README.md`](../adapters/openhands/README.md) |
| `pi` | VERIFIED | Skill support is a Pi host capability; provider/model billing and configured backend availability are separate. | Pi | Use .pi/skills/skick or .agents/skills/skick for a trusted project. For user scope use ~/.pi/agent/skills/skick or ~/.agents/skills/skick. Project Skills must respect Pi trust boundaries. | [`adapters/pi/README.md`](../adapters/pi/README.md) |
| `qoder` | VERIFIED | Host/plan/version dependent; see adapter. | Qoder | Use .qoder/skills/skick for project scope or ~/.qoder/skills/skick for user scope. Qoder IDE/CLI can also install compatible Skills through its Skills UI/CLI; QoderWork uses a separate ~/.qoderwork/skills root. | [`adapters/qoder/README.md`](../adapters/qoder/README.md) |
| `qwen` | VERIFIED_HOST_SPLIT | Host/plan/version dependent; see adapter. | Qwen Code CLI, Qwen Code editor integrations, Qwen model/web fallback | Use .qwen/skills/skick for project scope or ~/.qwen/skills/skick for personal scope; invoke explicitly with /skick when desired. | [`adapters/qwen/README.md`](../adapters/qwen/README.md) |
| `replit` | VERIFIED | Host/plan/version dependent; see adapter. | Replit | Install project Skills under .agents/skills/skick (Replit documentation displays /.agents/skills relative to the project root), through the Skills pane, or via a compatible skills CLI flow. | [`adapters/replit/README.md`](../adapters/replit/README.md) |
| `roo-code` | VERIFIED | Host/plan/version dependent; see adapter. | VS Code extension, Roo modes | Use .roo/skills/skick for project scope or ~/.roo/skills/skick for global scope; .agents/skills is also supported for cross-agent sharing. | [`adapters/roo-code/README.md`](../adapters/roo-code/README.md) |
| `sarvam` | HOST_RUNTIME_OR_GENERIC_FALLBACK | Host/plan/version dependent; see adapter. | model/provider surfaces | Use the actual host runtime adapter when known; otherwise use the generic prompt fallback. | [`adapters/sarvam/README.md`](../adapters/sarvam/README.md) |
| `tencent-hunyuan` | MODEL_PROVIDER_ROUTE_TO_HOST | Host/plan/version dependent; see adapter. | Tencent Hunyuan | Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session. | [`adapters/model-provider/README.md`](../adapters/model-provider/README.md) |
| `trae` | VERIFIED_PRODUCT_ECOSYSTEM | Host/plan/version dependent; see adapter. | TRAE IDE, TRAE SOLO, TRAE VS Code/plugin-style surfaces where Skills are exposed | Use .trae/skills/skick for project scope. For global scope use the product-specific global skill root documented by the installed TRAE edition (commonly ~/.trae/skills; TRAE CN may use ~/.trae-cn/skills). The Skills UI can also import external skills where available. | [`adapters/trae/README.md`](../adapters/trae/README.md) |
| `warp` | VERIFIED | Host/plan/version dependent; see adapter. | Warp | Use .agents/skills/skick or .warp/skills/skick for project scope and ~/.agents/skills/skick (or another currently documented Warp Skill root) for global scope. | [`adapters/warp/README.md`](../adapters/warp/README.md) |
| `windsurf` | VERIFIED | Host/plan/version dependent; see adapter. | Windsurf IDE, Cascade | Use .windsurf/skills/skick for workspace scope or ~/.codeium/windsurf/skills/skick for global scope. SKick can be auto-invoked by description or explicitly mentioned in Cascade. | [`adapters/windsurf/README.md`](../adapters/windsurf/README.md) |
| `zcode` | VERIFIED | Host/plan/version dependent; see adapter. | ZCode Agent, remote/SSH/WSL workspaces | Use ~/.zcode/skills/skick for user scope or ZCode Settings > Skills import/copy/symlink flows for supported external/project installs; use the generated plugin for distributable bundles when appropriate. | [`adapters/zcode/README.md`](../adapters/zcode/README.md) |
| `zed` | VERIFIED | Host/plan/version dependent; see adapter. | Zed | Use .agents/skills/skick in a trusted worktree for project scope or ~/.agents/skills/skick for user scope. Keep the Skill directory as a direct child of the Skills root and verify Zed discovery after changes. | [`adapters/zed/README.md`](../adapters/zed/README.md) |
| `zencoder` | VERIFIED | Host/plan/version dependent; see adapter. | Zencoder / Zenflow | Prefer the current open-standard .agents/skills/skick project/user roots. Zencoder also reads .claude/skills; legacy .zencoder/skills remains deprecated compatibility only. | [`adapters/zencoder/README.md`](../adapters/zencoder/README.md) |

## Detailed routing

### aider-desk

- **Aliases:** aider-desk, aiderdesk
- **Status:** `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY`
- **Surfaces:** AiderDesk
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the AiderDesk Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback.
- **Project/local paths:** `.aider-desk/skills/skick/`
- **User/personal paths:** `~/.aider-desk/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/aider-desk/README.md`](../adapters/aider-desk/README.md)
- **Primary source:** https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.

### amazon-nova

- **Aliases:** amazon nova, nova model
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** Amazon Nova
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### amp

- **Aliases:** amp, amp
- **Status:** `VERIFIED`
- **Surfaces:** Amp
- **Availability / gating:** Skill discovery is an Amp host capability; model/provider billing and account limits are separate from the Skill format.
- **Preferred install:** Use .agents/skills/skick for project scope. For user/machine scope use ~/.config/agents/skills/skick or another path explicitly documented by the active Amp release. Amp can also add Skills from supported sources through its native skill commands.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** `~/.config/agents/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/amp/README.md`](../adapters/amp/README.md)
- **Primary source:** https://ampcode.com/docs/customize/skills
- **Verification:**
  - Run Amp native Skill listing/discovery and confirm SKick is present.
  - Invoke a low-risk matching task and verify the complete Skill resources load.
- **Availability source:** https://ampcode.com/docs/customize/skills
- **Sources:**
  - https://ampcode.com/docs/customize/skills

### antigravity

- **Aliases:** antigravity, google antigravity
- **Status:** `VERIFIED`
- **Surfaces:** Antigravity visual agent/IDE
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use <workspace>/.agents/skills/skick for workspace scope or ~/.gemini/config/skills/skick for global scope. Do not use a fabricated plugin manifest.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** `~/.gemini/config/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/antigravity/README.md`](../adapters/antigravity/README.md)
- **Primary source:** https://antigravity.google/docs/skills/
- **Verification:**
  - Confirm SKick appears in the Antigravity skill inventory or is selected automatically for a matching low-risk prompt.

### antigravity-cli

- **Aliases:** antigravity cli, agy, google antigravity cli
- **Status:** `VERIFIED_DISTINCT_RUNTIME`
- **Surfaces:** terminal TUI
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Antigravity CLI uses workspace .agents/skills/ and global ~/.gemini/antigravity-cli/skills/ for CLI skills, but its documented local Skill examples are flat .md files. Use the adapter guidance and a deliberately flattened prompt for SKick unless the installed CLI version documents full directory-form Agent Skills; plugin packaging must follow the current Antigravity CLI plugin specification rather than guessed manifests.
- **Project/local paths:** `.agents/skills/`
- **User/personal paths:** `~/.gemini/antigravity-cli/skills/`
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/antigravity-cli/README.md`](../adapters/antigravity-cli/README.md)
- **Primary source:** https://antigravity.google/docs/cli/plugins/
- **Verification:**
  - Run /skills and confirm the installed/flattened SKick command is visible before relying on it.

### augment

- **Aliases:** augment, augment
- **Status:** `VERIFIED`
- **Surfaces:** Augment
- **Availability / gating:** Skill support is a host capability; Augment plan/usage limits and model-provider billing are separate from Skill discovery.
- **Preferred install:** Use .augment/skills/skick for Augment-specific project scope or .agents/skills/skick for a portable project install; Augment also discovers compatible Claude Skill roots. Use the corresponding documented user roots for personal scope.
- **Project/local paths:** `.augment/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`
- **User/personal paths:** `~/.augment/skills/skick/`, `~/.agents/skills/skick/`, `~/.claude/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/augment/README.md`](../adapters/augment/README.md)
- **Primary source:** https://docs.augmentcode.com/cli/skills
- **Verification:**
  - Use Augment Skill discovery (/skills or the current equivalent) and confirm SKick is present.
  - Invoke SKick or a matching low-risk task and verify supporting files resolve.
- **Availability source:** https://docs.augmentcode.com/cli/skills
- **Sources:**
  - https://docs.augmentcode.com/cli/skills

### baidu-ernie

- **Aliases:** ernie, baidu ernie
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** Baidu ERNIE
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### browsercode

- **Aliases:** browsercode, browser code
- **Status:** `VERIFIED_INHERITED_OPENCODE`
- **Surfaces:** BrowserCode CLI/TUI, headless BrowserCode runs, browser-native coding-agent sessions
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** BrowserCode is a fork of OpenCode and its repository contains .opencode/skills/*/SKILL.md. Install SKick using the OpenCode-compatible skill roots, then verify discovery in the installed BrowserCode build.
- **Project/local paths:** `.opencode/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.config/opencode/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/browsercode/README.md`](../adapters/browsercode/README.md)
- **Primary source:** https://github.com/browser-use/browsercode
- **Verification:**
  - Start BrowserCode (`bcode`) and verify SKick is visible/usable as a skill.
  - Run a low-risk browser-aware task and confirm SKick instructions are loaded before claiming successful installation.
- **Sources:**
  - https://github.com/browser-use/browsercode
  - https://opencode.ai/docs/skills

### bytedance-models

- **Aliases:** bytedance, doubao, seed, seed-code, seed coder
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** ByteDance / Doubao / Seed models
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in Trae or the actual host coding agent; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### chatgpt

- **Aliases:** chatgpt, chatgpt web, chatgpt desktop, chatgpt mobile, openai chatgpt
- **Status:** `VERIFIED`
- **Surfaces:** web, desktop, mobile/web-mobile
- **Availability / gating:** Native custom Skill creation/upload is currently documented for eligible ChatGPT Business, Enterprise, Healthcare, and Edu workspaces, subject to workspace settings and product availability. Do not assume Plus/Pro/Free expose the same managed Skill UI.
- **Preferred install:** Upload canonical skill.zip through Plugins > Skills > Create > Upload from your computer.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `skill.zip`
- **Adapter:** [`adapters/chatgpt/README.md`](../adapters/chatgpt/README.md)
- **Primary source:** https://help.openai.com/en/articles/20001066
- **Verification:**
  - Confirm SKick appears in Skills as installed/enabled.
  - Run a low-risk prompt that clearly matches the SKick description.
- **Limitations / caveats:**
  - Managed ChatGPT Skill availability is plan/workspace/surface dependent.
  - Codex has separate Skill support and plan availability; do not infer Codex eligibility from the ChatGPT managed-Skill gate.
- **Availability source:** https://help.openai.com/en/articles/20001066

### claude-app

- **Aliases:** claude web, claude app, claude desktop, claude.ai
- **Status:** `VERIFIED`
- **Surfaces:** web, desktop/mobile app where custom Skills are available
- **Availability / gating:** Custom Skills are currently documented for Claude Free, Pro, Max, Team, and Enterprise users. Code execution must be enabled; some creation/recording surfaces have narrower plan/device availability.
- **Preferred install:** Upload claude-web-skill.zip through Customize > Skills > + Create skill > Upload a skill. The archive contains a top-level skick folder with lowercase skill.md.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `claude-web-skill.zip`
- **Adapter:** [`adapters/claude-app/README.md`](../adapters/claude-app/README.md)
- **Primary source:** https://support.claude.com/en/articles/12512180-use-skills-in-claude
- **Verification:**
  - Confirm SKick is present/enabled in Claude Skills.
  - Invoke it on a low-risk research task.
- **Availability source:** https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- **Sources:**
  - https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
  - https://support.claude.com/en/articles/12512180-use-skills-in-claude

### claude-code

- **Aliases:** claude code, claude code cli, claude code vscode, claude code vs code, claude code jetbrains, claude code desktop
- **Status:** `VERIFIED`
- **Surfaces:** CLI, VS Code, JetBrains, Claude Code Desktop/local sessions
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .claude/skills/skick for project scope, ~/.claude/skills/skick for personal scope, or the generated Claude Code plugin for shared/plugin distribution.
- **Project/local paths:** `.claude/skills/skick/`
- **User/personal paths:** `~/.claude/skills/skick/`
- **Generated distribution:** `claude-code-plugin.zip`
- **Adapter:** [`adapters/claude-code/README.md`](../adapters/claude-code/README.md)
- **Primary source:** https://code.claude.com/docs/en/slash-commands
- **Verification:**
  - Confirm the skill is visible/invocable in the active Claude Code session.
  - For plugin testing, use the runtime-supported local plugin load flow and reload plugins after changes.

### cline

- **Aliases:** cline, cline vscode, cline cli, cline agent
- **Status:** `VERIFIED`
- **Surfaces:** VS Code extension, Cline agent surfaces
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Enable Skills in Cline when required, then install project-local at .cline/skills/skick or global at ~/.cline/skills/skick. Cline also supports explicit slash-command invocation for enabled skills.
- **Project/local paths:** `.cline/skills/skick/`
- **User/personal paths:** `~/.cline/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/cline/README.md`](../adapters/cline/README.md)
- **Primary source:** https://docs.cline.bot/customization/skills
- **Verification:**
  - Confirm SKick appears in the Cline Skills menu and is enabled.
  - Invoke `/skick` or a matching low-risk prompt and confirm use_skill loads it.
- **Sources:**
  - https://docs.cline.bot/customization/skills
  - https://github.com/cline/skills

### codex

- **Aliases:** codex, codex cli, codex app, codex ide, openai codex
- **Status:** `VERIFIED`
- **Surfaces:** CLI, app, IDE extension
- **Availability / gating:** Codex is currently included across ChatGPT Free, Go, Plus, Pro, Business, Edu, and Enterprise plans; limits vary by plan. This is separate from native Skill upload availability in ChatGPT chat.
- **Preferred install:** Prefer repository/user Agent Skill scope for a standalone SKick install; use codex-plugin.zip only for Codex plugin distribution.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `codex-plugin.zip`
- **Adapter:** [`adapters/codex/README.md`](../adapters/codex/README.md)
- **Primary source:** https://developers.openai.com/codex/skills/
- **Verification:**
  - Confirm SKick appears in the Codex skill selector/list.
  - If a change is not detected, restart/reload Codex and re-check.
- **Availability source:** https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits
- **Sources:**
  - https://developers.openai.com/codex/skills/
  - https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits

### cohere

- **Aliases:** cohere, command r, command a
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** Cohere
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### continue

- **Aliases:** continue, continue
- **Status:** `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY`
- **Surfaces:** Continue
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the Continue Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback.
- **Project/local paths:** `.continue/skills/skick/`
- **User/personal paths:** `~/.continue/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/continue/README.md`](../adapters/continue/README.md)
- **Primary source:** https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.

### crush

- **Aliases:** crush, charmbracelet crush, crush cli
- **Status:** `VERIFIED`
- **Surfaces:** CLI/TUI coding agent
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Prefer .crush/skills/skick or .agents/skills/skick for project scope; use current documented global Skill roots only for personal scope.
- **Project/local paths:** `.crush/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`, `.cursor/skills/skick/`
- **User/personal paths:** `~/.config/crush/skills/skick/`, `~/.agents/skills/skick/`, `~/.claude/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/crush/README.md`](../adapters/crush/README.md)
- **Primary source:** https://github.com/charmbracelet/crush
- **Verification:**
  - Confirm SKick appears in Crush native Skill discovery/invocation.
  - Run a low-risk explicit SKick trigger.
- **Sources:**
  - https://github.com/charmbracelet/crush

### cursor

- **Aliases:** cursor, cursor ide, cursor agent
- **Status:** `VERIFIED`
- **Surfaces:** desktop IDE, agent chat
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Prefer .cursor/skills/skick for project scope and ~/.cursor/skills/skick for user scope; Cursor also documents the shared .agents/skills paths.
- **Project/local paths:** `.cursor/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`, `.codex/skills/skick/`
- **User/personal paths:** `~/.cursor/skills/skick/`, `~/.agents/skills/skick/`, `~/.claude/skills/skick/`, `~/.codex/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/cursor/README.md`](../adapters/cursor/README.md)
- **Primary source:** https://prod.cursor.com/docs/skills
- **Verification:**
  - Open Cursor Customize > Skills or use Agent slash search and confirm SKick is discovered.

### custom-cli

- **Aliases:** custom cli, custom agent, custom harness
- **Status:** `GENERIC_CAPABILITY_BASED`
- **Surfaces:** custom CLI/harness
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** If the host supports Agent Skills, map SKick to its verified skill root. Otherwise inject the generic prompt adapter and preserve canonical files as reference resources.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/custom-cli/README.md`](../adapters/custom-cli/README.md)
- **Primary source:** https://agentskills.io/
- **Verification:**
  - Document the host contract and test discovery before calling it supported.

### deepcode

- **Aliases:** deep code, deepcode, deepseek deep code
- **Status:** `VERIFIED_WITH_PROVIDER_WARNING`
- **Surfaces:** Deep Code CLI, Deep Code VS Code extension
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use project .deepcode/skills/skick or the documented shared personal Agent Skill path. DeepSeek documentation identifies Deep Code as a third-party integration, so verify the installed Deep Code version before automation.
- **Project/local paths:** `.deepcode/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/deepcode/README.md`](../adapters/deepcode/README.md)
- **Primary source:** https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode
- **Verification:**
  - Confirm SKick is discovered by the actual Deep Code host; do not treat selecting a DeepSeek model as proof of Skill support.

### deepseek

- **Aliases:** deepseek, deepseek web, deepseek api, deep code
- **Status:** `HOST_RUNTIME_OR_FALLBACK`
- **Surfaces:** DeepSeek model/web/API, Deep Code or external coding hosts
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For a DeepSeek model inside another coding agent, install SKick into that host. For Deep Code specifically, use the separate deepcode entry; do not invent a model-only DeepSeek Skill path.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/deepseek/README.md`](../adapters/deepseek/README.md)
- **Primary source:** https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode
- **Verification:**
  - Verify the actual host runtime, not merely the DeepSeek model selection.

### devin

- **Aliases:** devin, devin
- **Status:** `VERIFIED_REPO`
- **Surfaces:** Devin
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Commit the complete Skill at .agents/skills/skick in the repository. Devin also scans several compatible repository Skill roots, but .agents/skills is the recommended portable path.
- **Project/local paths:** `.agents/skills/skick/`, `.github/skills/skick/`, `.claude/skills/skick/`, `.cursor/skills/skick/`, `.codex/skills/skick/`, `.cognition/skills/skick/`, `.windsurf/skills/skick/`
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/devin/README.md`](../adapters/devin/README.md)
- **Primary source:** https://docs.devin.ai/product-guides/skills
- **Verification:**
  - Confirm Devin discovers the repository Skill after indexing/cloning or a branch rescan.
  - Invoke with a matching request or @skills:skick and verify only the intended Skill is active.
- **Limitations / caveats:**
  - Current Devin Skills are repository-scoped; do not invent a global ~/.devin/skills route.
  - Devin currently activates one Skill at a time; a new Skill replaces the active Skill.
- **Sources:**
  - https://docs.devin.ai/product-guides/skills

### factory-droid

- **Aliases:** factory droid, droid, factory ai droid, factory agent
- **Status:** `VERIFIED`
- **Surfaces:** CLI/IDE engineering agent
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Prefer .factory/skills/skick for project scope; Factory also documents compatible .agents/skills and .agent/skills roots.
- **Project/local paths:** `.factory/skills/skick/`, `.agents/skills/skick/`, `.agent/skills/skick/`
- **User/personal paths:** `~/.factory/skills/skick/`, `~/.agents/skills/skick/`, `~/.agent/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/factory-droid/README.md`](../adapters/factory-droid/README.md)
- **Primary source:** https://docs.factory.ai/harness/skills
- **Verification:**
  - Use the native Factory Skills manager/discovery and confirm SKick is visible.
  - Run a low-risk explicit SKick trigger in the active project.
- **Sources:**
  - https://docs.factory.ai/harness/skills

### future-agent

- **Aliases:** future agent, unknown agent, unknown runtime
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** future/unknown runtimes
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Detect capability: Agent Skill if explicitly supported, then Agent Plugin v1 if explicitly supported, otherwise a thin verified wrapper or generic prompt.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/future-agent/README.md`](../adapters/future-agent/README.md)
- **Primary source:** https://agentskills.io/
- **Verification:**
  - Never invent install semantics for a new runtime; verify first-party docs before adding an adapter.

### gemini-apps

- **Aliases:** gemini apps, gemini app, gemini web, gemini.google.com
- **Status:** `VERIFIED`
- **Surfaces:** Gemini Apps web/app surfaces that expose Skills
- **Availability / gating:** Gemini Apps Skills are currently limited to Gemini Spark. Requirements include age 18+, a personal Google Account, Keep Activity on, and a qualifying Google AI subscription; work/school accounts are not supported. Geographic and subscription rules vary and can change.
- **Preferred install:** Upload gemini-apps-skill.zip. This generated archive keeps SKILL.md at ZIP root and intentionally excludes PNG/binary assets because Gemini Apps Skills support plain-text skill files only.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `gemini-apps-skill.zip`
- **Adapter:** [`adapters/gemini-apps/README.md`](../adapters/gemini-apps/README.md)
- **Primary source:** https://support.google.com/gemini/answer/17094296
- **Verification:**
  - Confirm the Skill is visible/enabled in the Gemini Skills UI and run a low-risk trigger test.
- **Limitations / caveats:**
  - Skills are a Gemini Spark feature, not a general Gemini chat feature.
  - Plain-text files are supported; binary/rich-media assets are excluded from the generated Gemini package.
  - Internet-dependent scripts are not supported in uploaded Skills.
- **Availability source:** https://support.google.com/gemini/answer/17094296?hl=en

### gemini-cli

- **Aliases:** gemini cli, google gemini cli
- **Status:** `VERIFIED`
- **Surfaces:** CLI/TUI, terminal integrations
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Prefer `gemini skills install <source> --scope workspace|user` or the documented .gemini/skills / .agents/skills discovery roots; use /skills reload after local changes when needed.
- **Project/local paths:** `.agents/skills/skick/`, `.gemini/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`, `~/.gemini/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/gemini-cli/README.md`](../adapters/gemini-cli/README.md)
- **Primary source:** https://geminicli.com/docs/cli/skills/
- **Verification:**
  - Use /skills list or gemini skills list --all.
  - Reload/refresh skills after changes and confirm SKick is enabled.

### github-copilot

- **Aliases:** github copilot, copilot cli, copilot vscode, copilot vs code, copilot jetbrains, copilot cloud agent, copilot app
- **Status:** `VERIFIED`
- **Surfaces:** GitHub cloud agent, code review, Copilot CLI, Copilot app, VS Code agent mode, JetBrains agent mode
- **Availability / gating:** Agent Skill availability varies by Copilot surface and plan. For example, Copilot code-review Skills are currently generally available to Copilot Pro, Pro+, Business, and Enterprise users; other Copilot agent surfaces have their own eligibility/limits.
- **Preferred install:** Prefer project .github/skills/skick or .agents/skills/skick; use ~/.copilot/skills/skick or ~/.agents/skills/skick for personal scope. GitHub CLI 2.90+ can preview/install/update Skills with gh skill.
- **Project/local paths:** `.github/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`
- **User/personal paths:** `~/.copilot/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/github-copilot/README.md`](../adapters/github-copilot/README.md)
- **Primary source:** https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- **Verification:**
  - Confirm SKick is discovered by the active Copilot surface.
  - For Copilot CLI, reload skills when needed and verify the discovered list.
- **Availability source:** https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/
- **Sources:**
  - https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
  - https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/

### glm

- **Aliases:** glm, z.ai glm, glm coding plan
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** GLM models/providers inside coding hosts
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Install SKick for the actual host (Claude Code, OpenCode, Cursor, Cline, etc.) and configure GLM separately as the model/provider.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/glm/README.md`](../adapters/glm/README.md)
- **Primary source:** https://docs.z.ai/devpack/quick-start
- **Verification:**
  - Verify the host Skill installation independently from model/provider configuration.

### goose

- **Aliases:** goose, goose
- **Status:** `VERIFIED`
- **Surfaces:** Goose
- **Availability / gating:** Goose Agent Skills are provided by the built-in Skills platform support; model/provider access and billing are separate.
- **Preferred install:** Use the open Agent Skills standard path: project .agents/skills/skick or user ~/.agents/skills/skick. Goose documents these as the recommended locations; legacy .goose/skills and compatible Claude roots are fallback compatibility only.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/goose/README.md`](../adapters/goose/README.md)
- **Primary source:** https://goose-docs.ai/docs/guides/context-engineering/using-skills/
- **Verification:**
  - Run `goose skills list` or `/skills` and confirm SKick is listed.
  - Invoke a low-risk matching task and confirm SKick supporting files can be read.
- **Limitations / caveats:**
  - Legacy `.goose/skills/` and Claude-compatible locations are backward-compatibility paths; prefer `.agents/skills/` for new installs.
- **Sources:**
  - https://goose-docs.ai/docs/guides/context-engineering/using-skills/

### grok

- **Aliases:** grok, grok web, grok ios, grok android, grok build
- **Status:** `VERIFIED_SPLIT_RUNTIME`
- **Surfaces:** Grok web/iOS/Android, Grok Build
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use Grok native Skills UI for consumer surfaces; for Grok Build use its documented skill/plugin paths. Do not assume ChatGPT-style ZIP compatibility for consumer Grok.
- **Project/local paths:** `.grok/skills/skick/`
- **User/personal paths:** `~/.grok/skills/skick/`
- **Generated distribution:** none dedicated
- **Adapter:** [`adapters/grok/README.md`](../adapters/grok/README.md)
- **Primary source:** https://docs.x.ai/build/features/skills-plugins-marketplaces
- **Verification:**
  - Confirm the native Grok Skill or Grok Build filesystem/plugin entry is visible and invocable.

### ibm-granite

- **Aliases:** granite, ibm granite
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** IBM Granite
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### iflow-cli

- **Aliases:** iflow-cli, iflow cli
- **Status:** `VERIFIED`
- **Surfaces:** iFlow CLI
- **Availability / gating:** Skill support is an iFlow CLI host capability; account/model/provider availability is separate.
- **Preferred install:** Use .iflow/skills/skick for project scope or ~/.iflow/skills/skick for personal scope, then refresh/list Skills in iFlow CLI.
- **Project/local paths:** `.iflow/skills/skick/`
- **User/personal paths:** `~/.iflow/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/iflow-cli/README.md`](../adapters/iflow-cli/README.md)
- **Primary source:** https://platform.iflow.cn/en/cli/examples/skill
- **Verification:**
  - Run `/skills refresh` (or the current equivalent) and confirm SKick is registered.
  - Invoke a low-risk matching task and verify supporting files resolve.
- **Sources:**
  - https://platform.iflow.cn/en/cli/examples/skill

### junie

- **Aliases:** junie, jetbrains junie
- **Status:** `VERIFIED`
- **Surfaces:** JetBrains Junie
- **Availability / gating:** Junie Skill support is documented in Junie surfaces; JetBrains AI entitlement/usage rules remain separate and may change.
- **Preferred install:** Use .junie/skills/skick for project scope or .agents/skills/skick for a portable project install. Use ~/.junie/skills/skick or ~/.agents/skills/skick for documented user scope.
- **Project/local paths:** `.junie/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.junie/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/junie/README.md`](../adapters/junie/README.md)
- **Primary source:** https://junie.jetbrains.com/docs/agent-skills.html
- **Verification:**
  - Confirm SKick appears in Junie Skill discovery for the selected project/user scope.
  - Run a low-risk matching task or the current explicit Skill invocation flow.
- **Availability source:** https://junie.jetbrains.com/docs/agent-skills.html
- **Sources:**
  - https://junie.jetbrains.com/docs/agent-skills.html

### kilo-code

- **Aliases:** kilo-code, kilo code
- **Status:** `VERIFIED`
- **Surfaces:** Kilo Code
- **Availability / gating:** Skill discovery is a Kilo Code host capability; model/provider billing or Kilo plan limits remain separate from the Skill directory format.
- **Preferred install:** Use .kilo/skills/skick for project scope or ~/.kilo/skills/skick for user scope; shared .agents/skills is also supported where documented. Treat older .kilocode/skills references as legacy unless the installed release explicitly documents them.
- **Project/local paths:** `.kilo/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.kilo/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/kilo-code/README.md`](../adapters/kilo-code/README.md)
- **Primary source:** https://kilo.ai/docs/customize/skills
- **Verification:**
  - Confirm SKick appears in Kilo Code Skill discovery for the selected scope.
  - Run a low-risk explicit/matching trigger and verify supporting files resolve.
- **Availability source:** https://kilo.ai/docs/customize/skills
- **Sources:**
  - https://kilo.ai/docs/customize/skills

### kimi

- **Aliases:** kimi code, kimi code cli, kimi, moonshot kimi
- **Status:** `VERIFIED_HOST_SPLIT`
- **Surfaces:** Kimi Code CLI, Kimi model/web fallback
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For Kimi Code use .kimi-code/skills/skick or .agents/skills/skick for project scope; use ~/.kimi-code/skills/skick or ~/.agents/skills/skick for user scope (or the equivalent $KIMI_CODE_HOME/skills/skick when KIMI_CODE_HOME is explicitly configured).
- **Project/local paths:** `.kimi-code/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.kimi-code/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `kimi-plugin.zip`
- **Adapter:** [`adapters/kimi/README.md`](../adapters/kimi/README.md)
- **Primary source:** https://moonshotai.github.io/kimi-code/en/customization/skills/
- **Verification:**
  - Confirm Kimi Code discovers the skill from the selected tier and that project scope overrides lower scopes when intended.
- **Limitations / caveats:**
  - Canonical explicit Kimi Code invocation is /skill:skick; plain /skick may depend on command-name collision/fallback behavior.
- **Sources:**
  - https://moonshotai.github.io/kimi-code/en/customization/skills/
  - https://github.com/MoonshotAI/kimi-code

### kiro-cli

- **Aliases:** kiro-cli, kiro cli
- **Status:** `VERIFIED`
- **Surfaces:** Kiro CLI
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .kiro/skills/skick for workspace scope or ~/.kiro/skills/skick for global scope. Skills work across current Kiro IDE/CLI/Web/Mobile surfaces with scope differences; GitHub import requires a Skill subdirectory or SKILL.md URL rather than an arbitrary repository root.
- **Project/local paths:** `.kiro/skills/skick/`
- **User/personal paths:** `~/.kiro/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/kiro-cli/README.md`](../adapters/kiro-cli/README.md)
- **Primary source:** https://kiro.dev/docs/skills/
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.
- **Sources:**
  - https://kiro.dev/docs/skills/

### longcat

- **Aliases:** longcat, longcat 2.0
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** LongCat models in agent harnesses, web fallback
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Install SKick into the actual host harness; use generic fallback where no persistent Skill mechanism is verified.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/longcat/README.md`](../adapters/longcat/README.md)
- **Primary source:** https://github.com/meituan-longcat/LongCat-2.0
- **Verification:**
  - Verify the actual host rather than inferring capabilities from the model name.
- **Sources:**
  - https://github.com/meituan-longcat/LongCat-2.0
  - https://longcat.chat/platform/docs/OpenCode.html

### manus

- **Aliases:** manus, manus ai, manus skills
- **Status:** `VERIFIED_MANAGED_IMPORT`
- **Surfaces:** managed Manus Skill surfaces
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use Skills > + Add > Import from GitHub for a public SKick repository URL, or Upload a skill for the validated archive/folder. Do not assert a filesystem path.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `skill.zip`
- **Adapter:** [`adapters/manus/README.md`](../adapters/manus/README.md)
- **Primary source:** https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus
- **Verification:**
  - Confirm SKick is imported/enabled in the Manus Skills surface.
  - Run a low-risk trigger test and distinguish UI import success from external tool availability.
- **Sources:**
  - https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus

### mcpjam

- **Aliases:** mcpjam, mcpjam
- **Status:** `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY`
- **Surfaces:** MCPJam
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the MCPJam Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback.
- **Project/local paths:** `.mcpjam/skills/skick/`
- **User/personal paths:** `~/.mcpjam/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/mcpjam/README.md`](../adapters/mcpjam/README.md)
- **Primary source:** https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.

### meta-llama

- **Aliases:** meta llama, llama, llama code
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** Meta Llama
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent or custom harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### meta-muse

- **Aliases:** meta ai, muse, muse spark, meta muse
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** Meta AI web, Meta Model API, external hosts
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use generic prompt fallback on model-only surfaces; when Muse runs through a coding host, install SKick for that host.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/meta-muse/README.md`](../adapters/meta-muse/README.md)
- **Primary source:** https://www.meta.ai/
- **Verification:**
  - Do not fabricate a Muse-specific manifest or path.

### mimo

- **Aliases:** mimocode, mimo code, xiaomi mimo, mimo
- **Status:** `VERIFIED_HOST_SPLIT`
- **Surfaces:** MiMoCode, MiMo models in other hosts
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For MiMoCode use its documented .mimocode skill path; for MiMo models in another agent install SKick in that host instead.
- **Project/local paths:** `.mimocode/skills/skick/`
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** none dedicated
- **Adapter:** [`adapters/mimo/README.md`](../adapters/mimo/README.md)
- **Primary source:** https://github.com/XiaomiMiMo/MiMo-Code
- **Verification:**
  - Confirm the installed MiMoCode release discovers SKick; otherwise verify through the actual host runtime.
- **Sources:**
  - https://github.com/XiaomiMiMo/MiMo-Code

### minimax

- **Aliases:** minimax, minimax model
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** MiniMax models in host agents, web/model fallback
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For MiniMax models inside another coding agent, install SKick into that actual host. MiniMax also has an evolving Code/Skills ecosystem; use a dedicated host route only after current first-party documentation establishes its exact discovery/install contract.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/minimax/README.md`](../adapters/minimax/README.md)
- **Primary source:** https://github.com/MiniMax-AI/skills
- **Verification:**
  - Verify the host runtime Skill installation; do not claim a MiniMax-specific path unless first-party docs establish one.
- **Limitations / caveats:**
  - Do not invent .minimax/skills or another filesystem path solely from the provider/model name.
- **Sources:**
  - https://github.com/MiniMax-AI/skills

### mistral

- **Aliases:** mistral vibe, vibe code, mistral vibe code, mistral vibe vscode, vibe work
- **Status:** `VERIFIED`
- **Surfaces:** Vibe Code CLI, Vibe Code VS Code extension, Vibe Work web
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For Vibe Code use .vibe/skills/skick or .agents/skills/skick project scope, ~/.vibe/skills/skick user scope, or configured skill_paths. Use the current Vibe Work UI for web/workspace Skills.
- **Project/local paths:** `.vibe/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.vibe/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/mistral/README.md`](../adapters/mistral/README.md)
- **Primary source:** https://docs.mistral.ai/vibe/code/cli/skills
- **Verification:**
  - Confirm the skill is discovered in the CLI/VS Code slash picker or Work Skills UI.

### mux

- **Aliases:** mux, mux
- **Status:** `VERIFIED_PRODUCT_SOURCE`
- **Surfaces:** Mux
- **Availability / gating:** Mux Skill support is evidenced by the product source tree/tool surface; re-check the active Mux release before scripted global rollout.
- **Preferred install:** Use .mux/skills/skick for project scope or ~/.mux/skills/skick for user scope. Mux source exposes Agent Skill list/read/write tools and uses .mux/skills in its own repository; verify the active release before unattended automation.
- **Project/local paths:** `.mux/skills/skick/`
- **User/personal paths:** `~/.mux/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/mux/README.md`](../adapters/mux/README.md)
- **Primary source:** https://github.com/coder/mux
- **Verification:**
  - Use Mux Skill listing/read tooling and confirm SKick is visible.
  - Run a low-risk matching task and confirm supporting files resolve.
- **Limitations / caveats:**
  - Treat source-level evidence as version-sensitive; verify the installed Mux build before unattended install/update automation.
- **Sources:**
  - https://github.com/coder/mux/blob/main/.mux/skills/tbench/SKILL.md
  - https://github.com/coder/mux/blob/main/docs/hooks/tools.mdx

### neovate

- **Aliases:** neovate, neovate
- **Status:** `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY`
- **Surfaces:** Neovate
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the Neovate Agent Skills path shown below only after confirming the installed release still supports it; otherwise use the shared .agents/skills path if documented or the generic fallback.
- **Project/local paths:** `.neovate/skills/skick/`
- **User/personal paths:** `~/.neovate/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/neovate/README.md`](../adapters/neovate/README.md)
- **Primary source:** https://auth0.github.io/auth0-cli/auth0_agent_skills_install.html
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.

### openai-plugin

- **Aliases:** openai plugin, chatgpt plugin, codex plugin directory, openai plugins
- **Status:** `VERIFIED`
- **Surfaces:** Codex plugin/workspace
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the Codex plugin wrapper when you intentionally distribute SKick as a Codex plugin; otherwise prefer a plain Agent Skill.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `codex-plugin.zip`
- **Adapter:** [`adapters/openai-plugin/README.md`](../adapters/openai-plugin/README.md)
- **Primary source:** https://github.com/openai/plugins
- **Verification:**
  - Confirm the plugin lists the SKick skill.
  - Verify any required apps separately; SKick itself does not grant app access.

### opencode

- **Aliases:** opencode, open code
- **Status:** `VERIFIED`
- **Surfaces:** CLI/TUI, web, IDE integrations that use OpenCode runtime
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .opencode/skills/skick or .agents/skills/skick for project scope; use a documented global path for personal scope.
- **Project/local paths:** `.opencode/skills/skick/`, `.agents/skills/skick/`, `.claude/skills/skick/`
- **User/personal paths:** `~/.config/opencode/skills/skick/`, `~/.agents/skills/skick/`, `~/.claude/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/opencode/README.md`](../adapters/opencode/README.md)
- **Primary source:** https://opencode.ai/docs/skills
- **Verification:**
  - Confirm SKick appears in the native skill tool/discovery list.
  - Check OpenCode skill permissions if it is hidden.
- **Sources:**
  - https://opencode.ai/docs/skills

### openhands

- **Aliases:** openhands, openhands
- **Status:** `VERIFIED_REPO`
- **Surfaces:** OpenHands
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** For repository-scoped OpenHands use .openhands/skills/skick or the shared .agents/skills/skick route supported by the active release; verify scope behavior before assuming organization/user-level persistence.
- **Project/local paths:** `.openhands/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/openhands/README.md`](../adapters/openhands/README.md)
- **Primary source:** https://www.openhands.dev/blog/20260227-creating-effective-agent-skills
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.
- **Limitations / caveats:**
  - Treat repository-level support as verified; re-check managed organization/user scope separately.
- **Sources:**
  - https://www.openhands.dev/blog/20260227-creating-effective-agent-skills

### pi

- **Aliases:** pi, pi
- **Status:** `VERIFIED`
- **Surfaces:** Pi
- **Availability / gating:** Skill support is a Pi host capability; provider/model billing and configured backend availability are separate.
- **Preferred install:** Use .pi/skills/skick or .agents/skills/skick for a trusted project. For user scope use ~/.pi/agent/skills/skick or ~/.agents/skills/skick. Project Skills must respect Pi trust boundaries.
- **Project/local paths:** `.pi/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.pi/agent/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/pi/README.md`](../adapters/pi/README.md)
- **Primary source:** https://pi.dev/docs/latest/skills
- **Verification:**
  - Confirm Pi discovers SKick in the selected scope.
  - Run a low-risk matching task and verify project trust allows Skill loading.
- **Limitations / caveats:**
  - Project Skills should load only from trusted projects/worktrees; do not bypass the host trust boundary.
- **Availability source:** https://pi.dev/docs/latest/skills
- **Sources:**
  - https://pi.dev/docs/latest/skills

### qoder

- **Aliases:** qoder, qoder
- **Status:** `VERIFIED`
- **Surfaces:** Qoder
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .qoder/skills/skick for project scope or ~/.qoder/skills/skick for user scope. Qoder IDE/CLI can also install compatible Skills through its Skills UI/CLI; QoderWork uses a separate ~/.qoderwork/skills root.
- **Project/local paths:** `.qoder/skills/skick/`
- **User/personal paths:** `~/.qoder/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/qoder/README.md`](../adapters/qoder/README.md)
- **Primary source:** https://docs.qoder.com/extensions/skills
- **Verification:**
  - Confirm SKick appears in Qoder Installed Skills or the CLI /skills list after reload/restart.
  - Invoke with /skick or a matching low-risk prompt and verify activation.
- **Limitations / caveats:**
  - QoderWork is a distinct surface with ~/.qoderwork/skills; do not reuse Qoder IDE paths blindly.
- **Sources:**
  - https://docs.qoder.com/extensions/skills
  - https://docs.qoder.com/qoderwork/skills

### qwen

- **Aliases:** qwen code, qwen code cli, qwen code vscode, qwen code jetbrains, qwen code zed, qwen
- **Status:** `VERIFIED_HOST_SPLIT`
- **Surfaces:** Qwen Code CLI, Qwen Code editor integrations, Qwen model/web fallback
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .qwen/skills/skick for project scope or ~/.qwen/skills/skick for personal scope; invoke explicitly with /skick when desired.
- **Project/local paths:** `.qwen/skills/skick/`
- **User/personal paths:** `~/.qwen/skills/skick/`
- **Generated distribution:** `shared-agent-skill.zip`
- **Adapter:** [`adapters/qwen/README.md`](../adapters/qwen/README.md)
- **Primary source:** https://qwenlm.github.io/qwen-code-docs/en/users/features/skills
- **Verification:**
  - Use the Qwen Code skills UI/command and test automatic activation; debug with the current runtime if discovery fails.
- **Sources:**
  - https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/

### replit

- **Aliases:** replit, replit
- **Status:** `VERIFIED`
- **Surfaces:** Replit
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Install project Skills under .agents/skills/skick (Replit documentation displays /.agents/skills relative to the project root), through the Skills pane, or via a compatible skills CLI flow.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/replit/README.md`](../adapters/replit/README.md)
- **Primary source:** https://docs.replit.com/build/use-agent-skills
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.
- **Sources:**
  - https://docs.replit.com/build/use-agent-skills
  - https://docs.replit.com/learn/agent-skills

### roo-code

- **Aliases:** roo, roo code, roo-code, roo vscode
- **Status:** `VERIFIED`
- **Surfaces:** VS Code extension, Roo modes
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .roo/skills/skick for project scope or ~/.roo/skills/skick for global scope; .agents/skills is also supported for cross-agent sharing.
- **Project/local paths:** `.roo/skills/skick/`, `.agents/skills/skick/`
- **User/personal paths:** `~/.roo/skills/skick/`, `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/roo-code/README.md`](../adapters/roo-code/README.md)
- **Primary source:** https://roocodeinc.github.io/Roo-Code/features/skills/
- **Verification:**
  - Ask Roo for a task matching SKick and confirm the skill loads.
  - If using mode-specific skills, keep SKick in the generic skills root unless a deliberate mode override is desired.
- **Sources:**
  - https://roocodeinc.github.io/Roo-Code/features/skills/

### sarvam

- **Aliases:** sarvam, sarvam model
- **Status:** `HOST_RUNTIME_OR_GENERIC_FALLBACK`
- **Surfaces:** model/provider surfaces
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use the actual host runtime adapter when known; otherwise use the generic prompt fallback.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/sarvam/README.md`](../adapters/sarvam/README.md)
- **Primary source:** https://www.sarvam.ai/
- **Verification:**
  - Do not infer a native Skill contract from the model family name.

### tencent-hunyuan

- **Aliases:** hunyuan, tencent hunyuan
- **Status:** `MODEL_PROVIDER_ROUTE_TO_HOST`
- **Surfaces:** Tencent Hunyuan
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Do not install SKick on the model name. Install it in the actual host coding agent/harness; if no persistent host exists, use the generic prompt fallback for the session.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **Generated distribution:** `generic-prompt.md`
- **Adapter:** [`adapters/model-provider/README.md`](../adapters/model-provider/README.md)
- **Primary source:** https://agentskills.io/home
- **Verification:**
  - Confirm which agent/harness actually runs the model, then verify SKick in that host.

### trae

- **Aliases:** trae, trae ide, trae solo, trae code, bytedance trae, trae cn
- **Status:** `VERIFIED_PRODUCT_ECOSYSTEM`
- **Surfaces:** TRAE IDE, TRAE SOLO, TRAE VS Code/plugin-style surfaces where Skills are exposed
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .trae/skills/skick for project scope. For global scope use the product-specific global skill root documented by the installed TRAE edition (commonly ~/.trae/skills; TRAE CN may use ~/.trae-cn/skills). The Skills UI can also import external skills where available.
- **Project/local paths:** `.trae/skills/skick/`
- **User/personal paths:** `~/.trae/skills/skick/`, `~/.trae-cn/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/trae/README.md`](../adapters/trae/README.md)
- **Primary source:** https://www.trae.ai/
- **Verification:**
  - Refresh/reload TRAE skill discovery or use the Skills/Commands UI.
  - Invoke SKick by name or run a matching task and confirm the runtime loads the skill rather than only copying files.
- **Sources:**
  - https://www.trae.ai/
  - https://forum.trae.cn/t/topic/67755

### warp

- **Aliases:** warp, warp
- **Status:** `VERIFIED`
- **Surfaces:** Warp
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .agents/skills/skick or .warp/skills/skick for project scope and ~/.agents/skills/skick (or another currently documented Warp Skill root) for global scope.
- **Project/local paths:** `.agents/skills/skick/`, `.warp/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/warp/README.md`](../adapters/warp/README.md)
- **Primary source:** https://docs.warp.dev/knowledge-and-collaboration/warp-drive/ai-objects
- **Verification:**
  - Confirm the Skill appears in Warp Agent/Skills discovery and invoke it with /skick or a matching task.
  - For cloud/Oz runs, verify the selected environment actually contains the repository Skill.
- **Sources:**
  - https://docs.warp.dev/knowledge-and-collaboration/warp-drive/ai-objects
  - https://docs.warp.dev/changelog

### windsurf

- **Aliases:** windsurf, cascade, windsurf cascade
- **Status:** `VERIFIED`
- **Surfaces:** Windsurf IDE, Cascade
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .windsurf/skills/skick for workspace scope or ~/.codeium/windsurf/skills/skick for global scope. SKick can be auto-invoked by description or explicitly mentioned in Cascade.
- **Project/local paths:** `.windsurf/skills/skick/`
- **User/personal paths:** `~/.codeium/windsurf/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/windsurf/README.md`](../adapters/windsurf/README.md)
- **Primary source:** https://docs.windsurf.com/windsurf/cascade/skills
- **Verification:**
  - Open Cascade Customizations > Skills and confirm SKick is listed.
  - Use @SKick or a matching prompt and confirm its instructions/resources load.
- **Sources:**
  - https://docs.windsurf.com/windsurf/cascade/skills

### zcode

- **Aliases:** zcode, z.ai zcode, z code
- **Status:** `VERIFIED`
- **Surfaces:** ZCode Agent, remote/SSH/WSL workspaces
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use ~/.zcode/skills/skick for user scope or ZCode Settings > Skills import/copy/symlink flows for supported external/project installs; use the generated plugin for distributable bundles when appropriate.
- **Project/local paths:** Managed/UI or host-dependent; no filesystem path asserted.
- **User/personal paths:** `~/.zcode/skills/skick/`
- **Generated distribution:** `zcode-plugin.zip`
- **Adapter:** [`adapters/zcode/README.md`](../adapters/zcode/README.md)
- **Primary source:** https://zcode-ai.github.io/zcode-docs/
- **Verification:**
  - Open Settings > Skills, Refresh, and confirm SKick is enabled under the expected source.
  - For remote workspaces, verify the skill exists on the remote host or use the supported sync flow.

### zed

- **Aliases:** zed, zed
- **Status:** `VERIFIED`
- **Surfaces:** Zed
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Use .agents/skills/skick in a trusted worktree for project scope or ~/.agents/skills/skick for user scope. Keep the Skill directory as a direct child of the Skills root and verify Zed discovery after changes.
- **Project/local paths:** `.agents/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/zed/README.md`](../adapters/zed/README.md)
- **Primary source:** https://zed.dev/docs/ai/skills
- **Verification:**
  - Verify the active runtime discovers SKick after installation.
  - Re-check current first-party documentation before scripting installation for a release-sensitive environment.
- **Limitations / caveats:**
  - Project Skills require a trusted worktree.
  - Keep Skill metadata lean; large catalogs can consume discovery budget.
- **Sources:**
  - https://zed.dev/docs/ai/skills

### zencoder

- **Aliases:** zencoder, zencoder / zenflow
- **Status:** `VERIFIED`
- **Surfaces:** Zencoder / Zenflow
- **Availability / gating:** Host/plan/version dependent; see current first-party documentation and adapter.
- **Preferred install:** Prefer the current open-standard .agents/skills/skick project/user roots. Zencoder also reads .claude/skills; legacy .zencoder/skills remains deprecated compatibility only.
- **Project/local paths:** `.agents/skills/skick/`, `.claude/skills/skick/`
- **User/personal paths:** `~/.agents/skills/skick/`
- **Generated distribution:** `runtime-skill.zip`
- **Adapter:** [`adapters/zencoder/README.md`](../adapters/zencoder/README.md)
- **Primary source:** https://docs.zencoder.ai/features/skills
- **Verification:**
  - Confirm SKick is discovered in Zencoder/Zenflow for the selected workspace/user scope.
  - Use a matching task; current Zencoder documentation says manual Skill selection is not supported.
- **Limitations / caveats:**
  - Legacy .zencoder/skills is deprecated; prefer .agents/skills.
  - Do not promise manual Skill selection where the current surface only auto-selects.
- **Sources:**
  - https://docs.zencoder.ai/features/skills
