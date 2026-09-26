"""Deficit Task

Daily fan-gain quota tracker feeding into the 150-million monthly quota
(see MonthlyTask/quota.py). Sends one Discord DM per day reporting whether
the member met quota, or how much surplus/deficit they have.

The DM is only sent for a member who is already linked: someone with both
a Discord user ID and a uma.moe trainer ID on file. That link is created
via the "link me" DM flow (see LilyAiMain/MainService/Interaction/Forms/
link_trainer.py) and stored by LilyAiMemory.TrainerLink.TrainerLinkStore.
Unlinked trainers are skipped rather than guessed at.

Rules:
- Base daily quota is 5,000,000 fans (5m * 30 days = 150,000,000 monthly).
- If a day falls short of its required amount, the shortfall (deficit)
  carries forward and is added on top of the next day's required quota.
  If the next day still doesn't cover it, the remaining shortfall keeps
  accumulating onto the following day, and so on, until it's paid off.
- If a day exceeds its required amount, the surplus carries forward too,
  reducing the required amount for the next day. This way, whether a
  day is short or over, later days automatically adjust so the month
  still totals exactly 150,000,000 by the end of the tally period.
"""

from dataclasses import dataclass
from typing import Iterable, Optional

import discord

# Base daily quota - 150,000,000 monthly quota spread over 30 days.
DAILY_QUOTA = 5_000_000

# Kept in sync with LilyAiTask/MonthlyTask/quota.py MONTHLY_QUOTA.
MONTHLY_QUOTA = 150_000_000


@dataclass
class LinkedMember:
    """A member with a confirmed Discord <-> uma.moe trainer link.

    Both ids must be present for a daily report to be sendable; this is
    the join point between the Discord side (where the DM goes) and the
    uma.moe side (where fan-gain numbers come from).
    """

    discord_id: int
    trainer_id: str
    trainer_name: Optional[str] = None

    @classmethod
    def from_trainer_link(cls, link) -> "LinkedMember":
        """Build a LinkedMember from a LilyAiMemory TrainerLink record."""
        return cls(
            discord_id=int(link.discord_id),
            trainer_id=link.trainer_id,
            trainer_name=link.trainer_name,
        )


def linked_members(trainer_link_store) -> list[LinkedMember]:
    """Fetch every currently linked member from LilyAiMemory's TrainerLinkStore.

    Args:
        trainer_link_store: A LilyAiMemory.TrainerLink.trainer_link.TrainerLinkStore
            (e.g. app.memory.trainer_link).
    """
    return [LinkedMember.from_trainer_link(link) for link in trainer_link_store.all_linked()]


class DeficitTracker:
    """Tracks daily fan gain against a rolling quota that self-adjusts.

    A shortfall on one day increases the required amount for the next
    day (and keeps stacking onto following days until paid off). A
    surplus on one day decreases the required amount for the next day.
    """

    def __init__(self, daily_quota: int = DAILY_QUOTA):
        self.daily_quota = daily_quota
        # Positive carry = deficit owed (adds to next day's requirement).
        # Negative carry = surplus/credit (reduces next day's requirement).
        self.carry = 0
        self.total_gained = 0
        self.history = []

    def required_today(self) -> int:
        """The fan gain required today, including any carried deficit/surplus."""
        return self.daily_quota + self.carry

    def record_day(self, fan_gain: int) -> dict:
        """Record today's fan gain and roll any shortfall/surplus into tomorrow.

        Args:
            fan_gain: Fans gained today.

        Returns:
            A dict summary of today's result: required, gained, met,
            and the new carry (deficit owed or surplus banked).
        """
        required = self.required_today()
        met = fan_gain >= required

        # Whatever's left over (positive) or short (negative) becomes
        # tomorrow's adjustment. If short, carry stays positive (owed).
        # If over, carry goes negative (credit), lowering tomorrow's ask.
        self.carry = required - fan_gain

        self.total_gained += fan_gain

        result = {
            "required": required,
            "gained": fan_gain,
            "met": met,
            "carry": self.carry,
            "total_gained": self.total_gained,
        }
        self.history.append(result)
        return result

    def is_month_quota_met(self) -> bool:
        """Check whether accumulated total meets the 150m monthly quota."""
        return self.total_gained >= MONTHLY_QUOTA

    def remaining_month_quota(self) -> int:
        """How many fans are still needed to hit the monthly quota."""
        return max(0, MONTHLY_QUOTA - self.total_gained)


