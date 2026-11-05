"""Recompute raw paired scans for current and baseline assays. Never edits input evidence."""
from pathlib import Path
import json,csv,subprocess,tempfile,shutil,concurrent.futures,collections,re,sys,argparse,itertools,functools
P=Path(__file__).resolve().parents[1]
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));RC=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN')
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0];d[k]=''
  else:d[k]+=l.upper()
 return d
def sites(q,s,reverse):
 motif=q[:3] if reverse else q[-3:];pattern='(?=('+''.join('['+I[x]+']' for x in motif)+'))';hits=[]
 for m in re.finditer(pattern,s):
  start=m.start() if reverse else m.start()-len(q)+3
  if start<0:continue
  t=s[start:start+len(q)]
  if len(t)!=len(q) or set(t)-set('ACGT'):continue
  mm=sum(b not in I[x] for x,b in zip(q,t))
  if mm<=2:hits.append((start,mm))
 return hits
args=argparse.ArgumentParser();args.add_argument('--output',default=str(P/'results/current_validation.json'));args.add_argument('--thermal',action='store_true');args=args.parse_args()
cat=json.loads((P/'results/catalog.json').read_text());rows=cat['assays'];originals=cat['originals'];report={'status':'RUNNING','pairs':len(rows),'scan_checks':[],'independent_checks':[],'thermal_checks':[]}
with tempfile.TemporaryDirectory(prefix='miurchin-revalidate-') as tmp:
 tmp=Path(tmp);binary=tmp/'scan';subprocess.run(['c++','-O3','-std=c++17',str(P/'scripts/scan.cpp'),'-o',str(binary)],check=True)
 def run(g):
  d=tmp/g;d.mkdir()
  for role in ['target','background']:shutil.copyfile(P/'data'/g/(role+'.fasta'),d/(role+'.fasta'))
  (d/'independent_primers.tsv').write_text('\n'.join('\t'.join([r['id'],r['F'],r['R']]) for r in rows+originals if r['gene']==g))
  with (d/'scan.log').open('w') as log:subprocess.run([str(binary),str(d)],check=True,stdout=log,stderr=log)
  hs=collections.defaultdict(set)
  for h in csv.DictReader((d/'independent_hits.tsv').open(),delimiter='\t'):
   for flag in ['exact','le2last3','le2','le3']:
    if h[flag]=='1':hs[h['name'],h['role'],h['model'],flag].add(h['accession'])
  checks=[]
  for r in [r for r in rows if r['gene']==g]:
   panel=set(r['panel']);base=next(x['id'] for x in originals if x['gene']==g and x['parent']==r['parent'])
   for id,col,exactcol in [(r['id'],'covered','exact'),(base,'original_covered','original_exact')]:
    assert len(hs[id,'target','WC','le2last3']&panel)==r[col],(r['id'],col)
    assert len(hs[id,'target','WC','exact']&panel)==r[exactcol],(r['id'],exactcol)
   for id,key in [(r['id'],'background'),(base,'original_background')]:
    for model,flag in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]:assert len(hs[id,'background',model,flag])==r[key][model+'_'+flag],(r['id'],key,model,flag)
   checks.append({'id':r['id'],'status':'PASS'})
  return checks
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for checks in pool.map(run,['16S','12S','COI','28S']):report['scan_checks']+=checks
# Independent target matching has no shared implementation with C++.
seqs={g:fasta(P/'data'/g/'target.fasta') for g in ['16S','12S','COI','28S']}
for r in rows:
 cov=exact=0
 for acc in r['panel']:
  covered=ex=False
  for s in [seqs[r['gene']][acc],seqs[r['gene']][acc].translate(RC)[::-1]]:
   for f,fm in sites(r['F'],s,False):
    for z,rm in sites(r['R'].translate(RC)[::-1],s,True):
     if z>=f+len(r['F']) and 60<=z+len(r['R'])-f<=650:covered=True;ex|=fm==0 and rm==0
  cov+=covered;exact+=ex
 assert (cov,exact)==(r['covered'],r['exact']),r['id'];report['independent_checks'].append({'id':r['id'],'covered':cov,'exact':exact,'status':'PASS'})
if args.thermal:
 import primer3
 report['primer3_version']=primer3.__version__
 @functools.lru_cache(None)
 def one(s,c):
  kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=c)
  return primer3.calc_tm(s,**kw),max(primer3.calc_hairpin(s,**kw).tm,primer3.calc_homodimer(s,**kw).tm)
 @functools.lru_cache(None)
 def het(x,y,c):return primer3.calc_heterodimer(x,y,mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=c).tm
 for r in rows:
  fv=list(map(''.join,itertools.product(*(I[x] for x in r['F']))));rv=list(map(''.join,itertools.product(*(I[x] for x in r['R']))))
  for scenario in range(2):
   fc=50 if scenario==0 else 200/len(fv);rc=50 if scenario==0 else 200/len(rv);ft=[one(x,fc) for x in fv];rt=[one(x,rc) for x in rv];st=max(x[1] for x in ft+rt)
   for x,y in itertools.combinations(fv,2):st=max(st,het(x,y,fc))
   for x,y in itertools.combinations(rv,2):st=max(st,het(x,y,rc))
   for x in fv:
    for y in rv:st=max(st,het(x,y,max(fc,rc)))
   obs=dict(F_tm=[min(x[0] for x in ft),max(x[0] for x in ft)],R_tm=[min(x[0] for x in rt),max(x[0] for x in rt)],structure_max=st)
   for key in ['F_tm','R_tm']:
    assert all(abs(x-y)<1e-6 for x,y in zip(obs[key],r['thermal'][scenario][key])),(r['id'],scenario,key)
   assert abs(st-r['thermal'][scenario]['structure_max'])<1e-6,(r['id'],scenario,'structure')
  report['thermal_checks'].append({'id':r['id'],'status':'PASS'})
report['status']='PASS';Path(args.output).write_text(json.dumps(report,indent=2));print('PASS',len(rows),'paired assays: raw scans, baseline comparisons, independent target matches'+(', both thermodynamic scenarios' if args.thermal else ''))
