# Retention decisions / 保留决策

每个长度只保留一套D方案，固定普通/A/B/D共同坐标，普通单对不变，A/B已重新选配。扩大简并候选后，在覆盖与完全匹配不低于原D的方案中，优先选取接近最佳评分但简并度更低的候选；收益不足以抵偿复杂度时不追求最高评分。

Retain one D portfolio per length at the existing shared ordinary/A/B/D coordinates; ordinary single pairs remain unchanged; A/B have since been re-selected. Among candidates that do not reduce either coverage or exact matching relative to the original D, prefer lower degeneracy near the best combined score, rather than maximizing matching at any complexity.

S采用54/48，M采用8/96，L采用1/16，XL采用8/24。S舍弃108/96档，以较低简并度和较高覆盖率换取较低完全匹配率；M、L舍弃完全匹配率仅多约2个百分点的更复杂档。

Retained F/R degeneracies: S 54/48, M 8/96, L 1/16, XL 8/24. S trades some exact matching for lower degeneracy and higher coverage than the 108/96 option; M and L avoid more complex options adding only about two percentage points of exact matching.

| D | F/R degeneracy | Coverage before → after % | Exact before → after % | WC≤3 | GT≤2 | WC≤4 |
|---|---|---|---|---:|---:|---:|
| SD | 54/48 | 63.27 → 73.47 | 16.33 → 22.45 | 3 | 0 | 22 |
| MD | 8/96 | 87.76 → 87.76 | 48.98 → 67.35 | 0 | 0 | 0 |
| LD | 1/16 | 87.76 → 93.88 | 34.69 → 36.73 | 2 | 1 | 228 |
| XLD | 8/24 | 85.71 → 100.00 | 6.12 → 57.14 | 16 | 26 | 47 |

This is a post-search benefit–complexity judgment, not a preregistered optimum. The near-best screen uses coverage+exact within five percentage points of the thermally feasible maximum; MiUrchin S additionally caps each direction at 64 variants. / 这是搜索后的收益与复杂度取舍，并非预注册最优阈值。

Current A/B selection / 当前A/B筛选：[expanded same-coordinate search and independent verification / 扩大同坐标搜索与独立复核](AB_COMPLEMENTARITY.md).
