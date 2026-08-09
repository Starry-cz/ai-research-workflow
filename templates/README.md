# 模板索引

按当前阶段复制模板到自己的研究仓库，不必一次使用全部模板。编号用于稳定链接，不表示必须按顺序填写。

## 最短使用路径

- **还不会运行脚本**：只填 `00`，然后阅读仓库内已填写演练；
- **正在选第一篇论文**：使用 `01 + 07 + 11`；
- **正在复现**：使用 `02 + 03`，真实数据到位后加入 `13`；
- **正在做正式实验**：使用 `04 + 14`，结果出来后使用 `15`；
- **正在投稿或回复**：使用 `09`。

`05 / 06 / 08 / 10 / 12` 是事件触发模板：只有出现组会、任务过大、算力迁移、调试求助或公式阻塞时才启用。导师、实验室或项目已有等价记录时，补齐缺失字段即可，不要维护两套重复台账。

同一时间建议只维护：一个阶段门控、一个当前任务或实验记录，以及最多一个按需卡。完成当前卡的决定和证据路径后再升级，不用为了“流程完整”提前填写未知信息。

| 模板 | 使用时机 | 完成标志 |
| --- | --- | --- |
| [00-readiness-checklist.md](00-readiness-checklist.md) | 开始科研前 | 找到当前最大能力缺口 |
| [01-research-brief.md](01-research-brief.md) | 选择方向和 baseline 时 | 问题、资源和风险边界明确 |
| [02-paper-reading-card.md](02-paper-reading-card.md) | 阅读核心论文时 | 方法与证据可以回到原文位置 |
| [03-reproduction-plan.md](03-reproduction-plan.md) | 克隆论文代码后 | 复现被拆成可验证关卡，AI 改动可审计 |
| [04-experiment-card.md](04-experiment-card.md) | 每次运行正式实验前 | 问题、运行模式、重复运行、选择规则和停止条件明确 |
| [05-weekly-review.md](05-weekly-review.md) | 每周、组会或阶段结束时 | 证据、反馈、决策和下一步已记录 |
| [06-daily-task-card.md](06-daily-task-card.md) | 每次开始独立学习或科研会话前 | 主任务、产物、验收、时间盒和停止条件明确 |
| [07-literature-search-log.md](07-literature-search-log.md) | 开始新方向检索或扩展核心论文集合时 | 关键词、查询、去重、版本和停止依据可追踪 |
| [08-compute-data-environment-checklist.md](08-compute-data-environment-checklist.md) | 使用实验室服务器、云 GPU 或迁移大数据前 | 干净安装、短试跑、恢复测试、预算和结果导出均有记录 |
| [09-submission-review-archive.md](09-submission-review-archive.md) | 投稿、作者回复、拒稿转投或录用归档时 | 规则、送审版本、评审问题、回复证据和版本链均可追溯 |
| [10-debug-help-request.md](10-debug-help-request.md) | 环境、代码、数据或研究流程卡住并准备求助时 | 问题、环境、命令、最小复现、排查记录和求助对象明确 |
| [11-first-baseline-gate.md](11-first-baseline-gate.md) | 从教学演练进入首篇真实论文前 | 候选经过低成本预检，目标、预算、停止与备选路径明确 |
| [12-math-concept-card.md](12-math-concept-card.md) | 公式阻塞论文理解、实现或实验判断时 | 符号、shape、假设、玩具数值与代码实现能够相互核对 |
| [13-dataset-card.md](13-dataset-card.md) | 下载、生成或接收数据后，运行 baseline 前 | 来源与权利明确，版本可识别，划分和处理可重建，泄漏与隐私风险有结论 |
| [14-evaluation-spec.md](14-evaluation-spec.md) | 设计实验且尚未查看最终测试结果时 | 主指标、实现、聚合、阈值、统计单位、不确定性和决策规则已冻结 |
| [15-result-claim-audit.md](15-result-claim-audit.md) | 实验完成后、制作论文图表或写结论前 | 结果完整，错误与反例已检查，图表可重建，主张不超过证据 |

第一次不知道这些字段如何衔接时，先完成[第一次可审计实验演练](../examples/first-workflow-drill/README.md)。
