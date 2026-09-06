# Contributing to SKick

SKick is designed to be forked and extended without losing a single canonical methodology. This guide explains how a human or AI maintainer should fork, modify, validate, and release it.

## 1. Fork and clone

Fork the repository on your Git hosting service, then clone your fork and create a focused branch.

```bash
git clone <your-fork-url>
cd <repo>
git checkout -b change/<short-topic>
```

If you received only the source ZIP, unpack it into a new git repository before making substantial changes so every modification is reviewable.

## 2. Read the project context first

Before editing, read:

1. `AI_HANDOFF.md`
2. `SPEC.md`
3. `SKILL.md`
4. the relevant `core/`, `adapter/`, integration, or docs file;
5. `SOURCES.md`, `UPSTREAMS.md`, and `THIRD_PARTY_NOTICES.md` when external projects or runtime behavior are involved.

For AI maintainers, also read `AI_CONTEXT.json`.

## 3. Change the correct layer

- Change **canonical behavior** in `core/`.
- Change **control-plane routing/indexing** in `SKILL.md`.
- Change **platform installation/discovery/tool specifics** in the matching runtime directory under `adapters/`.
- Change **operational/user documentation** in `docs/`.
- Change **optional specialist interoperability** in `integrations/`.
- Change **optional design specializations** in `extensions/`.
- Change **MCP metadata/config generation** in `mcp/` and its scripts.
- Change **generated wrappers** only by changing their builder/template source and rebuilding them.

Do not copy the whole `core/` methodology into an adapter, prompt, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, plugin manifest, or IDE rule file.

## 4. External/current claims

For version-sensitive platform behavior, installation paths, commands, manifests, APIs, plugin systems, or MCP support:

1. verify current first-party documentation;
2. prefer primary sources over blogs/aggregators;
3. record the evidence in `SOURCES.md`;
4. use conservative status language in `PORTABILITY.md`;
5. never upgrade a platform to `VERIFIED` based only on structural resemblance or a third-party claim.

## 5. Add regression coverage

When a change could regress behavior, add or update cases in `evals/` or `tests/`. Installation/platform changes should normally update portability coverage.

## 6. Validate locally

From the SKick root:

```bash
python3 scripts/scan_skill_package.py . --strict
python3 scripts/validate_mcp_catalog.py mcp/catalog.json
python3 scripts/validate_package.py .
python3 scripts/audit_release.py
python3 scripts/run_evals.py evals/evals.json --output /tmp/skick-evals.json --list
python3 scripts/run_evals.py evals/trigger-evals.json --output /tmp/skick-trigger-evals.json --list
python3 scripts/run_evals.py evals/portability-evals.json --output /tmp/skick-portability-evals.json --list
python3 scripts/build_provenance.py .
python3 scripts/verify_provenance.py .
```

Then rebuild distributions:

```bash
python3 scripts/build_distributions.py . /tmp/skick-dist
python3 scripts/validate_distributions.py /tmp/skick-dist
```

Use the official Skill validator/packager for the canonical upload artifact when available.

## 7. Version and changelog

- User-facing release labels use `v1.0`, `v1.1`, etc.
- Machine manifests that require semantic versioning use `1.0.0`, `1.1.0`, etc.
- Update `VERSION`, builder manifest versions, and `CHANGELOG.md` together when cutting a real release.
- Do not bump the release for an unshipped local experiment unless the project policy intentionally calls for it.

## 8. Rebuild, do not hand-patch

Generated archives are outputs and should not be committed as maintenance source. Rebuild them from canonical source. If a wrapper needs a new file, modify `scripts/build_distributions.py` or the corresponding canonical adapter/template and regenerate.

## 9. Pull request expectations

A good PR explains:

- what changed;
- why it changed;
- which runtime/version/source was verified if applicable;
- what tests/validators were run;
- any compatibility/security implications;
- whether target-runtime execution was actually performed.

## 10. Fork-specific customization

A fork may intentionally diverge in branding, default architecture, integrations, or policies. Record intentional divergences in a fork-local section of `SPEC.md` or a new `FORK_NOTES.md`; do not hide them inside generated outputs.

If the fork changes safety, trust, provenance, or action boundaries, call that out explicitly in the README and changelog.

## 11. Sending the fork to another AI

Do not rely on chat history. Ensure these files remain current:

- `START_HERE.md`
- `AI_HANDOFF.md`
- `AI_CONTEXT.json`
- `INSTALLATION_MANIFEST.json`
- `SPEC.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`

A future AI should be able to reconstruct the project's purpose, invariants, installation behavior, support status, and maintenance process from the repository alone.

## 12. vNext platform evidence requirements

A new or materially changed platform/runtime/provider route must update the canonical `INSTALLATION_MANIFEST.json` record rather than creating a second compatibility database. Provide:

- canonical platform ID and entity type;
- native Skill support (`yes`, `no`, `unknown`, or host-dependent equivalent);
- install method and scope/path only when evidenced;
- discovery mechanism;
- explicit activation state;
- literal `@SKick` support as `yes`, `no`, or `unknown` — never infer it from another host;
- native activation equivalent;
- automatic activation state;
- runtime/guarantee tier;
- relevant capabilities and limitations;
- verification status and last-verified date;
- first-party evidence when claiming `DOC_VERIFIED`;
- reproducible host/version/task metadata when claiming `LIVE_TESTED`.

A lower route count is acceptable when evidence shows a route is broken, host-dependent, or unknown. Truthful downgrades are not regressions by themselves.

After changing the registry, regenerate and check:

```bash
python3 scripts/generate_platform_catalog.py
python3 scripts/generate_platform_catalog.py --check
```

## 13. vNext module contribution requirements

A new `core/` or `extensions/` module must justify its context cost. The change should identify:

- the problem not adequately covered by existing modules;
- activation conditions and exclusion conditions where relevant;
- dependencies/capability requirements;
- estimated context cost using the repository's current estimate method;
- overlap with existing modules;
- at least one deterministic or behavioral eval case that would regress if the module/routing rule were removed.

Update `runtime/module_policies.json` where selection metadata is needed, regenerate `runtime/module_catalog.json`, and run the module compiler tests. Module count is not a quality target.

## 14. Module deprecation and merge process

When a module becomes redundant or harmful, prefer measured simplification. Record the deprecated module, replacement/merge target, reason, eval or ablation evidence, compatibility impact, and intended removal version. Remove references from `SKILL.md` and generated metadata together; do not leave dead progressive-loading links.

## 15. Evaluation and proof terminology

Keep these proof layers distinct in code, tests and documentation:

- static validation;
- deterministic runtime/integration test;
- behavioral evaluation;
- documentation verification;
- live platform test.

An eval runner must not accept the candidate's self-reported success as the sole pass criterion. Preserve raw results and make task-level regressions inspectable.
