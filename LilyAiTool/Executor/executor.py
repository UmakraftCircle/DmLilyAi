import asyncio
import inspect
import time

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiCore.Helpers.text import truncate
from LilyAiCore.Logging.logger import get_logger
from LilyAiTool.Models.tool_models import ToolContextData, ToolResult
from LilyAiTool.Registry.registry import ToolRegistry
from LilyAiTool.Validator.validator import validate_args

log = get_logger("tool")
MAX_OUTPUT_CHARS = 4000


class ToolExecutor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    async def execute(self, name: str, arguments: dict, ctx: ToolContextData) -> ToolResult:
        start = time.perf_counter()
        try:
            spec = self.registry.get(name)
            args = validate_args(spec.parameters, arguments)
            result = spec.handler(ctx, args)
            if inspect.isawaitable(result):
                result = await asyncio.wait_for(result, timeout=spec.timeout)
            out, ok = str(result), True
        except asyncio.TimeoutError:
            out, ok = "Tool timed out.", False
        except ToolError as e:
            out, ok = f"Tool error: {e}", False
        except Exception as e:  # tools must never crash the chat loop
            log.exception("tool %s crashed", name)
            out, ok = f"Tool crashed: {type(e).__name__}: {e}", False
        return ToolResult(name, ok, truncate(out, MAX_OUTPUT_CHARS), (time.perf_counter() - start) * 1000)
