"""Lily knows what she can do, and Trainer-link intents work in plain language (no network, no keys).

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import importlib
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

from LilyAiContext.CapabilityContext.capabilities import DM_ACTIONS, account_status_note, format_capabilities  # noqa: E402
from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse  # noqa: E402
from LilyAiMain.MainService.bootstrap import build_app  # noqa: E402
from LilyAiMain.MainService.Interaction.Forms.link_trainer import extract_trainer_id  # noqa: E402
from LilyAiMain.MainService.Interaction.messages import IncomingMessage  # noqa: E402

router_mod = importlib.import_module("LilyAiMain.MainService.Discord.Router.router")

CHAT_REPLY = "Hello from Lily, happy to help with whatever you need today."
_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class CapturingProvider(LLMProvider):
    """Answers plainly and remembers the last system prompt it was sent."""

    def __init__(self):
        self.last_system = ""

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        if json_mode:
            return LLMResponse('{"facts": []}')
        self.last_system = messages[0]["content"]
        return LLMResponse(CHAT_REPLY, model=model or "")

    async def list_models(self):
        return []


class CapabilityPromptTests(unittest.TestCase):
    def test_rules_and_every_dm_action_are_in_the_prompt(self):
        text = format_capabilities([{"function": {"name": "calculate"}}])
        self.assertIn("Never invent", text)
        self.assertIn("Tools available", text)
        for examples, _ in DM_ACTIONS:
            self.assertIn(examples, text)

    def test_says_so_when_there_are_no_tools(self):
        self.assertIn("no tools", format_capabilities([]))
        self.assertNotIn("no tools", format_capabilities([{"function": {"name": "calculate"}}]))

    def test_account_status_note(self):
        linked = account_status_note("612856830731", "Sam")
        self.assertIn("IS linked", linked)
        self.assertIn("612856830731", linked)
        self.assertIn("(Sam)", linked)
        self.assertIn("NOT linked", account_status_note(None))

    def test_dm_action_examples_match_the_router_patterns(self):
        """What the prompt tells users to say must actually trigger the action."""
        r = router_mod
        self.assertTrue(r._HELP.match("help"))
        self.assertTrue(r._HELP.match("menu"))
        self.assertTrue(r._LINK.search("link me"))
        self.assertEqual(extract_trainer_id("my trainer id is 123456789"), "123456789")
        self.assertTrue(r._UNLINK.search("unlink me"))
        self.assertTrue(r._LINK_STATUS.search("what's my trainer id"))
        self.assertTrue(r._LINK_STATUS.search("am I linked?"))
        self.assertTrue(r._SHOW_MEMORY.search("what do you remember about me"))
        self.assertTrue(r._FORGET.search("forget everything about me"))
        self.assertTrue(r._SETUP.search("set me up again"))
        self.assertIsNotNone(r.explicit_memory_request("remember that I like tea"))


class ExtractTrainerIdTests(unittest.TestCase):
    def test_recognised_sentences(self):
        for text, expected in [
            ("My trainer id is 612856830731", "612856830731"),
            ("my trainer ID: 123,456,789", "123456789"),
            ("my uma.moe trainer id is `123456789`.", "123456789"),
            ("link me to 987654321", "987654321"),
            ("link my trainer id 987654321", "987654321"),
        ]:
            self.assertEqual(extract_trainer_id(text), expected, text)

    def test_ignored_sentences(self):
        for text in [
            "unlink my trainer id 987654321",
            "my friend's trainer id is 123456789",
            "my trainer id is 12",
            "what is 2 + 2",
            "link me",
        ]:
            self.assertIsNone(extract_trainer_id(text), text)


class DMFlowTests(unittest.TestCase):
    def setUp(self):
        import os

        os.environ["LILYAI_DATA_DIR"] = tempfile.mkdtemp()
        os.environ["GROQ_API_KEY"] = ""
        self.provider = CapturingProvider()
        self.app = build_app(load_settings(), provider=self.provider, search_provider=object())

    def say(self, uid, text):
        return run(self.app.router.route(IncomingMessage(uid, text, "Tester", "simulator")))

    def test_trainer_id_in_a_plain_sentence_links_directly(self):
        self.app.memory.user.add("a1", "Test user")
        out = self.say("a1", "My trainer id is 612856830731")
        self.assertIn("linked", out[0].text)
        self.assertEqual(self.app.memory.trainer_link.by_discord_id("a1").trainer_id, "612856830731")
        out = self.say("a1", "my trainer id is 612856830731")
        self.assertIn("already linked", out[0].text)

    def test_link_status_question(self):
        self.app.memory.user.add("a2", "Test user")
        out = self.say("a2", "can you check my trainer id I linked with? Yes or no?")
        self.assertIn("not linked", out[0].text)
        self.app.memory.trainer_link.link("a2", "612856830731")
        out = self.say("a2", "can you check my trainer id I linked with? Yes or no?")
        self.assertIn("612856830731", out[0].text)

    def test_stats_question_still_reaches_the_chat_model(self):
        self.app.memory.user.add("a3", "Test user")
        out = self.say("a3", "show my trainer id stats")
        self.assertEqual(out[0].text, CHAT_REPLY)

    def test_prompt_carries_link_status_and_capabilities(self):
        self.app.memory.user.add("a4", "Test user")
        self.say("a4", "tell me something")
        self.assertIn("NOT linked", self.provider.last_system)
        self.assertIn("DM actions", self.provider.last_system)
        self.app.memory.trainer_link.link("a4", "612856830731")
        self.say("a4", "tell me something else")
        self.assertIn("IS linked to uma.moe Trainer ID 612856830731", self.provider.last_system)


if __name__ == "__main__":
    unittest.main()
