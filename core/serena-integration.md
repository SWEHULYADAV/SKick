# Serena Integration — Semantic Repository Provider Profile

## Status
**Serena is an optional semantic repository capability provider, not a constitutional preference.** Select it when observed capabilities, project fit, trust, context cost, and measured utility make it the best owner for repository mapping/editing. The workflow must remain functional when Serena is absent or a host-native semantic index/LSP is a better fit.

Serena provides semantic repository exploration, symbol discovery/search, references/call relationships and targeted symbol-level edits through language-server/IDE-backed capabilities and supported MCP clients.

## Capability-fit gate
For a non-trivial repository task:
1. determine which semantic repository capabilities are actually available in the active host;
2. compare Serena, native index/LSP, symbol/reference APIs, and exact-search fallbacks on task fit and proof quality;
3. when Serena wins that comparison, activate/identify the correct Serena project context and use its semantic symbol/reference tools to build the initial code map;
4. use native file/search/git/test/runtime tools for configuration, prose, generated assets, history and verification;
5. if Serena is unavailable or unsuitable, use the strongest native semantic/LSP/indexed fallback and continue;
6. report the fallback only when it materially affects confidence/editing safety or when the user explicitly requested Serena.

Do not claim Serena was used when it was not available. Do not stall an otherwise solvable task solely because Serena is missing.

## Installation/source rule
Use Serena only from the canonical `oraios/serena` project/current official package guidance. Re-check current official instructions before installing/configuring because client commands and contexts can change.

A general SKick task does **not** authorize silently installing Serena or any other executable/MCP. A bootstrap/install request that explicitly asks to configure SKick **and Serena** authorizes attempting the named Serena setup only when the host supports it, current official setup is verifiable, permissions are appropriate, and no credentials are embedded in the package.

Current official patterns may include launching `serena start-mcp-server` and using `--project-from-cwd` for a single active repository, but adapters must re-verify exact commands/context names before execution.

## Selection rule

Serena is selected only after the capability broker compares available semantic-repository implementations. Provider identity alone contributes no global score bonus.

```text
IF repository/code work benefits from semantic mapping:
    DISCOVER available semantic repository capabilities
    COMPARE task fit, trust, proof quality, context/latency cost, and edit/test support
    SELECT the strongest suitable provider
    IF selected provider is Serena:
        use the Serena workflow below
    ELSE:
        use the selected native/LSP/index/search provider
IF no semantic provider is usable:
    fall back to repository/file search + targeted reads
```

Do not require the user to name a provider unless the provider choice materially changes permissions, cost, or outcome.

## Serena workflow when selected
1. Activate/identify the correct project context.
2. Get a compact repository/symbol overview around the public seam or suspected mechanism.
3. Locate relevant definitions without reading whole files.
4. Discover references/callers to establish the change-impact boundary.
5. Read only relevant symbol bodies and nearby context.
6. Use semantic/project search for configuration/non-symbol text when supported; otherwise use native search.
7. Feed the map into `system-design-and-architecture.md` before broad implementation.
8. Apply targeted edits where semantic editing is safe.
9. Re-check references and tests after edits.
10. Use git diff/build/tests/runtime/browser/benchmark/security evidence as appropriate for final verification.

## Project activation discipline
Do not assume the current directory equals the correct Serena project. Confirm project context from repository markers/current host evidence. If automatic project inference fails, activate the intended project explicitly using the current supported Serena/client mechanism rather than guessing paths or declaring the repository unavailable.

## Do not misuse Serena
- Do not force Serena for binary assets, generated files, prose-only docs or tasks better handled by direct file tools.
- Do not assume a language-server feature exists for every language.
- Do not infer behavior from symbol names alone.
- Do not let Serena replace project tests, runtime evidence, git/history, browser checks or external current-version research.
- Do not treat an MCP marketplace entry as canonical installation authority.

## Capability mapping
Map Serena conceptually to:
- `REPO_SEARCH`
- `CODE_SEARCH`
- `SYMBOL_SEARCH`
- `REFERENCES`
- selected `FILE_READ`
- selected `FILE_WRITE` / semantic edit capabilities.

Web research, version verification, git history, shell, tests, browser and deployment remain independent capabilities.

## Graceful fallback
If Serena cannot be used, continue with the strongest available native semantic/indexed tools; otherwise use exact repository search plus targeted file reads and grep. Preserve the same architecture/change-impact and verification gates.

## Why it can be valuable
Semantic definitions/references can reduce broad repository reads, improve call-relationship understanding and make targeted refactors safer in large codebases. Selection is about capability quality, not model/vendor identity. Prefer another provider when it produces stronger evidence or lower cost for the active task.
