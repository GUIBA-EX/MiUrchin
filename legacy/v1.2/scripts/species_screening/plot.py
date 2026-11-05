from pathlib import Path
import csv,json,html,collections,sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data.IUPACData import ambiguous_dna_values as I
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');n,reg=sys.argv[1:];project={'miurchin':'MiUrchin'}[n];repo=root/'outputs'/project;out=root/'outputs'/f'{project}_species_refine'/reg;p=root/'work'/f'{n}_species_refine'/reg
def read(path):return list(csv.DictReader(path.open()))
panel=read(root/'work'/f'{n}_species_qc'/f'panel_{reg}.csv');al={r.id:str(r.seq).upper() for r in SeqIO.parse(root/'work'/f'{n}_species_qc/target_aligned.fasta','fasta')};ref='NC_001453.1';cols=[i for i,c in enumerate(al[ref]) if c!='-'];coord=read(repo/'results/current/binding_positions.csv');co=next(x for x in coord if x['name']==(reg if reg=='XS' else reg+'D'));hits=collections.defaultdict(set)
for row in csv.DictReader((p/'verify/independent_hits.tsv').open(),delimiter='\t'):
 if row['role']=='target' and row['model']=='WC':
  for flag in ('exact','le2last3'):
   if row[flag]=='1':hits[row['name'],flag].add(row['accession'])
unknown=json.loads((root/'outputs'/f'{project}_species_qc/window_evaluability_summary.json').read_text())[reg]['unknown_species'];orders=sorted({r['order'] for r in panel});basedata=[]
for candidate in json.loads((p/'selection.json').read_text()):
 name=candidate['name'];w=1900;h=200+len(panel)*21+len(orders)*32+60;es=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#f7fbff"/>']
 def text(x,y,s,size=14,fill='#173647',mono=False):es.append(f'<text x="{x}" y="{y}" font-family="{ "DejaVu Sans Mono" if mono else "DejaVu Sans"},sans-serif" font-size="{size}" fill="{fill}">{html.escape(str(s))}</text>')
 def rect(x,y,wi,he,fill,stroke=None):es.append(f'<rect x="{x}" y="{y}" width="{wi}" height="{he}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>')
 text(22,38,f'{project} {name} | Primer–template base matching',24);text(22,68,f'{len(panel)} evaluable species; {unknown} species not evaluable at this length',17);text(22,93,'Blue: compatible  |  Orange: mismatch  |  Grey: gap  |  Box: final 3 nt  |  primer 5′ → 3′',15)
 fx,rx,cell=580,1200,19;text(22,133,'Species / accession',15);text(535,133,'Hit',15)
 for side,x in [('F',fx),('R',rx)]:
  primer=candidate[side];text(x,133,f"{side} {co[side+'_start']}–{co[side+'_end']}  |  variants {candidate['degeneracy_'+side]}",15)
  for j,c in enumerate(primer):rect(x+j*cell,143,18,21,'#cce7f0');text(x+j*cell+4,159,c,14,mono=True)
 y=180
 for order in orders:
  group=sorted((x for x in panel if x['order']==order),key=lambda x:(x['organism'],x['accession']));rect(16,y,w-32,25,'#e2eaf3');text(22,y+18,f'{order} | {len(group)} species',15);y+=30
  for i,row in enumerate(group):
   if i%2==0:rect(16,y,w-32,20,'#eef5f9')
   text(22,y+15,row['organism']+' / '+row['accession'],12);state='E' if row['accession'] in hits[name,'exact'] else 'C' if row['accession'] in hits[name,'le2last3'] else '–';text(540,y+15,state,14)
   for side,x in [('F',fx),('R',rx)]:
    a,b=int(co[side+'_start']),int(co[side+'_end']);template=''.join(al[row['accession']][cols[j]] for j in range(a-1,b));template=str(Seq(template).reverse_complement()) if side=='R' else template;primer=candidate[side];assert len(primer)==len(template),(name,side,len(primer),len(template));full=al[row['accession']][cols[a-1]:cols[b-1]+1];ins=sum(c!='-' for c in full)-sum(c!='-' for c in template)
    basedata.append(dict(name=name,side=side,order=order,species=row['organism'],accession=row['accession'],primer=primer,template=template,insertions=ins,full_scan_state=state))
    for j,c in enumerate(template):rect(x+j*cell,y,18,19,'#d6edf4' if c in I[primer[j]] else '#e3e8ee' if c not in 'ACGT' else '#ffd5a1');text(x+j*cell+4,y+14,c,13,mono=True)
    if ins:text(x+len(primer)*cell+4,y+14,'+'+str(ins),12)
   y+=21
 for side,x in [('F',fx),('R',rx)]:rect(x+(len(candidate[side])-3)*cell-1,142,3*cell+1,y-142,'none','#173647')
 text(22,y+24,'E = exact pair match; C = ≤2 mismatches per primer with final 3 nt compatible; – = no predicted hit.',13);text(22,y+45,'Cells show fixed homologous reference columns; +n indicates insertions. Hit status uses full-sequence scanning.',13);es.append('</svg>');(out/f'base_matching_{name}.svg').write_text(''.join(es))
if basedata:
 with (out/'base_matching.csv').open('w') as f:
  writer=csv.DictWriter(f,fieldnames=list(basedata[0]));writer.writeheader();writer.writerows(basedata)
print(project,reg,len(panel),'species plotted')
