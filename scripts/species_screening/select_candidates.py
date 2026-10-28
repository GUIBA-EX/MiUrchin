from pathlib import Path
import collections,csv,json,sys
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');n,reg=sys.argv[1:];project={'miurchin':'MiUrchin'}[n];p=root/'work'/f'{n}_species_refine'/reg;out=root/'outputs'/f'{project}_species_refine'/reg;sys.path.insert(0,str(root/'work/milily'));from common import thermal,oligo_thermal
pairs=json.loads((p/'pairs.json').read_text());h=collections.defaultdict(lambda:collections.defaultdict(list))
for name,acc,ori,gt,pos,mm,last in csv.reader((p/'sites/background_sites.tsv').open(),delimiter='\t'):h[name,int(gt)][acc,ori].append((int(pos),int(mm),int(last)))
prior=[x for x in json.loads((root/'work/miurchin_3prime8/selection.json').read_text()) if x['region']==reg];priorseq={(x['F'],x['R']) for x in prior}
eligible=[x for x in pairs if max(x['degeneracy_F'],x['degeneracy_R'])>1]
with (root/'work'/f'{n}_species_qc'/f'panel_{reg}.csv').open() as f:panel_n=sum(1 for _ in csv.DictReader(f))
allowed_drop=max(5.0,100.0/panel_n+1e-9)
cov=lambda x:(x['pred_taxon_coverage'],x['pred_taxon_exact'],x['pred_order_coverage'],-x['degeneracy_F']-x['degeneracy_R'])
exact=lambda x:(x['pred_taxon_exact'],x['pred_taxon_coverage'],x['pred_order_exact'],-x['degeneracy_F']-x['degeneracy_R'])
ranked=sorted(eligible,key=cov,reverse=True);near=[x for x in eligible if x['pred_taxon_coverage']>=ranked[0]['pred_taxon_coverage']-10]
work=ranked[:1800]+sorted(eligible,key=exact,reverse=True)[:1200]+sorted(near,key=exact,reverse=True)[:1800]+[x for x in eligible if (x['F'],x['R']) in priorseq]
work=list({(x['F'],x['R']):x for x in work}.values());print('SCREEN',n,reg,len(work),'of',len(eligible),flush=True)
for r in work:
 for gt,limit,col,strict in [(0,3,'WC3',False),(1,2,'GT2',False),(0,4,'WC4',False),(0,2,'strict_WC',True),(1,2,'strict_GT',True)]:
  f,b=h[r['F_id'],gt],h[r['R_id'],gt];r[col]=len({acc for acc,ori in f.keys()&b.keys() if any(fm<=limit and rm<=limit and (not strict or (not fl and not rl)) and 0<=rp-fp-len(r['F'])<=1000 for fp,fm,fl in f[acc,ori] for rp,rm,rl in b[acc,ori])})
cache={}
def physical(x):
 k=(x['F'],x['R'])
 if k not in cache:
  a,b=oligo_thermal(k[0]),oligo_thermal(k[1]);pre=all(max(x[2],y[2])<55 and abs((x[0]+x[1]-y[0]-y[1])/2)<=5 for x,y in zip(a,b));cache[k]=thermal(*k) if pre else (False,[])
 return cache[k]
selected=[];audit=[]
for cap in (20,100):
 v=[x for x in work if max(x['WC3'],x['GT2'])<=cap and max(x['strict_WC'],x['strict_GT'])<=20];v.sort(key=cov,reverse=True);best=None
 for x in v:
  ok,th=physical(x)
  if ok:best=x;break
 if best is None:print('NO PASS',reg,cap,flush=True);continue
 # Allow five percentage points or one species, whichever is larger, for small panels.
 alternatives=[x for x in v if x['pred_taxon_coverage']>=best['pred_taxon_coverage']-allowed_drop];alternatives.sort(key=exact,reverse=True);bestexact=None
 for x in alternatives:
  ok,th=physical(x)
  if ok:bestexact=x;break
 for mode,x in [('coverage',best),('exact',bestexact)]:
  if x is None or any((a['F'],a['R'])==(x['F'],x['R']) for a in selected):continue
  z={k:v for k,v in x.items() if k not in ('cv','ex')};z.update(name=f'{reg}-R{cap}-{mode}',tier=cap,selection_mode=mode,thermal=cache[x['F'],x['R']][1]);selected.append(z);print('SELECT',z['name'],round(z['pred_taxon_coverage'],1),round(z['pred_taxon_exact'],1),z['strict_WC'],z['strict_GT'],flush=True)
with (out/'candidates_screened.csv').open('w') as f:
 rows=[{k:v for k,v in r.items() if k not in ('cv','ex')} for r in work];w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(p/'selection.json').write_text(json.dumps(selected,indent=2));(p/'selection_manifest.json').write_text(json.dumps(dict(total_pairs=len(pairs),eligible_pairs=len(eligible),screened_pairs=len(work),exact_priority_max_coverage_drop_pp=allowed_drop,background_limits=[20,100],strict_background_limit=20,thermal_checked=len(cache)),indent=2));print('DONE',n,reg,len(selected),flush=True)
