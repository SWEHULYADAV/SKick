# Purple-Team Research and Validation

## Purpose
Join adversary research, defensive telemetry, detection engineering, response, recovery and safe validation into one evidence-driven loop for authorized security work.

Use for red/blue/purple teaming, detection engineering, adversary emulation design, vulnerability validation, threat hunting, attack-path review, incident learning and AI/agent security. Pair with `security-research.md`, `offensive-defensive.md`, and governing safety/policy.

## Boundary first
Before consequential execution establish:
- target/environment and authorization;
- production vs lab/sandbox/synthetic environment;
- allowed technique classes and excluded assets/data;
- safety/availability constraints;
- cleanup/rollback and evidence-preservation needs;
- stop conditions and incident-escalation path.

Research and modeling can proceed broadly; real-world intrusive actions remain scoped by authorization and policy.

## Framework roles
Use frameworks for the job they actually model:
- **CWE**: software weakness classes/root causes;
- **CAPEC**: application attack patterns and threat-model vocabulary;
- **ATT&CK**: observed adversary behaviors/techniques and emulation/hunting vocabulary;
- **D3FEND**: defensive countermeasure/relationship vocabulary, not proof a control is effective;
- **Sigma**: portable detection-as-code for log/SIEM behavior;
- **YARA/Suricata/other engines**: content/network-specific detection when appropriate.

Framework IDs organize reasoning; they do not prove reachability, exploitability, coverage or control efficacy.

## Purple loop

`THREAT HYPOTHESIS -> PREREQUISITES -> SAFE STIMULUS/EMULATION -> OBSERVE -> DETECT -> RESPOND -> RECOVER -> GAP ANALYSIS -> IMPROVE -> RETEST`

For each behavior track distinct coverage states:
- hypothesized from intelligence;
- reachable in the target;
- emulated/executed in scope;
- telemetry observed;
- detection fired;
- triage/response succeeded;
- containment/recovery succeeded;
- regression guard retained.

Do not collapse these into a single "covered" checkbox.

## Red-team research lens
Model objective, prerequisites, access, trust boundary, primitive/weakness, technique chain, alternate paths, likely failure points and observable artifacts. Prefer behavior-based emulation over copying a threat actor's exact malware/tooling when a safer stimulus can test the same defensive hypothesis.

For authorized emulation, use the smallest reversible stimulus that answers the question. Unknown public exploit/malware code remains untrusted and is not auto-executed.

## Blue-team lens
Inventory the telemetry required to see the behavior:
- endpoint/process/file/module;
- identity/authentication/authorization;
- application/API/audit logs;
- cloud/IAM/control-plane;
- network/DNS/proxy;
- email/browser/SaaS;
- database/data-access;
- container/Kubernetes/CI/CD;
- agent/MCP/tool/memory traces when AI systems are involved.

For each detection specify data source, predicate/behavior, expected benign lookalikes, false-positive strategy, severity/triage context, response action and validation artifact.

## Detection engineering loop
Use:
`threat intelligence -> detection opportunity -> required telemetry -> synthetic/authorized event -> rule/query -> test corpus -> false-positive review -> deploy/approve -> observe -> tune -> retest`.

Treat detection rules like code: version, review, test, stage, deploy, monitor and roll back. New SigmaHQ-style rules begin as experimental rather than being assumed production-ready.

## Vulnerability and variant research
After confirming a real root cause:
1. calibrate an exact match to the known instance;
2. identify the invariant bug mechanism;
3. generalize one dimension at a time across identifiers/types/call sites/framework usage;
4. inspect every new match and update false-positive understanding;
5. use Semgrep/CodeQL/AST/grep/semantic search according to the pattern;
6. fix/test the root cause and likely variants, not only the original line.

Context building precedes vulnerability verdicts on unfamiliar code.

## Vulnerability prioritization
Do not rank remediation from CVSS alone. Combine as relevant:
- asset exposure/criticality and reachability;
- CISA KEV or equivalent evidence of known exploitation;
- EPSS/current exploitation probability;
- severity/impact and privileges/prerequisites;
- compensating controls/detection;
- patch availability and operational risk;
- business/safety impact.

Document why a lower-CVSS issue can outrank a higher-CVSS issue when exploitation and asset context justify it.

## DFIR / malware evidence integrity
For investigations:
- preserve original evidence read-only where possible;
- hash and record acquisition/source metadata;
- normalize timestamps/time zones explicitly (prefer UTC in analysis artifacts);
- separate raw evidence, extracted/derived artifacts, notes and final reports;
- retain tool/version/command/result metadata when reproducibility matters;
- validate that a tool actually produced the expected non-empty artifact before drawing conclusions.

Static analysis comes before dynamic execution of suspicious code unless isolation and the investigation require otherwise.

## AI and agentic red teaming
Include the full system, not only the model:
- prompt/context/retrieval injection;
- tool/MCP capability abuse and confused-deputy paths;
- identity, authorization and approval drift;
- memory poisoning/persistence;
- data exfiltration and secret exposure;
- plugin/Skill supply chain;
- model misuse/jailbreak classes;
- insecure code generation and execution sandboxes;
- agent-to-agent trust and delegated authority;
- monitoring, rollback and human-control failures.

Evaluate model, application, tools, data, infrastructure and runtime behavior as separate surfaces, then test cross-surface chains.

## Specialist routing
Strong optional references include Trail of Bits audit/variant/fuzzing skills, MITRE/Apache CALDERA for authorized adversary emulation, Sigma tooling for portable detections, and purpose-built DFIR/reverse-engineering skills. Invoke or reference them only after availability/provenance/license/security checks; SKick retains scope and evidence gates.
