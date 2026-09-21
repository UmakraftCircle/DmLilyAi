"""Model scan tests: probing, pool growth, retirement, persistence, catalog output. No network."""
import asyncio
import sys
import tempfile
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
try:
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiCore.Config.models import ModelPool  # noqa: E402
from LilyAiCore.Exceptions.errors import RateLimitError  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse, ToolCallRequest  # noqa: E402
from LilyAiLearning.Evaluation.model_scan import CATALOG_NAME, ModelScanner  # noqa: E402

_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class FakeGroq(LLMProvider):
    def __init__(self, infos):
        self.infos, self.probed = infos, []

    async def describe_models(self):
        return self.infos

    async def list_models(self):
        return [i["id"] for i in self.infos]

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        assert fallback is False, "probes must hit the exact model"
        if not tools:
            self.probed.append(model)
        if "limited" in model:
            raise RateLimitError()
        if "bad" in model:
            return LLMResponse("I am not sure.")
        if tools:
            return LLMResponse("", [ToolCallRequest("t", "calculate", {"expression": "1234 * 5678"})])
        return LLMResponse("391")


def info(mid, **kw):
    return {"id": mid, "owned_by": "test", "active": True, "context_window": 131072, "max_completion_tokens": 8192, **kw}


class ScanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.pool = ModelPool()
        self.base = set(self.pool.ids())

    def scanner(self, provider, pool=None, max_auto=6):
        return ModelScanner(provider, pool or self.pool, self.tmp / "state.json", self.tmp / "docs", max_auto=max_auto)

    def test_full_scan_flow(self):
        infos = [info("openai/gpt-oss-20b"), info("new/good-chat"), info("new/bad-chat"), info("new/limited-chat"),
                 info("whisper-large-v3"), info("meta/llama-guard-4"), info("groq/compound"), info("old/dead", active=False)]
        prov = FakeGroq(infos)
        sc = self.scanner(prov)
        rep = run(sc.scan())
        self.assertTrue(rep.ok)
        self.assertEqual(rep.added, ["new/good-chat"])
        self.assertEqual(rep.rejected, ["new/bad-chat"])
        self.assertEqual(rep.deferred, ["new/limited-chat"])
        self.assertTrue(self.pool.has("new/good-chat"))
        self.assertFalse(any(self.pool.has(m) for m in ["new/bad-chat", "whisper-large-v3", "meta/llama-guard-4", "groq/compound", "old/dead"]))
        self.assertNotIn("whisper-large-v3", prov.probed)
        spec = next(m for m in self.pool.all() if m.id == "new/good-chat")
        self.assertTrue(spec.supports_tools)

        catalog = (self.tmp / "docs" / CATALOG_NAME).read_text()
        self.assertIn("new/good-chat", catalog)
        self.assertIn("Rejected", catalog)
        self.assertIn("Not a chat model", catalog)

        # persistence: a fresh pool gets the auto-added model back at startup
        fresh = ModelPool()
        self.assertEqual(self.scanner(FakeGroq(infos), fresh).load_into_pool(), 1)
        self.assertTrue(fresh.has("new/good-chat"))

        # second scan: rejected model is not re-probed, deferred one is retried
        prov2 = FakeGroq(infos)
        run(self.scanner(prov2).scan())
        self.assertNotIn("new/bad-chat", prov2.probed)
        self.assertIn("new/limited-chat", prov2.probed)

    def test_retire_and_safety(self):
        infos = [info("openai/gpt-oss-20b"), info("new/good-chat")]
        run(self.scanner(FakeGroq(infos)).scan())
        self.assertTrue(self.pool.has("new/good-chat"))
        # empty listing must not wipe anything
        rep = run(self.scanner(FakeGroq([])).scan())
        self.assertFalse(rep.ok)
        self.assertTrue(self.pool.has("new/good-chat"))
        # model disappears -> retired, defaults untouched
        rep = run(self.scanner(FakeGroq([info("openai/gpt-oss-20b")])).scan())
        self.assertEqual(rep.retired, ["new/good-chat"])
        self.assertFalse(self.pool.has("new/good-chat"))
        self.assertTrue(self.base <= set(self.pool.ids()))

    def test_probe_budget_and_auto_cap(self):
        infos = [info(f"new/good-{i}") for i in range(5)]
        prov = FakeGroq(infos)
        rep = run(self.scanner(prov, max_auto=6).scan())
        self.assertEqual(len(prov.probed), 3)  # per-scan probe budget
        self.assertEqual(len(rep.added), 3)
        rep2 = run(self.scanner(FakeGroq(infos), max_auto=4).scan())
        self.assertEqual(len(rep2.added), 1)  # cap of 4 reached


if __name__ == "__main__":
    unittest.main()
