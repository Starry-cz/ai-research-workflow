# EXP-000 实验卡

## 1. 实验问题

- 运行模式：debug / pilot / confirmatory
- baseline 稳定化门：[11-first-baseline-gate.md](11-first-baseline-gate.md)
- 稳定化决定：READY_FOR_CHANGE / 其他状态不得进入方法比较
- 研究假设：
- 本轮唯一主要问题：
- 可检验预测：
- 替代解释：

## 2. 实验设计

- 评价协议：[14-evaluation-spec.md](14-evaluation-spec.md)
- baseline：
- 论文目标值与协议：
- 本地 baseline commit 与 run IDs：
- 本地 baseline 与论文目标的差距及边界：
- 唯一主要改动：
- 安全改码记录：[SAFE_FIRST_CODE_CHANGE.md](../docs/SAFE_FIRST_CODE_CHANGE.md)
- base commit、改动 commit 与分支：
- 改动类别与准入决定：RESEARCH_CHANGE + SAFE_FOR_PILOT / 其他状态不得进入 pilot
- 修改前后检查命令与证据位置：
- 科学变量：
- 干扰变量：
- 固定变量：
- 对照组：
- 数据与划分：
- 主指标与辅助指标：
- 统计单位与实际意义门槛：
- 预先计划的 run_id 与随机种子：
- 公平调参与搜索预算：[FAIR_TUNING_BUDGET.md](../docs/FAIR_TUNING_BUDGET.md)
- 调参协议 / study ID：
- 科学变量、共享干扰超参数与方法特有超参数：
- baseline 搜索空间、trial 上限与默认值来源：
- 候选搜索空间、trial 上限与新增参数理由：
- 总搜索预算、各方法预算与确认预算：
- 搜索算法、版本、随机状态与人工介入：
- 早停、剪枝、失败与边界扩展规则：
- 验证选择指标、并列与最终配置冻结规则：
- 全部 trial 台账路径：
- 测试集访问与测试后变更规则：
- 公平性决定：FAIR_TO_COMPARE / RE-TUNE_BASELINE / REDESIGN_SEARCH / EXPLORATORY_ONLY / STOP_BUDGET
- checkpoint / 模型选择规则：
- 结果汇总方式与波动来源：
- 预算：
- 停止门指南：[RESEARCH_STOPPING_AND_PIVOT.md](../docs/RESEARCH_STOPPING_AND_PIVOT.md)
- 复查触发器：最大 trial / 成本 / 日期 / 关键反证 / 风险：
- 支持、有效负结果与证据不足的预设判据：
- 停止条件与重开触发器：
- 产物生命周期指南：[EXPERIMENT_ARTIFACT_LIFECYCLE.md](../docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)
- pilot 升级到代表性规模的条件：
- 失败判定：
- 运行排除规则：

## 3. 版本与环境

- 代码 commit：
- 配置文件：
- 数据版本：
- 环境文件：
- GPU / CPU / 内存：
- 运行命令：

## 4. 运行前检查

- [ ] baseline 已取得 `READY_FOR_CHANGE`，证据与允许主张明确
- [ ] 本地 baseline 没有混入未审计的研究改动
- [ ] 修复、重构、观测和研究方法改动已经分离
- [ ] 已逐文件审查 diff，且最低检查覆盖本轮主要改动
- [ ] AI 生成的研究相关代码能够由作者解释，新增 API 与依赖已核验
- [ ] pilot 结果不会被直接当成完整协议结论
- [ ] 训练、验证、测试用途分离
- [ ] 除主要变量外的设置保持公平
- [ ] baseline 与候选的搜索机会、范围和成本已经审计
- [ ] pilot、剪枝、失败、中断和人工调整都进入 trial 台账
- [ ] 最终配置只根据允许的验证信息选择并已冻结
- [ ] seed、重复运行集合和选择规则在看结果前写定
- [ ] 每项计划尝试都说明将区分什么解释，以及不同结果如何改变决定
- [ ] 复查触发器、顶层决定和停止原因码已在运行前定义
- [ ] 输出目录不会覆盖已有结果
- [ ] 日志、配置和 checkpoint 会被保存
- [ ] 产物已按临时 / 恢复 / 证据 / 归档 / 受限分类，并声明负责人和首次复查日

## 5. 结果

- 主结果：
- 全部计划运行及状态：
- 中心趋势、离散程度或区间：
- 波动来源与计算方式：
- 训练与验证曲线：
- baseline / 候选的计划、完成、剪枝、失败与排除 trial 数：
- baseline / 候选的搜索与确认计算成本：
- 最终配置、冻结 commit 与选择证据：
- 测试结果可见后的所有变更：
- 运行时间、显存和吞吐量：
- 失败、中断与排除运行及理由：
- 产物位置、分类、大小、负责人、平台 TTL 与复查日：
- 生命周期决定：KEEP_ACTIVE / ARCHIVE_IMMUTABLE / PRUNE_BINARY_KEEP_RECORD / HOLD_RESTRICTED / REVIEW_REQUIRED
- 异常与失败案例：
- 与 baseline 的差异：
- pilot 到代表性规模：保持 / 减弱 / 反转 / 未检查
- 候选收益是否仍低于论文目标，以及这对当前主张的影响：

### 有信息增量的尝试台账

| attempt_id | 唯一新增信息与预测 | 改动 / 固定项 | 证据与成本 | 结果类别 | 已排除解释与决定影响 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | INVALID_RUN / VALID_NEGATIVE / INCONCLUSIVE / POSITIVE_BOUNDED / RISK_OR_POLICY_STOP |  |

## 6. 结论与决策

- 结果—主张审计：[15-result-claim-audit.md](15-result-claim-audit.md)
- 假设得到支持 / 部分支持 / 不支持：
- 证据：
- 无法排除的替代解释：
- 结论适用边界：
- 决策：PROCEED / REFINE / PIVOT / STOP
- 原因码：CONFIRMATORY_READY / NEXT_MILESTONE_READY / INVALID_PROTOCOL / SCOPE_TOO_BROAD / ONE_DISCRIMINATING_TEST / HYPOTHESIS_REFUTED / BASELINE_UNSUITABLE / EXTERNAL_CONSTRAINT_CHANGED / ANSWERED / BUDGET / RISK / NO_DISCRIMINATING_TEST
- 为什么下一项实验会新增可区分信息，或为什么不存在这样的实验：
- 已用 / 剩余预算与闭环可行性：
- 停止对象、保留证据与重开触发器：
- 下一轮唯一问题：
