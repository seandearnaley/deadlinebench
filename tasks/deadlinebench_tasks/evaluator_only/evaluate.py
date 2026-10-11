"""Small dispatcher: python evaluate.py TASK_ID SNAPSHOT_OUTPUT_DIRECTORY"""
import json,subprocess,sys
from pathlib import Path
base=Path(__file__).resolve().parent
task,output=sys.argv[1:3]
if task not in ['research_01','research_02','data_01','data_02','code_01','code_02']:
    raise SystemExit('Unknown task ID')
check=base/task/'checks.py';output=Path(output).resolve()
if not check.exists():
    print(json.dumps({'task':task,'automated_score':None,'human_rubric':str(base/task/'rubric.md'),'saved_report':(output/'report.md').exists()}));raise SystemExit(0)
try:
    result=subprocess.run([sys.executable,str(check),str(output)],capture_output=True,text=True,timeout=15,cwd=output.parent)
    print(result.stdout.strip() or json.dumps({'task':task,'error':result.stderr.strip(),'returncode':result.returncode}))
except (subprocess.TimeoutExpired,OSError) as exc:
    print(json.dumps({'task':task,'error':type(exc).__name__,'detail':str(exc),'automated_score':None}))
