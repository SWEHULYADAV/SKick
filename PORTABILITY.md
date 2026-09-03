# SKick Portability and Runtime Support

Verification baseline: **2026-09-03**. Runtime behavior changes quickly, so version-sensitive installation must be rechecked before unattended automation.

## The central rule

**Install SKick into the host runtime that loads Skills, not into the model/provider name.**

A MiniMax, MiMo, Qwen, Kimi, LongCat, DeepSeek, GLM, ByteDance/Seed, Llama, Nova, Cohere, Granite, ERNIE, Hunyuan, or other model may run inside many different agents. The host controls Skill discovery, paths, permissions, invocation, tools, and reload behavior.

## Support classes

SKick uses explicit support classes rather than pretending all platforms are equivalent:

- **VERIFIED** — current first-party documentation/source establishes the relevant Skill/upload contract.
- **VERIFIED_REPO** — current first-party evidence establishes repository-scoped Skill support, while user/org/global scope may still require separate verification.
- **VERIFIED_MANAGED_IMPORT** — current product documentation establishes a managed Skill import/share surface without asserting a filesystem root.
- **VERIFIED_HOST_SPLIT / VERIFIED_INHERITED** — a provider or fork is routed through a documented host/upstream mechanism, with runtime verification still required.
- **ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY** — credible ecosystem tooling documents a path, but first-party confirmation must be rechecked before unattended automation.
- **HOST_RUNTIME_OR_GENERIC_FALLBACK** — no independent provider-specific Skill root is asserted; install in the actual host or use a non-persistent prompt fallback.
- **GENERIC_CAPABILITY_BASED** — custom/future runtime; detect capability and implement the open Agent Skills lifecycle when possible.

These statuses are stored in `INSTALLATION_MANIFEST.json` and rendered in `docs/PLATFORM_CATALOG.md`. Plan, region, account and surface gates are tracked separately in `docs/PLANS_AND_SURFACES.md`; a technically supported Skill format does not imply every account can use it.

## Portable representations

1. **Canonical Agent Skill** — the SKick directory with `SKILL.md` and referenced resources.
2. **Runtime Skill ZIP** — a generated `skick/` directory archive for runtimes that want a portable Skill folder.
3. **Shared Agent Skill ZIP** — `.agents/skills/skick/` layout for hosts that explicitly support the shared root.
4. **Agent Plugins v1** — only for clients that explicitly support the standard.
5. **Host wrapper** — generated only when a distinct plugin/archive shape is documented.
6. **Generic prompt** — last-resort session/instruction fallback; never described as persistent installation.

## Verified or specially routed platforms

