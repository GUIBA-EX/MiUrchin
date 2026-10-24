# Methods

[中文](METHODS.zh-CN.md)

## Reference panel and candidate search

The common panel has 49 taxonomic labels and 80 haplotypes, weighted equally by label and then within label. Frozen target and background FASTA files contain 1,401 and 6,045 records. Coordinates refer to extracted, ungapped NC_001453.1 16S rRNA, not the complete mitogenome.

The initial pool contains observed and consensus primers from four homologous windows. The terminal-correction round adds 3′ shortening and extension by up to 6 bases around previously selected S/M oligos, retaining lengths 18–32 nt. Extensions use up to three observed flank sequences. IUPAC restrictions can remove concrete variants with long homopolymers without adding a base outside the original ambiguity code. Existing L/XL candidates remain available. This is a bounded candidate search.

## Terminal and thermodynamic constraints

Every concrete IUPAC variant must have: no terminal homotriplet; at least one G/C in the final three bases; 1–4 G/C in the final five bases; and no homopolymer longer than four bases anywhere. These are project-specific conservative filters informed by [Thermo Fisher guidance](https://www.thermofisher.com/blog/behindthebench/pcr-primer-design-tips/) and [Primer3 parameters](https://primer3.org/manual.html). A G/C at the very last base is not mandatory. Four-base internal runs can remain.

Primer3 uses 50 mM monovalent salt, 1.5 mM Mg²⁺ and 0.6 mM dNTP. Expand all concrete variants under two scenarios: 50 nM per variant, and 200 nM per direction divided equally among variants. Hairpin, homodimer, within-direction heterodimer and F/R heterodimer Tm must be below 55°C. The difference between F and R Tm-range midpoints must be ≤5°C in both scenarios; this does not constrain every cross-variant Tm difference. Unequal-concentration heterodimers use the larger concentration as an approximation.

The terminal audit also reports Primer3 end-stability ΔG at 37°C for each terminal 5-mer against its perfect reverse complement, at the stated salts and 200 nM. Variant minima/maxima are reported in kcal/mol. This descriptive calculation has no fitted pass/fail threshold and is not a prediction of PCR yield.

## Selection and independent verification

Target coverage permits ≤2 mismatches per primer and requires exact IUPAC compatibility in the last three bases. Exact matching requires zero mismatches in both primers. Target products must be 150–500 bp with ≥50 internal bases. Background scans cover both strands, correct orientation and 0–1,000 nt internal distance. Each portfolio allows at most five WC≤3 and five GT≤2 background accessions; WC≤4 is reported as a more permissive sensitivity result.

S/M/XL selections maximize the equally weighted sum of coverage and exact matching, then coverage, exact matching, lower total degeneracy and fewer background accessions. This explicitly trades some coverage for exact matching. L retains its coverage-first ranking because the prior selected pairs pass the terminal rules. Two-pair mixed portfolios reuse the selected degenerate single pair plus one ordinary pair. Identical target/background states are reduced to the lowest-degeneracy representative before selection; this bounded reduction is not a proof of global optimality.

A separate C++ all-window paired-product scanner verifies the selected sequences without the candidate scanner's early-rejection filter. The published verification contains 2,880 target-state checks with zero disagreements. The 12 portfolios contain 18 paired rows and 14 pair names / 28 exported oligos. Metrics are separate-PCR unions, not validated multiplex performance. Wet-lab validation is pending.

## Coordinate and base-matching figures

The position map is generated directly from each selected oligo's reference interval on one linear scale. Interval lengths are checked against oligo lengths. Homologous intervals can contain mismatches to NC_001453.1; reference bases and mismatch counts are included in the coordinate table. The representative SD, MD, L and XL spans are 188, 228, 343 and 440 bp, respectively. Base-matching diagrams show actual bases oriented 5′→3′ and mark the terminal three bases.

Design context: [Miya et al. 2015](https://doi.org/10.1098/rsos.150088). [Reproduction](REPRODUCIBILITY.md).
