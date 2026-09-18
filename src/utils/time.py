from datetime import datetime, timedelta, timezone


MICROSECONDS_PER_SECOND: int = 1_000_000
SECONDS_PER_DAY: int = 24 * 60 * 60
MICROSECONDS_PER_DAY: int = SECONDS_PER_DAY * MICROSECONDS_PER_SECOND

def get_current_webkit_timestamp() -> int:
    epoch_start: datetime = datetime(1601, 1, 1, tzinfo=timezone.utc)
    now: datetime = datetime.now(timezone.utc)
    return (now - epoch_start) // timedelta(microseconds=1)

def days_to_microseconds(days: int) -> int:
    return days * MICROSECONDS_PER_DAY

def get_webkit_timestamp_n_days_ago(days: int) -> int:
    return get_current_webkit_timestamp() - days_to_microseconds(days)
