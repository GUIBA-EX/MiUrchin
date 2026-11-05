from pathlib import Path
from Bio import SeqIO
import csv,sys,collections,json,shutil
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');n=sys.argv[1];proj={'miurchin':'MiUrchin'}[n];p=root/'work'/f'{n}_species_qc';out=root/'outputs'/f'{proj}_species_qc';repo=root/'outputs'/proj;ref='NC_001453.1';al={x.id:str(x.seq).upper() for x in SeqIO.parse(p/'target_aligned.fasta','fasta')};cols=[i for i,ch in enumerate(al[ref]) if ch!='-'];co={x['name']:x for x in csv.DictReader((repo/'results/current/binding_positions.csv').open())};panel=list(csv.DictReader((out/'panel.csv').open()));events=[];summary={}
for reg in ['S','M','L','XL']:
 c=co[reg if reg=='XS' else reg+'D'];valid=[]
 for x in panel:
  seq=al[x['accession']];first=next((i for i,ch in enumerate(seq) if ch!='-'),len(seq));last=next((len(seq)-1-i for i,ch in enumerate(reversed(seq)) if ch!='-'),-1);ok=True;details=[]
  for side in ['F','R']:
   a,b=cols[int(c[side+'_start'])-1],cols[int(c[side+'_end'])-1];t=seq[a:b+1];q=int(c[side+'_end'])-int(c[side+'_start'])+1;f=first<=a and last>=b and sum(ch in 'ACGT' for ch in t)>=.9*q and all(ch in 'ACGT-' for ch in t);ok &= f;details.append('complete' if f else 'missing_or_uncertain')
  events.append(dict(region=reg,accession=x['accession'],organism=x['organism'],order=x['order'],evaluable=int(ok),F=details[0],R=details[1]));
  if ok:valid.append(x)
 for x in valid:x=dict(x)
 path=p/f'panel_{reg}.csv'
 with path.open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(panel[0]));w.writeheader();w.writerows(valid)
 summary[reg]={'evaluable_species':len(valid),'unknown_species':len(panel)-len(valid),'evaluable_by_order':dict(collections.Counter(x['order'] for x in valid))}
 shutil.copy2(path,out/path.name)
 print(proj,reg,summary[reg],flush=True)
with (out/'window_evaluability.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(events[0]));w.writeheader();w.writerows(events)
(out/'window_evaluability_summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False));shutil.copy2(p/'representatives.fasta',out/'representatives.fasta');shutil.copy2(p/'target_aligned.fasta',out/'curated_alignment.fasta');shutil.copy2(p/'mafft.log',out/'mafft.log')
# Frozen representative full source sequences remain in original source orientation for raw scanner.
source=root/'work'/'miurchin'/'target.fasta';ids={x['accession'] for x in panel}
with (p/'target.fasta').open('w') as f:SeqIO.write((r for r in SeqIO.parse(source,'fasta') if r.id in ids),f,'fasta')
assert {r.id for r in SeqIO.parse(p/'target.fasta','fasta')}==ids
