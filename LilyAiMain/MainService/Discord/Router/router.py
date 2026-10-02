"""Platform-agnostic DM router. Discord, the HTTP API and the DM Simulator all enter here."""
import re
import time

from LilyAiCore.Logging.logger import get_logger
from LilyAiGameSpace.guide_builder import GuideBuilder, GuidePlan
from LilyAiLearning.MemoryLearning.memory_learning import explicit_memory_request
from LilyAiMain.MainService.Discord.Events.bus import EventBus
from LilyAiMain.MainService.Discord.Middleware.middleware import MAX_INPUT_CHARS, AccessControl, RateLimiter, clean_input
from LilyAiMain.MainService.Discord.Session.manager import SessionManager
from LilyAiMain.MainService.Interaction.Feedback.feedback import ReplyLog, ReplyRecord
from LilyAiMain.MainService.Interaction.Forms.forms import FormManager
from LilyAiMain.MainService.Interaction.Forms.link_trainer import LinkTrainerFlow
from LilyAiMain.MainService.Interaction.Menus.menus import HELP_TEXT, main_menu
from LilyAiMain.MainService.Interaction.messages import IncomingMessage, MenuItem, OutgoingMessage
from LilyAiMain.MainService.Interaction.Onboarding.onboarding import OnboardingFlow
from LilyAiMain.MainService.Interaction.Polls.polls import PollManager
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatRequest, ChatWorkflow
from LilyAiMemory.service import MemoryService

log = get_logger("router")

# NOTE: the example phrases in LilyAiContext/CapabilityContext/capabilities.py (DM_ACTIONS) are what Lily
# tells users to say. Keep them matching these patterns - tests/test_dm_capabilities.py enforces it.
_HELP = re.compile(r"^\s*(help|menu|\?|what can you do\??)\s*$", re.I)
_SHOW_MEMORY = re.compile(r"\b(what do you (?:remember|know) about me|show (?:me )?my memor(?:y|ies)|what have you learned about me)\b", re.I)
_FORGET = re.compile(r"\b(forget (?:everything|all)(?: about me)?|wipe my (?:memory|data)|delete my (?:memory|data))\b", re.I)
_SETUP = re.compile(r"\b(set me up again|redo (?:my )?setup|start onboarding)\b", re.I)
_LINK = re.compile(r"\blink (?:me|my (?:account|trainer(?: id)?))\b|\bconnect my trainer(?: id)?\b", re.I)
_UNLINK = re.compile(r"\bunlink (?:me|my (?:account|trainer(?: id)?))\b", re.I)
# "am I linked?" / "what's my trainer id" / "check my trainer id I linked". Skipped when the message is really a
# stats question ("show my trainer id stats") so that still reaches the chat model and its tools.
_LINK_STATUS = re.compile(
    r"^(?!.*\b(?:stats?|gains?|fans?|rank|quota|leaderboard)\b).*"
    r"\b(?:am i linked|is my (?:account|trainer(?: id)?) linked|"
    r"(?:what(?:'s| is)|check|show|tell me)\s+my\s+(?:linked\s+)?trainer\s*id)\b",
    re.I | re.S,
)
_LINK_STATUS_MAX_WORDS = 15
# "make a guide for Special Week" / "build me a guide on the URA scenario" / "guide for Gold Ship". Questions about
# guides ("is there a guide for ...", "what guides do you have") are left for the chat model.
_GUIDE_REQUEST = re.compile(
    r"^(?!\s*(?:is there|are there|do you have|does|which|what|where|any)\b)"
    r"(?=.*\b(?:(?:make|build|create|write|generate|draft|prepare|compile|give|put together)\b[^.?!\n]{0,40}?\bguide\b"
    r"|guide\s+(?:for|on|about|to)\b))",
    re.I | re.S,
)
_GUIDE_MAX_WORDS = 40
# Answers to "saved copy or generate a new one?" (the quick-reply buttons send exactly these phrases).
_GUIDE_SAVED = re.compile(r"^\s*(?:use\s+(?:the\s+)?)?(?:saved|cached?|old|existing)(?:\s+(?:guide|one|copy|version))?\s*[.!]*\s*$", re.I)
_GUIDE_NEW = re.compile(
    r"^\s*(?:generate\s+(?:a\s+)?)?(?:new|fresh)(?:\s+(?:guide|one|copy|version))?\s*[.!]*\s*$"
    r"|^\s*(?:regenerate|redo|rebuild|generate)(?:\s+(?:it|guide|one|again))?\s*[.!]*\s*$",
    re.I,
)
_YES = {"yes", "y", "yep", "confirm", "do it", "sure"}
_TRUNCATED_NOTICE = f"(Heads up: I only read the first {MAX_INPUT_CHARS} characters of that message - the rest got cut off.)"


