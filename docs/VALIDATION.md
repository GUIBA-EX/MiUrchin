# Validation / 验证

Current exports contain 12 portfolios, 18 paired entries and 15 unique pair names (30 FASTA records). S/M were independently rescanned: all 1,920 per-reference comparisons agree, including ordinary, degenerate and complementary mixed options. L/XL retain their previously validated sequences and metrics.

当前导出12套方案、18条配对记录、15个唯一配对名（30条FASTA记录）。S/M普通、简并及互补组合重新独立扫描，1,920项逐参考比较全部一致；L/XL沿用此前通过验证的序列及指标。

- [S/M validation](../results/sm_optimization/verification.json)
- [S/M thermodynamics](../results/sm_optimization/thermal.csv)
- [S/M raw hits](../results/sm_optimization/independent_hits.tsv)
- [L/XL and previous compact validation](../results/compact/independent_validation.json)

Run `python scripts/check_current.py` to recompute current coverage, exact matching and background counts. 该检查器从原始命中记录重算当前覆盖、完全匹配及背景命中。

Independent implementation agreement is computational verification; references are shared between design and evaluation. No wet-lab validation is claimed. 独立实现一致性属于计算验证，设计与评估复用参考，尚无湿实验验证。
