from LilyAiCore.Logging.logger import get_logger
from .bus import EventBus

log = get_logger("discord.events")


class DiscordEventHandlers:
    """Lifecycle events for the live bot, mirrored onto the bus so the Relay can show them."""

    def __init__(self, bus: EventBus):
        self.bus = bus
        self.connected = False
        self.bot_name = ""

    def on_ready(self, bot_name: str) -> None:
        self.connected, self.bot_name = True, bot_name
        log.info("connected as %s", bot_name)
        self.bus.publish("system", "discord", text=f"Bot connected as {bot_name}")

    def on_disconnect(self) -> None:
        self.connected = False
        self.bus.publish("system", "discord", text="Bot disconnected")

    def on_error(self, where: str, err: Exception) -> None:
        log.error("error in %s: %s", where, err)
        self.bus.publish("error", "discord", text=f"{where}: {type(err).__name__}: {err}")
