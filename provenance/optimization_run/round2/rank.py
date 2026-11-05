import json,csv,collections
from pathlib import Path
B=Path('work/round2');rows=json.load(open(B/'candidates.json'));hits=collections.defaultdict(set);sizes=collections.defaultdict(set)
for g in ['16S','12S','COI']:
 for h in csv.DictReader(open(B/g/'independent_hits.tsv'),delimiter='\t'):
  for flag in ['exact','le2last3','le2','le3']:
   if h[flag]=='1':hits[h['name'],h['role'],h['model'],flag].add(h['accession'])
  if h['role']=='target' and h['le2last3']=='1':sizes[h['name'],h['accession']].update(int(x) for x in h['sizes'].split(',') if x)
for r in rows:
 panel=set(r['panel']);base=r['gene']+'_'+r['parent']+'_original';r['covered']=len(hits[r['id'],'target','WC','le2last3']&panel);r['exact']=len(hits[r['id'],'target','WC','exact']&panel);r['original_covered']=len(hits[base,'target','WC','le2last3']&panel);r['original_exact']=len(hits[base,'target','WC','exact']&panel)
 r['background']={m+'_'+f:len(hits[r['id'],'background',m,f]) for m,f in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]};r['original_background']={m+'_'+f:len(hits[base,'background',m,f]) for m,f in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]};r['reasons']=[]
 if r['covered']!=len(panel):r['reasons'].append('raw_pair_not_all_covered')
 if any(v>r['original_background'][k] for k,v in r['background'].items()):r['reasons'].append('non_target_exceeds_original')
 r['product_lengths']=sorted(set().union(*(sizes[r['id'],acc] for acc in panel)))
selected=[];groups=collections.defaultdict(list)
for r in rows:
 if not r['reasons']:groups[r['gene'],r['parent'],r['clade']].append(r)
for rr in groups.values():selected.append(min(rr,key=lambda r:(min(t['margin'] for t in r['thermal'])<5,-r['exact'],sum(r['background'].values()),r['deg_F']+r['deg_R'],-min(t['margin'] for t in r['thermal']),abs(r['F_shift'])+abs(r['R_shift']))))
final=[]
for key in sorted(set((r['gene'],r['parent']) for r in selected)):
 used=set()
 for r in sorted([r for r in selected if (r['gene'],r['parent'])==key],key=lambda r:(-len(r['panel']),-r['exact'])):
  if set(r['panel'])&used:continue
  final.append(r);used.update(r['panel'])
(B/'all_evaluated.json').write_text(json.dumps(rows,indent=2));(B/'selected.json').write_text(json.dumps(final,indent=2))
print('FINAL',len(final),'PARENTS',sorted(set((r['gene'],r['parent']) for r in final)))
for r in final:print(r['id'],len(r['panel']),r['original_covered'],r['covered'],r['exact'],min(t['margin'] for t in r['thermal']))
