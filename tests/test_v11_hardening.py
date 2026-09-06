import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from runtime.capabilities import discover_capabilities
from runtime.claims import ClaimFirewallError, add_claim, set_claim_status
from runtime.prompt_intelligence import interpret_task
from runtime.state import add_evidence, new_run_state, validate_state


class PromptConstraintHardeningTests(unittest.TestCase):
    def test_positive_and_negative_user_constraints_are_locked(self):
        task = interpret_task(
            "Use Python. Only modify this file. Do not add dependencies. Do not browse."
        )
        text = "\n".join(task.constraints).lower()
        self.assertIn("use python", text)
        self.assertIn("only modify this file", text)
        self.assertIn("do not add dependencies", text)
        self.assertIn("do not browse", text)


class ClaimRelevanceHardeningTests(unittest.TestCase):
    def setUp(self):
        self.state = new_run_state("fix auth")
        self.claim_id = add_claim(
            self.state,
            "The authentication regression is fixed",
            status="implemented",
            claim_type="code_change",
        )

    def test_unrelated_passing_test_cannot_verify_claim(self):
        evidence = add_evidence(
            self.state,
            "test_result",
            "README formatting tests passed",
            status="passed",
        )
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, self.claim_id, "verified", evidence_ids=[evidence])

    def test_claim_bound_passing_test_can_verify_code_change(self):
        evidence = add_evidence(
            self.state,
            "test_result",
            "authentication callback regression test",
            status="passed",
            metadata={"supports_claim_ids": [self.claim_id]},
        )
        set_claim_status(self.state, self.claim_id, "verified", evidence_ids=[evidence])
        self.assertEqual(self.state["claims"][0]["status"], "verified")

    def test_current_fact_requires_explicit_freshness(self):
        current = add_claim(
            self.state,
            "Platform X supports Skills today",
            status="implemented",
            claim_type="current_fact",
        )
        docs = add_evidence(
            self.state,
            "first_party_documentation",
            "Platform X Skills documentation",
            status="verified",
            metadata={"supports_claim_ids": [current]},
        )
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, current, "verified", evidence_ids=[docs])
        fresh = add_evidence(
            self.state,
            "first_party_documentation",
            "Platform X current Skills documentation",
            status="verified",
            metadata={"supports_claim_ids": [current], "freshness": "current"},
        )
        set_claim_status(self.state, current, "verified", evidence_ids=[fresh])

    def test_platform_live_verified_requires_live_platform_test(self):
        claim = add_claim(
            self.state,
            "SKick works on Platform X",
            status="implemented",
            claim_type="platform_compatibility",
        )
        generic_runtime = add_evidence(
            self.state,
            "runtime_observation",
            "local Python runtime executed",
            status="passed",
            metadata={"supports_claim_ids": [claim]},
        )
        with self.assertRaises(ClaimFirewallError):
            set_claim_status(self.state, claim, "live_verified", evidence_ids=[generic_runtime])
        live = add_evidence(
            self.state,
            "live_platform_test",
            "Platform X installed, discovered, invoked, and completed smoke task",
            status="passed",
            metadata={"supports_claim_ids": [claim]},
        )
        set_claim_status(self.state, claim, "live_verified", evidence_ids=[live])


class CapabilityProbeHardeningTests(unittest.TestCase):
    def test_nonexistent_project_probe_does_not_create_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "does-not-exist"
            self.assertFalse(project.exists())
            snapshot = discover_capabilities(project)
            self.assertFalse(project.exists())
            self.assertEqual(snapshot.capabilities["filesystem_write"].state.value, "unavailable")


class SchemaEnforcementHardeningTests(unittest.TestCase):
    def test_runtime_state_schema_rejects_unknown_top_level_property(self):
        state = new_run_state("test")
        state["private_chain_of_thought"] = "must never be persisted"
        errors = validate_state(state)
        self.assertTrue(any("private_chain_of_thought" in item for item in errors), errors)

    def test_runtime_state_schema_validates_nested_task_interpretation(self):
        state = new_run_state("test", task_interpretation={"constraints": "not-an-array"})
        errors = validate_state(state)
        self.assertTrue(any("task_interpretation" in item and "constraints" in item for item in errors), errors)


