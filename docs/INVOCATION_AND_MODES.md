# SKick Invocation, Modes, and Depth

SKick should be easy to call explicitly and conservative about automatic activation.

## Explicit invocation

Treat an explicit SKick call as authoritative user intent. Examples:

```text
Use SKick to research this stack.
Use SKick to build this feature.
Use SKick to debug this issue.
Use SKick to review this repository.
Use SKick to secure this service.
Use SKick to design this interface.
Use SKick to install this package.
Use SKick to maintain/update this repository.
```

Runtime-specific syntaxes such as `/skick`, `@skick`, or a skill picker may be used when the host exposes them. Do not assume a slash/mention syntax unless the active runtime supports it.

## Automatic invocation

Auto-activate SKick when a task clearly benefits from multi-step engineering/research discipline, for example:

- repository analysis or implementation
- current technical research where sources/versions matter
- architecture or migration decisions
- debugging with multiple plausible mechanisms
- security analysis or hardening
- performance/reliability work
- browser/UI validation
- code review or release readiness
- agent/MCP/harness integration
- long-running or cross-runtime engineering work

Do not auto-activate SKick for trivial arithmetic, greetings, one-line factual answers that need no research, or unrelated creative tasks.

## Modes

Select one primary mode and add secondary lenses only when useful.

- `research` — source discovery, lateral search, verification, synthesis
- `build` — plan, implement, integrate, test, ship
- `debug` — reproduce/minimize, hypothesize, instrument, fix, regress-test
- `review` — correctness, maintainability, tests, security, compatibility
- `security` — offensive + defensive analysis within authorization/safety bounds
- `design` — product/UI/UX/interaction/system design with validation
- `install` — runtime detection, safe scope selection, install, reload, verify
- `maintain` — update, port, fork, provenance, compatibility, release work

If the user explicitly names a mode, honor it unless safety or runtime limitations require a narrower action.

## Depth

- `quick` — minimal sufficient work; no unnecessary exploration
- `standard` — normal production-quality engineering/research
- `deep` — broader source coverage, competing hypotheses, stronger verification
- `exhaustive` — bounded but wide coverage, contradiction/failure-mode search, independent review where possible

Choose `standard` by default. Escalate only when the request, uncertainty, impact, or evidence gap justifies it.

## Routing order

1. Preserve the user's exact objective and constraints.
2. Determine mode and depth.
3. Resolve runtime/tool capabilities.
4. Load only the core/reference files needed for that branch.
5. Research before planning when facts, APIs, versions, or unfamiliar systems matter.
6. Act only when implementation/change is requested.
7. Test/verify before reporting success.
8. Distinguish what was observed, inferred, attempted, and not verified.

## Executable runtime and declarative fallback

When local execution is available, `scripts/skick_runtime.py` can make depth selection, capability state, module compilation, budgets, evidence, and claim state observable. This runtime is optional. On declarative-only hosts, use the same quick/standard/deep/exhaustive semantics and progressive references directly from `SKILL.md`; mark runtime enforcement as unavailable rather than pretending it occurred.

Capability routing uses observed fit first. Named tools such as Serena may be preferred by a project policy or benchmark, but no vendor receives an unconditional global priority. Existing project architecture similarly outranks optional starter-stack profiles.
