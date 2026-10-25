from pathlib import Path
import csv,json,html,collections,sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data.IUPACData import ambiguous_dna_values as I
repo=Path(__file__).resolve().parents[1];p=repo/'results/D_optimization';from PIL import Image,ImageDraw,ImageFont
import matplotlib
fontdir=Path(matplotlib.get_data_path())/'fonts/ttf'
def read(f):return list(csv.DictReader(f.open()))
sel=json.loads((repo/'results/D_optimization/selected_D.json').read_text());panel=read(p/'panel.csv');al={r.id:str(r.seq).upper() for r in SeqIO.parse(repo/'analysis/target_aligned.fasta','fasta')};cols=[i for i,c in enumerate(al['NC_001453.1']) if c!='-'];coords={r['name']:r for r in read(repo/'results/current/binding_positions.csv')};metrics={r['scheme']:r for r in read(repo/'results/current/taxonomic_comparison.csv')};hits=collections.defaultdict(set)
for r in csv.DictReader((repo/'results/terminal_optimization/independent_hits.tsv').open(),delimiter='\t'):
 if r['role']=='target' and r['model']=='WC':
  for k in ['exact','le2last3']:
   if r[k]=='1':hits[r['name'],k].add(r['accession'])
orders=sorted({r['order'] for r in panel});W=2100;H=220+len(panel)*24+len(orders)*33+80;basedata=[]
for r in read(repo/'sequences/primer_pairs.csv'):
 name=r['name'];co=coords[name];m={}
 for mode,flag in [('coverage','le2last3'),('exact','exact')]:
  m['order_'+mode+'_pct']=100*sum(len({x['organism'] for x in panel if x['order']==o and x['accession'] in hits[name,flag]})/len({x['organism'] for x in panel if x['order']==o}) for o in orders)/len(orders)
 im=Image.new('RGB',(W,H),'#f7fbff');dr=ImageDraw.Draw(im);es=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#f7fbff"/>']
 def text(x,y,t,size=15,fill='#173647',mono=False):
  font='DejaVuSansMono.ttf' if mono else 'DejaVuSans.ttf';dr.text((x,y),str(t),font=ImageFont.truetype(str(fontdir/font),size),fill=fill,anchor='ls');es.append(f'<text x="{x}" y="{y}" font-family="{ "DejaVu Sans Mono" if mono else "DejaVu Sans"},sans-serif" font-size="{size}" fill="{fill}">{html.escape(str(t))}</text>')
 def rect(x,y,w,h,fill,stroke=None):
  if fill!='none':dr.rectangle((x,y,x+w,y+h),fill=fill)
  if stroke:dr.rectangle((x,y,x+w,y+h),outline=stroke,width=2)
  es.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>')
 text(28,46,'MiUrchin '+name+' | Primer–template base matching',30);text(28,80,f"Order-balanced coverage {float(m['order_coverage_pct']):.2f}%  |  Exact {float(m['order_exact_pct']):.2f}%  |  80 references / 49 labels / 11 orders",20)
 text(28,110,'Blue: IUPAC-compatible  ·  Orange: mismatch  ·  Grey: gap/unknown  ·  Box: final 3 nt  ·  Primer-oriented 5′ → 3′',17)
 fx=650;rx=1390;cell=23
 text(28,150,'Reference label / accession',17);text(594,150,'Hit',17)
 for side,xx in [('F',fx),('R',rx)]:
  q=r[side];text(xx,150,f"{side}  {co[side+'_start']}–{co[side+'_end']}  |  variants {r['degeneracy_'+side]}",18)
  for j,c in enumerate(q):rect(xx+j*cell,169,22,24,'#cce7f0');text(xx+j*cell+5,187,c,17,mono=True)
 y=212
 for o in orders:
  group=[x for x in panel if x['order']==o];rect(20,y,W-40,27,'#e2eaf3');text(28,y+20,o+'  |  '+str(len({x['organism'] for x in group}))+' labels',17);y+=33
  for k,x in enumerate(sorted(group,key=lambda x:(x['organism'],x['accession']))):
   if k%2==0:rect(20,y,W-40,23,'#eef5f9')
   text(28,y+17,x['organism']+' / '+x['accession'],14)
   state='E' if x['accession'] in hits[name,'exact'] else 'C' if x['accession'] in hits[name,'le2last3'] else '–';text(606,y+17,state,16)
   for side,xx in [('F',fx),('R',rx)]:
    a,b=int(co[side+'_start']),int(co[side+'_end']);t=''.join(al[x['accession']][cols[j]] for j in range(a-1,b));t=str(Seq(t).reverse_complement()) if side=='R' else t;q=r[side]
    full=al[x['accession']][cols[a-1]:cols[b-1]+1];insertions=sum(c!='-' for c in full)-sum(c!='-' for c in t)
    basedata.append(dict(name=name,side=side,order=o,label=x['organism'],accession=x['accession'],primer=q,template_reference_columns=t,inserted_bases=insertions,full_scan_state=state))
    for j,c in enumerate(t):rect(xx+j*cell,y,22,22,'#d6edf4' if c in I[q[j]] else '#e3e8ee' if c not in 'ACGT' else '#ffd5a1');text(xx+j*cell+5,y+17,c,16,mono=True)
    if insertions:text(xx+len(q)*cell+5,y+17,'+'+str(insertions),13)
   y+=24
 for side,xx in [('F',fx),('R',rx)]:rect(xx+(len(r[side])-3)*cell-1,168,3*cell+1,y-168,'none','#173647')
 text(28,y+33,'Hit: E = exact; C = ≤2 mismatches with compatible final 3 nt; – = not covered in the full-sequence scan.',16)
 text(28,y+59,'Cells follow homologous reference columns; +n marks inserted bases. Full-sequence scores are verified independently.',16)
 es.append('</svg>');svg=''.join(es)
 for folder in [repo/'figures',repo/'results/terminal_optimization']:(folder/f'base_matching_{name}.svg').write_text(svg)
 im.save(repo/'figures'/f'base_matching_{name}.png')
with (repo/'results/D_optimization/base_matching.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(basedata[0]),lineterminator='\n');w.writeheader();w.writerows(basedata)
# Keep the full gallery, including unchanged ordinary/A/B figures.
names=[r['name'] for r in read(repo/'sequences/primer_pairs.csv')]
(repo/'results/terminal_optimization/base_matching.html').write_text('<!doctype html><meta charset="utf-8"><title>MiUrchin base matching</title><style>body{font:16px/1.6 system-ui;margin:25px;color:#173647}img{max-width:100%}</style><h1>MiUrchin · Base matching / 碱基匹配</h1><p>D plots: fixed reference columns, WoRMS orders, independently checked raw hits.</p>'+''.join(f'<h2>{n}</h2><img src="../../figures/base_matching_{n}.svg">' for n in names))
print('Sixteen SVG/PNG base figures, source table and gallery generated')
