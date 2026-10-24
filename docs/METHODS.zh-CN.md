# MiUrchin

每个长度联合选择一个共同位点：普通、A、B、D的正反向起止坐标完全相同。位点内按覆盖率与完全匹配率之和选择普通单对、普通A/B并集和简并单对，三类评分等权平均选择位点。背景门槛为WC≤3及GT≤2各不超过5条记录。所有实际序列变体通过末端规则和两种浓度热力学检查。A/B指标为独立PCR并集，未验证混池；设计与评估共用参考数据，计算覆盖率不代表实测扩增效率。

Reference coordinates: NC_001453.1; 1-based, extracted ungapped 16S.

Terminal: no terminal homotriplet; ≥1 GC in last 3; 1–4 GC in last 5; no homopolymer >4. Primer3: 50 mM monovalent, 1.5 mM Mg, 0.6 mM dNTP; 50 nM per variant and 200 nM per direction. Structure Tm <55°C; F/R midpoint difference ≤5°C. Coverage: ≤2 mismatches per primer and IUPAC-compatible final 3 bases; exact: zero mismatches in both.
