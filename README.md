![MiUrchin](figures/MiUrchin_overview.png)

# MiUrchin: in silico design and evaluation of mitochondrial and nuclear primers for sea urchin (Echinoidea) eDNA metabarcoding

**Fei Xia**

[正體中文](README.md) · [English](README.en.md) · [简体中文](README.zh-CN.md)

> 保留原版概覽圖；圖中 bp 數為歷史 16S 區段长度，不代表所有新版分支引子的产物长度。

<!-- publication:start -->
**整合版本 v2.0.0 · 計算预印本 · 未經同行評审。**

[PDF](publications/MiUrchin_preprint.pdf) · [Markdown](publications/MiUrchin_preprint.md) · [CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [Supplement](publications/MiUrchin_supplement.md)
<!-- publication:end -->

MiUrchin 收录 76 對分支／分類群限定引子，涵盖 16S、12S、COI 和 28S：65 對優先驗證，11 對條件備選。每个 F/R 组合分别 PCR。

## 如何選擇區段

先選擇适用分類群，再選擇基因和原方案。優先方案在两种浓度下的結构温度余量均至少為 5°C；條件備選需要进一步評估。32 组原方案不再意味着普通／D引子具有相同坐標或包含关系。

## 引子序列與预测表现

序列均按 5′→3′ 书写。“覆盖”和“完全匹配”為各行设計面板的参考紀錄數；“严格非目標”為 WC / GT 两种模型的計數。面板内計算匹配不等于實驗检出率。

### 16S

| 方案／分類群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目標 |
| --- | --- | --- | --- | --- | --- | --- |
| L / Arbacioida | 優先 | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTTTTCCTTTAATCGCC` | 4/4 | 2/4 | 0 / 0 |
| LD / Aulodonta | 優先 | `GTCTCCTAAATAGAGACTAGCATGAATGGC` | `GCGGTAACTTTTTCCTTTGATCAYC` | 15/15 | 0/15 | 0 / 0 |
| LD / Cidaroidea | 優先 | `TCTCCTAAATAGAGACTAGYATGAAYGGC` | `GCGGTAACTTRTTCYTTTGATCAYC` | 10/10 | 10/10 | 0 / 0 |
| LD / Arbacioida | 優先 | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTDTTCCTTTRATCGCC` | 4/4 | 4/4 | 0 / 0 |
| M / Clypeasteroida | 優先 | `GCCAGACGAGAAGACCCTG` | `CTTTGATCACCTAAGTGGATCA` | 4/4 | 2/4 | 0 / 0 |
| MD / Irregularia | 條件備選 | `CGYYAGACGAGAAGACCCTR` | `CTTTGATCACCDDRGTGGATCA` | 29/29 | 27/29 | 0 / 0 |
| MD / Aulodonta | 條件備選 | `CGYYAGACGAGAAGACCCTR` | `YTTTGATCACCKDRRTGGATCA` | 15/15 | 13/15 | 0 / 0 |
| S / Diadematoida | 優先 | `TGTGTATAATGGATTGACTAGA` | `GGCTAAGACCAATTTCTCGG` | 4/4 | 2/4 | 0 / 0 |
| SD / Camarodonta | 優先 | `GTGTATAATGGATTAACRAGH` | `TTAGCTYARACTAATTTYTYGG` | 28/28 | 14/28 | 0 / 0 |
| SD / Diadematoida | 優先 | `TGTGTATAATGGATTRACTAGA` | `GCTAAGACCAATTTCTCGG` | 4/4 | 4/4 | 0 / 0 |
| SD / Cidaroidea | 優先 | `GTGTATAATGGATTAGCAAGA` | `GGCTTAGACCAATTTTRCRA` | 3/3 | 3/3 | 0 / 0 |
| SD / Echinothurioida | 優先 | `TGTGTATAATGGATTAACAAGW` | `GCTTAGCTTAGACTAATTTCTYRR` | 3/3 | 0/3 | 0 / 0 |
| XS / Holasteroida | 優先 | `CTCGTGTATAATGGATTAACAA` | `AAGCTAATTTTTTGGGGAAC` | 6/6 | 2/6 | 0 / 0 |
| XSD / Diadematoida | 優先 | `CTTGTGTATAATGGATTRACTA` | `ACCAATTTCTCGGYGAAC` | 4/4 | 4/4 | 0 / 2 |
| XL / Diadematoida | 優先 | `GGCCTAGAAGCAGCCACTTCAG` | `CCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 3/4 | 0 / 0 |
| XL / Cidaroidea | 優先 | `CCAAGTAGGCCTAGAAGCAGC` | `GACAGTTTAGTTCCGTCTTGCC` | 3/3 | 2/3 | 0 / 2 |
| XLD / Irregularia | 優先 | `GTAGGCCTARAAGCAGCCRACTWW` | `GYTCCGTCTTGCCATTCATDCCAGTC` | 11/11 | 10/11 | 0 / 0 |
| XLD / Diadematoida | 優先 | `GGCCYAGAAGCAGCCACTTCAGH` | `CCCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 4/4 | 0 / 0 |
| XLD / Cidaroidea | 優先 | `GCCYAGAAGCAGCCAACYT` | `GACAGTTTAGTTCCGTCTTGCCRTT` | 3/3 | 3/3 | 0 / 0 |

### 12S

| 方案／分類群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目標 |
| --- | --- | --- | --- | --- | --- | --- |
| LD / Holasteroida | 條件備選 | `ACCCTGYTATACTTAGMYGT` | `GTATTCCAGAGCTSTYTTCA` | 18/18 | 18/18 | 0 / 1 |
| LD / Clypeasteroida | 優先 | `ACCCTGCTATACTCAGAMGT` | `GCATTYCAGAGCTCTYTTCA` | 3/3 | 3/3 | 0 / 0 |
| LD / Cidaroidea | 條件備選 | `ACCCTGTTATACTTAGCCGT` | `GCATYCCAGAGCTRRCTTCA` | 3/3 | 3/3 | 0 / 1 |
| M / Diadematoida | 優先 | `CGGTTTTCCATATCTACCT` | `ACTACTGAATCCGATTTCA` | 4/4 | 3/4 | 0 / 0 |
| M / Cidaroidea | 條件備選 | `CGGTTTCCCAAACCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 2/3 | 0 / 0 |
| MD / Diadematoida | 優先 | `CGGTTTTCCAWATCTACCT` | `ACTACTGAATCCGRTTTCA` | 4/4 | 4/4 | 0 / 0 |
| MD / Cidaroidea | 條件備選 | `CGGTTTCCCAAAYCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 3/3 | 0 / 0 |
| SD / Aulodonta | 優先 | `GTCCTAGTCCCAACTTTARC` | `AATGTTTAGCACTGCAGWYG` | 10/10 | 3/10 | 0 / 1 |
| SD / Cidaroidea | 優先 | `GTCCTAGTCCCGATCTTAAC` | `AATGTTTAGCACTGCAGRTG` | 3/3 | 2/3 | 0 / 0 |
| XL / Echinothurioida | 優先 | `CCACATGCAAGCTAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 2/3 | 0 / 0 |
| XLD / Echinothurioida | 優先 | `CCACATGCAAGYYAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 3/3 | 1 / 1 |
| XSD / Echinothurioida | 條件備選 | `TGCCACATGCAAGYYAACTAG` | `TYTAGCACTGCAGWTGTGR` | 3/3 | 3/3 | 0 / 0 |
| L / Holasteroida | 優先 | `GATTAGATACCCTGCTATACTTAG` | `CGTATTCCAGAGCTGTCTTCA` | 18/18 | 8/18 | 0 / 0 |
| L / Cidaroidea | 優先 | `GATACCCTGTTATACTTAGCCGTAAAC` | `GAGTGACGGGCGATGTGTACG` | 3/3 | 3/3 | 0 / 0 |
| S / Irregularia | 優先 | `CCGATTTGGTCCTAGTCCC` | `TCTAATGTTTAGCACTGCAGT` | 19/19 | 11/19 | 0 / 0 |
| S / Temnopleuroida | 優先 | `CGATTTGGTCCTAGTCCC` | `CACTGCAGTTGTGGCGTAT` | 11/11 | 7/11 | 0 / 0 |
| S / Diadematoida | 優先 | `GTCCCAACTTTAACTAGCT` | `AATGTTTAGCACTGCAGA` | 4/4 | 3/4 | 0 / 0 |
| S / Cidaroidea | 優先 | `CGATTTGGTCCTAGTCCCGATCTTAAC` | `CTCTAATTGTCTAATGTTTAGCACTGC` | 3/3 | 2/3 | 0 / 0 |
| S / Echinothurioida | 優先 | `CCGATTTGGTCCTAGTCCCA` | `CCTGATTGTCTAATGTTTAGCACTGC` | 3/3 | 1/3 | 0 / 0 |
| XS / Holasteroida | 優先 | `GCCACATGCAAGCTAACTAGC` | `TCTAATGTTTAGCACTGCAGT` | 16/16 | 8/16 | 0 / 0 |
| XS / Diadematoida | 優先 | `AACTAGCAAACCAGTGAAGT` | `CCCTAATTGTCCAATGTTTAGCACT` | 4/4 | 3/4 | 0 / 0 |
| XS / Echinothurioida | 優先 | `CCACATGCAAGCTAACTAG` | `CCTGATTGTCTAATGTTTAGCACTG` | 3/3 | 1/3 | 0 / 0 |

### COI

| 方案／分類群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目標 |
| --- | --- | --- | --- | --- | --- | --- |
| MD / Cidaroidea | 條件備選 | `TCAAACCTTCAATGAGARAC` | `ACCTTTCTTCABAGDGGGTG` | 7/7 | 2/7 | 0 / 0 |
| SD / Cidaroidea | 條件備選 | `CARGGVTCAAAYCTYCAATG` | `AATCARTGWGARAAYCCDGC` | 7/7 | 5/7 | 0 / 1 |
| SD / Echinothurioida | 優先 | `CAAGGGTCYAAYCTRCARTG` | `AATCAGTGGGTRAAKCCDGC` | 3/3 | 1/3 | 0 / 0 |
| XSD / Cidaroidea | 條件備選 | `TCAAACCTTCAATGAGARAC` | `CRTAGTGRAAGTGGGCHAC` | 7/7 | 2/7 | 0 / 0 |
| XSD / Echinothurioida | 優先 | `TCTAACCTACAATGAGARAC` | `ACGTAATGAAAGTGTGCWAC` | 3/3 | 0/3 | 0 / 0 |
| M / Cidaroidea | 優先 | `AGGATCAAACCTTCAATG` | `CCTTTCTTCATAGAGGGTG` | 7/7 | 0/7 | 0 / 0 |
| XS / Echinothurioida | 優先 | `GTCTAACCTACAATGAGA` | `CTACATAGTAAGTGTCGTGA` | 3/3 | 0/3 | 0 / 0 |
| S / Holasteroida | 優先 | `TCAAACCTCCAATGAGAAAC` | `GCCAAATACAGCACCCAT` | 6/6 | 2/6 | 0 / 0 |
| S / genus_Lytechinus | 優先 | `TTCAGATGAATGGCCACACTACAAGG` | `GCGGGTGTAGGCTGTATCC` | 5/5 | 4/5 | 0 / 0 |
| S / genus_Echinometra | 優先 | `ATGGCAACCCTTCAAGGCTCAAA` | `AGTGGGTGTAGGTTGTATCCAGAGAAT` | 4/4 | 3/4 | 0 / 0 |
| S / genus_Clypeaster | 優先 | `TCAAACCTTCAATGAGAAAC` | `ACAGCTCCCATGGATAGT` | 4/4 | 2/4 | 0 / 0 |
| S / genus_Temnopleurus | 優先 | `TCCAACAGGAATTAAGGT` | `CTTCATAGGGGGTGTAAACTATA` | 3/3 | 1/3 | 0 / 0 |

### 28S

| 方案／分類群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目標 |
| --- | --- | --- | --- | --- | --- | --- |
| L / Echinacea | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| L / Aulodonta | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| L / Clypeasteroida | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| L / Cidaroidea | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| LD / Echinacea | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| LD / Aulodonta | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| LD / Clypeasteroida | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| LD / Cidaroidea | 優先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| M / Echinacea | 優先 | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 12/12 | 9/12 | 0 / 1 |
| M / Holasteroida | 優先 | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 9/11 | 0 / 1 |
| M / Diadematoida | 優先 | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGCGGCTCCAG` | 6/6 | 4/6 | 0 / 1 |
| M / Clypeasteroida | 優先 | `AATAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 3/5 | 0 / 1 |
| MD / Cidaroidea | 優先 | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCMR` | 17/17 | 15/17 | 0 / 2 |
| MD / Echinacea | 優先 | `AWRAGCCCATCGCCGAATCC` | `CYGACTCTTGGTGRCTCCAG` | 12/12 | 12/12 | 0 / 1 |
| MD / Holasteroida | 條件備選 | `AAGAGCCYATCGCYGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 11/11 | 0 / 1 |
| MD / Diadematoida | 優先 | `AAGAGCCCAKCGCYGAATCC` | `CCGACTCTTGGYGGCTCCAG` | 6/6 | 6/6 | 0 / 1 |
| MD / Clypeasteroida | 優先 | `AAKAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 5/5 | 0 / 1 |
| S / Irregularia | 優先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| S / Echinacea | 優先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 10/12 | 0 / 0 |
| S / Diadematoida | 優先 | `CCTGGAGCCGCCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 6/6 | 5/6 | 0 / 0 |
| SD / Irregularia | 優先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| SD / Echinacea | 優先 | `GCCTGGAGYCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 12/12 | 0 / 0 |
| SD / Aulodonta | 優先 | `CCTGGARCCRCCRWGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 9/9 | 8/9 | 0 / 0 |

[CSV](sequences/primer_pairs.csv) · [FASTA](sequences/all_markers.fasta) · [Priority FASTA](sequences/priority.fasta) · [Conditional FASTA](sequences/conditional.fasta)

## 結合位置與逐碱基匹配

移动后的結合位置依各自参考紀錄核验。详见[完整证據清单](results/catalog.json)與[原版／新版比较](report.html)；歷史坐標和匹配圖不作為新引子的結果。

![Exact comparison](figures/exact_comparison.svg)

## 参考面板與篩选規則

双端最后三位须严格 WC 匹配，每端总错配最多两处；四项非目標計數不得高于原引子。全部简并变体在两种浓度下检查結构。[中文方法](docs/METHODS.zh-CN.md) · [重现說明](docs/REPRODUCIBILITY.zh-CN.md)。

## 16S 補充評价

[歷史 v1.2](legacy/v1.2/README.zh-CN.md)保留旧版共同面板、留出與条碼分析，不用于驗證新序列。目前尚无獨立留出或湿實驗驗證。子引子不可直接混合，交叉配對仍可命中非目標。

## 引用與著作权

[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [COPYRIGHT](COPYRIGHT.md)

## 参考文献

[MiFish](https://doi.org/10.1098/rsos.150088) · [Anth-28S](https://doi.org/10.7717/peerj.18607) · [Echinoid phylogenomics](https://doi.org/10.7554/eLife.72460)