def _guide_choice_menu() -> list[MenuItem]:
    return [MenuItem("Use saved guide", "use saved guide"), MenuItem("Generate new guide", "generate new guide")]


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
        link_trainer: LinkTrainerFlow,
        guides: GuideBuilder | None = None,
    ):
        self.memory, self.chat, self.replies, self.bus = memory, chat, replies, bus
        self.sessions, self.limiter, self.access = sessions, limiter, access
        self.forms, self.polls, self.onboarding = forms, polls, onboarding
        self.link_trainer = link_trainer
        # Guides are written with the chat model and saved in the shared guide cache. The docs engine is
        # looked up lazily, so building the router never touches the docs folder.
        self.guides = guides or GuideBuilder(None, chat.provider, chat.settings.chat_model, memory.guide_cache)

    async def route(self, msg: IncomingMessage) -> list[OutgoingMessage]:
        text, truncated = clean_input(msg.text)
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
        if truncated:
            out = [OutgoingMessage(_TRUNCATED_NOTICE, kind="system"), *out]
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
        # "I already built that guide - saved copy or a new one?" is answered once; any other message drops
        # the question and is handled as usual.
        pending_guide: GuidePlan | None = session.data.pop("guide_choice", None)
        if pending_guide is not None:
            if _GUIDE_SAVED.match(text):
                return await self._guide_reply(uid, pending_guide, force=False)
            if _GUIDE_NEW.match(text):
                return await self._guide_reply(uid, pending_guide, force=True)
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
        if _UNLINK.search(text):
            unlinked = self.memory.trainer_link.unlink(uid)
            return sys("You're unlinked." if unlinked else "You weren't linked to a Trainer ID.")
        # The ID is right in the sentence ("my trainer id is 123456789", "link me to 123456789"): link it now
        # instead of asking for it again, and before the bare "link me" pattern which would start the form.
        direct = self.link_trainer.try_direct_link(uid, text)
        if direct:
            return sys(direct)
        if _LINK.search(text):
            return sys(self.link_trainer.start(uid))
        if len(text.split()) <= _LINK_STATUS_MAX_WORDS and _LINK_STATUS.search(text):
            return sys(self.link_trainer.status(uid))
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

        # Guide requests: built from the game docs. If the same guide was built before, ask whether to reuse
        # the saved copy or generate a new one. A request that names nothing the docs know falls through to chat.
        if len(text.split()) <= _GUIDE_MAX_WORDS and _GUIDE_REQUEST.match(text):
            plan = self.guides.plan(text)
            if plan is not None:
                saved = self.guides.lookup(plan)
                if saved is not None:
                    session.data["guide_choice"] = plan
                    return sys(self.guides.ask_text(saved), _guide_choice_menu())
                return await self._guide_reply(uid, plan, force=False)

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

    async def _guide_reply(self, uid: str, plan: GuidePlan, *, force: bool) -> list[OutgoingMessage]:
        """Serve the saved guide or build (and save) a new one. A failure is shown as a plain system message
        and is never saved or added to the chat history."""
        start = time.perf_counter()
        result = await self.guides.build_and_store(plan, force=force)
        if not result.ok:
            return [OutgoingMessage(result.text, kind="system")]
        text = f"{result.note}\n\n{result.text}" if result.note else result.text
        rid = self.replies.add(ReplyRecord(uid, plan.question, result.text, True, []))
        # Keep the chat history short: the guide itself is in the cache, so only note what was written.
        self.memory.conversation.append(uid, "user", plan.question)
        self.memory.conversation.append(
            uid, "assistant", f"(I wrote the guide \"{result.title}\" with these sections: {', '.join(result.sections)}.)"
        )
        meta = {
            "model": result.model, "tools": ["guide_builder"], "domains": [], "tokens": 0,
            "ms": round((time.perf_counter() - start) * 1000), "guide_cached": result.from_cache,
        }
        return [OutgoingMessage(text, reply_id=rid, meta=meta)]
