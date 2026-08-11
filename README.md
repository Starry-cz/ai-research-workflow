# AI 科研工作流工具库

> 面向零基础学习者的 AI / 计算机科研入门库：从第一次可检查运行，到论文复现、实验改进与研究表达。

[开始默认路径](#第一次来默认从这里开始) · [按当前状态选择](#30-秒选择入口) · [查看全部指南](docs/README.md) · [浏览资源目录](docs/GITHUB_RESOURCE_CATALOG.md)

---

## 先选一个入口

### 我刚开始，还没有可运行项目

从[零基础默认路径](#第一次来默认从这里开始)开始。先确认工具链、运行一次小实验，再决定是否进入机器学习、论文或真实项目。

### 我已经拿到代码、任务或实验结果

打开[30 秒选择入口](#30-秒选择入口)，按“导师任务、论文复现、结果分析或重复失败”进入对应工作流。

### 我想系统找课程、论文和工具

浏览[GitHub 科研入门资源目录](docs/GITHUB_RESOURCE_CATALOG.md)。每个资源均标注适用阶段、进入成本和建议留下的产物。

---

**研究主线**：方向 → 论文 → 代码 → baseline → 单变量实验 → 研究报告。

> **使用边界**：AI 可以帮助检索、解释、配置环境、阅读代码和检查遗漏；研究者必须理解并核验论文、代码、数据、实验和结论。

## 第一次来：默认从这里开始

如果暂时不知道自己属于 L0、L1 还是 L2，不必先浏览全部资源、模板和专项指南。先完成下面一条路径；已经拿到导师或团队任务时，先阅读[任务授权边界](docs/FIRST_MENTOR_TASK_BOUNDARY.md)。

第一次看到 `commit`、`origin`、`seed`、`run_id` 或 `baseline` 时，不需要先搜索一整套课程。只打开[零基础默认路径术语速查](docs/BEGINNER_GLOSSARY.md)的对应条目，看完“现在要做什么”和“不能推出什么”就返回当前步骤。

### 你会完成什么

- **适合谁**：第一次接触计算机 / AI 科研，尚未独立跑通过可检查实验的人。
- **会学到什么**：确认真实 Python 解释器，运行一次脚本，并从配置、日志和指标找到证据。
- **会留下什么**：包含本次实际配置副本、环境、日志和指标的独立运行目录；进入 L0 指南时还会在 `learning/first-run` 分支留下第一次本地版本记录（commit），不会自动发布。
- **前置条件**：一台允许安装 Git 与 Python 的电脑；不要求先会深度学习、Linux 或读完课程。
- **建议时间**：首轮预留 60–120 分钟；软件下载、网络、权限或系统故障时间另计，不以耗时判断能力。

1. 打开[零基础准备检查表](templates/00-readiness-checklist.md)，第一次只核对“工具能力”；有一项不知道如何验证，就进入[L0 工具链指南](docs/L0_TOOLCHAIN_START.md)；
2. 工具能力可验证后，完成[第一次可审计实验演练](examples/first-workflow-drill/README.md)，不要同时选择真实论文、GPU、Agent 或整套课程；
3. 看到验收脚本输出 `PASS`，并能指出四项产物、实际解释器和输出目录后，再回到[30 秒选择入口](#30-秒选择入口)决定进入机器学习闭环、方向选择还是已有项目接入。

**完成标志**：`verify_first_run.py` 输出 `PASS`；你能找到 `config.snapshot.json`、`environment.json`、`metrics.json` 和 `run.log`，并说明失败时要保留哪条命令与首个报错。第一次只完成单配置运行，三组公平比较属于第二轮。卡住时先看演练页的“常见失败”，仍无法区分再填写[调试与求助卡](templates/10-debug-help-request.md)。无论完成、误入其他页面还是中途停止，都可提交[零基础首次使用反馈](https://github.com/Starry-cz/ai-research-workflow/issues/new?template=beginner-first-use.yml)。

## 目录

- **开始与选择**：[适用对象](#这个仓库适合谁) · [默认路径](#第一次来默认从这里开始) · [30 秒选择](#30-秒选择入口) · [首次工作流演练](#先完成一次工作流演练)
- **学习与研究**：[能力地图](#零基础能力地图) · [八个里程碑](#八个能力里程碑) · [今天的任务](#把阶段目标变成今天的任务) · [完整科研工作流](#完整科研工作流)
- **执行与协作**：[全部指南](docs/README.md) · [求助](#卡住时如何求助) · [导师与协作](#周会导师与协作沟通) · [AI 的位置](#ai-在科研中的正确位置)
- **资源与维护**：[工具导航](#工具与入口导航) · [模板](#可直接复用的模板) · [项目结构](#推荐项目结构) · [常见误区](#新手常见误区) · [方法论](#方法论参考) · [维护方式](#维护方式) · [许可与引用](#许可引用与版本)

## 这个仓库适合谁

### 主要面向

- 没有科研经历，不知道选题、读论文和做实验分别要做什么；
- Python、Git、Linux 或深度学习基础不扎实；
- 能看懂少量代码，但没有完整跑通过论文仓库；
- 收藏了很多课程和工具，却始终没有形成自己的科研闭环；
- 希望使用 AI 辅助科研，同时避免幻觉引用、虚假实验和过度依赖。

### 本仓库重点解决

| 新手问题 | 对应解决方式 |
| --- | --- |
| 起步无从下手 | 能力自测、起步清单和八个能力里程碑。 |
| 不知学到何处 | “够用即可”的最低能力门槛和阶段验收。 |
| 读完不会实现 | 论文—公式—图—代码—张量—实验映射。 |
| 项目无法运行 | 从环境、预训练模型、单批次到完整训练的复现顺序。 |
| 改码失控 | 单变量改动、实验卡和回退机制。 |
| AI 内容存疑 | 来源分层、风险登记和人工验收。 |
| 实验难成文 | 从研究问题到证据表格的一一对应。 |
| 长期无进展 | 结果分类、有效尝试台账、预算 / 信息增量停止门和重开条件。 |
| 经验难复用 | 薄知识索引、原证据链接、适用范围、复用回写和 supersede 状态。 |
| 经验能否照做 | 原始症状查询、候选排除、身份核验、最小验证和安全复用演练。 |
| 检索无结果 | 原始查询、负面发现、唯一问题和权限随问题交接；回复验证后再回流。 |
| 多系统命令 | Windows、Ubuntu、macOS CI 矩阵与含中文、空格路径检查；个人 IDE、GPU 和服务器仍需本机验证。 |
| 结果如何表述 | V0–V4 验证等级、S0–S3 共享权限和用途状态。 |
| 他人难复查 | 唯一交接入口、指标重算和冷启动复跑。 |
| 任务能否执行 | 任务授权卡、三类动作与确认 / 升级状态。 |
| 报错反馈渠道 | 上游所有权、证据门、Issue / 私密报告 / PR 分流。 |
| 首页是否好用 | 不提示答案的首次使用观察、轻量反馈、隐私边界和另一位读者复查。 |

## 第一次使用：从这里开始

### 30 秒选择入口

不需要从头读完整份 README。先选择最接近自己的状态：

**现在还没有可运行项目**

- **刚接到导师或团队的第一项任务** → 先用[第一项导师任务授权边界](docs/FIRST_MENTOR_TASK_BOUNDARY.md)确认交付、允许读取 / 写入 / 运行 / 分享的范围和决定负责人，再进入方向选择或真实项目接入；
- **L0：不会终端、Git 或 Python 环境** → 先做[零基础准备检查表](templates/00-readiness-checklist.md)，按[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)确认远程所有者、创建个人练习分支并留下第一次本地 commit，再完成[第一次工作流演练](examples/first-workflow-drill/README.md)和里程碑 M1–M3；
- **L1：能运行 Notebook，但没有复现过论文** → 先完成[第一个机器学习闭环](docs/ML_FIRST_LOOP.md)和[第一次工作流演练](examples/first-workflow-drill/README.md)，再按[方向选择决策树](docs/DIRECTION_FIRST_CHOICE.md)建立[研究简报](templates/01-research-brief.md)和[文献检索账本](templates/07-literature-search-log.md)，从[首篇 baseline 筛选表](docs/CORE_RESEARCH_WORKFLOW.md#首篇-baseline-筛选表)进入 M4–M6；

**已经有代码、结果或明确阻塞**
- **L2：已经拿到或跑通过代码，但实验不可解释或不可复现** → 先按[真实代码库最小接入](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)映射现有 README、环境和实验台账，再使用[复现规划](templates/03-reproduction-plan.md)和[baseline 稳定化门](docs/BASELINE_STABILIZATION_GATE.md)决定下一步；
- **连续不提升、反复失败或预算快用完** → 先用[研究停止门](docs/RESEARCH_STOPPING_AND_PIVOT.md)区分无效运行、有效负结果与证据不足，再判断下一项实验是否真的会改变决定；
- **同一失败反复出现，或项目准备暂停 / 交接** → 用[研究知识提炼指南](docs/RESEARCH_KNOWLEDGE_CAPTURE.md)建立薄索引，条目只链接原证据并写清适用范围、状态与替代关系；
- **已经搜到相似经验，但不确定是否适用** → 先完成[第一次知识检索与安全复用演练](docs/FIRST_KNOWLEDGE_REUSE_DRILL.md)，比较至少两个候选，核对当前身份和来源后再执行最小动作；
- **检索无命中或候选仍无法区分** → 不要重新发送一句“跑不起来”；继续使用[知识复用演练的无死路分支](docs/FIRST_KNOWLEDGE_REUSE_DRILL.md#8-无命中或无法区分时不要重新开始)，把原始查询、已开候选、负面发现、权限和一个具体问题交给唯一所有者，回复验证后再关闭；
- **已经有实验结果，准备组会、共享、决策或写作** → 先用[实验结果证据等级与表达边界](docs/EVIDENCE_READINESS_AND_SHARING.md)分开判断证据成熟度和共享权限，再使用[结果—主张审计](templates/15-result-claim-audit.md)检查具体表述；
- **正在投稿、回复评审或转投** → 使用[投稿、评审与版本归档卡](templates/09-submission-review-archive.md)，先核验当前 venue 规则并冻结实际送审版本。

无法判断等级时，从 L0 检查表开始；已经掌握的项目直接跳过，但对应的最低产物必须能够拿出来验证。

### 只启用当前阶段的最小模板包

仓库提供的是工具箱，不是要求一次填完的表格作业。任何时候只打开当前阶段需要的模板；完成后归档，再进入下一包。

| 当前阶段 | 最小模板包与升级条件 |
| --- | --- |
| L0 工具起步 | 只填[准备检查表](templates/00-readiness-checklist.md)，其余先看[已填写演练](examples/first-workflow-drill/README.md)，不要复制全部空模板。<br>**升级**：能独立运行脚本并找到日志、配置和指标。 |
| L1 选方向 | [研究简报](templates/01-research-brief.md) + [文献检索账本](templates/07-literature-search-log.md) + [baseline 准入卡](templates/11-first-baseline-gate.md)；导师任务先填简报内的授权字段。<br>**升级**：候选通过低成本预检并有备选，下一步处于 `READY_WITHIN_SCOPE`。 |
| L2 做复现 | [论文阅读卡](templates/02-paper-reading-card.md) + [复现规划](templates/03-reproduction-plan.md)；取得数据后启用[数据集卡](templates/13-dataset-card.md)。<br>**升级**：论文目标与本地 baseline 已分开，并取得稳定化门控决定。 |
| L3 做实验 | 运行前用[实验卡](templates/04-experiment-card.md)和[评价协议卡](templates/14-evaluation-spec.md)；无进展或预算触发时先过[研究停止门](docs/RESEARCH_STOPPING_AND_PIVOT.md)，运行后再判[证据与共享等级](docs/EVIDENCE_READINESS_AND_SHARING.md)并完成[结果—主张审计](templates/15-result-claim-audit.md)。<br>**升级**：结果类别、继续 / 转向 / 停止依据、证据成熟度、受众权限与主张边界均可审计。 |

其他模板只在事件发生时启用：任务过大用[原子任务卡](templates/06-daily-task-card.md)，需要组会用[每周复盘](templates/05-weekly-review.md)，迁移算力用[迁移清单](templates/08-compute-data-environment-checklist.md)，关键运行需要交给别人复查时用[运行交接卡](templates/16-run-handoff.md)，卡住求助用[调试卡](templates/10-debug-help-request.md)，公式阻塞用[数学概念卡](templates/12-math-concept-card.md)，进入投稿再用[投稿归档卡](templates/09-submission-review-archive.md)。

同一时间建议只维护一个阶段门控、一个当前任务 / 实验记录，以及一个确有阻塞才启用的按需卡。导师或实验室已有等价记录时直接复用，不为匹配本仓库重复填写。

### 第一次执行的五件事

不要先下载几十个项目。下面五件事描述完整起步阶段，不要求同一天完成：

1. 用[零基础准备检查表](templates/00-readiness-checklist.md)判断自己目前在哪一层；已有导师或团队任务时，同时确认[第一项任务的授权边界](docs/FIRST_MENTOR_TASK_BOUNDARY.md)；
2. 按[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)安装并核验 Git、Python 和独立环境，不混用不同系统的命令；
3. 从一个成熟方向列出两到三个候选，使用[首篇真实 baseline 准入卡](templates/11-first-baseline-gate.md)完成低成本预检，再选择有官方代码、训练脚本和可承受算力的一篇；
4. 克隆选定项目后，按[真实代码库最小接入](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)盘点上游、任务授权和现有记录，再在获准范围内运行官方预训练模型的评测或演示，不要立刻从头训练；
5. 建立[复现规划](templates/03-reproduction-plan.md)补齐缺失证据；如果需要云端算力或迁移大数据，再完成[算力、数据与环境迁移清单](templates/08-compute-data-environment-checklist.md)。

### 第一天的最低产物

```text
research-project/
├── README.md              # 当前目标、运行入口和进度
├── papers/                # 论文 PDF 或链接索引
├── notes/                 # 阅读卡与问题清单
├── src/                   # 代码
├── configs/               # 可版本化配置
├── experiments/           # 实验记录
└── environment/           # 依赖与环境说明
```

第一天不要求提出创新点。只要能够解释“我要复现哪篇论文、为什么选择它、需要哪些数据和算力、哪些动作已经获准、下一步运行什么命令”，就已经完成起步。

## 先完成一次工作流演练

在下载真实论文代码前，建议先完成[第一次可审计实验演练](examples/first-workflow-drill/README.md)。它使用 Python 标准库和合成数据，在 CPU 上演示：

第一次只运行调试配置并用 `verify_first_run.py` 验收四项产物；看到第一个 `PASS` 后可以停止。下面的完整比较链属于第二轮：

```text
冻结问题与配置
  → 运行固定 seed 的调试实验
  → 保存命令、环境、日志与指标
  → 按预先声明的 seed 集合运行比较实验
  → 汇总全部计划运行与波动
  → 写出不超过证据范围的结论
```

这个演练的目的不是取得高准确率，而是让你第一次看见 `question → config → run_id → log → metrics → decision` 如何连成证据链。它不是论文复现，也不能作为算法创新、模型优越性或真实数据泛化能力的证据。

该最小链路已配置 GitHub Actions，在 Windows、Ubuntu 和 macOS 的 Python 3.11 环境执行，并额外检查含中文与空格的路径；各系统只有在对应 job 实际通过后才计为远端证据。绿色 CI 只证明对应提交在托管 runner 上通过；你的 IDE 解释器、WSL、CUDA / GPU、学校服务器和真实论文依赖仍需在目标环境单独核验，具体边界见[L0 工具链指南](docs/L0_TOOLCHAIN_START.md#本仓库实际验证到哪里)。

完成后再进入真实 baseline。此时至少应该能够回答：哪个文件固定了变量，哪条命令生成结果，哪个指标来自哪个 `run_id`，失败运行放在哪里，以及为什么不能只挑最好的一次。

如果还不能解释样本、特征、标签、loss、指标以及训练 / 验证 / 测试集的不同职责，先完成[第一个机器学习训练—验证—测试闭环](docs/ML_FIRST_LOOP.md)，再进入论文代码。

## 零基础能力地图

### 能力分级

| 阶段 | 当前状态与下一步 |
| --- | --- |
| L0 工具起步 | **当前**：不熟悉终端、Git、Python 环境和 Jupyter。<br>**下一步**：能确认远程所有者，在个人练习分支创建本地提交，并创建环境、安装依赖、运行脚本。 |
| L1 机器学习 | **当前**：能运行 Notebook，但不熟悉训练、验证和指标。<br>**下一步**：能修改样例、解释数据划分、训练循环和评价指标。 |
| L2 论文复现 | **当前**：能跑通训练代码，但无法解释论文与实现对应关系。<br>**下一步**：能复现 baseline、定位差异并形成复现报告。 |
| L3 研究实践 | **当前**：能复现论文，准备尝试改进。<br>**下一步**：能提出可证伪假设、完成对照实验和失败分析。 |

本仓库的核心目标是帮助读者从 L0 或 L1 到达 L2，并为进入 L3 提供规范。

### 三阶段成长路径

课程学习与科研实践不应完全割裂。更可执行的成长方式是边学边留下项目产物：

```text
广度打底：认识基础概念和常用工具，重点完成作业与小项目
    ↓
深度复现：围绕一个细分方向，吃透一篇论文及其代码和实验
    ↓
独立项目：提出可检验问题，完成实验、写作、展示与复盘闭环
```

1. **广度打底**：课程不求一次学完，以“能运行、能修改、能解释”为验收标准；
2. **深度复现**：聚焦一篇资料完整的论文，建立论文—代码—数据—实验映射；
3. **独立项目**：从真实失败现象或方法局限出发，用最小实验检验假设，再决定继续、优化或转向。

### 五项核心科研能力

| 核心能力 | 零基础阶段的可验证表现 |
| --- | --- |
| 发现问题 | 能说明问题为什么重要、现有方法在哪里失效，并形成研究简报。 |
| 设计方案 | 能提出可证伪假设，提前写出预期现象、对照组和最小实验。 |
| 完成实验 | 能复现 baseline，保留配置、日志、失败项和公平对照。 |
| 论文表达 | 能让每个主要主张对应到实验、图表、推导或可靠文献。 |
| 研究展示 | 能用五分钟讲清问题、方法、证据、局限和下一步，并回答质疑。 |

### 开始科研前的最低能力

你不需要先学完整个计算机本科，但至少需要能完成：

- **终端**：进入目录、查看文件、运行命令、阅读报错；
- **Git**：clone、status、diff、commit，知道 commit 是代码版本；
- **Python**：变量、函数、类、列表和字典、异常、模块导入；
- **环境**：创建独立环境、安装依赖、导出环境文件；
- **数据**：理解样本、特征、标签、训练集、验证集和测试集；
- **机器学习**：理解模型、损失、优化器、过拟合、指标和基线；
- **深度学习**：理解张量、shape、前向传播、反向传播和梯度。

### “学到够用”的判断标准

不要用观看时长判断是否学会。每一项基础都要留下可运行产物：

| 基础 | 最低产物 |
| --- | --- |
| 终端与 Git | 克隆一个仓库，完成一次小修改并查看 diff。 |
| Python | 写一个读取数据、调用函数并保存结果的小脚本。 |
| NumPy / Pandas | 读取数据，检查缺失值、分布和数据类型。 |
| 机器学习 | 完成一个训练—验证—测试闭环并解释指标。 |
| PyTorch | 写出 Dataset、DataLoader、模型、loss 和训练循环。 |
| 论文阅读 | 完成一张有证据位置的论文阅读卡。 |
| 按需数学 | 完成一张[数学概念卡](templates/12-math-concept-card.md)，用 shape、玩具数值和代码检查当前公式。 |

## 八个能力里程碑

可以把每个里程碑暂按一周估时，但它们不是统一日历。基础、任务、算力和指导条件不同，同一里程碑可能需要一天或数周；只有产物通过验收才升级。

| 阶段与主要任务 | 产物与完成标准 |
| --- | --- |
| **M1 工具与环境** | **任务**：终端、Git、Python 环境、Jupyter。<br>**产物**：环境文件、运行日志、第一次 commit。<br>**完成**：能独立重建环境并运行脚本。 |
| **M2 数据与机器学习** | **任务**：Python 数据处理与机器学习基本概念。<br>**产物**：小数据集训练与评价 Notebook。<br>**完成**：能解释数据划分、loss 和指标。 |
| **M3 深度学习基础** | **任务**：PyTorch、张量、梯度与训练循环。<br>**产物**：一个可过拟合小样本的模型。<br>**完成**：能解释输入输出 shape 和梯度来源。 |
| **M4 方向与 baseline** | **任务**：按[方向选择决策树](docs/DIRECTION_FIRST_CHOICE.md)扫描候选并筛选论文。<br>**产物**：任务句、非目标、研究简报、候选表和资源预算。<br>**完成**：选出一篇适合复现的 baseline，并保留备选。 |
| **M5 论文与代码** | **任务**：精读论文并阅读官方代码。<br>**产物**：阅读卡、模块映射、风险登记表。<br>**完成**：能画出数据流并定位代码入口。 |
| **M6 复现与评测** | **任务**：预训练评测、单批次测试、完整复现。<br>**产物**：复现日志、配置、指标差异表和[稳定化决定](docs/BASELINE_STABILIZATION_GATE.md)。<br>**完成**：论文目标与本地 baseline 已分开，差距、稳定性和允许主张明确。 |
| **M7 改进与失败分析** | **任务**：按[首次安全改码](docs/SAFE_FIRST_CODE_CHANGE.md)完成一个单变量改进。<br>**产物**：修改前快照、可审查 diff、检查证据、假设卡、有效尝试台账、实验矩阵和消融结果。<br>**完成**：只有 `READY_FOR_CHANGE` 的 baseline 进入改进；修复 / 重构 / 方法改动已分离；无效运行、有效负结果和证据不足已分开，继续实验能说明新增信息。 |
| **M8 分析与表达** | **任务**：结果分析、写作和复盘。<br>**产物**：研究报告、图表、失败项、[继续 / 转向 / 停止决定](docs/RESEARCH_STOPPING_AND_PIVOT.md)和下一步；按需形成[交接入口](docs/RUN_HANDOFF_REPLAY.md)、[知识条目](docs/RESEARCH_KNOWLEDGE_CAPTURE.md)和[产物保留决定](docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)。<br>**完成**：表达、共享与决定不混级；停止对象明确；跨运行经验可检索、可核验、可 supersede，每个结论仍回到原证据。 |

每次复盘只选择一种状态：

| 状态 | 下一步 |
| --- | --- |
| **PASS** | 产物与完成标准均通过，进入下一里程碑。 |
| **STAY** | 目标仍正确但证据不足，缩小任务并留在当前里程碑。 |
| **PAUSE** | 课程、健康、算力或外部条件中断；保存恢复入口，不制造虚假进度。 |
| **PIVOT** | baseline、数据、资源或假设不再可行；记录原因并切换备选。 |
| **ASK** | 同一阻塞重复出现，带调试卡、日志和明确问题向导师、同伴或维护者求助。 |

如果 M6 尚未复现成功，不要急着“做创新”。先把环境、数据、预处理、评测脚本、随机种子和官方 Issue 逐项核对；可信的复现失败本身也是研究结果。

## 把阶段目标变成今天的任务

里程碑规定能力目标，不规定每个人必须使用相同课表。真正开始工作前，用[原子科研任务卡](templates/06-daily-task-card.md)把当前目标缩成一次能够结束、能够检查的科研会话：

```text
原子任务 = 动作 + 对象 + 范围 + 产物 + 验收方式 + 时间盒
```

不要写“今天学 PyTorch”或“今天读论文”。可以写成：

```text
在 60 分钟内运行官方推理示例，记录输入输出 shape、命令和日志路径；
以示例成功退出，并且能够解释每个关键张量的含义作为验收标准。
```

根据当天可用时间选择任务粒度，而不是为了填满时间无限扩展范围：

- **约 30 分钟**：扫描一篇候选论文、复现并记录一个报错、核对一个数据字段，或补完阅读卡的一小节；
- **约 60 分钟**：跑通一个官方 demo 或小数据测试、画出一个模块的数据流，或完成一个明确问题的定向阅读；
- **约 120 分钟**：完成“运行—观察—受控改动—验证—记录”的小闭环，但仍只回答一个主要问题。

每次执行遵守五条规则：

1. 只设置一个必须完成的主任务，可以另设一个不影响验收的可选任务；
2. 开始前写清产物路径、验收标准、最大范围和停止条件；
3. 达到时间盒仍未完成时，保存错误、已排除原因和下一次最小动作，不临时扩展成无边界调试；
4. 用代码、笔记、图表、日志、配置或决策记录判断完成，不用“学习了多久”判断；
5. 每周保留机动时间；未完成任务先重新估时和缩小范围，再决定是否进入下周。

时间档位只是任务拆分示例，不是工时要求。课程、考试、健康或算力条件变化时可以暂停或延长；不能删掉阶段产物，也不要用熬夜补偿不合理的计划。

## 完整科研工作流

完整科研不是从选题单向走到论文，而是一个可以暂停、核验、优化或转向的循环：

```text
研究定义 → 文献发现 → 论文与代码映射 → baseline 复现
    → 假设生成 → 实验设计与执行 → 分析与决策 → 写作与归档
                                      └── 优化或转向 ──┘
```

本页只保留阶段地图。执行细节、通过条件和推荐产物统一放在[零基础 AI 科研核心工作流](docs/CORE_RESEARCH_WORKFLOW.md)，避免第一次访问就被数百行协议淹没。

| 当前阶段 | 下一项可验收产物 |
| --- | --- |
| **0 项目台账** | 新项目直接建立入口；已有代码库按[最小接入指南](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)先映射现有记录，只补缺口，不维护第二套台账。 |
| **1 方向与 baseline** | 两到三个候选完成低成本预检；保留一个通过项和一个备选项。 |
| **2 文献核验** | 按[论文发现与原文回溯](docs/PAPER_DISCOVERY_FIRST_PASS.md)分开记录发现入口、书目身份、原文版本和官方代码；检索式、筛选与停止条件可复查。 |
| **3 论文—代码映射** | 核心论文阅读卡能连接公式、文件、shape、配置和结果。 |
| **4 baseline 复现** | 环境、数据、命令、日志和评测齐全；按[稳定化门](docs/BASELINE_STABILIZATION_GATE.md)区分论文目标、本地 baseline 与候选方法，并作四选一决定。 |
| **5 研究问题** | 失败现象转成可证伪假设，并写出反例与最小验证实验。 |
| **6 实验设计** | 评价协议先冻结；先按[首次安全改码](docs/SAFE_FIRST_CODE_CHANGE.md)审查修改范围与最低测试，再按[公平调参与搜索预算](docs/FAIR_TUNING_BUDGET.md)审计 baseline 与候选的搜索机会；全部 trial 和确认运行可追踪。 |
| **7 分析与表达** | 观察、解释与主张分开；反例、替代解释和图表来源已审计。 |
| **8 交接与归档** | 关键运行完成对应深度的复查并取得产物保留决定；可复用失败 / 决定进入薄索引，真实复用经过候选排除、身份核验和结果写回；实际提交版本、评审、回复和负面结果已冻结。 |

四个停止检查点是：**G1 方向与 baseline、G2 文献与假设、G3 复现与实验、G4 证据与交付**。没有通过当前门控时，不进入下一阶段，也不允许 AI 自动批准关键研究判断。

第一次只需要完成“一份研究简报 → 一个可运行 baseline → 一次单变量实验 → 一份有边界的结果报告”。完整规范请在用到对应阶段时再打开：

- [核心工作流手册](docs/CORE_RESEARCH_WORKFLOW.md)
- [真实代码库最小接入](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)
- [第一次安全修改论文代码](docs/SAFE_FIRST_CODE_CHANGE.md)
- [运行交接与冷启动复查](docs/RUN_HANDOFF_REPLAY.md)
- [实验产物保留、归档与安全清理](docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)
- [导师与组会反馈闭环](docs/MENTOR_FEEDBACK_LOOP.md)
- [全部执行指南索引](docs/README.md)
- [数据集审计](docs/DATASET_FIRST_AUDIT.md)
- [评价协议](docs/EVALUATION_FIRST_SPEC.md)
- [公平调参与搜索预算](docs/FAIR_TUNING_BUDGET.md)
- [负结果、无进展与研究停止门](docs/RESEARCH_STOPPING_AND_PIVOT.md)
- [从实验记录到可检索研究知识](docs/RESEARCH_KNOWLEDGE_CAPTURE.md)
- [第一次检索并安全复用研究知识](docs/FIRST_KNOWLEDGE_REUSE_DRILL.md)
- [结果到主张](docs/RESULT_TO_CLAIM.md)
- [模板最短路径](templates/README.md)

## 卡住时如何求助

求助前先使用[调试与求助卡](templates/10-debug-help-request.md)把“跑不起来”转换成别人可以复查的问题，再按[第一次向开源上游求助与贡献](docs/UPSTREAM_HELP_AND_CONTRIBUTION.md)判断它属于本地使用、社区问答、上游缺陷、研究分歧还是私密安全问题：

```text
目标与预期行为
  → 实际行为与第一个关键报错
  → 完整命令、commit、配置和环境
  → 最小可复现样例
  → 原始查询、已开候选和负面发现
  → 一个所有者、一个渠道、一个具体问题
  → 回复作为候选在当前身份下验证
  → 结果写回原记录并决定是否更新知识
```

最小可复现不等于只截最后一行报错。应从未修改的官方示例开始，使用最小公开数据或合成数据复现，保留必要代码、配置、完整 traceback 和环境版本；删除无关模块后重新运行，确认精简后的样例仍能触发同一问题。

检索无命中只表示当前入口没有可用条目，不证明没有原因或存在上游 bug。不要让自助搜索变成死路：求助时附上搜索原文、已查看位置、已排除原因、最小观察和共享权限。导师、同伴或维护者的回复先标记为 `ANSWER_CANDIDATE`，在当前 commit、配置与新临时目录中验证后，才写成 `VERIFIED_WITHIN_SCOPE`；一次直接路径错误可以只改善现有文档，不必新建知识卡。

选择正确的求助位置：

- **第一次使用时误点、犹豫或不知道怎样开始**：使用[零基础首次使用反馈](https://github.com/Starry-cz/ai-research-workflow/issues/new?template=beginner-first-use.yml)，只写实际发生了什么；不要求提出改法或外部依据。导师、学习小组和维护者可按[首次使用可用性观察](docs/BEGINNER_USABILITY_OBSERVATION.md)组织不提示答案的复查；
- **本仓库的链接、表述、路线或模板有问题**：先搜索已有 Issue，再使用[仓库问题表单](https://github.com/Starry-cz/ai-research-workflow/issues/new/choose)提交位置、问题、预期改进和证据；
- **第三方项目的安装、API 或代码错误**：先读该项目 README、支持范围、贡献 / 安全说明和已有 Issue；只有在未修改的受支持版本上形成公开最小复现，才把状态升级为 `UPSTREAM_ISSUE_READY`；
- **自己的改动或私有数据导致的问题**：先缩成公开或合成数据的最小样例，与同伴、导师或代码维护者核对；
- **研究问题、实验协议和结论解释**：带着假设、`run_id`、对照、失败项和具体请求与导师或合作者讨论，不能只提交代码报错；
- **含有密钥、个人信息、未公开数据或匿名审稿材料**：不得粘贴到公开 Issue、聊天记录或外部 AI 服务。

完整的支持范围和信息安全边界见 [SUPPORT.md](SUPPORT.md)；发现安全漏洞时使用项目指定的私密报告渠道，不在普通 Issue 公开细节。

## 周会、导师与协作沟通

周会不是工作量展示，而是用最短时间获得高质量反馈。使用[每周与阶段复盘](templates/05-weekly-review.md)准备以下内容：

```text
一句话结论：本周最重要的新证据或判断是什么
证据：对应哪个实验、图表、代码或文献位置
阻塞：目前卡在哪里，已经排除了哪些原因
请求：希望导师或同伴回答哪个具体问题
下一步：根据不同反馈分别采取什么行动
```

汇报时先在 30 秒到 1 分钟内讲结论、阻塞和请求，再补必要背景。每一页只服务一个信息点，不确定内容要明确标记。没有正向结果时，也可以汇报复现差异、失败实验、阅读结论和已经排除的原因。

组会允许汇报调试信号和初步观察，但页面要按[证据等级与表达边界](docs/EVIDENCE_READINESS_AND_SHARING.md)写明 V 等级、共享范围、尚缺检查与允许表述。组会认可不是同行评审，公开 artifact 也不自动成为论文主张。

会后立即按[反馈闭环](docs/MENTOR_FEEDBACK_LOOP.md)记录：原始反馈与自己的解释、目标对象、接受 / 部分接受 / 有证据拒绝 / 延期 / 待澄清 / 冲突决定，以及负责人、产物、截止、验收和重开条件。口头建议没有进入行动和再次验收，不能算项目状态已经更新。关键运行将被他人用于决策、复算图表或接续工作时，再按[运行交接与冷启动复查](docs/RUN_HANDOFF_REPLAY.md)声明 H0–H3 深度。

**阶段验收**：协作者能够在一分钟内理解当前结论、证据、阻塞、待决策问题和下一步。

## AI 在科研中的正确位置

### 适合交给 AI 辅助

- 解释报错、配置环境和整理依赖；
- 把论文模块、公式、shape 和代码入口整理成表格；
- 搜索候选资料并生成待核验清单；
- 生成测试、检查遗漏和比较代码差异；
- 把实验日志整理为结构化记录；
- 检查写作中的逻辑跳跃、未定义符号和证据缺口。

### 必须由研究者负责

- 研究问题是否值得做；
- 文献是否真实且支持对应表述；
- 数据、划分、预处理和评价协议是否正确；
- 代码修改是否改变 baseline 的公平性；
- 实验是否真实运行、结果是否完整披露；
- 结论、署名、伦理和投稿合规。

### 复杂任务的通用任务卡

```text
目标：要完成什么？
输入：允许读取哪些论文、数据、代码和文件？
边界：不能修改什么，不能假设什么？
步骤：如何拆成可以单独验收的子任务？
检查：必须运行哪些测试、对照或核验？
交付：必须留下哪些文件、日志、结果和失败项？
```

执行前让 AI 复述目标和边界；执行后按原始清单逐项标记“完成、部分完成、未完成、待验证”。新对话或独立检查可以用于反驳方案，但不能替代回到原文和实验核验。

零基础阶段建议采用“AI 执行子任务、研究者通过门控”的协作方式。在 G1–G4 质量门控、数据或评价协议变化、实验结果解释和最终对外发布前必须暂停人工审核，不应默认自动批准。

## 工具与入口导航

按当前任务选择一个主入口，完成表中产物后再决定是否扩展。更多课程和项目见[GitHub 科研入门资源目录](docs/GITHUB_RESOURCE_CATALOG.md)；该目录按阶段和用途组织，并在点开前说明主要语言、最低前置、账号或算力门槛，不按 Star 排名。

**最常用的六个入口**

- **第一次配置环境**：[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)
- **理解第一次训练、验证与测试**：[第一个机器学习闭环](docs/ML_FIRST_LOOP.md)
- **选择研究方向或首篇 baseline**：[方向选择决策树](docs/DIRECTION_FIRST_CHOICE.md)
- **开始复现已有论文代码**：[真实代码库最小接入](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)
- **遇到报错或重复失败**：[调试与求助卡](templates/10-debug-help-request.md)
- **整理课程与外部项目**：[GitHub 科研入门资源目录](docs/GITHUB_RESOURCE_CATALOG.md)

**基础与学习**

- **补计算机基础**：[CS 自学指南](https://github.com/PKUFlyingPig/cs-self-learning) / [OSSU CS](https://github.com/ossu/computer-science)。<br>**留下**：选定课程与可运行作业，不要求一次学完。
- **第一次配置工具链**：[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)。<br>**留下**：解释器路径、独立环境、仓库历史、环境快照和第一次 commit。
- **继续学终端、Git 与调试**：[Missing Semester](https://missing.csail.mit.edu/)。<br>**留下**：命令记录、Git 提交和调试练习。
- **学经典机器学习**：[ML for Beginners](https://github.com/microsoft/ML-For-Beginners)。<br>**留下**：一个完整的训练—验证—测试 Notebook。
- **理解第一个 ML 闭环**：[第一个机器学习训练—验证—测试闭环](docs/ML_FIRST_LOOP.md)。<br>**留下**：用仓库内已运行示例解释样本、loss、数据划分、泄漏和结论边界。
- **学深度学习与 PyTorch**：[动手学深度学习](https://github.com/d2l-ai/d2l-zh) / [PyTorch Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning)。<br>**留下**：可修改的训练循环和小项目。
- **从零理解神经网络**：[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)。<br>**留下**：手写反向传播、MLP 或小型语言模型。
- **按当前任务补数学**：[按任务触发的数学补课指南](docs/MATH_ON_DEMAND.md) / [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io) / [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)。<br>**留下**：一张含符号、shape、假设、玩具数值与代码位置的数学概念卡。
- **选择方向与研究问题**：[方向选择决策树](docs/DIRECTION_FIRST_CHOICE.md) / [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)。<br>**留下**：任务句、非目标、候选比较、研究简报、假设、风险与资源约束。
- **规划科研成长与项目训练**：[Learning Research](https://github.com/pengsida/learning_research)。<br>**留下**：把广度学习、深度复现、独立项目和每周交流组织成个人路线。
- **组织完整科研流程**：[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)。<br>**留下**：调研、写作、审稿和投稿清单。
- **参考阶段化科研编排**：[AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)。<br>**留下**：学习阶段产物、人工门控、预算约束、证据核验和版本化归档；新手应优先理解流程，不把自动输出视为已验证研究。

**文献、数据与复现**

- **查论文**：[论文发现与原文回溯](docs/PAPER_DISCOVERY_FIRST_PASS.md) / [Google Scholar](https://scholar.google.com/) / [DBLP](https://dblp.org/)。<br>**留下**：只选一个发现入口，再留下稳定标识、实际原文版本和官方代码状态。
- **查顶会论文与评审**：[CV Paper Portal](https://hongsong-wang.github.io/CV_Paper_Portal/) / [OpenReview](https://openreview.net/)。<br>**留下**：正式论文版本、评审与回复记录。
- **管理文献与重复版本**：[Zotero](https://www.zotero.org/) / [重复项说明](https://www.zotero.org/support/duplicate_detection)。<br>**留下**：主记录、来源标签、版本链、阅读状态和可核验元数据。
- **查截止时间**：[CCFDDL](https://ccfddl.com/)。<br>**留下**：带时区的时间表，最终以官网为准。
- **查代码与数据**：[GitHub](https://github.com/) / [Hugging Face Datasets](https://huggingface.co/datasets)。<br>**留下**：官方仓库、commit、数据 revision、许可证和评测协议。趋势论文页只用于发现候选，不能替代代码与基准核验。
- **审计数据集**：[零基础数据集审计指南](docs/DATASET_FIRST_AUDIT.md) / [Hugging Face Dataset Cards](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md)。<br>**留下**：来源、许可证、revision、schema、划分、泄漏、隐私与可重建证据。
- **分层搜索与阅读论文**：[How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)。<br>**留下**：为检索结果分层，只对核心论文完成精读、讨论和可复用笔记。
- **学论文到代码映射**：[Annotated Deep Learning](https://github.com/labmlai/annotated_deep_learning_paper_implementations)。<br>**留下**：公式—代码—shape 对照表。

**实验、协作与表达**

- **接到第一项导师任务**：[任务授权边界](docs/FIRST_MENTOR_TASK_BOUNDARY.md) / [已填写示例](examples/first-workflow-drill/task-authority.md)。<br>**留下**：区分可直接执行、先确认和停止升级；技术权限不等于任务授权。
- **向开源上游求助或贡献**：[上游求助与贡献指南](docs/UPSTREAM_HELP_AND_CONTRIBUTION.md) / [已填写路由示例](examples/first-workflow-drill/upstream-routing.md)。<br>**留下**：确认问题所有者、最小复现、正确渠道、PR 范围和私密信息边界。
- **冻结评价协议**：[零基础评价协议指南](docs/EVALUATION_FIRST_SPEC.md) / [scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)。<br>**留下**：主指标、实现、聚合、阈值、统计单位、不确定性、人工评价和决策门槛。
- **从结果形成主张**：[从实验结果到可辩护主张](docs/RESULT_TO_CLAIM.md) / [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)。<br>**留下**：结果完整性、配对错误、替代解释、图表来源、主张范围与证据状态。
- **判断结果能否汇报、共享或写入论文**：[实验结果证据等级与表达边界](docs/EVIDENCE_READINESS_AND_SHARING.md) / [已填写教学示例](examples/first-workflow-drill/evidence-readiness.md)。<br>**留下**：分开判断 V0–V4 验证成熟度、S0–S3 共享权限、允许表述和用途状态。
- **长期无提升、负结果或预算耗尽时做决定**：[负结果、无进展与研究停止门](docs/RESEARCH_STOPPING_AND_PIVOT.md) / [已填写教学决定](examples/first-workflow-drill/stopping-decision.md)。<br>**留下**：区分无效运行、有效负结果和证据不足，只为能改变决定的新证据继续实验。
- **把失败和决定变成可检索、可安全复用的知识**：[研究知识提炼指南](docs/RESEARCH_KNOWLEDGE_CAPTURE.md) / [第一次知识复用演练](docs/FIRST_KNOWLEDGE_REUSE_DRILL.md)。<br>**留下**：按原始症状召回候选；无命中时把查询、负面发现和权限交给唯一所有者；回复验证后再改善入口、新建或 supersede。
- **第一次修改论文代码**：[第一次安全修改论文代码](docs/SAFE_FIRST_CODE_CHANGE.md) / [GitHub AI 代码审阅](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code)。<br>**留下**：修改前 baseline、改动类别、可审查 diff、按风险选择的检查和准入决定。
- **管理大文件与数据版本**：[Git LFS](https://git-lfs.com/) / [DVC](https://github.com/treeverse/dvc)。<br>**留下**：大文件指针、数据版本与外部存储位置；首个小实验只需先用 `.gitignore`、数据清单和校验值，规模增长后再引入。
- **设计实验与调参**：[公平调参与搜索预算](docs/FAIR_TUNING_BUDGET.md) / [Tuning Playbook](https://github.com/google-research/tuning_playbook)。<br>**留下**：科学与干扰变量、baseline / 候选搜索机会、完整 trial 台账、冻结配置和确认性实验。
- **规范研究代码**：[Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)。<br>**留下**：依赖、训练、评测、权重和复现命令。
- **设计论文配图**：[CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure)。<br>**留下**：图示草图、变量说明、可编辑源文件和人工校验。

## 可直接复用的模板

不要按编号顺序填写，也不要一次复制全部模板。首页的[最小模板包](#只启用当前阶段的最小模板包)负责选择；[模板目录](templates/README.md)负责说明每张模板的触发条件与完成标准。

第一次填写前先看[已完成的实验演练](examples/first-workflow-drill/README.md)。进入真实项目时先使用[最小接入指南](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)把字段映射到现有 README、tracker 或表格；只有现有系统无法承载时，才复制当前阶段的一张模板。示例数值来自仓库内脚本和配置，用于说明记录方法，不是论文结果。

## 推荐项目结构

全新项目第一次只建立能运行和复查的最小骨架；已有论文或实验室仓库不要照此搬家，先做[真实代码库最小接入](docs/ADOPT_WORKFLOW_IN_EXISTING_PROJECT.md)：

```text
research-project/
├── README.md              # 问题、安装、运行、结果和下一步
├── .gitignore             # 排除密钥、缓存、数据和大文件
├── environment/           # Python 与依赖
├── data/README.md         # 数据来源、版本、划分和本地路径
├── src/                   # 脚本或第一个 Notebook
├── configs/               # 本次运行的配置
└── experiments/           # 命令、日志、指标和失败
```

只有在文献、数据版本、实验数量、论文写作或协作规模增长时才扩展目录。完整升级触发条件和 L2–L3 结构见[科研项目结构指南](docs/PROJECT_STRUCTURE.md)。

## 新手常见误区

| 常见误区 | 更可靠的做法 |
| --- | --- |
| 收藏过多课程 | 每次只选一个主资源，并留下可运行产物。 |
| 数学尚未学完 | 围绕当前任务按需补数学，再用数值和代码核对。 |
| 下载即直接使用 | 先核对发布者、许可证、版本、隐私、划分和再分发边界。 |
| 有权限即修改 | 先确认本次任务允许的分支、数据、预算、共享修改与对外动作。 |
| 报错即提 Issue | 先验证支持范围、未修改代码、公开最小复现和真正的问题所有者。 |
| 指标越多越好 | 先固定一个对应主张的主指标，再用辅助指标解释代价与边界。 |
| 跑通即复现 | 区分官方评测、单批次测试、完整训练和结果容差。 |
| 新论文即 baseline | 首个 baseline 更看重代码、训练、评测、算力和可理解性。 |
| 看不懂就问 AI | 先形成自己的问题清单，再核对原文、公式和代码。 |
| 多模块同时改 | 一次一个主要变量，否则无法解释贡献。 |
| 只报最佳结果 | 预先确定协议，报告波动、失败和选择规则。 |
| 指标高即成立 | 先核对配对错误、反例、替代解释和主张所需的额外证据。 |
| AI 写完就投稿 | 作者必须理解、核验、修改并承担全部责任。 |
| 一次失败受影响 | 把反馈当信息，把复现失败和拒稿纳入正常迭代。 |

## 方法论参考

本仓库在独立整理零基础 AI 科研流程时，参考并重新组织了以下公开项目中的通用方法：

- [Learning Research](https://github.com/pengsida/learning_research)：吸收阶段化成长、项目制训练、科研五项能力、实验记录和研究展示等思路；其中部分案例面向 3D Vision，使用时应结合自己的方向调整。
- [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)：吸收阶段产物、人工门控、`PROCEED / REFINE / PIVOT` 决策、资源预算、声明核验和版本化归档等流程设计；本仓库将这些机制转换为新手可手动执行的检查清单，不承诺自动生成的研究结果天然可靠。
- [Made With ML](https://github.com/GokuMohandas/Made-With-ML)：吸收“先用一条可运行示例理解完整链路，再逐步拆成脚本和可追踪实验”的教学组织方式；其生产化工程内容不作为零基础起步的强制要求。
- [Tuning Playbook](https://github.com/google-research/tuning_playbook)：吸收科学变量、干扰变量、调参预算、公平比较和训练曲线诊断等实验原则；具体搜索空间和运行次数必须按任务调整。

这里提供的是面向零基础场景的重新编排，不是上述项目的镜像或替代文档。具体功能、适用条件与最新变化请以原仓库说明为准。

## 维护方式

机器可读的工具信息保存在 [tools.yml](tools.yml)，新增与修改规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

仓库的持续问题审计、经验材料对照和实际修改记录保存在[持续改进记录](docs/IMPROVEMENT_LOG.md)。新增观点应先记录“当前问题—对照证据—适用边界—采取行动”，再决定是否进入主 README。

最近一次外部入口核验见 [2026-08-09 URL 与 GitHub 项目状态审计](reports/URL_AUDIT_2026-08-09.md)。动态网络结果只表示检查时刻的状态，不代表资源质量或永久可用性。

新增资源时至少记录：原始链接、适用阶段、主要语言、最低进入要求、建议产物、维护状态、许可证、已知限制和最后核验日期。资源应能解决明确问题，不能只因为 Star 高或传播广而加入；费用、账号、云服务和算力要求不得写成永久不变的承诺。

建议维护频率：

- 每月检查失效链接和停止维护的项目；
- 每季度复核项目说明、许可证、登录和付费要求；
- 投稿季前核验 deadline、模板、匿名、伦理和 AI 使用政策；
- 每次更新保持 README 与 `tools.yml` 一致。

## 许可、引用与版本

- 面向读者的主要变化记录在 [CHANGELOG.md](CHANGELOG.md)，精确修改历史以 Git commit 为准；
- 在正式版本发布前引用本仓库时，请记录仓库名称、GitHub URL、访问日期和所使用的 commit；
- 当前仓库尚未选择开源许可证。公开可见不等于允许自由复制、修改或分发；在根目录出现正式 `LICENSE` 文件前，应按默认版权限制处理；
- 作者确认许可范围、引用署名和首个版本号后，再添加 `LICENSE`、`CITATION.cff` 和对应 GitHub Release。外部资源仍分别遵循各自许可证与使用条款。

## 免责声明

本项目是科研入门、工具导航与工作流参考，不构成论文发表、学术评价、数据安全、科研合规或投稿成功保证。工具功能、Star、价格、模型能力、数据覆盖、会议规则和服务条款会变化；涉及关键科研决策时，应访问官方来源并进行人工核验。
