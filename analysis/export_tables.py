from pathlib import Path
import csv,json,math
p=Path(__file__).resolve().parent;out=p.parent/'results';out.mkdir(exist_ok=True)
def read(n):return list(csv.DictReader((p/n).open(),delimiter='\t'))
def write(n,rr):
 with (out/n).open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rr[0]));w.writeheader();w.writerows(rr)
ss=json.loads((p/'portfolio_selected.json').read_text());risk={r['name']:r for r in read('portfolio_summary.tsv')};pan={(r['name'],r['panel']):r for r in read('portfolio_panel_comparison.tsv')};ol={r['id']:r for r in json.loads((p/'same_locus/oligos.json').read_text())};seq=[];pairs=[];summ=[]
for s in ss:
 lookup={}
 for d in ['F','R']:
  for i,(k,q) in enumerate(zip(s[d+'_ids'],s[d+'_sequences']),1):
   name=s['name']+'-'+d+str(i);lookup[k]=name;x=ol[k]
   seq.append(dict(scheme=s['name'],mode=s['mode'],primer_id=name,candidate_id=k,direction=d,sequence_5to3=q,length_nt=len(q),degeneracy=x['degeneracy'],Tm_min_C=round(x['tm_min'],2),Tm_max_C=round(x['tm_max'],2),Tm_scenario='50nM_per_concrete_variant',contains_possible_AAAA=any(all(c in 'ARWMDHVN' for c in q[j:j+4]) for j in range(len(q)-3))))
 for i,((f,r),name) in enumerate(zip(s['allowed_pairs'],s['allowed_pair_names']),1):pairs.append(dict(scheme=s['name'],mode=s['mode'],reaction='PCR'+str(i) if s['mode']=='separate' else 'ONE_POOL',F_id=lookup[f],R_id=lookup[r],F=ol[f]['sequence'],R=ol[r]['sequence'],pair_result_id=name,component_pair=[f,r] in s['component_pairs']))
 c=pan[s['name'],'common'];own=pan[s['name'],'own_region'];r=risk[s['name']]
 summ.append(dict(scheme=s['name'],mode=s['mode'],F_oligos=len(s['F_ids']),R_oligos=len(s['R_ids']),component_pairs=len(s['component_pairs']),evaluated_pairs=len(s['allowed_pairs']),common_labels=c['n_labels'],common_haplotypes=c['n_haplotypes'],common_coverage_pct=round(float(c['le2last3_pct']),2),common_exact_pct=round(float(c['exact_pct']),2),region_labels=own['n_labels'],region_haplotypes=own['n_haplotypes'],region_coverage_pct=round(float(own['le2last3_pct']),2),region_exact_pct=round(float(own['exact_pct']),2),region_product_min=own['product_min'],region_product_max=own['product_max'],WC2=r['WC_le2'],WC3=r['WC_le3'],GT2=r['GT_le2'],WC4=r['WC_le4'],WC_ambiguous=r['WC_ambiguous'],GT_ambiguous=r['GT_ambiguous']))
write('primers.csv',seq);write('pairings.csv',pairs);write('comparison.csv',summ);(out/'primers.fasta').write_text(''.join(f">{r['primer_id']}\n{r['sequence_5to3']}\n" for r in seq))
print('Exported',len(seq),'scheme-local oligos,',len(pairs),'allowed pairs')
