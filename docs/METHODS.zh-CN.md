# 方法

[English](METHODS.md)

以NC_001453.1的16S为坐标参考，在四个窗口起点±15 nt内搜索20–30 nt引物。按共同面板碱基频率构造WC及G–T相容共识，并加入每窗口最常见的3条真实结合序列；过滤GC 35–65%及连续6个相同碱基。目标3′末端3 nt必须完全匹配。

Primer3条件：单价盐50 mM、Mg²⁺ 1.5 mM、dNTP 0.6 mM、每条引物200 nM。单引物发卡/同源二聚体及配对异源二聚体Tm<55°C，正反Tm差≤5°C。

背景全序列双链扫描要求正确方向及0–1,000 nt内部距离。筛选每套组合WC≤3及GT≤2各≤5条记录。优先最大化共同面板覆盖，再最大化完全匹配；穷举通过约束的单对和两对，并合并相同命中状态以减少重复计算。

最后使用独立完整配对扫描复核目标产物（150–500 bp、内部≥50 nt）及背景。搜索范围有限，不代表全基因组全局最优。原始完整参考、旧分析及复核证据保留在analysis/。

[Miya et al. 2015](https://doi.org/10.1098/rsos.150088)


## S/M refinement / S与M补充优化

The S/M round adds previously designed ordinary and degenerate same-locus candidates to the shifted-window pool. Alignment gaps are removed before scanning actual sequence in the seed neighbourhood (±5 nt); the complete paired-product scanner supplies final metrics. Candidates from both existing pools are compared on the same 49-label / 80-haplotype panel. Retain the previous ordinary option’s coverage and exact matching as lower bounds, then maximize coverage, exact matching and parsimony in that order.

S/M补充轮将既有普通与简并同位点候选加入平移窗口候选池。先去除比对缺口，再在种子邻域±5 nt扫描真实序列，最终指标取完整配对产物扫描。共同面板保持49个名称标签、80个单倍型。筛选不低于上一版同对数普通方案的覆盖与完全匹配，随后依次优化覆盖、完全匹配与简并度。

Degenerate thermodynamics expand all variants. Evaluate 50 nM per concrete variant and 200 nM total per direction divided among variants, including hairpins, homodimers, within-direction heterodimers and F/R interactions. Unequal-concentration heterodimers use the larger concentration as an approximation. The structural Tm ceiling remains 55°C. Background limits remain WC≤3 ≤5 and GT≤2 ≤5 per portfolio.

简并热力学展开全部变体：每变体50 nM及每方向总量200 nM分摊两种情景，检查发卡、同源二聚体、同向异源二聚体及F/R相互作用。浓度不等时，二聚体使用较大浓度近似。结构Tm门槛仍为55°C，组合背景门槛仍为WC≤3与GT≤2各≤5条。
