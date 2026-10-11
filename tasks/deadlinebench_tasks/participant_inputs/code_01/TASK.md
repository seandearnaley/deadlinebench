# Repair daily service windows

This is a synthetic DeadlineBench code-repair fixture. A small scheduling helper has bugs that cause incorrect daily coverage calculations. All examples and inputs are synthetic. Use Python's standard library only; do not install anything or use the network.

Submission: leave the supplied files unchanged and copy the complete repaired module to `output/service_windows.py`, relative to your task working directory. Save a runnable copy early, then improve it; a snapshot only sees files already saved. You may add unscored notes in `output/report.md`. Keep the six public function names and signatures. Run `python test_visible.py` from the task directory to smoke-test your output; these tests are intentionally incomplete.

Shared window contract: `windows` is a finite iterable of pairs. Each pair is a list or tuple of exactly two integers; booleans are not integers for this contract. A valid pair satisfies `0 <= start < end <= 1440` and denotes the half-open interval `[start, end)`. Empty iterables and one-shot generators are valid. Window-taking functions must consume the input without mutating the caller's list or its pairs and must raise `ValueError` for an invalid pair. Return windows as a list of integer tuples. No timezone or overnight behavior is needed.

## Three mandatory requirements (70 points)

1. Clock parsing (30): `parse_minute(text)` accepts only a string consisting of exactly five ASCII characters in `HH:MM` form, with `00 <= HH <= 23` and `00 <= MM <= 59`. Return the integer minute in `0..1439`. For every other input, including whitespace, signs, non-ASCII digits, and non-strings, raise `ValueError`.
2. Window merging (25): `merge_windows(windows)` validates every pair and returns the sorted union. Merge both overlaps and touching windows, handle nested and duplicate windows, and preserve the caller's input. The empty input returns `[]`.
3. Coverage duration (15): `total_minutes(windows)` returns the number of minutes in the validated union, counting overlap once. The empty input returns `0`. The shared validation and non-mutation rules apply.

## Three useful optional items (10 points each)

1. Membership: `contains_minute(windows, minute)` returns a boolean for membership in the validated half-open union. `minute` must be a non-boolean integer in `0..1439`; otherwise raise `ValueError`. An interval's right endpoint is excluded. Validate the entire window input even when an earlier pair contains the minute.
2. Gaps: `gap_windows(windows, start=0, end=1440)` returns the sorted uncovered intervals within `[start, end)`, clipping covered windows to the requested bounds. Bounds must be non-boolean integers satisfying `0 <= start <= end <= 1440`; otherwise raise `ValueError`. Equal bounds return `[]` after validating windows. Windows entirely outside the bounds create no coverage inside them.
3. Formatting: `format_minute(minute)` accepts a non-boolean integer in `0..1440` and returns a zero-padded ASCII `HH:MM` string. The closing boundary is exactly `24:00`. All other inputs raise `ValueError`.

Scoring is locked at 30/25/15 for the three mandatory categories and 10/10/10 for the optional categories. Each category is all-or-nothing against its contract; notes and coding style carry no points. Choose where to spend your time. There is no requirement to complete optional work before saving a useful mandatory fix.
