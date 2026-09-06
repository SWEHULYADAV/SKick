# Changelog

## v1.1 — 2026-09-05

### Added
- Added an optional dependency-free Python runtime for capability state, quick/standard/deep/exhaustive selection, task interpretation, module/context compilation, instruction budgeting, structured run state, research planning/ledger, adversarial teaming, installation diagnostics, and claim-safe reporting.
- Added prompt intelligence with silent/visible/execution/strict-spec modes, explicit user-constraint locking, weak-prompt bounded interpretation, contradiction detection, and success/research/verification planning.
- Added adaptive research question maps, source/query classes, lateral/disconfirmation pivots, frontier/coverage state, source-lineage triangulation, typed findings, and contradiction-aware high-confidence fact handling.
- Added scoped Red/Blue/Purple/Black-Blind planning with authorization-aware safe-lab fallback and an owned cross-tenant authorization fixture for future model-based security evaluation.

### Improved
- Made capability routing brand-neutral: native indexes/LSP/symbol APIs, Serena, semantic search, grep and other providers compete by observed capability fit rather than constitutional vendor preference.
- Made project architecture authoritative over optional starter profiles; Python/vanilla-web guidance is no longer a universal invariant.
- Made runtime JSON schemas active contracts and expanded installation doctor diagnostics for malformed, duplicate and version-mismatched installs.
- Hardened the generic declarative fallback so the optional Python/vanilla web profile is never treated as a universal stack preference.
- Made generic GitHub/bootstrap repository-intelligence guidance capability-neutral; Serena remains an optional provider-specific capability rather than bootstrap authority.

### Fixed
- Fixed v1 package-manifest drift by generating/checking the canonical file list and rejecting provenance gaps.
- Fixed prompt enhancement dropping positive binding constraints such as `Use Python` and `Only modify this file`.
- Fixed capability probing that could create a nonexistent project directory.
- Fixed evaluation comparison paths that could treat legacy candidate self-report as scoring authority.
- Fixed deterministic eval artifacts leaking local absolute workspace paths; runner output now records package-relative suite paths.
- Fixed generated adapter drift after compatibility edits by re-synchronizing install blocks from the canonical manifest.

### Changed
- Compatibility now uses explicit proof states (`LIVE_TESTED`, `DOC_VERIFIED`, `COMMUNITY_VERIFIED`, `HOST_DEPENDENT`, `GENERIC_PROMPT_FALLBACK`, `BROKEN_UNSUPPORTED`, `UNKNOWN`) rather than a broad verified label.
- Installation proof states remain distinct: copied, installed, discovered, invokable, and live-tested.
- Runtime/package version is derived from the canonical `VERSION` file; v1.1 is the first release of the executable-runtime line.

### Deprecated
- Deprecated Serena-first repository policy and universal starter-stack policy. Vendor/starter preferences belong in runtime/project policy only.
- Deprecated ambiguous compatibility language that collapses documentation support into live support.

### Removed
- Removed the redundant `assets/icon.svg` that caused the v1 package-manifest inconsistency.
- Removed candidate access to deterministic evaluation oracles/check definitions.

### Security
- Hardened claim promotion so strong states require claim-bound evidence; code/security/current/platform claims have proof-specific burdens, current facts require freshness metadata, and live platform proof requires a live-platform artifact.
- Hardened installer path containment against project-scope symlink escape and reject source-package symlinks.
- Package validation now rejects leaked local-machine workspace paths in maintained release text/artifacts.
- Preserve repository/web/external-Skill/MCP content as untrusted evidence and keep observability local-first with no hidden telemetry.

### Compatibility
- Platform/provider records remain generated from `INSTALLATION_MANIFEST.json`; route count is informational and can decrease when evidence weakens.
- Literal `@SKick` is documented only where the canonical evidence record supports that transport; model providers are separated from Skill hosts.
- Rechecked current first-party transport evidence and corrected Cursor, Kiro, Gemini CLI, TRAE, Codex/ChatGPT and OpenAI plugin metadata without promoting any route to live-tested.
- External live-host testing remains `LIVE_TESTED = 0` in the release environment unless a route carries reproducible live-test metadata.

### Testing
- Added deterministic runtime, prompt, research, teaming, claim-honesty, injection, migration, installer and release-hardening tests plus local ablation suites.
- Model baseline-v1-v1.1 task-success and external cross-model/live-platform behavior remain `NOT_MEASURED`/`BLOCKED` where the environment cannot execute controlled trials; v1.1 does not convert local deterministic success into behavioral proof.

## v1.0 final portability, ecosystem and design hardening — 2026-09-03

