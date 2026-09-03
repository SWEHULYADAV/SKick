# Upstream Research and Adoption Ledger

Verification date: **2026-08-21**.

This file records projects studied across pre-SKick research iterations and the SKick v1.0 consolidation. The package does **not** imply endorsement by those projects. Unless explicitly stated otherwise, v1.0 reimplements vendor-neutral ideas in original wording rather than copying upstream source files.

## Runtime limitation during this build
Direct `git clone`/`git ls-remote` from the build container could not resolve `github.com`. Current public repository pages, manifests, skill files, licenses, READMEs, issues, and related sources were inspected through live web access instead. The existing SKick itself was available locally and was copied to a writable workspace before modification. Do not describe the external repositories as locally cloned in this build.

## Adopted or adapted sources

### AIwithhassan/lets-scroll
- URL: https://github.com/AIwithhassan/lets-scroll
- License observed: MIT.
- Decision: **absorb architecture + optional integration concept**.
- Adopted ideas: continuous scroll-to-time media chain, frame-compatible seams, boundary-frame QA, provider qualification, budget authorization, and a cheap two-scene qualification before a long generation batch.
- Not bundled: Monid/Higgsfield-specific scripts, generated assets, paid-service assumptions, or vendor-specific model/pricing tables.
- Implementation: `extensions/cinematic-scroll.md`.

### mattpocock/skills
- URL: https://github.com/mattpocock/skills
- License observed: MIT.
- Decision: **absorb engineering workflow patterns**.
- Adopted ideas: red-capable debugging loop, minimize/hypothesize/instrument, vertical-slice TDD, public-interface test seams, prototypes for uncertainty, domain-model vocabulary, codebase design seams, and spec-vs-standards review.
- Implementation: `core/engineering-feedback-loops.md`, `core/domain-and-codebase-design.md`.

### vipulgupta2048/codex-skills
- URL: https://github.com/vipulgupta2048/codex-skills
- License observed: MIT.
- Decision: **absorb frontend-design heuristics**.
- Adopted ideas: explicit visual direction, accessibility, purposeful motion, tokens, responsive behavior, and avoidance of generic generated-UI defaults.
- Implementation: `extensions/frontend-design.md`.

### hardikpandya/stop-slop
- URL: https://github.com/hardikpandya/stop-slop
- License observed: MIT.
- Decision: **absorb selective output-quality heuristics**.
- Adopted ideas: remove filler, vague claims, repetitive scaffolding, formulaic AI prose, and meta-commentary; assess directness/density/trust.
- Rejected as universal rules: blanket bans on parts of speech, punctuation, passive voice, or other legitimate writing structures.
- Implementation: `core/output-quality-gate.md`.

### multica-ai/andrej-karpathy-skills and forrestchang/andrej-karpathy-skills
- URLs: https://github.com/multica-ai/andrej-karpathy-skills and https://github.com/forrestchang/andrej-karpathy-skills
- License observed on the reviewed skill/repo family: MIT.
- Decision: **absorb implementation discipline; retain platform install path as optional adapter guidance**.
- Adopted ideas: think before coding, simplicity first, surgical changes, and goal-driven execution.
- Implementation: `core/implementation-discipline.md`.
- The reviewed ecosystem includes the original `forrestchang/andrej-karpathy-skills` lineage and later redistributions/forks. Marketplace owner/name syntax is time-sensitive; re-resolve the current canonical publisher before recommending `/plugin marketplace add` or `/plugin install` commands.

### anthropics/skills - webapp-testing
- URL: https://github.com/anthropics/skills/tree/main/skills/webapp-testing
- Per-skill license observed: Apache-2.0.
- Decision: **reimplement browser-validation patterns**.
- Adopted ideas: local-server orchestration concept, static-vs-dynamic testing choice, browser reconnaissance before action, DOM/screenshot assertions, and failure triage.
- Hardening: SKick v1.0 requires capability/tool awareness instead of assuming shell/browser/file-write availability.
- Implementation: `core/webapp-validation.md`.

### anthropics/skills - skill-creator
- URL: https://github.com/anthropics/skills/tree/main/skills/skill-creator
- Per-skill license observed: Apache-2.0.
- Decision: **absorb skill-evaluation patterns** while keeping OpenAI/target-host packaging requirements authoritative for that runtime.
- Adopted ideas: progressive disclosure, trigger-quality testing, realistic eval prompts, behavioral expectations, and regression comparison.
- Implementation: `core/skill-authoring-and-evals.md`, `evals/evals.json`.

