#!/usr/bin/env python3
"""Recreate Northstar Desk April metrics using only the Python standard library.
Run: python3 output/analysis.py input/ticket_export.csv output/metrics.json
"""
import argparse
import csv
import json
import os
from datetime import datetime
from pathlib import Path
from statistics import median

CUTOFF = datetime.fromisoformat('2026-05-01T00:00:00+00:00')
START = datetime.fromisoformat('2026-04-01T00:00:00+00:00')
SLA = {'P1': 1, 'P2': 4, 'P3': 12}
QUEUES = ('Billing', 'Technical', 'Account')
SEGMENTS = ('Enterprise', 'Small business', 'Consumer')
WEEKS = ('Apr 1-7', 'Apr 8-14', 'Apr 15-21', 'Apr 22-30')

def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))

def metrics(tickets):
    response_hours = []
    breached = unanswered = unresolved = 0
    for row in tickets:
        created = timestamp(row['created_at'])
        if row['first_response_at']:
            elapsed = (timestamp(row['first_response_at']) - created).total_seconds() / 3600
            response_hours.append(elapsed)
        else:
            unanswered += 1
            elapsed = (CUTOFF - created).total_seconds() / 3600
        breached += int(elapsed > SLA[row['priority']])
        unresolved += int(row['status'] != 'resolved')
    count = len(tickets)
    return {'tickets': count, 'breached': breached,
            'breach_rate_pct': round(100 * breached / count, 2) if count else None,
            'median_first_response_hours': round(median(response_hours), 2) if response_hours else None,
            'unanswered': unanswered, 'unresolved': unresolved}

def analyze(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    eligible = [r for r in rows if timestamp(r['updated_at']) < CUTOFF]
    latest = {}
    for row in eligible:
        key = row['ticket_id']
        if key not in latest or timestamp(row['updated_at']) > timestamp(latest[key]['updated_at']):
            latest[key] = row
    deduplicated = list(latest.values())
    tests = [r for r in deduplicated if r['is_test'].lower() == 'true']
    production = [r for r in deduplicated if r['is_test'].lower() != 'true']
    march = [r for r in production if timestamp(r['created_at']) < START]
    april = [r for r in production if START <= timestamp(r['created_at']) < CUTOFF]
    def week(row):
        day = timestamp(row['created_at']).day
        return WEEKS[min((day - 1) // 7, 3)]
    result = {
        'overall': metrics(april),
        'by_queue': {q: metrics([r for r in april if r['queue'] == q]) for q in QUEUES},
        'audit': {'raw_rows': len(rows), 'rows_at_or_after_cutoff': len(rows) - len(eligible),
                  'deduplicated_ids': len(deduplicated), 'test_ids_excluded': len(tests),
                  'march_ids_excluded': len(march)},
        'weekly': {w: metrics([r for r in april if week(r) == w]) for w in WEEKS},
        'by_segment': {s: metrics([r for r in april if r['customer_segment'] == s]) for s in SEGMENTS},
        'weekly_by_queue': {w: {q: metrics([r for r in april if week(r) == w and r['queue'] == q])
                                for q in QUEUES} for w in WEEKS},
        'additional_audit': {'rows_before_cutoff': len(eligible),
                             'duplicate_snapshot_rows_removed': len(eligible) - len(deduplicated),
                             'production_ids_outside_april_at_or_after_cutoff': sum(timestamp(r['created_at']) >= CUTOFF for r in production)},
        'definitions': {'as_of_utc': CUTOFF.isoformat(),
                        'deduplicated_ids': 'Distinct retained IDs after removing updates at or after cutoff, before test/cohort exclusions.',
                        'sla_hours': SLA, 'breach_comparison': 'strictly greater than priority target',
                        'breach_rate_denominator': 'all qualifying April tickets',
                        'median_denominator': 'qualifying tickets with nonblank first_response_at'}
    }
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path', type=Path)
    parser.add_argument('output_path', type=Path)
    args = parser.parse_args()
    result = analyze(args.csv_path)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output_path.with_name(args.output_path.name + '.tmp')
    temporary.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    os.replace(temporary, args.output_path)

if __name__ == '__main__':
    main()
