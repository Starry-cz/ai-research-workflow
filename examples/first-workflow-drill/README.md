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

先打开[已填写任务授权边界](task-authority.md)，确认哪些本地运行可以直接做、哪些改码和提交必须先确认、哪些数据与材料不得进入演练。再打开[已填写数据集卡](dataset-card.md)，确认 180 条样本由仓库脚本确定性生成、三组按索引固定切分、没有外部个人数据，并且这份合成数据不能代表真实任务。随后查看[已填写评价协议](evaluation-spec.md)，理解这里为什么报告 accuracy 与 loss、如何跨 seed 汇总，以及为什么总体标准差不是置信区间。

再打开[已填写实验卡](experiment-card.md)。重点检查：

- 本轮问题只是比较同一教学脚本中的两个学习率设置；
- 学习率是练习用变量，不被包装成科研贡献；
- 两组使用相同数据、epoch、seed 和选择规则；
- 在看结果前已经声明运行集合和停止条件；
- 单个最好结果不能代替全部运行的汇总。

## 2. 进入目录并创建独立环境

该脚本只使用 Python 标准库，建议使用 Python 3.10 或更高版本。先从仓库根目录进入演练目录；下面直接调用虚拟环境中的解释器，不依赖 shell 激活状态。

Windows PowerShell：

```powershell
Set-Location examples/first-workflow-drill
python --version
python -m venv .venv
.\.venv\Scripts\python.exe --version
```

macOS / Linux（bash 或 zsh）：

```bash
cd examples/first-workflow-drill
python3 --version
python3 -m venv .venv
./.venv/bin/python --version
```

如果第二次版本检查失败，不要改用另一个随机解释器继续运行；先回到[L0 工具链起步指南](../../docs/L0_TOOLCHAIN_START.md)核对解释器路径和 `venv`。`.venv` 已被 `.gitignore` 排除，不应提交到 Git。

## 3. 运行基线和候选设置

