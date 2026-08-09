# 实验结果证据等级与表达边界审计

- 审计日期：2026-08-09
- 审计对象：README、核心科研工作流、结果到主张、周会模板、结果—主张审计卡、真实项目接入与教学演练
- 问题编号：I-044

## 当前问题

仓库已经要求冻结协议、保留全部运行、检查替代解释并为论文主张绑定证据，也能把关键运行交给别人复查；但“当前结果能否在组会汇报、能否发给合作者、能否公开、能否支持项目决定、能否写入论文”没有统一分流。原模板中的“正式证据 / 初步观察 / 调试线索”和“允许进入位置”把证据强度、受众权限和文字用途混在一起。新手可能把单次最好结果做成组会结论，把公开可运行代码视为论文主张成立，也可能因结果尚不能写论文而不敢汇报有价值的失败与初步观察。

## 经验帖对照

- [研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e)反映按日期堆过程会导致汇报前无法快速找到问题与结果。本仓库吸收按问题、结果和下一步组织输出，但不把“结果导向”理解为只展示正向或最好结果；
- [科研习惯分享（三）：一次实验我写 3 份记录](https://www.xiaohongshu.com/explore/6612bab8000000001b013f7e)区分即时记录、个人复盘与组会表达。本仓库吸收不同受众需要不同视图，同时坚持配置、指标和运行状态只有一个主要来源，避免三份副本发生漂移；
- [知乎：深度学习实验是否可以汇报多次测试中的最高准确率](https://www.zhihu.com/en/answer/3249240394)的多个回答对最高值、均值、随机种子与 baseline 对齐方式意见不一。这种分歧本身说明个人经验不能批准报告方式；运行前协议、全部尝试和 venue 规则优先；
- [知乎：你们实验室的例会制度是怎样的](https://www.zhihu.com/question/322279340)反映例会可能停留在轮流汇报和进度比较，未形成有效建议。匿名个案只用于确认“汇报频率不等于证据审查”，不评价具体团队制度。

## GitHub 项目与正式规范对照

- [Learning Research](https://github.com/pengsida/learning_research)把做实验、写论文和 presentation 并列为科研能力，强调通过实践与交流学习，同时明确经验来自特定实验室。本仓库据此连接实验记录、组会表达和论文写作，但不照搬周频率、3D Vision 路线或个人表达模板；
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)当前提供实验运行、验证报告、误差条 / 置信区间图、人工门控和自动论文产物。它展示了阶段化产物的价值，但 pipeline 完成、自动 review 分数或 `paper.tex` 存在不能单独证明科研主张达到论文级证据；
- [AAAI-26 Reproducibility Checklist](https://aaai.org/conference/aaai/aaai-26/reproducibility-checklist/)要求区分事实、观点、假设与推测，并报告随机性、运行次数、指标和理论 / 实验证据；
- [REFORMS](https://reforms.cs.princeton.edu/)把有效性、计算可复现性、泛化总体和报告透明度分开，支持按主张类型与覆盖总体限制表达；
- [ACM Artifact Evaluation 示例](https://sigsim.acm.org/conf/pads/2024/blog/artifact-evaluation/)把 artifact 可得、功能 / 可复用和结果被另一团队复现作为不同判断，直接说明公开 artifact 不等于结论已验证；
- [Improving Reproducibility in Machine Learning Research](https://www.jmlr.org/papers/v22/20-303.html)总结 ML 报告中的选择性结果、适应性过拟合和超出证据范围的结论；
- [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)要求结果表关联精确训练与评价命令，支持共享 artifact 的执行链，但不替代具体科学主张审计。

## 适用边界

V0–V4 是本仓库的入门分流，不是期刊、会议、机构或统计学共同认可的通用等级，也不是论文质量分数。S0–S3 不构成法律、伦理、数据治理或许可证意见；正式政策与任务负责人优先。理论证明、定性研究、用户研究、临床与安全关键研究需要各自方法规范，不能机械套用计算实验字段。组会、公开、投稿和发表是不同事件；V4 不保证录用，S3 不授予复用权，独立复现也不能自动证明所有泛化主张。

## 采取行动

- 新增[实验结果证据等级与表达边界](../docs/EVIDENCE_READINESS_AND_SHARING.md)，定义 V0–V4 验证成熟度、S0–S3 共享权限、六种用途状态、受众表述、升级与降级规则；
- 新增[教学演练证据等级示例](../examples/first-workflow-drill/evidence-readiness.md)，把 debug 判为 V1、完整教学比较判为 V2，将公开可见与开放许可证、可运行 artifact 与科研主张分开；
- 升级结果—主张审计卡和已填写示例，不新增重复空白模板；
- 将证据 / 共享等级接入 README 分流、M8、周会模板、核心工作流、真实项目接入、指南与模板索引；
- 明确自动 pipeline、AI review 和论文文件首先是待审 artifact，不能自动批准 V3 / V4。

## 验证结果

- 教学演练验收通过：debug、baseline 与 candidate 三组冻结产物完整，全部计划运行完成，正式比较只改变 `learning_rate`；baseline 与 candidate 测试 accuracy 均值分别重算为 `0.840000` 与 `0.966667`；
- 仓库质量检查通过：共检查 70 个 Markdown 文件，相对链接、锚点、代码块、README 排版约束、两类索引与 51 个工具条目均通过；
- 术语一致性检查完成：验证成熟度统一使用 V0–V4，避免与产物生命周期的 `E2_EVIDENCE` 混淆；共享权限统一使用 S0–S3，六种用途状态在指南、模板和示例中一致；
- `git diff --check` 通过；远端提交与 GitHub Actions 状态将在推送后回填。

## 状态

文档实现与本地验证已完成，等待远端验证。
