# 第一次向开源上游求助与贡献审计

- 审计日期：2026-08-09
- 审计对象：README 求助入口、`SUPPORT.md`、`CONTRIBUTING.md`、调试与求助卡、Issue Form 和真实项目接入指南
- 问题编号：I-043

## 当前问题

I-011 已要求目标、命令、环境、完整 traceback 和最小复现，但仍把“能够复现后提交上游”压缩成一句话。它没有定义支持范围、问题所有者、Issue / Discussion / 私密报告 / PR 的分流，也没有说明论文复现差异为何不自动是软件 bug、功能改动为何应先讨论，以及维护者关闭或拒绝后如何回写本地研究记录。

## 经验帖对照

- [Python 环境要配死了](https://www.xiaohongshu.com/explore/68a2ff42000000001b01e5b5)和[跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)反映 Python、CUDA、路径、I/O、显存与预处理错误常被混在“项目跑不起来”中；本仓库据此先排本地身份和支持范围，不采用个人环境配置作为通用修复；
- [科研人员的极简 Git 实用指南](https://www.xiaohongshu.com/explore/6940d4ea000000000d00d9b9)反映 AI 与频繁改码后结果无法对应 commit、diff 难以回退。它支持在 Issue / PR 前固定上游和本地版本，但个人 Git 习惯不替代项目贡献规则；
- [知乎：如何正确地在 GitHub 上提 Issue](https://www.zhihu.com/question/21235917/answer/203370582)建议遵循模板、说明环境、复现、预期与实际，并使用社区可理解的语言。回答年代较早且为个人经验，本仓库只吸收可操作信息，当前上游规则优先；
- [知乎：如何加入开源项目](https://www.zhihu.com/question/26640695/answer/2425325922)建议从自己能完成的 Issue、`good first issue` 和有说明的 PR 开始。标签不能保证任务仍无人处理、无需讨论或一定合并。

## 官方与项目对照

- [GitHub 贡献指南](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)说明 `CONTRIBUTING.md` 与模板帮助贡献者形成有用的 Issue / PR；[Issue / PR 模板](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)可要求结构化信息并提供安全政策；
- [GitHub 创建 Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)会提示疑似重复项，也支持从 Discussion 转成 Issue；[创建 Pull Request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)区分 base / head branch、Draft PR 与 Issue 关联；
- [GitHub 私密漏洞报告](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately)只在仓库启用后可用；否则应按安全政策请求私密联系人，不能公开漏洞细节；
- [PyTorch](https://github.com/pytorch/pytorch)把初学者问答导向论坛，并提示新功能先开 Issue 讨论，说明不同问题需要不同维护通道；
- [Qwen Issue 模板](https://github.com/QwenLM/Qwen3.6/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml)要求模型 / 框架身份、最小复现、精确命令、预期 / 实际、环境和单一问题，并把不同产品路由到相应仓库或服务；
- [Transformers Issue #33405](https://github.com/huggingface/transformers/issues/33405)有 traceback 但模型与集成所有权不清，最终被指向另一项目。单个案例不能定义所有路由，但说明“完整日志”仍不等于“正确上游”。

## 适用边界

本指南适合公开 GitHub 上的 AI / 计算机科研软件，不替代项目自己的贡献、安全、行为准则和支持政策。私有实验室仓库、商业服务、受监管数据和匿名材料应使用内部或正式渠道。最小复现能证明行为存在，不自动证明根因、严重性或修复方案。维护者有权基于范围、兼容性、资源和路线拒绝 Issue 或 PR；贡献未被接受不等于研究观察无效。

## 采取行动

- 新增[第一次向开源上游求助与贡献](../docs/UPSTREAM_HELP_AND_CONTRIBUTION.md)，建立问题所有权、六级证据门、渠道分流、Issue 包、研究代码特殊路由、PR 闭环与八种状态；
- 新增[已填写路由示例](../examples/first-workflow-drill/upstream-routing.md)，实际验证一个非空输出目录触发的 `FileExistsError` 属于文档明确的本地使用问题，因此不提交上游；
- 升级调试与求助卡、README、支持说明、真实项目接入和指南 / 模板索引；
- 为本仓库新增 Pull Request 模板与安全报告说明，使维护规则与对读者的建议一致；
- 保留现有文档 Issue Form，不新增通用 bug 表单，因为本仓库不维护第三方运行代码。

## 验证结果

- 文档质量检查通过：共检查 67 个 Markdown 文件，相对链接、锚点、代码块、README 约束、两类索引和 51 个工具条目均通过；
- 第一次工作流演练验收通过：三组产物完整，全部计划运行完成，正式比较只改变 `learning_rate`；
- 修改后的 Issue Form 延续现有有效字段结构；推送后在已登录的 GitHub Issue 创建页确认“文档、路线或模板问题”可见，并同时出现私密安全报告入口。GitHub Community Profile API 暂未返回 Issue Form，静态 HTML 也未包含动态渲染标题，因此不把二者单独作为模板失效依据；
- Pull Request 模板与 `SECURITY.md` 已被 GitHub 识别，安全政策页可正常访问；
- [Repository quality](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31312513556) 与 [First workflow drill](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31312513587) 均通过；
- `git diff --check` 通过，提交 `35b91b0` 已推送至远端 `main`。

## 状态

已完成：文档、仓库社区文件、本地回归、远端页面与 GitHub Actions 均已验证。
