"""Numeric evidence only. Run: python checks.py /path/to/output"""
import json,sys
from pathlib import Path
key=json.loads((Path(__file__).parent/'answer_key.json').read_text()); path=Path(sys.argv[1])/'metrics.json'
try: got=json.loads(path.read_text())
except (OSError,ValueError) as exc:
    print(json.dumps({'numeric_points':0,'numeric_max':64,'error':str(exc)}));sys.exit(0)
results=[]
def check(category,path,points):
    a=got;b=key
    try:
        for part in path:a=a[part];b=b[part]
        tol=.020001 if path[-1]=='refund_rate_pct' else .010001 if isinstance(b,float) else 0
        ok=isinstance(a,(int,float)) and not isinstance(a,bool) and abs(a-b)<=tol
    except (KeyError,TypeError):ok=False
    results.append({'category':category,'path':'.'.join(path),'points':points if ok else 0,'max':points,'ok':ok})
for k in ['shipped_orders','gross_sales_usd','refunds_usd','net_sales_usd','product_shipping_cost_usd','marketing_spend_usd','contribution_usd']:check('M1',['overall',k],4)
for q in key['by_channel']:
    for k in ['contribution_usd','refund_rate_pct']:check('M2',['by_channel',q,k],2)
for k in ['raw_orders','non_may_orders','may_cancelled','raw_refund_rows','duplicate_refund_rows','qualifying_refund_events','refunded_order_count']:check('M3',['audit',k],1)
for q in key['by_week']:
    for k in ['shipped_orders','net_sales_usd']:check('O1',['by_week',q,k],1)
for q in key['stress_by_channel']:check('O2',['stress_by_channel',q],1)
check('O2',['stress_total_usd'],1)
print(json.dumps({'numeric_points':sum(r['points'] for r in results),'numeric_max':64,'checks':results},indent=2))