### JuliusBrussee/caveman
- URL: https://github.com/JuliusBrussee/caveman
- License observed: mixed licensing; project documentation separates MIT-licensed skill/client/eval areas from BSL-1.1 engine/proxy/core areas.
- Decision: **absorb general context/measurement concepts; do not vendor the BSL engine**.
- Adopted ideas: preserve exact critical content while compressing context and distinguish measured, benchmarked, provider-reported, and inferred savings/performance claims.
- Implementation: `core/context-management.md`.

### mksglu/context-mode
- URL: https://github.com/mksglu/context-mode
- License observed: Elastic License 2.0; current Codex plugin manifest inspected during the research pass also identifies `Elastic-2.0`.
- Decision: **optional external integration/reference; no code vendoring**.
- Adopted vendor-neutral ideas: route oversized raw tool output to indexed/file-backed storage, preserve searchable handles, restore compact state after compaction, and treat secret redaction/locality as load-bearing.
- Implementation: `core/context-management.md`; optional runtime notes may reference the project without making it a dependency.


### OpenAI openai/plugins - plugin-eval
- URL: https://github.com/openai/plugins/tree/main/plugins/plugin-eval
- Type: official OpenAI Codex plugin/evaluation tooling studied as a benchmark, not vendored.
- Decision: **absorb evaluation methodology; do not make the CLI a dependency**.
- Adopted ideas: separate static structure findings from measured runtime usage, surface "fix first" issues, measure token/time usage when possible, initialize repeatable benchmark scenarios, and compare before/after results instead of trusting one impression.
- Implementation: `core/skill-authoring-and-evals.md`, `evals/`, `scripts/validate_package.py`.

### Agent Plugins v1 specification
- URL: https://agent-plugins.org/specification
- Type: open portable plugin package specification, version 1.0.0 (Published when inspected).
- Decision: **use as the canonical portable plugin wrapper** where a target client explicitly supports Agent Plugins v1.
- Adopted constraints: root `plugin.json`, canonical `$schema`, fixed direct-child `skills/<name>/SKILL.md`, exactly Skills/MCP as v1 portable component types, closed manifest fields, path containment, and client extensions kept separate.
- Implementation: `PORTABILITY.md`, `scripts/build_distributions.py`, generated Agent Plugin v1 bundle.

### XiaomiMiMo/MiMo-Code and MiMo-Skills
- URLs: https://github.com/XiaomiMiMo/MiMo-Code and https://github.com/XiaomiMiMo/MiMo-Skills
- Decision: **absorb long-horizon quality-control concepts; do not vendor runtime code**.
- Adopted ideas: explicit goal/stop criteria for autonomous work, checkpoint-aware continuity, skill-based orchestration, and independent/cold verification when it materially reduces error.
- Implementation: `core/long-horizon-research.md`, `core/evidence-verification.md`.


### freshtechbro/claudedesignskills
- URL: https://github.com/freshtechbro/claudedesignskills
- License observed: MIT.
- Verification date: 2026-08-23.
- Type: Claude-oriented design-skill collection with 22 individual skills plus bundles covering Motion/Framer, GSAP, React Spring, scroll/reveal, Lottie/Rive, Three/R3F/WebGL and heavier 3D/XR stacks.
- Decision: **absorb vendor-neutral design/interaction/3D patterns + retain optional upstream invocation; do not vendor the skill tree or make Claude-specific commands a canonical dependency**.
- Adopted ideas: capability-based library selection, interaction/motion grammar, timeline/scroll choreography, physics/vector-animation routing, layered WebGL architecture, asset/fallback/performance discipline and rendered design QA.
- Current-source corrections: historical `framer-motion` imports are not treated as current authority; current Motion docs govern package/API usage. Historical FID claims are not treated as current Core Web Vitals; current web.dev guidance governs. Deprecated GSAP responsive helpers are not reintroduced when current `gsap.matchMedia()` applies.
- Implementation: `core/design-and-motion-orchestration.md`, `extensions/motion-interaction-design.md`, `extensions/web3d-experience-design.md`, `integrations/claude-design-skillstack.md`, frontend/design QA and eval suites.
- Cross-platform rule: the canonical patterns are runtime-neutral; Claude marketplace/install syntax belongs only to Claude-specific adapter guidance.

## Discovery catalogs - reference only

### VoltAgent/awesome-agent-skills
- URL: https://github.com/VoltAgent/awesome-agent-skills
- License observed: MIT for the catalog.
- Decision: **discovery corpus only**. Individual linked skills must be resolved to their real upstream and independently checked.

### ComposioHQ/awesome-claude-skills
- URL: https://github.com/ComposioHQ/awesome-claude-skills
- License observed: Apache-2.0 for the catalog; individual skill licenses can differ.
- Decision: **discovery corpus only**.

