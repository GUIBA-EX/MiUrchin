"""Local one-pair swaps to improve exact coverage within 0.5 percentage points of discovery coverage."""
from pathlib import Path
import json,numpy as np,collections,shutil
p=Path(__file__).resolve().parent
scope={'__file__':str(p/'optimize_portfolios.py')};code=(p/'optimize_portfolios.py').read_text();exec(code[:code.index('solutions=[]')],scope)
z=scope['z'];m=scope['m'];e=z['exact'];index=scope['index'];by=scope['by'];rows=scope['rows'];assess=scope['assess'];cfg=scope['cfg']
selected=json.loads((p.parent/'portfolio_selected.json').read_text());solutions=json.loads((p/'portfolio_search.json').read_text());shutil.copy2(p/'portfolio_search.json',p/'portfolio_search_before_exact.json');reports=[]
for s in selected:
 group=s['locus'];mode=s['mode'];w=z['weights_'+group];scope['w']=w
 def scores(pairs):
  _,_,allowed,mask=cfg(pairs,mode);exact=np.zeros(len(w),bool)
  for a,b in allowed:exact|=e[index[a]]&e[index[b]]
  return float(w[mask].sum()),float(w[exact].sum())
 pairs=[tuple(x) for x in s['component_pairs']];cov,ex=scores(pairs);floor=cov-.005
 cand=[(r['F_id'],r['R_id']) for r in rows if r['band']==group and r['WC_le3']<=5 and r['GT_le2']<=5 and float(r['tm_delta'])<=5]
 start=(cov,ex);iterations=0
 for step in range(6):
  ranked=[];seen=set()
  for slot in range(len(pairs)+(1 if len(pairs)<6 else 0)):
   for pair in cand:
    trial=pairs[:];trial[slot:slot+1]=[pair]
    if len(set(trial))!=len(trial):continue
    key=tuple(sorted(trial))
    if key in seen:continue
    seen.add(key);c,x=scores(trial)
    if c+1e-9<floor or x<=ex+1e-9:continue
    ranked.append((-x,-c,key))
  ranked.sort();best=None
  for nx,nc,trial in ranked:
   a=assess(list(trial),mode,5)
   if a is not None:best=a;pairs=list(trial);cov=-nc;ex=-nx;iterations+=1;break
  if best is None:break
  print(group,mode,'swap',step,'coverage',cov,'exact',ex,flush=True)
 a=assess(pairs,mode,5);a.update(locus=group,mode=mode,budget_per_model=5,max_component_pairs=len(pairs),exact_coverage=ex,selection_method='one-pair local swaps improve exact coverage; primary coverage retained within 0.5 percentage points of initial solution')
 solutions=[r for r in solutions if not(r['locus']==group and r['mode']==mode)]+[a]
 reports.append(dict(locus=group,mode=mode,initial_coverage=start[0],initial_exact=start[1],final_coverage=cov,final_exact=ex,iterations=iterations))
(p/'portfolio_search.json').write_text(json.dumps(solutions,indent=2));(p/'exact_refinement.json').write_text(json.dumps(reports,indent=2));print('DONE exact local refinement',flush=True)
