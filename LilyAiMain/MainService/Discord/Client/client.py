"""Discord DM client. Thin adapter: all behaviour lives in the router.

Also carries the (separate, opt-in) live-channel relay: the DM path above is untouched -
router.route() and everything downstream is still DM-only - but if the admin has picked a
channel to watch (see ChannelWatch / RelayChannelStore), messages posted there are mirrored
into that buffer for the web Relay page's Channel tab, and the same page can send messages
(optionally as a reply) back into that channel through send_channel_message().
"""
import asyncio
import re
import time
import urllib.parse
from collections import deque

import discord

from LilyAiCore.ExternalServices.Discord.helpers import split_reply
from LilyAiCore.ExternalServices.Discord.reconnect_state import ReconnectState
from LilyAiCore.Logging.logger import get_logger
from LilyAiMain.MainService.bootstrap import App
from LilyAiMain.MainService.Interaction.messages import IncomingMessage, MenuItem, OutgoingMessage

log = get_logger("discord.client")

_NO_CONTENT_REPLY = "I can't read images, files, or stickers yet - could you describe what you'd like in words?"


class FeedbackButton(discord.ui.DynamicItem[discord.ui.Button], template=r"lily_fb:(?P<rating>up|down):(?P<reply_id>[0-9a-f]{6,32})"):
    """Thumbs up/down. Stateless by design: everything it needs (which reply, which way) is
    encoded in custom_id and re-parsed by from_custom_id() on every click, so a single
    add_dynamic_items(FeedbackButton) call at startup covers every feedback button ever sent,
    including ones sent before the process last restarted."""

    def __init__(self, app: App, rating: int, reply_id: str):
        super().__init__(
            discord.ui.Button(
                label="\U0001F44D" if rating > 0 else "\U0001F44E",
                style=discord.ButtonStyle.secondary,
                custom_id=f"lily_fb:{'up' if rating > 0 else 'down'}:{reply_id}",
            )
        )
        self.app, self.rating, self.reply_id = app, rating, reply_id

    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Item, match: re.Match[str]) -> "FeedbackButton":
        rating = 1 if match["rating"] == "up" else -1
        return cls(interaction.client.app, rating, match["reply_id"])

    async def callback(self, interaction: discord.Interaction) -> None:
        user_id = str(interaction.user.id)
        note = self.app.feedback.handle(user_id, self.reply_id, self.rating)
        self.app.bus.publish("feedback", "discord", user_id, text=f"{'+1' if self.rating > 0 else '-1'} on {self.reply_id}")
        await interaction.response.edit_message(view=None)
        await interaction.followup.send(note, ephemeral=True)


class FeedbackView(discord.ui.View):
    """Thumbs up/down buttons under a reply, built from the persistent FeedbackButton above."""

    def __init__(self, app: App, reply_id: str):
        super().__init__(timeout=None)
        self.add_item(FeedbackButton(app, 1, reply_id))
        self.add_item(FeedbackButton(app, -1, reply_id))


class MenuButton(discord.ui.DynamicItem[discord.ui.Button], template=r"lily_menu:(?P<text>.+)"):
    """Quick-action button; replays its text through the router as if the user typed it.
    Persistent for the same reason as FeedbackButton - see its docstring."""

    def __init__(self, app: App, label: str, text: str):
        super().__init__(
            discord.ui.Button(label=label, style=discord.ButtonStyle.primary, custom_id=f"lily_menu:{urllib.parse.quote(text)}")
        )
        self.app, self.text = app, text

    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Item, match: re.Match[str]) -> "MenuButton":
        label = getattr(item, "label", None) or ""
        return cls(interaction.client.app, label, urllib.parse.unquote(match["text"]))

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        await interaction.client.process(interaction.user.id, interaction.user.display_name, self.text, interaction.channel)


class MenuView(discord.ui.View):
    """A row of quick-action buttons built from persistent MenuButton items."""

    def __init__(self, app: App, items: list[MenuItem]):
        super().__init__(timeout=None)
        for item in items:
            self.add_item(MenuButton(app, item.label, item.text))


