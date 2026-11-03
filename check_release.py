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

import subprocess,sys
# The published 16S assignments use the curated species panel.
subprocess.run([sys.executable,str(p/'scripts/check_species_release.py')],check=True)
subprocess.run([sys.executable,str(p/'markers/28S/verify_and_plot.py')],check=True)
from Bio import SeqIO
total=list(SeqIO.parse(p/'sequences/all_markers.fasta','fasta'))
assert len(total)==len({r.id for r in total})==64
catalog={r.id:str(r.seq) for r in total}
windows={}
for r in rows('markers/28S/selected.csv'):
    endpoints=(int(r['start']),int(r['start'])+len(r['F'])-1,int(r['end'])-len(r['R'])+1,int(r['end']))
    assert endpoints==windows.setdefault(r['region'],endpoints)
    for side in ('F','R'):
        assert catalog[f"MiUrchin-28S-{r['name']}_{side}"]==r[side]
    for filename in ('README.md','README.zh-CN.md','README.en.md'):
        section=(p/filename).read_text().split('### 28S')[1].split('## ')[0]
        assert f"| {r['name']} | `{r['F']}` | `{r['R']}` |" in section
print('PASS: current 16S and nuclear 28S panels, coordinates, FASTA and multilingual tables')
