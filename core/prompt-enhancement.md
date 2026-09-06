# Prompt Enhancement


## Executable-runtime ownership
When the optional Python runtime is available, `runtime/prompt_intelligence.py` owns the deterministic task interpretation contract: original-request preservation, enhancement mode, constraint locking, prompt-quality fields, contradiction detection, success/verification needs, and strict-spec structure. This module remains the procedural/declarative fallback and contains guidance that still requires host/model judgment. Do not claim the runtime executed this contract on declarative-only hosts.
## Purpose
Convert normalized user intent into a compact execution-quality technical brief without changing the user's objective, inventing facts, or making the user restate context.

Run this module **after** semantic intent resolution and **before** capability routing, task classification, research, architecture or implementation.

## Mandatory enhancement rule
For every non-trivial SKick task, perform a **SILENT** enhancement pass before execution. Non-trivial includes repository work, current/version-sensitive research, architecture, debugging, security, migration, performance, design/build work, multi-tool workflows, or any task with material ambiguity or verification risk.

Do not force this ceremony onto tiny syntax/formatting questions. Enhancement must reduce ambiguity or improve execution; it must not inflate the task.

## Modes

### SILENT — default
Build the brief internally and execute it. Do not show a rewritten prompt merely to prove that enhancement happened.

### PROMPT-BUILDER
Use when the user explicitly asks to improve, rewrite, expand, structure, or create a technical/research prompt. Return the improved reusable prompt as the requested artifact.

## Invariants
- Preserve explicit goals, constraints, target, environment, output needs, exclusions and authorization boundaries.
- Distinguish user-supplied facts from inferred assumptions.
- Never invent versions, credentials, deployment details, errors, repositories, permissions or requirements.
- Correct terminology only when project/current evidence supports it.
- Resolve discoverable details from the project or authoritative research instead of asking unnecessary questions.
- Keep uncertainty explicit.
- Research depth and response length are separate decisions.
- Do not weaken evidence/verification requirements to save tokens.
- Do not convert an implementation request into implementation before repository/system understanding is sufficient.

## Compact brief schema
Use only fields that matter:

```text
GOAL:
TASK TYPE:
KNOWN CONTEXT:
VERSION / ENVIRONMENT / HOST:
CANONICAL TERMS:
PROJECT / REPOSITORY EVIDENCE TO INSPECT:
CAPABILITIES / SPECIALISTS NEEDED:
SEMANTIC-REPOSITORY CAPABILITY NEED:       # if code/repo work
ARCHITECTURE / CHANGE-IMPACT GATE:        # if substantial engineering
EXTERNAL EVIDENCE TO VERIFY:
LATERAL ANGLES / SIDE-CLUE SURFACES:
KEY UNCERTAINTIES / COMPETING HYPOTHESES:
CONTRADICTION / NEGATIVE-EVIDENCE CHECK:
SECURITY MODE / TRUST BOUNDARIES:         # if relevant
IMPLEMENTATION BOUNDARY:                  # if coding requested
VERIFICATION / ACCEPTANCE CRITERIA:
OUTPUT DENSITY:
```

## Enhancement decisions
Infer the actual outcome: direct answer, investigation, research+implementation, comparison/selection, architecture decision, migration, performance/reliability, security, paper/algorithm research, reverse engineering, or undocumented behavior.

Then:
1. normalize terminology and scope;
2. identify which evidence can resolve the task;
3. run `capability-and-skill-routing.md` for non-trivial work;
4. flag semantic repository intelligence for code/repo work and route to the best observed provider by capability fit;
5. flag `system-design-and-architecture.md` when change impact is not obvious;
6. create a bounded lateral-search/thinking plan for non-trivial research;
7. state observable acceptance/verification criteria before implementation.

Infer research depth:
- QUICK for narrow low-risk questions.
- DEEP by default for non-trivial technical research where current evidence or multiple mechanisms matter.
- EXHAUSTIVE only when explicitly requested or justified by high impact, persistent uncertainty, difficult contradictions, historical reconstruction, security/production consequence, or a wide evidence frontier.

Infer output density separately:
- COMPACT by default;
- STANDARD when explanation needs structure;
- FULL when the user asks for a detailed evidence trail or durable design artifact.

## Security-aware enhancement
When security matters, preserve the stated legitimate context and build a dual-lens brief where useful:

```text
SECURITY MODE: DEFENSIVE | OFFENSIVE-RESEARCH | PURPLE-TEAM | TRIAGE | THREAT-INTEL | INCIDENT | MALWARE | SECURE-DESIGN | SUPPLY-CHAIN | VALIDATION
OBJECTIVE:
TARGET / SCOPE / AUTHORIZATION:
TRUST BOUNDARIES:
ADVERSARIAL QUESTION:
PREREQUISITES TO RESEARCH:
TELEMETRY / ARTIFACTS:
PREVENT / DETECT / LIMIT / RESPOND / RECOVER / VERIFY:
```

Do not add operational exploitation merely because the topic is security.

## Prompt-builder quality gate
When returning an enhanced prompt, ensure it:
1. states the intended outcome and non-goals;
2. defines evidence, freshness/version and project-inspection requirements;
3. asks the host to use the best task-matched installed capability rather than a fixed vendor stack;
4. requires capability-fit semantic repository work when it materially improves code understanding, with an explicit exact-search/file-read fallback;
5. requires architecture/change-impact understanding before broad implementation;
6. requires terminology mutation, lateral research/thinking and side-clue capture for non-trivial research;
7. requires contradiction/negative-evidence checking;
8. specifies implementation only if requested;
9. requires explicit acceptance criteria, verification and uncertainty;
10. remains portable by naming capabilities rather than proprietary tools except where a runtime adapter intentionally names them.
