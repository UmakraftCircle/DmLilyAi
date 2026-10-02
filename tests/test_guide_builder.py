"""Guide builder: subject resolution, per-section grounding, number verification, caching, and the DM flow.

The key rule under test: a failed build (provider error, offline provider, nothing found) is never cached.

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import importlib
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiContext.CapabilityContext.capabilities import DM_ACTIONS  # noqa: E402
from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Exceptions.errors import ProviderError  # noqa: E402
from LilyAiCore.ExternalServices.Database.sqlite import Database  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse  # noqa: E402
from LilyAiGameSpace.guide_builder import GuideBuilder, Passage, numbers_in, verify_section  # noqa: E402
from LilyAiGameSpace.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine  # noqa: E402
from LilyAiMain.MainService.bootstrap import build_app  # noqa: E402
from LilyAiMain.MainService.Interaction.messages import IncomingMessage  # noqa: E402
from LilyAiMemory.GuideCache.guide_cache import GuideCacheStore, is_cacheable  # noqa: E402
from LilyAiMemory.Storage.store import MemoryStore  # noqa: E402

router_mod = importlib.import_module("LilyAiMain.MainService.Discord.Router.router")

SPECIAL_WEEK = """# Special Week

**Japanese name:** スペシャルウィーク (Supesharu Wīku)

## Overview

Special Week is a runner from Hokkaido with a speed growth bonus of 85.

## Aptitudes

Turf A, Dirt G. Growth rate speed 10%.

## Skills

The unique skill gives a velocity boost in the final corner and costs 180 points.

## Sources

