# MiUrchin

[English](README.md) · [方法](docs/METHODS.zh-CN.md) · [复现](docs/REPRODUCIBILITY.md)

海胆线粒体16S引物：四个长度窗口保留单对与两对独立PCR方案，S和M同时比较普通、简并及互补组合。

长度依次为S、M、L、XL；单对直接使用长度名称，两对的具体配对加A、B，例如SA、SB，合用结果记为SA+SB。全部序列按5′→3′书写。

D仅用于简并配对；SD+SB与MD+MC分别表示简并单对加普通补充配对。MC是针对MD的普通补充引物。当前12套方案、18条配对记录，复用名称去重后为15个配对名、30条FASTA记录。

## 方案比较

共同面板为49个分类名称标签、80个标签内单倍型，采用标签等权及标签内单倍型等权。背景为6,045条记录。

| 方案 | 类型 | 对数 | 覆盖率 | 完全匹配率 | WC≤3 | GT≤2 | WC≤4 |
|---|---|---:|---:|---:|---:|---:|---:|
| S | 普通 | 1 | 40.82% | 20.41% | 0 | 3 | 4 |
| SA+SB | 普通 | 2 | 61.22% | 20.41% | 0 | 3 | 7 |
| SD | 简并 | 1 | 65.31% | 38.78% | 0 | 0 | 8 |
| SD+SB | 简并＋普通 | 2 | 79.59% | 38.78% | 0 | 3 | 10 |
| M | 普通 | 1 | 59.18% | 16.33% | 0 | 0 | 0 |
| MA+MB | 普通 | 2 | 77.55% | 16.33% | 1 | 1 | 30 |
| MD | 简并 | 1 | 87.76% | 48.98% | 0 | 1 | 0 |
| MD+MC | 简并＋普通 | 2 | 93.88% | 55.10% | 0 | 1 | 17 |
| L | 普通 | 1 | 75.51% | 19.39% | 2 | 1 | 161 |
| LA+LB | 普通 | 2 | 87.76% | 19.39% | 2 | 1 | 162 |
| XL | 普通 | 1 | 85.71% | 6.12% | 2 | 1 | 10 |
| XLA+XLB | 普通 | 2 | 100.00% | 26.53% | 0 | 2 | 9 |

覆盖允许每条引物最多2处错配，但3′末端3 nt必须完全匹配；完全匹配要求正反引物均0错配。GT为G–T容忍敏感性模型，单独统计，不算严格完全匹配。背景数字为accession数，非实验扩增比例。

**优先比较SD和MD单对。** SD覆盖65.31%、完全匹配38.78%；MD为87.76%和48.98%。补充普通引物后，SD+SB升至79.59%覆盖，MD+MC升至93.88%覆盖、55.10%完全匹配。两者都是一对简并加一对普通引物的独立PCR并集。

M普通单对也提高至59.18%覆盖、16.33%完全匹配；普通两对为77.55%和16.33%。S普通方案尚未改善。SD和MD均为F 12重、R 24重简并；同向总浓度固定时，每种实际序列的浓度会被分摊。完全匹配按IUPAC相容计算，不代表所有变体均匹配，也不等同于实验效率。

## 序列与证据

[Primer pairs](results/current/primer_pairs.csv) · [FASTA](results/current/primers.fasta) · [Comparison](results/current/comparison.csv) · [S/M missed references](results/sm_optimization/missed_references.csv) · [L/XL baseline gaps](results/compact/missed_references.csv) · [Verification](results/sm_optimization/verification.json)

## 碱基匹配图

显示实际碱基而非命中热图。蓝色表示IUPAC相容、橙色表示错配、紫色表示可能的G–T配对，方框标明3′末端3 nt。引物及同向参考按5′→3′展示；反向引物对应参考已反向互补。静态图展示两对方案及每目加权频率最高的结合序列；完整页面包含单对方案和目内所有不同结合序列。

![S base matching](figures/base_matching_S.svg)

![SD base matching](figures/base_matching_SD.svg)

![M base matching](figures/base_matching_M.svg)

![MD base matching](figures/base_matching_MD.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[S/M full base alignment](results/sm_optimization/base_matching.html) · [L/XL full base alignment](results/compact/base_matching.html)

## 适用范围

本轮优化共同面板，结果来自冻结参考库的计算筛选与全序列复核，尚无湿实验验证。区域面板的分类群组成不同，不能将共同面板结果视为全部海胆的覆盖。两对方案为独立PCR结果并集，尚未验证同管混合体系。

[Baseline analysis](docs/BASELINE.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
