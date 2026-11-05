from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1]
exclude={'SHA256SUMS.json','publications/SHA256SUMS.txt','publications/MiUrchin_Method_ResearchGate.md','publications/MiUrchin_Method_ResearchGate.pdf','publications/manuscript_provenance.json','publications/validation.json'}
files={}
for p in sorted(P.rglob('*')):
 rel=p.relative_to(P)
 if not p.is_file() or any(x in {'.git','.DS_Store','__pycache__'} for x in rel.parts) or str(rel) in exclude:continue
 files[str(rel)]=hashlib.sha256(p.read_bytes()).hexdigest()
(P/'SHA256SUMS.json').write_text(json.dumps(files,indent=2)+'\n')
(P/'publications/SHA256SUMS.txt').write_text(''.join(files[n]+'  '+n+'\n' for n in ['publications/MiUrchin_preprint.pdf','sequences/all_markers.fasta','sequences/priority.fasta','sequences/conditional.fasta','results/catalog.json']))
print('Stamped',len(files),'files')
