from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping

from .model import CapabilityRecord, CapabilitySnapshot, CapabilityState


HOST_ONLY_CAPABILITIES = (
    "web_search",
    "web_open",
    "browser_automation",
    "subagents",
    "approval_request",
    "secret_access",
    "mcp",
    "external_skill",
    "image_understanding",
    "image_generation",
)

LOCAL_EXECUTABLE_CAPABILITIES: dict[str, tuple[str, ...]] = {
    "shell": ("bash", "sh"),
    "git": ("git",),
    "repository_search": ("rg", "grep"),
    "package_manager": ("uv", "pip", "pip3", "npm", "pnpm", "yarn", "cargo", "go"),
}

LSP_EXECUTABLES = (
    "pyright-langserver",
    "pylsp",
    "typescript-language-server",
    "rust-analyzer",
    "gopls",
    "clangd",
    "jdtls",
)


def _record(state: CapabilityState, evidence: str, *, provider: str | None = None, **kwargs: Any) -> CapabilityRecord:
    return CapabilityRecord(state=state, provider=provider, evidence=[evidence], **kwargs)


def _first_executable(names: tuple[str, ...]) -> tuple[str, str] | None:
    for name in names:
        path = shutil.which(name)
        if path:
            return name, path
    return None


def _can_write_directory(project: Path) -> tuple[CapabilityState, str]:
    # Capability discovery must observe the environment, not mutate it. In
    # particular, probing a nonexistent project must never create that path.
    if not project.exists():
        return CapabilityState.UNAVAILABLE, "project path does not exist; write probe was not performed"
    if not project.is_dir():
        return CapabilityState.RESTRICTED, "project path is not a directory; write probe was not performed"
    try:
        with tempfile.NamedTemporaryFile(prefix=".skick-probe-", dir=project, delete=True) as handle:
            handle.write(b"probe")
            handle.flush()
        return CapabilityState.AVAILABLE, "write probe succeeded in existing project directory; probe file removed"
    except PermissionError:
        return CapabilityState.PERMISSION_REQUIRED, "write probe denied by filesystem permissions"
    except OSError as exc:
        return CapabilityState.RESTRICTED, f"write probe failed with {exc.__class__.__name__}"


def _git_repository(project: Path) -> CapabilityRecord:
    git = shutil.which("git")
    if not git:
        return _record(CapabilityState.UNKNOWN, "git executable unavailable, repository state not observable")
    proc = subprocess.run(
        [git, "-C", str(project), "rev-parse", "--is-inside-work-tree"],
        text=True,
        capture_output=True,
        check=False,
        timeout=3,
    )
    if proc.returncode == 0 and proc.stdout.strip() == "true":
        return _record(CapabilityState.AVAILABLE, "git rev-parse confirmed project is inside a work tree", provider="git")
    return _record(CapabilityState.UNAVAILABLE, "git rev-parse confirmed project is not a work tree", provider="git")


def _network_probe() -> CapabilityRecord:
    # Opt-in only. Failure to reach one neutral endpoint is a restriction signal, not
    # proof that every form of networking is unavailable.
    try:
        with socket.create_connection(("1.1.1.1", 53), timeout=1.0):
            return _record(CapabilityState.AVAILABLE, "opt-in TCP connectivity probe succeeded")
    except OSError as exc:
        return _record(CapabilityState.RESTRICTED, f"opt-in TCP probe failed with {exc.__class__.__name__}; broader network state remains uncertain")


def _merge_declared(capabilities: dict[str, CapabilityRecord], declared: Mapping[str, Mapping[str, Any]] | None) -> None:
    if not declared:
        return
    for name, raw in declared.items():
        if not isinstance(raw, Mapping):
            continue
        try:
            state = CapabilityState(str(raw.get("state", "unknown")))
        except ValueError:
            state = CapabilityState.UNKNOWN
        current = capabilities.get(name)
        # Trusted host declarations may resolve unknown/host-dependent capabilities,
        # but they may not erase a local observation made by this process.
        if current and current.state not in {CapabilityState.UNKNOWN, CapabilityState.HOST_DEPENDENT}:
            continue
        evidence = raw.get("evidence")
        if isinstance(evidence, list):
            evidence_list = [str(item) for item in evidence]
        else:
            evidence_list = ["trusted host declaration"]
        capabilities[name] = CapabilityRecord(
            state=state,
            provider=str(raw["provider"]) if raw.get("provider") is not None else None,
            version=str(raw["version"]) if raw.get("version") is not None else None,
            trust_level=str(raw["trust_level"]) if raw.get("trust_level") is not None else "host_declared",
            latency_class=str(raw["latency_class"]) if raw.get("latency_class") is not None else None,
            context_cost=str(raw["context_cost"]) if raw.get("context_cost") is not None else None,
            safety_risk=str(raw["safety_risk"]) if raw.get("safety_risk") is not None else None,
            provenance_quality=str(raw["provenance_quality"]) if raw.get("provenance_quality") is not None else None,
            evidence=evidence_list,
        )


