# Skill Authoring and Evaluation

## Purpose
Research, create, update, and validate reusable agent skills with progressive disclosure, strong trigger metadata, explicit capabilities, and regression evals.

## Structure principles
A portable skill normally needs:
- one entrypoint with a precise name and trigger-rich description;
- concise execution instructions;
- references for long domain material;
- scripts for deterministic/repetitive operations;
- assets only when outputs need them;
- runtime-specific metadata/adapters kept outside the canonical method when possible.

Follow the target platform's current specification. Do not assume optional frontmatter fields are portable across every host.

## Trigger quality
The description should state both:
- what the skill does;
- concrete situations/keywords in which it should trigger.

Avoid descriptions that are so broad they steal unrelated work or so narrow they under-trigger obvious use cases.

## Capability declaration
When the host supports capability/tool metadata, declare only what the skill actually needs. Cross-check instructions and scripts for undeclared shell, network, browser, file-write, secret, or external-service behavior.

## Progressive disclosure
Keep the entrypoint small. Load large references only when the current branch needs them. Prefer executing trusted helper scripts with `--help` or documented interfaces over reading thousands of lines into context when the script can act as a black box.

## Eval set
For non-trivial skills, maintain:
- positive trigger prompts;
- difficult negative/near-miss prompts that should not trigger;
- workflow/behavior prompts;
- failure and edge-case prompts;
- platform-specific packaging/install smoke cases when portability matters.

A useful trigger set is roughly balanced and varied; for a substantial skill, start around 20 realistic prompts rather than testing only obvious keywords. Keep a held-out subset when tuning the description so the trigger text is not optimized only to the examples used to write it.

Tests should be realistic multi-step requests, not trivial one-line tasks the base model can complete without the skill.

## Expectations
Each eval can define observable expectations such as:
- correct skill route selected;
- required source family consulted;
- no prohibited source treated as authoritative;
- expected artifact/section produced;
- destructive action not taken without authorization;
- test or verification step actually executed when claimed;
- compact output style preserved.

Keep qualitative review alongside any automated score. A numerical trigger score does not prove workflow quality. When repeated runtime evals are feasible, record run count, mean, dispersion/variance, model/runtime/version, and token/time measurements separately; a one-run improvement is not a stable benchmark.

Separate **static validation** (schema, links, manifests, files) from **behavioral evaluation** (triggering, workflow, quality). Static PASS never means the skill actually performed well in a target model.

## Executable harness
Use `scripts/run_evals.py` with a target-runtime runner adapter for repeated behavioral runs, and `scripts/compare_evals.py` for baseline/candidate metrics. The harness deliberately does not invent a semantic judge; the runtime adapter must return explicit pass/check results or leave them unscored.

## Learned-skill candidate gate
If a runtime mines prior sessions to propose a new Skill or Skill patch, treat the output as an inactive candidate. Redact secrets, validate format/target paths, dry-run patches, inspect the full diff, run relevant trigger/behavior evals, and require explicit promotion when the change would affect durable behavior. Never auto-merge transcript-derived instructions into a canonical Skill.

## Update workflow
For an existing skill:
1. preserve the canonical skill name unless the user asks for a rename;
2. copy to a writable workspace;
3. inspect current structure and tests;
4. research external patterns if useful;
5. make the smallest coherent update;
6. run validators and representative evals;
7. compare failures with the previous behavior where possible;
8. package the full updated skill, not a patch;
9. record upstream provenance and remaining limitations.

## Principle of least surprise
A skill should do what its description leads a user to expect. Hidden downloads, secret access, telemetry, external billing, destructive edits, or broad permissions require explicit disclosure and authorization.

## Maintenance specification
For a substantial skill, a separate design/maintenance contract can document intent, non-goals, eval assumptions, limitations and provenance without bloating runtime `SKILL.md`. This package uses root `SPEC.md` for that purpose. It is not a portable Skill requirement and must not be treated as governing runtime instruction.

For stronger external behavioral evaluation, load `evaluation-harness-integration.md`; do not optimize a skill solely against its own homegrown runner.

## Skill value and suite-composition evaluation
For a substantial or costly Skill, include a no-Skill baseline and exact-Skill variant where the runtime/harness supports it. Use held-out stimuli and avoid treating repeated runs of one prompt as many independent examples. Measure routing/activation, task correctness, tokens/context, latency and failure modes separately. Also test high-privilege Skills in realistic installed sets because composition can create risks that single-Skill tests miss. See `skill-supply-chain-and-lifecycle.md`.
