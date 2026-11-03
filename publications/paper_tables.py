"""Resolve the published tables from the four marker panels."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def rows(path):
    with (ROOT/path).open() as file:
        return list(csv.DictReader(file))
def table(columns, records):
    return '\n'.join('| '+' | '.join(map(str,r))+' |' for r in [columns,['---']*len(columns),*records])
def tables():
    records=[]
    folder='results/computational_evaluation/results/'
    panels=rows(folder+'panel_comparison.csv')
    own={r['name']:r for r in panels if r['panel']=='own'}
    for r in rows('results/current_primers/comparison.csv'):
        a=own[r['name']]
        records.append(('16S',r['name'],r['F'],r['R'],a['n'],a['covered'],a['exact'],r['strict_WC'],r['strict_GT']))
    for r in rows('markers/12S_COI/candidates.csv'):
        records.append(tuple(r[k] for k in ['gene','name','F','R','evaluable','covered','exact','WC','GT']))
    for r in rows('markers/28S/selected.csv'):
        records.append(('28S',*(r[k] for k in ['name','F','R','n','coverage','exact','strictWC','strictGT'])))
    oligos = {f'MiUrchin-{g}-{n}_{end}':seq for g,n,f,r,*_ in records for end,seq in [('F',f),('R',r)]}
    fa=(ROOT/'sequences/all_markers.fasta').read_text().split()
    assert oligos==dict(zip([h[1:].replace("12S_", "12S-").replace("COI_", "COI-") for h in fa[::2]],fa[1::2],strict=True))
    data=[('Oligos in synthesis orientation',table(['Marker','Assay','Forward (5′–3′)','Reverse (5′–3′)'],[r[:4] for r in records])),('Window-specific performance',table(['Marker','Pair','N','Covered','Exact','Strict WC','Strict GT'],[[*r[:2],*r[4:]] for r in records]))]
    return '\n\n'.join(f'## Table {i}. {title}\n\n{t}' for i,(title,t) in enumerate(data,1))+'\n'
