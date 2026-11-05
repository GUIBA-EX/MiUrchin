import json,csv,collections,itertools,functools,sys,contextlib,io
from pathlib import Path
sys.path.insert(0,str(Path('work').resolve()))
with contextlib.redirect_stdout(io.StringIO()):import all_clades as c
sys.path.insert(0,'/Users/xiafei/Documents/Codex/2026-10-24/ni/work/micucumber_mifish/deps');import primer3
a=c.a;I=a.I;rev=a.rev;comp=a.comp;rc=lambda s:s.translate(comp)[::-1]
wanted={'16S':['XL','XLD'],'12S':['XS','S','L'],'COI':['XS','S','M']};base=Path('work/round2')
@functools.lru_cache(None)
def variants(q):return list(map(''.join,itertools.product(*(I[x] for x in q))))
@functools.lru_cache(None)
def one(s,conc):
 kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=conc)
 return primer3.calc_tm(s,**kw),max(primer3.calc_hairpin(s,**kw).tm,primer3.calc_homodimer(s,**kw).tm)
@functools.lru_cache(None)
def het(x,y,conc):return primer3.calc_heterodimer(x,y,mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=conc).tm
@functools.lru_cache(None)
def oligo(q):
 vs=variants(q);out=[]
 for conc in [50,200/len(vs)]:
  ts=[one(s,conc) for s in vs];st=max(x[1] for x in ts)
  if st>=55:return None
  for x,y in itertools.combinations(vs,2):st=max(st,het(x,y,conc))
  lo=min(x[0] for x in ts);hi=max(x[0] for x in ts)
  if st>=55 or lo<45 or hi>75:return None
  out.append((lo,hi,st))
 return out