| Platform/runtime | Install model | Notes |
|---|---|---|
| ChatGPT | managed Skill upload | canonical `skill.zip`; native custom Skill upload is plan/workspace gated—see `docs/PLANS_AND_SURFACES.md` |
| Codex | Agent Skill / plugin | `.agents/skills`; Codex entitlement is separate from ChatGPT chat custom-Skill upload |
| Claude Code | Agent Skill / plugin | `.claude/skills/` or documented plugin flow |
| Claude web/app | managed Skill upload | separate package shape from Claude Code |
| GitHub Copilot | Agent Skill | project `.github/skills`, `.agents/skills`, `.claude/skills`; personal roots documented by GitHub |
| Cursor | Agent Skill | Cursor/shared roots; verify active Agent discovery |
| Gemini CLI | Agent Skill | Gemini/shared roots and CLI Skill controls |
| Gemini Apps | managed upload | generated text-only archive; do not include binary branding in that package |
| Factory Droid | Agent Skill | `.factory/skills`, compatible `.agents/skills` / `.agent/skills` roots |
| Crush | Agent Skill | `.crush/skills`, `.agents/skills` and documented compatible roots |
| Manus | managed Skill import | use current managed import/share/upload controls; no filesystem root asserted |
| Antigravity | Agent Skill | use documented Agent Skill roots, not a fabricated plugin |
| OpenCode | Agent Skill | `.opencode/skills`, `.agents/skills`, compatible roots |
| BrowserCode | OpenCode-compatible Agent Skill | BrowserCode is OpenCode-derived and contains OpenCode Skill structure; live discovery must still be checked |
| Qwen Code | Agent Skill / Agent Plugins v1 | `.qwen/skills`; verify the active Qwen Code invocation surface |
| Kimi Code | Agent Skill / plugin | `.kimi-code/skills` / `.agents/skills`; canonical explicit invocation is `/skill:skick` |
| MiMoCode | Agent Skill host | Xiaomi MiMoCode carries an OpenCode-derived Skill system; use MiMoCode adapter when it is the host |
| MiniMax | provider-to-host | official MiniMax Skills target hosts such as Claude Code, Cursor, Codex, OpenCode |
| LongCat | provider-to-host | install into the actual coding harness using LongCat |
| TRAE | host Agent Skill | use TRAE adapter when TRAE is the host; ByteDance model selection alone is not an install path |
| Cline | Agent Skill | `.cline/skills` project/personal roots |
| Roo Code | Agent Skill | Roo-specific/shared roots |
| Windsurf | Agent Skill | Windsurf workspace/global roots |
| Mistral Vibe | Skill runtime | adapter distinguishes Code vs managed Work surfaces |
| ZCode | Skill runtime | adapter defines current import/discovery route |
| Amp | Agent Skill | `.agents/skills`; native Skill commands and documented user scope |
| Augment | Agent Skill | `.augment/skills`, `.agents/skills`, compatible Claude roots |
| JetBrains Junie | Agent Skill | `.junie/skills` / `.agents/skills` |
| Kilo Code | Agent Skill | `.kilo/skills` / `.agents/skills`; older `.kilocode/skills` is legacy |
| Kiro | Agent Skill | `.kiro/skills`; GitHub import targets a Skill directory/`SKILL.md` |
| Devin | repository Agent Skill | prefer `.agents/skills`; no global `~/.devin/skills` asserted |
| OpenHands | repository Agent Skill | `.openhands/skills` / `.agents/skills`; managed scopes recheck |
| Pi | Agent Skill | `.pi/skills` / `.agents/skills`; respect project trust |
| Qoder | Agent Skill | `.qoder/skills`; QoderWork is a distinct surface |
| Replit | repository Agent Skill | `.agents/skills` / Skills pane |
| Warp | Agent Skill | `.agents/skills` / `.warp/skills` |
| Zed | Agent Skill | `.agents/skills`; trusted worktree required for project Skills |
| Zencoder / Zenflow | Agent Skill | prefer `.agents/skills`; legacy `.zencoder/skills` deprecated |

The full catalog also includes conservative/recheck routes such as Continue, Goose, Mux, iFlow CLI, MCPJam, Neovate, Aider Desk and other evolving hosts. Those entries remain intentionally conservative until current first-party evidence is strong enough.

## BrowserCode

BrowserCode is treated as a first-class target. Current source identifies it as OpenCode-derived and its repository includes OpenCode-style `.opencode/skills/*/SKILL.md` content. SKick therefore routes BrowserCode to:

```text
.opencode/skills/skick/
.agents/skills/skick/            # when supported by the installed build
~/.config/opencode/skills/skick/
~/.agents/skills/skick/          # when supported by the installed build
```

A copy into one of these paths is **not** a claim of runtime success; the active BrowserCode build must still discover and invoke SKick.

## Unknown/future agents and harnesses

A missing brand name does not make SKick unusable. Route by capability:

1. inspect the runtime's first-party documentation/source;
2. if it implements Agent Skills, use its native root;
3. if it explicitly supports `.agents/skills`, use that shared root;
4. if it supports persistent instructions with file/resource access, adapt SKick without pretending that is native Agent Skills;
5. otherwise use `adapters/generic/PROMPT.md` for the current session;
6. if you control the harness, implement discovery -> metadata -> activation -> on-demand resources using `docs/NEW_RUNTIME_INTEGRATION.md`.

Never guess a hidden directory, manifest, command, extension, or marketplace package.

## Source of truth

- Machine router: `INSTALLATION_MANIFEST.json`
- GitHub bootstrap prompts: `BOOTSTRAP_PROMPTS.md`
- GitHub bootstrap protocol: `docs/GITHUB_BOOTSTRAP.md`
- Full rendered table: `docs/PLATFORM_CATALOG.md`
- Installation policy: `docs/INSTALLATION.md`
- Runtime-family logic: `docs/RUNTIME_COMPATIBILITY.md`
- New/custom runtime guide: `docs/NEW_RUNTIME_INTEGRATION.md`
- Per-runtime details: `adapters/`
- Evidence ledger: `SOURCES.md`

## Verification boundary

Structural validation can prove that SKick's source, manifests, links, scripts, and generated archive shapes are internally consistent. It cannot prove that every third-party product version successfully executes SKick. A release report must state which checks were local/structural and which were live runtime tests.
