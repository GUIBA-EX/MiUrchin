"""Integrity checks for released primer assignments, numeric evidence and file hashes."""
from pathlib import Path
import csv,json,hashlib,re
p=Path(__file__).resolve().parent
def rows(n):return list(csv.DictReader((p/n).open(encoding='utf-8-sig')))
qa=json.loads((p/'analysis/independent_validation.json').read_text());assert qa['status']=='PASS' and qa['checks']==234496
assert json.loads((p/'analysis/final_validation.json').read_text())['status']=='PASS'
seq=rows('results/primers.csv');pairs=rows('results/pairings.csv');comp=rows('results/comparison.csv');assert len(comp)==8 and len(seq)==86 and len(pairs)==150
look={r['primer_id']:r for r in seq};assert len(look)==len(seq)
for r in pairs:
 for d in ['F','R']:
  q=look[r[d+'_id']];assert q['scheme']==r['scheme'] and q['direction']==d and q['sequence_5to3']==r[d]
for r in comp:
 pp=[x for x in pairs if x['scheme']==r['scheme']];assert len(pp)==int(r['evaluated_pairs']);assert int(r['WC3'])<=5 and int(r['GT2'])<=5
 assert len(pp)==(int(r['component_pairs']) if r['mode']=='separate' else int(r['F_oligos'])*int(r['R_oligos']))
 assert all(0<=float(r[k])<=100 for k in ['common_coverage_pct','common_exact_pct','region_coverage_pct','region_exact_pct'])
for n in ['README.md','README.zh-CN.md']:
 for link in re.findall(r'\]\(([^)]+)\)',(p/n).read_text()):
  if not link.startswith(('http','#')):assert (p/link).exists(),link
for n,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
print('PASS: assignments, sequence orientation, scheme risks/counts, links, evidence and SHA256')
