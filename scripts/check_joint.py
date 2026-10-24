from pathlib import Path
import csv,json,collections,hashlib
p=Path(__file__).resolve().parents[1]
d=p/'results' if p.name=='MiLily' else p/'results/terminal_optimization'
def rows(f):return list(csv.DictReader(f.open()))
a=rows(d/'primer_pairs.csv');assert len(a)==16 and len({r['name'] for r in a})==16
co=rows(d/'binding_positions.csv')
for reg in ['S','M','L','XL']:
 g=[r for r in co if r['region']==reg];assert {r['name'] for r in g}=={reg,reg+'A',reg+'B',reg+'D'}
 assert len({tuple(r[k] for k in ['F_start','F_end','R_start','R_end']) for r in g})==1
 for r in g:
  q=next(x for x in a if x['name']==r['name'])
  for side in ['F','R']:assert r[side+'_sequence']==q[side] and int(r[side+'_end'])-int(r[side+'_start'])+1==len(q[side])
for r in rows(d/'thermal.csv'):
 assert float(r['structure_max'])<55
 assert abs((float(r['F_tm_min'])+float(r['F_tm_max'])-float(r['R_tm_min'])-float(r['R_tm_max']))/2)<=5
v=json.loads((d/'verification.json').read_text());assert v['disagreements']==0 and v['background_disagreements']==0
assert rows(p/'sequences/primer_pairs.csv')==a
for n,h in json.loads((p/'SHA256SUMS.json').read_text()).items():assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
print('PASS: ordinary/A/B/D identical coordinates, 16 pairs, thermal checks, independent verification, sequence consistency and hashes')
