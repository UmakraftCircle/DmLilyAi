from LilyAiContext.ContextFormatter.formatter import format_block
from LilyAiContext.ContextWindow.window import trim_history
from LilyAiContext.MessageContext.message_context import history_to_messages
from LilyAiContext.ContextBuilder.models import BuiltContext, ContextInput
from LilyAiContext.SystemContext.system_context import build_system_prompt
from LilyAiContext.ToolContext.tool_context import format_tool_hint
from LilyAiContext.UserContext.user_context import format_user_context
from LilyAiCore.Helpers.text import estimate_tokens


class ContextBuilder:
    def __init__(self, token_budget: int = 6000):
        self.token_budget = token_budget

    def build(self, ci: ContextInput) -> BuiltContext:
        sections = {
            "user": format_user_context(ci.user_facts),
            "knowledge": format_block("Knowledge", ci.knowledge_snippets),
            "web": format_block("Web results", ci.web_snippets),
            "notes": "\n".join(ci.notes),
            "tools": format_tool_hint(ci.tool_schemas),
        }
        system = "\n\n".join([build_system_prompt(ci.display_name)] + [s for s in sections.values() if s])
        fixed = estimate_tokens(system) + estimate_tokens(ci.user_message) + 16
        history, dropped = trim_history(history_to_messages(ci.history), max(0, self.token_budget - fixed))

        messages = [{"role": "system", "content": system}, *history, {"role": "user", "content": ci.user_message}]
        total = sum(estimate_tokens(m["content"]) + 4 for m in messages)
        return BuiltContext(
            messages=messages,
            tools=ci.tool_schemas,
            token_estimate=total,
            dropped_history=dropped,
            sections={k: estimate_tokens(v) for k, v in sections.items() if v},
        )
