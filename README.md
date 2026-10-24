# MiUrchin

[中文](README.zh-CN.md) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md)

Mitochondrial 16S primers for sea urchins. MiFish-inspired base-level consensus design searches four length windows and selects one-pair and two-pair separate-PCR options.

Lengths are S, M, L and XL. A single pair uses the region name; the two-pair components use A and B, for example SA and SB, with union metrics labelled SA+SB. All sequences are 5′→3′.

## Portfolio comparison

The common panel contains 49 taxonomic name labels and 80 within-label haplotypes, weighted equally by label and then by haplotype within label. The background contains 6,045 records.

| Scheme | Pairs | Coverage | Exact | Product bp | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| S | 1 | 40.82% | 20.41% | 188–191 | 0 | 3 | 4 |
| SA+SB | 2 | 61.22% | 20.41% | 188–193 | 0 | 3 | 7 |
| M | 1 | 36.73% | 6.12% | 236–244 | 0 | 1 | 12 |
| MA+MB | 2 | 46.94% | 8.16% | 224–244 | 1 | 1 | 32 |
| L | 1 | 75.51% | 19.39% | 337–362 | 2 | 1 | 161 |
| LA+LB | 2 | 87.76% | 19.39% | 337–362 | 2 | 1 | 162 |
| XL | 1 | 85.71% | 6.12% | 442–456 | 2 | 1 | 10 |
| XLA+XLB | 2 | 100.00% | 26.53% | 434–457 | 0 | 2 | 9 |

Coverage permits up to two mismatches per primer with the terminal three bases exactly matched; exact matching requires zero mismatches in both primers. GT is a separate G–T tolerance sensitivity model, not strict exact matching. Background values count accessions, not experimental amplification fractions.

**Selection guidance:** compare L and XL when coverage is the priority. Short-fragment S and M have limited nondegenerate coverage. Two-pair versus six-pair baseline coverage is 61.22% vs 87.76%, 46.94% vs 95.92%, 87.76% vs 97.96%, and 100% vs 100%, respectively. Simplification is not an across-the-board performance improvement. L still hits 161–162 background accessions under WC≤4.

All 1,920 per-reference comparisons agreed with the independent full-sequence scan; all 12 paired entries passed thermodynamic gates. [Validation](results/compact/independent_validation.json) · [Thermodynamics](results/compact/thermal.csv)

## Sequences and evidence

[Primer pairs](results/compact/primer_pairs.csv) · [FASTA](results/compact/primers.fasta) · [Comparison](results/compact/comparison.csv) · [Missed references](results/compact/missed_references.csv) · [Verification](results/compact/verification.json)

## Base matching

Actual bases are shown: blue = match, orange = mismatch, purple = possible G–T pairing; boxes mark the terminal three bases. Primers and same-sense references are 5′→3′; reverse-reference sites are reverse-complemented. Static figures show A/B pairs and the most frequent weighted binding sequence in each order. The complete page includes single-pair options and all distinct binding sequences within each order.

![S base matching](figures/base_matching_S.svg)

![M base matching](figures/base_matching_M.svg)

![L base matching](figures/base_matching_L.svg)

![XL base matching](figures/base_matching_XL.svg)

[Full base alignment](results/compact/base_matching.html)

## Evaluation scope

This round optimizes the common panel using frozen references and full-sequence revalidation. Wet-lab validation is pending. Region panels differ in taxonomic composition; common-panel performance is not class-wide coverage. Two-pair metrics represent separate PCR unions, not a validated multiplex mixture.

[Baseline analysis](docs/BASELINE.md) · [Reproduction](docs/REPRODUCIBILITY.md)

## Copyright

Copyright © 2026 Fei Xia (GUIBA-EX). All rights reserved. [Terms / 使用声明](COPYRIGHT.md).
