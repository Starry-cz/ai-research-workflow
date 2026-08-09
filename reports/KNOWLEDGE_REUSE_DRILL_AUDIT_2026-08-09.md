# 第一次知识检索与安全复用演练审计

- 审计日期：2026-08-09
- 审计对象：研究知识指南、教学索引、首次工作流、调试与求助卡、核心流程和 README
- 问题编号：I-047

## 当前问题

仓库已经定义知识条目的标题、标签、来源、适用范围、状态与复用决定，但现有示例直接给出正确关键词、正确文件和最终答案。读者无需从自己的模糊症状形成查询，也不用面对多个相似候选、过期状态、无来源建议或破坏性动作。自动链接检查只能证明文档结构完整，不能证明零基础读者会安全使用知识。

## 经验帖对照

- [逻辑排错能力如何执行呢？](https://www.xiaohongshu.com/explore/6a5de291000000000c015350)描述新手在失败后重复实验、同时更换很多因素却无法定位原因，并询问逐项排除是否会消耗过多时间；本仓库据此训练按症状检索、候选区分和最小信息实验，不采用个人经历规定统一排错步骤或预算；
- [最近带了几个研一新生，谈谈感受](https://www.xiaohongshu.com/explore/674a942c0000000007035d9d)强调明确任务、针对性搜索、按基础 / 技术 / 课题问题选择求助对象，并用具体环境与现象提问；其中学历比较、工具偏好和管理经验不作为科研能力规则；
- [我把 AI 翻车记录做成了一张清单](https://www.xiaohongshu.com/explore/6a7546dd0000000033011d5f)提出核对原文、条件、对象和作者表述后再把 AI 内容写进记录；其医学科研语境只用于确认 AI 流畅输出造成的回源风险；
- [知乎：如何正确地在 GitHub 上提 Issue](https://www.zhihu.com/question/21235917/answer/203370582)建议说明环境、复现、预期与实际；该回答年代较早且属个人经验，上游当前模板和规则优先；
- [知乎：初学者如何使用 GitHub](https://www.zhihu.com/en/answer/961953665)建议用精确关键词搜索已有 Issue；该个人回答只说明检索入口，不证明搜索结果第一项适用。

## GitHub 项目与正式规范对照

- [GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)提供精确短语、布尔表达式、`repo:`、`path:`、`language:` 与正则查询；本仓库将它们作为缩小候选的技术，不把排名当作根因判断；
- [GitHub Debugging tutor](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/debugging-tutor)建议稳定复现、阅读错误、检查最近变化、最小样例和单变量测试，并以引导问题培养独立能力；它是 Copilot 自定义指令示例，需适配项目，不是科研方法学标准；
- [obra/superpowers 的 systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)把根因调查、模式比较、单一假设、最小测试与验证分阶段；本仓库吸收证据顺序，不采用其绝对措辞、固定失败次数或 agent 行为作为所有项目规则；
- [KCS Searching is Creating](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/010/030)要求保存请求者原始搜索词、环境和区分相似条目的特征；[Track Reuse](https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/201-Solve_Loop/Practice_1_Reuse/Technique_1.3)要求把知识与实际事件关联；[Reuse is Review](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/030/040/020)强调在真实使用中改进有价值条目；这些规则来自服务支持知识管理，不决定科研证据等级；
- [Diátaxis Tutorials](https://diataxis.fr/tutorials/)指出教程应让学习者通过具体行动、可见结果和重复形成能力，并需要真实观察用户；[How-to guides](https://diataxis.fr/how-to-guides/)则面向已经具备基本能力的使用者，支持把本轮材料从参考说明升级为独立教学演练。

## 适用边界

本演练验证的是公开教学脚本中的一条防覆盖路由，不覆盖模型不收敛、指标异常、数据泄漏、分布式故障、安全事件或实验室受限系统。教学干扰项是明确标记的评测夹具，不是历史事实，不得进入正式知识索引。自动脚本只能发现材料与当前 CLI 漂移，不能证明陌生新手理解、检索召回率或跨团队效果；这些需要预先定义任务并观察真实读者。

## 采取行动

- 新增[第一次检索并安全复用研究知识](../docs/FIRST_KNOWLEDGE_REUSE_DRILL.md)，把原始症状、Q0–Q4 查询阶梯、候选比较、最小验证、五种决定和写回组成闭环；
- 新增[闭卷式练习](../examples/first-workflow-drill/knowledge-retrieval-drill.md)、[明确标注的教学候选夹具](../examples/first-workflow-drill/knowledge-retrieval-fixtures.md)和[已填写结果](../examples/first-workflow-drill/knowledge-retrieval-result.md)；
- 新增 `verify_knowledge_retrieval.py`，实际核验命令帮助不存在 overwrite 选项、非空记录目录稳定拒绝覆盖、新临时目录能够生成完整产物；
- 已接入首次工作流与 CI、调试求助卡、知识提炼指南、核心流程、真实项目接入、项目结构、README、索引和持续改进记录；复用记录改为窄屏友好的分段卡片，避免六列宽表逐字换行。

## 验证结果

- `scripts/validate_repository.py`：通过，检查 82 个 Markdown 文件；相对链接、锚点、代码块、README 约束、两类索引和 51 个工具条目均通过；
- `verify_knowledge_retrieval.py`：通过，教学夹具、候选排除、当前 CLI 与防覆盖运行证据一致；
- 完整教学演练：通过，debug、baseline、candidate 三组运行及原公平比较验收通过，新知识复用检查同时通过；
- Windows 编码回归：子进程按当前系统首选编码严格读取，校验脚本自身固定输出 UTF-8；没有使用忽略解码错误的兜底；
- `git diff --check`：通过；仅有工作区 LF / CRLF 提示，没有空白错误；
- 实现提交：`119b7d0`（`docs: add safe knowledge reuse drill`），已推送到 `main`；
- [Repository quality](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31315525330)：通过；
- [First workflow drill](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31315525323)：通过，包含新增知识检索与安全复用校验。

## 状态

已完成。自动检查与真人可用性证据的边界仍保留在报告和教程中。
