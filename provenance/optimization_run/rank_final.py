import json,csv,collections
from pathlib import Path
rows=json.load(open('work/candidates.json'))+[r for r in json.load(open('work/terminal_candidates.json')) if r['clade']!='original']+json.load(open('work/local_candidates.json')); therm=json.load(open('work/thermal.json'));therm.update(json.load(open('work/terminal_thermal.json')))
therm.update(json.load(open('work/local_thermal.json')))
hits=collections.defaultdict(set)
for folder in ['validation','refined','terminal_only','local']:
 for gene in ['16S','12S','COI','28S']:
  if folder=='refined' and gene=='28S':continue
  for r in csv.DictReader(open(f'work/{folder}/{gene}/independent_hits.tsv'),delimiter='\t'):
   for flag in ['exact','le2last3','le2','le3','le4']:
    if r[flag]=='1':hits[r['name'],r['role'],r['model'],flag].add(r['accession'])
for r in rows:
 t=therm[r['id']];t['pass_gate']=t['structure_max']<55 and t['delta_mid_tm']<=5 and min(t['F_tm']+t['R_tm'])>=45 and max(t['F_tm']+t['R_tm'])<=75
 def hs(name,role,model,flag):return hits[name,role,model,flag]
 panel=set(r['panel']);base=r['gene']+'_'+r['parent']+'_original';r['thermal']=t
 r['covered']=len(hs(r['id'],'target','WC','le2last3')&panel);r['original_covered']=len(hs(base,'target','WC','le2last3')&panel);r['exact']=len(hs(r['id'],'target','WC','exact')&panel);r['original_exact']=len(hs(base,'target','WC','exact')&panel)
 r['background']={m+'_'+f:len(hs(r['id'],'background',m,f)) for m,f in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]};r['original_background']={m+'_'+f:len(hs(base,'background',m,f)) for m,f in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]}
 reasons=[]
 if not t['pass_gate']:reasons.append('热力学门槛未过')
 if r['clade']!='original':
  if r['covered']<len(panel):reasons.append('分支设计面板未全部达到双端≤2错配且末端3位匹配')
  if any(v>r['original_background'][k] for k,v in r['background'].items()):reasons.append('非目标计数超过原引物')
 r['reasons']=reasons
eligible=collections.defaultdict(list)
for r in rows:
 if r['clade']!='original' and not r['reasons']:eligible[r['gene'],r['parent'],r['clade']].append(r)
selected=[]
for key,rr in eligible.items():selected.append(min(rr,key=lambda r:(-r['exact'],sum(r['background'].values()),r['thermal']['deg_F']+r['thermal']['deg_R'],r['thermal']['structure_max'])))
Path('work/selected.json').write_text(json.dumps(selected,indent=2));Path('work/all_evaluated.json').write_text(json.dumps(rows,indent=2))
print('Selected',len(selected),collections.Counter(r['gene'] for r in selected))
for r in selected:print(r['id'],r['covered'],r['original_covered'],r['exact'],r['original_exact'])
