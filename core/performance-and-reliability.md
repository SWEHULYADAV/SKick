# Performance and Reliability Research

## Purpose
Diagnose latency, throughput, memory, resource, concurrency, outage, and scaling problems with reproducible measurements rather than intuition.

## Baseline first
Record workload, dataset, hardware, OS/runtime, dependency versions, configuration, warm/cold state, concurrency, cache state, network topology, and measurement tool before comparing results.

## Mechanism classes
Consider where relevant:
CPU, memory/GC, disk/I/O, network, serialization, database/query plans, locks/contention, queues/backpressure, connection pools, cache hit/miss, retries/timeouts, rate limits, scheduler/thread/event-loop behavior, GPU/accelerator utilization, startup/JIT, external dependencies.

## Measurement
Prefer profiles/traces/counters and repeated runs. Report distribution/variance (for example median/tail latency) rather than one best run. Separate throughput from latency and average from p95/p99 when tail behavior matters.

## Reliability
Model failure domains, retries, idempotency, timeout budgets, circuit breaking, overload/backpressure, graceful degradation, recovery, persistence/durability, and observability.

## Benchmark integrity
Do not compare benchmarks across incompatible hardware, versions, datasets, configurations, or load shapes without qualification. Prevent benchmark-specific optimization from masquerading as general improvement.

## Regression loop
`baseline -> reproduce -> profile/trace -> hypothesis -> smallest change -> same benchmark -> neighboring workloads -> resource/correctness regression check`.
