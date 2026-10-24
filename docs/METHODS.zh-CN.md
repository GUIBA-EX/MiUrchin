# MiUrchin

每个长度联合选择一个共同位点：普通、A、B、D的正反向起止坐标完全相同。位点内按覆盖率与完全匹配率之和选择普通单对、普通A/B并集和简并单对，三类评分等权平均选择位点。背景门槛：MiLily SD/MD为20条，MiUrchin XLD为50条，其余5条。所有实际序列变体通过末端规则和两种浓度热力学检查。A/B指标为独立PCR并集，未验证混池；设计与评估共用参考数据，计算覆盖率不代表实测扩增效率。

Reference coordinates: NC_001453.1; 1-based, extracted ungapped 16S.

Terminal: no terminal homotriplet; ≥1 GC in last 3; 1–4 GC in last 5; no homopolymer >4. Primer3: 50 mM monovalent, 1.5 mM Mg, 0.6 mM dNTP; 50 nM per variant and 200 nM per direction. Structure Tm <55°C; F/R midpoint difference ≤5°C. Coverage: ≤2 mismatches per primer and IUPAC-compatible final 3 bases; exact: zero mismatches in both.


每个长度只保留一套D方案，固定普通/A/B/D共同坐标，普通与A/B不变。扩大简并候选后，在覆盖与完全匹配不低于原D的方案中，优先选取接近最佳评分但简并度更低的候选；收益不足以抵偿复杂度时不追求最高评分。

S采用54/48，M采用8/96，L采用1/16，XL采用8/24。S舍弃108/96档，以较低简并度和较高覆盖率换取较低完全匹配率；M、L舍弃完全匹配率仅多约2个百分点的更复杂档。

Candidates use observed base support ≥1%, fixed random seed 17, per-direction degeneracy caps 8/16/32/64/128, and at most 30 top oligos per direction plus the original D. At 200 nM per direction, each concrete variant receives 200/degeneracy nM. Matching uses the design panel, not an independent validation set.
