# Serena Integration — Serena-First Engineering Gate

## Status
**Serena is first-class and important to this research system.** For repository/code engineering, SKick must check for Serena before broad file-by-file exploration and **prefer Serena automatically** when it is available and appropriate. The workflow must still remain functional when Serena is unavailable.

Serena provides semantic repository exploration, symbol discovery/search, references/call relationships and targeted symbol-level edits through language-server/IDE-backed capabilities and supported MCP clients.

## Serena-first gate
For a non-trivial repository task:
1. determine whether Serena is already available in the active host;
2. activate/identify the correct project context;
3. use semantic symbol/references tools to build the initial code map before broad reads;
4. use native file/search/git/test/runtime tools for configuration, prose, generated assets, history and verification;
5. if Serena is unavailable or unsuitable, use the strongest native semantic/LSP/indexed fallback and continue;
6. report the fallback only when it materially affects confidence/editing safety or when the user explicitly requested Serena.

Do not claim Serena was used when it was not available. Do not stall an otherwise solvable task solely because Serena is missing.

## Installation/source rule
Use Serena only from the canonical `oraios/serena` project/current official package guidance. Re-check current official instructions before installing/configuring because client commands and contexts can change.

A general SKick task does **not** authorize silently installing Serena or any other executable/MCP. A bootstrap/install request that explicitly asks to configure SKick **and Serena** authorizes attempting the named Serena setup only when the host supports it, current official setup is verifiable, permissions are appropriate, and no credentials are embedded in the package.

Current official patterns may include launching `serena start-mcp-server` and using `--project-from-cwd` for a single active repository, but adapters must re-verify exact commands/context names before execution.

## Automatic selection rule

```text
IF repository/code work is non-trivial:
    CHECK Serena availability first
IF Serena is available and appropriate:
    automatically prefer Serena for:
    - semantic repository exploration
    - symbol discovery/search
    - references/call relationships
    - code understanding/structure
    - targeted symbol-level edits
ELSE:
    fall back to:
    - host-native semantic code intelligence / LSP / index
    - repository/file search
    - grep/ripgrep or equivalent
    - uploaded project files
    - available coding/editing tools
```

Do not make the user repeat this preference per task.

## Preferred Serena workflow
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

## Why it is preferred
Semantic definitions/references can reduce broad repository reads, improve call-relationship understanding and make targeted refactors safer in large codebases. This preference is about capability quality, not model/vendor identity.
