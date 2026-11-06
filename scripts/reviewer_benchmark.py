"""Verified COI reference comparators, common input and paired-matching rules.
No inosine substitution; comparisons are descriptive on the archived library.
"""
from pathlib import Path
import csv,json,subprocess,shutil,collections,itertools
P=Path(__file__).resolve().parents[1];O=P/'results/reviewer_revision';D=O/'benchmark_COI';D.mkdir(exist_ok=True)
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));RC=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN')
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0].removeprefix('_R_');d[k]=''
  else:d[k]+=l.upper().strip()
 return d
bs=[r for r in json.loads((O/'literature_benchmarks.json').read_text())['benchmarks'] if r['status']=='verified_IUPAC_compatible'];rs=[r for r in json.loads((P/'results/catalog.json').read_text())['originals'] if r['gene']=='COI']+bs
for role in ['target','background']:shutil.copyfile(P/'data/COI'/f'{role}.fasta',D/f'{role}.fasta')
(D/'independent_primers.tsv').write_text(''.join('\t'.join([r['id'],r['F'],r['R']])+'\n' for r in rs));subprocess.run(['c++','-O3','-std=c++17',str(P/'scripts/scan.cpp'),'-o',str(D/'scan')],check=True)
with (D/'scan.log').open('w') as f:subprocess.run([str(D/'scan'),str(D)],stdout=f,stderr=f,check=True)
hs=collections.defaultdict(set)
for h in csv.DictReader((D/'independent_hits.tsv').open(),delimiter='\t'):
 for flag in ['exact','le2last3','le2','le3']:
  if h[flag]=='1':hs[h['name'],h['role'],h['model'],flag].add(h['accession'])
al=fasta(P/'legacy/v1.2/markers/12S_COI/COI/aligned.fasta');anchor=(P/'legacy/v1.2/markers/12S_COI/COI/anchor.txt').read_text().strip();cols=[i for i,b in enumerate(al[anchor]) if b!='-'];ref=''.join(al[anchor][i] for i in cols);raw=fasta(D/'target.fasta')
# Infer homologous coordinates from a unique lowest-mismatch pair on the fixed reference.
coords={};panels={}
original_coordinates={r['name']:r for r in csv.DictReader((P/'legacy/v1.2/markers/12S_COI/COI/pairs.csv').open())}
for r in rs:
 f=r['F'];z=r['R'].translate(RC)[::-1]
 def sites(q):return [(i,sum(b not in I[a] for a,b in zip(q,ref[i:i+len(q)]))) for i in range(len(ref)-len(q)+1)]
 if 'parent' in r:
  q=original_coordinates[r['parent']];i=int(q['F_start'])-1;j=int(q['R_start'])-1;score=sum(b not in I[a] for a,b in zip(f,ref[i:i+len(f)]))+sum(b not in I[a] for a,b in zip(z,ref[j:j+len(z)]))
 else:
  fs=sites(f);zs=sites(z);pairs=[(fm+rm,i,j) for i,fm in fs if fm<=8 for j,rm in zs if rm<=8 and j>=i+len(f) and 60<=j+len(z)-i<=650]
  assert pairs,r['id'];score=min(x[0] for x in pairs);best=[x for x in pairs if x[0]==score];assert len(best)==1,(r['id'],best)
  _,i,j=best[0]
 coords[r['id']]=(i,j,len(f),len(z),score)
 # Site completeness is assessed before matching and does not use assay success.
 panels[r['id']]={a for a in raw if a in al and all(al[a][cols[k]] in 'ACGT' for k in list(range(i,i+len(f)))+list(range(j,j+len(z))))}
common=set.intersection(*panels.values());summary=[]
for r in rs:
 key=r['id'];i,j,fl,rl,score=coords[key];cov=hs[key,'target','WC','le2last3'];exact=hs[key,'target','WC','exact'];panel=panels[key]
 summary.append(dict(id=key,F=r['F'],R=r['R'],reference_F_start=i+1,reference_R_end=j+rl,reference_mismatches=score,reference_total_bp=j+rl-i,archived_records=len(raw),site_complete_records=len(panel),complete_panel_covered=len(panel&cov),complete_panel_exact=len(panel&exact),common_panel_records=len(common),common_panel_covered=len(common&cov),common_panel_exact=len(common&exact),all_record_covered=len(cov),background_WC=len(hs[key,'background','WC','le2last3']),background_GT=len(hs[key,'background','GT','le2last3'])))
with (O/'COI_literature_comparison.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(summary[0]),lineterminator='\n');w.writeheader();w.writerows(summary)
(O/'COI_benchmark_panels.json').write_text(json.dumps(dict(anchor=anchor,common_panel=sorted(common),panels={k:sorted(v) for k,v in panels.items()},note='Homologous reference site completeness; contiguous raw paired scanning; marker lengths and design taxonomic scopes differ.'),indent=2)+'\n')
for role in ['target','background']:(D/f'{role}.fasta').unlink()
(D/'scan').unlink();print(json.dumps(summary,indent=2))
