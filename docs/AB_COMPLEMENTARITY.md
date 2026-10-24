# A/B complementarity / A/B互补性

A/B should contribute complementary target matches at identical binding coordinates. Preserve combined coverage and exact matching, then prefer balanced unique contributions from both components. Coverage and exact matching are assessed separately: one component may improve coverage while the other improves exact matching. / A/B应在相同起止坐标下各有独有贡献，保留并集覆盖与完全匹配后优先双方贡献更均衡的组合；覆盖互补和完全匹配互补分别评估。

| Region | A-only coverage | B-only coverage | A-only exact | B-only exact |
|---|---:|---:|---:|---:|
| S | 0.00% | 2.04% | 0.00% | 4.08% |
| M | 0.00% | 0.00% | 14.29% | 16.33% |
| L | 6.12% | 0.00% | 19.39% | 14.29% |
| XL | 12.24% | 10.20% | 18.37% | 6.12% |

Unique contributions are weighted reference-sequence fractions, not counts of new species. / 独有贡献为加权参考序列比例，不是新增物种数。

Re-screening the existing feasible ordinary candidate pool at the frozen coordinates found no replacement improving balanced unique contributions without reducing either union coverage or union exact matching. This is bounded to the existing candidate pool; sequences remain unchanged. / 当前坐标及候选池内复筛未找到兼顾既有并集指标且互补贡献更好的替代，序列未改动；不代表扩大搜索后不存在更优方案。

**S A/B is redundant relative to its stronger component on both evaluated metrics; retain as a comparator, not a recommended complementary enhancement. / S双对对两个指标均无增益，仅作比较，不作为互补增强推荐。**
