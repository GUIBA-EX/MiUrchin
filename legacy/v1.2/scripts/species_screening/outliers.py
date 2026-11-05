from pathlib import Path
import csv,collections,sys
from Bio import SeqIO
import numpy as np
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');short=sys.argv[1];project={'miurchin':'MiUrchin'}[short];p=root/'work'/f'{short}_species_qc';out=root/'outputs'/f'{project}_species_qc';repo=root/'outputs'/project;ref='NC_001453.1';seq={x.id:str(x.seq).upper() for x in SeqIO.parse(p/'target_aligned.fasta','fasta')};cols=[i for i,c in enumerate(seq[ref]) if c!='-'];co={x['name']:x for x in csv.DictReader((repo/'results/current/binding_positions.csv').open())};regs=['S','M','L','XL'];starts=[int(co[x if x=='XS' else x+'D']['F_start']) for x in regs];ends=[int(co[x if x=='XS' else x+'D']['R_end']) for x in regs];first,last=cols[min(starts)-1],cols[max(ends)-1];panel=list(csv.DictReader((out/'panel.csv').open()));mat=np.array([list(seq[x['accession']][first:last+1]) for x in panel]);valid=np.isin(mat,list('ACGT'));rows=[]
for i,x in enumerate(panel):
 genus=x['organism'].split()[0];res=[]
 for j,y in enumerate(panel):
  if j==i or y['organism'].split()[0]!=genus:continue
  mask=valid[i]&valid[j];overlap=int(mask.sum())
  if overlap>=100:res.append((float((mat[i,mask]==mat[j,mask]).mean()),overlap,y['accession'],y['organism']))
 if res:
  a=max(res);rows.append(dict(accession=x['accession'],organism=x['organism'],order=x['order'],closest_congener=a[3],other_accession=a[2],overlap=a[1],identity=round(a[0],6),review=int(a[0]<.8)))
 else:rows.append(dict(accession=x['accession'],organism=x['organism'],order=x['order'],closest_congener='',other_accession='',overlap=0,identity='',review='not_evaluable'))
with (out/'congener_outlier_review.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(project,'review flags',[(r['organism'],r['identity'],r['overlap'],r['closest_congener']) for r in rows if r['review']==1],flush=True)