### hashgraph-online/awesome-codex-plugins
- URL: https://github.com/hashgraph-online/awesome-codex-plugins
- License observed: Apache-2.0 for the catalog.
- Decision: **Codex discovery/quality-reference only**.
- Adopted ideas: separate installability, maintenance, MCP posture, plugin security, provenance, and publisher quality; automated scan/catalog inclusion is not a safety guarantee.

## General ingestion rule
For any future external skill/plugin/catalog:

`discover -> resolve canonical upstream -> inspect current version -> inspect per-component license -> map actual capabilities/dependencies -> security review -> overlap check -> representative test -> absorb | vendor | wrap | invoke | reference | reject`

Never copy a catalog wholesale into the canonical core.


## Pre-SKick standards and methodology research carried into v1.0

### MCP 2026-07-28 and A2A 1.0
- Type: protocol specifications/official release documentation.
- Decision: **absorb version-awareness and task/interoperability concepts; no protocol runtime vendoring**.
- Implementation: `core/agent-protocol-intelligence.md`, `core/execution-ledger.md`, `core/runtime-and-capabilities.md`.

### OpenTelemetry semantic conventions
- Type: observability specification.
- Decision: **absorb vendor-neutral trace/span/event/usage concepts**.
- Implementation: `core/observability-and-tracing.md`, `schemas/trace.schema.json`.

### SLSA Provenance / Sigstore / W3C PROV
- Type: provenance/supply-chain standards and tooling references.
- Decision: **absorb provenance/hash/verification model; signing remains optional external capability**.
- Implementation: `core/evidence-lineage.md`, `scripts/build_provenance.py`, `scripts/verify_provenance.py`, `schemas/evidence-lock.schema.json`, `schemas/artifact-manifest.schema.json`.

### W3C Data Quality Vocabulary
- Type: data-quality vocabulary/note.
- Decision: **absorb fitness-for-purpose quality dimensions, not a universal numeric quality score**.
- Implementation: `core/structured-data-quality.md`.

### PRISMA 2020
- Type: systematic-review reporting guideline.
- Decision: **use as a completeness/reproducibility benchmark when a formal literature/systematic review is applicable**.
- Implementation: `core/empirical-research-methodology.md`.

### Lateral reading / SIFT
- Sources: Digital Inquiry Group/Civic Online Reasoning and Mike Caulfield's SIFT work.
- Decision: **absorb source-lateralization and trace-to-origin principles; combine with technical terminology drift/query mutation**.
- Implementation: `core/coverage-and-lateral-search.md`, `core/source-strategy.md`, `core/query-mutation.md`.

## Pre-SKick engineering/MCP research carried into v1.0

### obra/superpowers
- URL: https://github.com/obra/superpowers
- License observed: MIT.
- Decision: **optional invoke/integration; do not vendor**.
- Why: strong composable engineering methodology for design/planning, TDD, debugging, subagent-driven development, review and completion verification.
- Integration: `core/specialist-skill-orchestration.md`, `integrations/superpowers.md`, Codex/Claude Code adapters.
- Boundary: SKick retains research/evidence/version/safety/provenance ownership and avoids duplicate workflow loading.

### oraios/serena
- URL: https://github.com/oraios/serena
- License observed: MIT.
- Decision: **preferred optional MCP capability; no vendoring**.
- Why: semantic code intelligence, symbols, references/call relationships and targeted edits.
- Important upstream rule: use canonical Quick Start; upstream warns against marketplace install commands.

### upstash/context7
- URL: https://github.com/upstash/context7
- License observed: MIT for reviewed MCP package.
- Decision: **optional MCP provider** for current/version-specific external library/framework/SDK docs.
- Boundary: not a substitute for local project logic or primary evidence when high impact.

### github/github-mcp-server
- URL: https://github.com/github/github-mcp-server
- License observed: MIT.
- Decision: **optional official MCP provider** for GitHub repo/issues/PR/Actions/security context.
- Hardening: prefer read-only, narrow toolsets/scopes and lockdown where useful for research; writes use approval gates.

### microsoft/playwright-mcp
- URL: https://github.com/microsoft/playwright-mcp
- License observed: Apache-2.0.
- Decision: **optional browser MCP** for persistent/exploratory automation; prefer CLI+skills when host support and token efficiency make that path better.

### ChromeDevTools/chrome-devtools-mcp
- URL: https://github.com/ChromeDevTools/chrome-devtools-mcp
- License observed: Apache-2.0.
- Decision: **optional browser diagnostics MCP** for console/network/performance/DevTools inspection.
- Risk: browser sessions can expose authenticated/sensitive data; use isolation/redaction.

