"""End-to-end smoke tests with a scripted provider (no network, no API keys).

Run:  python -m unittest discover -s tests -v
"""
import asyncio
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

from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse, ToolCallRequest  # noqa: E402
from LilyAiMain.MainService.bootstrap import App, build_app  # noqa: E402
from LilyAiMain.MainService.Interaction.messages import IncomingMessage  # noqa: E402


class ScriptedProvider(LLMProvider):
    """Calls `calculate` once for math questions, otherwise answers plainly."""

    def __init__(self):
        self.calls = []

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        self.calls.append({"model": model, "tools": bool(tools), "json": json_mode})
        if json_mode:
            return LLMResponse('{"facts": []}')
        last = messages[-1]
        if last["role"] == "tool":
            return LLMResponse(f"The answer is {last['content']}.", model=model or "")
        if "1234 * 5678" in last["content"] and tools:
            raw = {"role": "assistant", "content": "", "tool_calls": [{"id": "c1", "type": "function", "function": {"name": "calculate", "arguments": "{}"}}]}
            return LLMResponse("", [ToolCallRequest("c1", "calculate", {"expression": "1234 * 5678"})], model or "", raw_message=raw)
        return LLMResponse("Hello from Lily, happy to help with whatever you need today.", model=model or "")

    async def list_models(self):
        return []


_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class SmokeTests(unittest.TestCase):
    def setUp(self):
        import os

        self.tmp = tempfile.mkdtemp()
        os.environ["LILYAI_DATA_DIR"] = self.tmp
        os.environ["GROQ_API_KEY"] = ""
        self.provider = ScriptedProvider()
        self.app: App = build_app(load_settings(), provider=self.provider, search_provider=object())

    def say(self, uid, text):
        out = run(self.app.router.route(IncomingMessage(uid, text, "Tester", "simulator")))
        return out

    def test_onboarding_then_chat(self):
        out = self.say("u1", "hi")
        self.assertIn("call you", out[0].text)
        out = self.say("u1", "Sam")
        self.assertIn("How do you like replies", out[0].text)
        out = self.say("u1", "2")
        self.assertIn("Got it", out[0].text)
        facts = [f.fact for f in self.app.memory.user.list("u1")]
        self.assertIn("User's name is Sam", facts)
        self.assertIn("Prefers short, to-the-point replies", facts)
        out = self.say("u1", "tell me something")
        self.assertEqual(out[0].text, "Hello from Lily, happy to help with whatever you need today.")
        self.assertTrue(out[0].reply_id)

    def test_tool_loop(self):
        self.app.memory.user.add("u2", "Test user")
        out = self.say("u2", "What is 1234 * 5678?")
        self.assertIn("7006652", out[0].text)
        self.assertEqual(out[0].meta["tools"], ["calculate"])
        self.assertEqual(self.app.memory.conversation.count("u2"), 2)

    def test_remember_show_forget(self):
        self.app.memory.user.add("u3", "Seed fact")
        out = self.say("u3", "Remember that I like green tea")
        self.assertIn("green tea", out[0].text)
        out = self.say("u3", "what do you remember about me?")
        self.assertIn("green tea", out[0].text)
        self.say("u3", "forget everything about me")
        out = self.say("u3", "yes")
        self.assertIn("wiped", out[0].text)
        self.assertEqual(self.app.memory.user.list("u3"), [])

    def test_rag_and_feedback_promotion(self):
        n = self.app.rag.ingest_text("handbook.md", "Lily was built in Python.\n\nThe deploy target is Render using Docker containers.")
        self.assertGreater(n, 0)
        hits = self.app.rag.retrieve("Where is it deployed? Render docker")
        self.assertTrue(hits and "Render" in hits[0].chunk.text)
        self.app.memory.user.add("u4", "Test user")
        out = self.say("u4", "Where is Lily deployed? Render docker question")
        self.assertTrue(out[0].meta)
        note = self.app.feedback.handle("u4", out[0].reply_id, 1)
        self.assertIn("Thanks", note)
        self.assertIn("already", self.app.feedback.handle("u4", out[0].reply_id, 1))
        self.assertIn("learned:qa", self.app.rag.stats()["sources"])

    def test_tools_and_helpers(self):
        from LilyAiCore.Helpers.text import chunk_for_discord
        from LilyAiCore.Exceptions.errors import ToolError, ToolValidationError
        from LilyAiTool.UtilityTools import safe_calculate
        from LilyAiTool.Validator import validate_args

        self.assertEqual(safe_calculate("2 ** 10 + 1"), "1025")
        with self.assertRaises(ToolError):
            safe_calculate("__import__('os').system('x')")
        with self.assertRaises(ToolError):
            safe_calculate("9 ** 9999")
        with self.assertRaises(ToolValidationError):
            validate_args({"properties": {"a": {"type": "string"}}, "required": ["a"]}, {})
        parts = chunk_for_discord("word " * 900, 2000)
        self.assertTrue(all(len(p) <= 2000 for p in parts) and len(parts) >= 3)

    def test_ssrf_guard_and_rate_limit(self):
        from LilyAiWeb.Sources import is_safe_url

        self.assertFalse(is_safe_url("http://127.0.0.1:8000/x"))
        self.assertFalse(is_safe_url("http://169.254.169.254/latest"))
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertTrue(is_safe_url("https://example.com/a"))
        self.app.memory.user.add("u5", "x")
        outs = [self.say("u5", f"msg {i}") for i in range(10)]
        self.assertTrue(any("catch up" in o[0].text for o in outs))


if __name__ == "__main__":
    unittest.main()
