# SKick v1.0 Release Audit

This file records the release gates applied to the canonical SKick v1.0 source before packaging. It is evidence of checks performed on this repository state, not a guarantee that every external product version will behave identically forever.

## Audit scope

The release was checked across these categories:

- canonical Skill structure and frontmatter
- silent prompt-enhancement and invocation behavior
- best-skill/capability routing and specialist ownership
- Serena-first repository-intelligence fallback behavior
- system-design/change-impact gating before broad implementation
- deep research, lateral search, lateral thinking and side-clue capture
- research evidence frontier, opened-source discipline, claim/source lineage, counterevidence and decision-flip conditions
- language/framework/toolchain version fingerprinting and language-native proof surfaces
- UI design-system preservation, rendered-state validation and measured-vs-inferred evidence boundaries
- engineering wayfinding, decision frontiers, tracer-bullet slicing and prototype/merge-intent discipline
- red/blue/purple security lifecycle, detection engineering, DFIR integrity and vulnerability-priority reasoning
- external Skill/plugin full-bundle supply-chain inventory, pin/hash/lock lifecycle and composition privilege review
- SKick-only naming and stale-brand detection
- README image paths and local Markdown links
- PNG asset presence and dimensions
- Python syntax and JSON parsing
- runtime/platform manifest consistency
- ZIP and GitHub-URL AI bootstrap behavior
- installation safety and overwrite handling
- platform distribution structure
- Gemini Apps text-only distribution constraint
- MCP catalog validation
- static package safety scan
- eval-suite schema/load checks
- provenance and checksum generation/verification
- Skill validation/packaging contract
- GitHub CI/repository hygiene

## Runtime coverage model

`INSTALLATION_MANIFEST.json` contains **62 explicit routes**. The catalog deliberately distinguishes:

1. **Verified host routes** — current first-party or strong product documentation establishes a native Skill path, command, or UI contract.
2. **Verified managed imports** — the product exposes a managed upload/import flow rather than a writable local Skill directory.
3. **Inherited/product-ecosystem routes** — the host derives from or documents compatibility with a verified Skill-capable runtime; the installed version must still be checked before automation.
4. **Provider/model routes** — a model name is not treated as an installation target. SKick is installed in the actual host agent/harness instead.
5. **Unknown/future runtimes** — use the runtime-family fallback ladder in `docs/RUNTIME_COMPATIBILITY.md` and `docs/NEW_RUNTIME_INTEGRATION.md`; never invent a native path.

High-priority coverage includes ChatGPT/Codex, Claude/Claude Code, Gemini, GitHub Copilot, Cursor, OpenCode, BrowserCode, Qwen Code, Kimi Code, Xiaomi MiMoCode, Factory Droid, Crush, Manus, MiniMax-hosted workflows, LongCat-hosted workflows, TRAE/ByteDance-hosted workflows, Cline, Roo Code, Windsurf, Mistral, DeepSeek/DeepCode, GLM, Grok, ZCode, Sarvam and additional agent/harness families listed in the platform catalog.

## Current-source checks used for version-sensitive routes

The release source ledger records current documentation/repositories including:

- ChatGPT Skills/plan gate: `https://help.openai.com/en/articles/20001066`
- Claude custom Skills: `https://support.claude.com/en/articles/12512198-how-to-create-custom-skills`
- Kilo Code Skills: `https://kilo.ai/docs/customize/skills`
- Devin repository Skills: `https://docs.devin.ai/product-guides/skills`
- Qoder Skills: `https://docs.qoder.com/extensions/skills`
- Zed Agent Skills: `https://zed.dev/docs/ai/skills`
- Agent Skills open specification: `https://agentskills.io/`
- Cursor Agent Skills: `https://docs.cursor.com/context/skills`
- GitHub Copilot Agent Skills/CLI: `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills`
- Gemini CLI Agent Skills: `https://geminicli.com/docs/cli/skills/`
- Factory Droid Skills: `https://docs.factory.ai/harness/skills`
- Crush: `https://github.com/charmbracelet/crush`
- Manus Skills import: `https://help.manus.im/en/articles/14753565-how-to-share-and-use-skills-in-manus`
- OpenCode Skills: `https://opencode.ai/docs/skills`
- Qwen Code Agent Skills: `https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/`
- Kimi Code Agent Skills: `https://moonshotai.github.io/kimi-code/en/customization/skills/`
- Xiaomi MiMoCode source: `https://github.com/XiaomiMiMo/MiMo-Code`
- MiniMax Skills: `https://github.com/MiniMax-AI/skills`
- BrowserCode source: `https://github.com/browser-use/browsercode`
- LongCat source: `https://github.com/meituan-longcat/LongCat-2.0`
- Serena: `https://github.com/oraios/serena`
- Android Skills: `https://github.com/android/skills`
- Kotlin Agent Skills: `https://github.com/Kotlin/kotlin-agent-skills`
- Angular Agent Skills: `https://github.com/angular/skills`
- Microsoft Skills / Deep Wiki: `https://github.com/microsoft/skills`
- .NET Skills: `https://github.com/dotnet/skills`
- Playwright agent CLI/MCP: `https://playwright.dev/`
- Trail of Bits Skills: `https://github.com/trailofbits/skills`
- MITRE ATT&CK/D3FEND/CAPEC/CALDERA, SigmaHQ, CISA KEV and FIRST EPSS for security framework/data references
- OWASP GenAI agentic red-team taxonomy
- skills-lock: `https://github.com/luisalima/skills-lock`

