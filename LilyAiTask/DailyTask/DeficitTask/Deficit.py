"""Deficit Task

Daily fan-gain quota tracker feeding into the 150-million monthly quota
(see MonthlyTask/quota.py).

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

# Base daily quota - 150,000,000 monthly quota spread over 30 days.
DAILY_QUOTA = 5_000_000

# Kept in sync with LilyAiTask/MonthlyTask/quota.py MONTHLY_QUOTA.
MONTHLY_QUOTA = 150_000_000


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


def run():
    """Entry point for the Deficit daily task."""
    pass


if __name__ == "__main__":
    run()
