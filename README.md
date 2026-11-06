<div align="center">

# MiUrchin

**海膽 eDNA 引子設計與計算評價**

16S · 12S · COI · 28S  |  計算研究

[正體中文](README.md) · [English](README.en.md) · [簡體中文](README.zh-CN.md)

</div>

![MiUrchin 總覽](figures/MiUrchin_overview.png)

<sub>圖中長度為歷史 16S 窗口長度，其他基因和補充候選可能不同。</sub>

**32 對原始引子**為主方案；**76 對分支或分類群限定候選**為補充，不替代原方案。

## 快速入口

**主方案引子** · [FASTA](sequences/non_partitioned.fasta) · [配對表](sequences/non_partitioned_pairs.csv) · [名稱對照](sequences/primary_name_aliases.csv)

**區域資源** · [香港海膽交互地圖](https://guiba-ex.github.io/MiUrchin/) · [數據說明](resources/hong-kong-sea-urchins/README.md)

**稿件** · [PDF](publications/manuscript_20261106/MiUrchin_manuscript.pdf) · [Word](publications/manuscript_20261106/MiUrchin_manuscript.docx)

**證據與方法** · [方法](docs/METHODS.zh-CN.md) · [結果與局限](results/reviewer_revision/README.md) · [重現說明](docs/REPRODUCIBILITY.zh-CN.md)

[16S](#16s) · [12S](#12s) · [COI](#coi) · [28S](#28s) · [補充方案目錄](sequences/primer_pairs.csv) · [引用](CITATION.cff)

> **使用前須知：** 結果均為計算預測，尚未進行濕實驗驗證。補充分支設計面板中位數為 5 條紀錄；32 組比較中有 26 組候選並集丟失至少一條原方案匹配紀錄。非目標庫和獨立評價仍有限；補充候選須分別 PCR。[證據與局限](results/reviewer_revision/README.md)。

主方案 32 對均通過基本結構計算門檻，但其中 5 對在至少一種濃度情景下的最小結構餘量不足 5 °C；16S SD 的餘量為負。計算結果不能證明 PCR 表現，選擇前請查看[逐對結果](results/reviewer_revision/primary_pair_structures.csv)。

## 如何選擇擴增區段

可依研究目的選擇涵蓋較多物種的引子，或優先考慮兩端都與模板完全相符的引子。每個基因使用獨立的參考資料集；同一區段的兩種引子則用相同物種比較。

- **16S**　在五個區段都可評估的 49 種海膽中，XLD 涵蓋最多物種（45/49），LD 的雙端完全匹配數最高（19/49）。若關注 Spatangoida，MD 在其可評估資料集中涵蓋 0/37 種，LD 則涵蓋 36/38 種。
- **12S**　在 249 bp 的 M 區段，改用 MD 後，涵蓋物種由 25/69 增為 61/69，雙端完全匹配由 0 種增為 24 種。允許鳥嘌呤與胸腺嘧啶配對時，符合嚴格條件的非目標物種由 1 種增為 2 種。
- **COI**　152 bp 的 XSD 涵蓋 79/106 種，其中 3 種雙端完全匹配。209 bp 的 SD 涵蓋 63/105 種，其中 6 種雙端完全匹配。COI 參考資料集共有 314 種，但各保留區段僅有 103–106 種具備可評估的結合位置。此次篩選的 L 與 XL 候選均未通過非目標篩選門檻。
- **28S.** 核 28S 的 MD 在 111 個可評估物種中涵蓋 108 種，雙端完全匹配 72 種。短區段 SD 是計算篩選出的檢出候選；在 99 條取得的條碼中，僅 8 條在已取得的參考序列內具有獨有的內部序列。

## 引子序列與預測結果

FASTA 名稱依序標示基因、引子名稱與方向。例如，`MiUrchin-12S_MD_F` 是 12S M 區段的簡併正向引子。所有序列均依 5′→3′ 方向書寫。參考擴增長度依各基因內的座標計算，包含兩端引子；內部條碼長度只計算兩個結合位置之間的序列。 粒線體使用 NC_001453.1，核 28S 使用 XR_004063668.1。

**表格讀法。**「涵蓋」與「完全匹配」均以符合條件的物種數除以該區段可評估的物種數。「嚴格非目標」欄的兩個數字依序代表 **僅允許華生–克里克配對 / 另允許鳥嘌呤與胸腺嘧啶配對** 的結果。例如，16S XSD 的 0 / 7 表示兩種模型分別在 0 筆與 7 筆非目標紀錄中找到符合條件的引子配對。

### 16S

非目標背景包含 6,045 筆參考序列紀錄。

| 引子 | F（5′→3′） | R（5′→3′） | 參考擴增長度（bp） | 涵蓋 | 完全匹配 | 嚴格非目標 | 鹼基比對圖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `CTTGTGTATAATGGATTAACGA` | `AAACTAATTTCTTGGGAAAC` | 181 | 19/55 | 0/55 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/XS/base_matching_XS.svg) |
| XSD | `CTTGTGTATAATGGATTRACRA` | `AAACTAATTTCTTGGRRARC` | 181 | 35/55 | 6/55 | 0 / 7 | [檢視](legacy/v1.2/results/current_primers/XS/base_matching_XSD.svg) |
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` | 188 | 13/55 | 2/55 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/S/base_matching_S.svg) |
| SD | `TGTGTATAATGGATTAACRAGH` | `GCTTAGCTTAAACYAATTTCTYGR` | 188 | 29/55 | 3/55 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/S/base_matching_SD.svg) |
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` | 228 | 85/158 | 12/158 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/M/base_matching_M.svg) |
| MD | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCTDARTGGATCA` | 228 | 110/158 | 28/158 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/M/base_matching_MD.svg) |
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` | 343 | 103/159 | 18/159 | 0 / 0 | [檢視](legacy/v1.2/results/current_primers/L/base_matching_L.svg) |
| LD | `GTCTCCTAAATAGAGACTAGHATGAATGGC` | `GCGGTAACTTGTTYCTTTGRTCACY` | 343 | 141/159 | 30/159 | 2 / 12 | [檢視](legacy/v1.2/results/current_primers/L/base_matching_LD.svg) |
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` | 440 | 41/55 | 9/55 | 2 / 3 | [檢視](legacy/v1.2/results/current_primers/XL/base_matching_XL.svg) |
| XLD | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTY` | 440 | 51/55 | 6/55 | 0 / 4 | [檢視](legacy/v1.2/results/current_primers/XL/base_matching_XLD.svg) |

