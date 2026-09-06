# SKick Release Checklist

A release is a proof boundary, not a platform-count or README-size milestone.

## 1. Freeze identity and source

- [ ] Confirm the intended `VERSION`; do not bump solely for marketing.
- [ ] Record the exact release commit/tag.
- [ ] Confirm `SKILL.md` remains the compact declarative control plane and all progressive-loading links resolve.
- [ ] Confirm no secret, cache, local transcript, provider credential, generated ZIP or unrelated worktree artifact entered canonical source.

## 2. Regenerate canonical derived data

After all source edits are complete:

```bash
python3 scripts/generate_module_catalog.py
python3 scripts/generate_platform_catalog.py
python3 scripts/sync_adapter_install_blocks.py
```

Then verify regeneration is side-effect free:

```bash
python3 scripts/generate_module_catalog.py --check
python3 scripts/generate_platform_catalog.py --check
python3 scripts/sync_adapter_install_blocks.py --check
```

Update the package file manifest and provenance only after the source tree is final. Re-run the corresponding checks after generation so a generated file cannot invalidate an earlier audit.

## 3. STATIC proof layer

```bash
python3 -m compileall -q scripts runtime tests
python3 scripts/scan_skill_package.py . --strict
python3 scripts/validate_mcp_catalog.py mcp/catalog.json
python3 scripts/normalize_platform_registry.py --check
python3 scripts/generate_platform_catalog.py --check
python3 scripts/generate_module_catalog.py --check
python3 scripts/audit_freshness.py . --max-age-days 120 --fail-stale
python3 scripts/validate_package.py .
python3 scripts/audit_release.py
python3 scripts/verify_provenance.py .
```

STATIC success proves repository/package/config consistency. It does **not** prove AI behavior or external-platform execution.

## 4. UNIT proof layer

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/run_local_evals.py evals/runtime-routing-evals.json
python3 scripts/run_local_evals.py evals/claim-honesty-evals.json
python3 scripts/run_local_evals.py evals/security-injection-evals.json
python3 scripts/run_local_evals.py evals/ablation-evals.json
```

Record routing/depth, claim-honesty and ablation regressions explicitly.

## 5. INTEGRATION proof layer

Build outside canonical source:

```bash
python3 scripts/build_distributions.py . /tmp/skick-dist
python3 scripts/validate_distributions.py /tmp/skick-dist
```

Run installer dry-runs and isolated fixture installs for representative project/user scopes. A file-copy pass is not discovery or invocation proof.

## 6. BEHAVIORAL proof layer

Where model/provider access exists, compare controlled no-SKick baseline, released SKick and candidate SKick using held-out tasks and repeated trials where stochastic variance matters. Preserve raw executor results, deterministic checks, optional judge metadata and task-level regressions.

If a clean no-SKick baseline cannot be produced, mark the comparison `BASELINE_BLOCKED`; do not estimate the missing result.

## 7. PLATFORM proof layer

Every canonical compatibility route must have a current evidence status. `LIVE_TESTED` requires a reproducible live-test record with SKick version, host version/environment, activation method, test task/date and result. `DOC_VERIFIED` must never be rendered as live proof.

Route additions/removals/status downgrades are acceptable when evidence changes. Do not enforce a minimum route count.

## 8. Security and migration

- [ ] Run injection/claim-honesty suites.
- [ ] Review changed external Skills/MCP/tool dependencies and permissions.
- [ ] Verify installer path/overwrite/backup behavior on fixtures.
- [ ] Confirm `docs/SECURITY_THREAT_MODEL.md` still matches implementation.
- [ ] Test representative v1 -> candidate project-local migration and rollback without destroying user customization.

## 9. Release decision

Do not call a candidate production-ready unless static, unit and integration gates pass, compatibility claims are evidence-backed, generated data is synchronized, critical deterministic/behavioral metrics do not materially regress, migration/limitations are documented, and the security review is complete.

Cross-platform live testing may remain incomplete only if statuses say so explicitly.
