# 真实代码库最小接入审计（2026-08-09）

## 审计目标

检查零基础读者完成教学演练、拿到导师仓库或官方论文代码后，能否在不重构上游、不复制全部模板、不维护重复台账的前提下建立第一条真实证据链。

## 审计发现

仓库已经提供模板最短路径和渐进式项目结构，也提醒“已有等价记录时直接复用”。但这些是原则，不是接入步骤。读者仍无法确定：

- 应该 fork、直接 clone、修改上游 README，还是另建研究仓库；
- 原项目已有 README、tracker、组会表格时，模板字段放在哪里；
- 哪些文件可以移动，哪些应保持上游结构；
- Notebook、实验室成熟仓库和只读服务器目录是否采用同一方案；
- 第一次接入做到什么程度才算完成；
- 什么时候才需要复杂目录、实验平台或 MLOps 工具。

## 经验问题对照

- 小红书笔记[研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e)描述按天记录导致碎片化、结果未及时汇总、写论文或汇报前才集中整理，以及多个项目文档切换成本。它支持“按项目聚合证据、及时复盘”，但其周记录和数据库做法是个人系统，不要求所有读者照搬。
- 小红书笔记[科研人员的极简 Git 实用指南](https://www.xiaohongshu.com/explore/6940d4ea000000000d00d9b9)指出科研代码持续演进、AI 可能短时间修改大量文件，缺少版本记录后很难把结果对应到代码；评论中也出现忘记 commit、已迭代多次才发现的问题。它确认低门槛 Git 习惯的必要性，但不能替代上游、分支与数据安全规则。
- 小红书笔记[PhD 如何打造自己的代码模板库？](https://www.xiaohongshu.com/explore/68391d96000000001101d297)建议根据个人习惯沉淀科研通用代码。可吸收的是“复用经验证组件”，不能把个人代码模板直接升级为所有项目的目录标准。
- 知乎问题[计算机本科科研入门求助](https://www.zhihu.com/question/2036962382614900853/answer/2043702641105142901)反映个人笔记与团队协作工具之间的选择困难。回答提出双轨工具，本仓库只吸收“个人深读和团队共享职责不同”的观察；同一实验事实不应在两个系统手工维护两份。

## 规范与项目对照

- [Good Enough Practices in Scientific Computing](https://doi.org/10.1371/journal.pcbi.1005510)明确面向科研计算新手，强调项目组织、原始数据来源、代码、协作和记录的最低可采用实践，支持渐进接入而非一次达到成熟工程标准。
- [The Turing Way](https://github.com/the-turing-way/the-turing-way)覆盖可复现研究、项目设计与协作；其[可复现项目模板](https://github.com/the-turing-way/reproducible-project-template)明确允许使用者按需要编辑、删除或增加文件，README 负责项目目的、协作和关键资源入口。模板因此应被适配，而不是完整复制后长期留空。
- [GitHub Fork 文档](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)说明 fork 允许在不影响上游的情况下管理个人副本；[upstream 配置文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork)要求保留原仓库 remote 以便同步。
- [Made With ML 的 Notebook 到脚本指南](https://madewithml.com/courses/mlops/scripting/)将脚本化放在需要组织和复用工作负载之后；[Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)提供成熟结构。它们说明结构升级应由重复运行和协作需求触发，而不是首次复现的前置仪式。

## 修改结论

新增 `docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md`，提供五种接入场景、十五分钟只读盘点、单一来源映射、当前阶段单卡策略、第一条证据链、结构升级触发和五状态决定。同步调整首页、核心工作流、模板索引、项目结构和教学演练的真实项目入口。

本轮没有新增第 17 张模板，也没有提供自动脚本搬运目录。问题的根源是缺少映射与决策协议；自动复制会把上游差异、实验室规范和隐私权限变成隐藏风险。

## 适用边界

指南主要针对 Git 管理的计算机与 AI 研究代码。实验室若已有经过验证的 ELN、LIMS、内部平台或强制目录，应使用原系统并补缺，不迁移到本仓库格式。公开仓库可以 fork 不代表数据、权重和第三方内容都允许再分发；许可证、机构政策和数据协议需单独核验。

