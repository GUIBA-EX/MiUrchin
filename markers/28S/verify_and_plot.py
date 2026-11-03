"""Reconcile raw scan metrics and draw each primer-oriented binding matrix."""
import csv
from pathlib import Path
from html import escape
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data.IUPACData import ambiguous_dna_values as I
p=Path(__file__).resolve().parent
al={r.id.removeprefix('_R_'):str(r.seq).upper() for r in SeqIO.parse(p/'aligned.fa.out','fasta')}
species={r.id:r.description.split(' ',1)[1] for r in SeqIO.parse(p/'target.fasta','fasta')}
with (p/'independent_hits.tsv').open() as f:h=list(csv.DictReader(f,delimiter='\t'))
def text(x,y,s,size=13):return f'<text x="{x}" y="{y}" font-size="{size}">{escape(str(s))}</text>'
def box(x,y,w,h,c):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'
with (p/'selected.csv').open() as f:rows=list(csv.DictReader(f))
for q in rows:
 n=q['name'];l=int(q['start'])-1;r=int(q['end'])
 templates={a:(s[l:l+20],str(Seq(s[r-20:r]).reverse_complement())) for a,s in al.items()}
 panel={a for a,(f,z) in templates.items() if not set(f+z)-set('ACGT')}
 assert len(panel)==int(q['n'])
 sets={}
 for k,role,model,flag in [('coverage','target','WC','le2last3'),('exact','target','WC','exact'),('strictWC','background','WC','le2last3'),('strictGT','background','GT','le2last3'),('WC3','background','WC','le3'),('GT2','background','GT','le2')]:
  a={x['accession'] for x in h if x['name']==n and x['role']==role and x['model']==model and x[flag]=='1'}
  sets[k]=a&panel if role=='target' else a
  assert len(sets[k])==int(q[k]),(n,k)
 top=135;height=top+len(al)*19+12;svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 {height}" font-family="Arial,sans-serif" fill="#173647">',box(0,0,1240,height,'#f7fbff'),text(18,32,f'MiUrchin 28S {n} | Primer–template base matching',23),text(18,59,'Blue: compatible · Orange: mismatch · Grey: incomplete · Frames: terminal 3 nt · E: exact · C: covered · NA: unevaluable'),text(18,119,'Species / accession')]
 for side,x,t in [('F',410,f'{l+1}–{l+20}'),('R',825,f'{r-19}–{r}')]:
  svg.append(text(x,87,f'{side}  5′ → 3′   {t}',16))
  for j,b in enumerate(q[side]):svg.append(text(x+18*j,119,b))
 for i,a in enumerate(sorted(al,key=lambda a:species[a])):
  y=top+19*i;svg.extend([text(18,y+14,species[a]+' / '+a),text(370,y+14,'NA' if a not in panel else 'E' if a in sets['exact'] else 'C' if a in sets['coverage'] else '–')])
  for side,x,t in zip(('F','R'),(410,825),templates[a]):
   for j,b in enumerate(t):
    c='#d6edf4' if b in I[q[side][j]] else '#ffd5a1' if b in 'ACGT' else '#e3e8ee';svg.extend([box(x+18*j-3,y,17,18,c),text(x+18*j,y+14,b)])
 for x in (410,825):svg.append(f'<rect x="{x+17*18-4}" y="100" width="55" height="{height-110}" fill="none" stroke="#173647"/>')
 (p/'figures'/f'{n}.svg').write_text(''.join(svg)+'</svg>')