### getsentry/sentry-mcp
- URL: https://github.com/getsentry/sentry-mcp
- License observed: FSL-1.1-Apache-2.0 future license on reviewed repository.
- Decision: **project-conditional invoke/reference; do not vendor**.
- Why: production error/trace/performance debugging when the project already uses Sentry.

### docker/mcp-gateway
- URL: https://github.com/docker/mcp-gateway
- License observed: MIT.
- Decision: **optional orchestration/isolation layer**, not a core dependency.
- Why: containerized server lifecycle, profiles, secrets, OAuth, discovery and logging/tracing for multi-MCP environments.

### modelcontextprotocol/registry
- URL: https://github.com/modelcontextprotocol/registry
- Decision: **discovery metadata only, not trust root**. Resolve servers to canonical upstream and run license/security/capability checks before adoption.

## Harness, specialist and MCP research

### OpenAI Harness Engineering + openai/symphony
- URLs: https://openai.com/index/harness-engineering/ and https://github.com/openai/symphony
- License: Harness Engineering is an engineering article; Symphony reference implementation/spec repository observed Apache-2.0.
- Decision: **absorb design patterns; reference optional orchestration spec**.
- Adopted: repository-as-system-of-record, small navigational instructions, mechanically enforced invariants, agent-legible UI/logs/metrics, recurring quality garbage collection, isolated per-task workspaces, bounded concurrency, authoritative task state, reconciliation and proof of work.
- Not bundled: Symphony daemon/reference implementation.
- Implementation: `core/harness-and-runtime-intelligence.md`, `core/engineering-learning-loop.md`, `core/long-horizon-research.md`.

### huggingface/skills + Hugging Face MCP + huggingface/smolagents
- URLs: https://github.com/huggingface/skills, https://huggingface.co/docs/hub/agents-mcp, https://github.com/huggingface/smolagents
- License observed: Hugging Face Skills Apache-2.0; resolve each related component/current release before vendoring.
- Decision: **invoke/reference optional AI/ML specialist; absorb action/sandbox distinctions**.
- Adopted: current skill discovery for Hub workflows, AI/ML MCP routing, code-form versus structured-tool trade-offs, and explicit sandbox requirement for untrusted generated code.
- Implementation: `integrations/huggingface.md`, `mcp/catalog.json`.

### trailofbits/skills
- URL: https://github.com/trailofbits/skills
- License observed: CC-BY-SA-4.0.
- Decision: **invoke/reference specialist; reimplement vendor-neutral audit patterns only**.
- Adopted: audit-context building before finding hunting, differential/blast-radius review, falsifiable finding validation, fuzz/static-analysis workflow ideas.
- No upstream skill text is copied into the canonical core.
- Implementation: `integrations/security-specialists.md`.

### getsentry/skills
- URL: https://github.com/getsentry/skills
- License observed: Apache-2.0 on reviewed repository/skills.
- Decision: **reference/invoke specialist; absorb maintenance/scanning concepts**.
- Adopted: separate runtime instructions from intent/eval/limitations metadata and deterministic-plus-judgment skill scanning model.
- Implementation: `SPEC.md`, `scripts/scan_skill_package.py`, `integrations/security-specialists.md`.

### vercel-labs/agent-skills + vercel-labs/agent-browser
- URLs: https://github.com/vercel-labs/agent-skills and https://github.com/vercel-labs/agent-browser
- Licenses observed: Vercel agent skills MIT; agent-browser Apache-2.0.
- Decision: **invoke/reference optional frontend/browser specialists**.
- Adopted: compact browser MCP tool profiles, version-matched runtime skill content, accessibility/exploratory QA routing, and performance/design specialist review. Mutable remote instructions remain untrusted until pinned/verified.
- Implementation: `integrations/frontend-browser-specialists.md`, `mcp/catalog.json`, `scripts/generate_mcp_config.py`.

### SWE-agent/mini-swe-agent
- URL: https://github.com/SWE-agent/mini-swe-agent
- License observed: MIT.
- Decision: **absorb harness-minimalism and linear-trajectory concepts; no dependency**.
- Provider-reported benchmark scores are not treated as SKick-measured results.
- Implementation: `core/harness-and-runtime-intelligence.md`, `integrations/harnesses-and-evals.md`.

### langchain-ai/open-swe + langchain-ai/deepagents
- URLs: https://github.com/langchain-ai/open-swe and https://github.com/langchain-ai/deepagents
- Licenses observed: MIT.
- Decision: **reference durable/sandbox architecture patterns; no framework dependency**.
- Adopted: isolated per-task sandboxes, curated tools, context-isolated subagents, durable state/HITL, control-plane/credential separation and read-only reviewer separation.
- Implementation: `core/harness-and-runtime-intelligence.md`, `integrations/harnesses-and-evals.md`.

