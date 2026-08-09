# 教学演练运行交接卡

这是[第一次可审计实验演练](README.md)的已填写交接示例，不是论文或真实数据实验。

## 1. 交接范围

- 项目与唯一入口：本目录 [README](README.md)
- 交接人 / 接收者：仓库维护者 / 未接触维护者本地结果的复查者
- 日期与用途：2026-08-09；验证另一目录能否定位、重算并最小复跑教学链路
- 声明深度：`H2_REPLAY`
- 当前一句话结论：记录的三组教学产物完整，baseline 与 candidate 只改变学习率；该证据只验证工作流，不支持方法优越性主张。
- 当前决定：`PROCEED`，进入真实 baseline 筛选，而不是继续优化合成任务。
- 未解决问题与主张边界：未使用真实数据、论文协议或代表性算力，不能推广到任何真实任务。

## 2. 主要来源映射

| 对象 | 唯一来源或稳定 ID | 身份 / 版本 | 访问状态与负责人 |
| --- | --- | --- | --- |
| 代码 | `train.py`、`verify.py` | Git commit `ad6538378ff9c15a744d13ecfd9c17e1afc9de15` | 公开仓库 |
| 环境 | `environment.json` 与本页命令 | Python 3.10+，仅标准库 | 公开，无额外依赖 |
| 数据与 split | [数据集卡](dataset-card.md) | 由 `train.py` 固定生成；180 条；索引划分 | 无外部数据 |
| 配置 | `configs/*.json` | debug / baseline / candidate | 公开仓库 |
| 关键运行 | `teaching-debug-001`、`teaching-baseline-001`、`teaching-candidate-001` | 全部 `completed` | 公开仓库 |
| 日志 | `results/*-recorded/run.log` | 与对应 run ID 一致 | 公开仓库 |
| 产物 | `results/*-recorded/` | 每组含配置、环境、指标和日志 | `E2_EVIDENCE`；见[生命周期台账](artifact-lifecycle.md) |
| 指标与图表 | `verify.py`、`metrics.json` | accuracy 与 loss；按 seed 汇总 | 公开仓库 |
| 决策记录 | [实验卡](experiment-card.md)、[结果—主张审计](result-claim-audit.md) | 2026-08-09 | 公开仓库 |

## 3. 最小复查入口

- 起始目录：仓库根目录下 `examples/first-workflow-drill`
- 检出：`git checkout ad6538378ff9c15a744d13ecfd9c17e1afc9de15`
- 环境：使用 Python 3.10+ 的独立环境；脚本没有第三方依赖
- 允许共享资产：全部输入由脚本生成，不需要账号、密钥或下载
- 平台 TTL / 服务器回收日：不适用；记录产物由 Git 跟踪
- 生命周期决定：`ARCHIVE_IMMUTABLE`
- 已有产物核验：

```powershell
python verify.py `
  --debug-dir results/debug-recorded `
  --baseline-dir results/baseline-recorded `
  --candidate-dir results/candidate-recorded
```

- 预期信号：第一行以 `PASS` 开头；baseline accuracy 均值为 `0.840000`，candidate 为 `0.966667`
- 容差：验收脚本从每个 seed 重算汇总并使用脚本内数值容差；不要求跨平台逐位复现训练轨迹
- 最小复跑：在本目录执行以下命令；输出目录必须是新目录

```powershell
python train.py --config configs/debug.json --output-dir results/handoff-debug
python train.py --config configs/baseline.json --output-dir results/handoff-baseline
python train.py --config configs/candidate.json --output-dir results/handoff-candidate
python verify.py `
  --debug-dir results/handoff-debug `
  --baseline-dir results/handoff-baseline `
  --candidate-dir results/handoff-candidate
```

- 停止条件：debug 失败或超过一分钟时停止，不启动正式两组

## 4. 维护者冷启动记录

- 实际目录 / 机器：Windows 临时空目录，与工作区结果目录分离
- 实际 commit：`ad6538378ff9c15a744d13ecfd9c17e1afc9de15`
- 是否依赖口头修正：否
- H0 查找结果：通过
- H1 指标核验：通过
- H2 最小复跑：通过
- H3 接管准备：不适用
- 实际值：baseline `0.840000`，candidate `0.966667`
- 实际耗时：三组运行加验收共约 1.129 秒；普通 CPU 上为秒级，不作为性能保证
- 缺失入口、权限或过期引用：未发现
- 复查证据：[运行交接审计](../../reports/RUN_HANDOFF_AUDIT_2026-08-09.md)

## 5. 交接决定

- 最终状态：`HANDOFF_READY`
- 状态证据：空目录可以仅按仓库入口运行三组配置并通过自动验收
- 下一次复查触发条件：修改 `train.py`、`verify.py`、配置、记录产物或最低 Python 边界后重新执行
