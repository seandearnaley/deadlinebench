"""Serialize this bounded artifact-only human grading decision; no new tests."""
from pathlib import Path
import copy, hashlib, json, subprocess
from datetime import datetime, timezone

REPOSITORY=Path(__file__).resolve().parents[2]
ROOT=REPOSITORY/'live/blinded'
OUT=REPOSITORY/'live/grading'
EVAL=REPOSITORY/'tasks/deadlinebench_tasks/evaluator_only/data_01'
INPUT=REPOSITORY/'tasks/deadlinebench_tasks/participant_inputs/data_01'
MAXIMA={'M1':30,'M2':25,'M3':15,'O1':10,'O2':10,'O3':10}
REP={'A':90,'B':60,'C':90,'D':90,'E':60,'F':60,'G':60}
EVIDENCE={
'A':{
 'M1':[{'file':'report.md','lines':'5-9','text':'420 tickets; 206 breaches (49.05%); 58 unanswered; 172 unresolved; median 4.23 among 362 responded; all qualifying April denominator; 1/4/12 elapsed-hour priority SLAs, strict greater-than, unanswered age to instant.'},{'file':'analyze.py','lines':'24-41,47-56','text':'Creation-to-first-reply or cutoff; responded-only median; unanswered nonblank test; unresolved retained status != resolved; April arrival filtering.'}],
 'M2':[{'file':'report.md','lines':'3,11-19,44-46','text':'Technical 2, Billing 0, Account 0; available specialist can cover both whole shifts. Queue counts/rates are correct. Technical largest risk; Billing coverage opportunity cost; Account unresolved count is not first-response risk. No tickets-per-shift forecast; incident fix uncertainty; log arrivals, priority and actual shift hours, matured-cohort same-definition check and spillover.'}],
 'M3':[{'file':'report.md','lines':'30,42-46','text':'670 raw -> exclude 11 cutoff rows -> 576 latest eligible IDs -> exclude 16 tests -> 140 March -> 420 April. Recent unanswered tickets have less time to exceed SLA; explicit as-of instant; staffing causality cannot be established and incident disappearance cannot be assumed.'}],
 'O1':[{'file':'report.md','lines':'23-30','text':'83/57.83%; 115/44.35%; 90/51.11%; 132/46.21%. Rates fluctuate; final bucket nine days and recent tickets less mature.'}],
 'O2':[{'file':'report.md','lines':'32-38','text':'Enterprise 85/51.76%; Small business 158/47.47%; Consumer 177/49.15%. Only 4.29 percentage-point spread; queue/priority mix prevents segment-effect conclusion.'}],
 'O3':[{'file':'report.md','lines':'48','text':'python output/analyze.py input'},{'file':'analyze.py','lines':'3-91','text':'Standard-library script, correct semantics; disposable reconstruction exactly equals saved metrics JSON.'}]},
'B':{
 'M1':[{'file':'report.md','lines':'2,10,18,21','text':'All six correct values, April arrivals as of 2026-05-01 00:00 UTC, all-ticket denominator, strict elapsed 1/4/12-hour SLA including overdue unanswered, responded-only median and retained unresolved-status definition.'}],
 'M2':[{'file':'report.md','lines':'5-7,12-18,42','text':'Exactly two indivisible Technical specialist shifts, correct three-queue comparison, real largest Technical burden, explicit Billing/Account trade-off, unmeasured shift productivity and incident attribution, priority/arrival-mix post-trial check.'}],
 'M3':[{'file':'report.md','lines':'21,31,42-44','text':'All five audit counts and correct order; pre-cutoff filtering prevents historical-state replacement. Recent unanswered arrivals have less time to breach. Observational comparison cannot prove causation; fix effect not established at line 5.'}],
 'O1':[{'file':'report.md','lines':'24-31','text':'All four correct April-arrival weekly counts/rates; unequal final bucket and unequal-age/mix caution.'}],
 'O2':[{'file':'report.md','lines':'33-39','text':'All three correct segment counts/rates; Enterprise highest rate and Consumer largest breach count; priority/queue mix and no segment-effect inference.'}],
 'O3':[{'file':'report.md','lines':'46','text':'python3 output/analyze.py input/ticket_export.csv output/metrics.json'},{'file':'analyze.py','lines':'2-26','text':'Standard-library script, correct cleaning and metric semantics; full saved JSON reproduced exactly.'}]},
'C':{
 'M1':[{'file':'report.md','lines':'5-9,36','text':'All six correct values and required April-arrival/all-ticket SLA/overdue-unanswered/responded-only median definitions; unresolved status definition explicit.'}],
 'M2':[{'file':'report.md','lines':'3,11-19,38-40','text':'Exactly two whole Technical shifts covered by specialist, all three queues correctly compared, true high Technical risk, feasible Billing alternative and Account trade-off, no clearance estimate, incident uncertainty and priority/age-adjusted post-trial check.'}],
 'M3':[{'file':'report.md','lines':'30,36-40','text':'670 -> exclude 11 -> 576 retained IDs -> exclude 16 tests -> 140 March; April 1 inclusive/May 1 exclusive. Recent unanswered tickets may breach later. Observational snapshot cannot establish staffing causes, incident window cannot establish fix effect (line 17).'}],
 'O1':[{'file':'report.md','lines':'23-30','text':'All four correct weekly counts/rates; fluctuation, nine-day bucket, and maturation caution.'}],
 'O2':[{'file':'report.md','lines':'32','text':'All three correct segment counts/rates, Enterprise slightly highest rate and Consumer largest breach count; mix caution and no segment effect.'}],
 'O3':[{'file':'report.md','lines':'42','text':'python3 output/analysis.py input/ticket_export.csv output/metrics.json'},{'file':'analysis.py','lines':'5-92','text':'Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.'}]},
'D':{
 'M1':[{'file':'report.md','lines':'5-7,21,23','text':'All six correct values and definitions: April arrivals, all-ticket denominator, strict elapsed priority SLA with unanswered-to-cutoff, responded-only median and unresolved status.'}],
 'M2':[{'file':'report.md','lines':'3,9-17,46','text':'Both whole shifts to Technical specialist; correct queue facts, measured largest risk, Billing/Account trade-off, capacity/incident and May-demand uncertainty, log shifts/arrivals/priority and matured same-definition queue comparison.'}],
 'M3':[{'file':'report.md','lines':'23,34,46','text':'All five audit counts with cutoff-before-dedup-before-tests/cohort order. Newer arrivals less time to exceed SLA; exact April/as-of boundaries; no incident-fix or trial causal proof.'}],
 'O1':[{'file':'report.md','lines':'27-34','text':'All correct weekly counts/rates; no steady downward trend, nine-day final period and unequal-age caution.'}],
 'O2':[{'file':'report.md','lines':'36-42','text':'All correct segment counts/rates; Enterprise highest rate, narrow range and unknown queue/priority mix do not establish segment cause.'}],
 'O3':[{'file':'report.md','lines':'48','text':'python3 output/analyze.py input/ticket_export.csv output/metrics.json'},{'file':'analyze.py','lines':'2-93','text':'Standard-library correct reconstruction; full saved JSON reproduced exactly.'}]},
'E':{
 'M1':[{'file':'metrics.json','json_paths':['overall.tickets','overall.breached','overall.breach_rate_pct','overall.median_first_response_hours','overall.unanswered','overall.unresolved'],'text':'420, 206, 49.05, 4.23, 58, 172 exactly correct.'},{'file':'analyze.py','lines':'8,10-20','text':'Saved executable definitions: April start<=created<cutoff; priority 1/4/12 elapsed hours; reply or cutoff age strictly > target; rate over len(rows); median only nonblank first replies; unanswered blank and unresolved status != resolved.'}],
 'M2':[{'file':'metrics.json','json_paths':['by_queue.Billing','by_queue.Technical','by_queue.Account'],'text':'All 12 required queue facts correct. No allocation, risk justification, trade-off, staffing/source caution, or trial check exists in either saved file.'}],
 'M3':[{'file':'metrics.json','json_paths':['audit'],'text':'670 raw, 11 cutoff rows, 576 deduplicated IDs, 16 excluded tests, 140 excluded March IDs.'},{'file':'analyze.py','lines':'8-15,21','text':'Evaluation instant and April boundaries explicit; cutoff -> latest remaining ID -> exclude tests -> April cohort. No specific snapshot/unequal-age limitation or observational staffing/incident caution saved.'}],
 'O1':[{'file':'metrics.json','json_paths':['weekly'],'text':'All eight requested weekly count/rate values correct; no cautious interpretation saved.'}],
 'O2':[{'file':'metrics.json','json_paths':['by_segment'],'text':'All six requested segment count/rate values correct; no useful comparative observation or mix/causality caution saved.'}],
 'O3':[{'file':'analyze.py','lines':'1-25','text':'Correct standard-library reconstruction; full saved JSON reproduced exactly. argparse flags/defaults exist, but no authored one-line run instruction is saved. The evaluator run command is not participant credit.'}]},
'F':{
 'M1':[{'file':'report.md','lines':'7-9,27','text':'All six correct values and exact April/as-of definitions, all-ticket rate denominator, strict elapsed priority SLA with overdue unanswered, responded-only median and unresolved status.'}],
 'M2':[{'file':'report.md','lines':'3,13-23','text':'Exactly two whole Technical specialist shifts; correct queue facts, largest measured Technical risk, Billing/Account opportunity costs, feasible Billing generalist alternative; incident/productivity uncertainty; equal-follow-up priority-specific trial rates and arrivals check.'}],
 'M3':[{'file':'report.md','lines':'23,27,38,42','text':'All five audit counts in correct order; explicit cutoff/April boundaries. Equal follow-up and recent-ticket exposure limitations; observational comparison cannot isolate staffing effects; incident disappearance not assumed.'}],
 'O1':[{'file':'report.md','lines':'31-38','text':'All four correct weekly counts/rates; fluctuation, unequal final bucket and exposure caution.'}],
 'O2':[{'file':'report.md','lines':'40','text':'All three correct segment counts/rates; rates fairly close, Consumer most breaches, no causal interpretation and queue/priority mix caution.'}],
 'O3':[{'file':'report.md','lines':'44-46','text':'python3 output/analyze.py input/ticket_export.csv output/metrics.json'},{'file':'analyze.py','lines':'2-56','text':'Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.'}]},
'G':{
 'M1':[{'file':'report.md','lines':'8-17,34','text':'All six correct values and April/as-of boundaries; all-ticket denominator, strict 1/4/12 elapsed-hour SLA including unanswered cutoff age, responded-only median, unresolved retained-status definition.'}],
 'M2':[{'file':'report.md','lines':'4-6,10-17,36-38','text':'Exactly two whole Technical specialist shifts, all correct queue facts, real first-response-risk justification; Billing/Account and feasible generalist alternatives; unmeasured shift productivity, incident uncertainty; priority-stratified new-arrival trial check with volume and other queues.'}],
 'M3':[{'file':'report.md','lines':'28,34-38','text':'All five audit counts with cutoff-before-dedup-before-test/April order, explicit evaluation instant; recent arrivals less mature; cannot prove staffing caused breaches and fix-straddling window cannot establish its effect (line 4).'}],
 'O1':[{'file':'report.md','lines':'21-28','text':'All four correct weekly counts/rates; no steady improvement, final nine-day bucket and exposure caution.'}],
 'O2':[{'file':'report.md','lines':'30','text':'All three correct segment counts/rates; Enterprise highest rate, modest differences, mix caution and no segment-effect inference.'}],
 'O3':[{'file':'report.md','lines':'40','text':'python3 output/analyze.py input/ticket_export.csv output/metrics.json'},{'file':'analyze.py','lines':'3-55','text':'Correct standard-library supplied-input reconstruction; full saved JSON reproduced exactly.'}]},
}

