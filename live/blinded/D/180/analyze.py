#!/usr/bin/env python3
"""Recreate April support metrics using only the Python standard library.
Usage: python3 output/analyze.py input/ticket_export.csv output/metrics.json
"""
import argparse
import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

CUTOFF = datetime(2026, 5, 1, tzinfo=timezone.utc)
APRIL_START = datetime(2026, 4, 1, tzinfo=timezone.utc)
TARGETS = {"P1": 1, "P2": 4, "P3": 12}
QUEUES = ("Billing", "Technical", "Account")
SEGMENTS = ("Enterprise", "Small business", "Consumer")
WEEKS = (("Apr 1-7", 1, 7), ("Apr 8-14", 8, 14),
         ("Apr 15-21", 15, 21), ("Apr 22-30", 22, 30))


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def summarize(rows):
    response_hours = []
    breached = unanswered = unresolved = 0
    for row in rows:
        created = timestamp(row["created_at"])
        reply = row["first_response_at"]
        end = timestamp(reply) if reply else CUTOFF
        hours = (end - created).total_seconds() / 3600
        breached += int(hours > TARGETS[row["priority"]])
        unanswered += int(not reply)
        unresolved += int(row["status"] != "resolved")
        if reply:
            response_hours.append(hours)
    return {
        "tickets": len(rows),
        "breached": breached,
        "breach_rate_pct": round(100 * breached / len(rows), 2) if rows else 0.0,
        "median_first_response_hours": round(median(response_hours), 2) if response_hours else None,
        "unanswered": unanswered,
        "unresolved": unresolved,
    }


def analyze(csv_path):
    with open(csv_path, newline="", encoding="utf-8-sig") as handle:
        raw = list(csv.DictReader(handle))
    eligible = [r for r in raw if timestamp(r["updated_at"]) < CUTOFF]
    latest = {}
    for row in eligible:
        prior = latest.get(row["ticket_id"])
        if prior is None or timestamp(row["updated_at"]) > timestamp(prior["updated_at"]):
            latest[row["ticket_id"]] = row
    test_count = sum(r["is_test"].lower() == "true" for r in latest.values())
    real = [r for r in latest.values() if r["is_test"].lower() != "true"]
    march_count = sum(timestamp(r["created_at"]).year == 2026 and timestamp(r["created_at"]).month == 3 for r in real)
    april = [r for r in real if APRIL_START <= timestamp(r["created_at"]) < CUTOFF]
    return {
        "overall": summarize(april),
        "by_queue": {q: summarize([r for r in april if r["queue"] == q]) for q in QUEUES},
        "audit": {
            "raw_rows": len(raw),
            "rows_at_or_after_cutoff": len(raw) - len(eligible),
            "deduplicated_ids": len(latest),
            "test_ids_excluded": test_count,
            "march_ids_excluded": march_count,
            "duplicate_snapshot_rows_removed": len(eligible) - len(latest),
            "other_non_april_ids_excluded": len(real) - march_count - len(april),
        },
        "weekly": {label: summarize([r for r in april if low <= timestamp(r["created_at"]).day <= high])
                   for label, low, high in WEEKS},
        "by_segment": {s: summarize([r for r in april if r["customer_segment"] == s]) for s in SEGMENTS},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    metrics = analyze(args.csv_path)
    args.json_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.json_path.with_name(args.json_path.name + ".tmp")
    temporary.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, args.json_path)


if __name__ == "__main__":
    main()
