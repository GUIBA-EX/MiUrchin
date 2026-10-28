from pathlib import Path
import csv,json,math,re,collections,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parents[1]
def read(f,delimiter=','):
 with f.open() as h:return list(csv.DictReader(h,delimiter=delimiter))
rows=read(p/'sequences/primer_pairs.csv');names=[r['name'] for r in rows];assert set(names)=={'XS','XSD','S','SD','M','MD','L','LD','XL','XLD'} and len(names)==len(set(names))
fa={}
for line in (p/'sequences/primers.fasta').read_text().splitlines():
 if line.startswith('>'):k=line[1:];assert k not in fa;fa[k]=''
 else:fa[k]+=line
assert len(fa)==20
I={'A':'A','C':'C','G':'G','T':'T','R':'AG','Y':'CT','S':'CG','W':'AT','K':'GT','M':'AC','B':'CGT','D':'AGT','H':'ACT','V':'ACG','N':'ACGT'}
coords={r['name']:r for r in read(p/'results/current/binding_positions.csv')};panel=read(p/'results/species_qc/panel.csv');assert len(panel)==len(set(r['species_key'] for r in panel))==165
metrics={r['name']:r for r in read(p/'results/current_primers/comparison.csv')};assert set(metrics)==set(names)
for r in rows:
 name=r['name'];d=p/'results/current_primers'/r['region'];m=metrics[name];check=json.loads((d/(name+'_verification.json')).read_text());assert check['disagreements']==check['background_disagreements']==0
 targets={x['accession'] for x in read(p/'results/species_qc'/('panel_'+r['region']+'.csv'))};h=collections.defaultdict(set)
 for x in read(d/(name+'_independent_hits.tsv'),'\t'):
  assert x['name']==name
  for flag in ('exact','le2last3','le2','le3','le4'):
   if x[flag]=='1':h[x['role'],x['model'],flag].add(x['accession'])
 assert len(h['target','WC','le2last3']&targets)==int(m['covered_labels']);assert len(h['target','WC','exact']&targets)==int(m['exact_labels'])
 for model,flag,col in [('WC','le3','WC3'),('GT','le2','GT2'),('WC','le4','WC4'),('WC','le2last3','strict_WC'),('GT','le2last3','strict_GT')]:assert len(h['background',model,flag])==int(m[col]),(name,col)
 for side in ('F','R'):
  q=r[side];assert fa['MiUrchin-'+name+'_'+side]==q;assert math.prod(len(I[c]) for c in q)==int(r['degeneracy_'+side]);c=read(d/(name+'_coordinates.csv'))[0] if r['region']=='XS' else coords[r['region']+'D'];assert len(q)==int(c[side+'_end'])-int(c[side+'_start'])+1
  if name.endswith('D'):assert int(r['degeneracy_'+side])<=8 and set(q[:len(q)//2])<=set('ACGT')
 for base in read(d/(name+'_base_matching.csv')):assert base['name']==name and base['primer']==r[base['side']]
 ET.parse(d/('base_matching_'+name+'.svg'))
 if name.endswith('D'):
  thermal=json.loads((d/(name+'_thermal.json')).read_text());assert all(v['structure_max']<55 and abs((v['F_tm_min']+v['F_tm_max']-v['R_tm_min']-v['R_tm_max'])/2)<=5 for v in thermal)
xs=read(p/'results/current_primers/XS/XS_coordinates.csv')[0];xsd=read(p/'results/current_primers/XS/XSD_coordinates.csv')[0]
assert all(xs[k]==xsd[k] for k in ('reference','F_start','F_end','R_start','R_end','reference_span_bp'))
for name in ('README.md','README.zh-CN.md'):
 f=p/name;s=f.read_text()
 for r in rows:assert f"| {r['name']} | `{r['F']}` | `{r['R']}` |" in s
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if not link.startswith(('http:','https:','#')):assert (f.parent/link.split('#')[0]).exists(),link
print('PASS:',len(rows),'pairs, target/background hit sets, coordinates, variants, thermal checks, base diagrams and bilingual links')
