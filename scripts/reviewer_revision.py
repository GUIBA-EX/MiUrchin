"""Supplemental frozen-reference reanalysis; not independent biological validation.
Run with Python 3.12, primer3-py 2.4.0 and a C++17 compiler.
Never changes released primer sequences or previously recorded results.
"""
from pathlib import Path
import json,csv,collections,subprocess,shutil,itertools,functools,hashlib,concurrent.futures,statistics
P=Path(__file__).resolve().parents[1]; O=P/'results/reviewer_revision';O.mkdir(exist_ok=True)
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']))
cat=json.loads((P/'results/catalog.json').read_text());rows=cat['originals']+cat['assays']; inputs={}
def digest(p):inputs[str(p.relative_to(P))]=hashlib.sha256(p.read_bytes()).hexdigest()
def table(name,rows):
 if not rows:return
 with (O/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def fasta(p):
 d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0];d[k]=''
  elif l.strip():d[k]+=l.strip().upper()
 return d
digest(P/'results/catalog.json');digest(P/'scripts/scan.cpp')
binary=O/'scan';subprocess.run(['c++','-O3','-std=c++17',str(P/'scripts/scan.cpp'),'-o',str(binary)],check=True)
def run(g):
 d=O/g;d.mkdir(exist_ok=True)
 for role in ['target','background']:
  f=P/'data'/g/(role+'.fasta');digest(f);shutil.copyfile(f,d/f.name)
 (d/'independent_primers.tsv').write_text(''.join('\t'.join([r['id'],r['F'],r['R']])+'\n' for r in rows if r['gene']==g))
 with (d/'scan.log').open('w') as log:subprocess.run([str(binary),str(d)],check=True,stdout=log,stderr=log)
 print('Scanned',g,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(run,['16S','12S','COI','28S']))
binary.unlink()
# Taxonomy labels are archival; retain unresolved records rather than invent assignments.
meta={}
for g in ['12S','COI']:
 f=P/f'legacy/v1.2/markers/12S_COI/{g}/target_panel.csv';digest(f)
 for r in csv.DictReader(f.open()):meta[g,r['accession']]={'species':r['species'],'order':r['order']}
f=P/'legacy/v1.2/analysis/target_taxonomy.tsv';digest(f)
for r in csv.DictReader(f.open(),delimiter='\t'):meta['16S',r['accession']]={'species':r['organism'],'order':r['order']}
f=P/'legacy/v1.2/markers/28S/target.fasta';digest(f)
for l in f.read_text().splitlines():
 if l.startswith('>'):
  a,sp=l[1:].split(' ',1);meta['28S',a]={'species':sp,'order':'unresolved'}
full=[];barstats=[];union=[];cross=[];hitsets={};barall=[]
for g in ['16S','12S','COI','28S']:
 d=O/g;target=fasta(d/'target.fasta');hs=collections.defaultdict(set)
 for h in csv.DictReader((d/'independent_hits.tsv').open(),delimiter='\t'):
  for flag in ['exact','le2last3','le2']:
   if h[flag]=='1':hs[h['name'],h['role'],h['model'],flag].add(h['accession'])
 bars=collections.defaultdict(lambda:collections.defaultdict(set))
 for h in csv.DictReader((d/'target_barcodes.tsv').open(),delimiter='\t'):bars[h['name']][h['accession']].add(h['sequence'])
 for r in [r for r in rows if r['gene']==g]:
  key=r['id'];cov=hs[key,'target','WC','le2last3'];ex=hs[key,'target','WC','exact'];hitsets[key]=cov
  panel=set(r.get('panel',[]));full.append(dict(gene=g,id=key,collection='supplementary' if 'panel' in r else 'primary',archived_target_records=len(target),covered_records=len(cov),exact_records=len(ex),design_records=len(panel),covered_outside_selected_panel=len(cov-panel) if panel else '',note='all archived records; not a completeness-filtered or independent denominator'))
  for order in sorted({meta.get((g,a),{}).get('order','unresolved') for a in target}):
   members={a for a in target if meta.get((g,a),{}).get('order','unresolved')==order};cross.append(dict(gene=g,id=key,archived_order=order,total_records=len(members),covered=len(cov&members),exact=len(ex&members)))
  owners=collections.defaultdict(set)
  for a,seqs in bars[key].items():
   sp=meta.get((g,a),{}).get('species')
   if sp:
    for seq in seqs:owners[seq].add(sp)
  single=0;unique=0;unknown=0
  for a,seqs in bars[key].items():
   sp=meta.get((g,a),{}).get('species','')
   if not sp:unknown+=1
   if len(seqs)==1 and sp:
    single+=1;unique+=len(owners[next(iter(seqs))])==1
   for seq in sorted(seqs):barall.append(dict(gene=g,id=key,accession=a,species=sp,sequence=seq,length=len(seq),same_assay_species_sharing=len(owners[seq])))
  barstats.append(dict(gene=g,id=key,covered_records=len(cov),records_with_unambiguous_insert=len(bars[key]),single_insert_named_records=single,single_insert_unique_among_recovered_records=unique,multiple_distinct_insert_records=sum(len(x)>1 for x in bars[key].values()),unmapped_records=unknown,shared_insert_sequences=sum(len(x)>1 for x in owners.values()),scope='identity only among recovered inserts; not full-library resolution, species assignment accuracy or barcode gap'))
 for parent in [r for r in cat['originals'] if r['gene']==g]:
  subs=[r for r in cat['assays'] if r['gene']==g and r['parent']==parent['parent']];u=set().union(*(hitsets[r['id']] for r in subs));base=hitsets[parent['id']]
  union.append(dict(gene=g,parent=parent['parent'],archived_target_records=len(target),separate_PCR_candidates=len(subs),original_covered=len(base),union_covered=len(u),gained=len(u-base),lost=len(base-u),shared=len(u&base),unmatched_or_incomplete=len(set(target)-u),scope='union of separate reactions on archived records, not a multiplex or independent test'))
 for role in ['target','background']:(d/(role+'.fasta')).unlink()