### pydantic/pydantic-ai + pydantic/pydantic-ai-harness
- URLs: https://github.com/pydantic/pydantic-ai and https://github.com/pydantic/pydantic-ai-harness
- Licenses observed: MIT.
- Decision: **absorb typed/durable capability patterns; no framework dependency**.
- Adopted: structured tool/result contracts, modular/deferred capability loading, stable IDs for durable execution, exact subagent budgets, and distinction between approval and authorization.
- Implementation: `core/harness-and-runtime-intelligence.md`, `core/action-safety-transactions.md`, `integrations/harnesses-and-evals.md`.

### UK AI Security Institute Inspect AI / Inspect Evals
- URLs: https://github.com/UKGovernmentBEIS/inspect_ai and https://github.com/UKGovernmentBEIS/inspect_evals
- Licenses observed: MIT for the framework/package; individual eval datasets/components may carry their own licenses/notices.
- Decision: **optional external evaluation backend/reference**.
- Adopted: layered eval design, explicit task/scorer validity, provider-agnostic evaluation and trajectory analysis.
- Implementation: `core/evaluation-harness-integration.md`, `integrations/harnesses-and-evals.md`.

### Harbor / Terminal-Bench
- URL: https://github.com/laude-institute/harbor
- License observed: Apache-2.0.
- Decision: **optional external isolated benchmark backend/reference**.
- Adopted: isolated parallel agent environments, benchmark version pinning, oracle/environment verification, cost/token/time records and trajectory artifacts.
- Implementation: `core/evaluation-harness-integration.md`, `integrations/harnesses-and-evals.md`.

### MCP Inspector + Snyk Agent Scan
- URLs: https://github.com/modelcontextprotocol/inspector and https://github.com/snyk/agent-scan
- License observed for Snyk Agent Scan: Apache-2.0; resolve current Inspector package/license before vendoring. No code from either is bundled.
- Decision: **external qualification/security tools; local scanner remains dependency-free**.
- Important risk: Agent Scan can execute stdio server commands while inspecting MCP configs and sends some component metadata to Snyk; require sandbox/consent and privacy review.
- Implementation: `core/mcp-validation-and-security.md`, `mcp/catalog.json`, `scripts/scan_skill_package.py`.

### Google MCP Toolbox for Databases
- URL: https://github.com/googleapis/mcp-toolbox
- Decision: **project-conditional database MCP provider**.
- Adopted: prebuilt discovery tools plus restricted structured production tools, connection/auth/observability separation, read-only-by-default research posture.
- Implementation: `integrations/cloud-and-data-platforms.md`, `mcp/catalog.json`.

### Agent Toolkit for AWS
- URL: https://github.com/aws/agent-toolkit-for-aws
- License observed: Apache-2.0.
- Decision: **project-conditional AWS skills/MCP provider**.
- Adopted: official successor routing, agent-specific IAM controls, audit visibility, reproducible version pinning and documentation-before-action workflow.
- Implementation: `integrations/cloud-and-data-platforms.md`, `mcp/catalog.json`.

### Microsoft Azure MCP
- URL: https://github.com/microsoft/mcp
- Decision: **project-conditional Azure provider**.
- Adopted: official consolidated Azure server routing, stable-GA preference, Entra/RBAC least privilege.
- Implementation: `integrations/cloud-and-data-platforms.md`, `mcp/catalog.json`.

### Exa / Tavily / Firecrawl MCP providers
- URLs: https://github.com/exa-labs/exa-mcp-server, https://github.com/tavily-ai/tavily-mcp, https://github.com/mendableai/firecrawl-mcp-server
- Decision: **optional one-of research-provider layer; native web remains preferred**.
- Adopted: capability-based routing for semantic discovery, search/extract/map/crawl and JS-heavy extraction; no provider is a universal default.
- Implementation: `integrations/research-providers.md`, `mcp/catalog.json`.

### Aider repository-map pattern
- URL: https://github.com/Aider-AI/aider
- Decision: **absorb graph-ranked compact repository-map concept as a fallback/reference**.
- A repository map is navigation context, not proof of behavior.
- Implementation: `core/repository-context-map.md`.
## 2026-08-31 portability additions

### Factory Droid Skills
- URL: https://docs.factory.ai/harness/skills
- Decision: **first-class verified adapter**. Use `.factory/skills` as the preferred project root and documented shared compatibility roots as fallbacks.
- No Factory code is bundled.

