"""Synthetic DeadlineBench fixture: buggy daily service-window helpers.

Minute values use a single day, with 1440 allowed only as an end boundary.
See TASK.md for the complete repair contracts. This is not production code.
"""


def parse_minute(text):
    """Convert an exact HH:MM clock string into an integer minute."""
    hours, minutes = text.split(":")
    return int(hours) * 60 + int(minutes)


def merge_windows(windows):
    """Return sorted, disjoint windows, merging overlaps and touching ends."""
    windows.sort()
    merged = []
    for start, end in windows:
        if not 0 <= start < end <= 1440:
            raise ValueError("window outside day")
        if merged and start < merged[-1][1]:
            merged[-1] = (merged[-1][0], end)
        else:
            merged.append((start, end))
    return merged


def total_minutes(windows):
    """Measure the union of the windows without double-counting coverage."""
    total = 0
    for start, end in windows:
        total += end - start
    return total


def contains_minute(windows, minute):
    """Return whether a valid minute belongs to the half-open window union."""
    if not 0 <= minute <= 1440:
        raise ValueError("minute outside day")
    for start, end in windows:
        if start <= minute <= end:
            return True
    return False


def gap_windows(windows, start=0, end=1440):
    """Return uncovered half-open windows inside the supplied bounds."""
    gaps = []
    cursor = start
    for left, right in merge_windows(windows):
        if left > cursor:
            gaps.append((cursor, left))
        cursor = right
    return gaps


def format_minute(minute):
    """Format a day boundary as HH:MM, including the closing boundary 24:00."""
    if not 0 <= minute < 1440:
        raise ValueError("minute outside day")
    hours, minutes = divmod(minute, 60)
    return f"{hours}:{minutes:02d}"