class LilyDiscordClient(discord.Client):
    def __init__(self, app: App):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        super().__init__(intents=intents)
        self.app = app
        # Registered once; from_custom_id() reconstructs a fresh handler per click from the
        # custom_id alone, so this single call covers every button ever sent, past or future.
        self.add_dynamic_items(FeedbackButton, MenuButton)
        # Bounded FIFO de-dupe guard against a duplicate gateway dispatch of the same DM.
        self._seen_message_ids: deque[int] = deque(maxlen=2000)
        self._seen_message_id_set: set[int] = set()

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
        stored = self.app.relay_channel_store.get()
        if stored and self.app.channel_watch.channel_id is None:
            try:
                await self.watch_channel(stored["channel_id"])
            except Exception as e:
                log.warning("couldn't resume watching channel %s: %s", stored["channel_id"], e)

    async def on_disconnect(self):
        self.app.discord_state.on_disconnect()

    def _already_seen(self, message_id: int) -> bool:
        if message_id in self._seen_message_id_set:
            return True
        if len(self._seen_message_ids) >= self._seen_message_ids.maxlen:
            oldest = self._seen_message_ids.popleft()
            self._seen_message_id_set.discard(oldest)
        self._seen_message_ids.append(message_id)
        self._seen_message_id_set.add(message_id)
        return False

    async def on_message(self, message: discord.Message):
        if message.guild is not None:
            await self._relay_channel_message(message)
            return  # server messages never reach the AI chat pipeline - DM-only, unchanged
        if message.author.bot:
            return
        if self._already_seen(message.id):
            return
        if not message.content.strip():
            if message.attachments or message.stickers:
                await message.channel.send(_NO_CONTENT_REPLY)
            return
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
                    view = FeedbackView(self.app, out.reply_id)
                elif out.menu:
                    view = MenuView(self.app, out.menu)
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

    # ---- live channel relay (Relay page "Channel" tab) ----

    def list_channels(self) -> list[dict]:
        """Every text AND voice channel (voice channels support Discord's "text in voice
        chat"), across every server the bot is in, that it can actually post in - detected
        straight from the live gateway connection (no extra Discord API calls). Voice channels
        are included so an admin can also relay into one (e.g. to drop a link/file for people
        in a call); this only adds them to the picker - the bot never joins voice audio/video
        itself, and no voice-gateway dependency (PyNaCl/ffmpeg/libdave) is added by this. Stays
        strictly text-in-channel, same as the existing text-channel relay. channel_type tells
        the frontend which kind each entry is ("text" or "voice"). IDs go out as strings:
        they're 64-bit and JS's Number can't hold them exactly, so a raw JSON number gets
        silently corrupted round-tripping through the browser."""
        out = []
        for guild in self.guilds:
            me = guild.me
            if me is None:
                continue
            channels = [(ch, "text") for ch in guild.text_channels] + [(ch, "voice") for ch in guild.voice_channels]
            for ch, kind in channels:
                if ch.permissions_for(me).send_messages:
                    out.append({
                        "guild_id": str(guild.id), "guild_name": guild.name,
                        "channel_id": str(ch.id), "channel_name": ch.name, "channel_type": kind,
                    })
        return out

    async def watch_channel(self, channel_id: int | None) -> dict:
        """Switch (or clear, if channel_id is None) which channel is mirrored into
        self.app.channel_watch, persist the choice, and backfill recent history so the web
        UI isn't empty on first open."""
        watch, store = self.app.channel_watch, self.app.relay_channel_store
        if channel_id is None:
            watch.reset(None, "", None, "")
            store.clear()
            return watch.status()

        channel = self.get_channel(channel_id) or await self.fetch_channel(channel_id)
        guild = channel.guild
        watch.reset(channel.id, channel.name, guild.id, guild.name)
        store.set(channel.id, channel.name, guild.id, guild.name)
        try:
            async for msg in channel.history(limit=30, oldest_first=True):
                watch.add(
                    message_id=msg.id, author=msg.author.display_name, is_me=msg.author.id == self.user.id,
                    text=msg.content, ts=msg.created_at.timestamp(), reply_to=self._reply_meta(msg),
                )
        except discord.HTTPException as e:
            log.warning("couldn't backfill history for channel %s: %s", channel_id, e)
        return watch.status()

    async def send_channel_message(self, channel_id: int, text: str, reply_to: int | None = None) -> None:
        channel = self.get_channel(channel_id) or await self.fetch_channel(channel_id)
        reference = discord.MessageReference(message_id=reply_to, channel_id=channel.id, fail_if_not_exists=False) if reply_to else None
        await channel.send(text, reference=reference)

    def _reply_meta(self, msg: discord.Message) -> dict | None:
        ref = msg.reference
        if not ref or not ref.message_id:
            return None
        resolved = ref.resolved
        if isinstance(resolved, discord.Message):
            return {"message_id": resolved.id, "author": resolved.author.display_name, "text": resolved.content[:120]}
        return {"message_id": ref.message_id, "author": "", "text": ""}

    async def _relay_channel_message(self, message: discord.Message) -> None:
        watch = self.app.channel_watch
        if watch.channel_id is None or message.channel.id != watch.channel_id:
            return
        watch.add(
            message_id=message.id, author=message.author.display_name, is_me=message.author.id == self.user.id,
            text=message.content, ts=message.created_at.timestamp(), reply_to=self._reply_meta(message),
        )
