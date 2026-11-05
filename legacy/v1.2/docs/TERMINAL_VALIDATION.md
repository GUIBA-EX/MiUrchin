# Historical terminal-design snapshot / 原始末端设计快照

当前方案及验证见[VALIDATION](VALIDATION.md)和[D optimization](D_OPTIMIZATION.md)。下文保留原始阶段的数值，不用于当前主指标。/ The following records the original terminal-design stage, not current primary metrics.

# Terminal correction / 末端修正

## Material Passport

Verification status: VERIFIED for the frozen computational panel; wet-lab validation pending. / 冻结面板计算复核通过，实验验证待完成。

Scope: candidate redesign, full-sequence verification and coordinate correction. No hypothesis tests or population-wide confidence intervals are inferred from this optimization panel. / 范围为候选修正、全序列复核与坐标校正，不从优化面板推断总体置信区间或假设检验结论。

## Results / 结果

| Scheme | Previous coverage / exact | Current coverage / exact |
|---|---:|---:|
| S | 40.82% / 20.41% | 26.53% / 4.08% |
| SD | 65.31% / 38.78% | 67.35% / 20.41% |
| SD+SB | 79.59% / 38.78% | 77.55% / 20.41% |
| M | 59.18% / 16.33% | 69.39% / 16.33% |
| MD | 87.76% / 48.98% | 87.76% / 48.98% |
| MD+MB | 93.88% / 55.10% | 91.84% / 55.10% |
| L | 75.51% / 19.39% | 75.51% / 19.39% |
| XL | 85.71% / 6.12% | 81.63% / 18.37% |

All 28 current oligos pass terminal filters across their concrete variants. Nine of the 30 previous named oligos fail at least one new terminal/homopolymer rule. Independent target checks: 2,880; disagreements: 0. / 当前28条引物的实际变体全部通过末端规则；上一版30条命名引物中9条不满足至少一项新规则。独立目标状态检查2,880项，差异0项。

M improves or retains key metrics with fewer degenerate variants (MD F: 12→6). S pays a substantial exact-match cost after long-poly-T variants are excluded; ordinary S is not the preferred broad-coverage option. / MD正向简并度从12降至6，M主要指标改善或保留；S排除长串T变体后完全匹配率明显下降，普通S不作为广覆盖首选。

A provisional 91.84%-coverage MD single pair was rejected because the F/R Tm-range midpoint difference exceeded 5°C under fixed total directional concentration. Its results are not the published MD single-pair metrics. / 一个暂定覆盖91.84%的MD单对因固定同向总浓度下Tm范围中点差超过5°C被淘汰，未作为当前MD发布。

[Terminal audit](../results/terminal_optimization/terminal_audit.csv) · [Thermodynamics](../results/terminal_optimization/thermal.csv) · [Independent checks](../results/terminal_optimization/verification.json) · [Missed references](../results/terminal_optimization/missed_references.csv) · [Coordinates](../results/current/binding_positions.csv)

The coordinate map now uses all current intervals on a shared scale. In particular, L is F 932–961 and R 1250–1274: 343 bp on NC_001453.1, replacing the old seed-window 324 bp illustration. / 当前位置图按共同线性坐标绘制全部入选区间；L为F 932–961、R 1250–1274，参考跨度343 bp，已替换旧设计窗口324 bp的图示。

[Methods / 方法](METHODS.md) · [中文方法](METHODS.zh-CN.md) · [Reproduction / 复现](REPRODUCIBILITY.md)

Fresh source-bundle reproduction recovered identical selected sequences, metrics, thermodynamics and coordinate tables. All 36 paired-row/background-model accession-set comparisons also agree. / 从新解压源码包复现得到相同序列、指标、热力学结果及坐标表；36项配对记录/背景模型的accession集合复核也全部一致。
