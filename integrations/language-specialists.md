# Language and Framework Specialists

## Policy
Use official/project-maintained language/framework Skills first for fast-moving or under-modeled surfaces. Strong community Skills are discovery/reference candidates, not automatic dependencies. Always resolve the project version and load only the narrow Skills needed for the task.

## High-value official sources

### Android Skills (`android/skills`)
Apache-2.0, maintained from Android guidance. High-value because the project deliberately targets verifiable model knowledge gaps and fast-moving workflows such as AGP migrations, Navigation, adaptive UI, Intent security, Perfetto SQL/trace analysis, R8, testing strategy and policy compliance. Prefer as an optional specialist for Android projects.

### Kotlin Agent Skills (`Kotlin/kotlin-agent-skills`)
Apache-2.0. Use for Kotlin/JVM-specific backend/tooling and current Kotlin migration/toolchain patterns when matched. Do not infer that every Java pattern is idiomatic Kotlin.

### Angular Agent Skills (`angular/skills`)
Official Angular Skills for current architecture/reactivity/signals, SSR, accessibility, forms, routing, testing and new-app setup. Useful because framework APIs evolve faster than model training.

### .NET Skills (`dotnet/skills`)
Use as an engineering/evaluation reference for .NET-specific diagnostics, build/MSBuild, data and language/runtime workflows. Especially valuable: LSP/tool integration and paired no-skill vs exact-skill value experiments.

### Microsoft Skills (`microsoft/skills`)
Large language-segmented Azure/Foundry catalog across Python, .NET, TypeScript, Java and Rust. Useful routing pattern: detect domain + language and load only exact relevant Skills; verify current SDK docs and installed package versions first.

## Strong community/reference sources

### rewrite-rs/skills
BSD-3-Clause. Strong Rust craft/porting reference: ownership instead of reflexive cloning, unsafe/Miri, error/API design, performance/profile-first, and cross-language parity/differential migration. Absorb vendor-neutral mechanisms; do not make Rust-specific opinions global.

### Go specialist catalogs
Use current Go guidance (Effective Go, official docs, well-maintained style guides) plus audited Skills for idioms, context cancellation, error semantics, table/property testing and race/concurrency review.

### Python specialist catalogs
Prefer PyPA/Python official docs for packaging/runtime semantics. Community Skills may help coordinate Ruff/type checkers/pytest/Hypothesis/mutation/release workflows; qualify them before use.

### Swift/iOS specialist catalogs
Fast-moving SDK/language surfaces benefit from version-pinned Skills and themed bundles. Verify Xcode/Swift/SDK version and platform availability before accepting examples.

### Laravel/framework specialists
Prefer official framework Skills/docs where available. Convention-heavy frameworks should be routed by installed version rather than generic language style.

## Routing rule
`project fingerprint -> knowledge-gap/value gate -> official specialist if matched -> strong community specialist if it adds material value -> native model/project evidence fallback`.

One language does not imply one universal Skill. Build, packaging, diagnostics, UI, security and migration may need different specialists.
