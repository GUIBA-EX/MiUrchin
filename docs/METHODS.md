# Methods

Reference coordinates use the ungapped mitochondrial 16S rRNA of NC_001453.1 (1-based). The XSD candidate binds at F 183–204 and R 344–363 on this reference, producing a 181 bp reference span. Each S–XL window has fixed forward and reverse endpoints; the primer-inclusive reference spans are 188, 228, 343 and 440 bp. Product lengths vary among taxa.

The target library contains 1,401 records. After taxonomy and sequence-quality review, one representative per species is retained: 165 species in the panel, of which 55, 158, 159 and 55 are evaluable for S, M, L and XL. XSD has 55 evaluable species. The non-target library contains 6,045 records. The primary coverage and exact-match metrics weight evaluable species equally; order-level results are reported separately. Missing binding windows are not counted as failures.

Coverage requires at most two mismatches per primer and IUPAC-compatible final 3 nt. Exact matching requires zero mismatches at both primer sites. Target paired scans require total length 150–500 bp and internal length at least 50 bp for S–XL; for XSD they require 70–500 bp and an internal length of at least 20 bp; background internal distance is 0–1,000 bp. WC3 and GT2 are permissive screens without a terminal constraint; strict WC and GT retain the coverage rule. Counts refer to reference records.

Candidate oligos have at most eight concrete variants and ambiguity confined to the 3′ half. Terminal checks exclude homotriplet ends and homopolymers longer than four bases and require GC in the final 3 nt. Primer3 evaluates 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP, 50 nM per variant and 200 nM total per direction. Structure Tm must be below 55°C and the difference between forward and reverse duplex-Tm midpoints at most 5°C.

Independent C++ and Python scans evaluate the same reference data; they are algorithmic verification rather than independent biological validation. Scripts are retained as [analysis provenance](../scripts/species_screening/README.md). Experimental validation remains necessary.