def subitems(label):
    m1={'tickets':5,'breached':5,'breach_rate_pct':5,'responded_only_median':5,'unanswered':5,'unresolved':5}
    m2={'queue_facts':12,'exactly_two_whole_shifts':2,'real_risk_priority':3,'other_queues_tradeoff':2,'capacity_incident_uncertainty':2,'feasible_specialist_generalist':2,'concrete_post_trial_check':2}
    m3={'audit_counts_and_order':5,'as_of_unequal_age_limitation':4,'observational_causality_caution':4,'april_cohort_and_instant':2}
    o1={'weekly_ticket_counts_and_rates':8,'cautious_interpretation':2}
    o2={'segment_ticket_counts_and_rates':6,'useful_comparison':2,'mix_caution_or_noncausal_observation':2}
    o3={'reconstructs_submitted_mandatory_figures':6,'cleaning_metric_semantics':2,'valid_saved_run_instruction':2}
    if label=='E':
        m2={k:(12 if k=='queue_facts' else 0) for k in m2}
        m3['as_of_unequal_age_limitation']=0; m3['observational_causality_caution']=0
        o1['cautious_interpretation']=0
        o2['useful_comparison']=0; o2['mix_caution_or_noncausal_observation']=0
        o3['valid_saved_run_instruction']=0
    return {'M1':m1,'M2':m2,'M3':m3,'O1':o1,'O2':o2,'O3':o3}

