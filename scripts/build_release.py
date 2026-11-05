"""Generate current documentation, catalogs, figures and manuscript from one audited catalog."""
from pathlib import Path
import json,csv,collections,hashlib,html,math
P=Path(__file__).resolve().parents[1];cat=json.loads((P/'results/catalog.json').read_text());R=cat['assays'];version=cat['version'];genes=['16S','12S','COI','28S'];I=dict(zip('ACGTRYSWKMBDHVN',['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']));deg=lambda s:math.prod(len(I[x]) for x in s)
source1=json.loads((P/'results/evidence/round1.json').read_text());source2=json.loads((P/'results/evidence/round2.json').read_text())
(P/'results/pools.json').write_text(json.dumps(source1['pools']+source2['pools'],ensure_ascii=False,indent=2))
# Canonical catalog is the only current primer source.
flat=[]
for r in R:flat.append(dict(id=r['id'],gene=r['gene'],parent=r['parent'],mode=r['mode'],target_group=r['target_group'],tier=r['tier'],F=r['F'],R=r['R'],deg_F=deg(r['F']),deg_R=deg(r['R']),n_records=r['n_records'],covered=r['covered'],original_covered=r['original_covered'],exact=r['exact'],original_exact=r['original_exact'],minimum_structure_margin=r['minimum_structure_margin'],use=r['use']))
with (P/'sequences/primer_pairs.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
for name,subset in [('all_markers.fasta',R),('primers.fasta',R),('priority.fasta',[r for r in R if r['tier']=='priority']),('conditional.fasta',[r for r in R if r['tier']=='conditional'])]:
 (P/'sequences'/name).write_text(''.join('>'+r['id']+'_'+s+' | '+r['tier']+' | separate_PCR\n'+r[s]+'\n' for r in subset for s in ['F','R']))
for g in genes:
 d=P/'markers'/g;d.mkdir(parents=True,exist_ok=True);rr=[r for r in R if r['gene']==g];(d/'primers.fasta').write_text(''.join('>'+r['id']+'_'+s+'\n'+r[s]+'\n' for r in rr for s in ['F','R']));(d/'README.md').write_text(f'# {g}: current branch assays\n\n{len(rr)} catalog entries. Use ../../results/catalog.json and ../../sequences/primer_pairs.csv as the canonical source. These are separate-PCR, design-panel-limited candidates. Historical panels and coordinates are in ../../legacy/v1.2/.\n')
counts=[dict(gene=g,priority=sum(r['gene']==g and r['tier']=='priority' for r in R),conditional=sum(r['gene']==g and r['tier']=='conditional' for r in R),parents=len(set(r['parent'] for r in R if r['gene']==g))) for g in genes]
summary='| Gene | Parent schemes | Priority pairs | Conditional pairs |\n| --- | --- | --- | --- |\n'+''.join(f"| {x['gene']} | {x['parents']} | {x['priority']} | {x['conditional']} |\n" for x in counts)
parents=[]
for o in cat['originals']:
 rr=[r for r in R if r['gene']==o['gene'] and r['parent']==o['parent']];parents.append(dict(gene=o['gene'],parent=o['parent'],pairs=len(rr),groups=[r['target_group'] for r in rr],n=sum(r['n_records'] for r in rr),old=sum(r['original_covered'] for r in rr),new=sum(r['covered'] for r in rr)))
(P/'results/parent_summary.json').write_text(json.dumps(parents,indent=2))
table='| ID / target group | Tier | F (5′–3′) | R (5′–3′) | n records | Covered original → current | Exact original → current |\n| --- | --- | --- | --- | --- | --- | --- |\n'+''.join(f"| {r['id']} / {r['target_group']} | {r['tier']} | `{r['F']}` | `{r['R']}` | {r['n_records']} | {r['original_covered']} → {r['covered']} | {r['original_exact']} → {r['exact']} |\n" for r in R)
method='''# Current methods and evidence boundaries

The v2.0.0 catalog contains 76 branch/taxon-limited assay entries, derived from 32 historical ordinary/D schemes. Ordinary oligos contain only A/C/G/T. A D scheme may become nondegenerate within a conserved group. Names do not imply that a D assay contains its ordinary counterpart or shares identical coordinates. Each row is a separate PCR pairing; it is not a component of an approved multiplex.

## Design

Existing target labels were stratified into Cidaroidea, Aulodonta, Echinacea and Irregularia and, when useful, smaller order or genus-labelled groups. Genus labels are not newly verified monophyletic clades. Nuclear 28S taxonomy was transferred only for exact species-name matches to existing metadata; unresolved labels were not guessed. Groups contained at least three records. Record counts, rather than species-level detection rates, are the current comparison unit.

D design first covers observed final-three-base variants, then explores internal degeneracy. The initial search allowed up to 64 concrete variants per oligo; the shifted-window search used a 16-variant cap. Ordinary candidates retain concrete bases and require a conserved terminal triplet within the selected design group. Initial candidates used homologous sites or uniquely located raw-sequence pairs whose terminal eight bases agreed with the homologous templates. Five-prime trimming was allowed. The second round searched 18–27 nt primers with 3-prime endpoints moved by up to 20 nt per direction; COI S extended this to 50 nt and added genus-labelled groups. Only the top-ranked subsets entered background screening. This was a finite heuristic search, not a global optimum.

## Target and non-target matching

Both sequence orientations are scanned. Target products span 60–650 bp with non-overlapping primer sites. Coverage requires at most two mismatches per primer and exact IUPAC compatibility at the final three positions. Exact matching requires no mismatches at either end. Ambiguous template bases at binding sites are excluded. Background geometry allows 0–1,000 internal bases. Four background quantities are retained: strict Watson–Crick (WC), strict GT-permissive, relaxed WC with three mismatches per end, and relaxed GT with two. Strict models retain the terminal-triplet criterion; the GT model also permits its defined wobble compatibility there. The target terminal rule uses WC only.

Every adopted row covers all records in its own design panel and has each of the four background counts no higher than its original assay, re-scanned on the same inputs. Nonzero original/background counts can therefore remain. These are counts of known background records, not estimates of environmental specificity. The background does not test exclusivity against other echinoid branches. Separate PCR and downstream taxonomic assignment are required.

## Thermodynamic screening

Primer3-py 2.4.0 expands all IUPAC variants. Hairpins, homodimers, within-direction variant heterodimers and F/R heterodimers are tested. Monovalent salt is 50 mM, Mg 1.5 mM and dNTP 0.6 mM. Scenarios are 50 nM per variant and 200 nM total per direction, divided by its variant count. Both require structure Tm below 55 °C, oligo Tm 45–75 °C and a forward/reverse Tm-range-midpoint difference no greater than 5 °C. The heterodimer calculation uses the larger participating concentration. These are screening assumptions, not validated PCR conditions.

Priority rows have at least a 5 °C gap between the lowest primer Tm and the largest structure Tm in each scenario. Eleven rows pass the primary gates but have a smaller gap and remain conditional. Adapters and indices were not included. Mixed subprimer pools were assessed for cross-dimers and cross F/R products, but are not recommended: COI S cross-pair background matches and other relaxed hits remain. Use each listed F/R pairing separately.

## Verification and limitations

The current revalidation compiles an exhaustive C++ scanner, recomputes each candidate and its original comparator on frozen target/background FASTA files, and checks all four background metrics. A separate Python motif-extension implementation verifies candidate target pairing. Both thermodynamic scenarios are recalculated. The shifted candidates also have independent intended-position and product-length checks in the adopted round-two evidence.

All design and selection results are in-sample. No independent holdout test or wet-lab validation has been performed on these 76 assays. Historical 16S common-panel, genus-blocked and barcode-resolution analyses describe historical primers only. They must not be transferred to the new assays, especially those with shifted endpoints. Barcode discrimination for the new products remains unassessed. Incomplete or unclassified references are not counted as successful detection, and small groups do not establish coverage of unsampled relatives.
'''
(P/'docs/METHODS.md').write_text(method)
cn='''# 当前方法与证据边界

当前统一清单包含76对分支／分类群限定方案，覆盖32组历史普通／D方案。65对优先验证、11对条件备选。全部按独立F/R组合分别PCR，不是可直接混用的引物池。普通引物保持非简并；某些D方案在保守分支内也可以成为非简并。

首先保障设计组内双端3′最后三位匹配，再分配内部简并或移动窗口。首轮最多64个变体／端，移动窗口轮最多16个；后者长度18–27nt，一般端点移动±20nt，COI S扩展至±50nt。每组至少3条记录，属级分组不等于重新验证了单系性。

所有覆盖率只指该行设计记录。目标双端各≤2错配且末端三位严格WC相容，产物60–650bp；背景两引物间距0–1000bp。严格WC／GT与宽松WC≤3／GT≤2四项计数均不得高于原引物，不要求原本非零的计数变为零。没有验证分支特异性，也没有把其他海胆全部作为该分支的非目标。

展开全部简并变体，检查发夹、自二聚体、池内变体相互二聚体及F/R异二聚体。50nM／变体与200nM／方向两情景；单价盐50mM、Mg1.5mM、dNTP0.6mM；结构Tm<55°C、引物Tm45–75°C、中点Tm差≤5°C。结构温度余量至少5°C列为优先，其余为条件备选。未加入接头，不能据此直接确定实验退火温度。

全部76对已用冻结原始序列重新扫描并核对原版对照；独立Python算法复核目标配对，两种浓度下结构参数重新计算。移动窗口候选另核对预定位置和产物长度。COI S等混合方案存在交叉非目标命中，因此分别PCR。

设计和筛选使用相同面板，没有独立留出或湿实验验证。历史物种覆盖、共同面板、属级留出和条码分辨率结果归入legacy/v1.2，不能描述新引物。新扩增子的条码分辨率未重评；缺失、分类未定及未采样物种不能计为已覆盖。
'''
(P/'docs/METHODS.zh-CN.md').write_text(cn)
repro='''# Reproducibility

Current source of truth: `results/catalog.json`. Inputs: `data/<gene>/{target,background}.fasta`. Adopted evidence: `results/evidence/round1.json` and `round2.json`. Current tables and FASTA are generated, not edited independently.

Install `requirements.txt` with Python 3.12 and provide a C++17 compiler. Run from the project root:

```sh
python scripts/revalidate.py --thermal
python scripts/build_release.py
python scripts/build_paper.py
python scripts/stamp_checksums.py
python check_release.py
```

`revalidate.py` writes only a validation report and uses a temporary directory for compiled scans. It verifies all 76 candidate pairs, their 32 original comparators on the same accession sets, four background counts, a separate target-matching implementation and both thermodynamic scenarios. It does not rerun an exhaustive global primer-design search. Finite-search candidate histories are retained in the two evidence JSON files; historical design tools are archived under `legacy/v1.2/`.

Publication and remote tagging are manual. The validation workflow has read-only repository permissions and does not push commits or create releases. v2.0.0 denotes the local integrated revision until explicitly published.
'''
(P/'docs/REPRODUCIBILITY.md').write_text(repro)
(P/'docs/REPRODUCIBILITY.zh-CN.md').write_text('# 重现说明\n\n当前序列唯一来源为results/catalog.json。先运行scripts/revalidate.py --thermal，再生成文档、PDF和哈希，最后运行check_release.py。完整命令见[英文重现说明](REPRODUCIBILITY.md)。该流程重现已采用候选的验证，不宣称重跑全局最优设计搜索。\n')
(P/'docs/MIGRATION.md').write_text('# v1.2 → v2.0.0\n\n32 historical assays → 76 branch/taxon-specific entries, including 65 priority and 11 conditional entries. The catalog contains 152 named directional records; identical sequences across entries are allowed and are not additional independent discoveries. All 32 historical parent schemes now have at least one limited candidate, not whole-clade coverage. Historical source files are unchanged under legacy/v1.2. Old check scripts and auto-publication logic are archived. Existing untracked ResearchGate material is preserved as historical user material and is not part of current release claims.\n')
for filename,lead in [('README.md','# MiUrchin：海膽分支限定引子與計算驗證\n\n**Fei Xia · v2.0.0 本地整合修訂 · 尚未遠端發佈或經同儕審查**\n\n目前採用76對分支／分類群限定方案：65對優先驗證、11對條件備選。每對分別PCR；設計面板內末端三位匹配不等於對全部海膽有效。\n'),('README.zh-CN.md','# MiUrchin：海胆分支限定引物与计算验证\n\n**Fei Xia · v2.0.0 本地整合修订 · 尚未远端发布或经同行评审**\n\n当前采用76对分支／分类群限定方案：65对优先验证、11对条件备选。每对分别PCR；设计面板内末端三位匹配不等于对全部海胆有效。\n'),('README.en.md','# MiUrchin: branch-limited sea-urchin primer candidates\n\n**Fei Xia · v2.0.0 local integrated revision · Not remotely published or peer reviewed**\n\nThe adopted catalog contains 76 branch/taxon-limited pairs: 65 priority and 11 conditional. Use each F/R combination in a separate PCR. In-sample terminal-triplet compatibility does not establish coverage of all Echinoidea.\n')]:
 (P/filename).write_text(lead+'\n'+summary+'\n[Current interactive catalog](report.html) · [Complete pair table](sequences/primer_pairs.csv) · [Priority FASTA](sequences/priority.fasta) · [Conditional FASTA](sequences/conditional.fasta) · [All adopted FASTA](sequences/all_markers.fasta)\n\n![Current catalog](figures/catalog_counts.svg)\n\n[Methods](docs/METHODS.md) · [中文方法](docs/METHODS.zh-CN.md) · [Reproduce](docs/REPRODUCIBILITY.md) · [Migration](docs/MIGRATION.md) · [Manuscript](publications/MiUrchin_preprint.pdf) · [Supplement](publications/MiUrchin_supplement.md)\n\nThe current unit is a reference record in an assay-specific design panel. Target coverage, exact matches, baseline comparisons, four background models and both thermodynamic scenarios are available in [the canonical evidence catalog](results/catalog.json). No independent holdout or wet-lab validation is claimed. Shifted barcode resolution has not been evaluated. Mixed subprimer pools are not recommended; COI S cross-pair products include non-target records.\n\nHistorical 32-pair sequences, common-panel results, barcode analyses, figures and preprint are frozen in [legacy/v1.2](legacy/v1.2/README.md); they do not describe the current primers.\n')
# Localize the current entry pages without modifying canonical sequence data.
for fname,traditional in [('README.zh-CN.md',False),('README.md',True)]:
 f=P/fname;s=f.read_text()
 translations={
 'Gene':'基因','Parent schemes':'原方案数','Priority pairs':'优先验证','Conditional pairs':'条件备选',
 'Current interactive catalog':'当前交互清单','Complete pair table':'全部引物表','Priority FASTA':'优先序列 FASTA','Conditional FASTA':'条件备选 FASTA','All adopted FASTA':'全部采用序列 FASTA','Current catalog':'当前清单',
 'Methods':'方法','Reproduce':'重现说明','Migration':'版本整合说明','Manuscript':'预印本','Supplement':'补充表',
 'The current unit is a reference record in an assay-specific design panel. Target coverage, exact matches, baseline comparisons, four background models and both thermodynamic scenarios are available in [the canonical evidence catalog](results/catalog.json). No independent holdout or wet-lab validation is claimed. Shifted barcode resolution has not been evaluated. Mixed subprimer pools are not recommended; COI S cross-pair products include non-target records.':'当前统计单位是各方案设计面板中的参考记录。覆盖、精确匹配、原版对照、四项非目标计数与两种浓度下的结构结果见[统一证据清单](results/catalog.json)。尚无独立留出或湿实验验证；移动后条码分辨率未重评。不推荐直接混合子引物，COI S交叉配对可命中非目标。',
 'Historical 32-pair sequences, common-panel results, barcode analyses, figures and preprint are frozen in [legacy/v1.2](legacy/v1.2/README.md); they do not describe the current primers.':'历史32对序列、共同面板、条码分析、图表与预印本完整保存在[legacy/v1.2](legacy/v1.2/README.md)，不用于描述当前新引物。'}
 for old,new in translations.items():s=s.replace(old,new)
 if traditional:
  for old,new in [('当前','目前'),('清单','清單'),('优先','優先'),('验证','驗證'),('备选','備選'),('条','條'),('录','錄'),('数','數'),('据','據'),('实验','實驗'),('图','圖'),('对','對'),('与','與'),('种','種'),('体','體'),('内','內'),('旧','舊'),('历史','歷史'),('标','標'),('码','碼'),('发','發'),('独','獨'),('组','組'),('结果','結果'),('浓','濃'),('实','實'),('热','熱'),('为','為'),('该','該'),('单','單'),('动','動'),('阶','階'),('现','現'),('说明','說明'),('引物','引子'),('补','補'),('无','無')]:s=s.replace(old,new)
 f.write_text(s)

# Current report: filterable rows and exact evidence values.
report=['<!doctype html><meta charset="utf-8"><title>MiUrchin v2.0.0</title><style>body{font:15px/1.6 system-ui;margin:25px;color:#173642}table{border-collapse:collapse;width:100%;font-size:12px}th,td{padding:7px;border:1px solid #ccd8dd;vertical-align:top}th{background:#dcecf0;position:sticky;top:0}code{white-space:nowrap}.conditional{background:#fff0d6}input{padding:10px;width:60%}</style><h1>MiUrchin v2.0.0 · Current adopted catalog</h1><p>76 separate-PCR entries; 65 priority / 11 conditional. All results are in-sample, record-based computational predictions. No remote publication, wet-lab validation or independent holdout is claimed.</p><p><a href="docs/METHODS.zh-CN.md">中文方法</a> · <a href="docs/METHODS.md">Methods</a> · <a href="sequences/priority.fasta">Priority FASTA</a> · <a href="sequences/conditional.fasta">Conditional FASTA</a> · <a href="legacy/v1.2/README.md">Historical v1.2</a></p><input id="q" placeholder="Filter marker, parent, taxon or tier"><table><thead><tr><th>Assay / group / tier</th><th>F and R, 5′–3′</th><th>n; baseline → current covered / exact</th><th>Background current / baseline: WC,GT,WC3,GT2</th><th>Minimum structure margin</th></tr></thead><tbody>']
for r in R:
 bg=' · '.join(str(r['background'][k])+'/'+str(r['original_background'][k]) for k in ['WC_le2last3','GT_le2last3','WC_le3','GT_le2']);report.append(f"<tr class='{r['tier']}'><td>{r['id']}<br>{r['target_group']} · {r['tier']}</td><td>F <code>{r['F']}</code><br>R <code>{r['R']}</code></td><td>n={r['n_records']}<br>{r['original_covered']} → {r['covered']} / {r['original_exact']} → {r['exact']}</td><td>{bg}</td><td>{r['minimum_structure_margin']:.2f} °C</td></tr>")
report.append('</tbody></table><script>document.getElementById("q").oninput=e=>{for(const r of document.querySelectorAll("tbody tr"))r.hidden=!r.textContent.toLowerCase().includes(e.target.value.toLowerCase())}</script>');(P/'report.html').write_text(''.join(report))
# Scientific vector figures: standard reportlab graphics, not generative imagery.
from reportlab.graphics.shapes import Drawing,Rect,String,Line,Circle
from reportlab.graphics import renderSVG,renderPDF
from reportlab.lib.colors import HexColor
blue=HexColor('#207c91');amber=HexColor('#d39431');grey=HexColor('#657981')
def save(d,name):
 for folder in [P/'figures',P/'publications/figures']:
  renderSVG.drawToFile(d,str(folder/(name+'.svg')));renderPDF.drawToFile(d,str(folder/(name+'.pdf')))
d=Drawing(520,260);d.add(String(35,235,'Adopted assay entries by marker',fontSize=16));d.add(String(35,217,'Entries, not unique sequences or independent biological replicates',fontSize=9))
for i,x in enumerate(counts):
 xx=70+i*115;scale=6;d.add(Rect(xx,50,42,x['priority']*scale,fillColor=blue,strokeColor=None));d.add(Rect(xx,50+x['priority']*scale,42,x['conditional']*scale,fillColor=amber,strokeColor=None));d.add(String(xx,32,x['gene'],fontSize=11));d.add(String(xx+8,55+(x['priority']+x['conditional'])*scale,str(x['priority']+x['conditional']),fontSize=10))
d.add(Rect(55,10,9,9,fillColor=blue,strokeColor=None));d.add(String(70,10,'Priority (65)',fontSize=9));d.add(Rect(175,10,9,9,fillColor=amber,strokeColor=None));d.add(String(190,10,'Conditional (11)',fontSize=9));save(d,'catalog_counts')
d=Drawing(500,380);d.add(String(50,355,'Exact pairing on each assay-specific design panel',fontSize=15));d.add(String(50,337,'Each point is one catalog entry; both axes use the same accession set',fontSize=9));d.add(Line(70,55,360,55));d.add(Line(70,55,70,315));d.add(Line(70,55,360,315,strokeColor=grey,strokeDashArray=[3,3]))
for v in [0,.25,.5,.75,1]:d.add(String(64+290*v,38,str(int(v*100)),fontSize=8));d.add(String(40,52+260*v,str(int(v*100)),fontSize=8))
for r in R:d.add(Circle(70+290*r['original_exact']/r['n_records'],55+260*r['exact']/r['n_records'],3,fillColor=blue if r['tier']=='priority' else amber,strokeColor=None))
d.add(String(140,18,'Original exact pairing (%)',fontSize=10));d.add(String(8,325,'Current (%)',fontSize=10));save(d,'exact_comparison')
d=Drawing(500,340);d.add(String(45,315,'Structure margin in both concentration scenarios',fontSize=15));d.add(String(45,297,'One point per assay and scenario; conditional entries retained explicitly',fontSize=9));d.add(Line(65,45,430,45));d.add(Line(65,45,65,275))
for v in range(40,81,10):d.add(String(60+(v-40)/40*365,28,str(v),fontSize=8))
for v in range(-20,61,20):d.add(String(30,42+(v+20)/80*230,str(v),fontSize=8))
d.add(Line(65,45+(35+20)/80*230,65+25/40*365,275,strokeColor=grey,strokeDashArray=[3,3]))
for r in R:
 for t in r['thermal']:
  x=min(t['F_tm']+t['R_tm']);y=t['structure_max'];d.add(Circle(65+(x-40)/40*365,45+(y+20)/80*230,2.5,fillColor=blue if r['tier']=='priority' else amber,strokeColor=None))
d.add(String(145,10,'Minimum primer Tm (C)',fontSize=10));d.add(String(8,282,'Structure Tm (C)',fontSize=9));save(d,'structure_margin')
# Paper is newly scoped to the adopted catalog; historical metrics are not reused as new evidence.
unique_pairs=len(set((r['F'],r['R']) for r in R));unique_oligos=len(set(r[s] for r in R for s in ['F','R']))
paper=f'''# MiUrchin: terminal-triplet-first, branch-limited primer candidates for sea-urchin eDNA

**Fei Xia**

Local integrated computational manuscript v{version} · 5 November 2026 · Not peer reviewed or remotely published

## Abstract

We integrated two rounds of computational optimization into a catalog of 76 branch- or taxon-limited primer-pair entries derived from 32 historical ordinary and degenerate schemes across mitochondrial 16S, 12S and COI and nuclear 28S. Selection prioritized Watson–Crick compatibility at the final three primer positions within each design group. The catalog contains {unique_pairs} distinct F/R sequence combinations and {unique_oligos} distinct oligo sequences; repeated entries retain separate provenance and applicability. Each retained entry covers all records in its own selected design panel under a two-mismatch-per-end rule and does not exceed its original assay in four background-count comparisons. Exhaustive paired scans, an independent target-matching implementation and two thermodynamic concentration scenarios were reconciled. Sixty-five entries have a minimum modeled structure margin of at least 5 °C; eleven remain conditional. A second round moved binding endpoints and added 22 pairs for eight previously unresolved parent schemes. These are in-sample selection outcomes, not independent estimates of biological sensitivity. Mixed subprimer pools are not recommended, and barcode resolution for shifted products remains untested. The integrated resource provides explicit sequence provenance, separate-PCR pairings and reproducible computational checks while retaining the historical release unchanged.

## 中文摘要

本项目将两轮计算优化整合为76对分支或分类群限定方案，来源于四个标记的32组历史普通／D引物。设计首先保证各自设计面板内双端最后三位匹配，再优化内部简并、结合位置和结构。65对列为优先实验验证，11对保留为条件备选。原始序列扫描、独立算法及两种浓度情景下的结构结果一致。第二轮通过移动位置为此前未解决的8组加入22对候选。所有结果均为设计面板内计算筛选，不能解释为独立检出率，也不证明覆盖整个进化枝。建议分别PCR；移动后条码分辨率和湿实验性能尚未验证。

## Introduction

MiFish illustrates lineage-aware primer design around conserved mitochondrial sites, while Anth-28S illustrates incorporating supported nucleotide variants and separating divergent target groups (Miya et al., 2015; McCartin et al., 2024). These principles motivated a re-examination of the MiUrchin catalog. They do not validate sea-urchin primers by analogy. Deep echinoid relationships provide a useful stratification framework (Mongiardino Koch et al., 2022), but taxonomic labels in an archived library are not equivalent to a newly inferred phylogeny.

The present revision addresses a specific design requirement: observed variation at the terminal triplet must be handled before internal degeneracy is expanded. It also separates historical whole-panel summaries from branch-limited, selected-panel outcomes. Ordinary and D labels refer to their historical parent schemes; new endpoints, sequences and applicability can differ. No factorial comparison isolates a pure effect of degeneracy in this release.

## Materials and methods

### Frozen references and design panels

We used the existing project FASTA files without retrieving new public records. Marker-specific target and background inputs are hashed in the release manifest. Design groups used existing higher-taxon and order labels; exact species-name matches transferred available classifications to 28S. Unresolved labels were excluded from branch design. Later COI S searches included genus-labelled groups without asserting newly demonstrated monophyly. Each retained design group contains at least three records. Small and uneven groups limit generalization.

### Terminal-triplet-first search

Initial searches used existing homologous binding regions or unique nearest raw-sequence primer pairs whose terminal eight bases agreed with the reference alignment. Ordinary candidates remained concrete; D candidates first included all observed terminal-triplet bases, then considered internal ambiguity. The initial variant cap was 64 per end, with both terminal-only and internally expanded alternatives. Five-prime trimming was evaluated. A second round for 16S XL/XLD, 12S XS/S/L and COI XS/S/M searched 18–27 nt primers with endpoint offsets up to 20 nt; COI S extended this to 50 nt and finer taxonomic groups. This round capped degeneracy at 16 variants per end. Candidate ranking and top-subset screening make the search heuristic and finite.

### Paired matching and background gates

Both DNA orientations were scanned. Target products span 60–650 bp with non-overlapping primer sites. Coverage requires no more than two mismatches per end and WC-compatible final three bases; exact pairing requires no mismatches. Ambiguous binding-site template bases were excluded. Background scans permit 0–1,000 internal bases. We retained strict WC, strict GT-permissive, relaxed WC with three mismatches and relaxed GT with two mismatches per end. Only strict models preserve terminal-triplet compatibility; target matching uses WC. Every selected row matches its full design panel under the coverage rule and has no increase in any of the four background counts relative to its original parent on the same frozen input. Original nonzero counts can therefore remain. Background libraries do not establish specificity against all other sea-urchin branches.

### Structures, concentrations and pairing

Primer3-py 2.4.0 (Untergasser et al., 2012) expanded all variants and evaluated hairpins, homodimers, within-direction variant dimers and F/R dimers. Conditions were 50 mM monovalent salt, 1.5 mM Mg and 0.6 mM dNTP. Both 50 nM per variant and 200 nM total per direction were evaluated. Required limits were structure Tm below 55 °C, primer Tm 45–75 °C and F/R Tm-range-midpoint difference at most 5 °C. The larger participating concentration was used for heterodimers. Priority status additionally requires a 5 °C minimum primer-to-structure Tm margin in both scenarios. These model gates are not experimentally established annealing conditions. Sequencing adapters were not included.

### Verification and scope

The integrated validator recompiles the exhaustive C++ scanner and recalculates all candidate and baseline target/background quantities. A separate Python motif-extension implementation checks target pairing, and both thermodynamic scenarios are recomputed. The second-round evidence additionally checks intended shifted positions and product lengths. Cross-subprimer dimers and F-A/R-B products were evaluated separately. All proposed assays are designated for separate PCR. No independent holdout or wet-lab experiment was performed on the current catalog; historical holdout and barcode analyses are not transferred to these sequences.

## Results

### Catalog composition

{summary}

All 32 historical parent schemes have at least one group-limited candidate. This does not imply restoration of coverage across each original parent panel. There are 152 named directional FASTA records but only {unique_oligos} distinct sequences. Repeated sequences across provenance-defined entries are retained transparently. Sixty-five entries are priority and eleven conditional (Figure 1).

![Figure 1](figures/catalog_counts.svg)

**Figure 1.** Adopted entries by marker and tier. Counts refer to catalog entries, not unique sequences or independent assay discoveries.

### Same-panel comparisons and shifted candidates

Comparisons use exactly the accession set listed for each new entry. Coverage is 100% on these selected design sets by construction; it must not be presented as an unbiased sensitivity estimate. Exact matching can increase or decrease despite passing the coverage gate (Figure 2). For the eight unresolved parent schemes, the second round produced 22 additional pairs. On the union of their disjoint selected subgroup panels, 12S S coverage changed from 13/40 to 40/40, 12S L from 10/21 to 21/21, and COI S from 12/22 to 22/22. These fractions do not include unrepresented or unresolved taxa.

![Figure 2](figures/exact_comparison.svg)

**Figure 2.** Original versus current exact paired matching on each entry's own accession set. Multiple entries can share templates or sequences, so points are not independent biological replicates. The diagonal indicates equal exact proportions.

### Structural margins and mixed pools

Every adopted entry passed the two concentration-scenario gates. Eleven entries have a margin below 5 °C and remain conditional; modeled structure constraints therefore remain a material selection distinction (Figure 3). For the shifted COI S subprimer collection, unintended cross F/R combinations matched 26 strict-WC and 135 strict-GT background records. Passing individual-pair gates does not justify pooling. The current catalog prescribes separate PCRs.

![Figure 3](figures/structure_margin.svg)

**Figure 3.** Minimum primer Tm versus maximum structure Tm in each modeled scenario. The dashed line marks a 5 °C margin. Conditions are model assumptions and exclude adapters.

## Discussion

Terminal-triplet-first design can redirect degeneracy toward positions that were incompletely represented in previous candidates, while branch restriction and shifted sites can lower the burden on a single universal oligo. However, finer groups also make in-sample success easier to achieve. Neither the number of retained entries nor their complete design-panel coverage demonstrates superiority over an independently evaluated broad-range assay.

A central change in this revision is evidence bookkeeping. New branch-specific sequences, old parent comparisons and historical barcode-resolution studies have different scopes. Keeping them in separate versioned resources prevents the old common-panel and genus-blocked statistics from being interpreted as validation of new sequences. In particular, changes to product endpoints require renewed evaluation of taxonomic resolution. This has not yet been performed.

Small sample sizes, classification uncertainty, incomplete background sampling and absence of biological replication remain limitations. Genus-labelled COI S groups are not a substitute for phylogenetic testing. Other echinoids were not universally treated as negatives for each branch-specific candidate; the group label indicates design applicability, not proven branch exclusivity. Experimental work should test diverse samples, controls, concentration choices, adapters and cross-reactivity before practical use.

## Data, code and declarations

The local v2.0.0 integrated project contains a canonical JSON catalog, generated CSV/FASTA, frozen FASTA inputs, current verification code and immutable evidence from both rounds. The historical tracked v1.2 project is retained under legacy/v1.2. This local revision has not been remotely published; no release DOI or tag URL is asserted. Authorship is retained as Fei Xia. Funding, competing-interest and AI-assistance disclosure statements require author review before external submission; this manuscript does not infer those declarations.

## References

Miya M et al. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes. Royal Society Open Science 2:150088. https://doi.org/10.1098/rsos.150088

McCartin L et al. (2024). Nuclear eDNA metabarcoding primers for anthozoan coral biodiversity assessment. PeerJ 12:e18607. https://doi.org/10.7717/peerj.18607

Mongiardino Koch N et al. (2022). Phylogenomic analyses of echinoid diversification prompt a re-evaluation of their fossil record. eLife 11:e72460. https://doi.org/10.7554/eLife.72460

Untergasser A et al. (2012). Primer3—new capabilities and interfaces. Nucleic Acids Research 40:e115. https://doi.org/10.1093/nar/gks596

[Complete sequence and evidence supplement](MiUrchin_supplement.md)
'''
(P/'publications/MiUrchin_preprint.md').write_text(paper)
(P/'publications/MiUrchin_supplement.md').write_text('# MiUrchin v2.0.0 supplementary catalog\n\n76 provenance-defined assay entries. Record-based in-sample comparisons; use separate PCR. The 11 conditional entries are not elevated to priority. Complete numeric thermal and background evidence is in ../results/catalog.json.\n\n'+table)
(P/'publications/README.md').write_text('# Current manuscript\n\nMiUrchin_preprint.md/PDF describe the v2.0.0 branch-limited catalog. The prior v1.2 paper is archived under ../legacy/v1.2/publications. Existing untracked ResearchGate drafts in this folder are historical user files, not regenerated or endorsed by this revision. Build with scripts/build_paper.py, then inspect rendered pages. This is a local manuscript, not a remotely published release.\n')
(P/'publications/release.json').write_text(json.dumps({'version':version,'date':'2026-11-05','status':'local-unpublished','title':'MiUrchin: terminal-triplet-first, branch-limited primer candidates for sea-urchin eDNA','author':'Fei Xia'},indent=2))
(P/'CITATION.cff').write_text('cff-version: 1.2.0\nmessage: "Cite the exact catalog version used; v2.0.0 is a local unpublished revision."\ntype: software\ntitle: "MiUrchin: branch-limited sea-urchin primer candidates"\nauthors:\n  - family-names: Xia\n    given-names: Fei\nversion: "2.0.0"\nrepository-code: "https://github.com/GUIBA-EX/MiUrchin"\n')
(P/'CITATION.bib').write_text('@unpublished{Xia2026MiUrchin,\n author={Xia, Fei},\n title={MiUrchin: terminal-triplet-first, branch-limited primer candidates for sea-urchin eDNA},\n year={2026},\n note={Local integrated computational manuscript, version 2.0.0; not remotely published or peer reviewed}\n}\n')
(P/'CHANGELOG.md').write_text('# Changelog\n\n## 2.0.0 — 2026-11-05 (local integrated revision)\n\nAdopted 76 branch/taxon-limited pairs, retaining 65 priority and 11 conditional tiers. Unified catalog, raw revalidation, generated FASTA, three-language entry pages, current figures and rewritten manuscript. Archived v1.2 tracked source unchanged. Replaced legacy auto-publication with read-only validation. No remote push, tag or release. Historical user drafts preserved.\n')
print('Generated catalog/documentation/figures/manuscript:',len(R),'entries;',unique_pairs,'distinct pairs;',unique_oligos,'distinct oligos')

# Preserve the project's established README presentation.
import runpy
runpy.run_path(str(P/"scripts/build_readmes.py"),run_name="__main__")
