from pathlib import Path
import csv,json,collections,math,hashlib,html
P=Path('/Users/xiafei/Documents/Codex/2026-10-24/ni/outputs/MiUrchin'); O=Path('outputs'); inputs={}
I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT'])); rev={frozenset(v):k for k,v in I.items()}; comp=str.maketrans('ACGTRYMKSWBDHVN','TGCAYRKMSWVHDBN')
def read(p):
 inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest();return list(csv.DictReader(p.open()))
def fasta(p):
 inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest(); d={}
 for l in p.read_text().splitlines():
  if l.startswith('>'):k=l[1:].split()[0].removeprefix('_R_');d[k]=''
  else:d[k]+=l.upper()
 return d
assays=[]; templates={}
for q in read(P/'results/current_primers/comparison.csv'):
 q['gene']='16S';assays.append(q)
 rows=read(P/f"results/current_primers/{q['region']}/{q['name']}_base_matching.csv")
 for side in ['F','R']:templates['16S',q['name'],side]=[dict(accession=r['accession'],species=r['species'],order=r['order'],template=r['template'],insertions=int(r['insertions'])) for r in rows if r['side']==side]
for gene in ['12S','COI']:
 d=P/'markers/12S_COI'/gene; al=fasta(d/'aligned.fasta');anchor=(d/'anchor.txt').read_text().strip();cols=[i for i,b in enumerate(al[anchor]) if b!='-'];panel=read(d/'target_panel.csv')
 for q in read(d/'pairs.csv'):
  q['gene']=gene;assays.append(q)
  for side in ['F','R']:
   a,b=[int(q[side+'_'+v])-1 for v in ['start','end']]; ts=[]
   for r in panel:
    s=al[r['accession']];t=''.join(s[i] for i in cols[a:b+1]);ins=sum(x!='-' for x in s[cols[a]:cols[b]+1])-sum(x!='-' for x in t)
    if side=='R':t=t.translate(comp)[::-1]
    ts.append(dict(accession=r['accession'],species=r['species'],order=r['order'],template=t,insertions=ins))
   templates[gene,q['name'],side]=ts
al=fasta(P/'markers/28S/aligned.fa.out'); species={}
for l in (P/'markers/28S/target.fasta').read_text().splitlines():
 if l.startswith('>'):a,sp=l[1:].split(' ',1);species[a]=sp
for q in read(P/'markers/28S/selected.csv'):
 q['gene']='28S';assays.append(q);a=int(q['start'])-1;b=int(q['end'])
 for side in ['F','R']:templates['28S',q['name'],side]=[dict(accession=k,species=species[k],order='',template=s[a:a+20] if side=='F' else s[b-20:b].translate(comp)[::-1],insertions=0) for k,s in al.items()]
results=[]; exceptions=[]
for q in assays:
 for side in ['F','R']:
  seq=q[side];ts=templates[q['gene'],q['name'],side];valid=[r for r in ts if len(r['template'])==len(seq) and not set(r['template'])-set('ACGT') and not r['insertions']];n=len(valid)
  counts=[dict(collections.Counter(r['template'][j] for r in valid)) for j in range(len(seq))];miss=[sum(c for b,c in co.items() if b not in I[s]) for s,co in zip(seq,counts)]
  def match(s,t):return all(b in I[a] for a,b in zip(s,t))
  candidate=seq[:-3]+''.join(rev[frozenset(set(I[a])|set(co))] for a,co in zip(seq[-3:],counts[-3:]))
  deg=lambda s:math.prod(len(I[x]) for x in s)
  bad=[r for r in valid if not match(seq[-3:],r['template'][-3:])]
  for r in bad:exceptions.append(dict(gene=q['gene'],name=q['name'],side=side,primer=seq,**r))
  results.append(dict(gene=q['gene'],name=q['name'],side=side,primer=seq,valid=n,excluded=len(ts)-n,last3=seq[-3:],terminal3_match=n-len(bad),terminal1_miss=miss[-1],position_counts=counts,position_misses=miss,degeneracy=deg(seq),candidate_terminal_union=candidate,candidate_degeneracy=deg(candidate),exact=sum(match(seq,r['template']) for r in valid),candidate_exact=sum(match(candidate,r['template']) for r in valid)))