out=[];manifest=[]
for gene,names in wanted.items():
 raw=a.fasta(Path('work/validation')/gene/'target.fasta');near=list(csv.DictReader(open('work/validation/'+gene+'/nearest.tsv'),delimiter='\t'))
 for name in names:
  q=next(q for q in a.assays if q['gene']==gene and q['name']==name);meta={s:{t['accession']:t for t in a.templates[gene,name,s]} for s in ['F','R']};groups=collections.defaultdict(list);failed=[]
  for t in near:
   acc=t['accession']
   if t['name']!=gene+'_'+name+'_original' or acc not in meta['F'] or int(t['score'])>10:continue
   if any(t[s][-8:]!=meta[s][acc]['template'][-8:] for s in ['F','R']):failed.append(acc);continue
   positions=[]
   for ori,s in [('+',raw[acc]),('-',rc(raw[acc]))]:
    fs=[i for i in range(len(s)) if s.startswith(t['F'],i)];rs=[i for i in range(len(s)) if s.startswith(rc(t['R']),i)]
    for f in fs:
     for r in rs:
      if r>=f+len(t['F']) and 60<=r+len(t['R'])-f<=650:positions.append((ori,s,f,r))
   if len(positions)!=1:continue
   ori,s,f,r=positions[0];m=meta['F'][acc];rec=dict(accession=acc,sequence=s,F_end=f+len(t['F']),R_end=len(s)-r,orientation=ori,species=m['species'])
   cl=c.clade(m)
   if cl!='unresolved':groups[cl].append(rec)
   if m['order']:groups[m['order']].append(rec)
  for group,rr in groups.items():
   if len(rr)<3:continue
   choices={}
   for side in ['F','R']:
    opts=[]
    for shift in range(-20,21):
     for length in range(18,28):
      ts=[]
      for t in rr:
       s=t['sequence'] if side=='F' else rc(t['sequence']);end=t[side+'_end']+shift;seq=s[end-length:end] if end-length>=0 and end<=len(s) else ''
       if len(seq)!=length or set(seq)-set('ACGT'):break
       ts.append(seq)
      if len(ts)!=len(rr):continue
      sets=[set([collections.Counter(t[j] for t in ts).most_common(1)[0][0]]) for j in range(length)]
      if name.endswith('D'):
       for j in range(length-3,length):sets[j]={t[j] for t in ts}
      elif any(len({t[j] for t in ts})>1 for j in range(length-3,length)):continue
      def seq():return ''.join(rev[frozenset(x)] for x in sets)
      if c.deg(seq())>16:continue
      candidates={seq()}
      if name.endswith('D'):
       for j,b,n in sorted([(j,b,n) for j in range(length-3) for b,n in collections.Counter(t[j] for t in ts).items() if b not in sets[j]],key=lambda x:(-x[2],-x[0])):
        old=set(sets[j]);sets[j].add(b)
        if c.deg(seq())>16:sets[j]=old
       candidates.add(seq())
      for primer in candidates:
       if not all(sum(b not in I[x] for x,b in zip(primer,t))<=2 for t in ts):continue
       th=oligo(primer)
       if th is None:continue
       exact=sum(c.match(primer,t) for t in ts);margin=min(v[0]-v[2] for v in th)
       opts.append(dict(seq=primer,shift=shift,length=length,thermal=th,exact=exact,margin=margin,templates=ts))
    unique={}
    for v in sorted(opts,key=lambda v:(-v['exact'],-v['margin'],c.deg(v['seq']),abs(v['shift']))):unique.setdefault(v['seq'],v)
    choices[side]=list(unique.values())[:14]
   pairs=[]
   for f in choices['F']:
    for r in choices['R']:
     valid=True;th=[]
     for scenario in range(2):
      ft,rt=f['thermal'][scenario],r['thermal'][scenario];delta=abs((ft[0]+ft[1]-rt[0]-rt[1])/2)
      if delta>5:valid=False;break
      conc=50 if scenario==0 else max(200/c.deg(f['seq']),200/c.deg(r['seq']));st=max(ft[2],rt[2])
      for x in variants(f['seq']):
       for y in variants(r['seq']):st=max(st,het(x,y,conc))
      if st>=55:valid=False;break
      th.append(dict(F_tm=ft[:2],R_tm=rt[:2],structure_max=st,delta_mid_tm=delta,margin=min(ft[0],rt[0])-st))
     if not valid:continue
     exact=sum(c.match(f['seq'],x) and c.match(r['seq'],y) for x,y in zip(f['templates'],r['templates']));pairs.append(((-exact,-min(t['margin'] for t in th),c.deg(f['seq'])+c.deg(r['seq'])),f,r,th,exact))
   for num,(_,f,r,th,exact) in enumerate(sorted(pairs,key=lambda x:x[0])[:10]):
    out.append(dict(id=f'{gene}_{name}_{group}_shift{num}',gene=gene,parent=name,clade=group,F=f['seq'],R=r['seq'],F_shift=f['shift'],R_shift=r['shift'],panel=[t['accession'] for t in rr],species=[t['species'] for t in rr],thermal=th,design_exact=exact,deg_F=c.deg(f['seq']),deg_R=c.deg(r['seq'])))
   manifest.append(dict(gene=gene,parent=name,clade=group,n=len(rr),F_passing=len(choices['F']),R_passing=len(choices['R']),pairs_passing=len(pairs),anchor_failed=failed))
   print(gene,name,group,len(rr),'pairs',len(pairs),flush=True)
(base/'candidates.json').write_text(json.dumps(out,indent=2));(base/'search_manifest.json').write_text(json.dumps(manifest,indent=2))
import shutil
for g in wanted:
 d=base/g;d.mkdir(exist_ok=True)
 for role in ['target','background']:shutil.copyfile(Path('work/validation')/g/(role+'.fasta'),d/(role+'.fasta'))
 lines=['\t'.join([r['id'],r['F'],r['R']]) for r in out if r['gene']==g]
 for q in a.assays:
  if q['gene']==g and q['name'] in wanted[g]:lines.append('\t'.join([g+'_'+q['name']+'_original',q['F'],q['R']]))
 (d/'independent_primers.tsv').write_text('\n'.join(lines))
print('TOTAL',len(out),flush=True)
