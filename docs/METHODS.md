# Current methods and evidence boundaries

The v2.0.0 catalog contains 76 branch/taxon-limited assay entries, derived from 32 historical ordinary/D schemes. Ordinary oligos contain only A/C/G/T. A D scheme may become nondegenerate within a conserved group. Names do not imply that a D assay contains its ordinary counterpart or shares identical coordinates. Each row is a separate PCR pairing; it is not a component of an approved multiplex.

## Design

Existing target labels were stratified into Cidaroidea, Aulodonta, Echinacea and Irregularia and, when useful, smaller order or genus-labelled groups. Genus labels are not newly verified monophyletic clades. Nuclear 28S taxonomy was transferred only for exact species-name matches to existing metadata; unresolved labels were not guessed. Groups contained at least three records. Record counts, rather than species-level detection rates, are the current comparison unit.

D design first covers observed final-three-base variants, then explores internal degeneracy. The initial search allowed up to 64 concrete variants per oligo; the shifted-window search used a 16-variant cap. Ordinary candidates retain concrete bases and require a conserved terminal triplet within the selected design group. Initial candidates used homologous sites or uniquely located raw-sequence pairs whose terminal eight bases agreed with the homologous templates. Five-prime trimming was allowed. The second round searched 18–27 nt primers with 3-prime endpoints moved by up to 20 nt per direction; COI S extended this to 50 nt and added genus-labelled groups. Only the top-ranked subsets entered background screening. This was a finite heuristic search, not a global optimum.

## Target and non-target matching

Both sequence orientations are scanned. Target products span 60–650 bp with non-overlapping primer sites. Coverage requires at most two mismatches per primer and exact IUPAC compatibility at the final three positions. Exact matching requires no mismatches at either end. Ambiguous template bases at binding sites are excluded. Background geometry allows 0–1,000 internal bases. Four background quantities are retained: strict Watson–Crick (WC), strict GT-permissive, relaxed WC with three mismatches per end, and relaxed GT with two. Strict models retain the terminal-triplet criterion; the GT model also permits its defined wobble compatibility there. The target terminal rule uses WC only.

Every adopted row covers all records in its own design panel and has each of the four background counts no higher than its original assay, re-scanned on the same inputs. Nonzero original/background counts can therefore remain. These are counts of known background records, not estimates of environmental specificity. The background does not test exclusivity against other echinoid branches. Separate PCR and downstream taxonomic assignment are required.

## Thermodynamic screening

Primer3-py 2.4.0 expands all IUPAC variants. Hairpins, homodimers, within-direction variant heterodimers and F/R heterodimers are tested. Monovalent salt is 50 mM, Mg 1.5 mM and dNTP 0.6 mM. Scenarios are 50 nM per variant and 200 nM total per direction, divided by its variant count. Both require structure Tm below 55 °C, oligo Tm 45–75 °C and a forward/reverse Tm-range-midpoint difference no greater than 5 °C. The heterodimer calculation uses the larger participating concentration. These are screening assumptions, not validated PCR conditions.

Priority rows have at least a 5 °C gap between the lowest primer Tm and the largest structure Tm in each scenario. Eleven rows pass the primary gates but have a smaller gap and remain conditional. Adapters and indices were not included. Mixed subprimer pools were assessed for cross-dimers and cross F/R products, but are not recommended: COI S cross-pair background matches and other relaxed hits remain. Use each listed F/R pairing separately.

## Verification and limitations

The current revalidation compiles an exhaustive C++ scanner, recomputes each candidate and its original comparator on frozen target/background FASTA files, and checks all four background metrics. A separate Python motif-extension implementation verifies candidate target pairing. Both thermodynamic scenarios are recalculated. The shifted candidates also have independent intended-position and product-length checks in the adopted round-two evidence.

All design and selection results are in-sample. No independent holdout test or wet-lab validation has been performed on these 76 assays. Historical 16S common-panel, genus-blocked and barcode-resolution analyses describe historical primers only. They must not be transferred to the new assays, especially those with shifted endpoints. Barcode discrimination for the new products remains unassessed. Incomplete or unclassified references are not counted as successful detection, and small groups do not establish coverage of unsampled relatives.