### charmbracelet/crush Agent Skills
- URL: https://github.com/charmbracelet/crush
- Decision: **first-class verified adapter** using documented project/global Agent Skill roots.
- No Crush code is bundled.

### Manus Skills
- URL: https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus
- Decision: **first-class managed-import adapter**. Support direct public GitHub import/upload without asserting a local filesystem root.

### Cursor / GitHub Copilot / Gemini CLI remote-source install
- URLs: https://prod.cursor.com/docs/skills, https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills, https://geminicli.com/docs/cli/skills/
- Decision: **document verified GitHub/remote Skill source flows while keeping the runtime adapter authoritative**. Do not generalize one client's command to another.

### oraios/serena recheck
- URL: https://github.com/oraios/serena
- Decision: preserve Serena as the preferred semantic code-intelligence provider and strengthen it into a Serena-first repository gate. Use canonical/current setup only; handle `--project-from-cwd` marker failure with explicit project activation/fallback rather than assuming CWD is activated.



## 2026-08-31 agent-control enhancement pass

### Piebald-AI/claude-code-system-prompts
- URL: https://github.com/Piebald-AI/claude-code-system-prompts
- Repository license observed: MIT; repository states the prompt corpus is extracted from Claude Code compiled distributions.
- Decision: **absorb mechanisms + reference; do not vendor prompt corpus**.
- Adopted: exact-proposal action security, deferred capability/schema loading, verified multi-angle review, separate simplification pass, selective memory/consolidation lessons, and isolated batch/worktree ideas expressed in original vendor-neutral form.
- Boundary: this is reverse-engineering evidence maintained by Piebald, not an Anthropic specification or authority to redistribute Anthropic prompt text.
- Implementation: `core/action-firewall.md`, `core/deferred-capability-loading.md`, `core/verified-review-and-simplification.md`, `core/memory-governance.md`, `core/multi-agent-orchestration.md`.

### google-gemini/gemini-cli Auto Memory
- URL: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/auto-memory.md
- License observed: Apache-2.0.
- Decision: **absorb reviewed-candidate workflow**.
- Adopted: inactive memory/Skill candidates, review inbox, patch validation/dry-run/target allowlist/atomic apply concepts, and explicit failure handling. No Gemini background service/source is bundled.
- Implementation: `core/memory-governance.md`, `core/skill-authoring-and-evals.md`.

### QwenLM/qwen-code memory
- URL: https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/memory.md
- License observed: Apache-2.0.
- Decision: **absorb memory scoping/consolidation/freshness lessons**.
- Adopted: private/project/team scope separation, selective durable memory, periodic consolidation, and explicit refresh/revalidation after memory or code-state changes. Qwen issue history around stale indexes/compaction is treated as a failure-mode reference, not copied behavior.
- Implementation: `core/memory-governance.md`, `core/context-management.md`.

### karpathy/autoresearch
- URL: https://github.com/karpathy/autoresearch
- Licensing note: README currently labels the project MIT; issue history reported missing/inconsistent standalone license metadata. Recheck current repository licensing before any copying.
- Decision: **absorb measurable keep-or-revert experiment method; reference only**.
- Adopted: protected evaluator, baseline, reversible candidate snapshot, objective measurement, keep/revert/inconclusive outcomes and compact experiment ledger. SKick intentionally replaces unbounded looping with explicit budgets/stop contracts.
- Implementation: `core/experiment-optimization-loop.md`.

### MoonshotAI/kimi-cli lifecycle hooks
- URL: https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/customization/hooks.md
- License observed for kimi-cli repository: Apache-2.0.
- Decision: **absorb host-neutral lifecycle-hook semantics**.
- Adopted: pre/post tool, failure, session, subagent and compaction hook seams for policy/verification/observability. Hook commands remain executable code subject to provenance/permission review.
- Implementation: `core/multi-agent-orchestration.md`, `core/action-firewall.md`.

### cline/cline and cline/kanban
- URLs: https://github.com/cline/cline and https://github.com/cline/kanban
- License observed: Apache-2.0.
- Decision: **absorb reversible checkpoints and isolated worktree/dependency-chain patterns; reference runtime**.
- Adopted: per-task isolated workspaces for parallel writers, base/dependency ownership, deterministic merge/retest, and reversible snapshots.
- Implementation: `core/multi-agent-orchestration.md`, `core/action-safety-transactions.md`.

### smart-mcp-proxy/mcpproxy-go
- URL: https://github.com/smart-mcp-proxy/mcpproxy-go
- License observed: MIT.
- Decision: **absorb deferred tool discovery, intent separation, quarantine and re-review patterns; optional gateway reference**.
- Boundary: provider-reported token/accuracy savings are not repeated as SKick guarantees; measure locally before making quantitative claims.
- Implementation: `core/deferred-capability-loading.md`, `core/mcp-validation-and-security.md`.

