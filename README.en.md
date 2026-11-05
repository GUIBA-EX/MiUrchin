![MiUrchin](figures/MiUrchin_overview.png)

# MiUrchin: in silico design and evaluation of mitochondrial and nuclear primers for sea urchin (Echinoidea) eDNA metabarcoding

**Fei Xia**

[正體中文](README.md) · [English](README.en.md) · [简体中文](README.zh-CN.md)

> Original overview artwork; its bp labels describe the historical 16S windows, not every current branch assay.

<!-- publication:start -->
**Integrated version 2.0.0 · Computational preprint · Not peer reviewed.**

[PDF](publications/MiUrchin_preprint.pdf) · [Markdown](publications/MiUrchin_preprint.md) · [CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [Supplement](publications/MiUrchin_supplement.md)
<!-- publication:end -->

MiUrchin contains 76 branch/taxon-limited pairs across 16S, 12S, COI and 28S: 65 priority and 11 conditional entries. Use each pairing in a separate PCR.

## Choosing an assay

Choose the target group first, then marker and parent scheme. Priority entries have at least a 5°C modeled structure margin; conditional entries require additional assessment. The 32 parent schemes do not imply identical binding coordinates or ordinary/D sequence inclusion.

## Primer sequences and predicted performance

All sequences are 5′→3′. Coverage and exact matching are record counts on each row’s design panel. Strict non-target counts are WC / GT. These are in-sample predictions, not experimentally validated detection rates.

### 16S

| Scheme / group | Tier | F (5′→3′) | R (5′→3′) | Covered | Exact | Strict non-target |
| --- | --- | --- | --- | --- | --- | --- |
| L / Arbacioida | priority | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTTTTCCTTTAATCGCC` | 4/4 | 2/4 | 0 / 0 |
| LD / Aulodonta | priority | `GTCTCCTAAATAGAGACTAGCATGAATGGC` | `GCGGTAACTTTTTCCTTTGATCAYC` | 15/15 | 0/15 | 0 / 0 |
| LD / Cidaroidea | priority | `TCTCCTAAATAGAGACTAGYATGAAYGGC` | `GCGGTAACTTRTTCYTTTGATCAYC` | 10/10 | 10/10 | 0 / 0 |
| LD / Arbacioida | priority | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTDTTCCTTTRATCGCC` | 4/4 | 4/4 | 0 / 0 |
| M / Clypeasteroida | priority | `GCCAGACGAGAAGACCCTG` | `CTTTGATCACCTAAGTGGATCA` | 4/4 | 2/4 | 0 / 0 |
| MD / Irregularia | conditional | `CGYYAGACGAGAAGACCCTR` | `CTTTGATCACCDDRGTGGATCA` | 29/29 | 27/29 | 0 / 0 |
| MD / Aulodonta | conditional | `CGYYAGACGAGAAGACCCTR` | `YTTTGATCACCKDRRTGGATCA` | 15/15 | 13/15 | 0 / 0 |
| S / Diadematoida | priority | `TGTGTATAATGGATTGACTAGA` | `GGCTAAGACCAATTTCTCGG` | 4/4 | 2/4 | 0 / 0 |
| SD / Camarodonta | priority | `GTGTATAATGGATTAACRAGH` | `TTAGCTYARACTAATTTYTYGG` | 28/28 | 14/28 | 0 / 0 |
| SD / Diadematoida | priority | `TGTGTATAATGGATTRACTAGA` | `GCTAAGACCAATTTCTCGG` | 4/4 | 4/4 | 0 / 0 |
| SD / Cidaroidea | priority | `GTGTATAATGGATTAGCAAGA` | `GGCTTAGACCAATTTTRCRA` | 3/3 | 3/3 | 0 / 0 |
| SD / Echinothurioida | priority | `TGTGTATAATGGATTAACAAGW` | `GCTTAGCTTAGACTAATTTCTYRR` | 3/3 | 0/3 | 0 / 0 |
| XS / Holasteroida | priority | `CTCGTGTATAATGGATTAACAA` | `AAGCTAATTTTTTGGGGAAC` | 6/6 | 2/6 | 0 / 0 |
| XSD / Diadematoida | priority | `CTTGTGTATAATGGATTRACTA` | `ACCAATTTCTCGGYGAAC` | 4/4 | 4/4 | 0 / 2 |
| XL / Diadematoida | priority | `GGCCTAGAAGCAGCCACTTCAG` | `CCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 3/4 | 0 / 0 |
| XL / Cidaroidea | priority | `CCAAGTAGGCCTAGAAGCAGC` | `GACAGTTTAGTTCCGTCTTGCC` | 3/3 | 2/3 | 0 / 2 |
| XLD / Irregularia | priority | `GTAGGCCTARAAGCAGCCRACTWW` | `GYTCCGTCTTGCCATTCATDCCAGTC` | 11/11 | 10/11 | 0 / 0 |
| XLD / Diadematoida | priority | `GGCCYAGAAGCAGCCACTTCAGH` | `CCCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 4/4 | 0 / 0 |
| XLD / Cidaroidea | priority | `GCCYAGAAGCAGCCAACYT` | `GACAGTTTAGTTCCGTCTTGCCRTT` | 3/3 | 3/3 | 0 / 0 |

### 12S

| Scheme / group | Tier | F (5′→3′) | R (5′→3′) | Covered | Exact | Strict non-target |
| --- | --- | --- | --- | --- | --- | --- |
| LD / Holasteroida | conditional | `ACCCTGYTATACTTAGMYGT` | `GTATTCCAGAGCTSTYTTCA` | 18/18 | 18/18 | 0 / 1 |
| LD / Clypeasteroida | priority | `ACCCTGCTATACTCAGAMGT` | `GCATTYCAGAGCTCTYTTCA` | 3/3 | 3/3 | 0 / 0 |
| LD / Cidaroidea | conditional | `ACCCTGTTATACTTAGCCGT` | `GCATYCCAGAGCTRRCTTCA` | 3/3 | 3/3 | 0 / 1 |
| M / Diadematoida | priority | `CGGTTTTCCATATCTACCT` | `ACTACTGAATCCGATTTCA` | 4/4 | 3/4 | 0 / 0 |
| M / Cidaroidea | conditional | `CGGTTTCCCAAACCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 2/3 | 0 / 0 |
| MD / Diadematoida | priority | `CGGTTTTCCAWATCTACCT` | `ACTACTGAATCCGRTTTCA` | 4/4 | 4/4 | 0 / 0 |
| MD / Cidaroidea | conditional | `CGGTTTCCCAAAYCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 3/3 | 0 / 0 |
| SD / Aulodonta | priority | `GTCCTAGTCCCAACTTTARC` | `AATGTTTAGCACTGCAGWYG` | 10/10 | 3/10 | 0 / 1 |
| SD / Cidaroidea | priority | `GTCCTAGTCCCGATCTTAAC` | `AATGTTTAGCACTGCAGRTG` | 3/3 | 2/3 | 0 / 0 |
| XL / Echinothurioida | priority | `CCACATGCAAGCTAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 2/3 | 0 / 0 |
| XLD / Echinothurioida | priority | `CCACATGCAAGYYAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 3/3 | 1 / 1 |
| XSD / Echinothurioida | conditional | `TGCCACATGCAAGYYAACTAG` | `TYTAGCACTGCAGWTGTGR` | 3/3 | 3/3 | 0 / 0 |
| L / Holasteroida | priority | `GATTAGATACCCTGCTATACTTAG` | `CGTATTCCAGAGCTGTCTTCA` | 18/18 | 8/18 | 0 / 0 |
| L / Cidaroidea | priority | `GATACCCTGTTATACTTAGCCGTAAAC` | `GAGTGACGGGCGATGTGTACG` | 3/3 | 3/3 | 0 / 0 |
| S / Irregularia | priority | `CCGATTTGGTCCTAGTCCC` | `TCTAATGTTTAGCACTGCAGT` | 19/19 | 11/19 | 0 / 0 |
| S / Temnopleuroida | priority | `CGATTTGGTCCTAGTCCC` | `CACTGCAGTTGTGGCGTAT` | 11/11 | 7/11 | 0 / 0 |
| S / Diadematoida | priority | `GTCCCAACTTTAACTAGCT` | `AATGTTTAGCACTGCAGA` | 4/4 | 3/4 | 0 / 0 |
| S / Cidaroidea | priority | `CGATTTGGTCCTAGTCCCGATCTTAAC` | `CTCTAATTGTCTAATGTTTAGCACTGC` | 3/3 | 2/3 | 0 / 0 |
| S / Echinothurioida | priority | `CCGATTTGGTCCTAGTCCCA` | `CCTGATTGTCTAATGTTTAGCACTGC` | 3/3 | 1/3 | 0 / 0 |
| XS / Holasteroida | priority | `GCCACATGCAAGCTAACTAGC` | `TCTAATGTTTAGCACTGCAGT` | 16/16 | 8/16 | 0 / 0 |
| XS / Diadematoida | priority | `AACTAGCAAACCAGTGAAGT` | `CCCTAATTGTCCAATGTTTAGCACT` | 4/4 | 3/4 | 0 / 0 |
| XS / Echinothurioida | priority | `CCACATGCAAGCTAACTAG` | `CCTGATTGTCTAATGTTTAGCACTG` | 3/3 | 1/3 | 0 / 0 |

### COI

| Scheme / group | Tier | F (5′→3′) | R (5′→3′) | Covered | Exact | Strict non-target |
| --- | --- | --- | --- | --- | --- | --- |
| MD / Cidaroidea | conditional | `TCAAACCTTCAATGAGARAC` | `ACCTTTCTTCABAGDGGGTG` | 7/7 | 2/7 | 0 / 0 |
| SD / Cidaroidea | conditional | `CARGGVTCAAAYCTYCAATG` | `AATCARTGWGARAAYCCDGC` | 7/7 | 5/7 | 0 / 1 |
| SD / Echinothurioida | priority | `CAAGGGTCYAAYCTRCARTG` | `AATCAGTGGGTRAAKCCDGC` | 3/3 | 1/3 | 0 / 0 |
| XSD / Cidaroidea | conditional | `TCAAACCTTCAATGAGARAC` | `CRTAGTGRAAGTGGGCHAC` | 7/7 | 2/7 | 0 / 0 |
| XSD / Echinothurioida | priority | `TCTAACCTACAATGAGARAC` | `ACGTAATGAAAGTGTGCWAC` | 3/3 | 0/3 | 0 / 0 |
| M / Cidaroidea | priority | `AGGATCAAACCTTCAATG` | `CCTTTCTTCATAGAGGGTG` | 7/7 | 0/7 | 0 / 0 |
| XS / Echinothurioida | priority | `GTCTAACCTACAATGAGA` | `CTACATAGTAAGTGTCGTGA` | 3/3 | 0/3 | 0 / 0 |
| S / Holasteroida | priority | `TCAAACCTCCAATGAGAAAC` | `GCCAAATACAGCACCCAT` | 6/6 | 2/6 | 0 / 0 |
| S / genus_Lytechinus | priority | `TTCAGATGAATGGCCACACTACAAGG` | `GCGGGTGTAGGCTGTATCC` | 5/5 | 4/5 | 0 / 0 |
| S / genus_Echinometra | priority | `ATGGCAACCCTTCAAGGCTCAAA` | `AGTGGGTGTAGGTTGTATCCAGAGAAT` | 4/4 | 3/4 | 0 / 0 |
| S / genus_Clypeaster | priority | `TCAAACCTTCAATGAGAAAC` | `ACAGCTCCCATGGATAGT` | 4/4 | 2/4 | 0 / 0 |
| S / genus_Temnopleurus | priority | `TCCAACAGGAATTAAGGT` | `CTTCATAGGGGGTGTAAACTATA` | 3/3 | 1/3 | 0 / 0 |

### 28S

| Scheme / group | Tier | F (5′→3′) | R (5′→3′) | Covered | Exact | Strict non-target |
| --- | --- | --- | --- | --- | --- | --- |
| L / Echinacea | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| L / Aulodonta | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| L / Clypeasteroida | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| L / Cidaroidea | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| LD / Echinacea | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| LD / Aulodonta | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| LD / Clypeasteroida | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| LD / Cidaroidea | priority | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| M / Echinacea | priority | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 12/12 | 9/12 | 0 / 1 |
| M / Holasteroida | priority | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 9/11 | 0 / 1 |
| M / Diadematoida | priority | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGCGGCTCCAG` | 6/6 | 4/6 | 0 / 1 |
| M / Clypeasteroida | priority | `AATAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 3/5 | 0 / 1 |
| MD / Cidaroidea | priority | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCMR` | 17/17 | 15/17 | 0 / 2 |
| MD / Echinacea | priority | `AWRAGCCCATCGCCGAATCC` | `CYGACTCTTGGTGRCTCCAG` | 12/12 | 12/12 | 0 / 1 |
| MD / Holasteroida | conditional | `AAGAGCCYATCGCYGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 11/11 | 0 / 1 |
| MD / Diadematoida | priority | `AAGAGCCCAKCGCYGAATCC` | `CCGACTCTTGGYGGCTCCAG` | 6/6 | 6/6 | 0 / 1 |
| MD / Clypeasteroida | priority | `AAKAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 5/5 | 0 / 1 |
| S / Irregularia | priority | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| S / Echinacea | priority | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 10/12 | 0 / 0 |
| S / Diadematoida | priority | `CCTGGAGCCGCCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 6/6 | 5/6 | 0 / 0 |
| SD / Irregularia | priority | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| SD / Echinacea | priority | `GCCTGGAGYCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 12/12 | 0 / 0 |
| SD / Aulodonta | priority | `CCTGGARCCRCCRWGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 9/9 | 8/9 | 0 / 0 |

[CSV](sequences/primer_pairs.csv) · [FASTA](sequences/all_markers.fasta) · [Priority FASTA](sequences/priority.fasta) · [Conditional FASTA](sequences/conditional.fasta)

## Binding sites and comparisons

Shifted binding sites are specific to the applicable reference records. See the [full evidence catalog](results/catalog.json) and [comparison table](report.html); historical coordinates are not presented as current coordinates.

![Exact comparison](figures/exact_comparison.svg)

## Reference panels and screening

Final three bases must match under WC; each end allows at most two total mismatches. Background counts must not exceed the original assay. All variants were checked for structures in two concentration scenarios. [Methods](docs/METHODS.md) · [Reproducibility](docs/REPRODUCIBILITY.md).

## Historical supplementary analyses

[Archived v1.2](legacy/v1.2/README.en.md) retains the old common-panel, holdout and barcode analyses. They do not validate the new sequences. No current independent holdout or wet-lab validation is claimed. Do not directly pool subprimers: cross-pair non-target hits remain.

## Citation and copyright

[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [COPYRIGHT](COPYRIGHT.md)

## References

[MiFish](https://doi.org/10.1098/rsos.150088) · [Anth-28S](https://doi.org/10.7717/peerj.18607) · [Echinoid phylogenomics](https://doi.org/10.7554/eLife.72460)
