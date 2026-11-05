# 计算评价

冻结输入、共同面板比较、内部条码唯一性与属级条件性选配测试。正式引物不变。

```sh
python3 scripts/analyze.py
python3 scripts/distances.py
python3 scripts/sensitivity.py
python3 scripts/validate.py
```

在本目录使用Python 3.10+运行。数值分析仅用标准库；绘图`python3 scripts/plot.py`另需matplotlib。inputs为冻结输入，results为结果，manifest记录输入哈希。

方法、结果和解释见主目录中英文README。窗口发现早于折分，折内候选允许局部位移且未通过正式热力学/背景筛查。同条码来源冲突保留待核查。
