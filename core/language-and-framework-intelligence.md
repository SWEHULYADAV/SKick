# Language and Framework Intelligence

## Purpose
Route coding work through the language, framework, toolchain, and version semantics that actually determine correctness instead of applying generic style advice to every stack.

Use this module for non-trivial implementation, migration, review, performance, build, packaging, concurrency, API-design, security, and cross-language porting work.

## Value gate
Do not load or create a language Skill merely to restate syntax the base model already knows. Prefer a language/framework specialist when at least one is true:
- the surface changes quickly or the installed version matters materially;
- models commonly miss the workflow or failure mode;
- compiler/runtime semantics materially affect correctness;
- build/package/release tooling is specialized;
- platform APIs or deprecations changed recently;
- a domain-specific profiler, trace, analyzer, migration tool, or security model is needed;
- the project has strong local conventions that override generic advice.

A Skill should buy measurable correctness, freshness, efficiency, or safety. Otherwise prefer the native model plus project source/tests.

## Stack fingerprint
Before loading specialist guidance, establish the smallest useful fingerprint:

```text
Languages and file mix:
Runtime / compiler / SDK:
Frameworks and exact installed versions:
Package/build system:
Formatter/linter/static analysis:
Type checker / compiler strictness:
Test/benchmark/fuzz tooling:
Profiler/trace tooling:
Deployment target / ABI / architecture:
Generated code / FFI / native boundaries:
Project conventions and compatibility floor:
```

Derive this from manifests, lockfiles, build files, CI, toolchain files, source imports and actual installed commands before trusting remembered defaults.

## Capability profile
Map the active stack to available capabilities rather than hard-coding one tool:
- `LANGUAGE_SERVER` / semantic index;
- `COMPILER` / type checker;
- `FORMATTER` / linter;
- `STATIC_ANALYSIS` / security analyzer;
- `TEST_RUNNER` / property / mutation / fuzz runner;
- `BENCHMARK` / profiler / trace analyzer;
- `PACKAGE_MANAGER` / build system;
- `API_DOCS` / current official documentation;
- `MIGRATION_TOOL` / codemod / compatibility analyzer;
- `RUNTIME_DIAGNOSTICS` / logs / heap / CPU / trace artifacts.

Use the strongest observed repository-semantic capability for definitions/references, then combine it with language-native compiler/LSP/analyzer evidence. No provider replaces the other proof surfaces.

## Language-specific reasoning lenses
Load only the lenses that match the project.

### Python
Check interpreter/version constraints, packaging/`pyproject`, dependency locks, typing mode, sync/async boundaries, exception contracts, data-model semantics, pytest/property/mutation coverage, and distribution artifacts. Treat environment/import resolution as part of correctness.

### JavaScript / TypeScript
Resolve Node/browser/runtime target, ESM/CJS/bundler mode, `tsconfig` inheritance/strictness, package manager/lockfile, generated types, server/client boundaries, async cancellation/error behavior, and framework rendering/runtime semantics. Distinguish type-level safety from runtime validation.

### Go
Prefer idiomatic ownership through values/interfaces rather than class-pattern transplantation. Check error wrapping/identity, goroutine lifecycle, context cancellation, channel ownership, races, table-driven/property tests, interfaces at consumer boundaries, module/toolchain version, and profile-before-optimize behavior.

### Rust
Treat ownership/lifetimes, `Send`/`Sync`, unsafe boundaries, panic/error contracts, feature flags, MSRV, async cancellation, pinning, FFI/ABI, Clippy/Miri/sanitizers/fuzzing and benchmark evidence as first-class. Do not solve ownership problems by reflexive cloning.

### Java / Kotlin / JVM
Resolve JDK/JVM target, Gradle/Maven/plugin versions, nullability/annotations, reflection/proxy/codegen, classpath/module boundaries, coroutine/reactive semantics, serialization, framework lifecycle, JVM diagnostics and migration constraints. For Kotlin, distinguish Kotlin-native conventions from Java-shaped code.

### C / C++
Treat undefined behavior, lifetime/ownership, integer and memory safety, ABI/toolchain differences, build flags, sanitizer coverage, concurrency/data races, FFI/native boundaries and compiler diagnostics as proof surfaces. Compilation alone is weak evidence.

### C# / .NET
Resolve target framework/SDK, nullable/analyzer settings, async/cancellation, DI/lifetime, source generators, trimming/AOT, MSBuild/package behavior, diagnostics/traces and framework-version-specific APIs.

### Swift / Apple platforms
Resolve Swift language mode and SDK/platform versions, actor isolation/sendability, structured concurrency/cancellation, value/reference ownership, UI framework lifecycle, package/build settings, availability annotations, instruments/traces and platform-specific API deprecations.

### PHP / Laravel and similar convention-heavy frameworks
Resolve runtime/framework versions, package locks, container/config/cache behavior, request/job/queue lifecycle, ORM/query behavior, authorization/validation conventions, migrations and framework-supported testing patterns before generic PHP advice.

### SQL / data languages
Resolve engine/version/dialect, schema/index/cardinality, transaction/isolation semantics, query plan evidence, migration/rollback strategy and production safety. Syntax portability does not imply semantic or performance portability.

## Framework freshness rule
For fast-moving ecosystems, prefer:
`installed version -> project source/config -> current official docs -> official/maintained specialist Skill -> community reference`.

Do not copy a current example into an older project without checking the version boundary. When a Skill documents a moving API, record the version/date it was validated against and re-check after dependency upgrades.

## Cross-language porting contract
For ports/migrations, choose the intended end state first:
- full replacement;
- permanent interoperability/binding;
- temporary scaffold during migration.

Then define a parity contract:
`observable behavior + data formats + error semantics + concurrency/timing + performance envelope + compatibility constraints`.

Use differential tests against the old implementation where feasible. Generalize only after behavioral parity is demonstrated; a clean compile or matching API shape is not proof of equivalence.

## Specialist routing
Prefer official/project-maintained specialists for version-sensitive areas (for example Android/Kotlin, Angular, .NET, framework SDKs) and strong audited community specialists for narrow language craft/security gaps. Load only task-matched Skills; do not install a whole language catalog because one file uses the language.

Record external language specialists in `integrations/language-specialists.md` and qualify them through `external-skill-intelligence.md` plus `skill-supply-chain-and-lifecycle.md`.

## Validation contract
Before reporting success, use the strongest available language-native evidence:
`format/lint -> compile/typecheck -> unit/integration/property/fuzz -> runtime/trace/profile -> compatibility/package artifact`.

Run only the layers relevant to the task, but state what was not run when it matters.
