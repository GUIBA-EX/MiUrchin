# MiUrchin

[English](README.md) · [方法](docs/METHODS.zh-CN.md) · [复现](docs/REPRODUCIBILITY.md)

海胆线粒体16S引物：参考MiFish的逐位点共识设计，在四个长度窗口搜索普通引物，并精简为单对与两对独立PCR方案。

长度依次为S、M、L、XL；单对直接使用长度名称，两对的具体配对加A、B，例如SA、SB，合用结果记为SA+SB。全部序列按5′→3′书写。

## 方案比较

共同面板为49个分类名称标签、80个标签内单倍型，采用标签等权及标签内单倍型等权。背景为6,045条记录。

| Scheme | Pairs | Coverage | Exact | Product bp | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| S | 1 | 40.82% | 20.41% | 188–191 | 0 | 3 | 4 |
| SA+SB | 2 | 61.22% | 20.41% | 188–193 | 0 | 3 | 7 |
| M | 1 | 36.73% | 6.12% | 236–244 | 0 | 1 | 12 |
| MA+MB | 2 | 46.94% | 8.16% | 224–244 | 1 | 1 | 32 |
| L | 1 | 75.51% | 19.39% | 337–362 | 2 | 1 | 161 |
| LA+LB | 2 | 87.76% | 19.39% | 337–362 | 2 | 1 | 162 |
| XL | 1 | 85.71% | 6.12% | 442–456 | 2 | 1 | 10 |
| XLA+XLB | 2 | 100.00% | 26.53% | 434–457 | 0 | 2 | 9 |

覆盖允许每条引物最多2处错配，但3′末端3 nt必须完全匹配；完全匹配要求正反引物均0错配。GT为G–T容忍敏感性模型，单独统计，不算严格完全匹配。背景数字为accession数，非实验扩增比例。

**选择建议：**需要较高覆盖时优先比较L和XL；短片段S、M的普通引物覆盖有限。四档两对方案相较原6对基线的共同覆盖分别为61.22% vs 87.76%、46.94% vs 95.92%、87.76% vs 97.96%、100% vs 100%。精简并不等于整体性能提高。L在WC≤4下仍有161–162条背景命中。

独立全序列复核的1,920项逐参考比较全部一致，12条配对记录通过热力学门槛。[验证记录](results/compact/independent_validation.json) · [热力学](results/compact/thermal.csv)

## 序列与证据

[Primer pairs](results/compact/primer_pairs.csv) · [FASTA](results/compact/primers.fasta) · [Comparison](results/compact/comparison.csv) · [Missed references](results/compact/missed_references.csv) · [Verification](results/compact/verification.json)

## 碱基匹配图

显示实际碱基而非命中热图。蓝色表示相同、橙色表示错配、紫色表示可能的G–T配对，方框标明3′末端3 nt。引物及同向参考按5′→3′展示；反向引物对应参考已反向互补。静态图展示A/B方案及每目加权频率最高的结合序列；完整页面包含单对方案和目内所有不同结合序列。

![S base matching](figures/base_matching_S.svg)

![M base matching](figures/base_matching_M.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[Full base alignment](results/compact/base_matching.html)

## 适用范围

本轮优化共同面板，结果来自冻结参考库的计算筛选与全序列复核，尚无湿实验验证。区域面板的分类群组成不同，不能将共同面板结果视为全部海胆的覆盖。两对方案为独立PCR结果并集，尚未验证同管混合体系。

[Baseline analysis](docs/BASELINE.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
