# Migrating SKick v1.0 to v1.1

SKick v1.1 releases the optional executable runtime while preserving the declarative Skill entrypoint, thin adapters, and existing install-path philosophy. Reinstall the complete v1.1 package when upgrading; do not merge generated files piecemeal.

## What stays compatible

- `SKILL.md` remains the declarative entrypoint.
- `core/` remains the canonical methodology.
- Existing thin adapter locations remain valid unless their compatibility record says otherwise.
- Existing project-local and user-level filesystem installations can continue to load the declarative Skill.
- Existing generic prompt fallback remains available.

## What changes

- Optional `runtime/` code makes capability/depth/module/evidence/claim behavior observable and testable.
- Platform records use explicit evidence statuses instead of a broad “verified” label.
- Model providers are separated from Skill hosts.
- Serena and the Python/vanilla starter profile are no longer constitutional defaults; they are capability/project policy options.
- Installation state distinguishes copied, installed, discovered, invokable and live-tested.
- Generated platform reports and module metadata are checked for drift.
- Provenance verification rejects canonical files missing from the manifest.

## Safe project-local migration

1. Record the current installed `VERSION` and install path.
2. Back up the existing `skick` directory if it contains local edits.
3. Compare local modifications before replacement; do not merge generated files blindly.
4. Install the complete v1.1 checkout/package into a temporary or project-local Skill destination first.
5. Run the host discovery check when the host exposes one.
6. Run a low-risk explicit activation test using the host-native mechanism.
7. If executable runtime is available, run `python3 scripts/skick_doctor.py --json` and deterministic unit/local evals.
8. Keep the previous v1 directory or archive until the new installation is proven usable.

## User/global installations

Use the same backup and comparison discipline. Do not overwrite a global install merely because a project-local test passed. Confirm the target host documents that global path and that the scope is desired.

## Generated metadata

Do not hand-edit generated platform/module reports. Update the canonical manifest/policy source and regenerate:

```bash
python3 scripts/generate_platform_catalog.py
python3 scripts/generate_module_catalog.py
```

Before a release, regenerate `tests/package-manifest.txt`, provenance metadata and checksums using the release scripts documented in `docs/RELEASE_CHECKLIST.md`.

## Rollback

Rollback is file-level and intentionally simple:

1. remove or rename the v1.1 `skick` install directory;
2. restore the backed-up v1 directory;
3. reload/restart only as required by that host;
4. verify v1 discovery using the host-native check;
5. do not copy v1.1 runtime/registry files into the restored v1 tree.

If a managed host stores uploaded Skills rather than filesystem directories, use its current version/remove/re-upload UI and retain the v1 archive before replacing it.

## Compatibility caveat

A `DOC_VERIFIED` route is not a migration guarantee. Live install/discovery/invocation must be performed on the actual target host before calling the migration live-verified.
