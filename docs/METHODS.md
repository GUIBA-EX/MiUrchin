# Methods

## Input and alignment

Repartition the inherited MiStar/MiCucumber public accession set into Echinoidea targets (1,401) and background (6,045). Targets include 1,391 annotated and 10 title-only records. Background: Holothuroidea 1,846; Asteroidea 1,955; Ophiuroidea 1,736; Crinoidea 269; other Metazoa 239. Accessions are unique across sets. No fresh database query or synonym reconciliation was performed.

Select 86 unambiguous 1,100–2,000 nt representatives after deduplication within organism labels; identical sequences belonging to different labels are retained. MAFFT 7.526 aligns the backbone, then adds other target fragments with `--addfragments --keeplength`. The final 1,401-row alignment has 1,813 columns; all 86 backbone rows remain unchanged. The coordinate reference is extracted 16S of NC_001453.1, Strongylocentrotus purpuratus. Display coordinates are 1-based; internal intervals are 0-based half-open.

## Initial design

Explore anchors 100–1348 (0-based, step 4), oligo lengths 20–30 (step 2), IUPAC frequency thresholds 0.03/0.07/0.12/0.20/0.30, with and without terminal-three-base consensus locking. Discovery initially uses 49 named full-sequence labels. Require alignment support ≥75%, oligo target coverage ≥40%, pair coverage ≥35%, degeneracy ≤32, concrete-variant Tm 50–73°C with ≤10°C spread, hairpin Tm ≤55°C, and F/R mean-Tm difference ≤5°C. AAAA is flagged rather than automatically excluded.

The initial 1,656 oligos yield 63,613 pairs in four reference-span bins: XS 150–199, S 200–249, M 250–349, L 350–500 bp. These bins concern reference design spans; predicted product sizes in other taxa can cross those boundaries because of indels. There is no historical MiUrchin baseline in this release.

## Background and target models

Screen complete original sequences in both orientations. WC models allow up to 2, 3 or 4 mismatches per primer. GT≤2 applies the inherited MiStar G:T-tolerance transformation, then allows two other mismatches per primer; it is a sensitivity analysis, not a complete polymerase model. Background primer-free distances are 0–1,000 nt. Both primer sites must occur in a valid orientation on the same sequence. Counts are unions of accessions, including multiple accessions for identical sequences; they are not species counts or read fractions.

Binding sites containing ambiguous template bases are reported separately and excluded from confirmed hits, not treated as negative. Primary complete-scheme constraints are ≤5 WC≤3 and ≤5 GT≤2 background accessions. Wider WC≤4 risk is reported without a zero-hit claim. This analyst-selected operational threshold implements the user's preference for small residual risk, not an experimental contamination threshold.

Target coverage requires ≤2 mismatches per primer and perfect terminal three 3′ bases, product size 150–500 bp, and at least 50 nt internal sequence. Exact coverage requires both primers to match perfectly. The scanner does not allow binding-site indels; separate observed oligos can represent different physical lengths at homologous windows.

## Panels and supplementation

The frozen shared interval retains 49 binomial-format labels and 80 label-internal haplotypes. Use equal label weight and equal haplotype weight within each label. Eligibility requires both interval endpoints present, no ambiguous nucleotide in the aligned interval, and within-label deduplication after removing gaps. This defines evidence availability, not observed amplification.

A preliminary common-panel-only supplementation was expanded before release to all eligible records in each locus: XS 55 labels/70 haplotypes, S 165/446, M 165/483, L 55/77. Each locus uses its own weights. Generate observed and genus/all-panel consensus variants at the selected homologous positions, allowing observed lengths within ±4 nt of the seed and 18–36 nt overall. Degeneracy and thermal gates remain. The expanded search has 301 oligos and 5,072 complete F/R combinations.

Use limited multi-start greedy extension to at most six component pairs, at most six unique F and R oligos, and at most 8°C between oligo Tm midpoints in pools. Separate-PCR schemes evaluate explicit pair unions; pools evaluate every F×R cross pair. Choose compact solutions within 0.5 percentage points of the best discovery coverage. Local one-pair swaps (including additions up to six pairs) then improve exact coverage while retaining at least the initial selected coverage minus 0.5 percentage points and retaining complete background constraints. This is a local search, not proof of global optimality.

## Thermodynamics and independent validation

Primer3-py 2.3.1 parameters: monovalent salt 50 mM, Mg²⁺ 1.5 mM, dNTP 0.6 mM. Evaluate every concrete IUPAC variant. Scenarios: each concrete variant at 50 nM; or total 200 nM per direction split equally across ordered oligos and their variants. In pools, duplicate concrete variant concentrations are summed. Unequal-concentration dimers use the larger concentration as the single Primer3 scalar input; this is an approximate sensitivity model, not a PCR recipe.

Check hairpins, homodimers, same-direction and opposite-direction heterodimers; all published complete schemes pass the <55°C structural gate in both scenarios. This does not establish experimental competition, balanced amplification or an annealing temperature.

A Python scanner is checked against an independently implemented exhaustive C++ all-position scanner on all 1,401 targets and 6,045 background records. Final 170 selected/cross pairs pass 234,496 consistency checks on flags, product sizes and background counts. Synthetic/real-window tests pass 544 checks; a 15-pair ranking audit checks C++ aggregation against Python. Machine-readable evidence is retained in `analysis/`.

## Limitations and next validation

These are discovery-set predictions, not held-out or wet-lab validation. Sparse reference availability, historical source taxonomy, incomplete non-echinoderm background, mismatches and primer competition remain material limitations. A high percentage within a restricted panel is not class-wide universality. Use the per-order and missing-label tables to choose target and non-target positive controls. For both degraded environmental and higher-quality tissue DNA applications, compare multiple lengths experimentally rather than inferring performance from length alone. No laboratory recipe or classification accuracy is supplied.