def _fmt(n: int) -> str:
    """Format a fan count with thousands separators."""
    return f"{n:,}"


def format_daily_message(
    result: dict,
    member: Optional[LinkedMember] = None,
    monthly_gain: Optional[int] = None,
) -> str:
    """Build the daily DM text from a record_day() result.

    - Exactly met -> confirms quota met, no carry.
    - Gained more than required -> reports surplus banked for tomorrow.
    - Gained less than required -> reports deficit owed, added to tomorrow.

    monthly_gain, when given, overrides result["total_gained"] for the
    "Monthly progress" line. Pass the figure computed by
    LilyAiMemory.FanGain (the same snapshot-based calculation the fan
    gain embed reads) so this DM and the embed never disagree about a
    trainer's monthly total.
    """
    gained = result["gained"]
    required = result["required"]
    carry = result["carry"]
    total = monthly_gain if monthly_gain is not None else result["total_gained"]
    remaining = max(0, MONTHLY_QUOTA - total)

    header = "**Daily Fan Quota Report**"
    if member and member.trainer_name:
        header += f" \u2014 {member.trainer_name}"

    lines = [
        header,
        f"Gained today: {_fmt(gained)}",
        f"Required today: {_fmt(required)}",
    ]

    if carry == 0:
        lines.append("Status: \u2705 Quota met exactly \u2014 no carry into tomorrow.")
    elif carry > 0:
        lines.append(
            f"Status: \u26a0\ufe0f Deficit of {_fmt(carry)} \u2014 added to tomorrow's required quota."
        )
    else:
        lines.append(
            f"Status: \U0001f389 Surplus of {_fmt(-carry)} \u2014 credited, lowering tomorrow's required quota."
        )

    lines.append(f"Monthly progress: {_fmt(total)} / {_fmt(MONTHLY_QUOTA)} (remaining: {_fmt(remaining)})")

    return "\n".join(lines)


async def send_daily_dm(
    client: discord.Client,
    member: LinkedMember,
    result: dict,
    monthly_gain: Optional[int] = None,
) -> None:
    """Send the daily quota report as a Discord DM to a linked member.

    Requires the member to already be linked (has both a Discord ID and
    a uma.moe trainer ID) - if either is missing, the report is skipped
    rather than sent to a guessed/unverified user.

    Args:
        client: The logged-in discord.Client/Bot instance.
        member: The LinkedMember to DM (must have discord_id + trainer_id).
        result: The dict returned by DeficitTracker.record_day().
        monthly_gain: Optional snapshot-based monthly total (see
            format_daily_message) to keep this DM in sync with the fan
            gain embed.
    """
    if not member.discord_id or not member.trainer_id:
        return

    user = client.get_user(member.discord_id) or await client.fetch_user(member.discord_id)
    message = format_daily_message(result, member, monthly_gain)
    await user.send(message)


async def send_daily_reports(
    client: discord.Client,
    members: Iterable[LinkedMember],
    results_by_trainer_id: dict,
) -> None:
    """Send daily DMs for every linked member that has a result today.

    Args:
        client: The logged-in discord.Client/Bot instance.
        members: Linked members eligible for a DM (discord_id + trainer_id).
            Pass linked_members(app.memory.trainer_link) to pull the current
            set straight from storage.
        results_by_trainer_id: Maps trainer_id -> record_day() result dict.
    """
    for member in members:
        result = results_by_trainer_id.get(member.trainer_id)
        if result is None:
            continue
        await send_daily_dm(client, member, result)


def run():
    """Entry point for the Deficit daily task."""
    pass


if __name__ == "__main__":
    run()
