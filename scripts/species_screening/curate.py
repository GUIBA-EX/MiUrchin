from pathlib import Path
from Bio import SeqIO
from Bio.Seq import Seq
import csv,json,collections,re,sys,hashlib
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');n=sys.argv[1];project={'miurchin':'MiUrchin'}[n];source=root/'work'/'miurchin';repo=root/'outputs'/project;out=root/'outputs'/f'{project}_species_qc';out.mkdir(exist_ok=True);work=root/'work'/f'{n}_species_qc';work.mkdir(exist_ok=True)
ref='NC_001453.1';alpath=source/'target_aligned.fasta';raw={r.id:r for r in SeqIO.parse(source/'target.fasta','fasta')};al={r.id.removeprefix('_R_'):str(r.seq).upper() for r in SeqIO.parse(alpath,'fasta')};cols=[i for i,b in enumerate(al[ref]) if b!='-'];coords={x['name']:x for x in csv.DictReader((repo/'results/current/binding_positions.csv').open())};windows=[coords[x+'D'] for x in ['S','M','L','XL']];wmaps={x['name']:[(cols[int(x[side+'_start'])-1],cols[int(x[side+'_end'])-1]) for side in ['F','R']] for x in windows}
tax={x['name']:x for x in json.load((root/'work/miurchin_species_qc/gbif_matches.json').open())};accepted=json.load((root/'work/miurchin_species_qc/gbif_accepted.json').open());ncbi=json.load((root/'work/miurchin_species_qc/ncbi_fuzzy_resolution.json').open());
def sub(a,b):
 it=iter(b);return bool(a) and all(any(c==x for x in it) for c in a)
worms={x["name"]:x for x in json.load((root/"work/miurchin_species_qc/taxonomy.json").open())}
def classify(label):
 if not re.fullmatch(r"[A-Z][A-Za-z-]+ [a-z][a-z-]+",label):return None,"unidentified_or_non_species",None,None
 x=worms.get(label,{}); rec=x.get("record",{}); order=x.get("order"); key=rec.get("valid_AphiaID") or rec.get("AphiaID");canonical=rec.get("valid_name") or rec.get("scientificname")
 if rec.get("rank", "").lower() != "species" or not key or not order or not canonical:return None,"taxon_unresolved",None,None
 return str(key),"worms_"+str(rec.get("status","unknown")),canonical,order

rows=[];bykey=collections.defaultdict(list)
for acc,r in raw.items():
 label=r.description[len(r.id):].strip();key,tax_status,canonical,order=classify(label);q=str(r.seq).upper();a=al.get(acc,'');ungapped=a.replace('-','');rev=str(Seq(q).reverse_complement());orient='forward' if ungapped and ungapped in q else 'reverse' if ungapped and ungapped in rev else 'forward' if sub(ungapped,q) else 'reverse' if sub(ungapped,rev) else 'invalid';
 oriented=q if orient=='forward' else rev if orient=='reverse' else '';first=next((i for i,c in enumerate(a) if c!='-'),len(a));last=next((len(a)-1-i for i,c in enumerate(reversed(a)) if c!='-'),-1);window_results={};knowncols=set()
 for w,sites in wmaps.items():
  flag=True
  for a0,b0 in sites:
   region=a[a0:b0+1];knowncols.update(i for i in range(a0,b0+1) if i<len(a) and a[i] in 'ACGT');validbases=sum(c in 'ACGT' for c in region);needs=(sum(1 for i in cols if a0<=i<=b0));flag &= first<=a0 and last>=b0 and validbases>=.9*needs and all(c in 'ACGT-' for c in region)
  window_results[w]=bool(flag)
 locus_amb=sum(c not in 'ACGT' for c in ungapped);acgt=sum(c in 'ACGT' for c in ungapped);failure=''
 if orient=='invalid':failure='alignment_not_subsequence_of_source'
 elif acgt<100:failure='fewer_than_100_aligned_acgt_bases'
 elif locus_amb/max(1,len(ungapped))>0.05:failure='more_than_5pct_ambiguous_bases'
 elif not any(window_results.values()):failure='no_evaluable_primer_window'
 if not key:reason=tax_status
 elif failure:reason=failure
 else:reason='eligible'
 row=dict(accession=acc,original_name=label,species_key=key or '',accepted_name=canonical or '',order=order or '',taxonomy_status=tax_status,source_raw_len=len(q),aligned_acgt=acgt,aligned_ambiguous=locus_amb,orientation=orient,aligned_is_contiguous=(ungapped in oriented if oriented else False),reference_columns_present=len(knowncols),windows_complete=sum(window_results.values()),**{f'window_{w}':int(v) for w,v in window_results.items()},quality_status=reason,selection='')
 rows.append(row)
 if reason=='eligible':bykey[key].append(row)
