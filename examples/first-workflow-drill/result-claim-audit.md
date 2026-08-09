# 教学演练结果—主张审计

## 1. 分析快照

- analysis_id：`ANALYSIS-DEMO-001`
- 实验：[experiment-card.md](experiment-card.md)
- 数据卡：[dataset-card.md](dataset-card.md)
- 评价协议：[evaluation-spec.md](evaluation-spec.md)
- 配置：`configs/baseline.json` 与 `configs/candidate.json`
- 结果：`results/baseline-recorded/` 与 `results/candidate-recorded/`
- 计划运行：两组各 5 个 seed，共 10 次，均为 `completed`
- 分析限制：当前结果只保存逐 seed 汇总，没有逐样本预测，因此不能完成配对样本错误分析
- 证据与共享判断：[evidence-readiness.md](evidence-readiness.md)

## 2. 结果完整性

- [x] 全部计划 seed 有状态
- [x] 没有失败或排除运行
- [x] 两组使用相同数据、epoch、seed、模型和评价
- [x] 指标可由 `metrics.json` 与脚本中的汇总逻辑核对
- [x] README、实验卡与结果目录使用同一记录结果
- [x] 没有根据测试结果继续搜索学习率

当前结果可以作为工作流演练证据，不能作为真实方法比较证据。

## 3. 证据等级与共享边界

- 本次输出：公开仓库中的教学结果包与限定说明；
- 验证等级：V2 `AUDITABLE_RESULT`；全部计划运行可追溯、可重算，但没有真实研究问题与代表性任务；
- 共享等级：S3 `PUBLIC_VIEWABLE`；只使用脚本生成数据且已经公开，但仓库尚未确认许可证，公开可见不等于可自由复用；
- 允许表述：两组教学配置在固定协议下完成，记录数值可从冻结结果重算；
- 禁止表述：学习率 `0.4` 普遍更优，或这组结果构成新方法；
- 用途状态：`SHAREABLE_ARTIFACT_ONLY`；
- 降级触发：脚本、配置、数据生成、评价、记录产物或 README 数字发生变化。

## 4. 观察、反例与替代解释

- 协议内观察：baseline 测试 accuracy 为 `0.840000 ± 0.013333`，candidate 为 `0.966667 ± 0.000000`；这里的 `±` 是五个计划 seed 的总体标准差
- 反例：baseline 的 seed 71 达到 `0.866667`，其他四次为 `0.833333`，说明单个运行不能代表该配置
- 无法完成：没有逐样本预测，不能判断 candidate 修复和破坏了哪些样本
- 替代解释：候选差异可能只来自这条简单标签规则、固定 epoch、两个学习率和五个初始化
- 未覆盖：真实噪声、不同数据、模型、资源、阈值、统计总体与外部复现

## 5. 主张—证据台账

### CLAIM-DEMO-001

- 精确表述：两份预先声明的配置在同一教学协议下完成了全部计划运行，并保存了配置、环境、日志和指标
- 类型：协议内观察
- 证据：两组记录结果目录与[实验卡](experiment-card.md)
- 状态：`verified`
- 允许进入：教学 README

### CLAIM-DEMO-002

- 原表述候选：学习率 `0.4` 普遍优于 `0.1`
- 类型：泛化 / 方法比较
- 反证与缺口：只有一个合成数据生成规则、一个模型、固定预算和五个初始化；没有实际意义门槛、独立数据或逐样本分析
- 状态：`rejected`
- 允许进入：只能作为禁止主张的反例

### CLAIM-DEMO-003

- 限定表述：在当前固定合成数据、80 epoch、五个预先声明 seed 和阈值 `0.5` 下，candidate 的记录测试 accuracy 均值高于 baseline
- 类型：协议内观察
- 证据：两组 `metrics.json`
- 状态：`qualified`
- 允许进入：实验说明，必须与限制同时出现

## 6. 图表与下一步

- 本演练没有生成论文图表，不得根据手工截图创建方法优越性图片
- 迁移真实项目前应保存逐样本预测、样本 ID、标签、分数和错误类别，以支持配对分析
- 结果类别：`POSITIVE_BOUNDED`；教学预测在冻结协议内达到，不代表科研方法得到支持
- 无效 / 负结果边界：当前没有失败运行或有效负结果；未来命令、数据或评价失效必须记为 `INVALID_RUN`，不能用于反驳方法
- 决策：当前教学实验族 `STOP + ANSWERED`；主工作流 `PROCEED + NEXT_MILESTONE_READY` 到资料完整的真实 baseline
- 下一项实验：不再搜索本合成任务学习率；真实 baseline 将建立新的问题、预算和评价协议
- 重开触发器：脚本、数据生成、配置、评价、验收或冻结记录发生变化
- 证据：[已填写停止决定](stopping-decision.md)
