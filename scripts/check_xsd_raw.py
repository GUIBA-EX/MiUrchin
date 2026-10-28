"""Independently compare XS or XSD strict hit sets to raw references."""
from pathlib import Path
import csv, sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'scripts/species_screening'))
from xs_raw_helpers import fa,rc,scan
out=root/'results/current_primers/XS'
name=sys.argv[1] if len(sys.argv)>1 else 'XSD'
assert name in ('XS','XSD')
with (out/(name+'_independent_hits.tsv')).open() as f: rows=list(csv.DictReader(f,delimiter='\t'))
with (root/'results/species_qc/panel_XS.csv').open() as f: target_ids={r['accession'] for r in csv.DictReader(f)}
with (root/'sequences/primer_pairs.csv').open() as f: primer=next(r for r in csv.DictReader(f) if r['name']==name)
F,R=primer['F'],primer['R']
reference=fa(root/'analysis/target.fasta')['NC_001453.1']
for side,primer_seq,start in [('F',F,182),('R',R,343)]:
 matches=scan(reference,primer_seq,side=='R',2,False)
 assert any(pos==start and not last for pos,mm,last in matches),(name,side,'reference position')
for role in ('target','background'):
 db=fa(root/'analysis'/(role+'.fasta'))
 if role=='target':db={k:v for k,v in db.items() if k in target_ids};assert len(db)==len(target_ids)
 for model in (('WC',) if role=='target' else ('WC','GT')):
  observed=set();exact=set()
  for acc,s in db.items():
   for t in (s,rc(s)):
    for fp,fm,fl in scan(t,F,False,2,model=='GT'):
     for rp,rm,rl in scan(t,R,True,2,model=='GT'):
      inner=rp-fp-len(F);size=rp+len(R)-fp
      if not ((inner>=20 and 70<=size<=500) if role=='target' else (0<=inner<=1000)):continue
      if not fl and not rl:observed.add(acc)
      if fm==0 and rm==0:exact.add(acc)
  for flag,got in [('le2last3',observed),('exact',exact)]:
   expected={r['accession'] for r in rows if r['role']==role and r['model']==model and r[flag]=='1'}
   assert got==expected,(role,model,flag,len(got^expected))
   print(role,model,flag,len(got),'matched')
