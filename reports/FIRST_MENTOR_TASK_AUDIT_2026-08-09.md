# 第一项导师任务授权边界审计

- 审计日期：2026-08-09
- 审计对象：根 README、方向选择、真实代码库接入、第一次安全改码、研究简报、原子任务卡和算力迁移清单
- 问题编号：I-042

## 当前问题

仓库已经要求新手确认任务、数据权限、可修改范围和导师反馈，却没有给出统一的动作分类与开始状态。“导师让我跑一下”仍可能被误解为允许修改共享 baseline、把私有材料发给外部 AI、公开联系上游、使用付费算力或删除旧产物；另一端则可能把所有本地只读检查都停下来等待导师逐项批准。

## 经验帖对照

- [计算机博士 Codex 科研入门使用心得](https://www.xiaohongshu.com/explore/6a4e055c000000001702d0c8)建议在 AI 改码前说明目标、已有文件和预期结果，并限制修改原件。它支持“先写任务与文件边界”，但个人经验不能决定实验室、数据或对外权限，页面可能需要登录；
- [科研探索目的下 Codex 老在奇怪的地方使劲](https://www.xiaohongshu.com/explore/6a76af7d000000002500743e)反映 AI 过度扩展任务、投入无关工程工作的痛点。它支持时间盒和最大范围，不意味着伦理、数据和破坏性动作可以取消门控；
- [作为研究生新手，应该如何和导师沟通](https://zhuanlan.zhihu.com/p/2033116043812532613)建议把过程改写成问题、证据、选项和明确请求，帮助导师做决策。文章由科研服务机构发布，适合作为沟通痛点，不作为统一师生制度；
- [Learning Research](https://github.com/pengsida/learning_research)建议从课程作业进入具体论文和实验室项目，并通过高年级成员与每周讨论获得反馈。该经验来自特定 3D Vision 实验室；“跟着项目做”不能自动说明新成员拥有共享代码、数据和发布权限。

## 官方与项目对照

- [GitHub repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)把 Read、Triage、Write、Maintain 和 Admin 对应到不同平台动作，并建议使用完成职责所需的角色；平台写权限不能替代项目内部批准；
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)允许要求 PR 审阅、状态检查、对话解决和限制 push，说明共享变更应按仓库规则进入审查；
- [GitHub fork permissions and visibility](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)说明 fork 的可见性与权限受上游和组织政策影响，私有内容不能按公开 fork 习惯处理；
- [The Turing Way Data Management Plan](https://book.the-turing-way.org/reproducible-research/rdm/rdm-dmp/)要求说明谁能访问数据、谁授予访问、存储备份、公开边界和成本；敏感数据只给确有工作需要的人；
- [Sharing Sensitive Data](https://book.the-turing-way.org/project-design/data-security/sdpm/sharing-sensitive-data/)指出匿名化后仍可能重识别，受限访问可以是合法共享方式；
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)展示人工门控、拒绝、暂停、预算和版本化，也保留 `--auto-approve`。本仓库吸收可配置门控，不把自动批准设置为零基础真实科研默认模式。

## 适用边界

本次规则是入门级任务分流，不构成法律、伦理或安全意见，也不能单方面改变导师、实验室、机构、资助方、合同、数据提供者或目标 venue 的正式政策。不同团队可把同一动作放入不同类别，但必须留下决定负责人和依据。公开教学练习的本地运行通常可直接开始；医疗、人类参与者、商业敏感、国家安全或受监管项目需要更严格的专门流程。

## 采取行动

- 新增[第一项导师任务授权边界](../docs/FIRST_MENTOR_TASK_BOUNDARY.md)，定义任务授权卡、绿色 / 黄色 / 红色动作、第一次 30 分钟、Git / 数据 / 算力 / 外部 AI 边界和五种状态；
- 新增[已填写任务授权示例](../examples/first-workflow-drill/task-authority.md)，用公开合成数据演练区分本地运行、需确认改码与必须停止的动作；
- 将授权字段嵌入研究简报、原子任务卡和迁移清单，不新增第 18 张模板；
- 在方向选择、真实项目接入、安全改码、指南索引和首页入口中增加授权门控；
- 明确“技术权限不等于任务授权”“待确认不等于所有工作停摆”“自动审批不能替代决定负责人”。

## 验证结果

- 仓库文档质量检查通过：共检查 62 个 Markdown 文件，相对链接、锚点、代码块、README 约束、两类索引和 51 个工具条目均通过；
- 第一次工作流演练验收通过：三组记录产物完整，全部计划运行完成，正式比较只改变 `learning_rate`；
- `git diff --check` 通过；
- 远端 GitHub Actions 状态在本轮提交推送后回填。

## 状态

文档实现与本地验证已完成，等待远端验证。
