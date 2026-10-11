#!/usr/bin/env python3
"""Run: python3 output/analyze.py input/ticket_export.csv output/metrics.json"""
import csv,json,sys,statistics,os
from datetime import datetime
from pathlib import Path

def dt(s): return datetime.fromisoformat(s.replace('Z','+00:00'))
cutoff=dt('2026-05-01T00:00:00Z'); start=dt('2026-04-01T00:00:00Z')
source=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'input/ticket_export.csv'
target=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).resolve().parent/'metrics.json'
with source.open(newline='') as f: rows=list(csv.DictReader(f))
valid=[r for r in rows if dt(r['updated_at'])<cutoff]
latest={}
for r in valid:
    if r['ticket_id'] not in latest or dt(r['updated_at'])>dt(latest[r['ticket_id']]['updated_at']): latest[r['ticket_id']]=r
non_test=[r for r in latest.values() if r['is_test'].lower()!='true']
cohort=[r for r in non_test if start<=dt(r['created_at'])<cutoff]
limits={'P1':1,'P2':4,'P3':12}
def metrics(group):
    durations=[(dt(r['first_response_at'])-dt(r['created_at'])).total_seconds()/3600 for r in group if r['first_response_at']]
    breached=sum((dt(r['first_response_at']) if r['first_response_at'] else cutoff)-dt(r['created_at']) > __import__('datetime').timedelta(hours=limits[r['priority']]) for r in group)
    return dict(tickets=len(group),breached=breached,breach_rate_pct=round(100*breached/len(group),2) if group else 0,median_first_response_hours=round(statistics.median(durations),2) if durations else None,unanswered=sum(not r['first_response_at'] for r in group),unresolved=sum(r['status']!='resolved' for r in group))
result={'overall':metrics(cohort),'by_queue':{q:metrics([r for r in cohort if r['queue']==q]) for q in ['Billing','Technical','Account']},'audit':{'raw_rows':len(rows),'rows_at_or_after_cutoff':len(rows)-len(valid),'deduplicated_ids':len(latest),'test_ids_excluded':len(latest)-len(non_test),'march_ids_excluded':sum(dt(r['created_at']).month==3 and dt(r['created_at']).year==2026 for r in non_test)},'weekly':{label:metrics([r for r in cohort if lo<=dt(r['created_at']).day<=hi]) for label,lo,hi in [('Apr 1-7',1,7),('Apr 8-14',8,14),('Apr 15-21',15,21),('Apr 22-30',22,30)]},'by_segment':{s:metrics([r for r in cohort if r['customer_segment']==s]) for s in ['Enterprise','Small business','Consumer']},'extra_audit':{'rows_before_cutoff':len(valid),'duplicate_snapshots_removed':len(valid)-len(latest)},'queue_weekly':{q:{label:metrics([r for r in cohort if r['queue']==q and lo<=dt(r['created_at']).day<=hi]) for label,lo,hi in [('Apr 1-7',1,7),('Apr 8-14',8,14),('Apr 15-21',15,21),('Apr 22-30',22,30)]} for q in ['Billing','Technical','Account']}}
target.parent.mkdir(parents=True,exist_ok=True)
temp=target.with_suffix('.tmp'); temp.write_text(json.dumps(result,indent=2)+'\n'); os.replace(temp,target)
print(json.dumps(result,indent=2))
