# SKick Release Checklist

Use this for every release or externally shared fork build.

- [ ] Read `AI_HANDOFF.md`, `SPEC.md`, and the pending changelog.
- [ ] Confirm canonical changes live in the correct layer (`core/`, adapter, integration, docs, scripts).
- [ ] Re-check first-party sources for changed platform/runtime claims.
- [ ] Update `SOURCES.md`, `PORTABILITY.md`, and `INSTALLATION_MANIFEST.json` when install/support behavior changed.
- [ ] Update or add evals/tests for changed behavior.
- [ ] Confirm `BOOTSTRAP_PROMPTS.md` still contains a compact universal GitHub prompt and runtime-specific fast paths grounded in current docs.
- [ ] Confirm `docs/PLATFORM_INSTALL_GUIDE.md` matches the manifest/adapters for major managed and filesystem hosts and labels recheck-first-party/provider-only routes conservatively.
- [ ] Confirm `docs/GITHUB_BOOTSTRAP.md` preserves inspect-first GitHub handling, real-host detection, conservative scope, Serena authorization boundaries, and runtime discovery verification.
- [ ] Re-test capability-broker, Serena-first, architecture-gate, and lateral-thinking eval cases.
- [ ] Re-test language/framework version routing and language-native proof-surface evals.
- [ ] Re-test UI rendered-vs-inferred measurement and design-system/state-matrix evals.
- [ ] Re-test research frontier/opened-source/counterevidence/flip-condition evals.
- [ ] Re-test purple-team coverage-state, variant-analysis, vulnerability-priority and DFIR-integrity evals.
- [ ] Re-test external Skill full-bundle inventory, pin/hash/lock, cross-Skill privilege composition and marginal-value evals.
- [ ] Re-test decision-frontier/tracer-bullet/prototype/intent-merge engineering-wayfinding evals.
- [ ] Run `python3 scripts/scan_skill_package.py . --strict`.
- [ ] Run `python3 scripts/validate_mcp_catalog.py mcp/catalog.json`.
- [ ] Run `python3 scripts/validate_package.py .`.
- [ ] Run `python3 scripts/audit_release.py`.
- [ ] Load-check `evals/evals.json`, `evals/trigger-evals.json`, and `evals/portability-evals.json` with `scripts/run_evals.py ... --output <tmp> --list`.
- [ ] Run `python3 scripts/build_provenance.py .`.
- [ ] Run `python3 scripts/verify_provenance.py .`.
- [ ] Build distributions outside canonical source, e.g. `python3 scripts/build_distributions.py . /tmp/skick-dist`.
- [ ] Run `python3 scripts/validate_distributions.py /tmp/skick-dist`.
- [ ] Validate/package the canonical Skill with the official Skill tooling where available.
- [ ] Confirm `START_HERE.md`, `BOOTSTRAP_PROMPTS.md`, `AI_HANDOFF.md`, `AI_CONTEXT.json`, `INSTALLATION_MANIFEST.json`, and `docs/GITHUB_BOOTSTRAP.md` are included in the final ZIP.
- [ ] Confirm PNG logo/icon/favicon assets and all four README images are present, render correctly, and use SKick-only branding.
- [ ] Confirm no credentials, tokens, private keys, cookies, or local secret configuration entered the package.
- [ ] Confirm generated artifacts were rebuilt rather than hand-patched.
- [ ] Update `CHANGELOG.md` and release/version metadata.
- [ ] Record what was structurally validated versus actually executed in target runtimes.
