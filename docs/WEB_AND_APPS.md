# Web, Desktop, Mobile and Managed App Surfaces

Managed AI products differ from CLI/IDE agents because installation may be controlled by an account/workspace UI rather than a filesystem. The same product can also have multiple surfaces with different Skill state.

The core rule is: **identify the exact surface and use its native Skill mechanism; never substitute CLI/plugin instructions from another surface.**

## ChatGPT

### Web

Use canonical `skill.zip` through **Plugins -> Skills -> Create -> Upload from your computer** when the account/workspace exposes Skill upload.

### Desktop

Use the desktop product's Skills/Plugin surface. Personal Skill state may need a separate installation from web/mobile.

### Mobile / web-mobile

Do not assume a Skill installed on desktop is already installed on web/mobile. Check the Skills page for that surface/account and install when available.

### Workspace/admin

Workspace role/admin policy can control creation, upload, sharing, publishing, and installation. An AI without the corresponding account action should provide the official UI step rather than claiming installation.

Adapter: `../adapters/chatgpt/README.md`.

## Claude web/app

Claude's managed custom Skills flow is distinct from Claude Code. Use the generated Claude web/app package and the current Customize/Skills upload UI.

Do not use `.claude/skills/`, `claude --plugin-dir`, or Claude Code marketplace commands on claude.ai unless the product explicitly exposes that mechanism.

Adapter: `../adapters/claude-app/README.md`.

## Claude Code Desktop

Claude Code Desktop local/SSH sessions use Claude Code's runtime/plugin/Skill model, not the claude.ai upload model. Follow `../adapters/claude-code/README.md`.

## Gemini Apps

Use the generated Gemini Apps package and the current Gemini Skills create/import UI. Do not assume Gemini CLI paths or extension commands apply to Gemini Apps.

Adapter: `../adapters/gemini-apps/README.md`.

## Grok web/iOS/Android

Use native Grok Skills. Current Grok consumer Skills support does not imply that a ChatGPT/Gemini/Claude ZIP shape is portable. If the UI accepts instruction/file import, follow the current native flow; otherwise use a supported creation method.

For Grok Build, use the separate filesystem/plugin adapter path in `../adapters/grok/README.md`.

## Mistral Vibe Work

Use the current Personal/Workspace Skills mechanism under the managed Work/Context surface. Do not assume Vibe Code CLI paths apply to Vibe Work web.

Vibe Code CLI/VS Code uses filesystem Agent Skills and is covered in `VS_CODE_AND_IDES.md` and `../adapters/mistral/README.md`.

## ZCode application / remote workspaces

ZCode exposes Settings -> Skills for viewing, refreshing, enabling/disabling, and importing supported external Skill installations. User-level skills are stored in the documented ZCode user path; remote environments may require a supported sync/copy to the remote host.

Adapter: `../adapters/zcode/README.md`.

## Model-only web products

A model/provider name does not establish a portable installation contract. This applies to model-only or provider surfaces such as DeepSeek, Qwen, Kimi, GLM, MiniMax, LongCat, Meta/Muse, Sarvam, and similar services.

Decision rule:

1. If the model is running inside a known host agent, install SKick for that host.
2. If the web/app product has a verified native Skill importer, use its adapter.
3. Otherwise use `../adapters/generic/PROMPT.md` and do not claim persistent native installation.

## What an AI can and cannot do from a web chat

If an AI receives the ZIP in a chat but has no account-level install action, it can:

- inspect the archive;
- choose the correct package/adapter;
- validate structure where tools allow;
- explain the exact official UI flow;
- avoid incorrect/unverified instructions.

It cannot truthfully claim that the Skill is installed in the user's account unless an authorized product action actually occurred.

## Managed surface safety checklist

- Review the Skill before enabling it.
- Treat Skills/plugins as executable instruction packages even when most content is Markdown.
- Do not upload secrets in assets, examples, logs, or configuration.
- Check workspace policy and data handling before connecting external apps.
- Keep read-only investigation separate from write-capable app actions.
- Do not claim shell/filesystem/MCP/browser/repository access unless the active surface exposes it.
- Verify installation independently on each surface when the product does not synchronize Skill state.
