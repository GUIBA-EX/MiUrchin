from pathlib import Path
import json,sys,itertools,functools,math
import numpy as np
from Bio.Data.IUPACData import ambiguous_dna_values as I
p=Path(__file__).resolve().parent;root=p.parents[1];sys.path.insert(0,str(root/'work/micucumber_mifish/deps'));import primer3
rr=json.loads((p/'combined_pool.json').read_text());panel=json.loads((root/'work/miurchin_mifish/panel.json').read_text());w=np.array([x['weight'] for x in panel]);w/=w.sum()
# Include the previously screened shifted-window ordinary candidates with their original state vectors.
old=json.loads((root/'work/miurchin_mifish/specific/feasible.json').read_text());states=json.loads((root/'work/miurchin_mifish/specific/oligo_states.json').read_text())
for r in old:

 rr.append(dict(r,source='mifish_shifted',degeneracy_F=1,degeneracy_R=1,cv=(np.array(states[r['F_id']]['coverage'])&states[r['R_id']]['coverage']).tolist(),ex=(np.array(states[r['F_id']]['exact'])&states[r['R_id']]['exact']).tolist()))
kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6)
@functools.lru_cache(None)
def expand(q):return list(map(''.join,itertools.product(*(I[c] for c in q))))
@functools.lru_cache(None)
def single(q,c):return primer3.calc_tm(q,dna_conc=c,**kw),max(primer3.calc_hairpin(q,dna_conc=c,**kw).tm,primer3.calc_homodimer(q,dna_conc=c,**kw).tm)
@functools.lru_cache(None)
def hetero(a,b,c):return primer3.calc_heterodimer(a,b,dna_conc=c,**kw).tm
@functools.lru_cache(None)
def thermal(F,R):
 fs,rs=expand(F),expand(R);maxst=-100;report=[]
 for scenario in ['50_per_variant','200_per_direction']:
  fc=50 if scenario=='50_per_variant' else 200/len(fs);rc=50 if scenario=='50_per_variant' else 200/len(rs);ft=[single(q,fc) for q in fs];rt=[single(q,rc) for q in rs]
  st=max(v[1] for v in ft+rt)
  for a,b in itertools.combinations(fs,2):st=max(st,hetero(a,b,fc))
  for a,b in itertools.combinations(rs,2):st=max(st,hetero(a,b,rc))
  for a,b in itertools.product(fs,rs):st=max(st,hetero(a,b,max(fc,rc)))
  report.append(dict(scenario=scenario,F_tm_min=min(x[0] for x in ft),F_tm_max=max(x[0] for x in ft),R_tm_min=min(x[0] for x in rt),R_tm_max=max(x[0] for x in rt),structure_max=st));maxst=max(maxst,st)
 return maxst<55 and all(abs((t["F_tm_min"]+t["F_tm_max"]-t["R_tm_min"]-t["R_tm_max"])/2)<=5 for t in report),report
@functools.lru_cache(None)
def terminal_ok(q):
 for s in expand(q):
  if len(set(s[-3:]))==1 or not any(c in "GC" for c in s[-3:]) or any(c*5 in s for c in "ACGT"):return False
  if not 1<=sum(c in 'GC' for c in s[-5:])<=4:return False
 return True
rr=[r for r in rr if terminal_ok(r['F']) and terminal_ok(r['R'])]

import csv
from collections import defaultdict
ol={src:{x['id']:x for x in json.loads((root/'work/miurchin'/src/'oligos.json').read_text())} for src in ['same_locus','same_locus_common_panel']}
ol['terminal_adjustment']={x['id']:x for x in json.loads((p/'extended_oligos.json').read_text())}
sh={x['name']:x for x in csv.DictReader((root/'work/miurchin_mifish/specific/oligos.csv').open())}
def locus(r):
 coords=[]
 for side in ['F','R']:
  m=(sh if r['source']=='mifish_shifted' else ol[r['source']])[r[side+'_id']]
  coords.extend((int(m['start']),int(m['end'])) if r['source']=='mifish_shifted' else (m['left']+1,m['right']))
 return tuple(coords)
