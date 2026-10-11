#!/usr/bin/env python3
"""Recreate metrics.json using Python's standard library only."""
import argparse
import csv
import json
import os
from datetime import datetime
from pathlib import Path
from statistics import median

CUTOFF = datetime.fromisoformat('2026-05-01T00:00:00+00:00')
START = datetime.fromisoformat('2026-04-01T00:00:00+00:00')
TARGETS = {'P1': 1, 'P2': 4, 'P3': 12}
QUEUES = ('Billing', 'Technical', 'Account')
SEGMENTS = ('Enterprise', 'Small business', 'Consumer')
WEEKS = (('Apr 1-7', 1, 7), ('Apr 8-14', 8, 14), ('Apr 15-21', 15, 21), ('Apr 22-30', 22, 30))

def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))

def summarize(rows):
    response_hours = []
    breached = unanswered = unresolved = 0
    for row in rows:
        created = timestamp(row['created_at'])
        response = row['first_response_at']
        if response:
            elapsed = (timestamp(response) - created).total_seconds() / 3600
            response_hours.append(elapsed)
        else:
            unanswered += 1
            elapsed = (CUTOFF - created).total_seconds() / 3600
        breached += elapsed > TARGETS[row['priority']]
        unresolved += row['status'] != 'resolved'
    return {
        'tickets': len(rows),
        'breached': breached,
        'breach_rate_pct': round(100 * breached / len(rows), 2) if rows else None,
        'median_first_response_hours': round(median(response_hours), 2) if response_hours else None,
        'unanswered': unanswered,
        'unresolved': unresolved,
    }

def analyze(input_dir):
    with (input_dir / 'ticket_export.csv').open(newline='', encoding='utf-8') as stream:
        raw = list(csv.DictReader(stream))
    eligible = [r for r in raw if timestamp(r['updated_at']) < CUTOFF]
    latest = {}
    for row in eligible:
        prior = latest.get(row['ticket_id'])
        if prior is None or timestamp(row['updated_at']) > timestamp(prior['updated_at']):
            latest[row['ticket_id']] = row
    tests = [r for r in latest.values() if r['is_test'].lower() == 'true']
    non_tests = [r for r in latest.values() if r['is_test'].lower() != 'true']
    march = [r for r in non_tests if timestamp(r['created_at']).year == 2026 and timestamp(r['created_at']).month == 3]
    april = [r for r in non_tests if START <= timestamp(r['created_at']) < CUTOFF]
    weekly = {name: [r for r in april if lo <= timestamp(r['created_at']).day <= hi] for name, lo, hi in WEEKS}
    return {
        'overall': summarize(april),
        'by_queue': {q: summarize([r for r in april if r['queue'] == q]) for q in QUEUES},
        'audit': {
            'raw_rows': len(raw),
            'rows_at_or_after_cutoff': len(raw) - len(eligible),
            'deduplicated_ids': len(latest),
            'test_ids_excluded': len(tests),
            'march_ids_excluded': len(march),
        },
        'weekly': {name: summarize(rows) for name, rows in weekly.items()},
        'by_segment': {s: summarize([r for r in april if r['customer_segment'] == s]) for s in SEGMENTS},
        'weekly_by_queue': {name: {q: summarize([r for r in rows if r['queue'] == q]) for q in QUEUES} for name, rows in weekly.items()},
        'audit_details': {
            'rows_before_cutoff': len(eligible),
            'duplicate_snapshot_rows_removed': len(eligible) - len(latest),
            'responded_april_tickets': sum(bool(r['first_response_at']) for r in april),
            'other_non_april_ids_excluded': len(non_tests) - len(march) - len(april),
        },
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_dir', nargs='?', type=Path, default=Path(__file__).resolve().parent.parent / 'input')
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent / 'metrics.json')
    args = parser.parse_args()
    metrics = analyze(args.input_dir)
    temporary = args.output.with_name(args.output.name + '.tmp')
    temporary.write_text(json.dumps(metrics, indent=2) + '\n', encoding='utf-8')
    os.replace(temporary, args.output)
    print(json.dumps(metrics, indent=2))

if __name__ == '__main__':
    main()
