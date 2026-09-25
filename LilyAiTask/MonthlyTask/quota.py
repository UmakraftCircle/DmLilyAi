"""Quota Task

Monthly fan-gain quota tracker. The quota is a fixed target of 150 million
new fans that must be gained before the tally period closes, regardless of
how many days are in the given month (28-31). The target does NOT scale up
or down based on month length.
"""

# Fixed monthly quota target: 150 million fan gain.
# Does not vary with days in month (28-31).
MONTHLY_QUOTA = 150_000_000


def get_quota() -> int:
    """Return the fixed monthly fan-gain quota target."""
    return MONTHLY_QUOTA


def is_quota_met(fan_gain: int) -> bool:
    """Check whether the accumulated fan gain meets or exceeds the monthly quota.

    Args:
        fan_gain: The number of fans gained so far this month.

    Returns:
        True if fan_gain >= MONTHLY_QUOTA, False otherwise.
    """
    return fan_gain >= MONTHLY_QUOTA


def remaining_quota(fan_gain: int) -> int:
    """Return how many fans are still needed to reach the monthly quota (never negative)."""
    return max(0, MONTHLY_QUOTA - fan_gain)


def run():
    """Entry point for the Quota monthly task."""
    pass


if __name__ == "__main__":
    run()