feasible=rr+json.loads((p/"joint_extra_feasible.json").read_text())

def metrics(pp):
 wc=set().union(*(set(x['WC3']) for x in pp));gt=set().union(*(set(x['GT2']) for x in pp))
 if len(wc)>5 or len(gt)>5:return None
 c=float(w@np.logical_or.reduce([x['cv'] for x in pp]));e=float(w@np.logical_or.reduce([x['ex'] for x in pp]))
 return (round(c+e,12),round(c,12),round(e,12),-sum(x['degeneracy_F']+x['degeneracy_R'] for x in pp),-len(wc)-len(gt))
selected=[];audit=[];joint=[]
for reg in ['S','M','L','XL']:
 groups=defaultdict(dict)
 for r in feasible:
  if not terminal_ok(r["F"]) or not terminal_ok(r["R"]):continue
  if r['region']==reg:groups[locus(r)].setdefault((r['F'],r['R']),r)
 groups={k:list(v.values()) for k,v in groups.items()};rejected=set();thermal_rejections=0
 while True:
  options=[]
  for loc,g in groups.items():
   g=[r for r in g if (r['F'],r['R']) not in rejected];ordinary=[r for r in g if r['degeneracy_F']*r['degeneracy_R']==1];degen=[r for r in g if r['degeneracy_F']*r['degeneracy_R']>1]
   if len(ordinary)<2 or not degen:continue
   one=max(ordinary,key=lambda r:metrics([r]));d=max(degen,key=lambda r:metrics([r]));ab=None;best=None
   for pp in itertools.combinations(ordinary,2):
    score=metrics(pp)
    if score is not None and (best is None or score>best):ab=pp;best=score
   if ab is None:continue
   m=[metrics([d]),metrics([one]),best]
   # Equal weight for degenerate single, ordinary single and ordinary A/B performance.
   score=(round(sum(x[0] for x in m)/3,12),round(sum(x[1] for x in m)/3,12),round(sum(x[2] for x in m)/3,12),sum(x[3] for x in m),sum(x[4] for x in m))
   options.append((score,loc,d,one,ab,m))
  if not options:raise RuntimeError((reg,'no common locus supports D, ordinary and two distinct ordinary variants'))
  options.sort(key=lambda x:x[0],reverse=True);score,loc,d,one,ab,m=options[0];bad=[r for r in [d,one,*ab] if not thermal(r['F'],r['R'])[0]]
  if not bad:break
  rejected.update((r['F'],r['R']) for r in bad);thermal_rejections+=len(bad)
 for chem,pp,ms in [('degenerate',[d],m[0]),('ordinary',[one],m[1]),('ordinary',ab,m[2])]:
  count=len(pp);scheme=reg+'D' if chem=='degenerate' else reg if count==1 else reg+'A+'+reg+'B'
  for i,r in enumerate(pp):selected.append(dict(r,scheme=scheme,name=reg+'D' if chem=='degenerate' else reg if count==1 else reg+chr(65+i),chemistry=chem,option=count,union_coverage=ms[1],union_exact=ms[2],thermal=thermal(r['F'],r['R'])[1]))
  audit.append(dict(scheme=scheme,eligible=len(groups[loc]),thermal_rejections=thermal_rejections,coverage=ms[1],exact=ms[2],common_locus=loc));print(audit[-1],flush=True)
 joint.append(dict(region=reg,F_start=loc[0],F_end=loc[1],R_start=loc[2],R_end=loc[3],reference_span_bp=loc[3]-loc[0]+1,eligible_loci=len(options),joint_score=score[0]))
(p/'selected_joint.json').write_text(json.dumps(selected,indent=2));(p/'audit_joint.json').write_text(json.dumps(audit,indent=2));(p/'joint_locus.json').write_text(json.dumps(joint,indent=2));print('DONE',flush=True)
