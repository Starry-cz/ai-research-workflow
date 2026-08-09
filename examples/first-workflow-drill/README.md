# 第一次可审计实验演练

这是一个面向零基础读者的工作流演练。它用 Python 标准库训练一个极小的二分类模型，帮助你看懂一次实验如何从问题、配置和命令走到日志、指标与有限结论。

> 这里使用固定生成的合成数据，没有论文、真实业务数据或新方法。运行结果只能证明这条教学链路在记录的环境中执行过，不能证明论文复现成功、算法具有创新性或模型能够泛化到真实任务。

## 你会留下什么

```text
问题与边界
  → 两份只改变学习率的配置
  → 预先声明的 seed 集合
  → 每个 seed 的完整结果
  → 汇总指标与运行环境
  → 采用、回退或继续探索的决定
```

运行后，每个输出目录都包含：

- `config.snapshot.json`：实际读取的配置快照；
- `environment.json`：Python、平台和执行命令；
- `metrics.json`：全部计划运行、汇总值和状态；
- `run.log`：便于人工阅读的运行日志。

仓库已经保存一份实际运行产物，便于在运行前查看证据链的形状。你自己的运行必须写入新目录，不能覆盖示例结果。

## 1. 先读数据卡和实验卡

先打开[已填写数据集卡](dataset-card.md)，确认 180 条样本由仓库脚本确定性生成、三组按索引固定切分、没有外部个人数据，并且这份合成数据不能代表真实任务。再查看[已填写评价协议](evaluation-spec.md)，理解这里为什么报告 accuracy 与 loss、如何跨 seed 汇总，以及为什么总体标准差不是置信区间。

再打开[已填写实验卡](experiment-card.md)。重点检查：

- 本轮问题只是比较同一教学脚本中的两个学习率设置；
- 学习率是练习用变量，不被包装成科研贡献；
- 两组使用相同数据、epoch、seed 和选择规则；
- 在看结果前已经声明运行集合和停止条件；
- 单个最好结果不能代替全部运行的汇总。

## 2. 创建独立环境

该脚本只使用 Python 标准库，建议使用 Python 3.10 或更高版本。先在此目录创建并激活独立环境，再记录版本：

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS 或 Linux 的激活命令不同，应以所用 shell 和 Python 官方文档为准。`.venv` 不应提交到 Git。

## 3. 运行基线和候选设置

先用单一固定 seed 做调试运行，再执行预先声明的比较。请为自己的结果使用新的输出目录：

```powershell
python train.py --config configs/debug.json --output-dir results/my-debug
python train.py --config configs/baseline.json --output-dir results/my-baseline
python train.py --config configs/candidate.json --output-dir results/my-candidate
```

`debug.json` 只运行很少的 epoch，用来确认参数读取、训练、评价和写文件链路；它不进入 baseline 与 candidate 的正式比较。

脚本拒绝覆盖非空输出目录。需要重跑时创建新的 `run_id` 和目录，保留旧结果及其失败原因。

## 4. 按顺序核验

1. 检查调试运行是否生成四类产物，再确认两组比较实验的所有计划 seed 均为 `completed`；
2. 打开两组 `config.snapshot.json`，确认只有 `experiment_id` 与 `learning_rate` 不同；
3. 打开 `metrics.json`，确认 `runs` 中没有只保留最高分；
4. 核对 `environment.json` 中的命令、Python 与平台；
5. 将结果填回[实验卡](experiment-card.md)，再选择 `PROCEED / REFINE / PIVOT / STOP`。

如果运行失败，不要删除目录。保留首个关键报错，并使用[调试与求助卡](../../templates/10-debug-help-request.md)记录完整命令、环境、预期和实际行为。

## 5. 正确解释这个结果

可以写：

> 在记录的 Python 环境、固定合成数据、相同训练轮数和预先声明的 seed 集合下，候选配置与基线的结果见对应 `metrics.json`。本演练仅验证记录和比较流程。

不能写：

> 更高学习率普遍优于其他方法，已经证明一种新的训练策略。

原因是本例没有真实数据、代表性任务、独立调参协议或足以支持泛化主张的评价设计。

## 6. 迁移到真实论文复现

完成演练后，先使用[首篇真实 baseline 准入卡](../../templates/11-first-baseline-gate.md)比较两到三个候选，再把同一条证据链迁移到真实项目：

| 演练字段 | 真实项目中的对应内容 |
| --- | --- |
| [合成数据集卡](dataset-card.md) | 数据来源、许可证或条款、版本、校验值、字段、质量、划分与风险 |
| `train.py` | 锁定 commit 的官方训练与评测入口 |
| 两份 JSON 配置 | baseline 与候选方法的版本化配置 |
| seed 集合 | 按任务波动、预算和 venue 规则预先确定的重复运行 |
| `metrics.json` | 可定位到日志、checkpoint、图表和评价脚本的结果 |
| 教学边界声明 | 论文中的限制、失败案例与结论适用范围 |

真实复现还必须核对论文版本、官方仓库、数据预处理、预训练权重、评价协议、硬件差异和复现容差；本演练没有替代这些步骤。
