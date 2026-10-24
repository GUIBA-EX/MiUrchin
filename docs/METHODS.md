# MiUrchin

Each length uses one shared locus: ordinary, A, B and D have identical forward and reverse start/end coordinates. At each locus, ordinary single, ordinary A/B union and degenerate single are selected by coverage plus exact matching; their scores are averaged equally to select the locus. Background gates: MiLily SD/MD ≤20; MiUrchin XLD ≤50; other portfolios ≤5. All concrete variants pass terminal rules and both thermodynamic scenarios. A/B results are separate-PCR unions, not experimentally validated multiplex results. References are reused for design and evaluation; coverage is computational, not measured PCR efficiency.

Reference coordinates: NC_001453.1; 1-based, extracted ungapped 16S.

Terminal: no terminal homotriplet; ≥1 GC in last 3; 1–4 GC in last 5; no homopolymer >4. Primer3: 50 mM monovalent, 1.5 mM Mg, 0.6 mM dNTP; 50 nM per variant and 200 nM per direction. Structure Tm <55°C; F/R midpoint difference ≤5°C. Coverage: ≤2 mismatches per primer and IUPAC-compatible final 3 bases; exact: zero mismatches in both.


Retain one D portfolio per length at the existing shared ordinary/A/B/D coordinates; ordinary single pairs remain unchanged; A/B have since been re-selected. Among candidates that do not reduce either coverage or exact matching relative to the original D, prefer lower degeneracy near the best combined score, rather than maximizing matching at any complexity.

Retained F/R degeneracies: S 54/48, M 8/96, L 1/16, XL 8/24. S trades some exact matching for lower degeneracy and higher coverage than the 108/96 option; M and L avoid more complex options adding only about two percentage points of exact matching.

Candidates use observed base support ≥1%, fixed random seed 17, per-direction degeneracy caps 8/16/32/64/128, and at most 30 top oligos per direction plus the original D. At 200 nM per direction, each concrete variant receives 200/degeneracy nM. Matching uses the design panel, not an independent validation set.

Current A/B selection / 当前A/B筛选：[expanded same-coordinate search and independent verification / 扩大同坐标搜索与独立复核](AB_COMPLEMENTARITY.md).
