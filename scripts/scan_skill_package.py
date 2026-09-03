#!/usr/bin/env python3
"""Static, local, non-executing preflight for agent skill/plugin packages.

Findings are heuristic leads, not a malware/safety verdict. The scanner never
runs package commands, downloads dependencies, follows remote instructions, or
opens network connections.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".py", ".sh", ".bash", ".zsh", ".js", ".ts", ".mjs", ".cjs", ".ps1", ".bat", ".cmd"}
EXEC_SUFFIXES = {".py", ".sh", ".bash", ".zsh", ".js", ".ts", ".mjs", ".cjs", ".ps1", ".bat", ".cmd"}
SKIP_SELF = "scripts/scan_skill_package.py"

PATTERNS = [
    ("pipe-to-shell", re.compile(r"(?:curl|wget)[^\n|]{0,300}\|\s*(?:sh|bash|zsh|powershell|pwsh)\b", re.I), "high"),
    ("shell-true", re.compile(r"subprocess\.(?:run|call|Popen)\([^\n]{0,300}shell\s*=\s*True", re.I), "high"),
    ("dynamic-code-exec", re.compile(r"\b(?:eval|exec)\s*\(", re.I), "warn"),
    ("credential-path", re.compile(r"(?:~?/\.ssh\b|~?/\.aws\b|~?/\.kube\b|~?/\.config/gcloud\b|browser[^\n]{0,50}cookie|\.env\b)", re.I), "warn"),
    ("secret-exfil-language", re.compile(r"(?:upload|send|post|exfiltrat)[^\n]{0,120}(?:token|credential|password|cookie|private key|secret)", re.I), "warn"),
    ("broad-destructive-shell", re.compile(r"\brm\s+-rf\s+(?:/|~|\$HOME|\.\.)", re.I), "high"),
]


def text_read(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"Dockerfile", "Makefile"}:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def add(findings: list[dict], severity: str, code: str, path: str, detail: str) -> None:
    findings.append({"severity": severity, "code": code, "path": path, "detail": detail})


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true", help="return non-zero when high findings exist")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    findings: list[dict] = []

    for path in sorted(root.rglob("*")):
        rel_path = path.relative_to(root)
        rel = rel_path.as_posix()
        if ".git" in rel_path.parts or "__pycache__" in rel_path.parts or rel == SKIP_SELF:
            continue
        if path.is_symlink():
            try:
                target = path.resolve(strict=False)
                target.relative_to(root)
            except ValueError:
                add(findings, "high", "symlink-escape", rel, f"symlink resolves outside package: {target}")
            continue
        if not path.is_file():
            continue

        suffix = path.suffix.lower()
        executable = suffix in EXEC_SUFFIXES or bool(path.stat().st_mode & 0o111)
        text = text_read(path)
        if text is None:
            if executable:
                add(findings, "warn", "opaque-executable", rel, "executable/binary content requires manual provenance review")
            continue

        for code, regex, base_severity in PATTERNS:
            if regex.search(text):
                severity = base_severity if executable else "info"
                add(findings, severity, code, rel, "pattern present; inspect surrounding context and intent")

        if path.name == "package.json":
            try:
                pkg = json.loads(text)
                scripts = pkg.get("scripts", {}) if isinstance(pkg, dict) else {}
                for lifecycle in ["preinstall", "install", "postinstall", "prepare"]:
                    if isinstance(scripts, dict) and lifecycle in scripts:
                        cmd = str(scripts[lifecycle])
                        sev = "high" if re.search(r"(?:curl|wget|powershell|bash|sh\b|node\s+-e|python\s+-c)", cmd, re.I) else "warn"
                        add(findings, sev, "package-lifecycle", rel, f"{lifecycle} script: {cmd[:180]}")
            except json.JSONDecodeError:
                add(findings, "warn", "invalid-package-json", rel, "package.json could not be parsed")

        if path.name.lower() in {"skill.md", "skills.md"} and text.startswith("---"):
            end = text.find("\n---", 3)
            if end > 0:
                keys = []
                for line in text[3:end].splitlines():
                    if ":" in line and not line.startswith((" ", "\t")):
                        keys.append(line.split(":", 1)[0].strip())
                extra = sorted(set(keys) - {"name", "description"})
                if extra:
                    add(findings, "info", "nonportable-frontmatter", rel, f"extra frontmatter fields may be host-specific: {extra}")

    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in ["high", "warn", "info"]}
    result = {"root": str(root), "counts": counts, "findings": findings, "note": "Heuristic static preflight; findings require contextual review."}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"SKILL STATIC SCAN: high={counts['high']} warn={counts['warn']} info={counts['info']}")
        for f in findings:
            print(f"- {f['severity'].upper():4} {f['code']}: {f['path']} — {f['detail']}")
    return 1 if args.strict and counts["high"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
