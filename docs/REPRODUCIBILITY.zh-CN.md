# 重现说明

原始 32 对不分分类群引物为主方案，FASTA 和 CSV 位于 `sequences/non_partitioned.*`；76 对分类群限定候选为补充方案，记录于 `results/catalog.json`。发布检查会核对主方案与归档 v1.2 的序列、表格和名称对照。

运行 `python scripts/revalidate.py --thermal` 重算补充候选的冻结参考库配对和热力学筛选；运行 `python scripts/check_background_sample.py --full` 以独立实现复核完整背景库的严格 WC／GT 命中；运行 `python check_release.py` 检查主、补充方案及文件校验和。完整环境及命令见[英文重现说明](REPRODUCIBILITY.md)。

以上复核使用现有参考库，不代表独立外部样本或湿实验验证，也不宣称重跑全局最优设计。
