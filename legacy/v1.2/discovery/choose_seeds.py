from pathlib import Path
import json,csv
p=Path(__file__).resolve().parent
sel=json.loads((p/'shortlist_fast.json').read_text());summary={r['name']:r for r in csv.DictReader((p/'target_summary.tsv').open(),delimiter='\t') if r['panel']=='common'};th={r['name']:r for r in csv.DictReader((p/'pair_thermodynamics.tsv').open(),delimiter='\t') if r['scenario']=='variant50nM'};chosen=[]
for group,label in [('mini','XS'),('short','S'),('medium','M'),('long','L')]:
 options=[]
 for s in sel:
  if s['group']!=group or s['WC_le3']>5 or s['GT_le2']>5:continue
  t=th[s['name']];structure=max(float(v) for k,v in t.items() if k.endswith(('_hairpin_max','_homodimer_max','_same_side_heterodimer_max')) or k=='FR_heterodimer_max')
  if structure>=55:continue
  options.append(s)
 if not options:raise RuntimeError('No acceptable seed for '+group)
 # Prefer coverage within the primary risk constraint; break ties by relaxed risk.
 s=min(options,key=lambda s:(-float(summary[s['name']]['le2last3_pct']),s['WC_le4'],s['WC_le3']+s['GT_le2']))
 chosen.append(dict(s,label='MiUrchin-'+label,target=summary[s['name']]))
(p/'final_selected.json').write_text(json.dumps(chosen,indent=2));print([(r['label'],r['left'],r['right'],r['target']['le2last3_pct'],r['WC_le3'],r['GT_le2'],r['WC_le4']) for r in chosen])