def discover_capabilities(
    project: Path,
    *,
    declared: Mapping[str, Mapping[str, Any]] | None = None,
    active_network_probe: bool = False,
    runtime_candidates: dict[str, list[str]] | None = None,
) -> CapabilitySnapshot:
    project = project.resolve()
    capabilities: dict[str, CapabilityRecord] = {}

    if project.exists() and os.access(project, os.R_OK):
        capabilities["filesystem_read"] = _record(CapabilityState.AVAILABLE, "project directory is readable; observed locally", provider="filesystem")
    elif project.exists():
        capabilities["filesystem_read"] = _record(CapabilityState.PERMISSION_REQUIRED, "project exists but read access is denied; observed locally", provider="filesystem")
    else:
        capabilities["filesystem_read"] = _record(CapabilityState.UNAVAILABLE, "project path does not exist; observed locally", provider="filesystem")

    write_state, write_evidence = _can_write_directory(project)
    capabilities["filesystem_write"] = _record(write_state, f"{write_evidence}; observed locally", provider="filesystem")

    for capability, commands in LOCAL_EXECUTABLE_CAPABILITIES.items():
        found = _first_executable(commands)
        if found:
            command, path = found
            capabilities[capability] = _record(CapabilityState.AVAILABLE, f"executable {command} found at {path}; observed locally", provider=command)
        else:
            capabilities[capability] = _record(CapabilityState.UNAVAILABLE, f"none of the local executables were found: {', '.join(commands)}; observed locally")

    capabilities["git_repository"] = _git_repository(project)
    capabilities["code_execution"] = _record(CapabilityState.AVAILABLE, "SKick runtime is executing under Python; observed locally", provider="python")

    lsp = _first_executable(LSP_EXECUTABLES)
    if lsp:
        capabilities["lsp"] = _record(CapabilityState.AVAILABLE, f"language-server executable {lsp[0]} found at {lsp[1]}; observed locally", provider=lsp[0])
    else:
        capabilities["lsp"] = _record(CapabilityState.UNAVAILABLE, "no known language-server executable found in PATH; observed locally")
    capabilities["semantic_code_search"] = CapabilityRecord(
        state=CapabilityState.UNKNOWN,
        evidence=["semantic indexing is host/tool specific and cannot be inferred from generic executable presence"],
    )
    capabilities["test_execution"] = CapabilityRecord(
        state=CapabilityState.AVAILABLE if capabilities["code_execution"].state == CapabilityState.AVAILABLE else CapabilityState.UNKNOWN,
        provider="local_process",
        evidence=["local code execution is available; project-specific test command still requires discovery"],
    )

    for name in HOST_ONLY_CAPABILITIES:
        capabilities.setdefault(name, CapabilityRecord(state=CapabilityState.UNKNOWN, evidence=["not observable from the local SKick runtime without a host declaration"]))

    capabilities["network"] = _network_probe() if active_network_probe else CapabilityRecord(
        state=CapabilityState.UNKNOWN,
        evidence=["active network probing disabled by default; no network availability claim made"],
    )

    container_evidence = None
    if Path("/.dockerenv").exists():
        container_evidence = "Docker/container marker /.dockerenv observed locally"
    elif Path("/run/.containerenv").exists():
        container_evidence = "container marker /run/.containerenv observed locally"
    capabilities["container"] = CapabilityRecord(
        state=CapabilityState.AVAILABLE if container_evidence else CapabilityState.UNKNOWN,
        provider="local_runtime" if container_evidence else None,
        evidence=[container_evidence or "no reliable container marker observed; state left unknown"],
    )

    _merge_declared(capabilities, declared)
    return CapabilitySnapshot(
        project=str(project),
        capabilities=capabilities,
        runtime_candidates=runtime_candidates or {},
        probe_policy={"active_network_probe": bool(active_network_probe), "environment_values_collected": False},
    )


def load_declared_capabilities(path: Path) -> dict[str, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and isinstance(data.get("capabilities"), dict):
        data = data["capabilities"]
    if not isinstance(data, dict):
        raise ValueError("capability declaration must be an object or contain a capabilities object")
    return {str(k): dict(v) for k, v in data.items() if isinstance(v, dict)}
