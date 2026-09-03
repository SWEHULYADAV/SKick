# SKick Runtime Adapters

Adapters contain installation/discovery details for a specific host. The canonical engineering/research method remains in `../SKILL.md` and `../core/`; do not fork that method into runtime copies.

## Rule for choosing an adapter

Identify the **host runtime and surface**, not only the model provider. A DeepSeek model running inside Cursor uses the Cursor adapter; Gemini inside another coding agent uses that host's adapter. When no native Skill importer is verified, use `generic/PROMPT.md` rather than inventing a path.

## Main adapters

- `chatgpt/` — ChatGPT managed Skill upload
- `openai-plugin/`, `codex/` — OpenAI/Codex plugin and Agent Skill forms
- `claude-app/`, `claude-code/` — Claude managed Skills and Claude Code
- `cursor/`, `github-copilot/` — IDE/cloud/CLI Agent Skills
- `gemini-apps/`, `gemini-cli/` — Gemini managed upload and Gemini CLI
- `antigravity/`, `antigravity-cli/` — distinct Antigravity Agent/IDE and CLI surfaces
- `opencode/`, `qwen/`, `kimi/`, `zcode/`, `mistral/`, `grok/` — coding-agent runtimes
- `factory-droid/`, `crush/` — verified Agent Skills coding-agent runtimes
- `manus/` — managed Skill upload/direct GitHub import surface
- `deepcode/` — Deep Code third-party host documented by DeepSeek
- `deepseek/`, `glm/`, `minimax/`, `longcat/`, `meta-muse/`, `sarvam/` — model/provider routing to the real host or generic fallback
- `mimo/` — MiMoCode plus host-runtime split
- `generic/`, `custom-cli/`, `future-agent/` — capability-based fallbacks

Use `../INSTALLATION_MANIFEST.json` and `../docs/PLATFORM_CATALOG.md` for the machine-readable and human-readable support matrices.
