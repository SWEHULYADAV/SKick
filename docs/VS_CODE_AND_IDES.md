# SKick in VS Code, JetBrains and IDE Agents

**Install SKick for the agent runtime powering the editor, not for VS Code/JetBrains generically.** Multiple agents can coexist in one IDE and use different Skill roots.

## GitHub Copilot

Project:

```text
.github/skills/skick/
.agents/skills/skick/
.claude/skills/skick/   # GitHub documents this compatible project root
```

Personal:

```text
~/.copilot/skills/skick/
~/.agents/skills/skick/
```

Copilot Agent Skills apply across cloud agent, code review, CLI/app, VS Code agent mode, and JetBrains agent mode. In Copilot CLI, reload Skills if required and verify the discovered list.

Adapter: `../adapters/github-copilot/README.md`.

## Cline

Project:

```text
.cline/skills/skick/
```

Personal:

```text
~/.cline/skills/skick/
```

Enable the Skills feature where required, verify SKick in the Skills UI, and use `/skick` when explicit invocation is supported.

Adapter: `../adapters/cline/README.md`.

## Roo Code

Project:

```text
.roo/skills/skick/
.agents/skills/skick/
```

Personal:

```text
~/.roo/skills/skick/
~/.agents/skills/skick/
```

Keep SKick in the generic Skill root unless a deliberate mode-specific override is needed.

Adapter: `../adapters/roo-code/README.md`.

## Windsurf / Cascade

Workspace:

```text
.windsurf/skills/skick/
```

Global:

```text
~/.codeium/windsurf/skills/skick/
```

Verify through Cascade's current Skills/customizations surface and an explicit or matching task.

Adapter: `../adapters/windsurf/README.md`.

## Claude Code

Project:

```text
.claude/skills/skick/
```

Personal:

```text
~/.claude/skills/skick/
```

Claude Code VS Code/JetBrains/local sessions use Claude Code runtime behavior. Do not apply claude.ai managed-upload instructions to Claude Code.

Adapter: `../adapters/claude-code/README.md`.

## Cursor

Project:

```text
.cursor/skills/skick/
.agents/skills/skick/
```

Personal:

```text
~/.cursor/skills/skick/
~/.agents/skills/skick/
```

Verify via Cursor's current Skill/customization discovery.

Adapter: `../adapters/cursor/README.md`.

## Codex

Prefer the documented Agent Skill root for standalone project/user use:

```text
.agents/skills/skick/
~/.agents/skills/skick/
```

Use a Codex plugin wrapper only when plugin packaging is intentional.

Adapter: `../adapters/codex/README.md`.

## Gemini CLI in an IDE terminal

Project:

```text
.gemini/skills/skick/
.agents/skills/skick/
```

Personal:

```text
~/.gemini/skills/skick/
~/.agents/skills/skick/
```

Verify with current Gemini CLI Skill listing/reload controls. Do not assume every Gemini-branded IDE surface independently imports Gemini CLI Skills.

Adapter: `../adapters/gemini-cli/README.md`.

## Qwen Code

Project:

```text
.qwen/skills/skick/
```

Personal:

```text
~/.qwen/skills/skick/
```

Qwen Code supports automatic model invocation and explicit `/<skill-name>` invocation; `/skick` is the natural explicit call for SKick when user invocation is enabled.

Adapter: `../adapters/qwen/README.md`.

## Kimi Code

Use the documented Kimi project/user/shared Skill roots. Do not assume “Kimi model in another extension” means Kimi Code is the host.

Adapter: `../adapters/kimi/README.md`.

## MiMoCode (Xiaomi)

MiMoCode is an OpenCode-derived coding host with built-in Skills. Project override:

```text
.mimocode/skills/skick/
```

Use only user-level roots documented by the installed release. If a MiMo model is selected inside another IDE agent, install SKick for that agent instead.

Adapter: `../adapters/mimo/README.md`.

## OpenCode

Project:

```text
.opencode/skills/skick/
.agents/skills/skick/
```

Personal:

```text
~/.config/opencode/skills/skick/
~/.agents/skills/skick/
```

Adapter: `../adapters/opencode/README.md`.

## BrowserCode

BrowserCode is OpenCode-derived and its source carries OpenCode Skill structure. Use the OpenCode-compatible roots described in `../adapters/browsercode/README.md`, then verify discovery in BrowserCode itself. Browser/CDP access is a separate runtime capability from Skill loading.

## TRAE

When TRAE is the actual host, use its current Skill mechanism/path documented in `../adapters/trae/README.md`. If ByteDance/Seed/Doubao is merely the selected model in a different agent, install for that different host.

## MiniMax, LongCat, DeepSeek, GLM and other model providers

These model/provider names do not define an IDE Skill root. Install SKick for the host: Copilot, Claude Code, Cursor, Cline, Roo, Windsurf, OpenCode, BrowserCode, Qwen Code, Kimi Code, TRAE, etc.

## Additional IDE/agent ecosystems

The full manifest also routes Continue, Goose, Kiro CLI, Junie, OpenHands, Replit, Warp, Devin, Amp, Augment, Kilo Code, Qoder, Pi, Mux, Zed, iFlow, MCPJam, Zencoder, Neovate, and Aider Desk. Ecosystem-derived paths remain explicitly labeled for first-party recheck before automation.

## Verification checklist

1. Confirm the active agent/runtime identity and version.
2. Confirm the Skill folder is exactly `skick` and contains `SKILL.md`.
3. Preserve the complete directory so referenced resources resolve.
4. Check duplicate-name precedence across project/user/plugin roots.
5. Reload/refresh only as documented.
6. Confirm the active runtime lists or actually invokes SKick.
7. Verify MCP/browser/terminal/repository capabilities separately.
8. In remote/container/WSL/SSH setups, verify the Skill exists on the filesystem the agent actually reads.