# One representative per validated or documented NCBI species, chosen without reference to primer-match outcomes.
panel=[];selected=set()
for key,rr in sorted(bykey.items()):
 rr.sort(key=lambda x:(-x['windows_complete'],x['aligned_ambiguous'],-x['reference_columns_present'],not x['aligned_is_contiguous'],-x['aligned_acgt'],x['accession']))
 best=rr[0];selected.add(best['accession']);best['selection']='retained';panel.append(dict(accession=best['accession'],organism=best['accepted_name'],label=best['accepted_name'],order=best['order'],weight=0,original_name=best['original_name'],species_key=key,taxonomy_status=best['taxonomy_status'],windows_complete=best['windows_complete']))
 for x in rr[1:]:x['selection']='excluded_duplicate_species'
for x in rows:
 if not x['selection']:x['selection']='excluded_'+x['quality_status']
for x in panel:x['weight']=1/len(panel)
with (out/'panel.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(panel[0]));w.writeheader();w.writerows(panel)
with (out/'sequence_audit.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
# Recover original bases; long mitochondrial genomes are trimmed to the aligned gene span.
written=[]
with (work/'representatives.fasta').open('w') as f:
 for x in panel:
  acc=x['accession'];r=raw[acc];q=str(r.seq).upper();a=al[acc].replace('-','');orient=next(z['orientation'] for z in rows if z['accession']==acc);q=q if orient=='forward' else str(Seq(q).reverse_complement())
  if len(q)>2500:
   if a in q:i=q.index(a);q=q[i:i+len(a)]
   else:
    pos=-1;indices=[]
    for c in a:
     pos=q.find(c,pos+1)
     if pos<0:raise ValueError(('not subsequence',acc))
     indices.append(pos)
    q=q[indices[0]:indices[-1]+1]
  f.write('>'+acc+' '+x['organism']+'\n'+q+'\n');written.append(acc)
 assert len(written)==len(set(written))==len(panel)
# Reference anchor is a technical alignment coordinate, not an extra species record.
(work/'alignment_input.fasta').write_bytes((work/'representatives.fasta').read_bytes())
if ref not in written:
 r=raw[ref];a=al[ref].replace('-','');q=str(r.seq).upper();rev=str(Seq(q).reverse_complement());q=q if sub(a,q) else rev
 with (work/'alignment_input.fasta').open('a') as f:f.write('>'+ref+' reference-coordinate-anchor not in species panel\n'+q+'\n')
counts=collections.Counter(x['selection'] for x in rows);orders=collections.Counter(x['order'] for x in panel);print(project,'input',len(rows),'species reps',len(panel),'orders',dict(orders),'audit',dict(counts),'anchor additional',ref not in written,flush=True)
summary=dict(project=project,original_sequences=len(rows),retained_species=len(panel),retained_by_order=dict(orders),statuses=dict(counts),additional_alignment_anchor=ref not in written,reference=ref,quality_policy='full bound windows, ambiguous bases, aligned position extent and source consistency; no primer-match used for representative selection',taxonomy='GBIF exact species/accepted usage; unresolved records excluded');(out/'summary.json').write_text(json.dumps(summary,indent=2))
