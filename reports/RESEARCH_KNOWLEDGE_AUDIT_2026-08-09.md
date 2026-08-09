# 停止后研究知识沉淀与复用审计

- 审计日期：2026-08-09
- 审计对象：README、核心工作流、研究停止门、产物生命周期、真实项目接入、项目结构、实验卡、周复盘与教学演练
- 问题编号：I-046

## 当前问题

仓库已经能保留运行、失败、负结果、停止决定和墓碑记录，但这些事实分散在 config、tracker、日志、实验卡、Issue 和周会中。原“把负结果变成可复用证据”只规定保留内容，没有定义未来如何按症状检索、如何核对适用范围、复用后如何回写，也没有 supersede / retire 生命周期。新手可能再次从头排查同一错误；也可能建立第二套笔记，把指标和配置复制后逐渐漂移，或让 AI 摘要把猜测写成实验室规则。

## 经验帖对照

- [实验失败后，别只写“没做出来”](https://www.xiaohongshu.com/explore/6a3cb42f0000000021020e7b)指出只有失败标签时，之后无法知道失败位置、预期差异、对照、变化条件和下一步。本仓库将这些内容变成可检索条目，同时要求链接原始证据；
- [关于用 Obsidian 做实验记录的感受](https://www.xiaohongshu.com/explore/69e1ac9d0000000023013230)记录前期搭建成本、碎片整理、本地记录和 AI 总结体验，评论反映表格录入与工具选择摩擦。本仓库采用渐进式薄索引，不推荐指定插件，也不让 AI 汇总取代事实；
- [研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e)反映按日期堆过程不利于汇报和复盘；本仓库按未来会提出的问题组织知识，但保留时间和运行证据；
- [知乎：实验记录需要注意的关键点](https://zhuanlan.zhihu.com/p/534204566)举例说明未及时记录临时改变会让成功条件长期无法重建；文章偏生物 / 合规实验，只用于迁移即时身份和变更记录；
- [知乎：如何科学地进行实验设计和记录](https://zhuanlan.zhihu.com/p/69353695)强调实验无论是否符合预期都应整理说明的问题与下一步；文中的具体软件推荐较早且属个人经验；
- [知乎：上了电子实验记录本，之前的实验记录怎么办](https://zhuanlan.zhihu.com/p/2058238080742594121)反映历史记录迁移和原始数据可追溯需求；该文来自商业服务商，只确认痛点，不采用产品结论。

## GitHub 项目与正式规范对照

- [Architecture Decision Record](https://github.com/architecture-decision-record/architecture-decision-record)以 Markdown 保存上下文、决定、后果和 supersede 链，强调重要决定不应被静默改写。本仓库借鉴决策历史，不把软件 ADR 当作科学证据规范；
- [eLabFTW](https://github.com/elabftw/elabftw)展示实验搜索、团队权限、导入导出和本地部署；它面向实验室级 ELN，不是零基础 AI 项目的必装组件；
- [DVC](https://github.com/treeverse/dvc)把参数、指标和 artifact 元数据与 Git 版本关联，支持比较与恢复；本仓库吸收版本身份和来源链接，不要求首次实验部署 DVC；
- [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/tracking-api/)支持以 tags、notes、Git commit 和搜索定位 run；run 元数据不会自动形成可信根因、适用边界或研究结论；
- [The Turing Way：Electronic Lab Notebooks](https://book.the-turing-way.org/reproducible-research/rdm/rdm-elns/)同时列出搜索、共享和备份优势，以及成本、格式锁定、安全与学习曲线；本仓库据此要求导出和退出策略；
- [FAIR Guiding Principles](https://www.gofair.foundation/fair-principles)强调标识、丰富元数据、索引、合格引用、来源与访问条件，并允许数据消失后元数据仍可访问。本仓库只吸收入门级 findability、provenance 和墓碑，不宣称 Markdown 条目达到 FAIR 合规。

## 适用边界

本指南主要面向计算实验、论文复现和 AI / ML 项目中的失败模式与决定知识，不替代受监管电子实验记录、专利见证、临床、伦理、质量体系或机构档案政策。知识条目是检索入口和限定经验，不是原始数据、SOP 批准、统计证明或作者团队决定。`CONFIRMED_REUSE` 不表示跨任务普遍有效。受限资产、匿名材料和安全信息的标题与标签本身也可能敏感，S0–S3 与正式政策优先。

## 采取行动

- 新增[从实验记录到可检索研究知识](../docs/RESEARCH_KNOWLEDGE_CAPTURE.md)，定义提炼触发、六类条目、最小字段、五种状态、薄索引、复用前检查、五种复用决定和回写规则；
- 新增[教学知识索引](../examples/first-workflow-drill/knowledge-index.md)和[已填写条目](../examples/first-workflow-drill/knowledge-entry.md)，使用真实验证过的非空输出目录 `FileExistsError` 路由，不编造跨项目复用；
- 扩展实验卡和周复盘的知识提炼字段，不新增第 18 张空白模板；
- 将知识提炼接入研究停止门、核心流程、项目结构、真实项目接入、README 与指南索引；
- 保持 config、指标、日志、数据和决定的单一来源，条目只保存检索、边界、诊断顺序和后果。

## 验证结果

- `scripts/validate_repository.py`：通过，检查 77 个 Markdown 文件；相对链接、锚点、代码块、README 约束、两类索引和 51 个工具条目均通过；
- 完整教学演练：通过，debug、baseline、candidate 三组计划运行全部完成，`verify.py` 确认正式比较只改变 `learning_rate`；
- `git diff --check`：通过；仅出现 Windows 工作区的 LF / CRLF 转换提示，没有空白错误；
- 实现提交：`ed89004`（`docs: add reusable research knowledge workflow`），已推送到 `main`；
- [Repository quality](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31314669088)：通过；
- [First workflow drill](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31314669089)：通过。

## 状态

已完成。
