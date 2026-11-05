from pathlib import Path
import json,csv,collections
p=Path(__file__).resolve().parent
ss=json.loads((p/'portfolio_selected.json').read_text());detail=list(csv.DictReader((p/'target_detail.tsv').open(),delimiter='\t'));tab=collections.defaultdict(dict)
for r in detail:tab[r['name'],r['panel']][r['accession']]=r
summary=[];missed=[];taxrows=[];taxonomy={r['accession']:r['order'] for r in csv.DictReader((p/'target_taxonomy.tsv').open(),delimiter='\t')}
for s in ss:
 names=s['allowed_pair_names']
 for panel in ['common','own_region']:
  ids=set(tab[names[0],panel]);assert all(set(tab[n,panel])==ids for n in names)
  rr=[];sizes=set()
  for k in sorted(ids):
   r=tab[names[0],panel][k];d=dict(accession=k,organism=r['organism'],weight=float(r['weight']))
   for key in ['exact','le2last3','le2']:d[key]=any(tab[n,panel][k][key]=='True' for n in names)
   for n in names:sizes.update(map(int,filter(None,tab[n,panel][k]['sizes'].split(','))))
   rr.append(d)
  out=dict(name=s['name'],panel=panel,n_labels=len({r['organism'] for r in rr}),n_haplotypes=len(rr),product_min=min(sizes) if sizes else '',product_max=max(sizes) if sizes else '')
  for key in ['exact','le2last3','le2']:out[key+'_pct']=100*sum(r['weight'] for r in rr if r[key])
  summary.append(out)
  groups=collections.defaultdict(list)
  for r in rr:groups[taxonomy[r['accession']]].append(r)
  for order,sub in groups.items():
   taxrows.append(dict(name=s['name'],panel=panel,source_order=order,n_labels=len({r['organism'] for r in sub}),n_haplotypes=len(sub),coverage_pct=100*sum(r['weight'] for r in sub if r['le2last3'])/sum(r['weight'] for r in sub)))
  for label in sorted({r['organism'] for r in rr}):
   sub=[r for r in rr if r['organism']==label];hit=sum(r['le2last3'] for r in sub)
   if hit<len(sub):missed.append(dict(name=s['name'],panel=panel,organism=label,n_haplotypes=len(sub),detected_haplotypes=hit,coverage_pct=100*hit/len(sub)))
for n,data in [('portfolio_panel_comparison.tsv',summary),('uncovered_labels.tsv',missed),('portfolio_order_coverage.tsv',taxrows)]:
 with (p/n).open('w') as f:
  fields=list(data[0]) if data else ['name','panel','organism','n_haplotypes','detected_haplotypes','coverage_pct'];w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(data)
print('Panel summaries',len(summary),'incompletely covered label/scheme entries',len(missed))
