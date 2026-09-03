# Evidence Verification

## Claim ledger
For important conclusions, maintain compact internal claims such as:

```text
C1: feature introduced in v3.2
Evidence: release notes + tag/source
Version: 3.2+
Confidence: Verified
Contradictions: none
```

Do not expose private reasoning logs; expose concise evidence and uncertainty useful to the user.

## Confidence vocabulary
Use:
- **Verified**: direct matching primary/implementation evidence or reproduced behavior.
- **Strongly supported**: multiple strong sources align, though not directly reproduced.
- **Likely**: evidence favors the claim but a material gap remains.
- **Uncertain**: insufficient or indirect evidence.
- **Conflicting evidence**: credible sources disagree and reconciliation is incomplete.
- **Not verified**: plausible claim without adequate evidence.

## Version intelligence
For version-sensitive claims, establish where relevant:
- project/user version;
- current stable/beta/preview/nightly version;
- release date/channel;
- documentation version;
- repository tag/branch;
- breaking/deprecation/migration boundary;
- issue/PR/benchmark version.

Never combine incompatible versions as if they describe one system.

## Contradiction resolution
When credible sources disagree:
1. identify the exact conflict;
2. compare version/branch/environment;
3. compare publication/update date;
4. compare authority;
5. inspect source and tests;
6. inspect maintainer context;
7. reproduce safely if feasible.

If unresolved, label the answer conflicting rather than choosing silently.

## Adversarial verification
After forming a conclusion, actively seek evidence that would make it false: unsupported cases, limitations, known bugs, regressions, platform constraints, removed features, or production failures.

## Independent cold review
For high-impact, multi-source, or contentious conclusions, use an independent reviewer/subagent when the runtime supports one and the extra pass can materially reduce error.

Give the reviewer the claim, scope/version, strongest evidence, and relevant contradictions. When practical, avoid giving the reviewer the preferred conclusion; ask it to falsify, find missing evidence, and classify confidence independently. Reconcile disagreements against primary evidence rather than voting.

An independent reviewer is a quality-control mechanism, not a new source of truth. Do not upgrade confidence merely because two models agree.

## Freshness
For changing claims, consider publish/update date, software version, source branch/tag, and current release channel. Prefer current primary evidence for current questions; preserve old sources for historical reconstruction.

## False-positive and false-negative control
For bugs/security investigations, consider benign alternative explanations such as misconfiguration, stale cache, version mismatch, expected retries, logging artifacts, unrelated races, dependency overrides, or test-environment differences.

Also ask what could hide a real problem: missing logs, wrong branch/version, feature flags, environment-specific behavior, unexercised paths, stale docs, or incomplete tests.

## Reproducibility
When feasible, capture enough context to reproduce:
`version + environment + configuration + trigger + observed behavior + expected behavior + fix version/condition`.

Never claim a reproduction or test that was not performed.

## Validation gate
Before implementation, confirm:
- problem understood;
- relevant version/environment known;
- root cause/mechanism sufficiently supported;
- recommended mechanism verified;
- project constraints known;
- major security/compatibility risk checked.

After implementation:
`inspect diff -> targeted tests -> broader relevant checks -> compare with researched expectation -> regression check`.
Compilation/test success alone does not guarantee semantic correctness.

## Evidence graph for complex claims
When the investigation has multiple versions, implementation paths, tests, patches, or contradictions, use `evidence-graph.md` instead of relying only on a flat claim ledger. Link `claim <-> source <-> version/environment <-> code/commit <-> test/reproduction <-> contradiction` so confidence remains auditable after context compaction or handoff.

A claim should not be marked Verified merely because one strong source exists if material graph edges disagree or the relevant version/environment is unresolved.

## Opened-source and flip-condition rule
For load-bearing claims, distinguish discovery metadata from evidence actually read. A search snippet or AI summary may route the next step but does not count as an opened primary source. For consequential conclusions, record the strongest counterevidence/limitation and what new fact would materially flip or weaken the decision. Use `research-evidence-lifecycle.md` for the full claim/frontier contract.
