# Runtime and Capability Abstraction

## Model != runtime
Distinguish model family from the runtime hosting it. Configure for capabilities exposed by ChatGPT, Codex, Claude Code, Gemini CLI, Antigravity, OpenCode, IDE/browser/API/custom orchestrators, not the model name alone.

## Abstract capability contract
Map these conceptual capabilities to the strongest available native tools:

- `WEB_SEARCH`
- `WEB_READ`
- `STRUCTURED_DATA`
- `ACADEMIC_SEARCH`
- `MARKET_DATA`
- `LEGAL_GOV_DATA`
- `REPO_SEARCH`
- `CODE_SEARCH`
- `SYMBOL_SEARCH`
- `REFERENCES`
- `LANGUAGE_SERVER`
- `COMPILER`
- `TYPE_CHECKER`
- `FORMATTER_LINTER`
- `STATIC_ANALYSIS`
- `FUZZ_RUNNER`
- `PROFILER_TRACE`
- `PACKAGE_BUILD`
- `FILE_READ`
- `FILE_WRITE`
- `GIT_HISTORY`
- `SHELL`
- `TEST_RUNNER`
- `BROWSER`
- `BROWSER_AUTOMATION`
- `DESIGN_SYSTEM`
- `VISUAL_DIFF`
- `ACCESSIBILITY_TREE`
- `SUBAGENTS`
- `INDEXED_STORAGE`
- `HOOKS`
- `PERSISTENT_STATE`
- `TASKS`
- `AGENT_PROTOCOL`
- `MULTIMODAL_READ`
- `TRACE`
- `COST_METERING`
- `APPROVAL`
- `ROLLBACK`
- `ARTIFACT_HASHING`
- `SIGNING`
- `MCP_CLIENT`
- `SPECIALIST_SKILLS`
- `FORGE`
- `PRODUCTION_OBSERVABILITY`
- `SECURITY_TELEMETRY`
- `DETECTION_ENGINE`

These are conceptual names, not required literal tool names.

## Capability discovery
At the beginning of substantial work, infer silently whether the runtime can search/open the web, query structured/market/academic sources, inspect repositories/files, use semantic code search, execute commands, edit, run tests, automate a browser, inspect history, use connectors/MCP/hooks, delegate, index large outputs, or persist compact state; expose task/protocol primitives; inspect multimodal evidence; trace usage; meter cost; require approvals; support rollback; hash/sign artifacts; connect MCP providers; invoke specialist skills; access forge or production-observability systems.

Before a skill/plugin/tool integration, compare declared capabilities with actual instructions/scripts. Hidden shell/network/file-write/browser/secret access is a quality/security issue; use `external-skill-intelligence.md`.


## Engineering orchestration rule
For substantial engineering tasks, load `engineering-lifecycle.md`. If narrower specialist skills are installed, use `specialist-skill-orchestration.md`; if MCP is available, route through `mcp-stack.md`. Do not use an MCP when a native tool is stronger or when its tool schema/context overhead exceeds the value it adds.

## Source routing
Use `research-source-router.md` to map the research need to available capabilities. If a named source is unavailable, degrade to the best equivalent source and disclose the gap only when it affects confidence. Never claim an API/database was queried because it appears in the preferred-source list.

## Serena rule
If Serena is available, treat it as the preferred provider for semantic `REPO_SEARCH`, `CODE_SEARCH`, `SYMBOL_SEARCH`, `REFERENCES`, and targeted semantic edits. Otherwise map those capabilities to native code intelligence/LSP/search/grep/file tools. Combine Serena/navigation evidence with the language-native compiler/type checker/linter/analyzer/test/profiler that can prove runtime/toolchain semantics; Serena is not a substitute for those proof surfaces.

## Browser rule
For interactive web changes, prefer an actual browser/browser-automation capability for final behavioral verification. If no browser exists, run non-browser checks and provide/label remaining verification steps rather than claiming rendered success.

## Context rule
If the host offers indexed/file-backed storage or hooks, use `context-management.md` to keep oversized raw outputs out of active context while retaining searchable evidence. Do not require an external context engine when native tools are sufficient.

## Graceful degradation
`preferred capability unavailable -> equivalent native capability -> simpler search/read method -> disclose limitation only if confidence suffers`.

No Serena: native/LSP/indexed search -> repository search -> grep + targeted reads.
No live web/current data: repository/local docs/installed source -> mark currency limitation.
No execution: provide verification steps rather than claiming execution.
No browser: do not claim rendered/interaction verification.
No subagents: run branches sequentially without changing methodology.
No indexed storage: summarize source evidence compactly and preserve exact critical excerpts.
No persistent state: keep a compact checkpoint in current context/visible output and do not claim restart continuity.

## Portability
Core files remain plain Markdown and platform-neutral. Adapters may map paths, installation, permissions, MCP, hooks, or subagent syntax, but must not rewrite the research methodology or silently make optional external plugins mandatory.
