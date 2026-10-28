from pathlib import Path
import sys,json,csv,itertools,collections,functools,math,random
REG=sys.argv[1]
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Data.IUPACData import ambiguous_dna_values as I
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');sys.path.insert(0,str(root/'work/milily'));from common import terminal,deg,expand
repo=root/'outputs/MiUrchin';out=root/'outputs/MiUrchin_species_refine'/REG;out.mkdir(exist_ok=True);p=Path(__file__).parent/REG;p.mkdir(exist_ok=True)
panel=list(csv.DictReader((root/'work/miurchin_species_qc'/f'panel_{REG}.csv').open()));al={r.id:str(r.seq).upper() for r in SeqIO.parse(root/'work/miurchin_species_qc/target_aligned.fasta','fasta')};cols=[i for i,b in enumerate(al['NC_001453.1']) if b!='-'];coords={r['name']:r for r in csv.DictReader((repo/'results/current/binding_positions.csv').open())};prev=json.loads((root/'work/miurchin_taxon_optimization/oligos.json').read_text());current=list(csv.DictReader((repo/'sequences/primer_pairs.csv').open()))
labels=sorted(set(r['organism'] for r in panel));orders=sorted(set(r['order'] for r in panel)); lb={n:sum(1<<i for i,r in enumerate(panel) if r['organism']==n) for n in labels};og={o:[x for x in labels if next(r for r in panel if r['organism']==x)['order']==o] for o in orders};rev={frozenset(v):k for k,v in I.items() if k!='X'}
@functools.lru_cache(maxsize=1000000)
def score(bits):
 return (100*sum(sum(bool(bits & lb[n]) for n in og[o])/len(og[o]) for o in orders)/len(orders),100*sum(bool(bits&lb[n]) for n in labels)/len(labels))
def allow(q):return deg(q)<=8 and all(x in 'ACGT' for x in q[:len(q)//2]) and terminal(q)
def merge(a,b):return ''.join(rev[frozenset(set(I[x])|set(I[y]))] for x,y in zip(a,b))
allpool=[];allpairs=[];manifest={};
for reg in [REG]:
 c=coords[reg if reg=='XS' else reg+'D'];sidep={}
 for side in ['F','R']:
  a,b=int(c[side+'_start']),int(c[side+'_end']);L=b-a+1;observed=[];local=[]
  for x in panel:
   t=al[x['accession']][cols[a-1]:cols[b-1]+1];t=str(Seq(t).reverse_complement()) if side=='R' else t
   if len(t)==L and set(t)<=set('ACGT'):observed.append(t)
   v=al[x['accession']][cols[max(0,a-6)]:cols[min(len(cols)-1,b+4)]+1].replace('-','');v=str(Seq(v).reverse_complement()) if side=='R' else v
   local.append([v[i:i+L] for i in range(max(0,len(v)-L+1)) if set(v[i:i+L])<=set('ACGT')])
  observed=sorted(set(observed)); old=[x['sequence'] for x in prev if x['region']==reg and x['side']==side];seed=set(observed)
  for q in old:
   for v in expand(q):seed.add(v)
  for x in current:
   if x['region']==reg:
    for q in expand(x[side]):seed.add(q)
  seed={x for x in seed if len(x)==L and terminal(x)};cand=set(seed)
  # Anth-28S-style merging of variants in the 3-prime half only. Every merge adds bases seen in actual panel templates or existing concrete variants.
  groups=collections.defaultdict(list)
  for x in sorted(seed):groups[x[:L//2]].append(x)
  for same in groups.values():
   for x,y in itertools.combinations(same,2):
    if sum(a!=b for a,b in zip(x,y))<=3:
     q=merge(x,y)
     if allow(q):cand.add(q)
  # Grow supported intermediate mixtures toward observed templates, up to 8 variants.
  for q in list(cand):
   if deg(q)==1:continue
   for t in groups[q[:L//2]]:
    q2=merge(q,t)
    if allow(q2):cand.add(q2)
  matrices=[];valid_refs=[]
  for i,tt in enumerate(local):
   for t in tt:matrices.append([1<<('ACGT'.index(ch)) for ch in t]);valid_refs.append(i)
  arr=np.asarray(matrices,dtype=np.uint8);ids=np.asarray(valid_refs,dtype=np.int16); masks={'A':1,'C':2,'G':4,'T':8}
  rr=[]
  for q in sorted(cand):
   qm=np.array([sum(masks[x] for x in I[ch]) for ch in q],dtype=np.uint8);bad=(arr & qm)==0;n=bad.sum(axis=1);good=np.nonzero((n<=2)&(~bad[:,-3:].any(axis=1)))[0];zero=np.nonzero(n==0)[0];cv=sum(1<<int(i) for i in np.unique(ids[good]));ex=sum(1<<int(i) for i in np.unique(ids[zero]));rr.append(dict(region=reg,side=side,sequence=q,start=a,end=b,degeneracy=deg(q),cv=cv,ex=ex))
  ranked=sorted(rr,key=lambda x:(score(x['cv'])[1],score(x['ex'])[1],score(x['cv'])[0],score(x['ex'])[0],-x['degeneracy']),reverse=True)
  keep=ranked[:160]
  keep += sorted(rr,key=lambda x:(score(x['ex'])[1],score(x['cv'])[1],-x['degeneracy']),reverse=True)[:160]
  # Preserve targeted lineage representatives and inexpensive oligos.
  for o in orders:
   bit=sum(lb[n] for n in og[o]);keep+=sorted(rr,key=lambda x:(score(x['cv']&bit)[0],score(x['ex']&bit)[0],-x['degeneracy']),reverse=True)[:10]
  for cap in [1,2,4,8]:keep += [x for x in ranked if x['degeneracy']<=cap][:20]
  uniq={x['sequence']:x for x in keep};sidep[side]=list(uniq.values())
  for x in sidep[side]:x['id']='P%05d'%len(allpool);allpool.append(x)
  manifest[reg+'_'+side]={'observed_binding_templates':len(observed),'concrete_seeds':len(seed),'generated_oligos':len(cand),'retained_oligos':len(sidep[side]),'primer_length':L,'ambiguous_allowed_start_1based':L//2+1}
  print(reg,side,manifest[reg+'_'+side],flush=True)
 for f,r in itertools.product(sidep['F'],sidep['R']):
  cv=f['cv']&r['cv'];ex=f['ex']&r['ex'];allpairs.append(dict(region=reg,F=f['sequence'],R=r['sequence'],F_id=f['id'],R_id=r['id'],degeneracy_F=f['degeneracy'],degeneracy_R=r['degeneracy'],pred_order_coverage=score(cv)[0],pred_order_exact=score(ex)[0],pred_taxon_coverage=score(cv)[1],pred_taxon_exact=score(ex)[1],cv=cv,ex=ex))
(p/'oligos.json').write_text(json.dumps(allpool));(p/'pairs.json').write_text(json.dumps(allpairs));(out/'search_manifest.json').write_text(json.dumps(manifest,indent=2));print('FINISHED oligos',len(allpool),'pairs',len(allpairs),flush=True)
