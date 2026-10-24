![MiUrchin overview](figures/MiUrchin_overview.png)

![Current binding positions](figures/binding_positions.svg)

Badge spans are 188, 228, 343 and 440 bp for SD, MD, L and XL on the reference. The map uses one linear scale for all current pairs. Coordinates are 1-based on extracted, ungapped NC_001453.1 16S; product lengths vary among taxa.

# MiUrchin

[中文](README.zh-CN.md) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md)

Mitochondrial 16S primers for sea urchins. Four length windows retain one-pair and two-pair separate-PCR options, with ordinary, degenerate and complementary mixed options for S and M.

Lengths are S, M, L and XL. A single pair uses the region name; the two-pair components use A and B, for example SA and SB, with union metrics labelled SA+SB. All sequences are 5′→3′.

D identifies a degenerate pair. SD+SB and MD+MB reuse one degenerate pair and one ordinary supplement. There are 12 portfolios and 18 paired entries, with 14 pair names / 28 FASTA records.

## Portfolio comparison

The common panel contains 49 taxonomic name labels and 80 within-label haplotypes, weighted equally by label and then by haplotype within label. The background contains 6,045 records.

| Scheme | Type | Pairs | Coverage | Exact | WC≤3 | GT≤2 | WC≤4 |
|---|---|---:|---:|---:|---:|---:|---:|
| S | ordinary | 1 | 26.53% | 4.08% | 0 | 0 | 1 |
| SA+SB | ordinary | 2 | 42.86% | 4.08% | 0 | 3 | 7 |
| SD | degenerate | 1 | 67.35% | 20.41% | 3 | 0 | 18 |
| SD+SB | mixed | 2 | 77.55% | 20.41% | 3 | 3 | 19 |
| M | ordinary | 1 | 69.39% | 16.33% | 0 | 0 | 0 |
| MA+MB | ordinary | 2 | 77.55% | 22.45% | 0 | 1 | 12 |
| MD | degenerate | 1 | 87.76% | 48.98% | 0 | 1 | 0 |
| MD+MB | mixed | 2 | 91.84% | 55.10% | 0 | 2 | 12 |
| L | ordinary | 1 | 75.51% | 19.39% | 2 | 1 | 161 |
| LA+LB | ordinary | 2 | 87.76% | 19.39% | 2 | 1 | 162 |
| XL | ordinary | 1 | 81.63% | 18.37% | 3 | 5 | 11 |
| XLA+XLB | ordinary | 2 | 97.96% | 26.53% | 0 | 3 | 5 |

Coverage permits up to two mismatches per primer with the terminal three bases exactly matched; exact matching requires zero mismatches in both primers. GT is a separate G–T tolerance sensitivity model, not strict exact matching. Background values count accessions, not experimental amplification fractions.

**Prioritize MD, adding MB when needed.** MD gives 87.76% coverage / 48.98% exact matching, with F/R degeneracy 6/24; MD+MB gives 91.84% / 55.10%. Ordinary M gives 69.39% / 16.33%, and MA+MB gives 77.55% / 22.45%.

S retains a substantial trade-off: SD gives 67.35% / 20.41%, and SD+SB gives 77.55% / 20.41%; ordinary S coverage remains low. SD F/R degeneracy is 12/12. The terminal correction reduces S exact matching and is not an across-the-board improvement.

Every concrete variant excludes terminal homotriplets, has at least one G/C in the last three bases and 1–4 G/C in the last five, and has no homopolymer longer than four bases. A terminal G/C is not mandatory. Structure Tm and F/R Tm-range midpoint differences pass both concentration scenarios. See [terminal correction and verification](docs/TERMINAL_VALIDATION.md).

## Sequences and evidence

[Primer pairs](results/current/primer_pairs.csv) · [FASTA](results/current/primers.fasta) · [Comparison](results/current/comparison.csv) · [Binding coordinates](results/current/binding_positions.csv) · [Missed references](results/terminal_optimization/missed_references.csv) · [Terminal audit](results/terminal_optimization/terminal_audit.csv) · [Verification](results/terminal_optimization/verification.json)

## Base matching

Actual bases are shown: blue = IUPAC-compatible, orange = mismatch, purple = possible G–T pairing; boxes mark the terminal three bases. Primers and same-sense references are 5′→3′; reverse-reference sites are reverse-complemented. Static figures show two-pair options and the most frequent weighted binding sequence in each order. The complete page includes single-pair options and all distinct binding sequences within each order.

![S base matching](figures/base_matching_S.svg)

![SD base matching](figures/base_matching_SD.svg)

![M base matching](figures/base_matching_M.svg)

![MD base matching](figures/base_matching_MD.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[Full base alignment](results/terminal_optimization/base_matching.html)

## Evaluation scope

This round optimizes the common panel using frozen references and full-sequence revalidation. Wet-lab validation is pending. Region panels differ in taxonomic composition; common-panel performance is not class-wide coverage. Two-pair metrics represent separate PCR unions, not a validated multiplex mixture.

[Baseline analysis](docs/BASELINE.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
