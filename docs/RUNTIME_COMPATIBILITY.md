# SKick Runtime Compatibility

SKick is designed around the open Agent Skills shape: a directory containing `SKILL.md` plus optional supporting files. The package must remain usable even when a new model, agent, IDE, browser agent, or harness appears after this release.

## Compatibility principle

**Install to the host, not the model.** A model name (GPT, Claude, Gemini, Qwen, Kimi, MiniMax, MiMo, LongCat, DeepSeek, GLM, Llama, Doubao/Seed, etc.) does not by itself define where a Skill lives. The host agent/harness defines discovery, activation, file access, permissions, and persistence.

## Runtime families

### 1. Native Agent Skills clients

Use the exact adapter path when first-party documentation is known. Examples in this release include Codex, Claude Code, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Qwen Code, Kimi Code, MiMoCode, Cline, Roo Code, Windsurf, and others listed in `INSTALLATION_MANIFEST.json`.

### 2. Shared `.agents/skills` clients

Many clients scan a cross-agent root such as:

```text
<project>/.agents/skills/skick/
~/.agents/skills/skick/
```

Use this only when the active host documents or demonstrably supports the shared root.

### 3. Browser-native agents

BrowserCode and similar agents combine coding-agent skill discovery with browser execution. Install SKick through the coding-agent skill mechanism, then use `core/webapp-validation.md` for browser-specific verification. Browser access and Skill discovery are separate capabilities and must be tested separately.

### 4. Managed web/app Skill upload

Use the product's current upload/import UI. Never invent a filesystem path or claim an account-level action was performed when the current environment cannot perform it.

### 5. Rules/instructions-only runtimes

If the runtime lacks a verified Skill loader but supports persistent project instructions, use a host-specific instruction adapter or `adapters/generic/PROMPT.md`. Report that progressive Skill discovery was not established.

### 6. Model/API-only surfaces

Route to the actual agent/harness. If there is no persistent host, use a session-level prompt import.

### 7. New/custom harnesses

Implement the open Agent Skills lifecycle using `docs/NEW_RUNTIME_INTEGRATION.md` and the upstream Agent Skills client implementation guide.

## Support status meanings

- `VERIFIED` — current first-party evidence establishes the relevant Skill mechanism/path.
- `VERIFIED_*` — verified with an important scope/inheritance/product distinction.
- `ECOSYSTEM_VERIFIED_RECHECK_FIRST_PARTY` — current ecosystem installers/compatibility data support the path, but the release must re-check first-party docs before scripting consequential/global installs.
- `MODEL_PROVIDER_ROUTE_TO_HOST` — provider/model has no separate SKick installation contract; use the actual host.
- `HOST_RUNTIME_OR_GENERIC_FALLBACK` — provider/model or app should use a host adapter or session fallback.

## Future-proof fallback chain

1. Exact verified adapter.
2. Documented native Agent Skill root.
3. Documented shared `.agents/skills` root.
4. Persistent instruction/rule integration.
5. Session prompt fallback.
6. Custom harness implementation of Agent Skills.

If no step can be verified, stop and ask which host/runtime the user is actually using. Never guess an installation path.


## GitHub-source compatibility

A repository URL is portable only as **source transport**. The target AI still has to identify the active runtime, inspect the repository, choose the matching manifest adapter, and verify Skill discovery. See `../BOOTSTRAP_PROMPTS.md` and `GITHUB_BOOTSTRAP.md`.

Known first-class routes now also include Factory Droid and Crush Agent Skills plus Manus managed Skill import. For any new runtime, prefer an explicit verified adapter or the Agent Skills standard before persistent-instructions/session-prompt fallbacks.

## Capability quality after installation

Installation does not mean SKick should monopolize all work. On non-trivial tasks, the installed Skill must use `../core/capability-and-skill-routing.md` to select the strongest available task-matched specialist/native capability. For repository engineering, apply the Serena-first gate and architecture/change-impact gate before broad coding.
