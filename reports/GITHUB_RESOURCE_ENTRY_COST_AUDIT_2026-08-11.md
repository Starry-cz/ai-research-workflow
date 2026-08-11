# GitHub 科研入门资源进入成本审计（2026-08-11）

## 审计问题

仓库已经按 L0–L3、任务和最低产物整理 GitHub 资源，但读者仍要点开项目后，才知道材料是否以英文为主、是否需要 Python / Git / Notebook、是否依赖 AI 客户端、模型访问、云账号或较高算力。对零基础读者，“链接可用”不等于“现在能开始”；隐藏门槛会把一次选择变成新的搜索与安装任务。

本轮只审计进入决策，不给资源打总分，也不重新按 Star 排名。进入成本表示“开始前需要知道什么”，不是对费用、平台可用性或学习难度的永久保证。

## 经验材料对照

- 小红书笔记[研0暑假入门深度学习的一些经验（含踩坑）](https://www.xiaohongshu.com/explore/6880d5480000000017035390)记录了中文讲解更易进入、《动手学深度学习》直接开始门槛较高，以及个人电脑训练耗时较长等真实体验。它支持把语言、课程顺序和算力暴露在选择前；单个学习者的顺序与耗时不用于规定所有人的路线。
- 小红书笔记[研0看英文论文崩溃了](https://www.xiaohongshu.com/explore/6a54c18e000000001003cf25)及其可见讨论反复出现专业词汇导致阅读极慢、逐词理解与先抓结构之间的犹豫。它说明“英文资源”本身就是行动门槛；评论中的具体阅读工具与方法没有经过本轮核验，因此不进入推荐规则。
- 知乎回答[对于机器学习零基础的人，有哪些好的学习路线或建议](https://www.zhihu.com/question/666314243/answer/1994435066227598413)强调不要同时铺开过多材料，应通过小任务形成反馈。它支持“一次一个主资源和一个产物”，不作为课程质量或资源难度的官方证明。

## 官方项目对照

- [OSSU Computer Science](https://github.com/ossu/computer-science)把路线定义为完整计算机科学教育，并给出长期投入估算；因此目录明确其为能力地图，而非科研开始前的整套前置。
- [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)在官方 README 提供简体中文等多语言版本；目录据此标为多语言，而不是笼统写成英文课程。
- [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)把视频、Notebook、Colab 练习与主动完成练习绑定；目录据此写明英文、Python、少量微积分和 Notebook 前置。
- [Made With ML](https://github.com/GokuMohandas/Made-With-ML)明确提供个人电脑与集群路径，并说明个人电脑可运行但更慢；目录不再把集群或 GPU 暗示为起步前置。
- [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)的官方安装说明列出受支持客户端、模型访问和可选导出依赖；目录将“在线读方法”和“真正调用 skill”拆开描述。
- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure)列出 Claude Code 与 Codex 安装方式，并区分生成提示词与调用图像模型；目录据此暴露客户端和出图工具要求。
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)提供多语言 README，但完整流程包含本地环境、模型和领域执行器；目录将“能读说明”与“能运行系统”分开。

## 采取行动

1. `tools.yml` 升级到 v7，并为 22 个精选 GitHub 入门资源增加：
   - `primary_language`：`zh`、`en` 或 `multilingual`；
   - `entry_requirement`：最低前置、账号、依赖、算力或费用核验条件。
2. 补回目录已经使用但机器目录缺失的 `Made With ML` 条目，使人读目录与机器目录一一对应。
3. `docs/GITHUB_RESOURCE_CATALOG.md` 的每个资源使用“进入成本—吸收与边界”两段式说明，保持两列表格，避免移动端窄列。
4. `CONTRIBUTING.md` 要求新增精选资源同步填写进入成本，并禁止把动态费用或在线服务写成永久承诺。
5. 仓库校验脚本检查精选资源集合、语言枚举、进入要求、目录 URL 和 22 条可见进入成本说明。

## 验收与边界

- `python scripts/validate_repository.py`：通过，覆盖 93 份 Markdown、22 个精选 GitHub 资源进入成本和 52 个工具条目。
- 负向测试：临时移除 `ml-for-beginners.primary_language` 后，检查准确报错并退出 1；恢复字段后重新通过。
- 首次工作流回归：debug、baseline、candidate 三组运行、第一次单配置验收、公平比较、知识检索、无命中交接和中文空格路径检查全部通过。
- 机器检查能够阻止精选资源缺少语言或进入要求，也能阻止人读目录漏掉条目或进入成本。
- 字段只能减少“点开才发现不能开始”的情况，不能证明实际学习耗时、地区可访问性、账户资格、费用或硬件表现。
- 语言标记描述主要入口，不保证仓库内所有论文、视频、Issue 和外部课程均有相同语言版本。
- 真人是否能仅凭这些信息在一分钟内排除不合适资源，仍需按陌生读者观察协议验证，不能用字段齐全代替可用性证据。
