# A/B complementarity / A/B互补性

Expanded fixed-coordinate search has been applied to the released sequences. Ordinary single pairs remain unchanged; D has subsequently been optimized under [equal-order scoring](D_OPTIMIZATION.md). All four A/B combinations have contributions from both components, with neither union coverage nor union exact matching below the preceding selection. / 扩大同坐标搜索已落实到正式序列；普通单对不变，D已按[目间等权](D_OPTIMIZATION.md)另行优化。四个长度的A/B均有双方独有贡献，并集覆盖与完全匹配均不低于此前方案。

Changed pairs / 序列更新：SA, XLA, XLB.

| Region | A-only coverage | B-only coverage | A-only exact | B-only exact | Union coverage | Union exact |
|---|---:|---:|---:|---:|---:|---:|
| S | 15.31% | 26.53% | 2.04% | 4.08% | 41.84% | 6.12% |
| M | 0.00% | 0.00% | 14.29% | 16.33% | 59.18% | 30.61% |
| L | 6.12% | 0.00% | 19.39% | 14.29% | 75.51% | 33.67% |
| XL | 10.20% | 12.24% | 6.12% | 18.37% | 91.84% | 24.49% |

Unique contributions are weighted reference-sequence fractions, not new-species counts. Coverage and exact matching are distinct benefits; a component may add one without adding the other. A/B denotes separate-PCR unions. These are complementary options, not a requirement to use two pairs when a single or D meets the sampling objective. / 独有贡献为加权参考序列比例，不是新增物种数；覆盖与完全匹配分别评价。A/B表示独立PCR并集；有互补收益也不意味着所有样本都需要双对，单对或D满足需求时优先精简。

Search includes observed binding haplotypes, concrete variants of retained primers, and supported one- and two-position substitutions around a weighted consensus. Candidates pass terminal and thermodynamic checks. Each ordinary A/B union has ≤5 background accessions under both WC≤3 and GT≤2. Selection first requires non-decreasing union coverage and exact matching plus unique contributions from both components, then maximizes their sum and balances the contributions. Independent full-sequence scanning confirms target states and background accession sets. / 搜索纳入观测结合单倍型、现有引物实际变体和加权共识的受支持单、双位点替换。候选通过末端及热力学检查，普通A/B并集在WC≤3及GT≤2下各不超过5条背景记录。先要求两项并集指标不降且双方均有独有贡献，再提高总评分并平衡贡献；独立全序列扫描复核目标状态及背景集合。

[Search / 搜索](../results/ab_complementarity/reselection.csv) · [Metrics / 指标](../results/ab_complementarity/summary.csv) · [Unique references / 独有参考](../results/ab_complementarity/unique_reference_hits.csv)

## Previous → current / 前后比较

| Region | Coverage % | Exact % |
|---|---:|---:|
| S | 26.53 → 41.84 | 4.08 → 6.12 |
| M | 59.18 → 59.18 | 30.61 → 30.61 |
| L | 75.51 → 75.51 | 33.67 → 33.67 |
| XL | 91.84 → 91.84 | 24.49 → 24.49 |
