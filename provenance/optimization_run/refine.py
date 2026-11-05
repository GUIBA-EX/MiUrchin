import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):import optimize as o
# Reuses cached exact-variant structural calculations; optimize import repeats initial audit only.
import json,itertools,collections
from pathlib import Path
rows=json.load(open('work/candidates.json'));thermal=json.load(open('work/thermal.json'));extra=[]
@o.functools.lru_cache(None)
def oligo(q):
 vs=o.variants(q);tt=[o.single(s)[0] for s in vs];st=max(max(o.single(s)[1:]) for s in vs)
 for x,y in itertools.combinations(vs,2):st=max(st,o.het(x,y))
 return min(tt),max(tt),st
for r in rows:
 if r['clade']=='original':continue
 # Trim 5-prime only: last three bases never sacrificed to pass thermal gates.
 opts={}
 for side in ['F','R']:
  q=r[side];ls=[]
  for trim in range(min(7,len(q)-17)):
   s=q[trim:];v=oligo(s)
   if v[2]<45 and v[0]>=45 and v[1]<=75:ls.append((s,v,trim))
  opts[side]=ls
 best=None
 for f,fv,fi in opts['F']:
  for z,zv,zi in opts['R']:
   delta=abs((fv[0]+fv[1]-zv[0]-zv[1])/2)
   if delta>5:continue
   st=max(fv[2],zv[2],max(o.het(x,y) for x in o.variants(f) for y in o.variants(z)))
   if st>=45:continue
   score=(fi+zi,st,delta)
   if best is None or score<best[0]:best=(score,f,z,fv,zv,st,delta)
 if best and (best[1],best[2])!=(r['F'],r['R']):
  score,f,z,fv,zv,st,delta=best;n=dict(r,id=r['id']+'_trim',F=f,R=z);extra.append(n);thermal[n['id']]=dict(F_tm=list(fv[:2]),R_tm=list(zv[:2]),structure_max=st,delta_mid_tm=delta,pass_gate=True,deg_F=len(o.variants(f)),deg_R=len(o.variants(z)))
rows+=extra
Path('work/candidates.json').write_text(json.dumps(rows,indent=2));Path('work/thermal.json').write_text(json.dumps(thermal,indent=2))
for gene in ['16S','12S','COI','28S']:
 d=Path('work/refined')/gene;d.mkdir(parents=True,exist_ok=True)
 for role in ['target','background']:o.shutil.copyfile(Path('work/validation')/gene/(role+'.fasta'),d/(role+'.fasta'))
 (d/'independent_primers.tsv').write_text('\n'.join('\t'.join([r['id'],r['F'],r['R']]) for r in extra if r['gene']==gene)+'\n')
print('Additional passing trimmed candidates:',len(extra),flush=True)
