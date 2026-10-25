# Validation / 验证

Current release: 12 portfolios, 16 pairs, 32 oligos; four fixed windows. Current D pairs and their baselines agree on 1,280 target decisions, 32 strict/exact background sets and 40 background counts across independent C++/Python scans. Ordinary/A/B sequences remain unchanged; their raw-hit and complementarity evidence is retained.

当前发布12套方案、16对、32条序列；新旧D的独立扫描差异0，普通/A/B未变。所有具体变体通过末端与热力学门槛，每长度普通/A/B/D坐标一致。完整计算检查及独立目录复现均在发布前执行。

- [D verification](../results/D_optimization/verification.json)
- [Current combined evidence](../results/terminal_optimization/verification.json)
- [Thermodynamics](../results/terminal_optimization/thermal.csv)
- [Order metrics](../results/current/taxonomic_comparison.csv)
- [A/B complementarity](AB_COMPLEMENTARITY.md)

Historical compact/terminal design snapshots are separate from current evidence. Computational matching is not measured amplification efficiency.