unique=[]
for label,cutoff in REP.items():
    d=ROOT/label/str(cutoff)
    artifacts={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(d.iterdir()) if p.is_file() and p.name!='SNAPSHOT.json'}
    signature=hashlib.sha256(json.dumps({k:v['sha256'] for k,v in artifacts.items()},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    checker=json.loads(subprocess.run(['python3','-I','-S',str(EVAL/'checks.py'),str(d)],capture_output=True,text=True,check=True,timeout=10).stdout)
    (OUT/'reproduction'/f'{label}_numeric_checker.json').write_text(json.dumps(checker,indent=2)+'\n')
    parts=subitems(label)
    breakdown={k:{'score':sum(v.values()),'max':MAXIMA[k],'subitems':v,'evidence':EVIDENCE[label][k]} for k,v in parts.items()}
    core={'M1':True,'M2':label!='E','M3':label!='E','aggregate':label!='E'}
    core_reasons={'M1':'All values and definitions are correct in saved report and/or code.','M2':'All queue facts plus exactly two feasible whole shifts justified by true risk.','M3':'All audit counts/order, specific unequal-age limitation and clear staffing/incident noncausal caution.'}
    if label=='E':
        core_reasons['M1']='Pass: six exact values; saved code states correct April-arrival, strict elapsed priority SLA including overdue unanswered, and responded-only median definitions.'
        core_reasons['M2']='Fail: all queue facts correct, but no saved exactly-two-shift allocation or true-risk justification.'
        core_reasons['M3']='Fail: audit counts/order are correct, but no saved specific as-of/unequal-age limitation and no staffing/incident observational-causality caution.'
    report=d/'report.md'
    word_count=len(report.read_text().split()) if report.exists() else None
    reproduction=json.loads((OUT/'reproduction'/f'{label}.json').read_text())
    unique.append({'label':label,'representative_cutoff_seconds':cutoff,'artifact_hashset_sha256':signature,'artifacts':artifacts,'weighted_score':sum(p['score'] for p in breakdown.values()),'weighted_max':100,'mandatory_score':sum(breakdown[k]['score'] for k in ('M1','M2','M3')),'mandatory_max':70,'optional_score':sum(breakdown[k]['score'] for k in ('O1','O2','O3')),'optional_max':30,'rubric_breakdown':breakdown,'usable_core':core,'usable_core_reasons':core_reasons,'mandatory_items_complete':{'M1':True,'M2':label!='E','M3':label!='E'},'report':{'present':report.exists(),'word_count_method':'len(report_text.split()), conservative whitespace tokens including Markdown table tokens','word_count':word_count,'at_most_700_words':word_count<=700 if word_count is not None else None,'required_report_missing':not report.exists()},'numeric_checker':{'score':checker['numeric_points'],'max':checker['numeric_max'],'all_checks_ok':all(x['ok'] for x in checker['checks']),'evidence_file':f'reproduction/{label}_numeric_checker.json','interpretation':'Numeric evidence only, not complete grade.'},'reproduction':{k:v for k,v in reproduction.items() if k not in ('stdout','stderr')},'confidence':'high' if label!='E' else 'medium-high','confidence_note':'Direct saved evidence and exact disposable reconstruction.' if label!='E' else 'Omissions and numeric accuracy are certain; scoring explicitly credits correct saved executable definitions under artifact-anywhere rule, while requiring actual authored recommendations/cautions/interpretations and a saved run instruction.'})

by_label={x['label']:x for x in unique}
snapshots=[]
for manifest in sorted(ROOT.glob('*/*/SNAPSHOT.json'),key=lambda p:(p.parent.parent.name,int(p.parent.name))):
    label=manifest.parent.parent.name
    if label not in REP: continue
    m=json.loads(manifest.read_text()); d=manifest.parent
    actual={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in d.iterdir() if p.is_file() and p.name!='SNAPSHOT.json'}
    signature=hashlib.sha256(json.dumps(actual,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert signature==by_label[label]['artifact_hashset_sha256'], (label,d.name,'unexpected nondeduplicable snapshot')
    assert {f['file']:f['sha256'] for f in m['files']}==actual, (label,d.name,'manifest mismatch')
    snapshots.append({'label':label,'cutoff_seconds':m['cutoff_seconds'],'observed_elapsed_seconds':m['observed_elapsed_seconds'],'snapshot_utc':m['utc'],'artifact_hashset_sha256':signature,'all_manifest_files_stable_during_read':all(f['stable_during_read'] for f in m['files']),'manifest_hashes_match_actual_artifacts':True,'graded_unique_set':label,'deduplicated_to_representative_cutoff_seconds':REP[label],'weighted_score':by_label[label]['weighted_score'],'rubric_breakdown':{k:v['score'] for k,v in by_label[label]['rubric_breakdown'].items()},'usable_core':by_label[label]['usable_core'],'core_reasons':by_label[label]['usable_core_reasons'],'report_word_count':by_label[label]['report']['word_count'],'confidence':by_label[label]['confidence']})

method={'scope':'Seven distinct blinded saved artifact sets across 13 nominated snapshots; only frozen input pack, locked rubric/key/checker, and saved snapshots used as scoring evidence. No later report credit. No model ranking or causal treatment inference.','rubric_version':'data_01 version 1.0','code_as_definition_policy':'Correct saved executable formulas count as explicit definition/method evidence under “grade content wherever saved.” This is applied consistently to all sets; it does not create prose recommendation, caution, interpretation, or run-instruction credit.','missing_report_policy':'No global missing-report penalty beyond the rubric. Missing report is separately flagged and missing content earns zero only for its sub-item.','deduplication':'Hashset over artifact filenames and SHA-256 content digests; SNAPSHOT.json metadata excluded. A/C/D identical within label at 90/180/300. No unique artifact set rerun solely for later cutoff.','reproduction':'Inspected every participant script before execution. Copied supplied input and saved output into disposable /tmp workspaces, removed only copied metrics, reconstructed once per unique hashset. No original snapshot/output writes. No packages installed or network/paid calls.','actual_reproduction_limits':unique[0]['reproduction']['actual_limits'],'run_scope_limitations':'Only supplied-data reconstruction, not adversarial or broader generalization tests. C counts all pre-April production IDs as March; F tests month==3 without year. Both are correct on supplied data, which contains March/April 2026 only; no unrequested robustness penalty. All seven scripts exited 0 and reconstructed the full saved JSON exactly.','blinding_limitation':'Condition mapping, original-run directories, original-thread files and condition-label files were not opened. One incidental internal live-agent listing exposed generic completed-run summaries without a blinded-label mapping. This weakens strict process blinding; those summaries were not used as grading evidence. No further agent listings were made.','confidence':'High for direct artifact facts, numeric checks, file presence, and supplied-input reconstruction. Medium-high for E’s weighted/core M1 interpretation because its definitions are saved as executable formulas rather than a brief.'}
result={'graded_at_utc':datetime.now(timezone.utc).isoformat(),'status':'complete','method':method,'locked_source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in EVAL.iterdir() if p.is_file()},'input_source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUT.iterdir() if p.is_file()},'unique_artifact_sets':unique,'per_label_cutoff':snapshots}
(OUT/'scores.json').write_text(json.dumps(result,indent=2)+'\n')

lines=['# Deadline screening: blinded artifact grading','', '## Results','', 'Weighted rubric score and usable core are separate. Numeric checker: **61/61 for all seven sets**, which is evidence, not the final grade.','', '| Label | Cutoff (s) | M1 /30 | M2 /25 | M3 /15 | O1 /10 | O2 /10 | O3 /10 | Total /100 | Core M1/M2/M3 | Usable core |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|']
for s in snapshots:
    b=s['rubric_breakdown']; c=s['usable_core']
    lines.append('| '+s['label']+' | '+str(s['cutoff_seconds'])+' | '+' | '.join(str(b[k]) for k in MAXIMA)+' | '+str(s['weighted_score'])+' | '+' / '.join('pass' if c[k] else 'fail' for k in ('M1','M2','M3'))+' | '+('true' if c['aggregate'] else 'false')+' |')
lines+=['','A/C/D cutoff rows repeat the same within-label artifact hashes. They are not independent executions or improvements. B/E/F/G have only 60-second snapshots. All observed freezes were between nominal cutoff +0.0066 and +0.0790 seconds; hashes match manifests and all artifacts were reported stable during copying.','', '## Method and limits','',method['scope'],'',method['code_as_definition_policy'],'',method['missing_report_policy'],'',method['reproduction'],'', 'Actual enforced limits per participant reproduction: 15-second wall timeout, 5-second CPU soft/hard limits, 256 MiB address space, 10 MiB file size, 128 open descriptors. Python ran with -I -S. An audit hook denied socket events and subprocess/system execution; inspected participant scripts had no network operations. All runs exited 0, in 0.036–0.046 seconds wall time, without timeouts. Copied input and original snapshots remained unchanged. Full saved JSON equality, not merely correct mandatory counts, was established.','',method['run_scope_limitations'],'', '**Blinding limitation:** '+method['blinding_limitation'],'', 'No model ranking, deadline-treatment causality, or population-wide performance claim is supported by this grading.','', '## Report length','', 'Conservative whitespace token counts include Markdown table syntax and are still below 700: A 676, B 643, C 644, D 666, F 646, G 636. E has no report; its word count is unavailable, not zero.','', '## Exact evidence and sub-item decisions','']
for u in unique:
    label=u['label']; d=f'../blinded/{label}/{REP[label]}'
    lines += [f'### {label}: {u["weighted_score"]}/100; usable core {str(u["usable_core"]["aggregate"]).lower()}','',f'Applies to cutoff(s): '+', '.join(str(s['cutoff_seconds']) for s in snapshots if s['label']==label)+f' seconds. Confidence: {u["confidence"]}.','']
    for category in MAXIMA:
        b=u['rubric_breakdown'][category]
        lines += [f'**{category}: {b["score"]}/{b["max"]}.** '+ '; '.join(k.replace('_',' ')+': '+str(v) for k,v in b['subitems'].items())+'.']
        for evidence in b['evidence']:
            where=f'{d}/{evidence["file"]}'
            suffix=' lines '+evidence['lines'] if 'lines' in evidence else ' JSON '+', '.join(evidence['json_paths'])
            lines.append(f'- `{where}`{suffix}: {evidence["text"]}')
        lines.append('')
    lines += ['Core reasons:']+[f'- {k}: {u["usable_core_reasons"][k]}' for k in ('M1','M2','M3')]+['',f'Reproduction evidence: `reproduction/{label}.json`; deterministic numeric detail: `reproduction/{label}_numeric_checker.json`.','']
lines+=['## Interpretation','', 'Six unique artifact sets are fully correct and decision-ready under this task’s locked rubric. E is numerically complete and reproducible but is not a usable core decision brief at the saved cutoff: it lacks allocation/risk justification and material snapshot/causality cautions. Missing E report content was not reconstructed from later work. Its 71 points consist of M1 30, queue facts 12, audit/order plus explicit cohort/instant 7, weekly figures 8, segment figures 6, and reproduction/semantics 8.','', 'Artifact digests, all per-cutoff metadata, rubric sub-item scores, three individual core booleans and their aggregate AND, exact evidence, and actual run limits are in `scores.json`. This bounded grading is complete; no additional case generation or tests were performed.']
(OUT/'REPORT.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'status':'complete','snapshots':len(snapshots),'unique_artifact_sets':len(unique),'scores':{u['label']:u['weighted_score'] for u in unique},'usable_core':{u['label']:u['usable_core'] for u in unique},'report':str(OUT/'REPORT.md'),'scores_json':str(OUT/'scores.json')},indent=2))
