"""Verify all four assay panels, manuscript tables and PDF sequences."""
import hashlib
import json
import re
import subprocess
from paper_tables import ROOT, tables

p=ROOT/'publications'
md=(p/'MiUrchin_preprint.md').read_text()
assert md.split('## Table 1.')[1]==tables().split('## Table 1.')[1]
for link in re.findall(r'\]\(([^)]+)\)',md):
    if not link.startswith('https://'):assert (p/link).is_file(),link
pdf=p/'MiUrchin_preprint.pdf'
text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
for line in (ROOT/'sequences/all_markers.fasta').read_text().splitlines():
    if line and not line.startswith('>'):assert line in text,line
pages=[page for page in text.split('\f') if page.strip()]
assert all(len(page.strip())>150 for page in pages)
inputs=['sequences/all_markers.fasta','results/current_primers/comparison.csv','markers/12S_COI/candidates.csv','markers/28S/selected.csv']
inputs+=['results/computational_evaluation/results/'+f+'.csv' for f in ['panel_comparison','by_order','resolution','cv_summary']]
digest=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
(p/'preprint_provenance.json').write_text(json.dumps({'inputs':{f:digest(ROOT/f) for f in inputs},'artifacts':{f.name:digest(f) for f in [p/'MiUrchin_preprint.md',pdf]}},indent=2)+'\n')
(p/'preprint_validation.json').write_text(json.dumps(dict(project='MiUrchin',author='Fei Xia',pages=len(pages),oligos=64,status='PASS'),indent=2)+'\n')
