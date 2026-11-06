"""Independently verify target pairs and inserts for the frozen-reference reanalysis."""
from pathlib import Path
import json,csv,re,collections,hashlib
P=Path(__file__).resolve().parents[1];O=P/'results/reviewer_revision';I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));RC=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN')
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0];d[k]=''
  else:d[k]+=l.strip().upper()
 return d
def sites(q,s,reverse):
 tail=q[:3] if reverse else q[-3:];rx='(?=('+''.join('['+I[x]+']' for x in tail)+'))'
 for m in re.finditer(rx,s):
  a=m.start() if reverse else m.start()-len(q)+3
  if a<0:continue
  t=s[a:a+len(q)]
  if len(t)!=len(q) or set(t)-set('ACGT'):continue
  mm=sum(b not in I[x] for x,b in zip(q,t))
  if mm<=2:yield a,mm
cat=json.loads((P/'results/catalog.json').read_text());allrows=cat['originals']+cat['assays'];checks=[]
for g in ['16S','12S','COI','28S']:
 seqs=fasta(P/'data'/g/'target.fasta');rs=[r for r in allrows if r['gene']==g];d=O/g
 cases=[(d,rs)]
 if g=='COI':cases.append((O/'benchmark_COI',[r for r in rs if r in cat['originals']]+[r for r in json.loads((O/'literature_benchmarks.json').read_text())['benchmarks'] if r['status']=='verified_IUPAC_compatible']))
 for d,rs in cases:
  expected=collections.defaultdict(set);bars=collections.defaultdict(set)
  for h in csv.DictReader((d/'independent_hits.tsv').open(),delimiter='\t'):
   if h['role']=='target':
    for flag in ['exact','le2last3']:
     if h[flag]=='1':expected[h['name'],flag].add(h['accession'])
  for h in csv.DictReader((d/'target_barcodes.tsv').open(),delimiter='\t'):bars[h['name']].add((h['accession'],h['sequence']))
  for r in rs:
   cov=set();ex=set();bb=set();F=r['F'];R=r['R'].translate(RC)[::-1]
   for a,seq in seqs.items():
    for s in [seq,seq.translate(RC)[::-1]]:
     for f,fm in sites(F,s,False):
      for z,rm in sites(R,s,True):
       if z>=f+len(F) and 60<=z+len(R)-f<=650:
        cov.add(a)
        if fm==rm==0:ex.add(a)
        bar=s[f+len(F):z]
        if not set(bar)-set('ACGT'):bb.add((a,bar))
   assert cov==expected[r['id'],'le2last3'],r['id'];assert ex==expected[r['id'],'exact'],r['id'];assert bb==bars[r['id']],r['id'];checks.append(dict(id=r['id'],scope=d.name,status='PASS'))
  print('PASS',g,d.name,len(rs),flush=True)
for name in ['summary.json','terminal_input_hashes.json']:
 obj=json.loads((O/name).read_text());hs=obj.get('input_sha256',obj)
 for path,h in hs.items():assert hashlib.sha256((P/path).read_bytes()).hexdigest()==h,path
(O/'verification.json').write_text(json.dumps(dict(status='PASS',target_pair_and_insert_checks=checks,independent_biological_validation=False),indent=2)+'\n')
