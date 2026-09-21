"""Scheduled job: keep the Groq model pool and LilyAiGroqSupport/MODEL_CATALOG.md up to date."""
from LilyAiLearning.Evaluation.model_scan import ModelScanner, ScanReport
from LilyAiMain.MainService.Discord.Events.bus import EventBus


def make_model_scan_job(scanner: ModelScanner, bus: EventBus):
    async def run() -> ScanReport:
        report = await scanner.scan()
        bus.publish("system" if report.ok else "error", "scheduler", text=report.summary())
        return report

    return run
