"""Fixed homologous-site audit adapted from the archived 2026-11-05 audit. No primer replacement."""
from pathlib import Path
import csv,json,collections,math,hashlib,html
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/'legacy/v1.2'; O=ROOT/'results/reviewer_revision'; O.mkdir(exist_ok=True); inputs={}
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT'])); rev={frozenset(v):k for k,v in I.items()}; comp=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN')
def read(p):
 inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest();return list(csv.DictReader(p.open()))
def fasta(p):
 inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest(); d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0].removeprefix('_R_');d[k]=''
  else:d[k]+=l.upper()
 return d
assays=[]; templates={}
for q in read(P/'results/current_primers/comparison.csv'):
 q['gene']='16S';assays.append(q)
 rows=read(P/f"results/current_primers/{q['region']}/{q['name']}_base_matching.csv")
 for side in ['F','R']:templates['16S',q['name'],side]=[dict(accession=r['accession'],species=r['species'],order=r['order'],template=r['template'],insertions=int(r['insertions'])) for r in rows if r['side']==side]
for gene in ['12S','COI']:
 d=P/'markers/12S_COI'/gene; al=fasta(d/'aligned.fasta');anchor=(d/'anchor.txt').read_text().strip();cols=[i for i,b in enumerate(al[anchor]) if b!='-'];panel=read(d/'target_panel.csv')
 for q in read(d/'pairs.csv'):
  q['gene']=gene;assays.append(q)
  for side in ['F','R']:
   a,b=[int(q[side+'_'+v])-1 for v in ['start','end']]; ts=[]
   for r in panel:
    s=al[r['accession']];t=''.join(s[i] for i in cols[a:b+1]);ins=sum(x!='-' for x in s[cols[a]:cols[b]+1])-sum(x!='-' for x in t)
    if side=='R':t=t.translate(comp)[::-1]
    ts.append(dict(accession=r['accession'],species=r['species'],order=r['order'],template=t,insertions=ins))
   templates[gene,q['name'],side]=ts
al=fasta(P/'markers/28S/aligned.fa.out'); species={}
for l in (P/'markers/28S/target.fasta').read_text().splitlines():
 if l.startswith('>'):a,sp=l[1:].split(' ',1);species[a]=sp
for q in read(P/'markers/28S/selected.csv'):
 q['gene']='28S';assays.append(q);a=int(q['start'])-1;b=int(q['end'])
 for side in ['F','R']:templates['28S',q['name'],side]=[dict(accession=k,species=species[k],order='',template=s[a:a+20] if side=='F' else s[b-20:b].translate(comp)[::-1],insertions=0) for k,s in al.items()]

rows=[];pairrows=[];detail=[]
for q in assays:
 sets={}
 for side in ['F','R']:
  primer=q[side];ts=templates[q['gene'],q['name'],side];valid=[r for r in ts if len(r['template'])==len(primer) and set(r['template'])<=set('ACGT') and not r['insertions']]
  sets[side]={r['accession']:r for r in valid}
  row=dict(gene=q['gene'],assay=q['name'],side=side,primer=primer,all_aligned_records=len(ts),complete_no_insertion_records=len(valid),excluded_records=len(ts)-len(valid),variants=math.prod(len(I[x]) for x in primer))
  for n in [1,3,5]:row['terminal'+str(n)+'_compatible']=sum(all(b in I[a] for a,b in zip(primer[-n:],r['template'][-n:])) for r in valid)
  row['full_exact']=sum(all(b in I[a] for a,b in zip(primer,r['template'])) for r in valid)
  rows.append(row)
  for r in ts:
   reason='complete' if r['accession'] in sets[side] else 'length_gap_ambiguity_or_insertion'
   detail.append(dict(gene=q['gene'],assay=q['name'],side=side,accession=r['accession'],species=r['species'],status=reason,template=r['template'],insertions=r['insertions']))
 common=set(sets['F'])&set(sets['R']);both=sum(all(all(b in I[a] for a,b in zip(q[side][-3:],sets[side][acc]['template'][-3:])) for side in ['F','R']) for acc in common)
 pairrows.append(dict(gene=q['gene'],assay=q['name'],both_complete_no_insertion=len(common),both_terminal3_compatible=both,scope='fixed homologous sites, not raw paired PCR coverage'))
for name,data in [('primary_terminal_audit.csv',rows),('primary_terminal_paired.csv',pairrows),('primary_site_audit.csv',detail)]:
 with (O/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]),lineterminator='\n');w.writeheader();w.writerows(data)
(O/'terminal_input_hashes.json').write_text(json.dumps({str(Path(k).relative_to(ROOT)):v for k,v in inputs.items()},indent=2)+'\n')
assert len(rows)==64 and len(pairrows)==32
print('64 oligos audited; 32 paired homologous site audits. Indel/incomplete exclusions retained.')