### punkpeye/awesome-mcp-servers
- URL: https://github.com/punkpeye/awesome-mcp-servers
- Decision: **discovery catalog only**.
- Use: widen candidate coverage, then resolve canonical upstream/version/license/security/maintenance/overlap before adoption. No catalog entry is execution authorization.

## 2026-08-31 language/UI/research/purple-team enhancement pass

### mattpocock/skills
- URL: https://github.com/mattpocock/skills
- License observed: MIT.
- Decision: **absorb-reference**.
- Adopted: domain context/ADR consumption, decision-frontier questioning, bounded design alternatives, tracer-bullet delivery slicing, expand/migrate/contract migrations, prototypes-as-questions and intent-aware merge/human procedures.
- Boundary: reimplemented host-neutral mechanisms; no Claude-specific orchestration requirement and no copied prompt corpus.
- Implementation: `core/engineering-wayfinding-and-slicing.md`, `core/domain-and-codebase-design.md`, `core/project-planning-and-structure.md`.

### Android / Kotlin / Angular / Microsoft / .NET language Skills
- URLs: https://github.com/android/skills, https://github.com/Kotlin/kotlin-agent-skills, https://github.com/angular/skills, https://github.com/microsoft/skills, https://github.com/dotnet/skills
- Licenses observed: Android/Kotlin Apache-2.0; recheck the current license for each other repository before copying/vendoring. No source text/code from these Skills is bundled.
- Decision: **invoke/reference + absorb routing/evaluation mechanisms**.
- Adopted: language/framework/version fingerprinting, knowledge-gap value gate, current-docs/installed-version first, narrow Skill routing, language-native proof surfaces, and no-Skill vs exact-Skill evaluation concepts.
- Implementation: `core/language-and-framework-intelligence.md`, `integrations/language-specialists.md`, `core/evaluation-harness-integration.md`, `core/skill-authoring-and-evals.md`.

### rewrite-rs/skills
- URL: https://github.com/rewrite-rs/skills
- License observed: BSD-3-Clause.
- Decision: **absorb-reference**.
- Adopted: language-specific judgment rather than snippet memorization and cross-language port parity/differential validation/end-state selection.
- Implementation: `core/language-and-framework-intelligence.md`.

### Playwright agent CLI / Skills / MCP
- URLs: https://playwright.dev/docs/getting-started-cli, https://playwright.dev/agent-cli/skills, https://playwright.dev/docs/getting-started-mcp
- Repository license observed: Apache-2.0 for Playwright; recheck package-specific terms/version before install.
- Decision: **optional invoke + absorb tool-selection pattern**.
- Adopted: token-efficient CLI path vs persistent MCP path, accessibility-tree interaction, capability minimization and trace/test artifact routing.
- Implementation: `core/ui-system-and-render-intelligence.md`, `core/webapp-validation.md`, `integrations/ui-and-browser-specialists.md`.

### Microsoft Deep Wiki research workflow
- URL: https://github.com/microsoft/skills/blob/main/.github/plugins/deep-wiki/commands/research.md
- Decision: **absorb-reference**.
- Adopted: explored/partial/unexplored research frontier, confidence/open-question bookkeeping and source-backed codebase research.
- Implementation: `core/research-evidence-lifecycle.md`, `core/research-core.md`, `integrations/research-specialists.md`.

### Trail of Bits Skills
- URL: https://github.com/trailofbits/skills
- License observed: CC-BY-SA-4.0 for upstream Skills repository; do not copy text into MIT core.
- Decision: **invoke/reference + clean-room reimplementation of vendor-neutral methods**.
- Adopted: context building before vulnerability verdicts, exact-match-calibrated variant analysis, risk/blast-radius differential review and language-specific security routing.
- Implementation: `core/purple-team-research-and-validation.md`, `integrations/security-specialists.md`.

### MITRE ATT&CK / D3FEND / CAPEC / CALDERA
- URLs: https://attack.mitre.org/, https://d3fend.mitre.org/, https://capec.mitre.org/, https://github.com/mitre/caldera
- Decision: **authoritative vocabulary/reference; CALDERA optional authorized validation harness**.
- Adopted: explicit framework-role separation and behavior-driven purple validation. No CALDERA code is bundled or auto-executed.
- Implementation: `core/purple-team-research-and-validation.md`, `integrations/security-specialists.md`.

