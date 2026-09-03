#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RELEASE = "1.0"
REQUIRED = [
    ".gitignore", ".gitattributes", ".github/workflows/validate.yml", "LICENSE", "SECURITY.md",
    "VERSION", "SKILL.md", "SPEC.md", "START_HERE.md", "AI_HANDOFF.md", "AI_CONTEXT.json", "INSTALLATION_MANIFEST.json", "CONTRIBUTING.md", "agents/openai.yaml", "README.md", "CHANGELOG.md",
    "assets/logo.png", "assets/icon.png", "assets/favicon.png", "assets/favicon-32.png",
    "assets/readme/hero-banner.webp", "assets/readme/capabilities-banner.webp", "assets/readme/usage-guide.webp", "assets/readme/platforms-banner.webp",
    "docs/PLATFORM_CATALOG.md", "docs/AI_INSTALL_PROTOCOL.md", "docs/RELEASE_CHECKLIST.md", "docs/USAGE_PLAYBOOK.md", "docs/INSTALLATION.md", "docs/WEB_AND_APPS.md",
    "docs/VS_CODE_AND_IDES.md", "docs/WARNINGS.md", "docs/TROUBLESHOOTING.md", "docs/UPDATE_AND_PORTING.md", "docs/BRANDING.md",
    "docs/INVOCATION_AND_MODES.md", "docs/RUNTIME_COMPATIBILITY.md", "docs/NEW_RUNTIME_INTEGRATION.md", "docs/RELEASE_AUDIT.md",
    "ARTIFACT_MANIFEST.json", "SHA256SUMS.txt",
    "PORTABILITY.md", "SOURCES.md", "UPSTREAMS.md", "THIRD_PARTY_NOTICES.md",
    "core/semantic-intent-resolution.md", "core/prompt-enhancement.md", "core/capability-and-skill-routing.md", "core/deferred-capability-loading.md",
    "core/language-and-framework-intelligence.md", "core/ui-system-and-render-intelligence.md", "core/research-evidence-lifecycle.md",
    "core/purple-team-research-and-validation.md", "core/skill-supply-chain-and-lifecycle.md", "core/engineering-wayfinding-and-slicing.md",
    "core/engineering-lifecycle.md", "core/engineering-learning-loop.md", "core/experiment-optimization-loop.md", "core/harness-and-runtime-intelligence.md", "core/specialist-skill-orchestration.md", "core/mcp-stack.md", "core/mcp-validation-and-security.md",
    "core/coverage-and-lateral-search.md", "core/mechanism-first-reasoning.md",
    "core/design-and-motion-orchestration.md",
    "core/research-core.md", "core/research-source-router.md", "core/query-mutation.md",
    "core/source-strategy.md", "core/repository-research.md", "core/repository-context-map.md", "core/evidence-verification.md",
    "core/evidence-graph.md", "core/external-skill-intelligence.md",
    "core/domain-and-codebase-design.md", "core/system-design-and-architecture.md", "core/project-planning-and-structure.md", "core/python-vanilla-web-stack.md",
    "core/implementation-discipline.md",
    "core/engineering-feedback-loops.md", "core/verified-review-and-simplification.md", "core/code-integration.md",
    "core/webapp-validation.md", "core/performance-and-reliability.md", "core/formal-verification-and-fuzzing.md",
    "core/decision-analysis.md",
    "core/reverse-engineering-and-undocumented-behavior.md", "core/ml-ai-system-evaluation.md",
    "core/skill-authoring-and-evals.md", "core/evaluation-harness-integration.md", "core/empirical-research-methodology.md",
    "core/biomedical-and-health-research.md", "core/financial-and-economic-research.md",
    "core/legal-policy-and-patent-research.md", "core/structured-data-quality.md", "core/multimodal-evidence.md",
    "core/security-research.md", "core/offensive-defensive.md",
    "core/long-horizon-research.md", "core/execution-ledger.md", "core/resource-budgeting.md",
    "core/multi-agent-orchestration.md", "core/observability-and-tracing.md",
    "core/action-safety-transactions.md", "core/action-firewall.md", "core/untrusted-content-boundary.md",
    "core/agent-protocol-intelligence.md", "core/evidence-lineage.md",
    "core/network-resilience.md", "core/memory-governance.md", "core/research-checkpoint.md",
    "core/research-frontier.md", "core/context-management.md", "core/token-efficiency.md",
    "core/output-protocol.md", "core/output-quality-gate.md",
    "core/runtime-and-capabilities.md", "core/serena-integration.md",
    "extensions/frontend-design.md", "extensions/visual-design-qa.md", "extensions/motion-interaction-design.md", "extensions/web3d-experience-design.md", "extensions/cinematic-scroll.md",
    "schemas/task-state.schema.json", "schemas/trace.schema.json", "schemas/budget.schema.json",
    "schemas/evidence-lock.schema.json", "schemas/artifact-manifest.schema.json", "schemas/mcp-catalog.schema.json", "schemas/integration-catalog.schema.json",
    "integrations/README.md", "integrations/catalog.json", "integrations/superpowers.md", "integrations/claude-design-skillstack.md", "integrations/huggingface.md", "integrations/security-specialists.md",
    "integrations/harnesses-and-evals.md", "integrations/frontend-browser-specialists.md",
    "integrations/cloud-and-data-platforms.md", "integrations/research-providers.md", "integrations/research-specialists.md", "integrations/language-specialists.md", "integrations/ui-and-browser-specialists.md", "integrations/agent-control-patterns.md", "integrations/official-skill-ecosystems.md", "docs/PLANS_AND_SURFACES.md", "docs/DESIGN_REFERENCE_PLAYBOOK.md", "docs/SKILL_ECOSYSTEM_GUIDE.md", "mcp/README.md", "mcp/catalog.json",
    "adapters/generic/PROMPT.md", "adapters/zcode/README.md",
    "evals/evals.json", "evals/trigger-evals.json", "evals/portability-evals.json",
    "scripts/build_distributions.py", "scripts/validate_distributions.py",
    "scripts/run_evals.py", "scripts/compare_evals.py", "scripts/build_provenance.py",
    "scripts/verify_provenance.py", "scripts/audit_freshness.py", "scripts/visual_qa.py",
    "scripts/generate_mcp_config.py", "scripts/validate_mcp_catalog.py", "scripts/scan_skill_package.py", "scripts/install_skick.py", "scripts/detect_runtime.py", "scripts/audit_release.py", "scripts/sync_adapter_install_blocks.py", "scripts/generate_platform_catalog.py", "scripts/build_handoff_bundle.py", "scripts/build_github_bundle.py",
    "tests/research-prompts.md", "tests/package-manifest.txt",
]

