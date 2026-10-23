from pathlib import Path
import json,csv,collections
p=Path(__file__).resolve().parent
ss=json.loads((p/'portfolio_selected.json').read_text());summary=list(csv.DictReader((p/'portfolio_summary.tsv').open(),delimiter='\t'));therm=list(csv.DictReader((p/'portfolio_thermodynamics.tsv').open(),delimiter='\t'));pairs=list(csv.DictReader((p/'pair_thermodynamics.tsv').open(),delimiter='\t'));passed=[];failed=[]
for s in ss:
 th=[r for r in pairs if r['name'] in s['allowed_pair_names']]
 maxstructure=max(float(v) for r in th for k,v in r.items() if k.endswith(('_hairpin_max','_homodimer_max','_same_side_heterodimer_max')) or k=='FR_heterodimer_max')
 if s['mode']=='pool':maxstructure=max(maxstructure,*[float(r['all_pool_dimer_max']) for r in therm if r['name']==s['name']])
 r=next(r for r in summary if r['name']==s['name']);ok=maxstructure<55 and int(r['WC_le3'])<=5 and int(r['GT_le2'])<=5
 (passed if ok else failed).append(dict(name=s['name'],max_structure_Tm=maxstructure))
assert not failed,failed
assert len(ss)==8 and json.loads((p/'independent_validation.json').read_text())['status']=='PASS'
(p/'final_validation.json').write_text(json.dumps(dict(status='PASS',schemes=8,passed=passed,failed=failed,scope='Frozen in-silico candidates; complete allowed-pair unions, both concentration-scenario structure gates and independent scan agreement',wet_lab_validated=False),indent=2));print('PASS all 8 portfolios: specificity and structure gates')