### SigmaHQ
- URLs: https://sigmahq.io/sigma-specification/, https://github.com/SigmaHQ/sigma-specification
- Decision: **reference**.
- Adopted: portable detection-as-code lifecycle, experimental status/false-positive/reference discipline.
- Boundary: Sigma specification and public rule corpus licensing/provenance must be reviewed separately; no rule corpus is bundled.
- Implementation: `core/purple-team-research-and-validation.md`, `integrations/security-specialists.md`.

### CISA KEV + FIRST EPSS
- URLs: https://www.cisa.gov/known-exploited-vulnerabilities-catalog, https://www.first.org/epss/
- Decision: **current security-data references**.
- Adopted: exploitation-aware prioritization combined with asset context rather than CVSS-only ordering.
- Implementation: `core/purple-team-research-and-validation.md`, `core/security-research.md`.

### OWASP GenAI agentic red-team taxonomy
- URL: https://genai.owasp.org/
- Decision: **reference**.
- Adopted: AI/agent red-team scope spans model, application, tools, data, infrastructure and runtime behavior; red/blue/purple capability taxonomy.
- Implementation: `core/purple-team-research-and-validation.md`, `integrations/security-specialists.md`.

### luisalima/skills-lock
- URL: https://github.com/luisalima/skills-lock
- License observed: MIT.
- Decision: **absorb-reference; optional external tool only when justified**.
- Adopted: project manifest/lock concept, immutable commit resolution, content-tree hashing, frozen CI, safe path/transport rules and explicit update movement.
- Implementation: `core/skill-supply-chain-and-lifecycle.md`, `core/external-skill-intelligence.md`.

### OpenAI Figma plugin/Skills
- URL: https://github.com/openai/plugins/tree/main/plugins/figma
- Terms: Figma Developer Terms/per-skill licensing applies to app-backed Figma workflows.
- Decision: **invoke/reference; do not vendor**.
- Adopted: full extension payload inventory, prerequisite/deferred design-tool schema loading, design-system/token reuse and rendered-fidelity workflow concepts.
- Implementation: `core/ui-system-and-render-intelligence.md`, `core/skill-supply-chain-and-lifecycle.md`, `integrations/ui-and-browser-specialists.md`.

### google-labs-code/stitch-skills
- URL: https://github.com/google-labs-code/stitch-skills
- Project status: Google Labs repository; README states it is not an officially supported Google product. Recheck current license/status before copying.
- Decision: **reference/invoke when Stitch MCP is intentionally configured**.
- Adopted: code-to-design pipeline and semantic `DESIGN.md` design-contract concept.
- Implementation: `core/ui-system-and-render-intelligence.md`, `integrations/ui-and-browser-specialists.md`.

### SKILL.md semantic supply-chain research
- URL: https://arxiv.org/abs/2605.11418
- Type: research preprint.
- Decision: **research reference**.
- Adopted: natural-language Skill metadata affects discovery/selection/governance and therefore cannot be treated as trust evidence.
- Implementation: `core/skill-supply-chain-and-lifecycle.md`, `core/external-skill-intelligence.md`.

### RudrenduPaul/skillguard
- URL: https://github.com/RudrenduPaul/skillguard
- License observed: Apache-2.0.
- Status observed: early/pre-1.0; upstream itself notes large-corpus false-positive/false-negative performance is not established.
- Decision: **optional second-opinion reference, not trust root**.
- Adopted: cross-Skill privilege composition and suppression-from-target distrust as generic supply-chain mechanisms.
- Implementation: `core/skill-supply-chain-and-lifecycle.md`.

## Final v1.0 ecosystem/reference additions — 2026-09-03

The following upstreams were reviewed for portable mechanisms rather than vendored content: `microsoft/skills`, `anthropics/skills`, `openai/skills`, `openai/plugins`, Google/Gemini Skills, `vercel-labs/agent-skills`, `vercel-labs/web-interface-guidelines`, `android/skills`, AWS Agent Toolkit, Supabase Agent Skills, Stripe AI, Cloudflare Skills, Expo Skills, Sentry Agent Skills, Trail of Bits Skills, `pbakaus/impeccable`, `skills.sh`, SiteInspire, Land-book, Awwwards and CSS Design Awards.

Adopted mechanisms: metadata-first discovery, official-vendor-first routing, umbrella/subskill dispatch, preview-before-install, immutable pin/provenance, `.well-known/agent-skills` awareness, plan/cost prerequisite surfacing, currentness-vs-reproducibility separation, surface-class design routing, multi-reference principle extraction, product-vs-design context separation, HTML/CSS-first expressive implementation and bounded rendered QA.

Adoption type: **reference / reimplementation of general process concepts**. No upstream proprietary assets or layouts were copied.