| Source | URL |
|---|---|
| GameTora | https://gametora.com/umamusume/characters/special-week |
"""

_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class ScriptedProvider(LLMProvider):
    """Writes a plain supported section, or fails / goes offline / invents a number on demand."""

    def __init__(self, mode="ok"):
        self.mode, self.calls = mode, 0

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        self.calls += 1
        if self.mode == "fail":
            raise ProviderError("boom")
        if self.mode == "offline":
            return LLMResponse("(offline mode - set GROQ_API_KEY for real replies)", model="offline")
        if self.mode == "badnum":
            return LLMResponse("- Growth is 999% [S1]\n- Turf is her best surface [S1] [S9]", model="fake-model")
        return LLMResponse("- Speed growth bonus is 85 [S1]\n- The unique skill costs 180 points [S1]", model="fake-model")

    async def list_models(self):
        return []


class GuideBuilderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "Character").mkdir()
        (self.root / "Character" / "Special_Week.md").write_text(SPECIAL_WEEK, encoding="utf-8")
        self.engine = UmamusumeGameSpaceEngine(self.root, refresh_interval=0)
        self.cache = GuideCacheStore(MemoryStore(Database()))

    def tearDown(self):
        self.tmp.cleanup()

    def builder(self, mode="ok"):
        return GuideBuilder(self.engine, ScriptedProvider(mode), "fake-model", self.cache, retry_delay=0)

    def rows(self):
        return self.cache.db.query("SELECT * FROM guide_cache")

    # ---- plan
    def test_plan_resolves_subject_and_goal_and_same_question_shares_a_key(self):
        gb = self.builder()
        a = gb.plan("make a guide for Special Week")
        b = gb.plan("Build me a guide on special week!")
        c = gb.plan("make a guide for Special Week ura scenario")
        self.assertEqual(a.subject_ids, ["Character/Special_Week"])
        self.assertEqual(a.key, b.key)
        self.assertNotEqual(a.key, c.key)
        self.assertEqual(c.goal, "ura scenario")
        self.assertIsNone(gb.plan("make a guide for banana smoothies"))

    # ---- verification
    def test_numbers_and_verify_section(self):
        self.assertEqual(numbers_in("- Speed +20% costs 1,200 [S3], 2nd place, 3.50"), {"20", "1200", "3.5"})
        passages = [Passage("S1", "d", "T", "Sec", "Speed 85, cost 180. Growth 10%")]
        body, dropped = verify_section("- Speed 85 [S1]\n- Growth 999% [S1]\n- Fine. Bad 77 [S1] [S4]", passages)
        self.assertIn("Speed 85", body)
        self.assertNotIn("999", body)
        self.assertNotIn("77", body)
        self.assertNotIn("[S4]", body)  # a citation the passages don't have
        self.assertEqual(dropped, 2)

    # ---- build + cache
    def test_build_saves_and_second_ask_is_served_from_cache(self):
        gb = self.builder()
        plan = gb.plan("make a guide for Special Week")
        self.assertIsNone(gb.lookup(plan))
        first = run(gb.build_and_store(plan))
        self.assertTrue(first.ok and first.saved and not first.from_cache)
        self.assertIn("## Overview", first.text)
        self.assertIn("gametora.com", first.text)
        self.assertEqual(len(self.rows()), 1)
        calls = gb.provider.calls
        self.assertIn("saved", gb.ask_text(gb.lookup(plan)))
        again = run(gb.build_and_store(plan))
        self.assertTrue(again.from_cache)
        self.assertEqual(again.text, first.text)
        self.assertEqual(gb.provider.calls, calls)  # no model calls for a saved guide
        regen = run(gb.build_and_store(plan, force=True))
        self.assertTrue(regen.ok and not regen.from_cache)
        self.assertGreater(gb.provider.calls, calls)

    def test_saved_guide_is_flagged_stale_when_the_docs_change(self):
        gb = self.builder()
        plan = gb.plan("make a guide for Special Week")
        run(gb.build_and_store(plan))
        self.assertFalse(gb.lookup(plan).stale)
        path = self.root / "Character" / "Special_Week.md"
        path.write_text(SPECIAL_WEEK + "\n## Trivia\n\nLoves carrots.\n", encoding="utf-8")
        self.assertTrue(gb.lookup(plan).stale)

    def test_unsupported_numbers_are_dropped(self):
        gb = self.builder("badnum")
        result = run(gb.build_and_store(gb.plan("make a guide for Special Week")))
        self.assertTrue(result.ok)
        self.assertNotIn("999", result.text)
        self.assertNotIn("[S9]", result.text)
        self.assertGreaterEqual(result.dropped, 1)

    # ---- errors are never cached
    def test_failures_are_never_cached(self):
        for mode in ("fail", "offline"):
            gb = self.builder(mode)
            plan = gb.plan("make a guide for Special Week")
            result = run(gb.build_and_store(plan))
            self.assertFalse(result.ok, mode)
            self.assertFalse(result.saved, mode)
            self.assertEqual(self.rows(), [], mode)
            self.assertIsNone(self.cache.get(plan.key), mode)
            # and the next attempt really tries again instead of replaying the error
            gb.provider.mode = "ok"
            self.assertTrue(run(gb.build_and_store(plan)).ok)
            self.cache.delete(plan.key)

    def test_failed_regeneration_keeps_the_saved_guide(self):
        gb = self.builder()
        plan = gb.plan("make a guide for Special Week")
        good = run(gb.build_and_store(plan))
        gb.provider.mode = "fail"
        bad = run(gb.build_and_store(plan, force=True))
        self.assertFalse(bad.ok)
        self.assertEqual(self.cache.get(plan.key).content, good.text)

    def test_cache_refuses_error_text_and_drops_poisoned_rows(self):
        body = "x" * 300
        self.assertTrue(is_cacheable(body, ok=True, model="m"))
        self.assertFalse(is_cacheable(body, ok=False, model="m"))
        self.assertFalse(is_cacheable(body, ok=True, model="offline"))
        self.assertFalse(is_cacheable("I'm having trouble reaching my language model right now. " + body, ok=True))
        self.assertFalse(is_cacheable("short", ok=True))
        kwargs = dict(title="t", question="q", model="m", source_ids=[], docs_sig="")
        self.assertFalse(self.cache.put("k", content="short error", ok=True, **kwargs))
        self.assertFalse(self.cache.put("k", content=body, ok=False, **kwargs))
        self.assertEqual(self.rows(), [])
        self.cache.db.execute(
            "INSERT INTO guide_cache(cache_key,title,question,content,model,source_ids,docs_sig,created_at) "
            "VALUES ('bad','t','q',?, 'offline','[]','',1)", (body,))
        self.assertIsNone(self.cache.get("bad"))
        self.assertEqual(self.rows(), [])


class GuideRouterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "docs"
        (root / "Character").mkdir(parents=True)
        (root / "Character" / "Special_Week.md").write_text(SPECIAL_WEEK, encoding="utf-8")
        os.environ["LILYAI_DATA_DIR"] = tempfile.mkdtemp()
        os.environ["GROQ_API_KEY"] = ""
        self.provider = ScriptedProvider()
        self.app = build_app(load_settings(), provider=self.provider, search_provider=object())
        self.app.router.guides = GuideBuilder(
            UmamusumeGameSpaceEngine(root, refresh_interval=0), self.provider, "fake-model",
            self.app.memory.guide_cache, retry_delay=0,
        )
        self.app.memory.user.add("g1", "Test user")  # skip onboarding

    def tearDown(self):
        self.tmp.cleanup()

    def say(self, text):
        return run(self.app.router.route(IncomingMessage("g1", text, "Tester", "simulator")))

    def rows(self):
        return self.app.memory.guide_cache.db.query("SELECT * FROM guide_cache")

    def test_patterns(self):
        r = router_mod
        for text in ("make a guide for Special Week", "can you build me a guide on the URA scenario", "Give me a guide for Gold Ship"):
            self.assertTrue(r._GUIDE_REQUEST.match(text), text)
        for text in ("is there a guide for Special Week?", "what guides do you have", "how are you"):
            self.assertFalse(r._GUIDE_REQUEST.match(text), text)
        for text in ("use saved guide", "saved", "cache", "Use the cached one."):
            self.assertTrue(r._GUIDE_SAVED.match(text), text)
        for text in ("generate new guide", "new", "regenerate", "fresh"):
            self.assertTrue(r._GUIDE_NEW.match(text), text)
        self.assertTrue(any("make a guide" in examples for examples, _ in DM_ACTIONS))
        self.assertTrue(r._GUIDE_REQUEST.match("make a guide for Special Week"))

    def test_same_question_asks_then_serves_saved_or_regenerates(self):
        first = self.say("make a guide for Special Week")
        self.assertTrue(first[0].text.startswith("# Special Week Guide"))
        self.assertEqual(len(self.rows()), 1)
        calls = self.provider.calls

        ask = self.say("make me a guide for special week")
        self.assertEqual(self.provider.calls, calls)  # asking costs no model call
        self.assertIn("already built", ask[0].text)
        self.assertEqual([m.text for m in ask[0].menu], ["use saved guide", "generate new guide"])

        saved = self.say("use saved guide")
        self.assertIn("saved guide", saved[0].text)
        self.assertIn("# Special Week Guide", saved[0].text)
        self.assertEqual(self.provider.calls, calls)

        self.say("make a guide for Special Week")
        fresh = self.say("generate new guide")
        self.assertNotIn("saved guide", fresh[0].text)
        self.assertGreater(self.provider.calls, calls)
        self.assertEqual(len(self.rows()), 1)

    def test_failed_guide_is_shown_but_not_cached_or_remembered(self):
        self.provider.mode = "fail"
        out = self.say("make a guide for Special Week")
        self.assertEqual(out[0].kind, "system")
        self.assertIn("Nothing was saved", out[0].text)
        self.assertEqual(self.rows(), [])
        self.assertFalse(any("I wrote the guide" in t.content for t in self.app.memory.conversation.recent("g1", 20)))
        # asking again builds for real instead of replaying the error or asking about a saved copy
        self.provider.mode = "ok"
        again = self.say("make a guide for Special Week")
        self.assertTrue(again[0].text.startswith("# Special Week Guide"))
        self.assertEqual(len(self.rows()), 1)


if __name__ == "__main__":
    unittest.main()