assert len(assays)==32 and len(results)==64
out=dict(scope='fixed homologous binding sites; complete ACGT sites without insertions; counts are records, not deduplicated species; not full-sequence PCR prediction',results=results,terminal_mismatches=exceptions,input_sha256=inputs)
(O/'MiUrchin_terminal_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for r in results:
 if r['name'].endswith('D'):print(r['gene'],r['name'],r['side'],r['last3'],f"{r['terminal3_match']}/{r['valid']}",r['candidate_terminal_union'][-3:],r['degeneracy'],r['candidate_degeneracy'])
# Add diagnostic terminal-column statistics, distinguished from contiguous full sites.
for r in results:
 ts=templates[r['gene'],r['name'],r['side']]; usable=[t for t in ts if len(t['template'])==len(r['primer']) and set(t['template'][-3:])<=set('ACGT')]
 r['terminal_columns_n']=len(usable);r['terminal_columns_match']=sum(all(b in I[a] for a,b in zip(r['last3'],t['template'][-3:])) for t in usable)
 r['terminal_column_counts']=[dict(collections.Counter(t['template'][j] for t in usable)) for j in [-3,-2,-1]]
 r['length']=len(r['primer']);r['gc_min']=sum(set(I[x])<=set('GC') for x in r['primer'])/r['length']*100;r['gc_max']=sum(bool(set(I[x])&set('GC')) for x in r['primer'])/r['length']*100
splits=[]
for r in results:
 if not r['name'].endswith('D') or r['terminal3_match']==r['valid']:continue
 ts=[t for t in templates[r['gene'],r['name'],r['side']] if len(t['template'])==len(r['primer']) and set(t['template'])<=set('ACGT') and t['insertions']==0]
 groups=sorted(set(t['order'] for t in ts if t['order']))
 if len(groups)<2 or len(groups)>18:continue
 def tail(rows):return ''.join(rev[frozenset(t['template'][j] for t in rows)] for j in [-3,-2,-1])
 def de(s):return math.prod(len(I[x]) for x in s)
 best=None
 for mask in range(1,2**(len(groups)-1)):
  g={groups[j] for j in range(len(groups)) if mask>>j&1};a=[t for t in ts if t['order'] in g];b=[t for t in ts if t['order'] not in g]
  if len(a)<3 or len(b)<3:continue
  ta,tb=tail(a),tail(b);score=(max(de(ta),de(tb)),de(ta)+de(tb),abs(len(a)-len(b)))
  if best is None or score<best[0]:best=(score,g,ta,tb,len(a),len(b))
 if best:
  score,g,ta,tb,na,nb=best;splits.append(dict(gene=r['gene'],name=r['name'],side=r['side'],group_A=sorted(g),group_B=sorted(set(groups)-g),last3_A=ta,last3_B=tb,n_A=na,n_B=nb,sequence_A=r['primer'][:-3]+ta,sequence_B=r['primer'][:-3]+tb,deg_A=de(r['primer'][:-3]+ta),deg_B=de(r['primer'][:-3]+tb),status='order partition diagnostic only; monophyly and specificity unverified'))
lookup={(r['gene'],r['name'],r['side']):r for r in results};noninclusion=[]
for r in results:
 if r['name'].endswith('D'):
  ordinary=lookup[r['gene'],r['name'][:-1],r['side']]['primer'];bad=[i+1 for i,(a,b) in enumerate(zip(ordinary,r['primer'])) if not set(I[a])<=set(I[b])]
  if bad:noninclusion.append(dict(gene=r['gene'],name=r['name'],side=r['side'],positions_5prime=bad))
out.update(results=results,split_diagnostics=splits,ordinary_not_in_D=noninclusion)
(O/'MiUrchin_terminal_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('NONINCLUSION',noninclusion)
print('SPLITS',json.dumps(splits,ensure_ascii=False))
clade=[]
for r in results:
 if not r['name'].endswith('D') or r['gene']=='28S':continue
 ts=[t for t in templates[r['gene'],r['name'],r['side']] if len(t['template'])==len(r['primer']) and set(t['template'])<=set('ACGT') and t['insertions']==0]
 a=[t for t in ts if t['order']=='Cidaroida'];b=[t for t in ts if t['order'] and t['order']!='Cidaroida']
 if not a or not b:continue
 tail=lambda rows:''.join(rev[frozenset(t['template'][j] for t in rows)] for j in [-3,-2,-1])
 sa=r['primer'][:-3]+tail(a);sb=r['primer'][:-3]+tail(b)
 clade.append(dict(gene=r['gene'],name=r['name'],side=r['side'],Cidaroidea_n=len(a),Euechinoidea_n=len(b),Cidaroidea_sequence=sa,Euechinoidea_sequence=sb,deg_A=de(sa),deg_B=de(sb),single_union_deg=r['candidate_degeneracy']))
out['phylogenetic_root_split']=clade
(O/'MiUrchin_terminal_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
esc=html.escape
parts=['<!doctype html><meta charset="utf-8"><title>MiUrchin 普通与D引物复核</title><style>body{font:16px/1.65 system-ui;max-width:1350px;margin:35px auto;padding:20px;color:#163343}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:7px;border:1px solid #cbd7dd;text-align:left}th{background:#e7f1f4}code{font-family:monospace}strong{color:#a33}details{margin:16px 0}h1,h2{line-height:1.3}.note{background:#fff2da;padding:18px}</style><h1>MiUrchin 普通／D 引物复核</h1><p>2026-11-05 · 32 对引物、64 条寡核苷酸 · 现有本地 v1.2 数据 · 计算检查，无湿实验验证</p>', '<h2>结论与优先级</h2><p><strong>D 引物应先解决 3′末端三位的目标变异，再分配内部简并。</strong>现有 D 序列未全部满足这一要求。12S XSD-F、XLD-F，COI SD-R，以及16S SD-R、LD-R值得优先调整。28S SD的两端在本次完整结合区子集中无末端三位遗漏；MD、LD仍有少数遗漏，先核查异常记录。</p><p>普通引物保留非简并方案，但不能用允许整体错配的“覆盖率”掩盖末端不匹配。16S XL两端末端较保守，L的F端较保守而R端存在明显变异；12S M-F末端保守，M-R变异大；COI普通R端通常比D端遗漏更多。所有逐条数字见下表。</p>', '<h2>文献依据</h2><p><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4632578/">MiFish（Miya等，2015）</a>通过保守结合区、端部稳定性及分群引物兼顾扩增与覆盖，U/E方案提示：系统性分支差异可由不同子引物处理。文中的G–T配对策略不能当成本次末端三位的严格匹配。</p><p><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11606329/">Anth28S（McCartin等，2024）</a>先按序列分歧设计不同类群引物，再依据实际SNP加入简并；不是所有位点无差别加简并，也不是要求末端三位必须出现简并符号。保守位点应保持固定，变异位点才补足对应碱基。</p>', '<h2>统计口径与边界</h2><p>主统计仅用整条结合区为ACGT、无插入的模板；F/R独立统计，因此分母不同。这是参考同源位点审计，不是成对PCR检出率。全部数字是记录数，不能直接与原项目物种覆盖率比较。另列“末端列匹配”只要求末端三列为ACGT，允许内部缺失或插入，属于比对诊断。</p><p class="note">16S XS/XSD与S/SD的F端：完整且无插入的子集仅1条，不能据此宣称100%覆盖。末端列诊断分别显示XSD-F为50/55、SD-F为54/55；需从原始连续序列重新定位或移动结合窗口。缺口不能通过添加N修复。</p>', '<h2>全部引物：普通与D分别检查</h2><table><tr><th>基因／引物／方向</th><th>5′→3′</th><th>末端3位</th><th>末端匹配／完整无插入记录</th><th>末端列匹配／可读记录</th><th>全长精确匹配</th><th>简并度</th></tr>']
for r in results:parts.append(f"<tr><td>{r['gene']} {r['name']}-{r['side']}</td><td><code>{r['primer']}</code></td><td>{r['last3']}</td><td>{r['terminal3_match']}/{r['valid']}</td><td>{r['terminal_columns_match']}/{r['terminal_columns_n']}</td><td>{r['exact']}/{r['valid']}</td><td>{r['degeneracy']}</td></tr>")
parts+=['</table><h2>D端部补齐的代价</h2><p>下列是“保留现有内部序列，仅将完整无插入模板观察到的末端碱基加入IUPAC集合”的诊断候选。未经非目标扫描、热力学与二聚体复核，不是下单序列。高简并代价提示应拆分子引物或移动窗口。</p><table><tr><th>引物</th><th>现有→末端集合</th><th>全长简并度</th><th>遗漏记录</th></tr>']
for r in results:
 if r['name'].endswith('D') and r['terminal3_match']<r['valid']:parts.append(f"<tr><td>{r['gene']} {r['name']}-{r['side']}</td><td>{r['last3']} → {r['candidate_terminal_union'][-3:]}</td><td>{r['degeneracy']} → {r['candidate_degeneracy']}</td><td>{r['valid']-r['terminal3_match']}</td></tr>")
parts+=['</table><h2>两个子引物：按进化枝评估</h2><p>采用<a href="https://elifesciences.org/articles/72460">海胆系统基因组研究</a>支持的Cidaroidea／Euechinoidea根部分裂做首次诊断；按现有目标签将Cidaroida映射至前者。它不保证最优，也不应把“规则／不规则海胆”直接当作两个互为姐妹的单系群。下面保持内部序列，只分别汇总末端三位；若两枝末端相同，拆分本身无意义。28S现有表缺少目映射，本次不推断分类。</p><table><tr><th>引物</th><th>Cidaroidea末端（n）</th><th>Euechinoidea末端（n）</th><th>两子引物简并度</th><th>单条补齐简并度</th></tr>']
for c in clade:parts.append(f"<tr><td>{c['gene']} {c['name']}-{c['side']}</td><td>{c['Cidaroidea_sequence'][-3:]} ({c['Cidaroidea_n']})</td><td>{c['Euechinoidea_sequence'][-3:]} ({c['Euechinoidea_n']})</td><td>{c['deg_A']} / {c['deg_B']}</td><td>{c['single_union_deg']}</td></tr>")
parts+=['</table><p>另做了按目任意二分的数学诊断（JSON中保留），但这些最优组合常横跨不同进化枝，不能直接命名为分支引物。实际设计需将末端单倍型映射到系统树，允许只拆F或只拆R，共享另一端；若F/R都拆，应评估同枝配对及混合后交叉配对。优先优化每个分支的完整结合区，而非只复制同一内部序列。</p><h2>普通序列是否包含在D中</h2><p>16S SD-R的第9位，XLD-F的第1和3位，XLD-R的第19位不包含普通版碱基（从5′端计数）。它们同时涉及固定替换，应独立解释，不能把全部效果归因于简并。</p><h2>逐位频率与遗漏模板</h2><p>下列末端频率顺序为−3、−2、−1；来自完整无插入模板。展开可查看具体物种和登录号。</p>']
for r in results:
 bad=[e for e in exceptions if (e['gene'],e['name'],e['side'])==(r['gene'],r['name'],r['side'])]
 parts.append(f"<details><summary>{r['gene']} {r['name']}-{r['side']} · 遗漏{len(bad)}条</summary><p>{esc(str(r['position_counts'][-3:]))}</p><pre>"+esc('\n'.join(f"{e['accession']} | {e['species']} | {e['order']} | {e['template']}" for e in bad))+'</pre></details>')
parts+=['<h2>复核状态</h2><p>已完成64条序列、末端逐位频率、遗漏记录、简并度、普通/D包含关系与两分支初筛。候选未作全序列非目标扫描、Tm/发夹/二聚体计算或实验验证；本次未覆盖原始发布文件。输入SHA256、完整序列与记录见同目录JSON。</p>']
(O/'MiUrchin_primer_review.html').write_text(''.join(parts))
print('HTML report complete; clade entries',len(clade))
