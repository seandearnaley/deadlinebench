"""Bounded reproduction of the five already inspected blinded artifact sets."""
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import tempfile
import time

REPOSITORY = Path(__file__).resolve().parents[2]
BLINDED = REPOSITORY / 'live/blinded'
INPUT = REPOSITORY / 'tasks/deadlinebench_tasks/participant_inputs/data_01'
EVIDENCE = REPOSITORY / 'live/grading/reproduction'
KEY_DIR = REPOSITORY / 'tasks/deadlinebench_tasks/evaluator_only/data_01'
KEY = json.loads((KEY_DIR / 'answer_key.json').read_text())

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_FSIZE, (10 * 1024 * 1024, 10 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (128, 128))

WRAPPER = '''import runpy,sys\ndef deny(event,args):\n    if event.startswith("socket.") or event in ("subprocess.Popen", "os.system", "os.posix_spawn"):\n        raise RuntimeError("Reproduction denies network and subprocess execution")\nsys.addaudithook(deny)\nscript=sys.argv.pop(1)\nsys.argv[0]=script\nrunpy.run_path(script,run_name="__main__")\n'''

specs = [
    ('A', '90', 'analyze.py', ['input']),
    ('B', '60', 'analyze.py', ['input/ticket_export.csv', 'output/metrics.json']),
    ('C', '90', 'analysis.py', ['input/ticket_export.csv', 'output/metrics.json']),
    ('D', '90', 'analyze.py', ['input/ticket_export.csv', 'output/metrics.json']),
    ('E', '60', 'analyze.py', ['--input', 'input', '--output', 'output']),
    ('F', '60', 'analyze.py', ['input/ticket_export.csv', 'output/metrics.json']),
    ('G', '60', 'analyze.py', ['input/ticket_export.csv', 'output/metrics.json']),
]
results = []
for label, cutoff, filename, args in specs:
    if len(sys.argv) > 1 and label not in sys.argv[1:]:
        continue
    snapshot = BLINDED / label / cutoff
    before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot.iterdir() if p.is_file()}
    with tempfile.TemporaryDirectory(prefix='deadlinebench_grade_') as temporary:
        work = Path(temporary)
        shutil.copytree(INPUT, work / 'input')
        (work / 'output').mkdir()
        for p in snapshot.iterdir():
            if p.is_file() and p.name != 'SNAPSHOT.json':
                shutil.copy2(p, work / 'output' / p.name)
        source_before = {str(p.relative_to(work / 'input')): hashlib.sha256(p.read_bytes()).hexdigest() for p in (work / 'input').rglob('*') if p.is_file()}
        # Delete only the disposable copied metrics, to require reconstruction.
        (work / 'output' / 'metrics.json').unlink()
        (work / 'offline_runner.py').write_text(WRAPPER)
        command = [sys.executable, '-I', '-S', 'offline_runner.py', 'output/' + filename] + args
        started = time.monotonic()
        try:
            proc = subprocess.run(command, cwd=work, env={'PATH': os.environ.get('PATH', ''), 'PYTHONHASHSEED': '0'}, capture_output=True, text=True, timeout=15, preexec_fn=limits)
            record = {'label': label, 'representative_cutoff_seconds': int(cutoff), 'command': command, 'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr, 'elapsed_seconds': time.monotonic() - started, 'timed_out': False}
        except subprocess.TimeoutExpired as exc:
            record = {'label': label, 'representative_cutoff_seconds': int(cutoff), 'command': command, 'exit_code': None, 'stdout': exc.stdout.decode() if isinstance(exc.stdout, bytes) else exc.stdout or '', 'stderr': exc.stderr.decode() if isinstance(exc.stderr, bytes) else exc.stderr or '', 'elapsed_seconds': time.monotonic() - started, 'timed_out': True}
        generated = work / 'output' / 'metrics.json'
        if generated.exists():
            got = json.loads(generated.read_text())
            submitted = json.loads((snapshot / 'metrics.json').read_text())
            record['reconstructed_saved_json_semantic_equality'] = got == submitted
            record['generated_metrics_sha256'] = hashlib.sha256(generated.read_bytes()).hexdigest()
            mandatory = [('overall', k) for k in KEY['overall']]
            mandatory += [('by_queue', q, k) for q in KEY['by_queue'] for k in KEY['by_queue'][q]]
            mandatory += [('audit', k) for k in ('raw_rows','rows_at_or_after_cutoff','deduplicated_ids','test_ids_excluded','march_ids_excluded')]
            mismatch = []
            for path in mandatory:
                a, b = got, KEY
                for part in path:
                    a, b = a[part], b[part]
                if a != b:
                    mismatch.append({'path': '.'.join(path), 'got': a, 'expected': b})
            record['all_submitted_mandatory_figures_match_key'] = not mismatch
            record['mandatory_figure_mismatches'] = mismatch
        else:
            record['reconstructed_saved_json_semantic_equality'] = False
            record['all_submitted_mandatory_figures_match_key'] = False
        source_after = {str(p.relative_to(work / 'input')): hashlib.sha256(p.read_bytes()).hexdigest() for p in (work / 'input').rglob('*') if p.is_file()}
        record['disposable_input_unchanged'] = source_before == source_after
    after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot.iterdir() if p.is_file()}
    record['original_snapshot_unchanged'] = before == after
    record['actual_limits'] = {'wall_timeout_seconds': 15, 'cpu_soft_and_hard_seconds': 5, 'address_space_bytes': 268435456, 'file_size_bytes': 10485760, 'open_file_descriptors': 128, 'isolated_python': True, 'site_disabled': True, 'network_policy': 'Socket audit events and subprocess execution denied; inspected participant sources have no network calls.', 'packages_installed': False}
    (EVIDENCE / (label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
    results.append({k: v for k, v in record.items() if k not in ('stdout', 'stderr')})
all_records = []
for evidence_file in sorted(EVIDENCE.glob('[A-Z].json')):
    item = json.loads(evidence_file.read_text())
    all_records.append({k: v for k, v in item.items() if k not in ('stdout', 'stderr')})
(EVIDENCE / 'summary.json').write_text(json.dumps(all_records, indent=2) + '\n')
print(json.dumps(results, indent=2))