- Kept the release version at **v1.0** while finalizing the first public release.
- Added plan/account/region-aware Skill availability guidance so users can distinguish ChatGPT managed Skills, Codex, Claude, Gemini Spark and coding-host routes.
- Corrected/strengthened current host routing for GitHub Copilot (`gh skill`), Kilo Code, Devin, Qoder, OpenHands repo scope, Warp, Zed, Zencoder, Kiro and Replit; preserved conservative labels where evidence remains weaker.
- Added `PLANS_AND_SURFACES.md`, `SKILL_ECOSYSTEM_GUIDE.md`, and `DESIGN_REFERENCE_PLAYBOOK.md`.
- Expanded external Skill intelligence with official-vendor-first discovery, metadata-first routing, `.well-known/agent-skills`, preview/pin/update discipline, plan/cost prerequisites and currentness-vs-reproducibility controls.
- Added reference coverage for major official Skill ecosystems and cross-agent discovery without vendoring them as dependencies.
- Upgraded UI methodology with surface-class routing, multi-reference art-direction research, `PRODUCT.md` vs `DESIGN.md` separation, HTML/CSS-first expressive design, one-signature-move restraint and bounded two-pass rendered QA.
- Slimmed the public source tree by removing redundant host bridge files, generated MCP config snapshots, the duplicate AI continuation guide, an unconsumed design catalog/schema and the unused SVG icon; compressed README visuals from multi-megabyte PNGs to lightweight WebP while retaining PNG runtime branding.
- Kept provenance ledgers, evals, schemas, adapters and release tooling because they materially support portability, trust, regression testing and future maintenance.
- Promoted Goose and iFlow CLI to current first-party-verified Skill routes and Mux to product-source-verified routing; kept Continue/AiderDesk/Neovate/MCPJam conservative where evidence remains weaker.
- Hardened `.gitignore` so local ZIP/patch/diff archives, test caches and editor swap files cannot accidentally re-enter the canonical GitHub source tree.

## v1.0 — 2026-08-23

Initial SKick release.

- Renames/consolidates the portable engineering control-plane work as **SKick**.
- Preserves research-first, mechanism-first, evidence-lineage, security, long-horizon, evaluation and tool-routing methodology.
- Keeps the preferred greenfield web profile minimal: root `app.py`, Python/backend implementation in `backend/`, semantic HTML/CSS/vanilla JS/assets in `frontend/`, deeper folders only when justified.
- Keeps offensive + defensive analysis paired when adversarial/failure behavior is materially relevant.
- Adds full English setup/installation/usage/troubleshooting/update documentation.
- Adds dedicated web/app and VS Code/IDE installation guides.
- Defines explicit SKick safety, warning, provenance, and licensing boundaries.
- Removes former upstream branding/runtime coupling; SKick documentation and machine-readable handoff now identify SKick as self-contained.
- Adds PNG branding: `logo.png`, `icon.png`, `favicon.png`, and `favicon-32.png`.
- Keeps runtime adapters thin and the canonical methodology in `core/`.
- Supports portable distribution generation and local package/provenance/eval validation.
- Makes the archive self-describing for direct AI handoff with `START_HERE.md` and `INSTALLATION_MANIFEST.json`.
- Adds `AI_HANDOFF.md` / `AI_CONTEXT.json` so a future AI can continue development without the original conversation.
- Adds `CONTRIBUTING.md` and a release checklist covering forks, canonical-vs-generated ownership, validation, provenance, and rebuilds.
- Adds a deterministic AI install protocol and expands every runtime adapter with direct-ZIP install, verification, update/removal, and warning guidance.
- Expands the safe filesystem installer to verified project/user Skill roots with dry-run and ambiguity/overwrite protection.
- Expands runtime routing to 59 host/provider routes, including BrowserCode, MiMoCode/Xiaomi, MiniMax host routing, Qwen Code, Kimi Code, LongCat host routing, TRAE/ByteDance, OpenCode, GitHub Copilot, Cline, Roo Code, Windsurf, and future/custom harness fallbacks.
- Adds explicit invocation modes/depth controls and a host-not-model routing contract.
- Adds `docs/RUNTIME_COMPATIBILITY.md`, `docs/NEW_RUNTIME_INTEGRATION.md`, and `docs/INVOCATION_AND_MODES.md`.
- Adds GitHub Actions release validation, security policy, MIT license, release audit tooling, runtime detection, and safer overwrite backup behavior.
- Keeps generated distributions out of canonical maintenance source and adds a portable `runtime-skill.zip` build target.
- Reworks the GitHub README around installation, runtime coverage, direct-ZIP handoff, fork/update flow, and aligned SKick README artwork.
## v1.0 — universal GitHub/bootstrap hardening (2026-08-31)