UPSTREAM_MARKERS = [
    "AIwithhassan/lets-scroll", "mattpocock/skills", "vipulgupta2048/codex-skills",
    "hardikpandya/stop-slop", "VoltAgent/awesome-agent-skills",
    "multica-ai/andrej-karpathy-skills", "forrestchang/andrej-karpathy-skills",
    "anthropics/skills - webapp-testing", "anthropics/skills - skill-creator",
    "JuliusBrussee/caveman", "mksglu/context-mode",
    "ComposioHQ/awesome-claude-skills", "hashgraph-online/awesome-codex-plugins",
    "OpenAI openai/plugins - plugin-eval", "Agent Plugins v1 specification",
    "XiaomiMiMo/MiMo-Code", "MiMo-Skills",
    "obra/superpowers", "oraios/serena", "upstash/context7",
    "github/github-mcp-server", "microsoft/playwright-mcp",
    "ChromeDevTools/chrome-devtools-mcp", "getsentry/sentry-mcp",
    "docker/mcp-gateway", "modelcontextprotocol/registry",
    "openai/symphony", "huggingface/skills", "huggingface/smolagents",
    "trailofbits/skills", "getsentry/skills", "vercel-labs/agent-browser",
    "SWE-agent/mini-swe-agent", "langchain-ai/open-swe", "langchain-ai/deepagents",
    "pydantic/pydantic-ai", "pydantic/pydantic-ai-harness",
    "UKGovernmentBEIS/inspect_ai", "UKGovernmentBEIS/inspect_evals", "laude-institute/harbor",
    "modelcontextprotocol/inspector", "snyk/agent-scan", "googleapis/mcp-toolbox",
    "aws/agent-toolkit-for-aws", "microsoft/mcp", "exa-labs/exa-mcp-server",
    "tavily-ai/tavily-mcp", "mendableai/firecrawl-mcp-server", "Aider-AI/aider",
    "freshtechbro/claudedesignskills",
    "Piebald-AI/claude-code-system-prompts", "google-gemini/gemini-cli", "QwenLM/qwen-code",
    "karpathy/autoresearch", "MoonshotAI/kimi-cli", "cline/cline", "smart-mcp-proxy/mcpproxy-go", "punkpeye/awesome-mcp-servers",
    "mattpocock/skills", "android/skills", "Kotlin/kotlin-agent-skills", "angular/skills", "dotnet/skills", "microsoft/skills",
    "rewrite-rs/skills", "microsoft/playwright", "luisalima/skills-lock", "mitre/caldera", "SigmaHQ/sigma-specification",
]

