#!/usr/bin/env python3
"""Reproduce April support metrics using Python's standard library."""
import csv, json, statistics, sys
from datetime import datetime
from pathlib import Path

def dt(s):
    return datetime.fromisoformat(s.replace('Z', '+00:00'))

cutoff = dt('2026-05-01T00:00:00Z')
start = dt('2026-04-01T00:00:00Z')
source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / 'input' / 'ticket_export.csv'
destination = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent / 'metrics.json'
with source.open(newline='') as f:
    raw = list(csv.DictReader(f))
eligible = [r for r in raw if dt(r['updated_at']) < cutoff]
latest = {}
for r in eligible:
    tid = r['ticket_id']
    if tid not in latest or dt(r['updated_at']) > dt(latest[tid]['updated_at']):
        latest[tid] = r
non_test = [r for r in latest.values() if r['is_test'].lower() != 'true']
cohort = [r for r in non_test if start <= dt(r['created_at']) < cutoff]

def metrics(rows):
    responses = []
    breaches = unanswered = unresolved = 0
    for r in rows:
        created = dt(r['created_at'])
        if r['first_response_at']:
            hours = (dt(r['first_response_at']) - created).total_seconds() / 3600
            responses.append(hours)
        else:
            unanswered += 1
            hours = (cutoff - created).total_seconds() / 3600
        breaches += hours > {'P1': 1, 'P2': 4, 'P3': 12}[r['priority']]
        unresolved += r['status'] != 'resolved'
    return {'tickets': len(rows), 'breached': breaches, 'breach_rate_pct': round(100 * breaches / len(rows), 2) if rows else None,
            'median_first_response_hours': round(statistics.median(responses), 2) if responses else None,
            'unanswered': unanswered, 'unresolved': unresolved}

result = {'overall': metrics(cohort),
          'by_queue': {q: metrics([r for r in cohort if r['queue'] == q]) for q in ('Billing', 'Technical', 'Account')},
          'audit': {'raw_rows': len(raw), 'rows_at_or_after_cutoff': len(raw) - len(eligible), 'deduplicated_ids': len(latest),
                    'test_ids_excluded': len(latest) - len(non_test),
                    'march_ids_excluded': sum(dt(r['created_at']).year == 2026 and dt(r['created_at']).month == 3 for r in non_test)},
          'weekly': {label: metrics([r for r in cohort if lo <= dt(r['created_at']).day <= hi]) for label, lo, hi in
                     [('Apr 1-7', 1, 7), ('Apr 8-14', 8, 14), ('Apr 15-21', 15, 21), ('Apr 22-30', 22, 30)]},
          'by_segment': {s: metrics([r for r in cohort if r['customer_segment'] == s]) for s in ('Enterprise', 'Small business', 'Consumer')},
          'extra': {'eligible_snapshot_rows': len(eligible), 'superseded_snapshot_rows': len(eligible) - len(latest),
                    'late_april_by_queue': {q: metrics([r for r in cohort if r['queue'] == q and dt(r['created_at']).day >= 22]) for q in ('Billing', 'Technical', 'Account')}}}
tmp = destination.with_suffix('.tmp')
tmp.write_text(json.dumps(result, indent=2) + '\n')
tmp.replace(destination)
print(json.dumps(result, indent=2))
