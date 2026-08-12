# 零基础 AI 科研方法与工具知识库

这不是新的必修书单，而是按当前问题查询的决策入口。方法负责说明怎样做，工具只在能降低当前成本时启用；所有项目名称、功能和外部条件均以 `2026-08-12` 核验时的官方页面为依据。

机器可读条目保存在 [`knowledge-base.json`](../knowledge-base.json)，终端查询脚本为 [`query_knowledge_base.py`](../scripts/query_knowledge_base.py)。例如：

```powershell
python scripts/query_knowledge_base.py --query 文献
python scripts/query_knowledge_base.py --level L0 --activation 立即
python scripts/query_knowledge_base.py --activation 专项研究
```

## 三层启用规则

| 启用时机 | 判断方式 |
| --- | --- |
| **立即** | 当前动作本身就需要，且能在一次练习中留下可验证产物。 |
| **规模增长后** | 手工方式已经出现重复、混乱或交接成本，再引入追踪、版本或归档系统。 |
| **专项研究** | 只有明确开展 LLM、Agent 或 RAG 评测时启用，不进入通用零基础前置。 |

## 立即可用

### `first-github-loop`：第一次 GitHub 协作闭环

| 要点 | 内容 |
| --- | --- |
| **方法** | 在练习仓库完成分支、提交、Pull Request 和合并，再补本地 Git；不要把网页操作与本地环境混成一步。 |
| **留下** | 一个能从历史检查 branch、commit、PR 和 merge 的练习仓库。 |
| **工具** | [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github)；不要求本地 Git，适合第一次认识真实协作对象。 |
| **边界** | 完成练习不代表掌握远程所有权、团队权限或复杂冲突处理。 |

### `rebuildable-python-notebook`：可重建 Python 与 Notebook

