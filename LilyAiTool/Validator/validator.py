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
    "null": type(None),
}


def _type_names(spec: dict[str, Any]) -> list[str]:
    """spec["type"] is normally a single JSON-schema type name, but an optional
    field may declare a union like ["integer", "null"] - some models (seen with
    Groq's openai/gpt-oss-* models calling check_fan_gain's circle_id) pass null
    explicitly for an omitted optional argument instead of leaving it out, and
    without "null" in the schema's type list, Groq's own API-side validation
    rejects the tool call before it ever reaches this function. Always returns a
    list so callers don't need to branch on str vs list."""
    raw = spec.get("type", "")
    return raw if isinstance(raw, list) else [raw]


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
        names = _type_names(spec)
        if value is None:
            if "null" not in names:
                raise ToolValidationError(f"'{key}' must be {spec.get('type')}")
            clean[key] = value
            continue
        expected = tuple(_TYPES[n] for n in names if n in _TYPES) or (object,)
        if ("integer" in names or "number" in names) and isinstance(value, bool):
            raise ToolValidationError(f"'{key}' must be {spec.get('type')}")
        if not isinstance(value, expected):
            raise ToolValidationError(f"'{key}' must be {spec.get('type')}")
        if "enum" in spec and value not in spec["enum"]:
            raise ToolValidationError(f"'{key}' must be one of {spec['enum']}")
        clean[key] = value
    return clean
