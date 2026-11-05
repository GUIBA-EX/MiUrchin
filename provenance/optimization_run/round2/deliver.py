import json,csv,collections,hashlib,zipfile,html
from pathlib import Path
O=Path('outputs/round2');O.mkdir(exist_ok=True)
rows=[];checks=[];candidates=[];manifests=[];pools=[]
for folder in ['round2','round2b']:
 b=Path('work')/folder;rows+=json.load(open(b/'verified_selected.json'));checks+=json.load(open(b/'independent_checks.json'));candidates+=json.load(open(b/'all_evaluated.json'));manifests+=json.load(open(b/'search_manifest.json'))
 for p in json.load(open(b/'pool_structure.json')):
  hs=collections.defaultdict(set)
  for h in csv.DictReader(open(b/'pools'/p['gene']/'independent_hits.tsv'),delimiter='\t'):
   if h['name'].startswith(p['gene']+'_'+p['parent']+'_cross_') and h['role']=='background':
    for flag in ['le2last3','le2','le3']:
     if h[flag]=='1':hs[h['model'],flag].add(h['accession'])
  p['cross_background']={m+'_'+f:len(hs[m,f]) for m,f in [('WC','le2last3'),('GT','le2last3'),('WC','le3'),('GT','le2')]};pools.append(p)
for r in rows:r['tier']='优先实验验证' if min(t['margin'] for t in r['thermal'])>=5 else '条件备选：结构温度余量不足5°C'
keys=[('16S','XL'),('16S','XLD'),('12S','XS'),('12S','S'),('12S','L'),('COI','XS'),('COI','S'),('COI','M')]
summary=[]
for g,n in keys:
 rr=[r for r in rows if r['gene']==g and r['parent']==n];summary.append(dict(gene=g,parent=n,subpairs=len(rr),n=sum(len(r['panel']) for r in rr),original_covered=sum(r['original_covered'] for r in rr),new_covered=sum(r['covered'] for r in rr),clades=[r['clade'] for r in rr]))
