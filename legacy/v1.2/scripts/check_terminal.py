from pathlib import Path
import csv,json,itertools,math
p=Path(__file__).resolve().parents[1];I=dict(A='A',C='C',G='G',T='T',R='AG',Y='CT',S='CG',W='AT',K='GT',M='AC',B='CGT',D='AGT',H='ACT',V='ACG',N='ACGT')
def read(f):return list(csv.DictReader(f.open()))
rows=read(p/'results/current/primer_pairs.csv');unique={r['name']:r for r in rows}
for r in unique.values():
 for side in ['F','R']:
  for t in map(''.join,itertools.product(*(I[c] for c in r[side]))):
   assert len(set(t[-3:]))>1 and any(c in 'GC' for c in t[-3:]),(r['name'],side,t)
   assert 1<=sum(c in 'GC' for c in t[-5:])<=4
   assert not any(c*5 in t for c in 'ACGT')
for r in read(p/'results/terminal_optimization/thermal.csv'):
 assert float(r['structure_max'])<55
 assert abs((float(r['F_tm_min'])+float(r['F_tm_max'])-float(r['R_tm_min'])-float(r['R_tm_max']))/2)<=5
ref='';collect=False
for line in (p/'analysis/target_aligned.fasta').read_text().splitlines():
 if line.startswith('>'):collect=line[1:].split()[0]=='NC_001453.1'
 elif collect:ref+=line.upper().replace('-','')
assert ref
coords=read(p/'results/current/binding_positions.csv');assert {r['name'] for r in coords}==set(unique)
for r in coords:
 for side in ['F','R']:
  a,b=int(r[side+'_start']),int(r[side+'_end']);q=unique[r['name']][side];assert b-a+1==len(q)
  t=ref[a-1:b]
  if side=='R':t=t.translate(str.maketrans('ACGT','TGCA'))[::-1]
  assert t==r[side+'_reference_5to3'] and q==r[side+'_sequence']
  assert sum(c not in I[n] for n,c in zip(q,t))==int(r[side+'_reference_mismatches'])
 assert int(r['reference_span_bp'])==int(r['R_end'])-int(r['F_start'])+1
assert next(r['reference_span_bp'] for r in coords if r['name']=='L')=='343'
verification=json.loads((p/'results/terminal_optimization/verification.json').read_text())
assert verification['checks']==len(unique)*80*2 and verification['background_checks']==len(unique)*2 and verification['background_disagreements']==0
print('PASS: all concrete variant terminal rules, both concentration scenarios, 16 reference intervals, sequence lengths and reference bases')
