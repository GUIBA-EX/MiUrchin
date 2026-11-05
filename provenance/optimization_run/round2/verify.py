from pathlib import Path
code=Path('work/independent_verify.py').read_text().split('checks=[]')[0];exec(code)
import collections,sys,itertools,functools,shutil
B=Path('work/round2');rows=json.load(open(B/'selected.json'));near={}
for g in ['16S','12S','COI']:
 for x in csv.DictReader(open('work/validation/'+g+'/nearest.tsv'),delimiter='\t'):near[x['name'],x['accession']]=x
checks=[]
for r in rows:
 count=exact=0;lengths=[];anchored_exact=0
 for acc in r['panel']:
  cov=ex=False
  for s in [seqs[r['gene']][acc],rc(seqs[r['gene']][acc])]:
   for f,fm in sites(r['F'],s,False):
    for z,rm in sites(rc(r['R']),s,True):
     if z>=f+len(r['F']) and 60<=z+len(r['R'])-f<=650:cov=True;ex|=fm==0 and rm==0
  count+=cov;exact+=ex
  anchor=near[r['gene']+'_'+r['parent']+'_original',acc];poss=[]
  for s in [seqs[r['gene']][acc],rc(seqs[r['gene']][acc])]:
   for f in range(len(s)):
    if not s.startswith(anchor['F'],f):continue
    for z in range(f+len(anchor['F']),min(len(s),f+650)):
     if s.startswith(rc(anchor['R']),z) and 60<=z+len(anchor['R'])-f<=650:poss.append((s,f,z))
  assert len(poss)==1
  s,f,z=poss[0];fe=f+len(anchor['F'])+r['F_shift'];rs=z-r['R_shift'];fs=fe-len(r['F']);rend=rs+len(r['R']);ft=s[fs:fe];rt=rc(s[rs:rend]);mm=[]
  for q,t in [(r['F'],ft),(r['R'],rt)]:
   assert len(q)==len(t) and not set(t)-set('ACGT');assert all(b in I[x] for x,b in zip(q[-3:],t[-3:]));n=sum(b not in I[x] for x,b in zip(q,t));assert n<=2;mm.append(n)
  assert rs>=fe and 60<=rend-fs<=650;lengths.append(rend-fs);anchored_exact+=sum(mm)==0
 assert (count,exact)==(r['covered'],r['exact'])
 r['anchored_product_lengths']=sorted(set(lengths));r['anchored_exact']=anchored_exact
 checks.append(dict(id=r['id'],n=len(r['panel']),full_scan_covered=count,full_scan_exact=exact,anchored_exact=anchored_exact,disagreements=0))
(B/'verified_selected.json').write_text(json.dumps(rows,indent=2));(B/'independent_checks.json').write_text(json.dumps(checks,indent=2))
sys.path.insert(0,'/Users/xiafei/Documents/Codex/2026-10-24/ni/work/micucumber_mifish/deps');import primer3
@functools.lru_cache(None)
def variants(q):return list(map(''.join,itertools.product(*(I[x] for x in q))))
@functools.lru_cache(None)
def ht(x,y):return primer3.calc_heterodimer(x,y,mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=50).tm
pools=[]
for g in ['16S','12S','COI']:
 d=B/'pools'/g;d.mkdir(parents=True,exist_ok=True)
 for role in ['target','background']:shutil.copyfile(B/g/(role+'.fasta'),d/(role+'.fasta'))
 lines=[]
 for parent in sorted(set(r['parent'] for r in rows if r['gene']==g)):
  rr=[r for r in rows if r['gene']==g and r['parent']==parent]
  if len(rr)<2:continue
  vs=sorted(set(v for r in rr for side in ['F','R'] for v in variants(r[side])));st=max(ht(x,y) for x,y in itertools.combinations(vs,2));pools.append(dict(gene=g,parent=parent,structure_max=st,structure_pass=st<55))
  for i,r in enumerate(rr):
   for j,z in enumerate(rr):
    if i!=j:lines.append('\t'.join([g+'_'+parent+'_cross_'+str(i)+'_'+str(j),r['F'],z['R']]))
 (d/'independent_primers.tsv').write_text('\n'.join(lines))
(B/'pool_structure.json').write_text(json.dumps(pools,indent=2));print('All selected candidates independently verified, including intended shifted loci:',len(rows))
