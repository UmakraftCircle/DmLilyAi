"""Platform-agnostic DM router. Discord, the HTTP API and the DM Simulator all enter here."""
import re

from LilyAiCore.Logging.logger import get_logger
from LilyAiLearning.MemoryLearning.memory_learning import explicit_memory_request
from LilyAiMain.MainService.Discord.Events.bus import EventBus
from LilyAiMain.MainService.Discord.Middleware.middleware import AccessControl, RateLimiter, clean_input
from LilyAiMain.MainService.Discord.Session.manager import SessionManager
from LilyAiMain.MainService.Interaction.Feedback.feedback import ReplyLog, ReplyRecord
from LilyAiMain.MainService.Interaction.Forms.forms import FormManager
from LilyAiMain.MainService.Interaction.Menus.menus import HELP_TEXT, main_menu
from LilyAiMain.MainService.Interaction.messages import IncomingMessage, OutgoingMessage
from LilyAiMain.MainService.Interaction.Onboarding.onboarding import OnboardingFlow
from LilyAiMain.MainService.Interaction.Polls.polls import PollManager
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatRequest, ChatWorkflow
from LilyAiMemory.service import MemoryService

log = get_logger("router")

_HELP = re.compile(r"^\s*(help|menu|\?|what can you do\??)\s*$", re.I)
_SHOW_MEMORY = re.compile(r"\b(what do you (?:remember|know) about me|show (?:me )?my memor(?:y|ies)|what have you learned about me)\b", re.I)
_FORGET = re.compile(r"\b(forget (?:everything|all)(?: about me)?|wipe my (?:memory|data)|delete my (?:memory|data))\b", re.I)
_SETUP = re.compile(r"\b(set me up again|redo (?:my )?setup|start onboarding)\b", re.I)
_YES = {"yes", "y", "yep", "confirm", "do it", "sure"}


class DMRouter:
    def __init__(
        self,
        memory: MemoryService,
        chat: ChatWorkflow,
        replies: ReplyLog,
        bus: EventBus,
        sessions: SessionManager,
        limiter: RateLimiter,
        access: AccessControl,
        forms: FormManager,
        polls: PollManager,
        onboarding: OnboardingFlow,
    ):
        self.memory, self.chat, self.replies, self.bus = memory, chat, replies, bus
        self.sessions, self.limiter, self.access = sessions, limiter, access
        self.forms, self.polls, self.onboarding = forms, polls, onboarding

    async def route(self, msg: IncomingMessage) -> list[OutgoingMessage]:
        text = clean_input(msg.text)
        if not text:
            return []
        uid = msg.user_id
        self.bus.publish("dm_in", msg.source, uid, msg.display_name, text)

        if not self.access.permits(uid, msg.source):
            return self._out(msg, [OutgoingMessage("Sorry, I'm not available for you yet.", kind="system")])
        wait = self.limiter.check(uid)
        if wait:
            return self._out(msg, [OutgoingMessage(f"Give me about {int(wait) + 1}s to catch up, then try again.", kind="system")])

        async with self.sessions.lock(uid):
            out = await self._dispatch(msg, text)
        return self._out(msg, out)

    def _out(self, msg: IncomingMessage, out: list[OutgoingMessage]) -> list[OutgoingMessage]:
        for o in out:
            self.bus.publish("dm_out", msg.source, msg.user_id, "Lily", o.text, msg_kind=o.kind, **o.meta)
        return out

    async def _dispatch(self, msg: IncomingMessage, text: str) -> list[OutgoingMessage]:
        uid = msg.user_id
        session, _ = self.memory.session.touch(uid)
        sys = lambda t, menu=None: [OutgoingMessage(t, kind="system", menu=menu or [])]  # noqa: E731

        # 1. Pending confirmation / form / poll
        if session.data.get("confirm") == "forget":
            session.data.pop("confirm")
            if text.lower().strip(" .!") in _YES:
                self.memory.forget_user(uid)
                self.forms.cancel(uid)
                self.polls.cancel(uid)
                return sys("Done. I've wiped everything I knew about you.")
            return sys("Okay, I've kept everything.")
        if self.forms.active(uid):
            reply, _ = self.forms.submit(uid, text)
            return sys(reply)
        if self.polls.active(uid):
            reply, _ = self.polls.answer(uid, text)
            return sys(reply)

        # 2. First contact
        if self.onboarding.needs_onboarding(uid) and not _HELP.match(text):
            return sys(self.onboarding.start(uid))

        # 3. Natural-language intents (no slash commands)
        if _HELP.match(text):
            return sys(HELP_TEXT, main_menu())
        if _SETUP.search(text):
            return sys(self.onboarding.start(uid))
        if _SHOW_MEMORY.search(text):
            facts = self.memory.user.list(uid)
            if not facts:
                return sys("I don't have anything saved about you yet. Tell me something with \"remember that ...\".")
            return sys("Here's what I remember:\n" + "\n".join(f"- {f.fact}" for f in facts))
        if _FORGET.search(text):
            session.data["confirm"] = "forget"
            return sys("This will erase your saved facts and our chat history. Reply \"yes\" to confirm.")
        fact = explicit_memory_request(text)
        if fact:
            added = self.memory.user.add(uid, fact, source="user")
            return sys(f"Got it, I'll remember that: {fact}" if added else "I already had that one.")

        # 4. Chat
        reply = await self.chat.handle(ChatRequest(uid, text, msg.display_name))
        if not reply.ok:
            return sys(reply.text)
        rid = self.replies.add(ReplyRecord(uid, text, reply.text, reply.used_evidence, reply.domains))
        meta = {
            "model": reply.model, "tools": reply.tools_used, "domains": reply.domains,
            "tokens": reply.token_estimate, "ms": round(reply.elapsed_ms),
        }
        return [OutgoingMessage(reply.text, reply_id=rid, meta=meta)]
