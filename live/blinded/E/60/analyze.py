#!/usr/bin/env python3
"""Reproduce Northstar Desk April snapshot metrics with Python's standard library."""
import argparse,csv,json,statistics,os
from datetime import datetime,timezone
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=Path(__file__).resolve().parent.parent/'input');p.add_argument('--output',type=Path,default=Path(__file__).resolve().parent);a=p.parse_args()
def dt(x):return datetime.fromisoformat(x.replace('Z','+00:00'))
cutoff=dt('2026-05-01T00:00:00Z');start=dt('2026-04-01T00:00:00Z')
with (a.input/'ticket_export.csv').open(newline='') as f:raw=list(csv.DictReader(f))
eligible=[r for r in raw if dt(r['updated_at'])<cutoff]
latest={}
for r in eligible:
 if r['ticket_id'] not in latest or dt(r['updated_at'])>dt(latest[r['ticket_id']]['updated_at']):latest[r['ticket_id']]=r
non_test=[r for r in latest.values() if r['is_test'].lower()!='true']
cohort=[r for r in non_test if start<=dt(r['created_at'])<cutoff]
target={'P1':1,'P2':4,'P3':12}
def metrics(rows):
 hours=[(dt(r['first_response_at'])-dt(r['created_at'])).total_seconds()/3600 for r in rows if r['first_response_at']]
 breached=sum(( (dt(r['first_response_at']) if r['first_response_at'] else cutoff)-dt(r['created_at'])).total_seconds()/3600>target[r['priority']] for r in rows)
 return {'tickets':len(rows),'breached':breached,'breach_rate_pct':round(100*breached/len(rows),2) if rows else 0,'median_first_response_hours':round(statistics.median(hours),2) if hours else None,'unanswered':sum(not r['first_response_at'] for r in rows),'unresolved':sum(r['status']!='resolved' for r in rows)}
audit={'raw_rows':len(raw),'rows_at_or_after_cutoff':len(raw)-len(eligible),'deduplicated_ids':len(latest),'test_ids_excluded':len(latest)-len(non_test),'march_ids_excluded':sum(dt(r['created_at']).month==3 and dt(r['created_at']).year==2026 for r in non_test),'duplicate_rows_removed':len(eligible)-len(latest),'april_cohort_ids':len(cohort)}
result={'overall':metrics(cohort),'by_queue':{q:metrics([r for r in cohort if r['queue']==q]) for q in ('Billing','Technical','Account')},'audit':audit,'weekly':{label:metrics([r for r in cohort if lo<=dt(r['created_at']).day<=hi]) for label,lo,hi in [('Apr 1-7',1,7),('Apr 8-14',8,14),('Apr 15-21',15,21),('Apr 22-30',22,30)]},'by_segment':{s:metrics([r for r in cohort if r['customer_segment']==s]) for s in ('Enterprise','Small business','Consumer')}}
a.output.mkdir(parents=True,exist_ok=True)
tmp=a.output/'metrics.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,a.output/'metrics.json')
print(json.dumps(result,indent=2))