table('full_target_coverage.csv',full);table('separate_PCR_union.csv',union);table('order_cross_matching.csv',cross);table('recovered_insert_identity.csv',barstats);table('recovered_inserts.csv',barall)
# Apply the SAME screening rules to every original pair; report failures without replacing sequences.
import primer3
assert primer3.__version__=='2.4.0'
@functools.lru_cache(None)
def one(s,c):
 kw=dict(mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=c)
 return primer3.calc_tm(s,**kw),primer3.calc_hairpin(s,**kw).tm,primer3.calc_homodimer(s,**kw).tm
@functools.lru_cache(None)
def het(a,b,c):return primer3.calc_heterodimer(a,b,mv_conc=50,dv_conc=1.5,dntp_conc=.6,dna_conc=c).tm
thermal=[]
for r in cat['originals']:
 fv=list(map(''.join,itertools.product(*(I[x] for x in r['F']))));rv=list(map(''.join,itertools.product(*(I[x] for x in r['R']))))
 for scenario in ['50nM_per_variant','200nM_total_per_direction']:
  fc=50 if scenario.startswith('50') else 200/len(fv);rc=50 if scenario.startswith('50') else 200/len(rv)
  ft=[one(x,fc) for x in fv];rt=[one(x,rc) for x in rv];hair=max(x[1] for x in ft+rt);homo=max(x[2] for x in ft+rt)
  within=max([het(a,b,fc) for a,b in itertools.combinations(fv,2)]+[het(a,b,rc) for a,b in itertools.combinations(rv,2)]+[0]);fr=max(het(a,b,max(fc,rc)) for a in fv for b in rv);st=max(hair,homo,within,fr);lo=min(x[0] for x in ft+rt);hi=max(x[0] for x in ft+rt)
  delta=abs((min(x[0] for x in ft)+max(x[0] for x in ft)-min(x[0] for x in rt)-max(x[0] for x in rt))/2);reasons=[]
  if st>=55:reasons.append('structure_Tm_ge55')
  if lo<45 or hi>75:reasons.append('primer_Tm_outside45_75')
  if delta>5:reasons.append('midpoint_difference_gt5')
  thermal.append(dict(gene=r['gene'],id=r['id'],scenario=scenario,F_variants=len(fv),R_variants=len(rv),F_variant_nM=fc,R_variant_nM=rc,primer_min_Tm=lo,primer_max_Tm=hi,hairpin_max_Tm=hair,homodimer_max_Tm=homo,within_direction_max_Tm=within,FR_max_Tm=fr,structure_max_Tm=st,midpoint_difference=delta,minimum_margin=lo-st,screen_pass=not reasons,failed_rules=';'.join(reasons)))
table('primary_pair_structures.csv',thermal)
summary=dict(primary_pairs=32,supplementary_entries=76,design_panel_median=statistics.median(r['n_records'] for r in cat['assays']),design_panels_le5=sum(r['n_records']<=5 for r in cat['assays']),design_panels_eq3=sum(r['n_records']==3 for r in cat['assays']),primary_failures=sorted({r['id'] for r in thermal if not r['screen_pass']}),new_external_data=False,independent_validation=False,geometry='uniform 60-650 bp total, nonoverlapping primer sites, <=2 mismatches/end, final3 WC compatible; descriptive reanalysis not replacement of original denominators',primer3_version=primer3.__version__,input_sha256=inputs)
(O/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary)[:1500],flush=True)
