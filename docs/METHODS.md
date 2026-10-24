# MiUrchin

Each length uses one shared locus: ordinary, A, B and D have identical forward and reverse start/end coordinates. At each locus, ordinary single, ordinary A/B union and degenerate single are selected by coverage plus exact matching; their scores are averaged equally to select the locus. Background limits are WC≤3 ≤5 and GT≤2 ≤5 accessions. All concrete variants pass terminal rules and both thermodynamic scenarios. A/B results are separate-PCR unions, not experimentally validated multiplex results. References are reused for design and evaluation; coverage is computational, not measured PCR efficiency.

Reference coordinates: NC_001453.1; 1-based, extracted ungapped 16S.

Terminal: no terminal homotriplet; ≥1 GC in last 3; 1–4 GC in last 5; no homopolymer >4. Primer3: 50 mM monovalent, 1.5 mM Mg, 0.6 mM dNTP; 50 nM per variant and 200 nM per direction. Structure Tm <55°C; F/R midpoint difference ≤5°C. Coverage: ≤2 mismatches per primer and IUPAC-compatible final 3 bases; exact: zero mismatches in both.