metadata=dict(date='2026-11-05',scope='Remaining 8 original assay groups; branch/taxon-limited candidates, not whole-Echinoidea replacement',search='primer length18–27nt; each 3prime endpoint shift−20..+20nt; COI S extended−50..+50nt and genus-label groups; minimum3 records per group; ordinary no degeneracy; D first covers all observed final3 then optional internal variants cap16 per primer',gates='all design records both primers<=2 mismatches with final3 exact; original and new scanned on same target/background files; background four counts not exceeding original; all IUPAC variants expanded; structureTm<55C, oligoTm45–75C, midpoint deltaTm<=5C in both 50nM/variant and 200nM/direction scenarios; 50mM monovalent,1.5mM Mg,0.6mM dNTP; no adapters; priority only if structure margin>=5C',validation='Independent full-sequence Python paired scan equals C++ exhaustive scan; additional direct validation at intended shifted positions with exact final3; cross F/R background scan and all-variant pool dimers; separate PCR recommended',limitations='same panel used for design and selection; no holdout or wetlab validation; existing local taxon labels, not new tree inference; genus-level groups not demonstrated monophyletic; non-target panel incomplete; specificity to the selected clade vs other echinoids not established',software={'primer3-py':'2.4.0'},input_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('work/validation').glob('*/*.fasta')})
result=dict(metadata=metadata,summary=summary,recommended=rows,independent_checks=checks,pools=pools,search_manifest=manifests,all_candidates=candidates)
(O/'remaining8_comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(O/'remaining8_recommended.fasta').write_text(''.join('>'+r['id']+'_'+s+' | '+r['tier']+' | separate_PCR\n'+r[s]+'\n' for r in rows for s in ['F','R']))
old=Path('outputs/MiUrchin_recommended.fasta').read_text();(O/'MiUrchin_combined_recommended.fasta').write_text(old+(O/'remaining8_recommended.fasta').read_text())
p=['<!doctype html><meta charset="utf-8"><title>MiUrchin 剩余8组优化</title><style>body{font:16px/1.6 system-ui;max-width:1550px;margin:30px auto;padding:20px;color:#173642}table{border-collapse:collapse;width:100%;font-size:13px}td,th{border:1px solid #ccd8df;padding:8px;text-align:left;vertical-align:top}th{background:#e3eff3}code{overflow-wrap:anywhere}.note{background:#fff1d5;padding:16px}h2{margin-top:32px}</style><h1>MiUrchin：剩余8组的结合位置与分支优化</h1><p>2026-11-05 · 普通引物仍保持非简并；XLD按末端三位优先加入简并。</p>',f'<p>搜索并完成非目标扫描的候选共{len(candidates)}组；本轮入选{len(rows)}组分支／分类群限定子引物，涉及{sum(s["subpairs"]>0 for s in summary)}/8组原方案。{sum(r["tier"]=="优先实验验证" for r in rows)}组列为优先实验验证，其他为条件备选。</p>', '<p class="note">获得某个分支的替代不等于覆盖该原方案的全部目标物种。所有推荐均限于表中分类群与已有设计记录，不代表已经实验验证，也没有证明只扩增该分支而排除其他海胆。建议分别PCR，不把子引物直接混合使用。</p><h2>与原方案比较：相同入选分支面板</h2><p>n为记录数；分支组合选择时排除重叠面板。原→新覆盖采用双端各≤2错配且末端三位完全相容。未进入设计的残缺、分类不明或定位不确定记录不计为成功。</p><table><tr><th>原方案</th><th>子引物对数</th><th>分支／分类群</th><th>n</th><th>原→新覆盖</th></tr>']
for s in summary:p.append(f"<tr><td>{s['gene']} {s['parent']}</td><td>{s['subpairs']}</td><td>{', '.join(s['clades'])}</td><td>{s['n']}</td><td>{s['original_covered']}→{s['new_covered']}</td></tr>")
p+=['</table><h2>推荐序列与验证结果</h2><p>序列均为5′→3′。F/R位移是沿各自引物方向的3′端移动量：正数表示3′端前移，负数表示后退；长度另行优化，不能把它直接理解为参考正链坐标增减。产物长度由原始序列预定位置独立核对。非目标新/原依次是严格WC、严格GT、宽松WC≤3、宽松GT≤2。</p><table><tr><th>编号／适用范围</th><th>F、R序列</th><th>端点位移F/R；产物范围</th><th>同面板覆盖／精确 原→新</th><th>简并F/R；结构Tm两情景</th><th>非目标 新/原</th></tr>']
for r in rows:
 bg=' · '.join(str(r['background'][k])+'/'+str(r['original_background'][k]) for k in ['WC_le2last3','GT_le2last3','WC_le3','GT_le2']);sz=r['anchored_product_lengths'];p.append(f"<tr><td>{r['gene']} {r['parent']} / {r['clade']}<br>{r['tier']}<br><small>{r['id']}</small></td><td>F <code>{r['F']}</code><br>R <code>{r['R']}</code></td><td>{r['F_shift']:+d} / {r['R_shift']:+d} nt<br>{min(sz)}–{max(sz)} bp</td><td>n={len(r['panel'])}<br>覆盖 {r['original_covered']}→{r['covered']}<br>精确 {r['original_exact']}→{r['anchored_exact']}</td><td>{r['deg_F']} / {r['deg_R']}<br>{r['thermal'][0]['structure_max']:.1f} / {r['thermal'][1]['structure_max']:.1f}°C</td><td>{bg}</td></tr>")
p+=['</table><h2>交叉配对与混合使用风险</h2><p>以下计算同一原方案内各子引物混合的所有变体相互二聚体，并额外扫描F-A/R-B等交叉配对；非目标为交叉组合并集，不含本来指定配对。结构通过也不代表混合扩增效率已验证。</p><table><tr><th>方案</th><th>池内最大二聚体Tm（50nM／200nM上界）</th><th>交叉配对非目标 严格WC/GT</th><th>结论</th></tr>']
for x in pools:p.append(f"<tr><td>{x['gene']} {x['parent']}</td><td>{x['structure_max']:.1f} / {x['structure_max_200nM_upper_bound']:.1f}°C</td><td>{x['cross_background']['WC_le2last3']} / {x['cross_background']['GT_le2last3']}</td><td>分别PCR；不推荐直接混合</td></tr>")
p+=['</table><h2>方法、证据和限制</h2><p>起始位置来自与原引物最接近且唯一的原始序列成对定位，并要求两端末端8位与原同源比对一致；再移动结合位置。一般搜索±20nt，COI S扩展±50nt。18–27nt长度，分支内至少3条记录。对普通引物要求末端三位在设计组内一致；D先合并末端三位的全部已观察碱基，再分配内部简并，每条最多16个变体。</p><p>每个候选逐变体检查Tm、发夹、自二聚体、同一简并池变体二聚体和F/R异二聚体。50nM/变体、200nM/方向两种浓度情景；单价盐50mM、Mg1.5mM、dNTP0.6mM。两情景均要求结构Tm&lt;55°C，引物Tm45–75°C，中点Tm差≤5°C。结构温度距离最低引物Tm不足5°C者明确降为条件备选，且这些数值不是实测退火条件。未含测序接头。</p><p>非目标使用原本地面板；扫描两条链，目标产物60–650bp，背景两引物间距0–1000bp。严格模型每端≤2错配且末端3位匹配；另计WC≤3与GT≤2的宽松结果。所有入选方案四项背景计数均不高于原引物。独立Python算法复核全部入选面板成对结果，并在预定移动位置再次逐碱基验证最后三位及产物长度。</p><p>分类基于现有项目标签。属级组是分类限定候选，不是此次新推断并验证的单系进化枝。设计／筛选使用同一面板，无独立留出或湿实验验证。末端匹配与无已知非目标命中不等于实际PCR无偏性；也未重评移动后条码的物种分辨率。少数记录的分支建议先扩大验证面板。</p><h2>下载</h2><p><a href="remaining8_recommended.fasta">本轮序列FASTA</a> · <a href="MiUrchin_combined_recommended.fasta">合并上轮54组的总FASTA</a> · <a href="remaining8_comparison.json">全部候选、失败原因、面板记录、序列、参数与输入哈希</a></p>']
(O/'remaining8_report.html').write_text(''.join(p))
with zipfile.ZipFile(O/'MiUrchin_remaining8_validation.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in O.iterdir():
  if f.suffix in ['.html','.json','.fasta']:z.write(f,f.name)
 for folder in ['round2','round2b']:
  b=Path('work')/folder
  for f in b.glob('*.py'):z.write(f,'scripts/'+folder+'/'+f.name)
  for f in b.glob('*/independent_hits.tsv'):z.write(f,'validation/'+folder+'/'+f.parent.name+'/'+f.name)
  for f in b.glob('pools/*/independent_hits.tsv'):z.write(f,'validation/'+folder+'/pools/'+f.parent.name+'/'+f.name)
  z.write(b/'independent_checks.json','validation/'+folder+'/independent_checks.json')
 for f in ['scan.cpp','independent_verify.py']:z.write(Path('work')/f,'scripts/'+f)
print('DELIVERED',len(rows),'subpairs;',sum(s['subpairs']>0 for s in summary),'of8 original groups')
for s in summary:print(s)
