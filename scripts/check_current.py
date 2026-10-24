from pathlib import Path
import csv,json,collections,math,re
from functools import reduce
from operator import mul
p=Path(__file__).resolve().parents[1];d=p/'results/current'
def read(f):return list(csv.DictReader(f.open()))
pairs=read(d/'primer_pairs.csv');comp=read(d/'comparison.csv');assert len(pairs)==18 and len(comp)==12
I=dict(A='A',C='C',G='G',T='T',R='AG',Y='CT',S='CG',W='AT',K='GT',M='AC',B='CGT',D='AGT',H='ACT',V='ACG',N='ACGT');unique={}
for r in pairs:
 for side in ['F','R']:
  q=r[side];assert set(q)<=I.keys();assert reduce(mul,[len(I[b]) for b in q],1)==int(r['degeneracy_'+side])
  key=r['name']+'_'+side
  if key in unique:assert unique[key]==q
  unique[key]=q
fasta={};key=None
for line in (d/'primers.fasta').read_text().splitlines():
 if line.startswith('>'):
  key=line[1:];assert key not in fasta;fasta[key]=''
 else:fasta[key]+=line
assert len(unique)==28 and unique==fasta
weights={r['accession']:float(r['weight']) for r in json.loads((p/'results/compact/panel.json').read_text())};h=collections.defaultdict(set)
for sub in ['terminal_optimization']:
 for r in csv.DictReader((p/'results'/sub/'independent_hits.tsv').open(),delimiter='\t'):
  if sub=='compact' and not r['name'].startswith(('L','XL')):continue
  for flag in ['exact','le2last3','le2','le3','le4']:
   if r[flag]=='1':h[r['name'],r['role'],r['model'],flag].add(r['accession'])
for r in comp:
 pp=[x for x in pairs if x['scheme']==r['scheme']];assert len(pp)==int(r['pairs']) and len(pp) in [1,2]
 def union(role,model,flag):return set().union(*(h[x['name'],role,model,flag] for x in pp))
 for flag,col in [('le2last3','coverage_pct'),('exact','exact_pct')]:assert math.isclose(100*sum(weights.get(a,0) for a in union('target','WC',flag))/sum(weights.values()),float(r[col]),abs_tol=1e-8)
 for model,flag,col in [('WC','le3','WC3'),('GT','le2','GT2'),('WC','le4','WC4')]:assert len(union('background',model,flag))==int(r[col])
 assert int(r['WC3'])<=5 and int(r['GT2'])<=5
assert json.loads((p/'results/terminal_optimization/verification.json').read_text())['disagreements']==0
assert all(float(r['structure_max'])<55 for r in read(p/'results/terminal_optimization/thermal.csv'))
for f in [p/'README.md',p/'README.zh-CN.md',*list((p/'docs').glob('*.md'))]:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not link.startswith(('http','#')):assert (f.parent/link.split('#')[0]).exists(),(f,link)
print('PASS: 12 portfolios, 18 paired rows, 28 unique FASTA entries, IUPAC degeneracy, recomputed metrics, thermal limits and links')
