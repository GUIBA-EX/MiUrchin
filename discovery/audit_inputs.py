from pathlib import Path
from Bio import SeqIO
import json,collections
p=Path(__file__).resolve().parent
D={n:list(SeqIO.parse(p/(n+'.fasta'),'fasta')) for n in ['target','background']}
for n,rs in D.items():assert len(rs)==len({r.id for r in rs});assert all(set(str(r.seq).upper())<=set('ACGTRYSWKMBDHVNX') for r in rs)
assert not {r.id for r in D['target']}&{r.id for r in D['background']}
a={r.id:str(r.seq).upper() for r in SeqIO.parse(p/'full_aligned.fasta','fasta')};b={r.id:str(r.seq).upper() for r in SeqIO.parse(p/'target_aligned.fasta','fasta')}
assert len(b)==len(D['target']);assert set(b)=={r.id for r in D['target']};assert len({len(x) for x in b.values()})==1
for k,v in a.items():assert b[k]==v
(p/'input_audit.json').write_text(json.dumps(dict(status='PASS',target=len(D['target']),background=len(D['background']),alignment_rows=len(b),backbone_rows_unchanged=len(a),alignment_columns=len(next(iter(b.values()))),same_accession_overlap=0),indent=2));print('PASS input and alignment invariants')
