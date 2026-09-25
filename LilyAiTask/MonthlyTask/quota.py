"""Quota Task

Monthly quota tracker. The quota is a fixed target of 150 (m) that must be
fully met before the tally period closes, regardless of how many days are
in the given month (28-31). The target does NOT scale up or down based on
month length.
"""

# Fixed monthly quota target - does not vary with days in month (28-31).
MONTHLY_QUOTA = 150


def get_quota() -> int:
    """Return the fixed monthly quota target."""
    return MONTHLY_QUOTA


def is_quota_met(current_total: int) -> bool:
    """Check whether the accumulated total meets or exceeds the monthly quota.

    Args:
        current_total: The amount accumulated so far this month.

    Returns:
        True if current_total >= MONTHLY_QUOTA, False otherwise.
    """
    return current_total >= MONTHLY_QUOTA


def remaining_quota(current_total: int) -> int:
    """Return how much is left to reach the monthly quota (never negative)."""
    return max(0, MONTHLY_QUOTA - current_total)


def run():
    """Entry point for the Quota monthly task."""
    pass


if __name__ == "__main__":
    run()
