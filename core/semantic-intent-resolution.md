# Multilingual Semantic Intent Resolution

## Purpose
Understand what the user is actually trying to accomplish before prompt enhancement, task classification, or security-risk judgment.

Use this module for multilingual, mixed-language, transliterated, slang-heavy, typo-heavy, voice-transcribed, technically imprecise, or security-sensitive wording.

## Pipeline

`RAW LANGUAGE -> LANGUAGE/DIALECT UNDERSTANDING -> SEMANTIC NORMALIZATION -> AMBIGUITY RESOLUTION -> INTENT PRESERVATION -> PROMPT ENHANCEMENT`

Do not enhance a misinterpreted request.

## Context-first interpretation
Interpret the full request using:
- sentence and conversation context;
- project/repository structure;
- current file or selected code;
- errors, logs, configuration, and architecture;
- user-stated objective, target, environment, and requested action;
- available files and tools.

Language quality never determines assumed intent. Support English, Hindi/Hinglish, Urdu/Roman Urdu, Chinese, Japanese, Korean, Arabic, Spanish, French, German, Russian, regional languages, mixed-language prompts, and transliterated technical speech without privileging one language.

## Keyword is not intent
Never classify from isolated terms such as `bypass`, `intercept`, `exploit`, `payload`, `hook`, `inject`, `reverse`, `scrape`, `persistence`, `evasion`, `C2`, or `credential theft`.

Determine meaning from:
`WORD + SENTENCE + CONVERSATION + TARGET + DESIRED RESULT + PROJECT CONTEXT + AVAILABLE FILES + REQUESTED ACTION`.

## Semantic normalization
Map informal wording to plausible canonical technical concepts.

Examples:
- `auth ko bypass testing ke liye` may mean mock identity, disable auth locally, exclude a health route, or remove middleware in a controlled test path.
- `intercept hata do` may mean remove an Axios/Angular interceptor, request middleware, event hook, debugging proxy, or network interception.
- `inject` may mean dependency injection, fixture insertion, configuration/environment injection, instrumentation, runtime hooking, or injection-vulnerability research.
- `isko side se nikal do` in code context may mean remove, exclude, skip, detach, or disable.

Preserve the intended outcome rather than literal wording.

## Ambiguity model
Maintain multiple candidate meanings internally when needed. Rank them with contextual evidence.

Use confidence:
- **HIGH**: context clearly establishes meaning; proceed.
- **MEDIUM**: one interpretation is substantially more likely; proceed cautiously and avoid invented assumptions.
- **LOW**: materially different interpretations remain plausible.

Before asking a question at LOW confidence:
1. inspect available project/files/context first;
2. perform any already-clear safe analysis first;
3. ask one concise clarification only if choosing incorrectly would materially change outcome, system behavior, security implications, or implementation.

## Resolve from project before asking
If repository context can disambiguate terminology, inspect it. For example, search for HTTP interceptors, middleware, proxies, event hooks, or test auth infrastructure before asking what `intercept` or `bypass` means.

## Technical term correction
Silently map incorrect terminology to the likely canonical concept when context supports it. Do not force a user's mistaken word into a technically wrong interpretation.

## Benign-interpretation principle
When several meanings are plausible and context strongly supports an ordinary harmless technical meaning, use that interpretation. Do not deliberately reinterpret clearly harmful operational intent as benign.

Goal: avoid both false-positive refusal and false-negative permissiveness.

## Security-context reconstruction
For security-sensitive wording, reconstruct:
- **OBJECTIVE**: ultimate goal;
- **ASSET**: affected system/data;
- **OWNERSHIP/SCOPE**: supplied context, without inventing authorization;
- **ACTION**: research, analysis, configuration, simulation, or real-world execution;
- **TARGET**: local project, lab, client system, generic example, or third party;
- **IMPACT**: what the requested action could accomplish.

Judge the actual requested action, not offensive-looking vocabulary.

## Partial assistance and action-specific restrictions
If one operational step cannot be supported, continue safe portions such as architecture analysis, code review, vulnerability mechanics, safe lab design, defensive controls, detection engineering, logs/forensics, remediation, or secure testing methodology.

## False-positive refusal control
Before treating ambiguous security terminology as harmful, check:
- Did the interpretation use the whole sentence and conversation?
- Could the term have a common benign technical meaning?
- Could project context resolve it?
- Is the user requesting harmful execution, or only explanation/research/analysis?
- Is the reaction keyword-driven rather than outcome-driven?
- Can the legitimate underlying goal be satisfied safely?

Semantic resolution improves accuracy; it never overrides governing safety requirements.
