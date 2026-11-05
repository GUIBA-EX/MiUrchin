from pathlib import Path
import csv,json,collections
from scan_core import database
p=Path(__file__).resolve().parent
assert (p/'background_screen_complete.json').exists()
db=database(p/'background.fasta');refs=db[3]
hits={f.stem:json.loads(f.read_text()) for f in (p/'background_hits').glob('*.json')}
def risk(F,R):
 out={}
 for model in ['WC','GT']:
  ff=hits[F]['hits'][model];rr=hits[R]['hits'][model];sets={k:set() for k in ['le2','le3','le4','ambiguous']}
  for rec in ff.keys()&rr.keys():
   for f,fm,f5,fa in ff[rec]:
    for r,rm,r5,ra in rr[rec]:
     if not 0<=r-f-len(hits[F]['sequence'])<=1000:continue
     keys=['ambiguous'] if fa or ra else [f'le{k}' for k in [2,3,4] if fm<=k and rm<=k]
     for k in keys:sets[k].update(refs[int(rec)]['accessions'])
  for k,v in sets.items():out[model+'_'+k]=len(v)
 return out
rows=list(csv.DictReader((p/'discovery_pairs.tsv').open(),delimiter='\t'));res=[]
for i,r in enumerate(rows):
 r.update(risk(r['F_id'],r['R_id']));r['strict_gate']=r['WC_le3']==0 and r['GT_le2']==0;res.append(r)
 if i%10000==0:print(i,'pairs',flush=True)
with (p/'screened_pairs.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(res[0]),delimiter='\t');w.writeheader();w.writerows(res)
selected=[]
for group in ['v4_local','short','medium','long']:
 rr=[r for r in res if (r['v4_local']=='True' if group=='v4_local' else r['band']==group)]
 rr.sort(key=lambda r:(not r['strict_gate'],r['WC_le3']+r['GT_le2'],r['WC_le4'],-float(r['coverage']),-float(r['exact']),int(r['degeneracy_sum'])))
 print(group,'pairs',len(rr),'strict_pass',sum(r['strict_gate'] for r in rr),'top',rr[:1],flush=True)
 chosen=[]
 for r in rr:
  if any(r['F']==s['F'] and r['R']==s['R'] for s in chosen):continue
  chosen.append(r)
  if len(chosen)>=6:break
 for j,r in enumerate(chosen,1):selected.append(dict(r,name=f'MC_{group}_{j}',group=group))
for b in json.loads((p/'baselines.json').read_text()):print('BASELINE',b['name'],risk(b['name']+'_F',b['name']+'_R'),flush=True)
(p/'shortlist.json').write_text(json.dumps(selected,indent=2))