先用单一固定 seed 做调试运行，再执行预先声明的比较。请为自己的结果使用新的输出目录。

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe train.py --config configs/debug.json --output-dir results/my-debug
.\.venv\Scripts\python.exe train.py --config configs/baseline.json --output-dir results/my-baseline
.\.venv\Scripts\python.exe train.py --config configs/candidate.json --output-dir results/my-candidate
```

macOS / Linux：

```bash
./.venv/bin/python train.py --config configs/debug.json --output-dir results/my-debug
./.venv/bin/python train.py --config configs/baseline.json --output-dir results/my-baseline
./.venv/bin/python train.py --config configs/candidate.json --output-dir results/my-candidate
```

`debug.json` 只运行很少的 epoch，用来确认参数读取、训练、评价和写文件链路；它不进入 baseline 与 candidate 的正式比较。

三条命令在普通 CPU 上通常应在较短时间内结束。本仓库维护者在 Windows、Python 3.11.2 环境中的一次核验总耗时约 0.83 秒；这只是环境记录，不是性能保证。如果调试命令持续超过一分钟，先中断并检查解释器、当前目录和首个报错，不要继续启动后两组。

脚本拒绝覆盖非空输出目录。需要重跑时创建新的 `run_id` 和目录，例如 `my-debug-02`，保留旧结果及其失败原因。个人运行产生的 `results/*` 默认被演练目录的 `.gitignore` 排除，仓库自带的三个 `*-recorded` 目录除外。

## 4. 按顺序核验

1. 检查调试运行是否生成四类产物，再确认两组比较实验的所有计划 seed 均为 `completed`；
2. 打开两组 `config.snapshot.json`，确认只有 `experiment_id` 与 `learning_rate` 不同；
3. 打开 `metrics.json`，确认 `runs` 中没有只保留最高分；
4. 核对 `environment.json` 中的命令、Python 与平台；
5. 将结果填回[实验卡](experiment-card.md)，使用[已填写结果—主张审计](result-claim-audit.md)检查反例和结论边界，查看[证据等级与共享判断](evidence-readiness.md)区分公开教学 artifact 与科研主张，再参考[已填写停止决定](stopping-decision.md)选择 `PROCEED / REFINE / PIVOT / STOP` 及原因码。

如果运行失败，不要删除目录。保留首个关键报错，并使用[调试与求助卡](../../templates/10-debug-help-request.md)记录完整命令、环境、预期和实际行为。

[已填写上游路由示例](upstream-routing.md)进一步演示：把输出写到已有 `debug-recorded` 目录会触发文档明确的防覆盖异常，因此应修正个人命令，不应仅因出现 traceback 就提交上游 Issue。

### 成功标志

每个新输出目录都应存在四个文件，且命令正常退出：

```text
config.snapshot.json
environment.json
metrics.json
run.log
```

打开 `metrics.json`，调试目录应有一项运行，baseline 与 candidate 应包含配置中预先声明的全部 seed，且状态为 `completed`。文件存在但运行状态失败，不算完成。

完成三组运行后，用自动验收脚本一次检查文件、seed、状态、汇总重算、数据一致性和唯一主要变量。

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe verify.py `
  --debug-dir results/my-debug `
  --baseline-dir results/my-baseline `
  --candidate-dir results/my-candidate
```

macOS / Linux：

```bash
./.venv/bin/python verify.py \
  --debug-dir results/my-debug \
  --baseline-dir results/my-baseline \
  --candidate-dir results/my-candidate
```

成功时第一行以 `PASS` 开头；失败时第一行以 `FAIL` 开头并说明首个未通过规则。验收通过只证明教学证据链完整，不证明候选设置或方法普遍更优。

如果你想检查“另一人能否只根据一个入口复查”，打开[已填写运行交接卡](run-handoff.md)。它把已有产物的指标核验与空目录重新运行分开，并记录 H2 冷启动结果；真实项目应按用途选择 H0–H3，不必每次重跑完整训练。

[已填写产物生命周期台账](artifact-lifecycle.md)进一步说明为什么仓库内三组记录结果属于结论证据，而个人练习输出和冷启动临时副本不能被同样处理。它示范按用途决定保留，不按分数高低或文件年龄直接删除。

[已填写反馈闭环](feedback-loop.md)演示如何把“另一人真的能复查吗”和“分数更高能否声称方法更好”两项审阅问题，分别关闭为新增证据与收缩主张。示例来自仓库审计，不伪装成真实导师意见。

[已填写证据等级与共享判断](evidence-readiness.md)把调试运行判为 V1、完整教学比较判为 V2，并将公开状态写为 S3 `PUBLIC_VIEWABLE`。它同时说明：公开可见不代表已有开放许可证，教学 artifact 可重算也不代表方法主张达到 V3 / V4。

### 常见失败与下一步

| 现象 | 先检查什么 |
| --- | --- |
| 找不到 `python`、`python3` 或虚拟环境解释器 | 回到 L0 指南核对安装与真实解释器路径，不混用多个 Python。 |
| 找不到 `train.py` 或 `configs/...` | 运行 `Get-Location`（PowerShell）或 `pwd`（macOS/Linux），确认当前目录是 `first-workflow-drill`。 |
| 输出目录已存在或非空 | 不覆盖旧证据；改用带序号的新目录。 |
| 命令退出但结果状态不是 `completed` | 先读 `run.log` 和 `metrics.json` 中的失败项，再填写调试卡。 |
| 想从头重跑 | 保留需审计的旧目录；仅对自己创建且确认无保留价值的目录做清理，然后使用新的 `run_id`。不要改动三个 `*-recorded` 示例目录。 |

## 5. 正确解释这个结果

可以写：

> 在记录的 Python 环境、固定合成数据、相同训练轮数和预先声明的 seed 集合下，候选配置与基线的结果见对应 `metrics.json`。本演练仅验证记录和比较流程。

不能写：

> 更高学习率普遍优于其他方法，已经证明一种新的训练策略。

原因是本例没有真实数据、代表性任务、独立调参协议或足以支持泛化主张的评价设计。

## 6. 迁移到真实论文复现

完成演练后，先使用[首篇真实 baseline 准入卡](../../templates/11-first-baseline-gate.md)比较两到三个候选，再按[真实代码库最小接入](../../docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)盘点上游结构和现有台账，把同一条证据链映射到真实项目，而不是复制整套示例目录：

| 演练字段 | 真实项目中的对应内容 |
| --- | --- |
| [合成数据集卡](dataset-card.md) | 数据来源、许可证或条款、版本、校验值、字段、质量、划分与风险 |
| `train.py` | 锁定 commit 的官方训练与评测入口 |
| 两份 JSON 配置 | baseline 与候选方法的版本化配置 |
| seed 集合 | 按任务波动、预算和 venue 规则预先确定的重复运行 |
| `metrics.json` | 可定位到日志、checkpoint、图表和评价脚本的结果 |
| 教学边界声明 | 论文中的限制、失败案例与结论适用范围 |

真实复现还必须核对论文版本、官方仓库、数据预处理、预训练权重、评价协议、硬件差异和复现容差；本演练没有替代这些步骤。
