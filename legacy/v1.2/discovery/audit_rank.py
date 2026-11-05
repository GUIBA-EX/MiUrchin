from pathlib import Path
import csv,json,random
p=Path(__file__).resolve().parent
# Load original Python pair-risk implementation only, not its original full ranking loop.
s=(p/'rank_pairs.py').read_text();scope={'__file__':str(p/'rank_pairs.py')};exec(s[:s.index('\nrows=list(')],scope)
rows=json.loads((p/'rank_pair_order.json').read_text());risks=list(csv.DictReader((p/'fast_risks.tsv').open(),delimiter='\t'));random.seed(261024)
indices=sorted(set([0,len(rows)-1,len(rows)-2]+random.sample(range(len(rows)-2),12)))
for i in indices:
 r=rows[i];a=scope['risk'](r['F_id'],r['R_id']);b=risks[i]
 for k in ['WC_le2','WC_le3','WC_le4','WC_ambiguous','GT_le2','GT_ambiguous']:assert a[k]==int(b[k]),(i,k,a[k],b[k])
 print(i,'PASS',flush=True)
(p/'rank_audit.json').write_text(json.dumps(dict(status='PASS',n_pairs=len(indices),indices=indices,scope='C++ risk aggregation vs original Python; not independent sequence scan'),indent=2))