- Adds mandatory silent prompt enhancement for non-trivial work.
- Adds `core/capability-and-skill-routing.md`: SKick now explicitly brokers the best task-matched installed/native Skill, plugin, MCP or tool per phase while retaining evidence/safety/provenance/final-verification control.
- Makes repository engineering Serena-first when available, with explicit semantic/LSP/indexed fallbacks and no fake Serena-use claims.
- Adds `core/system-design-and-architecture.md` and an architecture/change-impact gate before broad implementation.
- Expands lateral research into lateral thinking, side-clue/serendipity capture, alternative hypotheses, adjacent-ecosystem analogies and bounded exploration.
- Adds GitHub repository bootstrap via `BOOTSTRAP_PROMPTS.md` and `docs/GITHUB_BOOTSTRAP.md`, including a short universal prompt and runtime-specific fast paths.
- Expands routing from 59 to 62 platform/provider routes with verified Factory Droid, Crush and managed Manus adapters.
- Updates runtime detection/installer support for Factory Droid and Crush and refreshes current Kimi Skill-source routing.



## v1.0 — agent-control hardening (2026-08-31)

- Adds `core/action-firewall.md`: exact-proposal authorization binding, provenance, blast-radius classification, soft/hard block semantics, scope-drift re-approval and independent postcondition verification.
- Adds `core/deferred-capability-loading.md`: compact capability discovery followed by on-demand Skill/tool schema loading, with snapshot freshness and measurement rules.
- Adds `core/verified-review-and-simplification.md`: independent review angles, CONFIRMED/PLAUSIBLE/REFUTED finding verification, bounded gap sweep, post-correctness simplification and mandatory retest.
- Adds `core/experiment-optimization-loop.md`: protected evaluator, baseline, reversible candidates, keep/revert/inconclusive outcomes, stochastic repeated trials and bounded stop contracts.
- Hardens `core/memory-governance.md` with reviewed learning candidates, selective recall, team/private scope separation, code/config freshness anchors, stale-memory invalidation, compaction reload and provenance-preserving consolidation.
- Hardens MCP qualification with package/schema pinning, quarantine/re-quarantine, declared read/write/destructive intent, request/response inspection and non-LLM approval boundaries where the host supports them.
- Hardens multi-agent implementation with isolated worktree ownership, shared-write collision detection, base/dependency tracking, deterministic merge/retest and lifecycle-hook safety.
- Adds `integrations/agent-control-patterns.md` and provenance records for Piebald Claude Code prompt research, Gemini/Qwen memory, Karpathy autoresearch, Kimi hooks, Cline worktrees/checkpoints, Smart MCP Proxy and awesome-MCP discovery.
- Adds regression evals for approval drift, deferred tool loading, reviewed learning, stale-code memory, measurable keep/revert optimization, finding verification, worktree collisions and MCP rug-pull requalification.

## v1.0 — language/UI/research/purple-team hardening (2026-08-31)

- Adds `core/language-and-framework-intelligence.md`: stack/version fingerprinting, knowledge-gap/value gating, language-native proof surfaces, framework freshness, and parity/differential contracts for cross-language ports.
- Adds `core/ui-system-and-render-intelligence.md`: project design-contract extraction, design-token/component reuse, rendered state matrices, browser/design-tool routing, and measured-vs-inferred UI/performance boundaries.
- Adds `core/research-evidence-lifecycle.md`: research-mode routing, explored/partial/unexplored frontier, opened-source discipline, claim/source-lineage ledger, counterevidence and decision-flip conditions.
- Adds `core/purple-team-research-and-validation.md`: authorized red/blue/purple lifecycle, ATT&CK/CAPEC/CWE/D3FEND role separation, detection engineering, safe emulation, vulnerability prioritization, variant analysis, DFIR evidence integrity and AI/agent security surfaces.
- Adds `core/skill-supply-chain-and-lifecycle.md`: full plugin-bundle inventory, descriptor distrust, immutable pin/hash/lock records, safe install transactions, cross-Skill privilege composition, update requalification and revocation.
- Adds `core/engineering-wayfinding-and-slicing.md`: decision-frontier grilling, durable domain context, bounded design alternatives, tracer-bullet vertical slicing, expand/migrate/contract migrations, prototypes-as-questions, intent-aware conflict resolution and human-only procedures.
- Adds language/UI/research specialist registries and expands the integration catalog with Android, Kotlin, Angular, .NET, Microsoft Skills, rewrite-rs, Playwright, skills-lock, CALDERA, SigmaHQ, OWASP agentic red-team and Matt Pocock engineering references.
- Hardens Skill evaluation with no-Skill vs exact-Skill marginal-value experiments, held-out stimuli, distinct-stimulus independence and suite-composition security tests.
- Adds a human-friendly platform-by-platform installation guide, aligns README GitHub publishing instructions with the canonical source workflow, and documents runtime discovery verification including a dated Codex Windows Desktop repo-skill troubleshooting note.

## v1.0 — GitHub CI checkout hotfix (2026-09-02)

- Excludes Git checkout metadata under `.git/` from both canonical package-manifest comparison and static Skill scanning; GitHub Actions checkouts now validate/scan the same canonical source set as release ZIPs.
- Updates the validation workflow to current `actions/checkout@v7` and `actions/setup-python@v7` majors.
- Keeps the release version at v1.0 because this corrects release validation/CI portability rather than changing SKick runtime behavior.