class EvalOracleHardeningTests(unittest.TestCase):
    def test_candidate_runner_does_not_receive_scoring_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            suite = d / "suite.json"
            suite.write_text(json.dumps({"cases": [{
                "id": "oracle",
                "prompt": "Answer safely",
                "expected_answer": "SECRET_ORACLE",
                "checks": [{"type": "contains", "field": "response", "value": "SAFE"}],
            }]}), encoding="utf-8")
            runner = d / "runner.py"
            runner.write_text(
                "import json,sys\np=json.load(sys.stdin)\n"
                "case=p['case']\n"
                "print(json.dumps({'response':'SAFE','received_case':case}))\n",
                encoding="utf-8",
            )
            output = d / "out.json"
            proc = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "run_evals.py"), str(suite),
                "--output", str(output), "--runner", sys.executable, str(runner),
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(output.read_text(encoding="utf-8"))
            received = data["results"][0]["candidate_result"]["received_case"]
            self.assertNotIn("checks", received)
            self.assertNotIn("expected_answer", received)


class InstallerPathHardeningTests(unittest.TestCase):
    def test_manifest_project_path_cannot_escape_project_through_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            project = d / "project"
            outside = d / "outside"
            project.mkdir(); outside.mkdir()
            try:
                (project / ".opencode").symlink_to(outside, target_is_directory=True)
            except OSError as exc:
                if os.name == "nt" and getattr(exc, "winerror", None) == 1314:
                    self.skipTest("Windows symlink privilege unavailable; enable Developer Mode or run elevated")
                raise
            proc = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "install_skick.py"),
                "--source", str(ROOT), "--target", "opencode", "--scope", "project",
                "--project", str(project), "--path-index", "0",
            ], text=True, capture_output=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("escape", (proc.stderr + proc.stdout).lower())
            self.assertFalse((outside / "skills" / "skick").exists())


class VersionIdentityHardeningTests(unittest.TestCase):
    def test_runtime_state_and_runtime_package_derive_version_from_version_file(self):
        import runtime
        package_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(runtime.__version__, package_version + ".0" if package_version.count(".") == 1 else package_version)
        self.assertEqual(new_run_state("test")["skick_version"], package_version)



class WeakPromptSecondPassTests(unittest.TestCase):
    def test_make_secure_routes_to_security_without_inventing_target(self):
        task = interpret_task("make secure")
        self.assertIn("security", task.domains)
        self.assertTrue(task.unknowns)
        self.assertTrue(any("security" in item.lower() or "risk" in item.lower() for item in task.success_criteria))

    def test_check_this_project_is_project_scoped_not_generic(self):
        task = interpret_task("check this project")
        self.assertIn("software_engineering", task.domains)
        self.assertTrue(any("project" in item.lower() or "repository" in item.lower() for item in task.success_criteria))

    def test_why_broken_generates_failure_verification(self):
        task = interpret_task("why broken")
        self.assertIn("software_engineering", task.domains)
        self.assertTrue(task.verification_needs)
        self.assertTrue(any("root cause" in item.lower() or "failure" in item.lower() for item in task.success_criteria))

    def test_find_everything_is_research_but_still_bounded(self):
        task = interpret_task("find everything about this")
        self.assertIn("research", task.domains)
        self.assertTrue(task.research_needs)
        self.assertTrue(task.non_goals)


class GracefulDegradationSecondPassTests(unittest.TestCase):
    def test_missing_major_capabilities_keeps_truth_guards_and_fallbacks_without_fake_availability(self):
        from runtime.model import CapabilitySnapshot, CapabilityRecord, CapabilityState
        from runtime.depth import classify_task
        from runtime.modules import compile_modules
        names = [
            "filesystem_read", "filesystem_write", "shell", "git", "git_repository",
            "repository_search", "semantic_code_search", "web_search", "web_open",
            "browser_automation", "lsp", "mcp", "external_skill", "subagents",
            "network", "code_execution", "test_execution",
        ]
        hard_missing = {"filesystem_read", "filesystem_write", "shell", "git", "git_repository", "repository_search", "lsp", "code_execution", "test_execution"}
        caps = CapabilitySnapshot(
            project="simulated",
            capabilities={
                name: CapabilityRecord(
                    state=CapabilityState.UNAVAILABLE if name in hard_missing else CapabilityState.UNKNOWN,
                    evidence=["simulated missing capability"],
                )
                for name in names
            },
        )
        task = "Deeply research and review this repository security design with the capabilities currently available."
        plan = compile_modules(task, ROOT, caps, decision=classify_task(task), budget_tokens=10000)
        selected = {item.path for item in plan.selected}
        self.assertIn("core/evidence-verification.md", selected)
        self.assertIn("core/untrusted-content-boundary.md", selected)
        self.assertNotIn("core/serena-integration.md", selected)
        self.assertTrue(any("fallback" in note.lower() for note in plan.routing_notes))
        self.assertEqual(plan.required_capabilities, [])


