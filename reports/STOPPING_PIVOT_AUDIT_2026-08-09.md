# 负结果、无进展与研究停止门审计

- 审计日期：2026-08-09
- 审计对象：README、核心工作流、实验卡、每周复盘、结果—主张审计和第一次工作流演练
- 问题编号：I-045

## 当前问题

仓库已经使用 `PROCEED / REFINE / PIVOT / STOP`，也要求记录预算、失败和停止条件，但没有统一说明什么是无效运行、有效负结果或证据不足，也没有要求继续实验必须增加能够改变决定的信息。零基础读者可能把环境 / 数据 / 指标错误写成“方法失败”，看到一次不提升就过早放弃，或在测试结果可见后无限更换参数、seed 和切片。固定次数同样不能解决问题：不同任务成本、波动、风险和证据门槛不同。

## 经验帖对照

- [科研探索目的下 Codex 老在奇怪的地方使劲](https://www.xiaohongshu.com/explore/6a76af7d000000002500743e)反映 AI 容易把科研任务扩张为过度实现；本仓库用唯一问题、最大范围和信息增量约束继续运行，不把单个工具体验外推到所有 AI；
- [跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)反映环境、数据、评价和方法失败容易混淆；本仓库先判协议有效性，再判断假设；
- [研一暑假做实验才发现，数据管理比调参更重要](https://www.xiaohongshu.com/explore/6a5f37be00000000110120f5)反映数据版本、划分和设置缺失会造成反复核对；本仓库要求停止决定回到唯一证据入口；
- [研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e)反映流水记录难以汇总；本仓库按问题、尝试、证据和决定组织，同时保留全部失败与负结果；
- [知乎：负面结果怎么写？让失败实验也有发表价值](https://zhuanlan.zhihu.com/p/1973701811283195210)可用于确认“负结果”和“失败实验”常被混用；它是二手经验内容，不用于定义统计结论或发表门槛；
- [知乎：我的博士生已经半个月没主动联系我了，怎么能让他更主动一点？](https://zhuanlan.zhihu.com/p/2058886370387571300)反映长期卡住时问题可能没有及时转成可讨论证据；个人导师经验不规定统一汇报频率或停止次数。

## GitHub 项目与正式规范对照

- [Learning Research](https://github.com/pengsida/learning_research/blob/master/getting_advanced_in_research.md)把分析实验为何不工作和实验记录列为实验能力。本仓库吸收“失败也要分析和记录”，不照搬特定实验室的研究方向或成长安排；
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)展示阶段化决定、人工门控、版本化产物、迭代上限和费用保护。本仓库吸收门控、预算和暂停机制，但不把其固定轮数或金额写成普适标准，也不允许自动批准关键科研停止决定；
- [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook)讨论有限预算、试验 / 搜索 / 数据方差、训练曲线诊断和改进收益与复杂度。本仓库据此审计边际信息和公平搜索，但不规定统一 trial 数；
- [Position: Embracing Negative Results in Machine Learning](https://arxiv.org/abs/2406.03980)区分新方法未获支持与复现 / 失败模式类负结果，并强调排除实现质量问题；该文是立场论文，其术语不能替代具体统计设计；
- [ORI：Selective Reporting of Results](https://ori.hhs.gov/selective-reporting-results)要求遵守预先计划，并披露和解释事后分析、异常值处理与方法改变；
- [Fostering Integrity in Research](https://www.ncbi.nlm.nih.gov/books/NBK475939/)讨论不发表负结果和只保留正结果造成的偏差，并指出负结果可帮助发现方法缺陷、避免无效重复。

## 适用边界

停止门管理一个明确问题、假设或实验族，不评价个人能力、学业、职业或整个学科方向。`VALID_NEGATIVE` 不等于证明零效应；等价、非劣、因果和安全结论需要对应设计。固定 review 次数、成本和阈值应由任务、团队、领域和资源决定。理论、定性、用户研究、临床和安全关键研究需要各自规范。机构政策、任务负责人、数据权利方和目标 venue 的当前规则优先。

## 采取行动

- 新增[负结果、无进展与研究停止门](../docs/RESEARCH_STOPPING_AND_PIVOT.md)，定义五类结果、有信息增量的尝试、复查触发器、五个停止门、四类决定与原因码；
- 扩展实验卡、周复盘和结果—主张审计，不新增重复模板；
- 新增[教学演练停止决定](../examples/first-workflow-drill/stopping-decision.md)，基于现有真实产物作出 `STOP + ANSWERED`，演示成功后也应关闭当前实验族；
- 将停止门接入 README 分流、能力里程碑、核心工作流、指南索引和模板索引；
- 明确停止不删除证据，转向要冻结旧问题，重开必须由新证据或条件变化触发。

## 验证结果

- 教学演练验收通过：debug、baseline 与 candidate 三组产物完整，全部计划运行完成，正式比较只改变 `learning_rate`；baseline 与 candidate 测试 accuracy 均值分别重算为 `0.840000` 与 `0.966667`；
- 仓库质量检查通过：共检查 73 个 Markdown 文件，相对链接、锚点、代码块、README 排版约束、两类索引与 51 个工具条目均通过；
- 术语检查完成：结果类别统一为五类，顶层决定统一使用 `PROCEED / REFINE / PIVOT / STOP`，具体依据统一放在原因码中；
- `git diff --check` 通过；
- Git 提交、远端推送与 GitHub Actions 待完成后回填。

## 状态

本地实现与回归已完成，等待远端验证。
