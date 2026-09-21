import ast
import operator
from datetime import datetime, timedelta, timezone

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiTool.Models.tool_models import ToolSpec

_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.Mod: operator.mod, ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        left, right = _eval(node.left), _eval(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ToolError("exponent too large")
        return _OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    raise ToolError("unsupported expression")


def safe_calculate(expression: str) -> str:
    try:
        value = _eval(ast.parse(expression.strip(), mode="eval"))
    except ZeroDivisionError:
        raise ToolError("division by zero")
    except SyntaxError:
        raise ToolError("invalid expression")
    return str(round(value, 10) if isinstance(value, float) else value)


def _calculate(ctx, args):
    return safe_calculate(args["expression"])


def _current_time(ctx, args):
    offset = args.get("utc_offset_hours", 0)
    if not -12 <= offset <= 14:
        raise ToolError("utc_offset_hours must be between -12 and 14")
    now = datetime.now(timezone.utc) + timedelta(hours=offset)
    sign = "+" if offset >= 0 else "-"
    return now.strftime(f"%A %Y-%m-%d %H:%M:%S (UTC{sign}{abs(offset)})")


def utility_tools() -> list[ToolSpec]:
    return [
        ToolSpec(
            "calculate",
            "Evaluate an arithmetic expression exactly (+ - * / ** % //, parentheses).",
            {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]},
            _calculate,
        ),
        ToolSpec(
            "current_time",
            "Get the current date and time, optionally at a UTC offset in hours.",
            {"type": "object", "properties": {"utc_offset_hours": {"type": "number"}}, "required": []},
            _current_time,
        ),
    ]
