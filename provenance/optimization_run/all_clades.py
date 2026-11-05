import contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
 import audit as a
from collections import defaultdict,Counter
import json,html
# Transfer only exact species-level classifications already present in this project.
orders=defaultdict(set)
for ts in a.templates.values():
 for t in ts:
  if t['order']:orders[t['species']].add(t['order'])
for ts in a.templates.values():
 for t in ts:
  if not t['order'] and len(orders[t['species']])==1:t['order']=next(iter(orders[t['species']]))
clades={'Cidaroidea':{'Cidaroida'},'Aulodonta':{'Aspidodiadematoida','Diadematoida','Echinothurioida','Pedinoida','Phymosomatoida'},'Echinacea':{'Arbacioida','Camarodonta','Stomopneustoida','Salenioida','Temnopleuroida'},'Irregularia':{'Clypeasteroida','Echinolampadacea','Holasteroida','Spatangoida','Echinoneoida'}}
def clade(t):return next((k for k,v in clades.items() if t['order'] in v),'unresolved')
def consensus(ts):return ''.join(a.rev[frozenset(t[j] for t in ts)] for j in range(len(ts[0])))
def deg(s):return a.math.prod(len(a.I[x]) for x in s)
def match(q,t):return all(b in a.I[x] for x,b in zip(q,t))
res=[]
for q in a.assays:
 sides={s:{t['accession']:t for t in a.templates[q['gene'],q['name'],s]} for s in ['F','R']}; groups=defaultdict(list);excluded=0;unknown=[]
 for acc,f in sides['F'].items():
  r=sides['R'].get(acc)
  if not r or any(t['insertions'] or len(t['template'])!=len(q[s]) or set(t['template'])-set('ACGT') for s,t in [('F',f),('R',r)]):excluded+=1;continue
  c=clade(f)
  if c=='unresolved':unknown.append(f['species'])
  groups[c].append((f,r))
 summary=[]
 for c,rr in groups.items():
  d={'clade':c,'n':len(rr),'species':sorted(set(f['species'] for f,r in rr)),'sides':{}}
  for j,s in enumerate(['F','R']):
   ts=[x[j]['template'] for x in rr];cons=consensus(ts);modal=''.join(Counter(t[i] for t in ts).most_common(1)[0][0] for i in range(len(ts[0])));candidate=q[s][:-3]+cons[-3:]
   d['sides'][s]={'current':q[s],'terminal_union':cons[-3:],'current_terminal_match':sum(match(q[s][-3:],t[-3:]) for t in ts),'terminal_candidate':candidate,'terminal_candidate_deg':deg(candidate),'full_union_deg':deg(cons),'full_union':cons,'ordinary_modal_diagnostic':modal,'modal_terminal_match':sum(t[-3:]==modal[-3:] for t in ts)}
  d['current_pair_terminal_match']=sum(match(q['F'][-3:],f['template'][-3:]) and match(q['R'][-3:],r['template'][-3:]) for f,r in rr);summary.append(d)
 known=[d for d in summary if d['clade']!='unresolved'];patterns={s:len(set(d['sides'][s]['terminal_union'] for d in known)) for s in ['F','R']}
 status='分类／完整结合区不足' if len(known)<2 else '两端均比较分支子引物' if min(patterns.values())>1 else '优先拆F，R可比较共享' if patterns['F']>1 else '优先拆R，F可比较共享' if patterns['R']>1 else '末端集合相同，未见末端拆分收益'
 res.append({'gene':q['gene'],'name':q['name'],'status':status,'excluded_pair_records':excluded,'unknown_species':unknown,'groups':summary})
