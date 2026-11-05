from pathlib import Path
import json,subprocess
p=Path(__file__).resolve().parent;root=p.parents[1];pool=json.loads((p/'oligos.json').read_text());sites=p/'sites';sites.mkdir(exist_ok=True)
bg=p/'background.fasta'
if not bg.exists():bg.symlink_to(root/'work/miurchin_taxon_release/analysis/background.fasta')
(p/'reused_background_sites.tsv').write_text('');(sites/'oligos.tsv').write_text(''.join(f"{r['id']} {r['side']} {r['sequence']}\n" for r in pool))
subprocess.run([str(root/'work/micucumber_taxon_optimization/scan_sites'),str(sites)],check=True)
