# Query Mutation Engine

## Purpose
Search semantically, iteratively, and version-consciously rather than repeating the user's wording.

## Concept extraction
Identify relevant:
- entity/product/library;
- feature/component;
- symptom/behavior;
- expected behavior;
- error text;
- function/class/symbol/configuration;
- version/environment;
- architecture concept;
- possible synonyms or historical names.

## Query families
Batch related variants rather than issuing one search per tiny wording change.

### A — Canonical terminology
Search the user term plus likely official/internal terms, synonyms, acronyms/full forms, renamed APIs, specification language, and competitor terminology.

### B — Behavior and symptom
Search expected behavior, failure behavior, state loss/reset, unexpected result, exact error strings in quotes, and observable symptoms.

### C — Implementation symbols
Search exact class/function/config/exception names, including forms such as `function_name(` or constants.

### D — Version and migration
Search feature + version, migration, breaking change, deprecated, removed, replacement, changelog, release notes, historical behavior, old class/module names.

### E — Repository evidence
Use site/repository scopes for source, issues, PRs, discussions, tests, commits, releases, tags, and design docs.

### F — Negative/adversarial evidence
Search `unsupported`, `limitation`, `does not work`, `cannot`, `bug`, `regression`, `unexpected`, `won't fix`, `not planned`, and platform-specific failure forms.

### G — Alternatives and related implementations
Search alternatives, comparisons, ports, wrappers, forks, and how other ecosystems name or implement the same mechanism.

### H — Production/security/performance
When relevant, search incidents, postmortems, CVEs/advisories, benchmarks, scale behavior, production migrations, and operational failure modes.

### I — Lateral terminology and source evaluation
Search renamed/trendy terms, old terminology, implementation analogues, translations, adjacent ecosystems, and the provenance/reputation of unfamiliar sources. Use `coverage-and-lateral-search.md` for the full lateral workflow.

### J — Mechanism and analogy
Search the underlying behavior/primitive/causal pathway plus analogous implementations in other domains when the user-facing label may be misleading. Verify analogies before transferring conclusions.

## Search operators
Use targeted operators when supported:
- domain/site filters for official docs, repositories, issue trackers, standards, arXiv, Stack Overflow;
- exact phrases for errors/symbols;
- version + feature + migration combinations;
- exclusions when noise is high.

Search snippets are discovery only; open the underlying source.

## Iterative terminology discovery
New evidence may reveal better terms. Immediately branch searches from those terms.

Example:
`memory -> persistence -> checkpoint -> checkpointer -> thread state -> store`

Maintain a compact evolving vocabulary rather than a fixed initial query list.

## Research graph
Follow evidence links across:
`docs -> source -> test -> issue -> PR -> commit -> release -> spec -> production report -> alternative implementation`.

Do not force research into a linear search sequence.

## Bug-root-cause query strategy
Trace:
`symptom/error -> call path/symbol -> dependency behavior -> version-specific implementation -> issue/PR -> patch -> regression test -> fix/release`.

Separate symptom, immediate failure, trigger, underlying mechanism, root cause, environment/version condition, fix, workaround, and regression protection.

## Saturation
Stop expanding query families when important uncertainties are resolved and new mutations mostly reproduce existing evidence.
