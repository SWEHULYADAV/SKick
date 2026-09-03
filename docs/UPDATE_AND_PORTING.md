# Updating and Porting SKick

## Goal

Keep one canonical methodology while allowing many runtimes to install or invoke it differently.

## Update rule

Never fork `core/` into platform-specific copies. Update canonical methodology once, then keep adapters thin.

## Before changing a platform adapter

1. Identify the actual runtime and installed version.
2. Read current first-party documentation for Skills/plugins/instructions/MCP/hooks/subagents/persistent state.
3. Determine whether the change is installation-only or changes runtime capability.
4. Update `SOURCES.md` with the first-party source.
5. Update the relevant runtime adapter README under the adapters directory.
6. Update `PORTABILITY.md` status if native support changed.
7. Add/adjust portability evals if the change can regress behavior.
8. Rebuild generated distributions and validate them.

## Adding a new runtime

Prefer, in order:

1. Native/open Agent Skill support.
2. Agent Plugin v1 if explicitly supported.
3. A thin host plugin wrapper.
4. Project/global instruction bridge.
5. Generic prompt fallback.

Do not invent a manifest or install path from another runtime.

## Updating the core

A core change should normally update:

- the relevant canonical core module;
- `SKILL.md` only if the control plane/index changes;
- evals/tests that protect the behavior;
- `CHANGELOG.md`;
- upstream/provenance notes if external research materially informed the change;
- validation scripts if a new required invariant/file is introduced.

## Versioning

User-facing release: `v1.0` style.

Machine-facing manifests should use valid semantic versions where required (for example `1.0.0`). Keep the two representations intentionally mapped rather than accidentally mixing them.

## Compatibility philosophy

A portable Skill should preserve behavior even when tools differ. A host may change how files are searched, commands are executed, browser automation is performed, or MCP is configured. It should not silently change the research method, safety boundaries, or default architecture profile.


## Fork workflow

A fork should preserve its divergence explicitly rather than burying changes in generated archives.

1. Fork/clone the canonical source.
2. Read `../AI_HANDOFF.md`, `../AI_CONTEXT.json`, `../SPEC.md`, and `../CONTRIBUTING.md`.
3. Record intentional fork differences in source control (optionally `FORK_NOTES.md`).
4. Change the canonical layer first.
5. Update `../INSTALLATION_MANIFEST.json` and adapters when platform behavior changes.
6. Add/adjust evals and validation rules.
7. Rebuild provenance and distributions.
8. Run the release checklist in `RELEASE_CHECKLIST.md`.
9. Publish generated artifacts only after the canonical tree passes validation.

## AI-to-AI continuation

A future AI should not depend on chat history. Keep `../START_HERE.md`, `../AI_HANDOFF.md`, `../AI_CONTEXT.json`, `../INSTALLATION_MANIFEST.json`, `../CONTRIBUTING.md`, and `../CHANGELOG.md` current. Use `../AI_HANDOFF.md` as the canonical continuation contract.
