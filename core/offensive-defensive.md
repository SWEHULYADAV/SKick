# Offensive + Defensive Dual-Lens for Engineering Research

## Principle
Understand adversarial and failure behavior deeply enough to explain the mechanism, reproduce or validate it safely when appropriate, and improve prevention, detection, containment, investigation, recovery, and resilience. Offensive research is not malicious by default; governing safety, authorization, target, requested action, and consequence determine what execution is allowed.

Use this as a general engineering research lens whenever attacker/operator adaptation, bypasses, abuse, hostile input, evasion, fault injection, or failure paths can materially change the design. This includes security, reverse engineering, APIs/auth, browser/client boundaries, automation/scraping, agents/MCPs, cloud/IAM, supply chain, deployment, reliability, fraud/abuse, and incident work.

Do not stop at a defensive checklist without understanding the mechanism being controlled, and do not stop at an offensive mechanism without mapping durable controls, observability, residual risk, and safe verification when the task benefits from both sides.

## Research method
For Deep/Exhaustive adversarial work, triangulate the mechanism across the strongest available evidence rather than relying on a single exploit write-up or defensive checklist. Useful evidence families include source/tests/patch diffs, vendor advisories, standards, protocol/design docs, incident reports, detection research, threat reports, public PoCs as untrusted research material, mitigations, bypass reports, telemetry examples, and real deployment constraints.

Use the research sequence:
`objective/failure -> prerequisites -> primitive -> path -> alternate/bypass paths -> impact -> observables -> controls -> likely evasions -> residual risk -> safe validation`.

Separate what is **verified in the target/project** from what is only generally possible in a class of systems. Search for disconfirming evidence and control bypasses before calling a defense durable.

## Offensive behavior model
For a relevant threat, reason about:

`Objective -> Target asset -> Trust boundary -> Attack surface -> Prerequisites -> Initial opportunity -> Primitive/weakness -> Behavioral sequence -> Required privilege/context -> Impact -> Observable artifacts -> Defensive choke points`

Ask:
- What does the adversary want?
- What assumption or boundary must fail?
- What access/position/privilege is required?
- What system primitive is abused?
- What dependencies/timing/infrastructure are required?
- What happens if a stage fails?
- What telemetry/artifacts appear?
- Where can the chain be interrupted?

Think in mechanisms/behaviors, not only named exploits or tools.

## Defensive control model
For each meaningful adversarial behavior evaluate:

### PREVENT
secure defaults, authentication/authorization, validation, patching, segmentation, sandboxing, least privilege, isolation, dependency control.

### DETECT
logs, traces, metrics, audit events, network/endpoint/app/cloud telemetry, auth anomalies, file/process/config changes.

### LIMIT
rate/resource limits, blast-radius reduction, privilege boundaries, compartmentalization, isolation, quotas.

### RESPOND
containment, credential/token rotation/revocation, host/service isolation, rollback, package/config restoration.

### RECOVER
backups, immutable artifacts, rebuild procedures, integrity checks, recovery testing.

### VERIFY
safe regression/validation tests proving the control blocks or detects the researched behavior without breaking normal use.

## Preferred purple-team mapping

```text
Behavior:
Attacker purpose:
Required condition:
System event / observable:
Available telemetry:
Detection idea:
Likely false positives:
Preventive control:
Containment / response:
Evidence to preserve:
Validation method:
```

Prefer behavioral detection over brittle exact strings/tool names when practical.

## Attack-chain interruption
For chain `A -> B -> C -> D`, identify at each stage:
`prerequisite / observable / prevention / detection / containment / evidence`.
A strong defense may only need to reliably break one critical dependency.

## Adversary adaptation
Ask what alternative preserves the attacker's objective if a defense blocks the current technique. Prefer controls that force higher privilege, greater cost, more infrastructure, or noisier/more detectable behavior.

## Defender-advantage research
Study attacker constraints: required access, timing, privilege, infrastructure, protocol limits, tool limitations, operational mistakes, resource cost, environment assumptions, persistence and communication requirements.

## Assumption attacking
For architecture/security decisions, challenge assumptions such as:
- authentication is bypassed;
- API key leaks;
- dependency/plugin becomes malicious;
- trusted internal service is compromised;
- user-controlled text reaches an agent/tool;
- documentation is stale.

Use failures to discover missing trust boundaries and defense-in-depth layers.

## Abuse cases
For dual-use features, compare intended workflow with plausible misuse: who can trigger it, accessible resources, limits, audit trail, abuse controls, and failure mode at scale.

## Security validation loop
For authorized fixes:
`understand behavior -> identify weakness -> implement mitigation -> create safe regression -> verify old behavior blocked -> verify normal behavior -> confirm useful telemetry`.

## Purple-team closure
When the task includes validation/detection engineering, continue through `purple-team-research-and-validation.md`: safe stimulus/emulation -> telemetry observation -> detection -> response/recovery -> gap -> retest. A defense is not "covered" merely because a rule exists, and an emulation is not proof a detector saw it.
