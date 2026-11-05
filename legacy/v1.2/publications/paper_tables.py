"""Build paper tables directly from the frozen marker-specific result files."""
import csv,itertools,math
from pathlib import Path
from Bio.Data.IUPACData import ambiguous_dna_values as I
ROOT=Path(__file__).resolve().parents[1]
def rows(path):
 with (ROOT/path).open() as f:return list(csv.DictReader(f))
def table(columns,records):
 return '\n'.join('| '+' | '.join(map(str,r))+' |' for r in [columns,['---']*len(columns),*records])
def assays():
 own={r['name']:r for r in rows('results/computational_evaluation/results/panel_comparison.csv') if r['panel']=='own'}
 coords={r['locus']:r for r in rows('figures/current_region_coordinates.csv')};out=[]
 for r in rows('results/current_primers/comparison.csv'):
  a=own[r['name']];out.append(dict(gene='16S',name=r['name'],region=r['region'],F=r['F'],R=r['R'],n=a['n'],covered=a['covered'],exact=a['exact'],WC=r['strict_WC'],GT=r['strict_GT'],WC3=r['WC3'],GT2=r['GT2'],**{k:coords[r['region']][k] for k in ['F_start','F_end','R_start','R_end']},span=coords[r['region']]['reference_span_bp']))
 for r in rows('markers/12S_COI/candidates.csv'):
  out.append(dict(gene=r['gene'],name=r['name'],region=r['window'],n=r['evaluable'],**{k:r[k] for k in ['F','R','covered','exact','WC','GT','WC3','GT2','F_start','F_end','R_start','R_end','span']}))
 for r in rows('markers/28S/selected.csv'):
  out.append(dict(gene='28S',name=r['name'],region=r['region'],F=r['F'],R=r['R'],n=r['n'],covered=r['coverage'],exact=r['exact'],WC=r['strictWC'],GT=r['strictGT'],WC3=r['WC3'],GT2=r['GT2'],F_start=r['start'],F_end=str(int(r['start'])+len(r['F'])-1),R_start=str(int(r['end'])-len(r['R'])+1),R_end=r['end'],span=str(int(r['end'])-int(r['start'])+1)))
 return out
def deg(s):return math.prod(len(I[b]) for b in s)
def nesting():
 rr=assays();out=[]
 for a in rr:
  if a['name'].endswith('D'):continue
  b=next(x for x in rr if x['gene']==a['gene'] and x['name']==a['name']+'D')
  assert all(a[k]==b[k] for k in ['F_start','F_end','R_start','R_end'])
  bad=[f'{side}{i+1}: {x}>{y}' for side in 'FR' for i,(x,y) in enumerate(zip(a[side],b[side])) if x not in I[y]]
  out.append(dict(gene=a['gene'],pair=b['name'],nested='No' if bad else 'Yes',excluded='; '.join(bad) or 'None',n=a['n'],ordinary_covered=a['covered'],D_covered=b['covered'],ordinary_exact=a['exact'],D_exact=b['exact']))
 return out
def tables():
 properties={(x['gene'],x['assay'],x['side']):x for x in rows('publications/evidence/oligo_properties.csv')}
 records=[]
 for a in assays():
  for side in 'FR':
   p=properties[a['gene'],a['name'],side];records.append([a['gene'],a['name']+'-'+side,a[side],len(a[side]),deg(a[side]),p['GC_range'],p['Tm_50_range']])
 t1='## Table 1. Oligos and predicted properties\n\nAll sequences run 5′–3′. Variant count is per end. GC and Tm ranges span all concrete variants; Tm uses 50 nM per variant. The 200 nM-per-direction scenario is supplied in the supplementary data.\n\n'+table(['Gene','Oligo','Sequence','nt','Variants','GC %','Tm °C'],records)
 common={x['name']:x for x in rows('results/computational_evaluation/results/panel_comparison.csv') if x['panel']=='common'}
 records=[]
 for a in assays():
  c=common.get(a['name']) if a['gene']=='16S' else None
  records.append([a['gene'],a['name'],a['span'],f"{a['covered']}/{a['n']}",f"{a['exact']}/{a['n']}",f"{c['covered']}/{c['n']}" if c else 'NA',f"{c['exact']}/{c['n']}" if c else 'NA',a['WC']+'/'+a['GT'],a['WC3']+'/'+a['GT2']])
 t2='## Table 2. Predicted target and background matches\n\nSpan is the primer-inclusive reference interval, not an observed product-length distribution. Common denotes the 49-species 16S intersection. NA indicates that a common-panel comparison was not performed for that marker. Strict and relaxed columns give WC/GT hits. Background units are records for 16S and 28S and one representative per species for 12S and COI.\n\n'+table(['Gene','Pair','Span bp','Own covered','Own exact','Common covered','Common exact','Strict bg','Relaxed bg'],records)
 t3='## Table 3. Ordinary-to-D sequence inclusion audit\n\nA nested D pair includes both ordinary oligos among its concrete variants. Positions run from the 5′ end in synthesis orientation. Excluded ordinary bases identify coupled sequence replacement; this audit is not a factorial re-screen of hypothetical intermediates. All pairs have identical reference endpoints.\n\n'+table(['Gene','D pair','Nested','Excluded ordinary bases','N','Covered O/D','Exact O/D'],[[x['gene'],x['pair'],x['nested'],x['excluded'],x['n'],x['ordinary_covered']+'/'+x['D_covered'],x['ordinary_exact']+'/'+x['D_exact']] for x in nesting()])
 return '\n\n'.join([t1,t2,t3])+'\n\n[Supplementary material](MiUrchin_supplement.md)\n'
