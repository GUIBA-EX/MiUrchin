from pathlib import Path
import csv,json,sys,shutil
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni')
n,reg=sys.argv[1:3]; pairmode=len(sys.argv)>3 and sys.argv[3]=='pair'; project={'miurchin':'MiUrchin'}[n]
regionpath=root/'work'/f'{n}_species_refine'/reg; p=regionpath/'pair' if pairmode else regionpath; p.mkdir(exist_ok=True)
out=root/'outputs'/f'{project}_species_refine'/reg
if pairmode:out=out/'pair';out.mkdir(exist_ok=True)
v=p/'verify';v.mkdir(exist_ok=True)
panel=list(csv.DictReader((root/'work'/f'{n}_species_qc'/f'panel_{reg}.csv').open()))
ids={x['accession'] for x in panel}
sys.path.insert(0,str(root/'outputs/MiCucumber/scripts'))
from xs_raw_helpers import fa
target=fa(root/'work'/f'{n}_species_qc/target.fasta')
(v/'target.fasta').write_text(''.join(f'>{acc}\n{target[acc]}\n' for acc in sorted(ids)))
bg=root/'work'/'miurchin'/'background.fasta'
link=v/'background.fasta'
if link.is_symlink() or link.exists():link.unlink()
link.symlink_to(bg)
selections=json.loads((regionpath/'pair_comparison.json').read_text())['pairs'] if pairmode else json.loads((p/'selection.json').read_text())
if pairmode:
 for x in selections:
  for k in ('pred_order_coverage','pred_order_exact'):x[k]=float(x[k])
  for k in ('WC3','GT2','WC4','strict_WC','strict_GT','degeneracy_F','degeneracy_R'):x[k]=int(x[k])
rows=list(csv.DictReader((root/'outputs'/project/'sequences/primer_pairs.csv').open()))
baseline=next(x for x in rows if x['scheme']==reg+'D')
baseline=dict(name=f'{reg}-baseline',region=reg,F=baseline['F'],R=baseline['R'],degeneracy_F=int(baseline['degeneracy_F']),degeneracy_R=int(baseline['degeneracy_R']),baseline=True)
sel=selections if pairmode else selections+[baseline]
(p/'verification_selection.json').write_text(json.dumps(sel,indent=2))
(v/'independent_primers.tsv').write_text(''.join(f"{x['name']}\t{x['F']}\t{x['R']}\n" for x in sel))
src=(root/'work'/f'{n}_3prime8/verify_raw.py').read_text()
start=src.index('p=Path(__file__)');end=src.index('\nh=collections.defaultdict(set)',start)
scanner=root/'work'/('micucumber_nondegenerate/independent_scan.cpp')
header=f"p=Path({str(p)!r});root=Path({str(root)!r});sys.path.insert(0,str(root/'outputs/MiCucumber/scripts'))\nfrom xs_raw_helpers import fa,rc,scan\nout=Path({str(out)!r});sel=json.loads((p/'verification_selection.json').read_text());v=p/'verify';src=Path({str(scanner)!r});subprocess.run(['c++','-O3','-std=c++17',str(src),'-o',str(v/'independent_scan')],check=True);subprocess.run([str(v/'independent_scan'),str(v)],check=True)"
src=src[:start]+header+src[end:]
src=src.replace("panel=list(csv.DictReader((p/'panel.csv').open()))",f"panel=list(csv.DictReader(Path({str(root/'work'/f'{n}_species_qc'/f'panel_{reg}.csv')!r}).open()))")
oldtarget="target=fa(root/'outputs/MiUrchin/analysis/target.fasta');background=fa(root/'outputs/MiUrchin/analysis/background.fasta')"
src=src.replace(oldtarget,"target=fa(v/'target.fasta');background=fa(v/'background.fasta')")
src=src.replace(";assert row[col]==int(x[col]),(name,col,row[col],x[col])",";assert x.get('baseline') or row[col]==x[col],(name,col,row[col],x.get(col))")
src=src.replace("row['prediction_coverage_delta_pp']=row['order_coverage_pct']-float(x['pred_order_coverage']);row['prediction_exact_delta_pp']=row['order_exact_pct']-float(x['pred_order_exact'])", "row['prediction_coverage_delta_pp']=row['order_coverage_pct']-x['pred_order_coverage'] if not x.get('baseline') else '';row['prediction_exact_delta_pp']=row['order_exact_pct']-x['pred_order_exact'] if not x.get('baseline') else ''")
(p/'verify_species.py').write_text(src)
print(n,reg,'evaluable',len(panel),'candidates',len(sel))
