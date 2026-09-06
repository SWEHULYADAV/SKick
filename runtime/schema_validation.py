from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

SCHEMA_ROOT = Path(__file__).resolve().parents[1] / "schemas"


@lru_cache(maxsize=64)
def _load_schema(name: str) -> dict[str, Any]:
    path = (SCHEMA_ROOT / name).resolve()
    try:
        path.relative_to(SCHEMA_ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"schema reference escapes schema root: {name}") from exc
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"schema must be a JSON object: {name}")
    return data


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def _validate(instance: Any, schema: dict[str, Any], path: str, errors: list[str]) -> None:
    ref = schema.get("$ref")
    if isinstance(ref, str):
        if "://" in ref or ref.startswith("#"):
            errors.append(f"{path}: unsupported schema reference {ref}")
            return
        _validate(instance, _load_schema(ref), path, errors)
        return

    expected_type = schema.get("type")
    if expected_type is not None:
        types = [expected_type] if isinstance(expected_type, str) else list(expected_type)
        if not any(_matches_type(instance, str(item)) for item in types):
            errors.append(f"{path}: expected type {types}, got {type(instance).__name__}")
            return

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum")

    if isinstance(instance, str):
        min_length = schema.get("minLength")
        if isinstance(min_length, int) and len(instance) < min_length:
            errors.append(f"{path}: string shorter than minLength {min_length}")
        pattern = schema.get("pattern")
        if isinstance(pattern, str) and re.search(pattern, instance) is None:
            errors.append(f"{path}: string does not match pattern {pattern!r}")

    if isinstance(instance, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(instance):
                _validate(item, item_schema, f"{path}[{index}]", errors)

    if isinstance(instance, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            for key in required:
                if key not in instance:
                    errors.append(f"{path}: missing required property {key}")
        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            properties = {}
        for key, sub_schema in properties.items():
            if key in instance and isinstance(sub_schema, dict):
                _validate(instance[key], sub_schema, f"{path}.{key}", errors)
        extras = [key for key in instance if key not in properties]
        additional = schema.get("additionalProperties", True)
        if additional is False:
            for key in extras:
                errors.append(f"{path}.{key}: additional property is not allowed")
        elif isinstance(additional, dict):
            for key in extras:
                _validate(instance[key], additional, f"{path}.{key}", errors)


def validate_schema_instance(instance: Any, schema_name: str) -> list[str]:
    errors: list[str] = []
    _validate(instance, _load_schema(schema_name), "$", errors)
    return errors