See `SOURCES.md` and each adapter for the full evidence trail and support classification.

## Local automated results

The following checks were executed against the v1.0 source during the final 2026-09-03 v1.0 hardening cycle:

| Gate | Result |
| --- | --- |
| Python compile check | PASS |
| Strict static Skill scan | PASS — 0 high, 0 warning; 8 informational context matches only |
| MCP catalog validation | PASS — 15 servers, 13 profiles, 3 validators |
| Release audit script | PASS — 62 platform routes, 0 errors, 0 warnings |
| Canonical package validation | PASS — 73 core modules, 58 adapter docs |
| General eval suite load/list | PASS — 97 cases |
| Trigger eval suite load/list | PASS — 53 cases |
| Portability check suite load/list | PASS — 38 checks |
| Distribution build | PASS — 9 ZIP distributions plus generic prompt/installer docs |
| Distribution structural validation | PASS |
| Distribution ZIP integrity | PASS — every generated ZIP passed archive testing |
| GitHub bootstrap payload presence | PASS — root bootstrap prompt, protocol, capability broker and architecture gate present in runtime package |
| GitHub checkout source parity | PASS — `.git/` metadata is excluded from canonical package-file comparison and static package scanning |
| Repository slimming | PASS — redundant bridge/generated files removed; README visual assets compressed to WebP; runtime/provenance/eval files retained |
| Platform install guide | PASS — managed, verified filesystem, recheck-first-party, provider-only and generic/future routes documented with verification boundaries |
| Filesystem installer smoke tests | PASS — Factory Droid and Crush project installs |
| Existing-install refusal | PASS |
| Provenance verification | PASS — 235 tracked source files after repository slimming |
| Skill quick-validation contract | PASS — frontmatter/name/description checks |
| Skill packaging contract | PASS — exactly one `SKILL.md`; canonical archive below the 25 MiB upload limit |
| Canonical ZIP integrity | PASS — no corrupt archive entry detected |
| GitHub-ready bundle integrity | PASS |
| Universal handoff bundle integrity | PASS |

Because this report and final release scripts are part of the source tree, provenance, distributions and canonical packaging are regenerated once more after this report is finalized. Published artifacts must therefore be checked against the final checksums rather than intermediate byte counts.

## Behavior-specific regression coverage

The eval suites now explicitly cover:

- selecting the best available capability/specialist rather than blindly using SKick internals
- preserving one workflow owner per phase while SKick keeps objective/evidence/safety/verification control
- mandatory silent prompt enhancement for non-trivial work
- Serena-first repository mapping when Serena is actually available and a documented semantic fallback when it is not
- architecture/change-impact understanding before broad implementation
- lateral query mutation, adjacent-source exploration, competing hypotheses and side-clue/serendipity capture
- GitHub URL bootstrap, real host-runtime detection, project-scope preference and non-invention of unsupported install paths
- language/framework version routing, language-native compiler/analyzer/test/trace proof surfaces and differential port parity
- UI design-system/state-matrix behavior plus rendered/measured-vs-inferred evidence boundaries
- research opened-source/frontier/source-lineage/counterevidence/flip-condition behavior
- decision-frontier wayfinding, tracer-bullet delivery, prototypes-as-questions and intent-aware merge resolution
- purple-team coverage-state separation, detection lifecycle, KEV/EPSS-aware prioritization, variant analysis and DFIR evidence integrity
- external Skill full-bundle inventory, pin/hash/lock lifecycle, cross-Skill privilege composition and no-Skill-vs-Skill marginal-value evaluation

## What was not claimed

- The audit does **not** claim live execution inside all 62 external products.
- A successful filesystem copy is not the same as runtime discovery.
- Managed web/app installs may require user, admin, authentication or UI actions that a filesystem agent cannot perform.
- Ecosystem-derived paths must be rechecked against the installed product version before large-scale automation.
- Model/provider names do not prove a Skill installation mechanism.
- Serena is never reported as active unless the current host actually exposes and activates it; otherwise SKick must use and report the documented semantic-code fallback.
- Ideas discovered through lateral thinking are hypotheses until corroborated by evidence or validated by testing.

## Release rule

Do not publish a release if any required local gate fails. If a platform changes after release, update its adapter and source evidence, add regression coverage where practical, regenerate the platform catalog, rebuild distributions and rerun the full checklist in `docs/RELEASE_CHECKLIST.md`.

## 2026-09-03 final hardening boundary

The new language, UI, research, purple-team and supply-chain modules are portable methodology and reference routing. This release does **not** claim live execution inside every language/framework specialist, Playwright/DevTools/Figma/Stitch surface, CALDERA deployment, SIEM, DFIR lab, or external Skill scanner. External runtime/tool behavior must still be detected, authorized, version-checked and verified at use time. Security framework mappings organize hypotheses and evidence; they do not prove exploit reachability, detection efficacy or operational authorization.
