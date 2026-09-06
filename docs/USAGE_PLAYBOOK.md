# SKick Usage Playbook

## What

SKick is an engineering/research control plane. It adds process intelligence to a compatible AI runtime: intent resolution, research, repository mapping, architecture, implementation, testing, review, security, provenance, and delivery.

## Why

Use it to reduce common agent failures such as coding before understanding the problem, trusting stale documentation, over-scaffolding simple projects, skipping tests, misreading model names as runtime capabilities, blindly enabling MCP servers, or presenting guesses as verified facts.

## When

Use SKick automatically for substantial technical/research work, especially when one or more of these are true:

- the answer depends on current or external evidence;
- a repository/codebase must be understood before editing;
- architecture, migration, performance, security or reliability decisions are involved;
- a new project needs a research-backed plan before implementation;
- the task spans tools, MCPs, plugins, skills or multiple runtimes;
- the task is deep/exhaustive or long-running;
- the work involves uncertainty, contradictory evidence, version drift or terminology drift;
- the UI requires design/motion/browser validation;
- offensive behavior, abuse paths, hostile input or bypasses could materially affect the design;
- the output will be used for a consequential decision.

Do not inflate tiny tasks. A small deterministic edit should remain a small deterministic edit.

## Where

SKick can run as an Agent Skill, a host plugin wrapper, a project-local Skill, a user-global Skill, or a generic prompt adapter depending on the runtime. The canonical method stays identical; only installation and capability mapping change.

## How

### Standard engineering task

1. Resolve the real objective and constraints.
2. Inspect current repository/project evidence if available.
3. Research current external facts only where needed.
4. Choose the smallest capable harness/tools.
5. Plan the minimal safe change.
6. For consequential mutations, bind the exact proposal through the action firewall.
7. Implement surgically.
8. Run relevant tests/validation.
9. Verify review findings, then simplify only from a green state when cleanup is useful.
10. Report what changed, what was verified, and what remains uncertain.

### Deep/exhaustive research

Expand lateral search, source-origin tracing, contradiction checks, negative evidence, mechanism analysis, full relevant-unit reading, version boundaries, evidence lineage, uncertainty and a bounded frontier scan.

### Security / adversarial engineering

Use both lenses when material:

- offensive/mechanism lens: prerequisites, trust boundaries, exploit path, bypasses, failure conditions and observables;
- defensive lens: prevention, detection, containment, investigation, recovery, validation and regression tests.

This dual-lens method never overrides authorization, safety policy, system restrictions or least-privilege requirements.

### New web project

First resolve explicit user constraints, ecosystem conventions, existing dependencies, deployment needs, and product requirements. If no stronger constraint exists, the project may opt into the low-dependency Python/vanilla starter profile documented in `core/python-vanilla-web-stack.md`; it is not a universal default.

## Output expectations

SKick should distinguish:

- observed facts vs inference;
- current vs historical behavior;
- source/runtime/model/version boundaries;
- tested vs untested claims;
- structural validation vs target-runtime validation;
- confidence, caveats and unresolved risks.

### Language/framework-specific engineering
Before loading a language Skill, fingerprint the actual runtime/compiler/framework/toolchain version. Use `core/language-and-framework-intelligence.md` to decide whether a specialist adds real value, then combine the selected semantic repository capability with native compiler/type/lint/test/profile evidence.

Example: `Use SKick to migrate this Android/Kotlin codebase across the installed AGP/Navigation versions. Research the current official guidance, use only the task-matched specialist Skills, inspect the real repo with the strongest available semantic repository capability, then validate with the project toolchain and traces.`

### UI / rendered product validation
Load `core/ui-system-and-render-intelligence.md`. Preserve the design system, choose a representative responsive/accessibility/loading/error state matrix, and use a real browser/device/design artifact before claiming visual parity, accessibility or performance measurements.

Example: `Use SKick to redesign this dashboard, preserve our tokens/components, test keyboard/mobile/loading/error/reduced-motion states, and verify the final UI in the browser.`

### Research with evidence frontier
For Deep/Exhaustive work load `core/research-evidence-lifecycle.md`: track explored/partial/unexplored areas, opened sources, claim/source lineage, counterevidence and what would flip the recommendation.

Example: `Use SKick in exhaustive research mode. Build an evidence frontier, chase primary sources and material citations, compare contrary evidence, and tell me what new evidence would change the recommendation.`

### Purple-team security validation
Load `core/purple-team-research-and-validation.md` for authorized red/blue/purple work. Separate threat hypothesis, reachability, safe emulation, telemetry, detection, response/recovery and regression retest rather than calling a control covered because a rule exists.

Example: `Use SKick for an authorized lab purple-team exercise: research the behavior, emulate the smallest safe stimulus, confirm telemetry and detection, exercise response/recovery, close gaps, and retest.`

### External Skill/plugin supply-chain audit
Use `core/skill-supply-chain-and-lifecycle.md` plus `core/external-skill-intelligence.md` before adopting third-party behavior. Inventory Skills, agents, hooks, MCP, LSP, scripts, settings and binaries; pin/hash reviewed versions where appropriate; test composition risk and requalify updates.
