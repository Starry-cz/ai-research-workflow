# AI 科研项目结构：从最小骨架逐步升级

目录结构的目标是让别人找到输入、代码、配置、运行记录和结论，不是展示工程复杂度。零基础项目先使用最小骨架；只有当数据、实验或协作真的增长时才新增目录。

本页用于新项目或已经确认需要升级的项目。拿到导师、实验室或论文官方仓库时，先使用[真实代码库最小接入](ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)，不要为了匹配下方示例移动上游文件。

## L0–L1：第一个可运行项目

```text
research-project/
├── README.md              # 当前问题、安装、运行命令、结果和下一步
├── .gitignore             # 排除密钥、缓存、数据和大文件
├── environment/           # Python 版本与依赖文件
├── data/README.md         # 数据来源、版本、划分和本地路径；数据通常不提交
├── src/                   # 脚本；尚未拆脚本时可先放一个 Notebook
├── configs/               # 至少保存本次运行使用的配置
└── experiments/           # 命令、日志、指标和失败记录
```

最低验收：换一个空目录后，读者能根据 README 建立环境、找到数据说明、运行一个命令并定位输出。暂时没有论文、投稿、多人协作或大数据时，不创建对应空目录。

## 什么时候升级

| 触发事件 | 新增结构 |
| --- | --- |
| 文献开始超过零散链接 | 新增 `papers/index.md`、检索账本和阅读卡目录。 |
| 数据有多个来源或处理版本 | 拆分 `data/raw`、`data/processed` 与 `data/manifests`；原始数据保持只读。 |
| 同一实验出现多组配置 | 新增实验矩阵、独立配置文件和唯一 `run_id` 目录。 |
| 开始形成论文结论 | 新增 `analysis/` 与 `figures/`，保存主张审计和图表生成链。 |
| 需要共享权重或大产物 | 新增 `artifacts/README.md`，记录外部位置、版本、校验值、负责人、保留状态和复查日。 |
| 同一失败 / 决定开始跨运行复用 | 新增 `knowledge/index.md` 与按需条目；只链接原证据，不复制配置和指标。 |
| 进入投稿或回复评审 | 新增按 venue 和年份划分的 `submissions/`，冻结实际提交版本。 |
| 多人协作或长期维护 | 新增测试、贡献规范、决策日志、发布与引用文件。 |

升级只追加当前需要的结构。不要为了匹配模板移动一个已经清晰、可复现的成熟项目；可以在原目录补充索引和缺失证据。现有 tracker、实验室表格或 Wiki 已经承担某项职责时，只在入口页链接，不复制同一事实。

## L2–L3：可扩展研究项目

```text
research-project/
├── README.md                  # 目标、状态、安装与运行入口
├── .gitignore                 # 排除数据、缓存、密钥和大体积产物
├── .env.example               # 只保留变量名，不包含真实凭证
├── research_brief.md          # 研究问题、假设和资源约束
├── baseline_candidates.md     # 候选、准入证据、停止规则与备选
├── evaluation_spec.md         # 指标、实现、统计单位和决策门槛
├── papers/
│   ├── search_log.md          # 关键词、查询、筛选与去重
│   ├── index.md               # 论文主记录、版本和来源
│   ├── domain_map.md          # 方法、数据、评价、争议与缺口
│   ├── reading_cards/         # 结构化阅读卡
│   └── math_cards/            # 被任务触发的数学概念卡
├── data/
│   ├── README.md              # 来源、权利、版本、内容、划分与风险
│   ├── manifests/             # 文件清单、校验值与 split ID
│   ├── raw/                   # 原始数据，通常不提交 Git
│   └── processed/             # 处理后数据，通常不提交 Git
├── src/
│   ├── data/                  # 数据加载与预处理
│   ├── models/                # 模型与模块
│   ├── train.py               # 训练入口
│   └── evaluate.py            # 评测入口
├── configs/                   # 可版本化配置
├── tests/                     # shape、数据和关键逻辑测试
├── experiments/
│   ├── matrix.md              # 实验矩阵
│   ├── records/               # 单次实验卡
│   └── logs/                  # 日志索引或外部链接
├── analysis/
│   ├── claim_audit.md         # 主张、证据、反证、替代解释和状态
│   └── error_slices.md        # 配对错误、预设切片与探索性发现
├── artifacts/
│   └── README.md              # 大结果的位置、版本、校验值、保留状态与清理记录
├── knowledge/
│   ├── index.md               # ID、症状 / 组件标签、状态、最后核验与替代项
│   └── entries/               # 按触发创建的失败模式、复现差异和决定知识
├── figures/                   # 图表、生成脚本和来源记录
├── paper/                     # 论文、报告和补充材料
├── submissions/
│   └── venue-year/
│       ├── submission-v1/     # 实际送审文件与版本清单
│       ├── reviews/           # 原始评审与原子问题卡
│       ├── response/          # 回复、证据与作者核对记录
│       └── decision.md        # 决定、修订范围与转投条件
├── decisions.md               # 关键决策与放弃理由
└── environment/
    ├── README.md              # 系统、驱动、框架、安装和验证命令
    └── requirements.lock      # 示例名：依赖锁定文件或等价规范
```

这不是强制标准。领域仓库可能使用 `notebooks/`、`benchmarks/`、`prompts/`、`simulations/` 或其他结构；只要输入、运行、证据和版本关系清楚即可。

## 目录设计检查

- README 是否给出从零运行的最短命令，而不是只介绍方法？
- 配置是否与代码分离，并能定位每个主要结果？
- 原始数据是否保持只读，处理步骤是否可重建？
- 日志、指标、图表和 checkpoint 是否能关联同一 `run_id`？
- 失败、中断和排除运行是否仍可找到？
- 平台 TTL、账号到期、产物负责人和复查日是否明确？
- 清理后的资产是否留下原因、时间、影响和替代入口？
- 可复用经验是否链接原证据、写清不适用范围，并能标记 superseded？
- 新成员能否从自己的症状词找到多个候选，并在执行前排除过期、近似和越权建议？
- 大文件、私有数据和密钥是否被安全排除？
- 新目录是否解决真实查找或协作问题，而不是为了“看起来专业”？

## 参考边界

[Made With ML](https://madewithml.com/courses/mlops/scripting/)展示从 Notebook 逐步迁移到脚本和项目目录的过程；[Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)提供成熟数据科学结构。两者适合学习演进方向，但不要求第一次练习立即采用完整生产工程。
