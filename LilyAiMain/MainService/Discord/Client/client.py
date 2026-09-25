"""Discord DM client. Thin adapter: all behaviour lives in the router."""
import asyncio
import time

import discord

from LilyAiCore.ExternalServices.Discord.helpers import split_reply
from LilyAiCore.ExternalServices.Discord.reconnect_state import ReconnectState
from LilyAiCore.Logging.logger import get_logger
from LilyAiMain.MainService.bootstrap import App
from LilyAiMain.MainService.Interaction.messages import IncomingMessage, MenuItem, OutgoingMessage

log = get_logger("discord.client")


class FeedbackView(discord.ui.View):
    """Thumbs up/down buttons under a reply."""

    def __init__(self, app: App, reply_id: str, user_id: str):
        super().__init__(timeout=6 * 3600)
        self.app, self.reply_id, self.user_id = app, reply_id, user_id

    async def _rate(self, interaction: discord.Interaction, rating: int):
        note = self.app.feedback.handle(self.user_id, self.reply_id, rating)
        self.app.bus.publish("feedback", "discord", self.user_id, text=f"{'+1' if rating > 0 else '-1'} on {self.reply_id}")
        self.stop()
        await interaction.response.edit_message(view=None)
        await interaction.followup.send(note, ephemeral=True)

    @discord.ui.button(label="\U0001F44D", style=discord.ButtonStyle.secondary)
    async def up(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._rate(interaction, 1)

    @discord.ui.button(label="\U0001F44E", style=discord.ButtonStyle.secondary)
    async def down(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._rate(interaction, -1)


class MenuView(discord.ui.View):
    """Quick-action buttons; each one replays its text through the router as if the user typed it."""

    def __init__(self, client: "LilyDiscordClient", items: list[MenuItem]):
        super().__init__(timeout=3600)
        for item in items:
            btn = discord.ui.Button(label=item.label, style=discord.ButtonStyle.primary)

            async def callback(interaction: discord.Interaction, text=item.text):
                await interaction.response.defer()
                await client.process(interaction.user.id, interaction.user.display_name, text, interaction.channel)

            btn.callback = callback
            self.add_item(btn)


class LilyDiscordClient(discord.Client):
    def __init__(self, app: App):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        super().__init__(intents=intents)
        self.app = app

    async def run_forever(self, token: str, reconnect_state: ReconnectState | None = None) -> None:
        """Connect with exponential backoff. Catches connect-time failures (e.g. a
        Cloudflare/rate-limit block returned as HTTPException) instead of letting them
        propagate and take the whole process down with them. Returns normally once
        self.close() causes start() to exit cleanly (e.g. during app shutdown).

        A Cloudflare error 1015 ("You are being rate limited") is an IP-level ban, not a
        normal gateway rate limit - it needs a much higher floor/ceiling than an ordinary
        connect failure, or repeated short retries just extend it. backoff is persisted via
        reconnect_state (if given) so a Render redeploy landing mid-cooldown resumes the wait
        instead of resetting to the floor and immediately retrying into the same ban.
        """
        backoff, ceiling = 30, 900
        CF_FLOOR, CF_CEILING = 300, 3600  # 5min - 1hr: Cloudflare 1015 bans typically run tens of minutes

        if reconnect_state:
            next_at, saved_backoff = reconnect_state.get()
            wait = next_at - time.time()
            if wait > 0:
                log.warning("resuming a discord reconnect cooldown from before restart: waiting %ss", int(wait))
                await asyncio.sleep(wait)
            if saved_backoff:
                backoff = saved_backoff

        while True:
            try:
                await self.start(token)
                if reconnect_state:
                    reconnect_state.clear()
                return
            except discord.HTTPException as e:
                if "cloudflare" in str(e).lower() or "error code: 1015" in str(e).lower():
                    backoff, ceiling = max(backoff, CF_FLOOR), CF_CEILING
                    log.error("discord connection blocked by Cloudflare (IP rate-limited, not just a gateway 429): %r", e)
                else:
                    log.error("discord connection failed: %r", e)
            except Exception:
                log.exception("discord stopped unexpectedly")
            if self.is_closed():
                return
            log.warning("retrying discord connection in %ss", backoff)
            if reconnect_state:
                reconnect_state.set(time.time() + backoff, backoff)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, ceiling)

    async def on_ready(self):
        self.app.discord_state.on_ready(str(self.user))

    async def on_disconnect(self):
        self.app.discord_state.on_disconnect()

    async def on_message(self, message: discord.Message):
        if message.author.bot or message.guild is not None:
            return  # DM-first: ignore servers and other bots
        async with message.channel.typing():
            await self.process(message.author.id, message.author.display_name, message.content, message.channel)

    async def process(self, user_id: int, name: str, text: str, channel: discord.abc.Messageable):
        try:
            outgoing = await self.app.router.route(IncomingMessage(str(user_id), text, name, "discord"))
            for out in outgoing:
                await self._send(channel, out, str(user_id))
        except Exception as e:
            log.exception("failed to handle DM")
            self.app.discord_state.on_error("on_message", e)
            await channel.send("Something went wrong on my side. Try again in a moment.")

    async def _send(self, channel, out: OutgoingMessage, user_id: str):
        parts = split_reply(out.text)
        for i, part in enumerate(parts):
            view = None
            if i == len(parts) - 1:
                if out.reply_id:
                    view = FeedbackView(self.app, out.reply_id, user_id)
                elif out.menu:
                    view = MenuView(self, out.menu)
            await channel.send(part, view=view) if view else await channel.send(part)

    async def send_dm(self, user_id: str, text: str) -> bool:
        """Actuator entry point: send a DM the user didn't just prompt (reminders, notifications).
        Satisfies the Notifier protocol - see LilyAiCore/ExternalServices/Discord/notifier.py."""
        try:
            user = await self.fetch_user(int(user_id))
            dm = await user.create_dm()
            for part in split_reply(text):
                await dm.send(part)
            return True
        except Exception as e:
            log.error("failed to send unsolicited DM to %s: %s", user_id, e)
            return False