a.O.joinpath('MiUrchin_all_clades.json').write_text(json.dumps({'method':'paired complete ACGT homologous sites, no insertions; exact species classification transfer only; exploratory 4-clade stratification, not new phylogeny; candidates not validated','results':res},ensure_ascii=False,indent=2))
p=['<!doctype html><meta charset="utf-8"><title>全部MiUrchin分支审计</title><style>body{font:16px/1.6 system-ui;max-width:1300px;margin:35px auto;padding:20px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid #ccc;padding:7px}th{background:#e2eff2}code{overflow-wrap:anywhere}details{margin:18px 0}</style><h1>全部普通／D引物的进化枝分层检查</h1><p>2026-11-05 · 32对、64条 · 四个基因全部纳入，不限于已有末端错配的D引物。</p><p>依据<a href="https://elifesciences.org/articles/72460">海胆系统基因组研究</a>使用Cidaroidea、Aulodonta、Echinacea、Irregularia进行诊断分层。目标签沿用现有项目，28S仅借用其他标记中完全同名物种的唯一目分类；无可靠对应者保留未定，不按属名猜测。分层用于寻找变异集中在哪个分支，不强制每组恰好拆成两个，也不把任意两个目的组合叫作进化枝。</p><p><b>优先级：分支内末端三位覆盖 → 末端更长区域及全长错配 → 简并度／分支代表性 → 非目标、热力学和混合配对验证。</b>普通版仍保持非简并：若分支内末端存在多种单倍型，单条普通子引物不能保证全覆盖，应进一步分支或使用D版本。</p><p>本表只统计F和R同时具有完整无插入结合区的记录，因此与上次单端审计分母不同。排除记录不是未检出。各分支样本量小或缺失时不宣称通用性。16S XS/S结合区插入问题仍需重新定位。下列是诊断，不是替换或下单名单。</p><table><tr><th>基因／方案</th><th>分支检查结果</th><th>完整已分类记录</th><th>未分类记录</th><th>结合区不完整／插入</th></tr>']
for r in res:p.append(f"<tr><td>{r['gene']} {r['name']}</td><td>{r['status']}</td><td>{sum(d['n'] for d in r['groups'] if d['clade']!='unresolved')}</td><td>{len(r['unknown_species'])}</td><td>{r['excluded_pair_records']}</td></tr>")
p.append('</table><h2>逐组分支证据</h2>')
for r in res:
 p.append(f"<details><summary>{r['gene']} {r['name']} — {r['status']}</summary><table><tr><th>分支</th><th>n</th><th>F末端集合／现有匹配</th><th>R末端集合／现有匹配</th><th>现有双端末端匹配</th><th>仅替换末端后全长简并度F/R</th></tr>")
 for d in r['groups']:
  f,z=d['sides']['F'],d['sides']['R'];p.append(f"<tr><td>{d['clade']}</td><td>{d['n']}</td><td>{f['terminal_union']} / {f['current_terminal_match']}</td><td>{z['terminal_union']} / {z['current_terminal_match']}</td><td>{d['current_pair_terminal_match']}</td><td>{f['terminal_candidate_deg']} / {z['terminal_candidate_deg']}</td></tr>")
 p.append('</table><p>完整分支序列集合、普通版多数碱基诊断序列、末端候选与物种名单见JSON；多数碱基组合不一定是天然单倍型，均未完成全序列扫描或热力学验证。</p></details>')
p.append('<h2>如何决定两个子引物</h2><p>先在上述分支中识别需要补偿的系统性差异；如仅一端不同，比较两个F+共享R或共享F+两个R。若某大分支内末端仍高度分化，应向内部有支持的节点继续细分或移动窗口。四个分支不能任意拼成两个单系群。仅凭末端集合不同只能提出拆分候选，不能证明覆盖收益或PCR效率提升。</p><p>本轮完成所有引物的分支筛查；尚未形成经过非目标、结构及配对验证的正式新引物。28S未分类记录和16S插入结合区明确保留为证据缺口。</p>')
a.O.joinpath('MiUrchin_all_clades.html').write_text(''.join(p))
assert len(res)==32
print(Counter(r['status'] for r in res));print('28S',[(r['name'],len(r['unknown_species'])) for r in res if r['gene']=='28S'])
