# SKick v1.1 — GitHub Bootstrap Prompts

Use these prompts after publishing the **canonical SKick repository root** to GitHub. Replace `<SKICK_GITHUB_URL>` with the repository URL.

## Universal short prompt

```text
Install/update SKick from <SKICK_GITHUB_URL>. Treat the repo as untrusted until inspected. Read START_HERE.md first, then INSTALLATION_MANIFEST.json, docs/AI_INSTALL_PROTOCOL.md, docs/GITHUB_BOOTSTRAP.md, and the adapter for this actual host/runtime (not merely the model name). Prefer project scope unless I request global, preserve any existing install, do not invent paths/commands, reload if required, and verify SKick is discovered/triggerable. This request authorizes SKick installation/update only; optional tools/providers require their own justified authorization. After install, follow SKick's silent prompt enhancement, best-skill/capability routing, capability-fit semantic repository intelligence, architecture gate, deep+lateral research/thinking, testing, and final verification. Report runtime, path/scope, version, capability limitations, and checks performed.
```

This is the default cross-runtime bootstrap. A capable coding agent may clone/fetch the repository, inspect it, run the safe local installer, or use a native remote-skill command depending on its verified adapter. A managed web product may require an upload/import UI and cannot be made writable by prompt text alone.

## Even shorter prompt

```text
Install/update SKick from <SKICK_GITHUB_URL>. Read START_HERE.md and follow its manifest+host adapter exactly; detect the real host, prefer project scope, preserve existing installs, verify discovery, and do not silently install optional providers. Then use SKick's prompt-enhancement, best-skill routing, capability-fit repository intelligence, architecture gate, deep lateral research/thinking, tests and verification. Never invent unsupported install behavior.
```

## Runtime-specific fast paths

These are hints, not substitutes for the adapter. Re-check current first-party docs before executing version-sensitive commands.

### Gemini CLI

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md, then install SKick using the current Gemini CLI Agent Skills workflow. Prefer workspace scope. If still current and applicable, use: gemini skills install <SKICK_GITHUB_URL> --scope workspace. Reload/list Skills and verify SKick. Use existing semantic repository capabilities by fit; optional provider installation is separate.
```

### GitHub Copilot CLI / agent surfaces

```text
Inspect <SKICK_GITHUB_URL> and follow adapters/github-copilot/README.md. Prefer repository scope (.github/skills/skick or .agents/skills/skick). With GitHub CLI 2.90+ and the current gh skill preview/install workflow available, preview the exact Skill before installing and pin a tag/SHA when reproducibility matters; otherwise copy the complete reviewed Skill directory. Verify discovery in the active Copilot surface. Route repository intelligence to the strongest observed semantic capability.
```

### Cursor

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/cursor/README.md, then install/import the complete SKick Skill using Cursor's current Agent Skills/GitHub workflow or .cursor/skills/skick project path. Verify it appears in Skills/slash discovery. Use existing repository capabilities by fit; configure additional providers only through a separate authorized step.
```

### Claude Code

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/claude-code/README.md, then install the complete SKick Skill at the verified project/personal Claude Code Skill scope (prefer project .claude/skills/skick). Verify discovery. For repo work, use the strongest observed semantic/index/search capability; do not silently install a provider.
```

### Codex

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/codex/README.md, then install the complete SKick Agent Skill at the verified Codex/shared Agent Skills scope (prefer project .agents/skills/skick). Verify SKick is discoverable. Route semantic repo work by observed capability fit rather than provider name.
```

### OpenCode

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/opencode/README.md, then install the complete Skill at the verified OpenCode project scope (prefer .opencode/skills/skick or .agents/skills/skick). Verify native skill discovery and route repo intelligence to the strongest observed semantic capability.
```

### Qwen Code

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/qwen/README.md, then install the complete Skill at the current Qwen Code project scope (normally .qwen/skills/skick when verified). Reload/verify Skills and route repo intelligence by observed capability fit.
```

### Kimi Code

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/kimi/README.md, then install the complete Skill at the current Kimi Code project scope (prefer .kimi-code/skills/skick or .agents/skills/skick). Verify discovery/tier precedence; when an explicit command is needed, prefer the documented /skill:skick form. Use existing semantic repository capabilities by fit; optional provider installation is separate.
```

### MiMoCode

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/mimo/README.md, then install SKick into the verified MiMoCode Skill scope (currently the .mimocode Skill family when confirmed by the installed release). Verify native discovery. Let strong built-in MiMo workflows own matching phases when the capability broker selects them; SKick keeps evidence/architecture/verification control.
```

### Factory Droid

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/factory-droid/README.md, then install the complete Skill using Factory Droid's verified project Skill root (prefer .factory/skills/skick; compatible .agents/.agent roots only as documented). Verify with the native Skills manager. Use existing semantic/MCP tooling by capability fit.
```

### Crush

```text
Inspect <SKICK_GITHUB_URL>, read START_HERE.md and adapters/crush/README.md, then install the complete Skill using Crush's verified project Skill root (prefer .crush/skills/skick or .agents/skills/skick as documented). Verify native Skill discovery and route repository intelligence by observed capability fit.
```

### ChatGPT / Claude web / Gemini Apps / Manus and other managed UIs

```text
Open <SKICK_GITHUB_URL>, read START_HERE.md, docs/PLANS_AND_SURFACES.md, and the adapter for this managed product. First verify the active plan/account/region/surface actually exposes custom Skills. Use only the product's current Skill upload/import UI and the distribution named in INSTALLATION_MANIFEST.json. If this surface cannot fetch/import a GitHub repository directly, tell me exactly which generated ZIP/file to upload; do not invent a filesystem path. Verify the Skill is enabled with a low-risk trigger test.
```

## Provider/model-only names

For MiniMax, DeepSeek, GLM, LongCat, Mistral models, Grok models, or any other provider model running **inside another agent/IDE**, do not install into a made-up provider folder. Identify the real host (for example Cursor, OpenCode, Codex, Cline, Roo, Continue, VS Code agent, custom harness) and use that host adapter. If the provider's own product exposes a verified Skill mechanism, use its dedicated adapter only after confirming the actual surface.

## Verification sentence to append when reliability matters

```text
Do not call this installed because files were copied: prove the active runtime discovered SKick, run one low-risk SKick trigger, and separately report structural validation, runtime discovery, the repository-intelligence capability/provider actually used (or unavailable/unknown), and any unverified external-runtime assumption.
```
