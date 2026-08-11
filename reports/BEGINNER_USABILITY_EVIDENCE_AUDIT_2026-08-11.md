# 零基础首次使用证据审计（2026-08-11）

## 审计结论

仓库已有首屏默认入口、可运行演练、自动验收和求助卡，但此前没有面向未参与编写者的观察任务，也只有一份要求“预期改进 + 外部依据”的通用 Issue 表单。现有证据可以证明文档结构与演练产物一致，不能证明真正的零基础读者会找到入口、理解术语或在首次报错后继续。

本轮建立低负担首次使用反馈和可复查的陌生读者观察协议；截至本报告日期，尚未录入真实参与者结果，因此状态是 `PROTOCOL_READY / HUMAN_EVIDENCE_PENDING`。

## 经验材料对照

- 小红书笔记[研0科研小白求助](https://www.xiaohongshu.com/explore/6a51acbe000000001101def3)的评论同时建议长课程链、只学最新 YOLO、直接使用代码 Agent 或转方向，呈现新手面对互相冲突且工具导向建议时难以选择第一步。它是一则个人求助与评论样本，只用于识别入口不确定性，不定义课程、方向或就业规则；
- [计算机科研新手快速入门](https://www.xiaohongshu.com/explore/6a55f71400000000170282b1)的评论继续追问如何选方向、找 baseline，以及 Agent 完成工作后自己没有学会什么，说明短路线发布后仍需要观察读者是否真正理解并行动；评论不能证明本仓库当前入口有同样问题；
- 知乎问题[计算机本科科研入门求助](https://www.zhihu.com/question/2036962382614900853/answer/2043702641105142901)把 Zotero、Obsidian、协作平台和多种 AI 工具同时放进入门决策，反映工具选择本身会成为起步负担；回答含产品推荐，只支持“需要更明确第一步”，不支持具体工具选择；
- 知乎回答[本科生小白如何入门机器学习](https://www.zhihu.com/question/666314243/answer/1994435066227598413)建议不要同时启动全部资源，并以小任务和可展示产物推进；它属于个人经验，不能替代参与者实际使用本仓库的观察。

## 规范与项目对照

- [GitHub Skills Quickstart Guide](https://skills.github.com/quickstart)要求邀请潜在学习者实际测试课程并提供反馈入口，说明维护者自测不是课程可用性的终点；
- [Diátaxis Tutorials](https://diataxis.fr/tutorials/)要求通过行动和可见结果建立能力，并强调在真实学习者使用中发现教程缺口；它提供文档方法，不证明某个具体任务已经可用；
- [GOV.UK 的 moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing)要求观察目标用户完成清晰、可信且不暗示答案的任务，告诉参与者测试的是服务而不是个人，并主要观察与倾听；[研究记录指南](https://www.gov.uk/service-manual/user-research/taking-notes-and-recording-user-research-sessions)要求把可见行为与研究者解释分开；政府服务方法需要缩小后才能用于开源教程，不能把其人员数量或组织流程机械搬入个人仓库；
- [GitHub Issue Forms 语法](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)支持用下拉、文本区和必填校验收集一致信息；结构化表单只改善输入，不保证参与者愿意公开 GitHub 账号或问题完整；
- [Learning Research](https://github.com/pengsida/learning_research)明确文档可能不完整、特定实验室经验不一定适用于其他情境，并通过开源审阅持续改进；本仓库吸收经验边界和交流反馈，不把 3D Vision 路线普遍化；
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)公开邀请测试者并提供测试指南，同时保留多种人工介入模式；本仓库只吸收“明确测试入口与反馈回路”，不采用自动产出论文或自动批准作为新手验收。

## 发现的问题

1. 通用文档表单要求提交者提供问题位置、预期改进和外部依据，适合成熟贡献者，不适合只知道“我不知道下一步点哪里”的首次读者；
2. README 的求助段只覆盖调试和文档问题，没有把首次误点、犹豫、无报错停止纳入可观察反馈；
3. 仓库没有统一的中性任务、观察状态码、提示规则、隐私边界和复查条件；
4. 自动检查通过后容易产生“零基础已验证”的表达风险，但没有明确的人证门控。

## 已采取行动

- 新增 `.github/ISSUE_TEMPLATE/beginner-first-use.yml`，只要求起始状态、本次结果、首次动作、首次卡点和帮助来源，不要求新手提出解决方案或查找外部证据；
- 新增[零基础首次使用可用性观察](../docs/BEGINNER_USABILITY_OBSERVATION.md)，固定不提示答案的任务、观察字段、状态码、问题级别、隐私要求和陌生读者复查条件；
- 在 README、支持说明、贡献指南和指南索引增加就近入口，并区分首次体验反馈与正式文档改进；
- 在仓库质量脚本中校验轻量表单存在、关键观察字段齐全，且没有把“预期改进”和“外部依据”设为新手必填项。

## 证据边界与下一步

本轮证明的是协议和反馈入口已经建立，不是真人使用成功。GitHub Issue 会公开账号与内容，不能覆盖不愿公开者；观察者应保存脱敏摘要。后续需要邀请未参与编写、符合目标起始状态的读者，在不提示正确文件的情况下执行任务；逐次报告环境、观察事实、提供过的提示和最终状态，不从少量样本外推普遍成功率。
