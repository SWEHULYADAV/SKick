# Plans, Surfaces, and Skill Availability

Last reviewed: **2026-09-03**.

Plan names, regional rollouts, admin controls, and product surfaces change faster than SKick's core methodology. Treat this page as a routing snapshot, not a permanent entitlement guarantee. Before a consequential or automated install, re-check the linked first-party source.

## The rule that prevents most installation mistakes

Separate three questions:

1. **What model/provider is answering?** Examples: Qwen, MiniMax, DeepSeek, GLM, Llama.
2. **What host/runtime loads Skills?** Examples: Codex, Claude Code, Cursor, OpenCode, Qwen Code, Kimi Code.
3. **What surface/account is active?** Examples: ChatGPT Business workspace, Claude Free web, Gemini Spark, a local CLI, a cloud coding agent.

Install SKick into the **host/runtime that actually discovers Skills**. A model name is not a filesystem destination.

## Major managed surfaces

| Surface | Current SKick route | Availability/gating snapshot |
|---|---|---|
| ChatGPT chat | upload canonical `skill.zip` | Native custom Skills are currently documented for eligible Business, Enterprise, Healthcare, and Edu workspaces; workspace settings/product availability still apply. |
| Claude web/app | upload `claude-web-skill.zip` | Custom Skills are currently documented for Free, Pro, Max, Team, and Enterprise; code execution must be enabled. |
| Gemini Apps | upload `gemini-apps-skill.zip` in Gemini Spark | 18+, personal Google Account, Keep Activity, qualifying Google AI subscription, and current geographic availability are required; work/school accounts are not supported. |
| Manus | managed GitHub import/upload | Use the current Manus Skills UI; no local filesystem path is asserted. |
| Mistral Vibe Work | managed product flow | Re-check current workspace/plan behavior before automation. |

Sources:
- https://help.openai.com/en/articles/20001066
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://support.google.com/gemini/answer/17094296?hl=en

## Coding-agent hosts

Coding hosts usually make SKick easier to use than managed chat surfaces because project-local Skills can be versioned with the repository. Important current routes include:

| Host | Preferred project route | Notes |
|---|---|---|
| Codex | `.agents/skills/skick/` | Codex plan availability is separate from ChatGPT chat's native Skill-upload gate. |
| Claude Code | `.claude/skills/skick/` | Project/local by default; plugin distribution is optional. |
| Cursor | `.cursor/skills/skick/` or `.agents/skills/skick/` | Verify current local/cloud-worker discovery behavior. |
| GitHub Copilot | `.github/skills/skick/` or `.agents/skills/skick/` | GitHub CLI 2.90+ provides `gh skill preview/install/update`; always preview untrusted Skills first. |
| Gemini CLI | `.gemini/skills/skick/` or `.agents/skills/skick/` | Native `gemini skills` workflow can install from Git sources. |
| OpenCode | `.opencode/skills/skick/` or `.agents/skills/skick/` | Project/shared Agent Skills are first-class. |
| Qwen Code | `.qwen/skills/skick/` | Model/provider authentication is separate from Skill support. |
| Kimi Code | `.kimi-code/skills/skick/` or `.agents/skills/skick/` | Canonical explicit invocation is `/skill:skick`. |
| MiMoCode | `.mimocode/skills/skick/` | Do not invent a personal path not documented by the active release. |
| Kilo Code | `.kilo/skills/skick/` or `.agents/skills/skick/` | `.kilocode/skills` should be treated as legacy unless a current release explicitly documents it. |
| Kiro | `.kiro/skills/skick/` | GitHub import expects a Skill subdirectory or direct `SKILL.md` URL, not an arbitrary repository root. |
| Qoder | `.qoder/skills/skick/` | QoderWork is distinct and uses `~/.qoderwork/skills/`. |
| Devin | `.agents/skills/skick/` | Repository-scoped; current docs do not assert a global `~/.devin/skills` route. |
| Zed | `.agents/skills/skick/` | Project Skills require a trusted worktree. |
| Warp | `.agents/skills/skick/` or `.warp/skills/skick/` | Cloud/Oz runs also require the selected environment to contain the Skill. |
| Zencoder/Zenflow | `.agents/skills/skick/` | `.zencoder/skills` is legacy/deprecated compatibility. |
| Replit | `.agents/skills/skick/` | Project-installed Skills persist across chats and can be version controlled. |
| Goose | `.agents/skills/skick/` | Goose documents `.agents/skills` as the recommended standard; legacy Goose/Claude roots are compatibility paths. |
| iFlow CLI | `.iflow/skills/skick/` | Project and personal Skill roots are documented; refresh/list Skills after changes. |
| Mux | `.mux/skills/skick/` | Product source exposes Skill tools and repository Skills; verify the active build before unattended rollout. |

Use `docs/PLATFORM_CATALOG.md` for the complete machine-generated 62-route inventory.

## Model/provider-only names

For MiniMax, DeepSeek, GLM, LongCat, Llama, Nova, Cohere, Granite, ERNIE, Hunyuan, ByteDance/Seed/Doubao and similar providers, ask: **which host is running this model?**

Examples:

```text
DeepSeek in Cursor -> install for Cursor
GLM in Claude Code -> install for Claude Code
MiniMax in OpenCode -> install for OpenCode
Qwen model in Codex -> install for Codex
```

Do not manufacture provider paths such as `~/.deepseek/skills/` without first-party host documentation.

## What 'installed' means

A copy/upload is only stage one:

`FILES/UPLOAD -> RUNTIME DISCOVERY -> SKILL VISIBLE -> LOW-RISK TRIGGER -> SUPPORTING FILES RESOLVE -> EXPECTED BEHAVIOR`

Report each stage separately. If a plan, region, admin policy, or runtime build blocks one stage, say so instead of claiming success.
