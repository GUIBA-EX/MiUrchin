# Methods

[中文](METHODS.zh-CN.md)

Using extracted 16S NC_001453.1 coordinates, search 20–30 nt primers within ±15 nt of four seed starts. Generate WC and G–T-compatible consensus sequences from common-panel base frequencies, adding the three most frequent observed binding sequences per window. Filter to 35–65% GC and exclude six-base homopolymers. Target terminal three bases must match exactly.

Primer3: 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP and 200 nM per oligo. Hairpin, homodimer and pair heterodimer Tm must be below 55°C; F/R Tm difference ≤5°C.

Background scans cover both strands, correct orientation and 0–1,000 nt internal distance. Each portfolio permits ≤5 WC≤3 and ≤5 GT≤2 accessions. Maximize common-panel coverage, then exact matching. Enumerate feasible single and two-pair states, collapsing identical target/background states.

Independently rescan complete paired products: target length 150–500 bp with ≥50 nt internal sequence, and background as above. The bounded search does not establish a genome-wide optimum. Frozen references and baseline evidence remain under analysis/.

[Miya et al. 2015](https://doi.org/10.1098/rsos.150088)


## S/M refinement / S与M补充优化

The S/M round adds previously designed ordinary and degenerate same-locus candidates to the shifted-window pool. Alignment gaps are removed before scanning actual sequence in the seed neighbourhood (±5 nt); the complete paired-product scanner supplies final metrics. Candidates from both existing pools are compared on the same 49-label / 80-haplotype panel. Retain the previous ordinary option’s coverage and exact matching as lower bounds, then maximize coverage, exact matching and parsimony in that order.

S/M补充轮将既有普通与简并同位点候选加入平移窗口候选池。先去除比对缺口，再在种子邻域±5 nt扫描真实序列，最终指标取完整配对产物扫描。共同面板保持49个名称标签、80个单倍型。筛选不低于上一版同对数普通方案的覆盖与完全匹配，随后依次优化覆盖、完全匹配与简并度。

Degenerate thermodynamics expand all variants. Evaluate 50 nM per concrete variant and 200 nM total per direction divided among variants, including hairpins, homodimers, within-direction heterodimers and F/R interactions. Unequal-concentration heterodimers use the larger concentration as an approximation. The structural Tm ceiling remains 55°C. Background limits remain WC≤3 ≤5 and GT≤2 ≤5 per portfolio.

简并热力学展开全部变体：每变体50 nM及每方向总量200 nM分摊两种情景，检查发卡、同源二聚体、同向异源二聚体及F/R相互作用。浓度不等时，二聚体使用较大浓度近似。结构Tm门槛仍为55°C，组合背景门槛仍为WC≤3与GT≤2各≤5条。
