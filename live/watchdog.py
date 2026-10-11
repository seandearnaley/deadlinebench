"""Measurement-only pilot observer. Freezes delivered files; does not kill models."""
import argparse, datetime, hashlib, json, pathlib, shutil, time
p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('--cutoffs',default='90,180,300');a=p.parse_args()
r=pathlib.Path(a.root);r.mkdir(parents=True,exist_ok=True)
cutoffs=[int(x) for x in a.cutoffs.split(',')]
active={};done=set()
def write(path,data):
 tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2));tmp.replace(path)
print('observer ready',flush=True)
while True:
 for launch in r.glob('*/launch.json'):
  name=launch.parent.name
  if name not in active and name not in done:
   cfg=json.loads(launch.read_text());active[name]=(cfg,float(cfg['monotonic_start']),set())
 for name,(cfg,start,taken) in list(active.items()):
  now=time.monotonic();elapsed=now-start;base=r/name
  if cfg.get('clock_feedback'):
   write(base/'clock.json',{'elapsed_seconds':round(elapsed,2),'remaining_seconds':round(max(0,max(cutoffs)-elapsed),2),'deadline_utc':cfg['deadline_utc']})
  for cutoff in cutoffs:
   if elapsed>=cutoff and cutoff not in taken:
    dest=base/'snapshots'/str(cutoff);dest.mkdir(parents=True,exist_ok=True);records=[]
    out=base/'output'
    if out.exists():
     for f in sorted(out.rglob('*')):
      if f.is_file() and not f.is_symlink():
       before=f.stat();data=f.read_bytes();after=f.stat();relative=f.relative_to(out)
       target=dest/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
       records.append({'file':str(relative),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'stable_during_read':before.st_mtime_ns==after.st_mtime_ns and before.st_size==after.st_size})
    write(dest/'SNAPSHOT.json',{'cutoff_seconds':cutoff,'observed_elapsed_seconds':elapsed,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':records})
    taken.add(cutoff);print(name,cutoff,'snapshot',len(records),'files',flush=True)
  if len(taken)==len(cutoffs):done.add(name);del active[name]
 if (r/'launches_complete').exists() and not active and len(done)>0:break
 time.sleep(.1)
print('all snapshots complete',flush=True)
