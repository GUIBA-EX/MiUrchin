from pathlib import Path
import json,urllib.request,urllib.parse,concurrent.futures,time
p=Path(__file__).resolve().parent;root=p.parents[1];from Bio import SeqIO;import re; names=sorted({x.description[len(x.id):].strip() for x in SeqIO.parse(root/'work/miurchin/target.fasta','fasta') if re.fullmatch(r'[A-Z][A-Za-z-]+ [a-z][a-z-]+',x.description[len(x.id):].strip())})
def get(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MiUrchin-research-taxonomy/1.0'}),timeout=25) as f:return json.load(f)
def task(name):
 path=p/'taxonomy_raw'/((name.replace(' ','_'))+'.json');path.parent.mkdir(exist_ok=True)
 if path.exists():
  cached=json.loads(path.read_text())
  if cached.get('order'):return cached
 url='https://www.marinespecies.org/rest/AphiaRecordsByName/'+urllib.parse.quote(name)+'?like=false&marine_only=true'
 try:
  records=get(url);matches=[r for r in records or [] if r['scientificname'].lower()==name.lower()];record=next((r for r in matches if r['status']=='accepted'),matches[0] if matches else None)
  if not record:raise ValueError('No exact taxonomic-name result')
  aid=record.get('valid_AphiaID') or record['AphiaID'];tree=get('https://www.marinespecies.org/rest/AphiaClassificationByAphiaID/'+str(aid));orders=[];z=tree
  while z:
   if z.get('rank')=='Order':orders.append(z['scientificname'])
   z=z.get('child')
  row=dict(name=name,record=record,classification=tree,order=orders[0] if len(orders)==1 else None,source_url=url,accessed='2026-10-25')
 except Exception as e:row=dict(name=name,error=str(e),source_url=url)
 path.write_text(json.dumps(row,indent=2));print(name,row.get('order',row.get('error')),flush=True);return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(task,names))
(p/'taxonomy.json').write_text(json.dumps(rows,indent=2))
