"""Fail on drift between adopted evidence, current catalog, FASTA, reports and checksums."""
from pathlib import Path
import json,csv,hashlib,re,math,collections
P=Path(__file__).resolve().parent
cat=json.loads((P/'results/catalog.json').read_text());rows=cat['assays'];assert len(rows)==76 and len(cat['originals'])==32
assert len({r['id'] for r in rows})==76 and len({(r['gene'],r['parent']) for r in rows})==32
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']))
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0];assert k not in d;d[k]=''
  else:d[k]+=l
 return d
allfa=fasta(P/'sequences/all_markers.fasta');assert len(allfa)==152
assert allfa==fasta(P/'sequences/primers.fasta')
source={}
for file in ['round1.json','round2.json']:
 for r in json.loads((P/'results/evidence'/file).read_text())['recommended']:source[r['id']]=r
used=collections.defaultdict(set)
for r in rows:
 assert r['covered']==r['n_records']==len(r['panel'])>=3
 assert len(set(r['panel']))==r['n_records']
 key=(r['gene'],r['parent']);assert not used[key].intersection(r['panel']);used[key].update(r['panel'])
 for s in ['F','R']:
  assert r[s]==allfa[r['id']+'_'+s]==source[r['id']][s]
  assert set(r[s])<=set(I)
  if r['mode']=='ordinary':assert set(r[s])<=set('ACGT')
 for k,v in r['background'].items():assert v<=r['original_background'][k]
 margin=min(min(t['F_tm']+t['R_tm'])-t['structure_max'] for t in r['thermal']);assert abs(margin-r['minimum_structure_margin'])<1e-8
 assert r['tier']==('priority' if margin>=5 else 'conditional')
 for t in r['thermal']:assert t['structure_max']<55 and min(t['F_tm']+t['R_tm'])>=45 and max(t['F_tm']+t['R_tm'])<=75 and t['delta_mid_tm']<=5
 assert r['use']=='separate_PCR'
assert sum(r['tier']=='priority' for r in rows)==65
for tier in ['priority','conditional']:
 f=fasta(P/'sequences'/f'{tier}.fasta');assert f=={r['id']+'_'+s:r[s] for r in rows if r['tier']==tier for s in ['F','R']}
flat=list(csv.DictReader((P/'sequences/primer_pairs.csv').open()));assert len(flat)==76
for a,b in zip(flat,rows):assert a['id']==b['id'] and a['F']==b['F'] and a['R']==b['R']
v=json.loads((P/'results/current_validation.json').read_text());assert v['status']=='PASS'
for k in ['scan_checks','independent_checks','thermal_checks']:assert len(v[k])==76 and {r['id'] for r in v[k]}=={r['id'] for r in rows}
assert 'Local integrated computational manuscript v2.0.0' in (P/'publications/MiUrchin_preprint.md').read_text()
assert (P/'publications/MiUrchin_preprint.pdf').stat().st_size>10000
# Current documentation links resolve; historical documents remain independently archived.
for f in [P/'README.md',P/'README.en.md',P/'README.zh-CN.md',*list((P/'docs').glob('*.md')),P/'publications/MiUrchin_preprint.md',P/'publications/MiUrchin_supplement.md']:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not link.startswith(('http','#')):assert (f.parent/link.split('#')[0]).exists(),(f,link)
for name,digest in json.loads((P/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
print('PASS: adopted sources,76 pairs,152 named oligos,65/11 tiers,32 parents,raw+thermal validation,links,and checksums')
