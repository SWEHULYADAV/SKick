from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class CapabilityState(StrEnum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"
    RESTRICTED = "restricted"
    PERMISSION_REQUIRED = "permission_required"
    HOST_DEPENDENT = "host_dependent"


@dataclass(slots=True)
class CapabilityRecord:
    state: CapabilityState
    provider: str | None = None
    version: str | None = None
    trust_level: str | None = None
    latency_class: str | None = None
    context_cost: str | None = None
    safety_risk: str | None = None
    provenance_quality: str | None = None
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["state"] = self.state.value
        return data


@dataclass(slots=True)
class CapabilitySnapshot:
    project: str
    capabilities: dict[str, CapabilityRecord]
    runtime_candidates: dict[str, list[str]] = field(default_factory=dict)
    probe_policy: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "project": self.project,
            "probe_policy": self.probe_policy,
            "runtime_candidates": self.runtime_candidates,
            "capabilities": {name: record.to_dict() for name, record in sorted(self.capabilities.items())},
        }


@dataclass(slots=True)
class DepthDecision:
    activate: bool
    mode: str
    depth: str
    score: int
    reasons: list[str]
    explicit_depth: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
