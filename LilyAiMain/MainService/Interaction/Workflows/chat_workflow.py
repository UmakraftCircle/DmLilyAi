"""The main chat pipeline: gather context from every domain, call the model, run tools, store the turn."""
import asyncio
import re
import time
from dataclasses import dataclass, field

from LilyAiContext.service import ContextBuilder, ContextInput, HistoryMessage
from LilyAiCore.Config.settings import Settings
from LilyAiCore.Constants.constants import MAX_TOOL_ROUNDS
from LilyAiCore.Exceptions.errors import ProviderError
from LilyAiCore.Logging.logger import get_logger
from LilyAiCore.Providers.base import LLMProvider
from LilyAiLearning.service import LearningService, extract_facts, name_from_message
from LilyAiMemory.service import MemoryService
from LilyAiRag.service import RagService
from LilyAiTool.service import ToolContextData, ToolService

log = get_logger("workflow.chat")

_HARD = re.compile(
    r"\b(step[- ]by[- ]step|analy[sz]e|compare|explain why|prove|derive|debug|refactor|architecture|trade-?offs?|"
    r"write (?:a|an|the) (?:function|script|program|essay|report)|code)\b",
    re.I,
)

FALLBACK_ERROR = "I'm having trouble reaching my language model right now. Give me a minute and try again."


@dataclass
class ChatRequest:
    user_id: str
    text: str
    display_name: str = ""


@dataclass
class ChatReply:
    text: str
    ok: bool = True
    model: str = ""
    tools_used: list[str] = field(default_factory=list)
    domains: list[str] = field(default_factory=list)
    used_evidence: bool = False
    token_estimate: int = 0
    elapsed_ms: float = 0.0


class ChatWorkflow:
    def __init__(
        self,
        settings: Settings,
        provider: LLMProvider,
        memory: MemoryService,
        rag: RagService,
        tools: ToolService,
        context: ContextBuilder,
        learning: LearningService,
    ):
        self.settings, self.provider = settings, provider
        self.memory, self.rag, self.tools, self.context, self.learning = memory, rag, tools, context, learning
        self._bg: set[asyncio.Task] = set()

    def pick_model(self, text: str) -> str:
        return self.settings.reasoning_model if len(text) > 500 or _HARD.search(text) else self.settings.chat_model

    async def handle(self, req: ChatRequest) -> ChatReply:
        start = time.perf_counter()
        uid, text = req.user_id, req.text

        rag_hits = self.rag.retrieve(text, k=3)
        history = [HistoryMessage(t.role, t.content) for t in self.memory.conversation.recent(uid, self.settings.history_turns)]
        schemas = self.tools.schemas() if self.settings.web_enabled else [
            s for s in self.tools.schemas() if s["function"]["name"] not in {"web_search", "read_webpage"}
        ]
        built = self.context.build(
            ContextInput(
                user_message=text,
                user_id=uid,
                display_name=req.display_name,
                history=history,
                user_facts=self.memory.relevant_user_facts(uid, text),
                knowledge_snippets=[h.as_snippet() for h in rag_hits],
                tool_schemas=schemas,
            )
        )
        self.learning.context.record(built.token_estimate, built.dropped_history)

        messages = list(built.messages)
        tool_ctx = ToolContextData(uid, req.display_name, {"domains": []})
        model = self.pick_model(text)
        used: list[str] = []
        final = None
        try:
            for round_no in range(MAX_TOOL_ROUNDS + 1):
                final = await self.provider.chat(
                    messages, model=model, tools=schemas if (schemas and round_no < MAX_TOOL_ROUNDS) else None
                )
                if not final.tool_calls:
                    break
                messages.append(final.raw_message)
                for call in final.tool_calls:
                    result = await self.tools.run(call.name, call.arguments, tool_ctx)
                    self.learning.tools.record(call.name, result.ok, result.duration_ms)
                    used.append(call.name)
                    messages.append({"role": "tool", "tool_call_id": call.id, "content": result.output})
        except ProviderError as e:
            log.error("provider failed: %s", e)
            return ChatReply(FALLBACK_ERROR, ok=False, elapsed_ms=(time.perf_counter() - start) * 1000)

        reply_text = (final.content if final else "") or "I couldn't put a good answer together. Could you rephrase that?"
        self.memory.conversation.append(uid, "user", text)
        self.memory.conversation.append(uid, "assistant", reply_text)

        if self.settings.learn_from_chats:
            name_fact = name_from_message(text)
            if name_fact:
                self.memory.user.add(uid, name_fact, source="learned")
            self._spawn(self._learn_facts(uid, text, reply_text))

        domains = list(dict.fromkeys(tool_ctx.extra["domains"]))
        return ChatReply(
            text=reply_text,
            model=final.model if final else model,
            tools_used=used,
            domains=domains,
            used_evidence=bool(rag_hits or domains),
            token_estimate=built.token_estimate,
            elapsed_ms=(time.perf_counter() - start) * 1000,
        )

    async def _learn_facts(self, user_id: str, text: str, reply: str) -> None:
        for fact in await extract_facts(self.provider, text, reply, model=self.settings.chat_model):
            self.memory.user.add(user_id, fact, source="learned")

    def _spawn(self, coro) -> None:
        task = asyncio.create_task(coro)
        self._bg.add(task)
        task.add_done_callback(self._bg.discard)