class PromptWeakExamplesSecondPassTests(unittest.TestCase):
    def test_listed_weak_prompts_gain_bounded_execution_goals(self):
        from runtime.prompt_intelligence import interpret_task
        cases = {
            "fix this": "software_engineering",
            "research this": "research",
            "make better": "general",
            "compare these": "research",
        }
        for raw, domain in cases.items():
            with self.subTest(raw=raw):
                task = interpret_task(raw)
                self.assertIn(domain, task.domains)
                self.assertNotEqual(task.interpreted_goal.lower(), raw.lower())
                self.assertLessEqual(len(task.success_criteria), 3)
                self.assertLessEqual(len(task.research_needs), 2)
                self.assertLessEqual(len(task.assumptions), 1)
                self.assertFalse(any("python" in item.lower() or "serena" in item.lower() for item in task.assumptions))


class DepthSecondPassTests(unittest.TestCase):
    def test_broad_high_risk_current_production_security_work_can_reach_exhaustive(self):
        from runtime.depth import classify_task
        decision = classify_task(
            "Research the current production vulnerability across this distributed monorepo, prove exploitability, patch it, and validate regression tests."
        )
        self.assertEqual(decision.depth, "exhaustive")
        self.assertTrue(decision.activate)


class InstallDoctorSecondPassTests(unittest.TestCase):
    def test_doctor_reports_duplicate_malformed_and_version_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            first = project / ".opencode" / "skills" / "skick"
            second = project / ".agents" / "skills" / "skick"
            for path in (first, second):
                path.mkdir(parents=True)
                (path / "SKILL.md").write_text("not valid skill frontmatter\n", encoding="utf-8")
                (path / "VERSION").write_text("0.9\n", encoding="utf-8")
            proc = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "skick_doctor.py"),
                "--project", str(project), "--target", "opencode", "--json",
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
        self.assertGreaterEqual(len(data.get("existing_installs", [])), 2)
        problems = "\n".join(data.get("problems", [])).lower()
        self.assertIn("duplicate", problems)
        self.assertIn("frontmatter", problems)
        self.assertIn("version", problems)


class EvalComparisonHardeningTests(unittest.TestCase):
    def test_legacy_candidate_self_report_is_not_scored_by_compare(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            legacy = {
                "summary": {"pass_rate": None},
                "results": [{"case_id": "a", "run_index": 0, "result": {"passed": True}}],
            }
            base = d / "base.json"; cand = d / "cand.json"
            base.write_text(json.dumps(legacy), encoding="utf-8")
            cand.write_text(json.dumps(legacy), encoding="utf-8")
            proc = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "compare_evals.py"), str(base), str(cand)
            ], text=True, capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            data = json.loads(proc.stdout)
        self.assertEqual(data["paired"]["pairs"], 0)
        self.assertIsNone(data["metrics"]["pass_rate"]["baseline"])
        self.assertEqual(data["tasks"], {})


class ResearchContradictionSecondPassTests(unittest.TestCase):
    def test_high_confidence_fact_with_unresolved_contradiction_is_rejected(self):
        from runtime.state import add_evidence, new_run_state
        from runtime.research_ledger import ResearchLedgerError, add_research_finding

        state = new_run_state("research compatibility")
        ev = add_evidence(state, "first_party_documentation", "Official docs claim support", status="passed", source="https://example.test/docs")
        with self.assertRaises(ResearchLedgerError):
            add_research_finding(
                state,
                "Does platform support native Skills?",
                "Platform supports native Skills",
                kind="fact",
                evidence_ids=[ev],
                confidence="high",
                contradictions=["Current release notes say the feature was removed"],
            )

