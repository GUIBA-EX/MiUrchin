import json,re,csv
from pathlib import Path
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));comp=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN');rc=lambda s:s.translate(comp)[::-1]
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0];d[k]=''
  else:d[k]+=l.upper()
 return d
seqs={g:fasta(Path('work/validation')/g/'target.fasta') for g in ['16S','12S','COI','28S']}
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
checks=[]
for r in json.load(open('work/final_recommended.json')):
 count=exact=0
 for acc in r['panel']:
  cov=ex=False
  for s in [seqs[r['gene']][acc],rc(seqs[r['gene']][acc])]:
   for f,fm in sites(r['F'],s,False):
    for z,rm in sites(rc(r['R']),s,True):
     length=z+len(r['R'])-f
     if z>=f+len(r['F']) and 60<=length<=650:cov=True;ex|=fm==0 and rm==0
  count+=cov;exact+=ex
 assert (count,exact)==(r['covered'],r['exact']),(r['id'],count,exact,r['covered'],r['exact'])
 checks.append(dict(id=r['id'],covered=count,exact=exact,disagreements=0))
Path('work/independent_verification.json').write_text(json.dumps(checks,indent=2));print('Independent raw paired verification:',len(checks),'all matched')
