from pathlib import Path
import csv,json,re
p=Path(__file__).resolve().parents[1];d=p/'results/compact'
def rows(n):return list(csv.DictReader((d/n).open()))
r=rows('primer_pairs.csv');c=rows('comparison.csv');assert len(c)==8
assert {x['scheme'] for x in r}=={x['scheme'] for x in c}
for x in c:
 pp=[y for y in r if y['scheme']==x['scheme']];assert len(pp)==int(x['pairs']) and len(pp) in [1,2]
 assert int(x['WC3'])<=5 and int(x['GT2'])<=5
 assert 0<=float(x['exact_pct'])<=float(x['coverage_pct'])<=100+1e-8
 for y in pp:
  for side in ['F','R']:assert set(y[side])<=set('ACGT')
  assert abs(float(y['F_tm'])-float(y['R_tm']))<=5+1e-8
fasta={};key=None
for line in (d/'primers.fasta').read_text().splitlines():
 if line.startswith('>'):key=line[1:];fasta[key]=''
 else:fasta[key]+=line
assert len(fasta)==2*len(r)
for x in r:
 for side in ['F','R']:assert fasta[x['name']+'_'+side]==x[side]
assert all(x['background_pass'] for x in json.loads((d/'verification.json').read_text()))
for f in [p/'README.md',p/'README.zh-CN.md',*list((p/'docs').glob('*.md'))]:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not link.startswith(('http','#')):assert (f.parent/link.split('#')[0]).exists(),(f,link)
# Recompute published metrics from independent raw hits and panel weights.
import collections,math
weights={x['accession']:float(x['weight']) for x in json.loads((d/'panel.json').read_text())}
hits=collections.defaultdict(set)
for x in csv.DictReader((d/'independent_hits.tsv').open(),delimiter='\t'):
 for flag in ['exact','le2last3','le2','le3','le4']:
  if x[flag]=='1':hits[x['name'],x['role'],x['model'],flag].add(x['accession'])
for x in c:
 names=[y['name'] for y in r if y['scheme']==x['scheme']]
 def union(role,model,flag):return set().union(*(hits[n,role,model,flag] for n in names))
 for flag,col in [('le2last3','coverage_pct'),('exact','exact_pct')]:
  val=100*sum(weights.get(a,0) for a in union('target','WC',flag))/sum(weights.values())
  assert math.isclose(val,float(x[col]),abs_tol=1e-8)
 for model,flag,col in [('WC','le3','WC3'),('GT','le2','GT2'),('WC','le4','WC4')]:assert len(union('background',model,flag))==int(x[col])
assert json.loads((d/'independent_validation.json').read_text())['disagreements']==0
print('PASS: eight compact portfolios, sequences, counts, thresholds, metrics and document links')
