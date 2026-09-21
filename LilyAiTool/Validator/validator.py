"""Minimal JSON-schema-ish argument validation (required, type, enum). Enough for tool calls."""
from typing import Any

from LilyAiCore.Exceptions.errors import ToolValidationError

_TYPES = {
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "array": list,
    "object": dict,
}


def validate_args(schema: dict[str, Any], args: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(args, dict):
        raise ToolValidationError("arguments must be an object")
    props = schema.get("properties", {})
    for req in schema.get("required", []):
        if req not in args:
            raise ToolValidationError(f"missing required argument '{req}'")
    clean: dict[str, Any] = {}
    for key, value in args.items():
        spec = props.get(key)
        if spec is None:
            continue  # ignore unknown args silently; models sometimes add extras
        expected = _TYPES.get(spec.get("type", ""), object)
        if spec.get("type") in {"integer", "number"} and isinstance(value, bool):
            raise ToolValidationError(f"'{key}' must be {spec['type']}")
        if not isinstance(value, expected):
            raise ToolValidationError(f"'{key}' must be {spec.get('type')}")
        if "enum" in spec and value not in spec["enum"]:
            raise ToolValidationError(f"'{key}' must be one of {spec['enum']}")
        clean[key] = value
    return clean
