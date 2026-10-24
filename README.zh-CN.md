![MiUrchin 项目介绍](figures/MiUrchin_overview.png)

![当前引物结合位置](figures/binding_positions.svg)

图中徽标为SD、MD、L、XL在参考序列上的跨度，分别为188、228、343、440 bp；下图按同一线性比例展示所有当前配对。坐标为NC_001453.1提取的16S序列位置（1起始、去缺口），实际产物长度随类群变化。

# MiUrchin

[English](README.md) · [方法](docs/METHODS.zh-CN.md) · [复现](docs/REPRODUCIBILITY.md)

海胆线粒体16S引物：四个长度窗口保留单对与两对独立PCR方案，S和M同时比较普通、简并及互补组合。

长度依次为S、M、L、XL；单对直接使用长度名称，两对的具体配对加A、B，例如SA、SB，合用结果记为SA+SB。全部序列按5′→3′书写。

D表示简并单对；SD+SB、MD+MB分别复用简并单对与一对普通补充引物。当前12套方案、18条配对记录，包含14个配对名、28条FASTA序列。

## 方案比较

共同面板为49个分类名称标签、80个标签内单倍型，采用标签等权及标签内单倍型等权。背景为6,045条记录。

| 方案 | 类型 | 对数 | 覆盖率 | 完全匹配率 | WC≤3 | GT≤2 | WC≤4 |
|---|---|---:|---:|---:|---:|---:|---:|
| S | 普通 | 1 | 26.53% | 4.08% | 0 | 0 | 1 |
| SA+SB | 普通 | 2 | 42.86% | 4.08% | 0 | 3 | 7 |
| SD | 简并 | 1 | 67.35% | 20.41% | 3 | 0 | 18 |
| SD+SB | 简并＋普通 | 2 | 77.55% | 20.41% | 3 | 3 | 19 |
| M | 普通 | 1 | 69.39% | 16.33% | 0 | 0 | 0 |
| MA+MB | 普通 | 2 | 77.55% | 22.45% | 0 | 1 | 12 |
| MD | 简并 | 1 | 87.76% | 48.98% | 0 | 1 | 0 |
| MD+MB | 简并＋普通 | 2 | 91.84% | 55.10% | 0 | 2 | 12 |
| L | 普通 | 1 | 75.51% | 19.39% | 2 | 1 | 161 |
| LA+LB | 普通 | 2 | 87.76% | 19.39% | 2 | 1 | 162 |
| XL | 普通 | 1 | 81.63% | 18.37% | 3 | 5 | 11 |
| XLA+XLB | 普通 | 2 | 97.96% | 26.53% | 0 | 3 | 5 |

覆盖允许每条引物最多2处错配，但3′末端3 nt必须完全匹配；完全匹配要求正反引物均0错配。GT为G–T容忍敏感性模型，单独统计，不算严格完全匹配。背景数字为accession数，非实验扩增比例。

**优先验证MD单对，必要时补充MB。** MD覆盖87.76%、完全匹配48.98%，F/R简并度为6/24；MD+MB为91.84%/55.10%。普通M单对为69.39%/16.33%，MA+MB为77.55%/22.45%。

S仍有明显取舍：SD为67.35%/20.41%，SD+SB为77.55%/20.41%；普通S方案覆盖较低。SD的F/R简并度为12/12。末端修正降低了S的完全匹配率，不能将其描述为全面提升。

全部实际变体均排除3′端三连同碱基，末端3位至少含1个G/C，末端5位含1–4个G/C，全序列同碱基连续长度不超过4。末端最后一位不强制为G/C。双浓度情景的结构Tm与正反Tm范围中点差均复核通过。详见[末端修正与验证](docs/TERMINAL_VALIDATION.md)。

## 序列与证据

[引物配对](results/current/primer_pairs.csv) · [FASTA序列](results/current/primers.fasta) · [方案比较](results/current/comparison.csv) · [结合坐标](results/current/binding_positions.csv) · [漏检参考](results/terminal_optimization/missed_references.csv) · [末端审计](results/terminal_optimization/terminal_audit.csv) · [独立复核](results/terminal_optimization/verification.json)

## 碱基匹配图

显示实际碱基而非命中热图。蓝色表示IUPAC相容、橙色表示错配、紫色表示可能的G–T配对，方框标明3′末端3 nt。引物及同向参考按5′→3′展示；反向引物对应参考已反向互补。静态图展示两对方案及每目加权频率最高的结合序列；完整页面包含单对方案和目内所有不同结合序列。

![S base matching](figures/base_matching_S.svg)

![SD base matching](figures/base_matching_SD.svg)

![M base matching](figures/base_matching_M.svg)

![MD base matching](figures/base_matching_MD.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[完整碱基匹配图](results/terminal_optimization/base_matching.html)

## 适用范围

本轮优化共同面板，结果来自冻结参考库的计算筛选与全序列复核，尚无湿实验验证。区域面板的分类群组成不同，不能将共同面板结果视为全部海胆的覆盖。两对方案为独立PCR结果并集，尚未验证同管混合体系。

[Baseline analysis](docs/BASELINE.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
