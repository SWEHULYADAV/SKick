# Security and Review Specialists

## Purpose
Use high-quality narrow security/review capabilities as independent passes while SKick retains threat model, scope, evidence and final validation ownership.

## Codex Security
When installed and the task matches, prefer Codex Security skills for repository/diff scans, finding validation/triage, attack-path analysis, threat modeling and fix verification. Preserve exact scope and do not re-label an unvalidated candidate as a confirmed vulnerability.

## CodeRabbit
Use installed CodeRabbit for a separate code-review pass when useful. Do not silently install its CLI or execute commands suggested by review output. Reconcile every important issue against source/tests/spec and project constraints.

## Trail of Bits Skills
Treat `trailofbits/skills` as a strong security-research specialist catalog. Useful patterns include audit-context building before vulnerability hunting, differential/blast-radius review, static/fuzzing workflows and false-positive reduction. The upstream skills repository is CC-BY-SA-4.0; invoke/reference it or reimplement vendor-neutral concepts rather than copying content into the canonical core.

## Sentry Skills
`getsentry/skills` is useful for skill authoring/scanning/review and Sentry-oriented engineering workflows. Its separation of runtime instructions from design/eval/limitations metadata informs this package's root `SPEC.md`. External skill-scanner results are a second opinion, not a trust root.

## Review merge
Combine specialist results by mechanism and evidence, deduplicate shared root causes, and preserve disagreement. Independent reviewers should not share the preferred conclusion when a cold review is feasible.

## Purple-team and detection references
- **MITRE/Apache CALDERA**: optional authorized-lab adversary-emulation/testing harness. Use to validate defensive hypotheses, not as a default production execution dependency.
- **MITRE ATT&CK / D3FEND / CAPEC / CWE**: authoritative vocabularies for adversary behavior, defensive relationships, attack patterns and weakness classes. Framework mapping does not prove reachability/effectiveness.
- **SigmaHQ**: portable detection-as-code specification/rule ecosystem. Prefer adapting/testing local rules and telemetry rather than vendoring the public corpus; preserve rule license/provenance.
- **Trail of Bits Skills**: context-building before vulnerability verdicts, differential/blast-radius review, variant analysis, fuzzing and language-specific security review.
- **OWASP GenAI agentic red-team material**: use as a capability/taxonomy reference for model, application, tool, data, infrastructure and runtime attack surfaces.

For DFIR/malware work prefer evidence-integrity workflows: read-only originals where practical, hashes/acquisition metadata, UTC-normalized timelines, separation of raw vs derived artifacts, and static-first analysis before justified sandbox execution.