SOURCE_MARKERS = [
    "arXiv", "PubMed", "medRxiv", "bioRxiv", "ClinicalTrials.gov", "DailyMed",
    "WHO", "ChEMBL", "PubChem", "DrugBank", "Open Targets", "NPI Registry",
    "NIH RePORTER", "Stock prices", "Crypto", "Forex", "Commodities", "ETFs",
    "mutual funds", "SEC filings", "Insider transactions", "Polymarket", "Kalshi",
    "BLS", "FRED", "USAspending.gov", "World Bank", "IMF", "German labor",
    "UK case law", "UK legislation", "UK Parliament", "UK rail", "Ship tracking",
    "CERN Open Data", "Patents", "GitHub", "CISA KEV", "OSV",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`\n]+)`")
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def load_json(root: Path, rel: str, errors: list[str]):
    try:
        return json.loads((root / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"invalid JSON {rel}: {exc}")
        return None


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for rel in REQUIRED:
        if not (root / rel).is_file():
            fail(errors, f"missing required file: {rel}")

    version = root / "VERSION"
    if version.is_file() and version.read_text(encoding="utf-8").strip() != RELEASE:
        fail(errors, f"VERSION must be {RELEASE}")

    # Canonical skill must contain exactly one uppercase entrypoint.
    skills = sorted(root.rglob("SKILL.md"))
    if skills != [root / "SKILL.md"]:
        fail(errors, "canonical package must contain exactly one SKILL.md at package root")

    skill_path = root / "SKILL.md"
    skill_text = ""
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        m = FRONT_RE.match(skill_text)
        if not m:
            fail(errors, "SKILL.md missing YAML frontmatter")
        else:
            keys: list[str] = []
            values: dict[str, str] = {}
            for line in m.group(1).splitlines():
                if ":" in line and not line.startswith((" ", "\t")):
                    k, v = line.split(":", 1)
                    keys.append(k.strip())
                    values[k.strip()] = v.strip()
            if set(keys) != {"name", "description"} or len(keys) != 2:
                fail(errors, f"SKILL.md frontmatter must contain only name and description; got {keys}")
            name = values.get("name", "")
            desc = values.get("description", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
                fail(errors, f"invalid lowercase hyphenated skill name: {name!r}")
            if not (80 <= len(desc) <= 1024):
                fail(errors, f"description length should be 80..1024 chars, got {len(desc)}")
        if len(skill_text.splitlines()) >= 500:
            fail(errors, "SKILL.md must remain under 500 lines")
        if "v1.0" not in skill_text:
            fail(errors, "SKILL.md must identify release v1.0")
        if any(stage not in skill_text for stage in ["HARNESS", "ORCHESTRATE", "ROUTE", "LATERAL", "COVER", "MECHANISM", "PLAN", "REVIEW", "LEARN", "QUALITY"]):
            fail(errors, "SKILL.md control loop missing v1.0 required stages")

    # Prevent stale release claims in maintained text/config files.
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".txt"}:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if ("2026-" + "08-15") in text:
            fail(errors, f"stale verification date in {p.relative_to(root)}")

    # Validate every relative Markdown link.
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            resolved = (md.parent / path_part).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                fail(errors, f"link escapes package: {md.relative_to(root)} -> {target}")
                continue
            if not resolved.exists():
                fail(errors, f"broken relative link: {md.relative_to(root)} -> {target}")

    # Validate package-relative paths named in inline code while excluding host install paths.
    prefixes = ("core/", "adapters/", "extensions/", "integrations/", "mcp/", "schemas/", "evals/", "tests/", "scripts/", "../")
    root_names = {"PORTABILITY.md", "SOURCES.md", "README.md", "UPSTREAMS.md", "THIRD_PARTY_NOTICES.md", "CHANGELOG.md", "SPEC.md", "VERSION"}
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for token in CODE_RE.findall(text):
            token = token.strip().rstrip(".,;:")
            if " " in token or "\n" in token or "{" in token or "}" in token or "<" in token or ">" in token:
                continue
            if not (token.startswith(prefixes) or token in root_names):
                continue
            candidate = (md.parent / token).resolve() if token.startswith("../") else (root / token).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                fail(errors, f"inline path escapes package: {md.relative_to(root)} -> {token}")
                continue
            if not candidate.exists():
                fail(errors, f"broken inline package path: {md.relative_to(root)} -> {token}")

    # Every canonical core and extension is reachable directly from the entrypoint.
    if skill_text:
        for rel in REQUIRED:
            if (rel.startswith("core/") or rel.startswith("extensions/")) and rel not in skill_text:
                fail(errors, f"module not directly referenced by SKILL.md: {rel}")

    # Thin adapters must not become alternate manuals.
    adapters = root / "adapters"
    if adapters.exists():
        for md in adapters.rglob("*.md"):
            lines = md.read_text(encoding="utf-8").splitlines()
            if len(lines) > 140:
                fail(errors, f"adapter is too large ({len(lines)} lines): {md.relative_to(root)}")

    # Serena remains first-class but optional.
    if skill_text and "prefer Serena automatically" not in skill_text:
        fail(errors, "SKILL.md must explicitly preserve automatic Serena preference")
    serena = root / "core/serena-integration.md"
    if serena.is_file():
        st = serena.read_text(encoding="utf-8")
        for phrase in ["semantic repository exploration", "symbol discovery/search", "references/call relationships", "targeted symbol-level edits"]:
            if phrase not in st:
                fail(errors, f"Serena module missing required preference: {phrase}")

    # Source-family coverage required for v1.0.
    router = root / "core/research-source-router.md"
    if router.is_file():
        rt = router.read_text(encoding="utf-8")
        for marker in SOURCE_MARKERS:
            if marker.lower() not in rt.lower():
                fail(errors, f"research source router missing requested source family: {marker}")

    # Provenance: every material upstream supplied/studied must remain auditable.
    upstreams = root / "UPSTREAMS.md"
    if upstreams.is_file():
        ut = upstreams.read_text(encoding="utf-8")
        for marker in UPSTREAM_MARKERS:
            if marker.lower() not in ut.lower():
                fail(errors, f"UPSTREAMS.md missing provenance marker: {marker}")
        if "do not describe the external repositories as locally cloned" not in ut.lower():
            fail(errors, "UPSTREAMS.md must preserve the build-time clone limitation")

    # Evals: static schema/count/balance checks.
    behavior = load_json(root, "evals/evals.json", errors)
    if isinstance(behavior, dict):
        cases = behavior.get("cases")
        if not isinstance(cases, list) or len(cases) < 40:
            fail(errors, "behavior eval suite must contain at least 40 cases")
    trigger = load_json(root, "evals/trigger-evals.json", errors)
    if isinstance(trigger, dict):
        cases = trigger.get("cases")
        if not isinstance(cases, list) or len(cases) < 20:
            fail(errors, "trigger eval suite must contain at least 20 cases")
        elif cases:
            labels = []
            for c in cases:
                if isinstance(c, dict):
                    for key in ("should_trigger", "trigger", "expected_trigger"):
                        if key in c and isinstance(c[key], bool):
                            labels.append(c[key]); break
            if labels and (all(labels) or not any(labels)):
                fail(errors, "trigger eval suite must include both positive and negative cases")
            if not labels:
                # Allow string labels but still require both classes.
                raw = json.dumps(cases).lower()
                if not ("positive" in raw and "negative" in raw):
                    fail(errors, "trigger eval suite must visibly contain positive and negative classes")
    portability = load_json(root, "evals/portability-evals.json", errors)
    if isinstance(portability, dict):
        checks = portability.get("checks")
        if not isinstance(checks, list) or len(checks) < 9:
            fail(errors, "portability eval suite must contain at least 9 checks")

    # JSON schemas must parse and declare an object schema.
    for rel in ["schemas/task-state.schema.json", "schemas/trace.schema.json", "schemas/budget.schema.json", "schemas/evidence-lock.schema.json", "schemas/artifact-manifest.schema.json", "schemas/mcp-catalog.schema.json", "schemas/integration-catalog.schema.json"]:
        d = load_json(root, rel, errors)
        if isinstance(d, dict) and d.get("type") != "object":
            fail(errors, f"schema must have type=object: {rel}")

    integration_catalog = load_json(root, "integrations/catalog.json", errors)
    if isinstance(integration_catalog, dict):
        if integration_catalog.get("schema_version") != 1 or integration_catalog.get("release") != "v1.0":
            fail(errors, "integration catalog must use schema_version 1 and release v1.0")
        items = integration_catalog.get("integrations")
        required_integrations = {"superpowers", "huggingface-skills", "trailofbits-skills", "sentry-skills", "vercel-agent-skills", "agent-browser", "coderabbit", "codex-security", "mini-swe-agent", "open-swe", "deepagents", "pydantic-ai-harness", "inspect-ai", "harbor", "openai-symphony", "freshtechbro-claude-design-skillstack"}
        ids = {i.get("id") for i in items if isinstance(i, dict)} if isinstance(items, list) else set()
        if not required_integrations.issubset(ids):
            fail(errors, f"integration catalog missing v1.0 specialists: {sorted(required_integrations - ids)}")
        if isinstance(items, list) and len(ids) != len(items):
            fail(errors, "integration catalog contains duplicate/missing ids")

    # Universal engineering + specialist/MCP control-plane coverage.
    if skill_text:
        for phrase in ["engineering control plane", "core/engineering-lifecycle.md", "core/engineering-learning-loop.md", "core/experiment-optimization-loop.md", "core/harness-and-runtime-intelligence.md", "core/specialist-skill-orchestration.md", "core/mcp-stack.md", "core/mcp-validation-and-security.md", "core/design-and-motion-orchestration.md", "core/python-vanilla-web-stack.md", "extensions/motion-interaction-design.md", "extensions/web3d-experience-design.md", "integrations/superpowers.md", "integrations/claude-design-skillstack.md"]:
            if phrase.lower() not in skill_text.lower():
                fail(errors, f"SKILL.md missing v1.0 engineering integration marker: {phrase}")

    # Preferred web-stack profile must be first-class and cross-platform.
    web_profile = root / "core/python-vanilla-web-stack.md"
    if web_profile.is_file():
        wt = web_profile.read_text(encoding="utf-8").lower()
        for phrase in ["python backend", "vanilla javascript", "backend/", "frontend/", "app.py", "cross-platform agent rule"]:
            if phrase not in wt:
                fail(errors, f"python/vanilla web profile missing required marker: {phrase}")
    if skill_text and "core/python-vanilla-web-stack.md" not in skill_text:
        fail(errors, "SKILL.md must directly reference the Python/vanilla web profile")

    mcp_catalog = load_json(root, "mcp/catalog.json", errors)
    if isinstance(mcp_catalog, dict):
        if mcp_catalog.get("schema_version") != 2 or mcp_catalog.get("release") != "v1.0":
            fail(errors, "MCP catalog must use schema_version 2 and release v1.0")
        servers = mcp_catalog.get("servers")
        required_ids = {"serena", "context7", "github", "agent-browser", "playwright", "chrome-devtools", "huggingface", "mcp-toolbox-databases", "aws-agent-toolkit", "azure-mcp", "sentry", "docker-mcp-gateway", "exa", "tavily", "firecrawl"}
        ids = {s.get("id") for s in servers if isinstance(s, dict)} if isinstance(servers, list) else set()
        if not required_ids.issubset(ids):
            fail(errors, f"MCP catalog missing recommended providers: {sorted(required_ids - ids)}")
        if isinstance(servers, list):
            if len(ids) != len(servers):
                fail(errors, "MCP catalog contains duplicate or missing server ids")
            for s in servers:
                if not isinstance(s, dict):
                    fail(errors, "MCP catalog server entry must be an object"); continue
                if not str(s.get("upstream", "")).startswith("https://"):
                    fail(errors, f"MCP catalog upstream must be https for {s.get('id')}")
                if not isinstance(s.get("role"), list) or not s.get("role"):
                    fail(errors, f"MCP catalog role list missing for {s.get('id')}")
                if not isinstance(s.get("priority"), int) or not (0 <= s.get("priority") <= 100):
                    fail(errors, f"MCP catalog priority invalid for {s.get('id')}")
        profiles = mcp_catalog.get("profiles")
        validators = mcp_catalog.get("validators")
        if not isinstance(profiles, list) or not {"core-code", "browser-fast", "browser-e2e", "browser-diagnostics", "ai-ml", "database", "cloud-aws", "cloud-azure", "research-web", "engineering"}.issubset({p.get("id") for p in profiles if isinstance(p, dict)}):
            fail(errors, "MCP catalog missing v1.0 profiles")
        if not isinstance(validators, list) or not {"mcp-inspector", "snyk-agent-scan", "skick-static-scan"}.issubset({v.get("id") for v in validators if isinstance(v, dict)}):
            fail(errors, "MCP catalog missing qualification validators")
        raw = json.dumps(mcp_catalog).lower()
        for forbidden in ["ghp_", "sk-proj-", "sk_live_", "sk_test_", "bearer your", "actual_token"]:
            if forbidden in raw:
                fail(errors, f"MCP catalog appears to contain a credential-like value: {forbidden}")

    install_manifest = load_json(root, "INSTALLATION_MANIFEST.json", errors)
    if isinstance(install_manifest, dict):
        if install_manifest.get("schema_version") != "1.0":
            fail(errors, "INSTALLATION_MANIFEST.json must use schema_version 1.0")
        pkg = install_manifest.get("package")
        if not isinstance(pkg, dict) or pkg.get("name") != "skick" or pkg.get("version") != RELEASE:
            fail(errors, "INSTALLATION_MANIFEST.json package identity/version mismatch")
        platforms = install_manifest.get("platforms")
        if not isinstance(platforms, dict) or not platforms:
            fail(errors, "INSTALLATION_MANIFEST.json must contain platform entries")
        else:
            referenced_adapters = {
                entry.get("adapter") for entry in platforms.values() if isinstance(entry, dict) and isinstance(entry.get("adapter"), str)
            }
            unreferenced = []
            for adapter_dir in (root / "adapters").iterdir():
                if not adapter_dir.is_dir() or adapter_dir.name == "generic":
                    continue
                readme = (adapter_dir / "README.md").relative_to(root).as_posix()
                if readme not in referenced_adapters:
                    unreferenced.append(readme)
            if unreferenced:
                fail(errors, f"adapter docs not referenced by installation manifest: {sorted(unreferenced)}")
            for pid, entry in platforms.items():
                if not isinstance(entry, dict):
                    fail(errors, f"installation manifest entry must be object: {pid}"); continue
                adapter = entry.get("adapter")
                if not isinstance(adapter, str) or not (root / adapter).is_file():
                    fail(errors, f"installation manifest adapter missing for {pid}: {adapter}")

    ai_context = load_json(root, "AI_CONTEXT.json", errors)
    if isinstance(ai_context, dict):
        if ai_context.get("schema_version") != "1.0":
            fail(errors, "AI_CONTEXT.json must use schema_version 1.0")
        identity = ai_context.get("identity")
        if not isinstance(identity, dict) or identity.get("name") != "SKick" or identity.get("release") != "v1.0":
            fail(errors, "AI_CONTEXT.json identity mismatch")

    # Python scripts must parse/compile before packaging.
    for rel in ["scripts/validate_package.py", "scripts/build_distributions.py", "scripts/validate_distributions.py", "scripts/run_evals.py", "scripts/compare_evals.py", "scripts/build_provenance.py", "scripts/verify_provenance.py", "scripts/audit_freshness.py", "scripts/visual_qa.py", "scripts/generate_mcp_config.py", "scripts/validate_mcp_catalog.py", "scripts/scan_skill_package.py", "scripts/install_skick.py", "scripts/detect_runtime.py", "scripts/audit_release.py", "scripts/sync_adapter_install_blocks.py", "scripts/generate_platform_catalog.py", "scripts/build_handoff_bundle.py", "scripts/build_github_bundle.py"]:
        p = root / rel
        if p.is_file():
            try:
                compile(p.read_text(encoding="utf-8"), str(p), "exec")
            except Exception as exc:
                fail(errors, f"python compile failed for {rel}: {exc}")

    # Manifest should list all canonical package files except itself and ephemeral bytecode.
    manifest = root / "tests/package-manifest.txt"
    if manifest.is_file():
        listed = {line.strip() for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()}
        actual = {
            p.relative_to(root).as_posix()
            for p in root.rglob("*")
            if p.is_file()
            and ".git" not in p.relative_to(root).parts
            and "__pycache__" not in p.relative_to(root).parts
            and p.relative_to(root).as_posix() != "tests/package-manifest.txt"
        }
        if listed != actual:
            missing = sorted(actual - listed)
            extra = sorted(listed - actual)
            if missing: fail(errors, f"package manifest missing files: {missing[:12]}")
            if extra: fail(errors, f"package manifest lists absent files: {extra[:12]}")

    if errors:
        print("PACKAGE VALIDATION: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print("PACKAGE VALIDATION: PASS")
    print(f"Root: {root}")
    print(f"Release: v{RELEASE}")
    print(f"Markdown files: {sum(1 for _ in root.rglob('*.md'))}")
    print(f"Core modules: {sum(1 for _ in (root / 'core').glob('*.md'))}")
    print(f"Adapters: {sum(1 for _ in (root / 'adapters').rglob('README.md'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
