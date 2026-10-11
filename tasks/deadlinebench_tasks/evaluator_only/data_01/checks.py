"""Numeric evidence only. Run: python checks.py /path/to/output"""
import json, sys
from pathlib import Path
key=json.loads((Path(__file__).parent/'answer_key.json').read_text())
output=Path(sys.argv[1]); path=output/'metrics.json'
try: got=json.loads(path.read_text())
except (OSError,ValueError) as exc:
    print(json.dumps({'numeric_points':0,'numeric_max':61,'error':str(exc)}));sys.exit(0)
results=[]
def check(category,path,points):
    a=got;b=key
    try:
        for part in path: a=a[part];b=b[part]
        ok=isinstance(a,(int,float)) and not isinstance(a,bool) and abs(a-b)<=(.020001 if isinstance(b,float) else 0)
    except (KeyError,TypeError): ok=False
    results.append({'category':category,'path':'.'.join(path),'points':points if ok else 0,'max':points,'ok':ok})
for k in ['tickets','breached','breach_rate_pct','median_first_response_hours','unanswered','unresolved']:check('M1',['overall',k],5)
for q in ['Billing','Technical','Account']:
    for k in ['tickets','breached','breach_rate_pct','unanswered']:check('M2',['by_queue',q,k],1)
for k in ['raw_rows','rows_at_or_after_cutoff','deduplicated_ids','test_ids_excluded','march_ids_excluded']:check('M3',['audit',k],1)
for q in key['weekly']:
    for k in ['tickets','breach_rate_pct']:check('O1',['weekly',q,k],1)
for q in key['by_segment']:
    for k in ['tickets','breach_rate_pct']:check('O2',['by_segment',q,k],1)
print(json.dumps({'numeric_points':sum(r['points'] for r in results),'numeric_max':61,'checks':results},indent=2))
