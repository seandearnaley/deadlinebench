#!/usr/bin/env python3
"""Run: python3 output/analyze.py input/ticket_export.csv output/metrics.json"""
import csv, json, sys, statistics
from datetime import datetime
from pathlib import Path

def dt(s):
    return datetime.fromisoformat(s.replace('Z', '+00:00'))

def analyze(path):
    cutoff = dt('2026-05-01T00:00:00Z')
    start = dt('2026-04-01T00:00:00Z')
    with open(path, newline='') as f:
        raw = list(csv.DictReader(f))
    eligible = [r for r in raw if dt(r['updated_at']) < cutoff]
    latest = {}
    for r in eligible:
        key = r['ticket_id']
        if key not in latest or dt(r['updated_at']) > dt(latest[key]['updated_at']):
            latest[key] = r
    retained = list(latest.values())
    non_test = [r for r in retained if r['is_test'].lower() != 'true']
    cohort = [r for r in non_test if start <= dt(r['created_at']) < cutoff]
    def metrics(rows):
        responses = []
        breached = unanswered = unresolved = 0
        for r in rows:
            created = dt(r['created_at'])
            reply = dt(r['first_response_at']) if r['first_response_at'] else None
            elapsed = ((reply or cutoff) - created).total_seconds()/3600
            breached += elapsed > {'P1':1,'P2':4,'P3':12}[r['priority']]
            unanswered += reply is None
            unresolved += r['status'] != 'resolved'
            if reply is not None:
                responses.append(elapsed)
        return dict(tickets=len(rows), breached=breached,
                    breach_rate_pct=round(100*breached/len(rows),2) if rows else None,
                    median_first_response_hours=round(statistics.median(responses),2) if responses else None,
                    unanswered=unanswered, unresolved=unresolved)
    audit = dict(raw_rows=len(raw), rows_at_or_after_cutoff=len(raw)-len(eligible),
                 deduplicated_ids=len(retained), test_ids_excluded=len(retained)-len(non_test),
                 march_ids_excluded=sum(dt(r['created_at']).month == 3 for r in non_test))
    result = dict(overall=metrics(cohort),
                  by_queue={q:metrics([r for r in cohort if r['queue']==q]) for q in ['Billing','Technical','Account']},
                  audit=audit,
                  weekly={label:metrics([r for r in cohort if lo <= dt(r['created_at']).day <= hi]) for label,lo,hi in [('Apr 1-7',1,7),('Apr 8-14',8,14),('Apr 15-21',15,21),('Apr 22-30',22,30)]},
                  by_segment={s:metrics([r for r in cohort if r['customer_segment']==s]) for s in ['Enterprise','Small business','Consumer']})
    result['audit']['duplicate_snapshot_rows_removed'] = len(eligible)-len(retained)
    return result

if __name__ == '__main__':
    result = analyze(sys.argv[1])
    dest = Path(sys.argv[2])
    tmp = dest.with_suffix('.tmp')
    tmp.write_text(json.dumps(result, indent=2)+'\n')
    tmp.replace(dest)
