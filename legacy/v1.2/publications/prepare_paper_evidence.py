"""Recalculate descriptive oligo properties and assemble archived result summaries."""
import csv,itertools,json,hashlib
from pathlib import Path
import primer3
from Bio.Data.IUPACData import ambiguous_dna_values as I
from paper_tables import ROOT,assays,deg,nesting,rows,table
out=ROOT/'publications/evidence';out.mkdir(exist_ok=True)
def save(file,data):
 with (out/file).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
def span(v,d=1):
 a,b=round(min(v),d),round(max(v),d)
 return f'{a:.{d}f}' if a==b else f'{a:.{d}f}–{b:.{d}f}'
props=[]
for a in assays():
 for side in 'FR':
  q=a[side];variants=[''.join(z) for z in itertools.product(*(I[b] for b in q))]
  kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6)
  p=dict(gene=a['gene'],assay=a['name'],side=side,sequence=q,nt=len(q),variants=len(variants),GC_range=span([100*sum(b in 'GC' for b in s)/len(s) for s in variants],0))
  for key,conc in [('Tm_50_range',50),('Tm_200_total_range',200/len(variants))]:p[key]=span([primer3.calc_tm(s,dna_conc=conc,**kw) for s in variants])
  props.append(p)
save('oligo_properties.csv',props);save('nesting.csv',nesting());save('assay_summary.csv',assays())
source=['results/current_primers/comparison.csv','sequences/primer_pairs.csv','figures/current_region_coordinates.csv','markers/12S_COI/candidates.csv','markers/28S/selected.csv','results/computational_evaluation/results/panel_comparison.csv','results/computational_evaluation/results/by_order.csv','results/computational_evaluation/results/resolution.csv','results/computational_evaluation/results/cv_summary.csv']
(out/'manifest.json').write_text(json.dumps(dict(primer3_py=primer3.__version__,source_sha256={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in source}),indent=2)+'\n')
supp='# MiUrchin supplementary material\n\n**Fei Xia**\n\n## Table S1. Oligo properties at a fixed total concentration\n\nEach direction contains 200 nM total primer, divided equally among its concrete variants. Calculations use 50 mM monovalent salt, 1.5 mM Mg²⁺ and 0.6 mM dNTP. These descriptive properties do not replace archived pairwise structure screening.\n\n'+table(['Gene','Oligo','Variants','Tm °C'],[[x['gene'],x['assay']+'-'+x['side'],x['variants'],x['Tm_200_total_range']] for x in props])
supp+='\n\n## Table S2. Conditional genus-blocked sequence-selection outcomes at 16S\n\nWindow discovery preceded the folds. Fold candidates use local alignment offsets and were not filtered by the complete release chemistry and background criteria.\n\n'+table(['Window','Test species','Covered','Exact'],[[x['region'],x['n'],x['covered'],x['exact']] for x in rows('results/computational_evaluation/results/cv_summary.csv')])
supp+='\n\n## Table S3. 16S reference-insert uniqueness\n\nThe common row restricts queries to the 49-species intersection but retains uniqueness defined against all evaluable, unambiguous same-window inserts. It is not a reclassification using only the common panel.\n\n'+table(['Window','Panel','N','Unique','Insert range bp'],[[x['region'],x['panel'],x['n'],x['identity_unique_species'],x['insert_min']+'–'+x['insert_max']] for x in rows('results/computational_evaluation/results/resolution.csv')])
supp+='\n\n## Table S4. Nuclear 28S barcode diagnostics\n\nBarcoded and unique counts reproduce the archived assay-specific target-barcode table. They are conditional on recovered inserts and use different species subsets from the 16S comparison.\n\n'+table(['Pair','Evaluable','Covered','Barcoded','Unique'],[[x['name'],x['n'],x['coverage'],x['barcoded'],x['unique']] for x in rows('markers/28S/selected.csv')])
supp+='\n\n[All order-level 16S results](../results/computational_evaluation/results/by_order.csv) · [Fold sequences](../results/computational_evaluation/results/cv_folds.csv) · [Accession-level nearest neighbors](../results/computational_evaluation/results/nearest_neighbors.csv) · [Oligo properties](evidence/oligo_properties.csv) · [Input hashes](evidence/manifest.json)\n'
(ROOT/'publications/MiUrchin_supplement.md').write_text(supp)