### 12S

非目標背景包含 459 種其他棘皮動物，每種取一條代表序列。

| 引子 | F（5′→3′） | R（5′→3′） | 參考擴增長度（bp） | 涵蓋 | 完全匹配 | 嚴格非目標 | 鹼基比對圖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `TGCCACATGCAAGCTTATTAG` | `TTTAGCACTGCAGATGTGG` | 153 | 27/67 | 0/67 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_XS.svg) |
| XSD | `TGCCACATGCAAGCYWAYTAG` | `TTTAGCACTGCAGDYGTGG` | 153 | 32/67 | 19/67 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_XSD.svg) |
| S | `GTCCTAGTCCCAATTTTAAC` | `AATGTTTAGCACTGCAGTTG` | 188 | 27/64 | 1/64 | 0 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_S.svg) |
| SD | `GTCCTAGTCCCAAYWTTARC` | `AATGTTTAGCACTGCAGDYG` | 188 | 56/64 | 19/64 | 0 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_SD.svg) |
| M | `CGGTTTTCCAAACCTCCCT` | `ACTGCTGAATCCAGTTTCT` | 249 | 25/69 | 0/69 | 1 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_M.svg) |
| MD | `CGGTTTTCCAWAYCTCCCT` | `ACTGCTGAATCCARTTTCN` | 249 | 61/69 | 24/69 | 2 / 2 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_MD.svg) |
| L | `ACCCTGTTATACTTAGACGT` | `GCATTCCAGAGCTCTCTTCA` | 347 | 23/69 | 0/69 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_L.svg) |
| LD | `ACCCTGTTATACTTAGMHGT` | `GCATTCCAGAGCTSWYTTCA` | 347 | 56/69 | 17/69 | 0 / 3 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_LD.svg) |
| XL | `CCACATGCAAGCTAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 452 | 32/67 | 15/67 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_XL.svg) |
| XLD | `CCACATGCAAGYYAAYTAGC` | `AAACCGCCAARTCCTTTGAR` | 452 | 40/67 | 21/67 | 2 / 3 | [檢視](legacy/v1.2/markers/12S_COI/figures/12S_XLD.svg) |

### COI

非目標背景包含 1,719 種其他棘皮動物，每種取一條代表序列。

| 引子 | F（5′→3′） | R（5′→3′） | 參考擴增長度（bp） | 涵蓋 | 完全匹配 | 嚴格非目標 | 鹼基比對圖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `TCAAACCTACAATGAGAAAC` | `ACATAGTGGAAGTGAGCTAC` | 152 | 34/106 | 0/106 | 0 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_XS.svg) |
| XSD | `TCAAACCTACARTGRGARAC` | `ACATAGTGGAAGTGDGCWAC` | 152 | 79/106 | 3/106 | 0 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_XSD.svg) |
| S | `CAAGGATCAAACCTACAATG` | `AATCAGTGAGTAAATCCTGC` | 209 | 28/105 | 3/105 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_S.svg) |
| SD | `CAAGGATCAAAYYTACARTG` | `AATCAGTGAGTRAAYCCWGC` | 209 | 63/105 | 6/105 | 1 / 1 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_SD.svg) |
| M | `TCAAACCTACAATGGGAAAC` | `ACCTTTCCTCATAGTGGGTG` | 248 | 22/103 | 0/103 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_M.svg) |
| MD | `TCAAACCTACARTGRGARAC` | `ACCTTTCCTCAWAGYGGRTG` | 248 | 57/103 | 1/103 | 0 / 0 | [檢視](legacy/v1.2/markers/12S_COI/figures/COI_MD.svg) |

### 28S

28S 以 122 個海膽雙名各一條序列建立面板，依目標模板的變異在引子後半段加入簡併位點。832 條非目標序列包含其他四綱棘皮動物與常見海洋動物。海參僅 3–4 條序列完整涵蓋各區段兩端。比對圖呈現全部 122 條模板，NA 表示無法評估。

| 引子 | F（5′→3′） | R（5′→3′） | 參考擴增長度（bp） | 涵蓋 | 完全匹配 | 嚴格非目標 | 鹼基比對圖 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 102 | 99/101 | 78/101 | 0 / 0 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/S.svg) |
| SD | `GCCTGGAGCCRCCAAGARTC` | `TTGTCTGCTATCGGTCTCGT` | 102 | 99/101 | 83/101 | 0 / 0 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/SD.svg) |
| M | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 176 | 104/111 | 49/111 | 0 / 1 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/M.svg) |
| MD | `AAGAGCCCATCGCYGAATCS` | `CCGACTCTTGGYGRCTCCMG` | 176 | 108/111 | 72/111 | 0 / 2 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/MD.svg) |
| L | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 282 | 88/91 | 82/91 | 0 / 0 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/L.svg) |
| LD | `AAGCTGGGCGCCTGYTCGAC` | `AATCGCTGCGGACCTCCACC` | 282 | 89/91 | 82/91 | 0 / 0 | [逐鹼基比對](legacy/v1.2/markers/28S/figures/LD.svg) |

[16S CSV](legacy/v1.2/results/current_primers/comparison.csv) · [12S / COI CSV](legacy/v1.2/markers/12S_COI/candidates.csv) · [28S CSV](legacy/v1.2/markers/28S/selected.csv)


## 補充：分支／分類群優化方案

[分支優化預印本](publications/MiUrchin_preprint.pdf) · [分支證據清單](results/catalog.json)

<details>
<summary>展開 76 對補充分支引子及方法說明</summary>

## 如何選擇區段

先選擇適用分類群，再選擇基因和原方案。優先方案在兩種濃度下的結構溫度餘量均至少為 5°C；條件備選需要進一步評估。補充候選的結合位置可能移動；D 引子不一定包含對應的普通引子序列。

## 引子序列與預測表現

序列均按 5′→3′ 書寫。“覆蓋”和“完全匹配”為各行設計面板的參考紀錄數；“嚴格非目標”為 WC / GT 兩種模型的計數。面板內計算匹配不等於實驗檢出率。

### 16S

| 方案／分類群 | 分級 | F（5′→3′） | R（5′→3′） | 覆蓋 | 完全匹配 | 嚴格非目標 |
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

| 方案／分類群 | 分級 | F（5′→3′） | R（5′→3′） | 覆蓋 | 完全匹配 | 嚴格非目標 |
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

| 方案／分類群 | 分級 | F（5′→3′） | R（5′→3′） | 覆蓋 | 完全匹配 | 嚴格非目標 |
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

| 方案／分類群 | 分級 | F（5′→3′） | R（5′→3′） | 覆蓋 | 完全匹配 | 嚴格非目標 |
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

## 結合位置與逐鹼基匹配

移動後的結合位置依各自參考紀錄核驗。詳見[完整證據清單](results/catalog.json)與[原版／新版比較](report.html)；歷史座標和匹配圖不作為新引子的結果。

![Exact comparison](figures/exact_comparison.svg)

## 參考面板與篩選規則

雙端最後三位須嚴格 WC 匹配，每端總錯配最多兩處；四項非目標計數不得高於原引子。全部簡併變體在兩種濃度下檢查結構。[中文方法](docs/METHODS.zh-CN.md) · [重現說明](docs/REPRODUCIBILITY.zh-CN.md)。

## 16S 補充評價

[歷史 v1.2](legacy/v1.2/README.zh-CN.md)保留舊版共同面板、留出與條碼分析，不用於驗證新序列。目前尚無獨立留出或濕實驗驗證。子引子不可直接混合，交叉配對仍可命中非目標。

## 引用與著作權

[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [COPYRIGHT](COPYRIGHT.md)

## 參考文獻

[MiFish](https://doi.org/10.1098/rsos.150088) · [Anth-28S](https://doi.org/10.7717/peerj.18607) · [Echinoid phylogenomics](https://doi.org/10.7554/eLife.72460)

</details>
