import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):import all_clades as c
import json,collections,shutil,itertools,sys,functools
from pathlib import Path
sys.path.insert(0,'/Users/xiafei/Documents/Codex/2026-10-24/ni/work/micucumber_mifish/deps')
import primer3
a=c.a;dest=Path('work/terminal_only');dest.mkdir(exist_ok=True)
rows=[]
def design(ts,mode):
 modal=''.join(collections.Counter(t[j] for t in ts).most_common(1)[0][0] for j in range(len(ts[0])))
 if mode=='ordinary':return modal
 sets=[set(x) for x in modal]
 for j in range(len(modal)-3,len(modal)):sets[j]={t[j] for t in ts}
 def seq():return ''.join(a.rev[frozenset(x)] for x in sets)
 if c.deg(seq())>64:return None
 # Allocate remaining degeneracy to frequent unresolved variants, prioritizing proximity to 3-prime.
 while False:
  opts=[]
  for j in range(len(modal)-3):
   cnt=collections.Counter(t[j] for t in ts)
   for b,n in cnt.items():
    if b in sets[j]:continue
    newdeg=c.deg(seq())*(len(sets[j])+1)//len(sets[j])
    if newdeg<=64 and n/len(ts)>=.05:opts.append((n/len(ts)*(1+j/len(modal)),j,b))
  if not opts:break
  _,j,b=max(opts);sets[j].add(b)
 return seq()
for q in a.assays:
 gene=q['gene'];mode='D' if q['name'].endswith('D') else 'ordinary'
 rows.append(dict(id=gene+'_'+q['name']+'_original',gene=gene,parent=q['name'],clade='original',F=q['F'],R=q['R'],panel=[]))
 maps={s:{t['accession']:t for t in a.templates[gene,q['name'],s]} for s in ['F','R']}; groups=collections.defaultdict(list)
 for acc,f in maps['F'].items():
  r=maps['R'][acc]
  if any(t['insertions'] or len(t['template'])!=len(q[s]) or set(t['template'])-set('ACGT') for s,t in [('F',f),('R',r)]):continue
  cl=c.clade(f)
  if cl!='unresolved':groups[cl].append((f,r))
 for cl,rr in groups.items():
  if len(rr)<3:continue
  F=design([x[0]['template'] for x in rr],mode);R=design([x[1]['template'] for x in rr],mode)
  if F and R:rows.append(dict(id=gene+'_'+q['name']+'_'+cl+'_terminal',gene=gene,parent=q['name'],clade=cl,F=F,R=R,panel=[x[0]['accession'] for x in rr],n_design=len(rr)))
for gene in ['16S','12S','COI','28S']:
 d=dest/gene;d.mkdir(exist_ok=True)
 source=a.P/'analysis' if gene=='16S' else a.P/'markers/28S' if gene=='28S' else a.P/'markers/12S_COI'/gene
 for role in ['target','background']:shutil.copyfile(source/(role+'.fasta'),d/(role+'.fasta'))
 (d/'independent_primers.tsv').write_text('\n'.join('\t'.join([r['id'],r['F'],r['R']]) for r in rows if r['gene']==gene)+'\n')
Path('work/terminal_candidates.json').write_text(json.dumps(rows,indent=2))
print('Candidates incl originals:',len(rows),flush=True)
kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=50)
@functools.lru_cache(None)
def variants(s):return list(map(''.join,itertools.product(*(a.I[x] for x in s))))
@functools.lru_cache(None)
def single(s):return [primer3.calc_tm(s,**kw),primer3.calc_hairpin(s,**kw).tm,primer3.calc_homodimer(s,**kw).tm]
@functools.lru_cache(None)
def het(x,y):return primer3.calc_heterodimer(x,y,**kw).tm
thermal={}
for r in rows:
 fs,rs=variants(r['F']),variants(r['R']);vs=sorted(set(fs+rs));st=max(max(single(s)[1:]) for s in vs);pairmax=max(het(x,y) for x in fs for y in rs)
 for x,y in itertools.combinations(vs,2):st=max(st,het(x,y))
 ft=[single(x)[0] for x in fs];rt=[single(x)[0] for x in rs];dt=abs((min(ft)+max(ft)-min(rt)-max(rt))/2)
 thermal[r['id']]=dict(F_tm=[min(ft),max(ft)],R_tm=[min(rt),max(rt)],structure_max=st,FR_heterodimer_max=pairmax,delta_mid_tm=dt,pass_gate=st<45 and dt<=5 and min(ft+rt)>=45 and max(ft+rt)<=75,deg_F=len(fs),deg_R=len(rs))
 print(r['id'],thermal[r['id']]['pass_gate'],flush=True)
Path('work/terminal_thermal.json').write_text(json.dumps(thermal,indent=2))
