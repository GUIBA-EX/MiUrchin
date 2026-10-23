# Validation / 验证

## Material Passport

- Mode / 模式: computational experiment execution and deterministic validation / 计算实验与确定性复核。
- Data / 数据: frozen accession-labelled nucleotide sequences; no participant data / 冻结公共accession核酸数据，无人类受试者资料。
- Scope / 范围: selection of in-silico Echinoidea 16S candidates; no wet-lab claims / 海胆16S计算候选筛选，不含湿实验结论。
- Authorization / 授权: user requested design and explicitly approved public release of methods, primers, references, results and scripts / 用户要求设计并明确同意全部公开。

## Recorded checks / 已记录检查

| Evidence / 证据 | Result / 结果 |
|---|---|
| Target/background accession separation | 1,401 / 6,045; no accession overlap |
| Backbone preservation | 86 unchanged rows in 1,401 × 1,813 alignment |
| Independent window fixtures | 544 checks passed |
| Ranking aggregation audit | 15 sampled pairs passed |
| Final independent all-position comparison | 170 pairs; 234,496 checks passed |
| Complete scheme risk and structure gates | 8/8 passed |
| Revalidation from published layout | PASS: revalidate.py completed; final summaries, thermodynamics and exported tables match the working analysis byte-for-byte |

Original checks: `analysis/input_audit.json`, `scanner_test_result.json`, `rank_audit.json`, `independent_validation.json`, `portfolio_qa.json`, `final_validation.json`. Local swap histories: `analysis/same_locus/exact_refinement.json`.

No p-values, confidence intervals, population-level efficacy estimates or causality claims are computed. Coverage is a descriptive weighted fraction of an in-sample eligible reference panel. Taxonomic/sequence sampling, panel exclusion and prior selection limit generalization; the 49-label common panel is not representative evidence for all Echinoidea. Exact coverage and broad mismatch risks are explicitly reported. No evidence of wet-lab validation is claimed.

本分析不计算p值、置信区间、总体实验效能或因果效应。覆盖率是发现集内可评估参考面板的描述性加权比例；分类和序列采样、片段排除及事先筛选限制外推。49标签共同面板不能代表全部海胆纲；完全匹配与放宽错配风险已单列，未宣称完成湿实验验证。
