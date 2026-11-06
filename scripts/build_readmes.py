"""Restore the historical README layout using the current adopted catalog."""
from pathlib import Path
import json,shutil
P=Path(__file__).resolve().parents[1];rows=json.loads((P/'results/catalog.json').read_text())['assays']
shutil.copyfile(P/'legacy/v1.2/figures/MiUrchin_overview.png',P/'figures/MiUrchin_overview.png')
shutil.copyfile(P/'legacy/v1.2/sequences/all_markers.fasta',P/'sequences/non_partitioned.fasta')
import csv
with (P/'sequences/non_partitioned_pairs.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['id','gene','parent','F','R'],lineterminator='\n');w.writeheader();w.writerows(json.loads((P/'results/catalog.json').read_text())['originals'])
for name,lang in [('README.md','tw'),('README.zh-CN.md','cn'),('README.en.md','en')]:
 en=lang=='en';old=(P/'legacy/v1.2'/name).read_text();head=old.split('<!-- publication:start -->')[0]
 text=head+('> Original overview artwork; its bp labels describe the historical 16S windows, not every current branch assay.\n\n' if en else '> 保留原版概览图；图中 bp 数为历史 16S 窗口长度，不代表所有新版分支引物的产物长度。\n\n')
 text+='<!-- publication:start -->\n**'+('Manuscript revised 6 November 2026 · Computational study · Not peer reviewed.' if en else '稿件修订于 2026-11-06 · 计算研究 · 未经同行评审。')+'**\n\n[PDF](publications/manuscript_20261106/MiUrchin_manuscript.pdf) · [Word](publications/manuscript_20261106/MiUrchin_manuscript.docx) · [Markdown](publications/manuscript_20261106/MiUrchin_manuscript.md) · [CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [Supplement](publications/MiUrchin_supplement.md)\n<!-- publication:end -->\n\n'
 text+=('MiUrchin contains 76 branch/taxon-limited pairs across 16S, 12S, COI and 28S: 65 priority and 11 conditional entries. Use each pairing in a separate PCR.\n\n## Choosing an assay\n\nChoose the target group first, then marker and parent scheme. Priority entries have at least a 5°C modeled structure margin; conditional entries require additional assessment. The 32 parent schemes do not imply identical binding coordinates or ordinary/D sequence inclusion.\n\n## Primer sequences and predicted performance\n\nAll sequences are 5′→3′. Coverage and exact matching are record counts on each row’s design panel. Strict non-target counts are WC / GT. These are in-sample predictions, not experimentally validated detection rates.\n' if en else 'MiUrchin 收录 76 对分支／分类群限定引物，涵盖 16S、12S、COI 和 28S：65 对优先验证，11 对条件备选。每个 F/R 组合分别 PCR。\n\n## 如何选择窗口\n\n先选择适用分类群，再选择基因和原方案。优先方案在两种浓度下的结构温度余量均至少为 5°C；条件备选需要进一步评估。32 组原方案不再意味着普通／D引物具有相同坐标或包含关系。\n\n## 引物序列与预测表现\n\n序列均按 5′→3′ 书写。“覆盖”和“完全匹配”为各行设计面板的参考记录数；“严格非目标”为 WC / GT 两种模型的计数。面板内计算匹配不等于实验检出率。\n')
 for g in ['16S','12S','COI','28S']:
  text+='\n### '+g+'\n\n'
  text+=('| Scheme / group | Tier | F (5′→3′) | R (5′→3′) | Covered | Exact | Strict non-target |\n' if en else '| 方案／分类群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目标 |\n')+'| --- | --- | --- | --- | --- | --- | --- |\n'
  for r in rows:
   if r['gene']!=g:continue
   tier=r['tier'] if en else ('优先' if r['tier']=='priority' else '条件备选');text+=f"| {r['parent']} / {r['target_group']} | {tier} | `{r['F']}` | `{r['R']}` | {r['covered']}/{r['n_records']} | {r['exact']}/{r['n_records']} | {r['background']['WC_le2last3']} / {r['background']['GT_le2last3']} |\n"
 text+='\n[CSV](sequences/primer_pairs.csv) · [FASTA](sequences/all_markers.fasta) · [Priority FASTA](sequences/priority.fasta) · [Conditional FASTA](sequences/conditional.fasta)\n\n'
 text+=('## Binding sites and comparisons\n\nShifted binding sites are specific to the applicable reference records. See the [full evidence catalog](results/catalog.json) and [comparison table](report.html); historical coordinates are not presented as current coordinates.\n\n' if en else '## 结合位置与逐碱基匹配\n\n移动后的结合位置依各自参考记录核验。详见[完整证据清单](results/catalog.json)与[原版／新版比较](report.html)；历史坐标和匹配图不作为新引物的结果。\n\n')
 text+='![Exact comparison](figures/exact_comparison.svg)\n\n'
 text+=('## Reference panels and screening\n\nFinal three bases must match under WC; each end allows at most two total mismatches. Background counts must not exceed the original assay. All variants were checked for structures in two concentration scenarios. [Methods](docs/METHODS.md) · [Reproducibility](docs/REPRODUCIBILITY.md).\n\n## Historical supplementary analyses\n\n[Archived v1.2](legacy/v1.2/README.en.md) retains the old common-panel, holdout and barcode analyses. They do not validate the new sequences. No current independent holdout or wet-lab validation is claimed. Do not directly pool subprimers: cross-pair non-target hits remain.\n\n' if en else '## 参考面板与筛选规则\n\n双端最后三位须严格 WC 匹配，每端总错配最多两处；四项非目标计数不得高于原引物。全部简并变体在两种浓度下检查结构。[中文方法](docs/METHODS.zh-CN.md) · [重现说明](docs/REPRODUCIBILITY.zh-CN.md)。\n\n## 16S 补充评价\n\n[历史 v1.2](legacy/v1.2/README.zh-CN.md)保留旧版共同面板、留出与条码分析，不用于验证新序列。目前尚无独立留出或湿实验验证。子引物不可直接混合，交叉配对仍可命中非目标。\n\n')
 text+=('## Citation and copyright\n\n' if en else '## 引用与著作权\n\n')+'[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [COPYRIGHT](COPYRIGHT.md)\n\n'+('## References\n\n' if en else '## 参考文献\n\n')+'[MiFish](https://doi.org/10.1098/rsos.150088) · [Anth-28S](https://doi.org/10.7717/peerj.18607) · [Echinoid phylogenomics](https://doi.org/10.7554/eLife.72460)\n'
 if lang=='tw':
  for a,b in [('引物','引子'),('概览','概覽'),('图','圖'),('历史','歷史'),('数','數'),('为','為'),('窗口','區段'),('当前','目前'),('记录','紀錄'),('优先','優先'),('验证','驗證'),('条件','條件'),('备选','備選'),('对','對'),('实验','實驗'),('匹配','匹配'),('与','與'),('分类','分類'),('选择','選擇'),('结','結'),('规','規'),('则','則'),('说明','說明'),('复','複'),('据','據'),('标','標'),('评','評'),('计','計'),('应','應'),('码','碼'),('筛','篩'),('经','經'),('独','獨'),('发','發'),('补','補')]:text=text.replace(a,b)
 # Put the unchanged original, non-taxon-partitioned assays first.
 start={'en':'## Choosing a window','cn':'## 如何选择窗口','tw':'## 如何選擇擴增區段'}[lang]
 end={'en':'## Binding','cn':'## 结合位置','tw':'## 結合位置'}[lang]
 original=old[old.index(start):]
 original=original[:original.index(end)]
 import re
 original=re.sub(r'\]\((?!https?:|#)([^)]+)\)',lambda m:'](legacy/v1.2/'+m[1]+')',original)
 intro=(
 'The original **32 non-taxon-partitioned pairs (ordinary and D)** remain the primary collection and are shown first below. Their sequences and original evaluation results are unchanged. The 76 branch/taxon-limited entries are retained as supplementary optimization candidates, not replacements.\n\n[Primary collection FASTA](sequences/non_partitioned.fasta) · [Primary collection CSV](sequences/non_partitioned_pairs.csv) · [Original manuscript](legacy/v1.2/publications/MiUrchin_preprint.pdf)\n\nOriginal tables use their original evaluable-species denominators. Supplementary branch tables use selected design-record panels; these percentages are not directly interchangeable. Neither collection is wet-lab validated here.\n\n'
 if en else
 '原来的 **32 对不按分类群拆分的引物（普通及 D）**继续作为主方案保留，优先展示如下，序列及原始评价结果均保持不变。76 对分支／分类群限定引物作为补充优化方案保留，不替代原方案。\n\n[主方案 FASTA](sequences/non_partitioned.fasta) · [主方案 CSV](sequences/non_partitioned_pairs.csv) · [原方案预印本](legacy/v1.2/publications/MiUrchin_preprint.pdf)\n\n原方案表格使用原有可评价物种分母；补充分支方案使用筛选后的设计记录面板，两者百分比不能直接互换。这里不宣称两套方案已经湿实验验证。\n\n')
 branch=text[text.index('## Choosing an assay' if en else ('## 如何選擇' if lang=='tw' else '## 如何选择窗口')):]
 pub=head+('**Original non-partitioned collection first · Branch candidates as supplements**\n\n' if en else '**原始不分分类群方案优先展示 · 分支方案作为补充**\n\n')
 pub+=('Revised manuscript (6 November 2026)' if en else '修订稿件（2026-11-06）')+' · [PDF](publications/manuscript_20261106/MiUrchin_manuscript.pdf) · [Word](publications/manuscript_20261106/MiUrchin_manuscript.docx) · [Markdown](publications/manuscript_20261106/MiUrchin_manuscript.md)\n\n'
 text=pub+intro+original+'\n## '+('Supplementary branch-specific optimization' if en else '补充：分支／分类群优化方案')+'\n\n'+('[Branch manuscript](publications/MiUrchin_preprint.pdf) · [Branch catalog](results/catalog.json)\n\n' if en else '[分支优化预印本](publications/MiUrchin_preprint.pdf) · [分支证据清单](results/catalog.json)\n\n')+'<details>\n<summary>'+('Expand the 76 supplementary branch assays and methods' if en else '展开 76 对补充分支引物及方法说明')+'</summary>\n\n'+branch+'\n</details>\n'
 if lang=='tw':
  for a,b in [('原来的','原來的'),('对','對'),('分类','分類'),('优先','優先'),('补充','補充'),('序列及原始评价结果均保持不变','序列及原始評價結果均保持不變'),('引物','引子'),('记录','紀錄'),('验证','驗證'),('实验','實驗'),('预印本','預印本'),('方案优先展示','方案優先展示'),('优化','優化'),('证据','證據'),('清单','清單'),('展开','展開'),('与','與'),('筛选','篩選')]:text=text.replace(a,b)
 (P/name).write_text(text)
