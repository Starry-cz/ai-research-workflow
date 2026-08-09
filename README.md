# AI 科研工作流工具库：零基础入门版

面向第一次接触计算机科研、人工智能、机器学习和深度学习的学生与自学者。

这个仓库不是工具收藏夹，也不承诺“用 AI 自动发论文”。它提供的是一条可以执行、检查和复盘的入门路线，帮助你从“不会检索、不会读论文、不会跑代码”，逐步走到：

```text
选定一个可执行的小方向
  → 读懂一篇代表性论文
  → 跑通官方代码与预训练模型
  → 复现一个可信 baseline
  → 完成一次单变量改进实验
  → 用证据写出研究报告或论文初稿
```

> AI 可以帮助检索、解释、配置环境、阅读代码和检查遗漏，但研究者必须理解并核验论文、代码、数据、实验和结论。

## 目录

- [这个仓库适合谁](#这个仓库适合谁)
- [第一次使用：从这里开始](#第一次使用从这里开始)
- [30 秒选择入口](#30-秒选择入口)
- [先完成一次工作流演练](#先完成一次工作流演练)
- [零基础能力地图](#零基础能力地图)
- [可调节的八周入门路线](#可调节的八周入门路线)
- [把八周路线变成今天的任务](#把八周路线变成今天的任务)
- [完整科研工作流](#完整科研工作流)
- [卡住时如何求助](#卡住时如何求助)
- [周会、导师与协作沟通](#周会导师与协作沟通)
- [AI 在科研中的正确位置](#ai-在科研中的正确位置)
- [工具与入口导航](#工具与入口导航)
- [可参考的 GitHub 入门资源](#可参考的-github-入门资源)
- [推荐组合](#推荐组合)
- [可直接复用的模板](#可直接复用的模板)
- [推荐项目结构](#推荐项目结构)
- [新手常见误区](#新手常见误区)
- [方法论参考](#方法论参考)
- [维护方式](#维护方式)
- [许可、引用与版本](#许可引用与版本)

## 这个仓库适合谁

### 主要面向

- 没有科研经历，不知道选题、读论文和做实验分别要做什么；
- Python、Git、Linux 或深度学习基础不扎实；
- 能看懂少量代码，但没有完整跑通过论文仓库；
- 收藏了很多课程和工具，却始终没有形成自己的科研闭环；
- 希望使用 AI 辅助科研，同时避免幻觉引用、虚假实验和过度依赖。

### 本仓库重点解决

| 新手问题 | 本仓库提供的解决方式 |
| --- | --- |
| 不知道从哪里开始 | 能力自测、起步清单和八周路线 |
| 基础很多，不知道学到什么程度 | “够用即可”的最低能力门槛和阶段验收 |
| 论文读完仍不会实现 | 论文—公式—图—代码—张量—实验映射 |
| GitHub 项目跑不起来 | 从环境、预训练模型、单批次到完整训练的复现顺序 |
| 一改代码就失控 | 单变量改动、实验卡和回退机制 |
| AI 给出的内容真假难辨 | 来源分层、风险登记和人工验收 |
| 实验做了很多却写不成论文 | 从研究问题到证据表格的一一对应 |

## 第一次使用：从这里开始

### 30 秒选择入口

不需要从头读完整份 README。先选择最接近自己的状态：

- **L0：不会终端、Git 或 Python 环境** → 先做[零基础准备检查表](templates/00-readiness-checklist.md)，按[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)留下环境记录和第一次 commit，再完成[第一次工作流演练](examples/first-workflow-drill/README.md)和八周路线第 1–3 周；
- **L1：能运行 Notebook，但没有复现过论文** → 先完成[第一个机器学习闭环](docs/ML_FIRST_LOOP.md)和[第一次工作流演练](examples/first-workflow-drill/README.md)，再建立[研究简报](templates/01-research-brief.md)和[文献检索账本](templates/07-literature-search-log.md)，从[首篇 baseline 筛选表](docs/CORE_RESEARCH_WORKFLOW.md#首篇-baseline-筛选表)进入第 4–6 周；
- **L2：已经跑通代码，但实验不可解释或不可复现** → 直接使用[复现规划](templates/03-reproduction-plan.md)与[实验卡](templates/04-experiment-card.md)，重点执行质量门控、单变量实验和失败分析；
- **正在投稿、回复评审或转投** → 使用[投稿、评审与版本归档卡](templates/09-submission-review-archive.md)，先核验当前 venue 规则并冻结实际送审版本。

无法判断等级时，从 L0 检查表开始；已经掌握的项目直接跳过，但对应的最低产物必须能够拿出来验证。

### 只启用当前阶段的最小模板包

仓库提供的是工具箱，不是要求一次填完的表格作业。任何时候只打开当前阶段需要的模板；完成后归档，再进入下一包。

| 当前阶段 | 最小模板包与升级条件 |
| --- | --- |
| **L0 工具起步** | 只填[准备检查表](templates/00-readiness-checklist.md)，其余先看[已填写演练](examples/first-workflow-drill/README.md)，不要复制全部空模板。<br>**升级**：能独立运行脚本并找到日志、配置和指标。 |
| **L1 选方向** | [研究简报](templates/01-research-brief.md) + [文献检索账本](templates/07-literature-search-log.md) + [baseline 准入卡](templates/11-first-baseline-gate.md)。<br>**升级**：候选通过低成本预检并有备选。 |
| **L2 做复现** | [论文阅读卡](templates/02-paper-reading-card.md) + [复现规划](templates/03-reproduction-plan.md)；取得数据后启用[数据集卡](templates/13-dataset-card.md)。<br>**升级**：官方评测或目标复现达到预设判定。 |
| **L3 做实验** | 运行前用[实验卡](templates/04-experiment-card.md)和[评价协议卡](templates/14-evaluation-spec.md)，运行后用[结果—主张审计](templates/15-result-claim-audit.md)。<br>**升级**：主张、反证、图表和结论均可回到证据。 |

其他模板只在事件发生时启用：任务过大用[原子任务卡](templates/06-daily-task-card.md)，需要组会用[每周复盘](templates/05-weekly-review.md)，迁移算力用[迁移清单](templates/08-compute-data-environment-checklist.md)，卡住求助用[调试卡](templates/10-debug-help-request.md)，公式阻塞用[数学概念卡](templates/12-math-concept-card.md)，进入投稿再用[投稿归档卡](templates/09-submission-review-archive.md)。

同一时间建议只维护一个阶段门控、一个当前任务 / 实验记录，以及一个确有阻塞才启用的按需卡。导师或实验室已有等价记录时直接复用，不为匹配本仓库重复填写。

### 第一次执行的五件事

不要先下载几十个项目。下面五件事描述完整起步阶段，不要求同一天完成：

1. 用[零基础准备检查表](templates/00-readiness-checklist.md)判断自己目前在哪一层；
2. 按[L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)安装并核验 Git、Python 和独立环境，不混用不同系统的命令；
3. 从一个成熟方向列出两到三个候选，使用[首篇真实 baseline 准入卡](templates/11-first-baseline-gate.md)完成低成本预检，再选择有官方代码、训练脚本和可承受算力的一篇；
4. 先运行官方预训练模型的评测或演示，不要立刻从头训练；
5. 建立[复现规划](templates/03-reproduction-plan.md)，把缺失信息写入风险登记表；如果需要云端算力或迁移大数据，再完成[算力、数据与环境迁移清单](templates/08-compute-data-environment-checklist.md)。

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

第一天不要求提出创新点。只要能够解释“我要复现哪篇论文、为什么选择它、需要哪些数据和算力、下一步运行什么命令”，就已经完成起步。

## 先完成一次工作流演练

在下载真实论文代码前，建议先完成[第一次可审计实验演练](examples/first-workflow-drill/README.md)。它使用 Python 标准库和合成数据，在 CPU 上演示：

```text
冻结问题与配置
  → 运行固定 seed 的调试实验
  → 保存命令、环境、日志与指标
  → 按预先声明的 seed 集合运行比较实验
  → 汇总全部计划运行与波动
  → 写出不超过证据范围的结论
```

这个演练的目的不是取得高准确率，而是让你第一次看见 `question → config → run_id → log → metrics → decision` 如何连成证据链。它不是论文复现，也不能作为算法创新、模型优越性或真实数据泛化能力的证据。

完成后再进入真实 baseline。此时至少应该能够回答：哪个文件固定了变量，哪条命令生成结果，哪个指标来自哪个 `run_id`，失败运行放在哪里，以及为什么不能只挑最好的一次。

如果还不能解释样本、特征、标签、loss、指标以及训练 / 验证 / 测试集的不同职责，先完成[第一个机器学习训练—验证—测试闭环](docs/ML_FIRST_LOOP.md)，再进入论文代码。

## 零基础能力地图

### 能力分级

| 等级 | 当前状态与下一阶段目标 |
| --- | --- |
| L0 工具零基础 | **当前**：不熟悉终端、Git、Python 环境和 Jupyter。<br>**下一步**：能克隆仓库、创建环境、安装依赖、运行脚本。 |
| L1 AI 基础入门 | **当前**：能运行 Notebook，但不熟悉训练、验证和指标。<br>**下一步**：能修改样例、解释数据划分、训练循环和评价指标。 |
| L2 论文复现入门 | **当前**：能跑通训练代码，但无法解释论文与实现对应关系。<br>**下一步**：能复现 baseline、定位差异并形成复现报告。 |
| L3 研究实践入门 | **当前**：能复现论文，准备尝试改进。<br>**下一步**：能提出可证伪假设、完成对照实验和失败分析。 |

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
| 发现问题 | 能说明问题为什么重要、现有方法在哪里失效，并形成研究简报 |
| 设计方案 | 能提出可证伪假设，提前写出预期现象、对照组和最小实验 |
| 完成实验 | 能复现 baseline，保留配置、日志、失败项和公平对照 |
| 论文表达 | 能让每个主要主张对应到实验、图表、推导或可靠文献 |
| 研究展示 | 能用五分钟讲清问题、方法、证据、局限和下一步，并回答质疑 |

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
| 终端与 Git | 克隆一个仓库，完成一次小修改并查看 diff |
| Python | 写一个读取数据、调用函数并保存结果的小脚本 |
| NumPy / Pandas | 读取数据，检查缺失值、分布和数据类型 |
| 机器学习 | 完成一个训练—验证—测试闭环并解释指标 |
| PyTorch | 写出 Dataset、DataLoader、模型、loss 和训练循环 |
| 论文阅读 | 完成一张有证据位置的论文阅读卡 |
| 按需数学 | 完成一张[数学概念卡](templates/12-math-concept-card.md)，用 shape、玩具数值和代码检查当前公式 |

## 可调节的八周入门路线

八周只是参考节奏。每周时间少可以延长，但不要跳过阶段产物和验收。

| 阶段与主要任务 | 产物与完成标准 |
| --- | --- |
| **第 1 周：工具与环境**<br>终端、Git、Python 环境、Jupyter | **产物**：环境文件、运行日志、第一次 commit。<br>**完成**：能独立重建环境并运行脚本。 |
| **第 2 周：数据与机器学习**<br>Python 数据处理与机器学习基本概念 | **产物**：小数据集训练与评价 Notebook。<br>**完成**：能解释数据划分、loss 和指标。 |
| **第 3 周：深度学习基础**<br>PyTorch、张量、梯度与训练循环 | **产物**：一个可过拟合小样本的模型。<br>**完成**：能解释输入输出 shape 和梯度来源。 |
| **第 4 周：方向与 baseline**<br>扫描方向并筛选代表论文 | **产物**：研究简报、候选论文表、资源预算。<br>**完成**：选出一篇适合复现的 baseline。 |
| **第 5 周：论文与代码**<br>精读论文并阅读官方代码 | **产物**：阅读卡、模块映射、风险登记表。<br>**完成**：能画出数据流并定位代码入口。 |
| **第 6 周：复现与评测**<br>预训练评测、单批次测试、完整复现 | **产物**：复现日志、配置、指标差异表。<br>**完成**：baseline 达到预设容差或差异可解释。 |
| **第 7 周：改进与失败分析**<br>失败案例与单变量改进 | **产物**：假设卡、实验矩阵、消融结果。<br>**完成**：改动的效果能被独立检验。 |
| **第 8 周：分析与表达**<br>结果分析、写作和复盘 | **产物**：研究报告、图表、失败项和下一步。<br>**完成**：每个结论都能回到代码、日志或文献。 |

如果第 6 周仍未复现成功，不要急着“做创新”。把环境、数据、预处理、评测脚本、随机种子和官方 issue 逐项核对，复现失败本身也是需要记录的研究结果。

## 把八周路线变成今天的任务

八周路线规定阶段目标，不规定每个人必须使用相同课表。真正开始工作前，用[原子科研任务卡](templates/06-daily-task-card.md)把本周目标缩成一次能够结束、能够检查的科研会话：

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

时间档位只是任务拆分示例，不是工时要求。课程、考试或身体状态发生变化时，可以延长八周路线；不能删掉阶段产物，也不要用熬夜补偿不合理的计划。

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
| **0 建立台账** | 当前问题、资料入口、最新结果、失败项和下一步写进项目 README。 |
| **1 选择方向与 baseline** | 两到三个候选完成低成本预检；保留一个通过项和一个备选项。 |
| **2 文献发现与核验** | 检索式、筛选、版本和停止条件可复查；关键表述回到原文。 |
| **3 论文与代码映射** | 核心论文阅读卡能连接公式、文件、shape、配置和结果。 |
| **4 baseline 复现** | 环境、数据、命令、日志和评测齐全；结果达到容差或差异可解释。 |
| **5 形成研究问题** | 失败现象转成可证伪假设，并写出反例与最小验证实验。 |
| **6 实验设计与执行** | 评价协议先冻结；一次只改一个主要变量；全部计划运行可追踪。 |
| **7 分析与表达** | 观察、解释与主张分开；反例、替代解释和图表来源已审计。 |
| **8 投稿与归档** | 官方规则已核验；实际提交版本、评审、回复和负面结果已冻结。 |

四个停止检查点是：**G1 方向与 baseline、G2 文献与假设、G3 复现与实验、G4 证据与交付**。没有通过当前门控时，不进入下一阶段，也不允许 AI 自动批准关键研究判断。

第一次只需要完成“一份研究简报 → 一个可运行 baseline → 一次单变量实验 → 一份有边界的结果报告”。完整规范请在用到对应阶段时再打开：

- [核心工作流手册](docs/CORE_RESEARCH_WORKFLOW.md)
- [数据集审计](docs/DATASET_FIRST_AUDIT.md)
- [评价协议](docs/EVALUATION_FIRST_SPEC.md)
- [结果到主张](docs/RESULT_TO_CLAIM.md)
- [模板最短路径](templates/README.md)

## 卡住时如何求助

求助前先使用[调试与求助卡](templates/10-debug-help-request.md)把“跑不起来”转换成别人可以复查的问题：

```text
目标与预期行为
  → 实际行为与第一个关键报错
  → 完整命令、commit、配置和环境
  → 最小可复现样例
  → 已尝试的排查及其结果
  → 希望对方帮助判断的具体问题
```

最小可复现不等于只截最后一行报错。应从未修改的官方示例开始，使用最小公开数据或合成数据复现，保留必要代码、配置、完整 traceback 和环境版本；删除无关模块后重新运行，确认精简后的样例仍能触发同一问题。

选择正确的求助位置：

- **本仓库的链接、表述、路线或模板有问题**：先搜索已有 Issue，再使用[仓库问题表单](https://github.com/Starry-cz/ai-research-workflow/issues/new/choose)提交位置、问题、预期改进和证据；
- **第三方项目的安装、API 或代码错误**：先读该项目 README、文档和已有 Issue；能够在未修改官方代码上复现后，再按上游模板提交；
- **自己的改动或私有数据导致的问题**：先缩成公开或合成数据的最小样例，与同伴、导师或代码维护者核对；
- **研究问题、实验协议和结论解释**：带着假设、`run_id`、对照、失败项和具体请求与导师或合作者讨论，不能只提交代码报错；
- **含有密钥、个人信息、未公开数据或匿名审稿材料**：不得粘贴到公开 Issue、聊天记录或外部 AI 服务。

完整的支持范围和信息安全边界见 [SUPPORT.md](SUPPORT.md)。

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

会后立即记录：收到的反馈、采纳或不采纳的理由、责任人、截止时间和下一次验收标准。口头建议如果没有进入决策日志和下周行动项，就不能算项目状态已经更新。

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

| 任务 | 入口与必须留下的产物 |
| --- | --- |
| **补计算机基础** | [CS 自学指南](https://github.com/PKUFlyingPig/cs-self-learning) / [OSSU CS](https://github.com/ossu/computer-science)<br>选定课程与可运行作业，不要求一次学完。 |
| **第一次配置工具链** | [L0 工具链最小起步指南](docs/L0_TOOLCHAIN_START.md)<br>解释器路径、独立环境、仓库历史、环境快照和第一次 commit。 |
| **继续学终端、Git 与调试** | [Missing Semester](https://missing.csail.mit.edu/)<br>命令记录、Git 提交和调试练习。 |
| **学经典机器学习** | [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)<br>一个完整的训练—验证—测试 Notebook。 |
| **理解第一个 ML 闭环** | [第一个机器学习训练—验证—测试闭环](docs/ML_FIRST_LOOP.md)<br>用仓库内已运行示例解释样本、loss、数据划分、泄漏和结论边界。 |
| **学深度学习与 PyTorch** | [动手学深度学习](https://github.com/d2l-ai/d2l-zh) / [PyTorch Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning)<br>可修改的训练循环和小项目。 |
| **从零理解神经网络** | [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)<br>手写反向传播、MLP 或小型语言模型。 |
| **按当前任务补数学** | [按任务触发的数学补课指南](docs/MATH_ON_DEMAND.md) / [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io) / [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)<br>一张含符号、shape、假设、玩具数值与代码位置的数学概念卡。 |
| **确定研究问题** | [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)<br>研究简报、假设、风险与资源约束。 |
| **规划科研成长与项目训练** | [Learning Research](https://github.com/pengsida/learning_research)<br>把广度学习、深度复现、独立项目和每周交流组织成个人路线。 |
| **组织完整科研流程** | [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)<br>调研、写作、审稿和投稿清单。 |
| **参考阶段化科研编排** | [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)<br>学习阶段产物、人工门控、预算约束、证据核验和版本化归档；新手应优先理解流程，不把自动输出视为已验证研究。 |
| **查论文** | [Google Scholar](https://scholar.google.com/) / [DBLP](https://dblp.org/) / [AI arXiv Paper Portal](https://hongsong-wang.github.io/AI_arXiv_Portal/)<br>检索式、筛选记录和核心论文集合。 |
| **查顶会论文与评审** | [CV Paper Portal](https://hongsong-wang.github.io/CV_Paper_Portal/) / [OpenReview](https://openreview.net/)<br>正式论文版本、评审与回复记录。 |
| **管理文献与重复版本** | [Zotero](https://www.zotero.org/) / [重复项说明](https://www.zotero.org/support/duplicate_detection)<br>主记录、来源标签、版本链、阅读状态和可核验元数据。 |
| **查截止时间** | [CCFDDL](https://ccfddl.com/)<br>带时区的时间表，最终以官网为准。 |
| **查代码与数据** | [GitHub](https://github.com/) / [Papers with Code](https://paperswithcode.com/)<br>官方仓库、commit、数据版本和评测协议。 |
| **审计数据集** | [零基础数据集审计指南](docs/DATASET_FIRST_AUDIT.md) / [Hugging Face Dataset Cards](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md)<br>来源、许可证、revision、schema、划分、泄漏、隐私与可重建证据。 |
| **冻结评价协议** | [零基础评价协议指南](docs/EVALUATION_FIRST_SPEC.md) / [scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)<br>主指标、实现、聚合、阈值、统计单位、不确定性、人工评价和决策门槛。 |
| **从结果形成主张** | [从实验结果到可辩护主张](docs/RESULT_TO_CLAIM.md) / [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)<br>结果完整性、配对错误、替代解释、图表来源、主张范围与证据状态。 |
| **管理大文件与数据版本** | [Git LFS](https://git-lfs.com/) / [DVC](https://github.com/iterative/dvc)<br>大文件指针、数据版本与外部存储位置；首个小实验只需先用 `.gitignore`、数据清单和校验值，规模增长后再引入。 |
| **分层搜索与阅读论文** | [How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)<br>为检索结果分层，只对核心论文完成精读、讨论和可复用笔记。 |
| **学论文到代码映射** | [Annotated Deep Learning](https://github.com/labmlai/annotated_deep_learning_paper_implementations)<br>公式—代码—shape 对照表。 |
| **设计实验与调参** | [Tuning Playbook](https://github.com/google-research/tuning_playbook)<br>实验目标、变量分类、曲线和决策。 |
| **规范研究代码** | [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)<br>依赖、训练、评测、权重和复现命令。 |
| **设计论文配图** | [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure)<br>图示草图、变量说明、可编辑源文件和人工校验。 |

## 可参考的 GitHub 入门资源

以下 Star 为 **2026-08-07 的近似快照**，只表示社区可见度，不代表学习顺序或质量排名。使用前请核对最新 README、许可证、依赖和维护状态。

| 资源（Star 快照；适合阶段） | 建议吸收的内容与使用边界 |
| --- | --- |
| [OSSU Computer Science](https://github.com/ossu/computer-science)<br>Star：20.7 万+；阶段：L0–L1 | 完整 CS 能力地图、先修关系和项目式学习；按当前需要选择模块，不必学完整套课程后才开始科研。 |
| [Papers We Love](https://github.com/papers-we-love/papers-we-love)<br>Star：10.8 万+；阶段：L1–L3 | 阅读和讨论经典计算机论文，建立技术品味；将其作为选读材料，不要当成必须全部完成的书单。 |
| [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)<br>Star：8.9 万+；阶段：L0–L1 | 通过回归、分类、聚类、NLP、时间序列与强化学习练习建立基础；不要只看课程文字而不运行作业。 |
| [动手学深度学习](https://github.com/d2l-ai/d2l-zh)<br>Star：7.9 万+；阶段：L1–L2 | 学习中文、可运行的深度学习知识和代码；先掌握训练基础，再进入复杂模型。 |
| [CS 自学指南](https://github.com/PKUFlyingPig/cs-self-learning)<br>Star：7.4 万+；阶段：L0–L2 | 用于课程筛选、作业了解和 CS 学习规划；一次只推进少量课程，避免长期只收藏不产出。 |
| [Annotated Deep Learning](https://github.com/labmlai/annotated_deep_learning_paper_implementations)<br>Star：6.7 万+；阶段：L2–L3 | 建立论文解释与 PyTorch 实现的并排映射；教学实现不能直接等同于论文官方复现。 |
| [Tuning Playbook](https://github.com/google-research/tuning_playbook)<br>Star：3 万+；阶段：L2–L3 | 学习科学变量、干扰变量、实验轮次和训练诊断；先跑通 baseline，再开展系统调参。 |
| [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)<br>Star：2.5 万+；阶段：L0–L1 | 用于机器学习公式推导和中文补充说明；必须结合代码与数据理解公式。 |
| [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)<br>Star：2.3 万+；阶段：L1–L2 | 练习反向传播、梯度、训练诊断和小型模型实现；不要只观看视频，要完成代码练习。 |
| [PyTorch Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning)<br>Star：1.8 万+；阶段：L1–L2 | 学习 PyTorch 基础、训练流程和项目式练习；先掌握张量与数据管线，再套用模型。 |
| [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io)<br>Star：1.5 万+；阶段：L0–L2 | 按需补充线性代数、微积分、概率和优化；不必先学完所有数学再开始实践。 |
| [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)<br>Star：1 万左右；阶段：L2–L3 | 参考数据、代码、模型和报告的项目结构；首个小实验不必过早引入复杂工程层。 |
| [Missing Semester](https://github.com/missing-semester/missing-semester)<br>Star：6000 左右；阶段：L0–L1 | 补充 Shell、编辑器、Git、调试和数据整理能力；把工具学习放进实际项目中练习。 |
| [Lightning Hydra Template](https://github.com/ashleve/lightning-hydra-template)<br>Star：5300 左右；阶段：L2–L3 | 参考配置化实验、日志和模块化项目模板；熟悉普通 PyTorch 训练循环后再迁移。 |
| [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)<br>Star：2900 左右；阶段：L2–L3 | 检查依赖、训练、评测、权重和结果命令的完整性；不要只优化 README 外观而忽略可复现性。 |

## 推荐组合

### 组合一：完全零基础

```text
Missing Semester 的终端与 Git
  → CS 自学指南或 OSSU 中的 Python 基础
  → ML for Beginners 完成一个小项目
  → 动手学深度学习完成训练循环
  → 本仓库的首篇论文复现流程
```

### 组合二：会 Python，但不会科研

```text
研究简报
  → Google Scholar / DBLP 建立小型论文集合
  → 论文阅读卡
  → 官方预训练评测
  → shape 检查 + 单批次过拟合
  → 完整 baseline + 复现报告
```

### 组合三：已经跑通 baseline

```text
失败案例与默认假设
  → 假设卡
  → 每轮一个主要变量
  → 主实验 + 消融 + 泛化 + 效率 + 失败分析
  → 研究报告或论文初稿
```

### 组合四：算力有限

优先选择小数据、小模型、参数高效方法、训练免费方法、模型压缩、推理效率、迁移、鲁棒性或可解释性问题。无论选择什么方向，都报告 GPU、训练时间、数据规模、参数量、吞吐量、延迟、显存和资源限制对结论的影响。

## 可直接复用的模板

不要按编号顺序填写，也不要一次复制全部模板。先按[最小模板包](#只启用当前阶段的最小模板包)选择当前阶段，再在事件发生时启用按需模板。

| 模板 | 用途 |
| --- | --- |
| [零基础准备检查表](templates/00-readiness-checklist.md) | 判断当前能力和补课优先级 |
| [研究简报](templates/01-research-brief.md) | 固定问题、假设、资源和风险 |
| [论文阅读卡](templates/02-paper-reading-card.md) | 重建论文的方法与证据链 |
| [复现规划](templates/03-reproduction-plan.md) | 管理模块、shape、超参数、风险和关卡 |
| [实验卡](templates/04-experiment-card.md) | 约束单变量实验和采用决策 |
| [每周、组会与阶段复盘](templates/05-weekly-review.md) | 记录进度、证据、反馈、失败和下一步 |
| [原子科研任务卡](templates/06-daily-task-card.md) | 把阶段目标缩成一次可执行、可验收的科研会话 |
| [文献检索账本与领域地图](templates/07-literature-search-log.md) | 管理关键词、查询、去重、论文版本、领域结构和停止条件 |
| [算力、数据与环境迁移清单](templates/08-compute-data-environment-checklist.md) | 在使用实验室服务器或云 GPU 前核对资源、路径、缓存、预算、断点恢复和结果导出 |
| [投稿、评审与版本归档卡](templates/09-submission-review-archive.md) | 核验会议规则，冻结投稿版本，管理评审回复、负面结果、转投与归档 |
| [调试与求助卡](templates/10-debug-help-request.md) | 把环境、命令、报错和最小复现整理成可回答的问题 |
| [首篇真实 baseline 准入卡](templates/11-first-baseline-gate.md) | 比较两到三个候选，完成资料、数据、命令、算力与最小链路预检，并保留退出和备选路径 |
| [数学概念卡](templates/12-math-concept-card.md) | 围绕当前阻塞公式完成符号、shape、假设、数值与代码验收 |
| [数据集卡](templates/13-dataset-card.md) | 固定数据来源、使用权、版本、内容、划分、泄漏和处理证据 |
| [评价协议卡](templates/14-evaluation-spec.md) | 在运行前固定主指标、实现、聚合、阈值、统计单位与决策规则 |
| [结果—主张审计卡](templates/15-result-claim-audit.md) | 在写论文结论前核对错误、反例、图表来源与每项主张的证据强度 |

第一次不知道如何填写时，先看[第一次可审计实验演练](examples/first-workflow-drill/README.md)。示例中的数值来自仓库内脚本和配置，只用于说明记录方法，不是论文结果。

## 推荐项目结构

```text
research-project/
├── README.md                  # 目标、状态、安装与运行入口
├── .gitignore                 # 排除数据、缓存、密钥和大体积产物
├── .env.example               # 只保留变量名和示例，不包含真实凭证
├── research_brief.md          # 研究问题、假设和资源约束
├── baseline_candidates.md     # 首篇 baseline 候选、准入证据、停止规则与备选
├── evaluation_spec.md         # 主指标、实现、统计单位、不确定性与决策门槛
├── papers/
│   ├── search_log.md          # 关键词、查询、筛选与去重记录
│   ├── index.md               # 论文主记录、版本和来源路径
│   ├── domain_map.md          # 方法、数据、评价、争议与缺口
│   ├── reading_cards/         # 结构化阅读卡
│   └── math_cards/            # 被任务触发的数学概念卡
├── data/
│   ├── README.md              # 数据集卡：来源、使用权、版本、内容、划分与风险
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
│   └── README.md              # 权重、checkpoint 和大结果的外部位置与校验值
├── figures/                   # 可追溯图表与生成脚本
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
    └── requirements.lock      # 示例名：依赖锁定文件或等价环境规范
```

## 新手常见误区

| 误区 | 更可靠的做法 |
| --- | --- |
| 先收藏几十个课程 | 每次只选一个主资源，并留下可运行产物 |
| 数学没学完就不能科研 | 围绕当前任务按需补数学，再用数值和代码核对 |
| 数据能下载就能直接使用 | 先核对发布者、许可证、版本、隐私、划分和再分发边界 |
| 指标越多越能证明有效 | 先固定一个对应主张的主指标，再用辅助指标解释代价与边界 |
| 代码跑起来就是复现成功 | 区分官方评测、单批次测试、完整训练和结果容差 |
| 越新的论文越适合当 baseline | 首个 baseline 更看重代码、训练、评测、算力和可理解性 |
| 看不懂就让 AI 全部解释 | 先形成自己的问题清单，再核对原文、公式和代码 |
| 一次加入多个模块更容易涨点 | 一次一个主要变量，否则无法解释贡献 |
| 只报告最好的一次结果 | 预先确定协议，报告波动、失败和选择规则 |
| 指标提高就代表研究成立 | 先核对配对错误、反例、替代解释和主张所需的额外证据 |
| AI 写得像论文就可以投稿 | 作者必须理解、核验、修改并承担全部责任 |
| 情绪受一次失败影响 | 把反馈当信息，把复现失败和拒稿纳入正常迭代 |

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

新增资源时至少记录：原始链接、适用阶段、前置能力、建议产物、维护状态、许可证、已知限制和最后核验日期。资源应能解决明确问题，不能只因为 Star 高或传播广而加入。

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
