# Reverse Engineering and Undocumented Behavior

## Purpose
Investigate black-box, undocumented, legacy, or partially specified systems by combining safe observation, differential testing, artifacts, source/history when available, and protocol/file-format evidence.

## Start non-destructively
Prefer:
- documentation/version/archive discovery;
- metadata/manifests/strings/configuration;
- input/output observation;
- network/protocol traces when authorized and available;
- differential behavior across versions/configs;
- static code/binary analysis where lawful and relevant;
- generated fixtures and minimal probes.

## Differential method
Change one variable at a time and compare observable outputs/state. Use known-good/bad versions, feature flags, environments, or implementations to isolate hidden rules.

## Hypothesis discipline
Document what is observed separately from inferred internal implementation. An externally consistent model is not proof of exact internals.

## History
Archived docs, old binaries/tags, changelogs, package metadata, symbols, error strings, patents/skick, and removed tests can reveal behavior no longer documented.

## Safety
Do not execute unknown binaries/scripts casually. For suspicious code use the security/malware analysis workflow and isolated environments as appropriate.

## Deliverable
Prefer a reproducible behavioral specification: inputs, outputs, state transitions, version boundaries, confidence, and tests that distinguish the inferred rules.
