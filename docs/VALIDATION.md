# Validation / 验证

Current primer sequences, fixed coordinates, degeneracy, independent target/background scans and documentation links are checked with `python3 scripts/check_species_release.py`. Per-candidate results and hit sets are provided under `results/current_primers/`.

当前引物的序列、固定坐标、简并度、独立扫描结果和文档链接使用上述脚本检查；逐引物结果和命中集合见 `results/current_primers/`。

For XSD, `python3 scripts/check_xsd_raw.py` independently rescans the released target and background sequences and compares exact and terminal-constrained hit sets to the C++ results. The XSD base diagram displays fixed homologous alignment columns; its hit labels use the full-sequence scan.

XSD 可用上述脚本独立扫描项目中的原始目标和非目标序列，核对完全匹配及末端约束命中。碱基图显示固定参考同源列，命中标记来自全序列扫描。