| 要点 | 内容 |
| --- | --- |
| **方法** | 记录解释器、独立环境和直接依赖；重启内核后从头运行，消除隐藏状态。 |
| **留下** | 环境/锁文件、可从头执行的 Notebook 或脚本、干净运行日志。 |
| **工具** | [Jupyter](https://docs.jupyter.org/en/stable/)用于探索与解释；[uv](https://docs.astral.sh/uv/)可统一 Python、环境、依赖和锁定，但已有项目不必为了流行度立即迁移。 |
| **边界** | 环境锁定不自动固定数据、GPU、随机性与外部 API。 |

### `first-ml-baseline`：第一个机器学习 baseline

| 要点 | 内容 |
| --- | --- |
| **方法** | 从小型表格数据理解样本、特征、标签、划分和预处理 Pipeline，再评价简单 baseline。 |
| **留下** | 数据审查、训练—验证—测试、主指标和错误样例齐全的 Notebook。 |
| **工具** | [scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/)提供数据探索、预处理、交叉验证和练习；仓库内继续使用[第一个 ML 闭环](ML_FIRST_LOOP.md)验收。 |
| **边界** | 跑通课程作业不是论文贡献或真实项目泛化证据。 |

### `literature-map-and-library`：文献地图与主记录

| 要点 | 内容 |
| --- | --- |
| **方法** | 搜索入口负责发现，OpenAlex/DBLP/DOI 负责书目与引用关系，Zotero 负责主记录、PDF、标签和引用。 |
| **留下** | 查询与纳排记录、稳定标识、版本关系、核心论文和下一轮引用追踪方向。 |
| **工具** | [OpenAlex API](https://developers.openalex.org/api-reference/introduction)适合开放元数据查询与自动化；[Zotero](https://www.zotero.org/support/quick_start_guide)适合项目文献库和引用。 |
| **边界** | 开放索引存在覆盖、作者消歧和状态误差，关键事实必须回到原文与正式书目来源。 |

### `three-pass-paper-reading`：按价值决定阅读深度

| 要点 | 内容 |
| --- | --- |
| **方法** | 第一遍判断是否值得读；第二遍掌握内容、图表和关键引用；只有核心论文进入第三遍重建假设与实现。 |
| **留下** | 带阅读层级、主张、证据位置、假设、疑问和继续/停止决定的阅读卡。 |
| **依据** | S. Keshav 的 [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)明确区分三遍的目标。 |
| **边界** | 三遍法用于控制投入，不要求每篇论文都读到底。 |

### `reproducible-project-design`：从项目开始保留复现证据

| 要点 | 内容 |
| --- | --- |
| **方法** | 研究问题确定时同步规划数据、分析、环境、版本、协作、伦理与发布边界。 |
| **留下** | Research Brief、数据与环境身份、运行入口、评价协议、权限边界和复跑记录。 |
| **工具** | [The Turing Way](https://book.the-turing-way.org/)覆盖可复现研究、项目设计、协作、沟通和伦理；按当前缺口读一章即可。 |
| **边界** | 可复现不等于所有材料都公开；受限研究仍需元数据、协议和获授权复查。 |

### `tool-adoption-gate`：新工具准入

| 要点 | 内容 |
| --- | --- |
| **方法** | 先写当前阻塞、已有替代、最小试用、退出成本和验收产物，再决定采用。 |
| **留下** | 一张工具候选比较和采用/拒绝决定。 |
| **验证** | 工具确实解决原问题，核心证据可导出，移除工具后不丢失研究身份。 |
| **边界** | Star、榜单和宣传案例只负责发现，不承担质量证明。 |

## 规模增长后启用

### `experiment-tracking-upgrade`：实验追踪升级

| 要点 | 内容 |
| --- | --- |
| **触发** | run 数量已难以手工比较，或第二位成员需要按参数、指标和版本检索。 |
| **方法** | 先固定 `commit—config—data revision—run_id—result`，再使用 [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)搜索 run，必要时用 DVC 管理数据身份。 |
| **留下** | 从图表可反查 run，从 run 可反查代码、配置、数据、日志和 artifact。 |
| **边界** | 追踪平台不能自动保证公平实验、科学解释或长期备份。 |

### `research-release-and-citation`：发布、归档与引用

| 要点 | 内容 |
| --- | --- |
| **触发** | 代码和结果准备公开、投稿补充材料或冻结正式版本。 |
| **方法** | 先完成复跑和权利检查，再由作者决定许可证；使用 `CITATION.cff` 和 [Zenodo–GitHub 集成](https://help.zenodo.org/docs/github/)归档 release。 |
| **留下** | 可复跑 release、版本号、许可证决定、引用元数据、归档记录与 DOI。 |
| **边界** | 本仓库目前仍未选择许可证；任何自动化都不能替作者决定授权范围。 |

## 专项研究才启用

### `llm-evaluation-protocol`：LLM 与 Agent 评测

| 要点 | 内容 |
| --- | --- |
| **方法** | 冻结任务、模型/API、prompt、解码、权限和 scorer；先抽查样例解析，再做重复评测和人工校准。 |
| **工具** | [Inspect](https://inspect.aisi.org.uk/)适合定义任务、solver、scorer 和日志；[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)适合共享标准或自定义任务配置。 |
| **留下** | Eval Spec、配置、原始响应/轨迹、评分、成本时延和错误分类。 |
| **边界** | 公共 benchmark 不等于真实任务，LLM judge 不得未经校准成为唯一评分者。 |

### `rag-diagnostic-evaluation`：RAG 模块级诊断

| 要点 | 内容 |
| --- | --- |
| **方法** | 分开评测解析、切分、召回、排序、上下文、生成和引用，不用一个总分掩盖失败位置。 |
| **工具** | [RAGChecker](https://github.com/amazon-science/RAGChecker)提供检索器和生成器的细粒度诊断指标；先在自己的人工小集上核验指标。 |
| **留下** | 冻结问答集、语料版本、模块级指标、失败分类和代表性样例。 |
| **边界** | 自动 claim-level 与模型评审依赖仍需人工校准，不能替代任务专家判断。 |

## 维护与核验

- 工具事实保存在 [`tools.yml`](../tools.yml)，本页只负责问题到方法与工具的路由；
- 机器知识卡中的 `tool_ids` 必须指向现有工具条目，`guide` 必须指向仓库内真实文件；
- 动态功能、费用、账号、API 和安装方式应在使用当天回到官方页面；
- 新增知识卡前先证明现有卡无法覆盖，并同时填写最小产物、验证方式和边界；
- 更新后运行 `python scripts/validate_repository.py` 和至少一条实际知识库查询。
