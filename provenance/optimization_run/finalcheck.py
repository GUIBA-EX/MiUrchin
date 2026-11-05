import json,sys,csv,itertools,functools,collections
from pathlib import Path
sys.path.insert(0,'/Users/xiafei/Documents/Codex/2026-10-24/ni/work/micucumber_mifish/deps');import primer3
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));vs=lambda q:list(map(''.join,itertools.product(*(I[x] for x in q))))
rows=json.load(open('work/selected.json'));clades=json.load(open('outputs/MiUrchin_all_clades.json'))['results'];audit=json.load(open('outputs/MiUrchin_terminal_audit.json'))
# Reference-locus check: both last 8 reference-aligned bases must agree with raw extraction.
import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):import all_clades as c
raw={}
for g in ['16S','12S','COI','28S']:
 for t in csv.DictReader(open('work/validation/'+g+'/nearest.tsv'),delimiter='\t'):raw[t['name'],t['accession']]=t
maps={(g,n,s):{t['accession']:t for t in ts} for (g,n,s),ts in c.a.templates.items()}
accepted=[];rejected=[]
@functools.lru_cache(None)
def single(q,conc):
 kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=conc)
 return primer3.calc_tm(q,**kw),max(primer3.calc_hairpin(q,**kw).tm,primer3.calc_homodimer(q,**kw).tm)
@functools.lru_cache(None)
def hetero(f,r,conc):return primer3.calc_heterodimer(f,r,mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=conc).tm
for r in rows:
 if r['id'].endswith('_local'):
  base=r['gene']+'_'+r['parent']+'_original';bad=[]
  for acc in r['panel']:
   if any(raw[base,acc][s][-8:]!=maps[r['gene'],r['parent'],s][acc]['template'][-8:] for s in ['F','R']):bad.append(acc)
  r['locus_unconfirmed']=bad
  if bad:r['reasons'].append('原始序列定位与参考末端8位不一致')
 fs,rs=vs(r['F']),vs(r['R']);fc,rc=200/len(fs),200/len(rs);ft=[single(x,fc)[0] for x in fs];rt=[single(x,rc)[0] for x in rs];st=max([single(x,fc)[1] for x in fs]+[single(x,rc)[1] for x in rs])
 for x,y in itertools.combinations(fs,2):st=max(st,hetero(x,y,fc))
 for x,y in itertools.combinations(rs,2):st=max(st,hetero(x,y,rc))
 for x in fs:
  for y in rs:st=max(st,hetero(x,y,max(fc,rc)))
 delta=abs((min(ft)+max(ft)-min(rt)-max(rt))/2);r['thermal_200nM_total']=dict(F_tm=[min(ft),max(ft)],R_tm=[min(rt),max(rt)],structure_max=st,delta_mid_tm=delta)
 if not(st<55 and delta<=5 and min(ft+rt)>=45 and max(ft+rt)<=75):r['reasons'].append('每方向总浓度200nM情景未过门槛')
 (rejected if r['reasons'] else accepted).append(r)
# Keep nonoverlapping applicability: broad clade when it passes, otherwise narrower order.
final=[]
for key in sorted(set((r['gene'],r['parent']) for r in accepted)):
 group=[r for r in accepted if (r['gene'],r['parent'])==key];used=set()
 for r in sorted(group,key=lambda r:(-len(r['panel']),-r['exact'],r['thermal']['deg_F']+r['thermal']['deg_R'])):
  if set(r['panel'])&used:continue
  final.append(r);used.update(r['panel'])
Path('work/final_recommended.json').write_text(json.dumps(final,ensure_ascii=False,indent=2));Path('work/final_rejections.json').write_text(json.dumps(rejected,ensure_ascii=False,indent=2))
# Cross-subprimer heterodimer check, explicitly separate from each intended pair.
pools=[]
for key in sorted(set((r['gene'],r['parent']) for r in final)):
 rr=[r for r in final if (r['gene'],r['parent'])==key]
 if len(rr)<2:continue
 seqs=sorted(set(x for r in rr for s in ['F','R'] for x in vs(r[s])));worst=max(hetero(x,y,50) for x,y in itertools.combinations(seqs,2));pools.append(dict(gene=key[0],parent=key[1],max_cross_structure_tm=worst,structure_pass=worst<55))
Path('work/pool_structures.json').write_text(json.dumps(pools,indent=2))
print('Final',len(final),'parents',len(set((r['gene'],r['parent']) for r in final)),'locus/concentration rejected',len(rejected),flush=True)
# All cross F/R combinations for actual mixed pool specificity check.
for g in ['16S','12S','COI','28S']:
 d=Path('work/pools')/g;d.mkdir(parents=True,exist_ok=True)
 import shutil
 for role in ['target','background']:shutil.copyfile(Path('work/validation')/g/(role+'.fasta'),d/(role+'.fasta'))
 lines=[]
 for p in pools:
  if p['gene']!=g:continue
  rr=[r for r in final if r['gene']==g and r['parent']==p['parent']]
  for i,x in enumerate(rr):
   for j,y in enumerate(rr):
    if i!=j:lines.append('\t'.join([g+'_'+p['parent']+'_cross_'+str(i)+'_'+str(j),x['F'],y['R']]))
 (d/'independent_primers.tsv').write_text('\n'.join(lines))
