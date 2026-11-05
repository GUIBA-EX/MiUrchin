import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):import all_clades as c
import json,csv,collections,sys,itertools,functools,shutil
from pathlib import Path
sys.path.insert(0,'/Users/xiafei/Documents/Codex/2026-10-24/ni/work/micucumber_mifish/deps');import primer3
a=c.a;kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=50)
@functools.lru_cache(None)
def vs(q):return list(map(''.join,itertools.product(*(a.I[x] for x in q))))
@functools.lru_cache(None)
def single(s):return primer3.calc_tm(s,**kw),max(primer3.calc_hairpin(s,**kw).tm,primer3.calc_homodimer(s,**kw).tm)
@functools.lru_cache(None)
def het(x,y):return primer3.calc_heterodimer(x,y,**kw).tm
@functools.lru_cache(None)
def oligo(q):
 v=vs(q);tm=[single(x)[0] for x in v];st=max(single(x)[1] for x in v)
 for x,y in itertools.combinations(v,2):st=max(st,het(x,y))
 return min(tm),max(tm),st
out=[];thermal={}
for gene in ['16S','12S','COI','28S']:
 raw=list(csv.DictReader(open('work/validation/'+gene+'/nearest.tsv'),delimiter='\t'))
 for q in [q for q in a.assays if q['gene']==gene]:
  meta={t['accession']:t for t in a.templates[gene,q['name'],'F']};groups=collections.defaultdict(list)
  for t in raw:
   if t['name']!=gene+'_'+q['name']+'_original' or t['accession'] not in meta or int(t['score'])>10:continue
   m=meta[t['accession']];cl=c.clade(m)
   if cl!='unresolved':groups[cl].append(t)
   if m['order']:groups[m['order']].append(t)
  for cl,rr in groups.items():
   if len(rr)<3:continue
   mode=q['name'].endswith('D');seqs={}
   for s in ['F','R']:
    ts=[t[s] for t in rr];modal=''.join(collections.Counter(t[j] for t in ts).most_common(1)[0][0] for j in range(len(ts[0])));opts=set([modal]) if not mode else set()
    if mode:
     sets=[set(x) for x in modal]
     for j in range(len(modal)-3,len(modal)):sets[j]={t[j] for t in ts}
     def seq():return ''.join(a.rev[frozenset(x)] for x in sets)
     if c.deg(seq())<=64:
      opts.add(seq())
      for j,b,n in sorted([(j,b,n) for j in range(len(modal)-3) for b,n in collections.Counter(t[j] for t in ts).items() if b not in sets[j]],key=lambda x:(-x[2],-x[0])):
       old=set(sets[j]);sets[j].add(b)
       if c.deg(seq())>16:sets[j]=old
      opts.add(seq())
    candidates=[]
    for v in opts:
     for trim in range(min(7,len(v)-17)):
      z=v[trim:];vtherm=oligo(z)
      if vtherm[2]<55 and vtherm[0]>=45 and vtherm[1]<=75:
       cover=sum(sum(b not in a.I[x] for x,b in zip(z,t[trim:]))<=2 and c.match(z[-3:],t[-3:]) for t in ts)
       candidates.append((z,vtherm,cover,trim))
    seqs[s]=candidates
   best=None
   for f,ft,fc,fi in seqs['F']:
    for z,zt,rc,ri in seqs['R']:
     if min(fc,rc)<len(rr):continue
     dt=abs((ft[0]+ft[1]-zt[0]-zt[1])/2)
     if dt>5:continue
     st=max(ft[2],zt[2],max(het(x,y) for x in vs(f) for y in vs(z)))
     if st>=55:continue
     exact=sum(c.match(f,t['F'][fi:]) and c.match(z,t['R'][ri:]) for t in rr);score=(-exact,c.deg(f)+c.deg(z),fi+ri,st)
     if best is None or score<best[0]:best=(score,f,z,ft,zt,dt,st)
   if best:
    score,f,z,ft,zt,dt,st=best;id=gene+'_'+q['name']+'_'+cl+'_local';out.append(dict(id=id,gene=gene,parent=q['name'],clade=cl,F=f,R=z,panel=[t['accession'] for t in rr],n_design=len(rr),locus_method='unique best raw pair within 60–650 bp, <=10 total mismatches to original; reference-locus identity not independently established'))
    thermal[id]=dict(F_tm=list(ft[:2]),R_tm=list(zt[:2]),structure_max=st,delta_mid_tm=dt,pass_gate=True,deg_F=c.deg(f),deg_R=c.deg(z))
Path('work/local_candidates.json').write_text(json.dumps(out,indent=2));Path('work/local_thermal.json').write_text(json.dumps(thermal,indent=2))
for gene in ['16S','12S','COI','28S']:
 d=Path('work/local')/gene;d.mkdir(parents=True,exist_ok=True)
 for role in ['target','background']:shutil.copyfile(Path('work/validation')/gene/(role+'.fasta'),d/(role+'.fasta'))
 (d/'independent_primers.tsv').write_text('\n'.join('\t'.join([r['id'],r['F'],r['R']]) for r in out if r['gene']==gene))
print('Local candidates passing structure/target design',len(out),flush=True)