class PlatformEvidenceSecondPassTests(unittest.TestCase):
    def test_current_first_party_activation_and_paths_are_not_overclaimed(self):
        import json
        manifest = json.loads((ROOT / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
        platforms = manifest["platforms"]
        self.assertEqual(platforms["cursor"]["activation"]["literal_at_skick"], "no")
        self.assertEqual(platforms["cursor"]["activation"]["native_equivalent"], "/skick")
        self.assertEqual(platforms["kiro-cli"]["activation"]["explicit"], "supported")
        self.assertEqual(platforms["kiro-cli"]["activation"]["literal_at_skick"], "no")
        self.assertEqual(platforms["kiro-cli"]["activation"]["native_equivalent"], "/skick")
        self.assertEqual(platforms["kiro-cli"]["activation"]["automatic"], "supported")
        self.assertIn(".agents/skills/skick/", platforms["trae"]["project_paths"])
        self.assertNotIn(".trae/skills/skick/", platforms["trae"]["project_paths"])
        self.assertEqual(platforms["chatgpt"]["activation"]["literal_at_skick"], "yes")

class ReleaseIdentitySecondPassTests(unittest.TestCase):
    def test_v11_identity_is_consistent_across_canonical_metadata(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, "1.1")
        release = "v" + version
        manifest = json.loads((ROOT / "INSTALLATION_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["package"]["version"], version)
        self.assertEqual(manifest["package"]["release"], release)
        self.assertEqual(json.loads((ROOT / "AI_CONTEXT.json").read_text())["identity"]["release"], release)
        for rel in ("integrations/catalog.json", "mcp/catalog.json", "evals/evals.json", "evals/trigger-evals.json", "evals/portability-evals.json"):
            self.assertEqual(json.loads((ROOT / rel).read_text())["release"], release, rel)
        self.assertIn("SKick v1.1", (ROOT / "SKILL.md").read_text(encoding="utf-8"))
        self.assertNotIn("vNext runtime development", (ROOT / "SKILL.md").read_text(encoding="utf-8"))

    def test_active_policy_sources_do_not_reintroduce_serena_first_or_starter_stack_bias(self):
        active = [ROOT / "SKILL.md", ROOT / "AI_CONTEXT.json", ROOT / "adapters" / "generic" / "PROMPT.md"] + list((ROOT / "core").glob("*.md"))
        offenders = []
        starter_bias = []
        for path in active:
            text = path.read_text(encoding="utf-8").lower()
            if "use serena first" in text or "check serena first" in text:
                offenders.append(str(path.relative_to(ROOT)))
            if path.name != "python-vanilla-web-stack.md" and (
                "prefer python backend" in text or "prefer the host-neutral `python backend" in text
            ):
                starter_bias.append(str(path.relative_to(ROOT)))
        self.assertEqual(offenders, [])
        self.assertEqual(starter_bias, [])
        context = (ROOT / "AI_CONTEXT.json").read_text(encoding="utf-8").lower()
        self.assertNotIn("prefer tiny root app.py", context)
        self.assertNotIn("configure canonical serena", context)


class PackageHygieneSecondPassTests(unittest.TestCase):
    def test_maintained_package_text_has_no_local_machine_paths_and_validator_enforces_it(self):
        offenders = []
        ignored = {"docs/superpowers/specs/2026-09-05-vnext-runtime-upgrade-design.md", "docs/superpowers/plans/2026-09-05-vnext-runtime-upgrade.md", "scripts/validate_package.py", "tests/test_v11_hardening.py"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            if path.relative_to(ROOT).as_posix() in ignored:
                continue
            if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".txt"}:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if "/mnt/data" in text or "/home/oai" in text:
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])
        validator = (ROOT / "scripts" / "validate_package.py").read_text(encoding="utf-8")
        self.assertIn("LOCAL_PATH_MARKERS", validator)


class BootstrapCapabilityNeutralityTests(unittest.TestCase):
    def test_generic_bootstrap_does_not_require_serena_as_a_special_provider(self):
        generic = [ROOT / "BOOTSTRAP_PROMPTS.md", ROOT / "docs" / "GITHUB_BOOTSTRAP.md"]
        forbidden = ("serena status", "serena availability", "use/attempt serena", "configure canonical serena")
        offenders = []
        for path in generic:
            text = path.read_text(encoding="utf-8").lower()
            if any(item in text for item in forbidden):
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])
        portability = json.loads((ROOT / "evals" / "portability-evals.json").read_text(encoding="utf-8"))
        github_case = next(item for item in portability["checks"] if item["id"] == "github-bootstrap-protocol")
        self.assertNotIn("Serena", github_case["expect"])


class FinalAuditArtifactTests(unittest.TestCase):
    def test_final_v11_audit_is_required_and_records_proof_boundaries(self):
        audit = ROOT / "docs" / "V1_1_FINAL_AUDIT.md"
        self.assertTrue(audit.is_file())
        text = audit.read_text(encoding="utf-8")
        for marker in (
            "Architecture and dependency map",
            "Specification vs implementation",
            "Schema enforcement map",
            "Black / blind release review",
            "READY WITH DOCUMENTED LIMITATIONS",
            "NOT_MEASURED",
            "LIVE_TESTED = 0",
        ):
            self.assertIn(marker, text)
        validator = (ROOT / "scripts" / "validate_package.py").read_text(encoding="utf-8")
        self.assertIn('"docs/V1_1_FINAL_AUDIT.md"', validator)

if __name__ == "__main__":
    unittest.main()
