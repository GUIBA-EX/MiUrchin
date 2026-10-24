![MiUrchin overview](figures/MiUrchin_overview.png)

Reference seed windows on NC_001453.1: S 188 bp, M 228 bp, L 324 bp and XL 440 bp. The diagram is not to scale; optimized binding positions and product lengths vary.

# MiUrchin

[中文](README.zh-CN.md) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md)

Mitochondrial 16S primers for sea urchins. Four length windows retain one-pair and two-pair separate-PCR options, with ordinary, degenerate and complementary mixed options for S and M.

Lengths are S, M, L and XL. A single pair uses the region name; the two-pair components use A and B, for example SA and SB, with union metrics labelled SA+SB. All sequences are 5′→3′.

D identifies a degenerate pair. SD+SB and MD+MC combine a degenerate pair with an ordinary supplement; MC is the ordinary supplement selected for MD. There are 12 portfolios and 18 paired entries, with 15 unique pair names / 30 FASTA records after name reuse is deduplicated.

## Portfolio comparison

The common panel contains 49 taxonomic name labels and 80 within-label haplotypes, weighted equally by label and then by haplotype within label. The background contains 6,045 records.

| Scheme | Type | Pairs | Coverage | Exact | WC≤3 | GT≤2 | WC≤4 |
|---|---|---:|---:|---:|---:|---:|---:|
| S | ordinary | 1 | 40.82% | 20.41% | 0 | 3 | 4 |
| SA+SB | ordinary | 2 | 61.22% | 20.41% | 0 | 3 | 7 |
| SD | degenerate | 1 | 65.31% | 38.78% | 0 | 0 | 8 |
| SD+SB | mixed | 2 | 79.59% | 38.78% | 0 | 3 | 10 |
| M | ordinary | 1 | 59.18% | 16.33% | 0 | 0 | 0 |
| MA+MB | ordinary | 2 | 77.55% | 16.33% | 1 | 1 | 30 |
| MD | degenerate | 1 | 87.76% | 48.98% | 0 | 1 | 0 |
| MD+MC | mixed | 2 | 93.88% | 55.10% | 0 | 1 | 17 |
| L | ordinary | 1 | 75.51% | 19.39% | 2 | 1 | 161 |
| LA+LB | ordinary | 2 | 87.76% | 19.39% | 2 | 1 | 162 |
| XL | ordinary | 1 | 85.71% | 6.12% | 2 | 1 | 10 |
| XLA+XLB | ordinary | 2 | 100.00% | 26.53% | 0 | 2 | 9 |

Coverage permits up to two mismatches per primer with the terminal three bases exactly matched; exact matching requires zero mismatches in both primers. GT is a separate G–T tolerance sensitivity model, not strict exact matching. Background values count accessions, not experimental amplification fractions.

**Prioritize SD and MD single-pair comparisons.** SD reaches 65.31% coverage and 38.78% exact matching; MD reaches 87.76% and 48.98%. Adding an ordinary pair gives 79.59% coverage for SD+SB, and 93.88% coverage / 55.10% exact matching for MD+MC. These are separate-PCR unions of one degenerate and one ordinary pair.

Ordinary M improves to 59.18% coverage / 16.33% exact matching; its two-pair option reaches 77.55% / 16.33%. Ordinary S remains unchanged. SD and MD each have 12-fold F and 24-fold R degeneracy; a fixed directional concentration is divided among concrete variants. Exact matching means IUPAC compatibility, not that every variant matches or that amplification efficiency is established.

## Sequences and evidence

[Primer pairs](results/current/primer_pairs.csv) · [FASTA](results/current/primers.fasta) · [Comparison](results/current/comparison.csv) · [S/M missed references](results/sm_optimization/missed_references.csv) · [L/XL baseline gaps](results/compact/missed_references.csv) · [Verification](results/sm_optimization/verification.json)

## Base matching

Actual bases are shown: blue = IUPAC-compatible, orange = mismatch, purple = possible G–T pairing; boxes mark the terminal three bases. Primers and same-sense references are 5′→3′; reverse-reference sites are reverse-complemented. Static figures show two-pair options and the most frequent weighted binding sequence in each order. The complete page includes single-pair options and all distinct binding sequences within each order.

![S base matching](figures/base_matching_S.svg)

![SD base matching](figures/base_matching_SD.svg)

![M base matching](figures/base_matching_M.svg)

![MD base matching](figures/base_matching_MD.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[S/M full base alignment](results/sm_optimization/base_matching.html) · [L/XL full base alignment](results/compact/base_matching.html)

## Evaluation scope

This round optimizes the common panel using frozen references and full-sequence revalidation. Wet-lab validation is pending. Region panels differ in taxonomic composition; common-panel performance is not class-wide coverage. Two-pair metrics represent separate PCR unions, not a validated multiplex mixture.

[Baseline analysis](docs/BASELINE.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
