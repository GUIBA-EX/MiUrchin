# Methods / 方法

Reference: NC_001453.1, extracted ungapped mitochondrial 16S rRNA, 1-based coordinates. Each S–XL window has fixed ordinary/A/B/D endpoints; 188/228/343/440 bp reference spans include primers. Products vary among taxa.

参考坐标为NC_001453.1提取的无gap 16S序列，1-based；各长度普通/A/B/D坐标一致。参考跨度包含引物，实际产物长度随类群变化。

The target library has 1,401 records, the common panel 80 references/49 species labels, and the background 6,045 records. Primary coverage and exact scores equally average within-order label detection over 11 WoRMS orders. Any matching reference detects a label; partial/full within-label states are reported separately. Legacy reference-weighted metrics remain secondary.

主覆盖率与完全匹配率先按目内检出标签比例计算，再对11个目等权；标签有任一参考命中即检出，种内完整/部分匹配另列。旧参考加权指标作次要比较。

Coverage: ≤2 mismatches per primer plus IUPAC-compatible final 3 nt. Exact: zero mismatches at both ends. Paired target scans require total 150–500 bp and internal ≥50 bp. Background internal distance is 0–1,000 bp on both strands. Broad WC3/GT2 omit the terminal constraint; strict WC/GT retain it. Counts are records, not PCR fractions.

每条具体变体：无末端三连、末端3 nt至少一个GC、末端5 nt含1–4个GC、无超过4 nt的同聚物；允许3′简并。Primer3 uses 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP, 50 nM per variant and 200 nM per direction. All intra-/inter-variant structures require Tm<55°C and F/R duplex-Tm midpoint difference ≤5°C. At fixed total concentration, each variant receives 200/degeneracy nM.

Current D: order-balanced search of 10,394 pairs, per-direction degeneracy≤128, strict background≤20 and broad background≤100 records each. Exact matching cannot decrease at order or label level; label coverage can fall at most four percentage points. Ordinary/A/B retain their original sequences and ≤5 broad WC3/GT2 gates. A/B represent separate-PCR unions with mutual contributions.

当前D搜索、分类来源、筛选取舍、浓度代价和类群增减详见[D optimization](D_OPTIMIZATION.md)。A/B的原有互补性证据见[AB_COMPLEMENTARITY](AB_COMPLEMENTARITY.md)。独立算法复核同一参考库，不构成独立生物样本验证。
