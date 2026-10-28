from pathlib import Path
import sys,json,csv,collections
root=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni');p=root/'work/miurchin_3prime8';out=root/'outputs/MiUrchin_3prime8';sys.path.insert(0,str(root/'work/milily'));from common import thermal,oligo_thermal
pairs=json.loads((p/'pairs.json').read_text());h=collections.defaultdict(lambda:collections.defaultdict(list))
for n,acc,ori,gt,pos,mm,last in csv.reader((p/'sites/background_sites.tsv').open(),delimiter='\t'):h[n,int(gt)][acc,ori].append((int(pos),int(mm),int(last)))
selected=[]; audited=[]; cands=[]
for reg in ['S','M','L','XL']:
 rr=[x for x in pairs if x['region']==reg];rr.sort(key=lambda x:(x['pred_order_coverage'],x['pred_order_exact'],x['pred_taxon_coverage'],-x['degeneracy_F']-x['degeneracy_R']),reverse=True)
 # First 1000 target-ranked pairs plus additional low-variant alternatives for sensitivity.
 work=rr[:1000]+[x for x in rr if max(x['degeneracy_F'],x['degeneracy_R'])<=4][:200];work=list({(x['F'],x['R']):x for x in work}.values());print('SCREEN',reg,len(work),flush=True)
 for r in work:
  for gt,lim,col,strict in [(0,3,'WC3',False),(1,2,'GT2',False),(0,4,'WC4',False),(0,2,'strict_WC',True),(1,2,'strict_GT',True)]:
   f,b=h[r['F_id'],gt],h[r['R_id'],gt];r[col]=len({acc for acc,ori in f.keys()&b.keys() if any(fm<=lim and rm<=lim and (not strict or (not fl and not rl)) and 0<=rp-fp-len(r['F'])<=1000 for fp,fm,fl in f[acc,ori] for rp,rm,rl in b[acc,ori])})
  cands.append({k:v for k,v in r.items() if k not in ('cv','ex')})
 # Tiered gates: 20, 50, 100 broad; strict always ≤20. Output 1 per tier if different.
 for cap in [20,50,100]:
  candidates=[r for r in work if max(r['WC3'],r['GT2'])<=cap and max(r['strict_WC'],r['strict_GT'])<=20]
  candidates.sort(key=lambda x:(x['pred_order_coverage'],x['pred_order_exact'],x['pred_taxon_coverage'],-x['degeneracy_F']-x['degeneracy_R']),reverse=True)
  for x in candidates:
   if any(v['F']==x['F'] and v['R']==x['R'] for v in selected):print('DUP',reg,cap,flush=True);break
   ft,rt=oligo_thermal(x['F']),oligo_thermal(x['R']);pre=all(max(a[2],b[2])<55 and abs((a[0]+a[1]-b[0]-b[1])/2)<=5 for a,b in zip(ft,rt));ok,th=thermal(x['F'],x['R']) if pre else (False,[]);audited.append(dict(region=reg,tier=cap,F=x['F'],R=x['R'],precheck=pre,thermal_pass=ok))
   if ok:
    rec={k:v for k,v in x.items() if k not in ('cv','ex')};rec.update(name=f'{reg}-3P8-{cap}',thermal=th,tier=cap);selected.append(rec);print('SELECT',reg,cap,round(x['pred_order_coverage'],2),round(x['pred_order_exact'],2),x['degeneracy_F'],x['degeneracy_R'],flush=True);break
  else:print('NO PASS',reg,cap,flush=True)
(p/'selection.json').write_text(json.dumps(selected,indent=2))
for name,rows in [('candidates_screened.csv',cands),('thermal_audit.csv',audited)]:
 with (out/name).open('w') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('FINISHED',len(selected),len(cands),flush=True)
