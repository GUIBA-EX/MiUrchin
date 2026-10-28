from pathlib import Path
import csv,json,math,re,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parents[1]
def read(f):
 with f.open() as h:return list(csv.DictReader(h))
rows=read(p/'sequences/primer_pairs.csv');names=[r['name'] for r in rows];assert len(names)==len(set(names)) and not any(re.fullmatch(r'(?:S|M|L|XL)[AB]',n) for n in names)
fa={}
for line in (p/'sequences/primers.fasta').read_text().splitlines():
 if line.startswith('>'):k=line[1:];assert k not in fa;fa[k]=''
 else:fa[k]+=line
assert len(fa)==2*len(rows)
I={'A':'A','C':'C','G':'G','T':'T','R':'AG','Y':'CT','S':'CG','W':'AT','K':'GT','M':'AC','B':'CGT','D':'AGT','H':'ACT','V':'ACG','N':'ACGT'}
coords={r['name']:r for r in read(p/'results/current/binding_positions.csv')};panel=read(p/'results/species_qc/panel.csv');assert len(panel)==len(set(r['species_key'] for r in panel))==165
for r in rows:
 for side in ('F','R'):
  q=r[side];assert fa['MiUrchin-'+r['name']+'_'+side]==q;assert math.prod(len(I[c]) for c in q)==int(r['degeneracy_'+side]);c=coords[r['region']+'D'];assert len(q)==int(c[side+'_end'])-int(c[side+'_start'])+1
  if r['name'] not in ('S','M','L','XL'):assert int(r['degeneracy_'+side])<=8 and set(q[:len(q)//2])<=set('ACGT')
 if r['name'] not in ('S','M','L','XL'):
  d=p/'results/species_refine'/r['region'];selection=json.loads((d/'selected.json').read_text());thermal=next(z['thermal'] for z in selection if z['name']==r['name']);assert all(v['structure_max']<55 and abs((v['F_tm_min']+v['F_tm_max']-v['R_tm_min']-v['R_tm_max'])/2)<=5 for v in thermal);v=json.loads((d/'verification.json').read_text());assert v['disagreements']==v['background_disagreements']==0;x=next(z for z in read(d/'verified_comparison.csv') if z['name']==r['name']);assert (r['F'],r['R'])==(x['F'],x['R']);ET.parse(d/('base_matching_'+r['name']+'.svg'))
for name in ('README.md','README.zh-CN.md'):
 f=p/name
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not link.startswith(('http:','https:','#')):assert (f.parent/link.split('#')[0]).exists(),link
print('PASS:',len(rows),'primer pairs, species panel, coordinates, variants, independent checks and links')
