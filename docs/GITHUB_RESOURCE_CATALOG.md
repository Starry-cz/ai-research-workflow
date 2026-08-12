# 可参考的 GitHub 科研入门资源

这份目录用于扩展学习，不是必须全部完成的书单。先从根目录 README 的 L0–L3 入口判断当前阶段，每次只选择一个主资源，并留下可运行作业、阅读卡、复现记录或实验报告。

Star、Fork 和榜单位置会变化，只能表示社区可见度，不能证明内容正确、适合当前任务或仍被维护。本目录不按 Star 排名。每项先给出“进入成本”，帮助你在点开前判断主要语言、最低前置、账号或算力要求；费用、服务条款和依赖仍会变化，使用当天必须回到项目 README 与官方页面复核。

## L0–L1：工具与计算机基础

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Introduction to GitHub](https://github.com/skills/introduction-to-github)<br>L0 | **进入成本**：英文交互练习；需 GitHub 账号和浏览器，不要求先安装 Git，模板仓库会使用 GitHub Actions。<br>**吸收与边界**：完成 branch、commit、Pull Request 和 merge 的真实闭环；本地 Git、终端和团队权限仍需单独练习。 |
| [Missing Semester](https://github.com/missing-semester/missing-semester)<br>L0–L1 | **进入成本**：中英文材料；练习需 Shell，Git 章节需本地 Git，不要求 GPU。<br>**吸收与边界**：补 Shell、Git、调试和数据整理能力；把练习嵌入实际项目，不要求先完成全部课程。 |
| [uv](https://github.com/astral-sh/uv)<br>L0–L2 | **进入成本**：英文文档；需安装跨平台可执行文件，安装器可能修改 PATH。<br>**吸收与边界**：统一 Python、环境、依赖和锁定；已有稳定项目不要只为换工具迁移，锁文件也不能固定数据、GPU 或外部 API。 |
| [JupyterLab](https://github.com/jupyterlab/jupyterlab)<br>L0–L2 | **进入成本**：英文文档；需 Python 环境和 JupyterLab，本地探索不要求 GPU。<br>**吸收与边界**：用于交互探索、教学与解释；交付前必须重启内核并从头运行，稳定逻辑逐步下沉到脚本或模块。 |
| [CS 自学指南](https://github.com/PKUFlyingPig/cs-self-learning)<br>L0–L2 | **进入成本**：中文导航可直接读；外部课程的语言、账号、环境和作业要求各异。<br>**吸收与边界**：用于筛选课程和先修关系；一次只推进与当前阻塞相关的一门课。 |
| [OSSU Computer Science](https://github.com/ossu/computer-science)<br>L0–L1 | **进入成本**：英文长期课程地图；具体课程要求分别核对。<br>**吸收与边界**：参考完整 CS 能力地图、先修关系和项目式学习；不是开始科研前的必修清单。 |

## L0–L2：机器学习与深度学习

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [scikit-learn MOOC](https://github.com/INRIA/scikit-learn-mooc)<br>L0–L1 | **进入成本**：英文课程与 Notebook；静态内容可在线阅读，练习需基础 Python 或在线 Notebook 环境。<br>**吸收与边界**：从表格数据、预处理 Pipeline、交叉验证和评价建立第一个经典 ML baseline；课程作业不等于论文复现。 |
| [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)<br>L0–L1 | **进入成本**：含简体中文等多语言材料；练习需 Python 与 Notebook。<br>**吸收与边界**：用经典任务建立基础；至少运行并修改一个作业，不只读课程文字。 |
| [动手学深度学习](https://github.com/d2l-ai/d2l-zh)<br>L1–L2 | **进入成本**：中文教材；练习需 Python 与所选框架，基础章节可先用 CPU。<br>**吸收与边界**：先掌握数据、训练循环和评价，再进入复杂模型。 |
| [PyTorch Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning)<br>L1–L2 | **进入成本**：英文课程；需基本 Python，可使用本地环境或 Colab。<br>**吸收与边界**：学习张量、数据管线和训练流程；不能用高层 API 代替 shape 与梯度解释。 |
| [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)<br>L1–L2 | **进入成本**：英文视频与 Notebook；需基本 Python、少量微积分，部分练习可用 Colab。<br>**吸收与边界**：练习反向传播、训练诊断和小模型实现；不能只观看视频。 |
| [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)<br>L0–L1 | **进入成本**：中文推导；需结合《机器学习》对应章节，代码核对只需基础 Python。<br>**吸收与边界**：围绕当前任务查公式，并用数值和代码核对。 |
| [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io)<br>L0–L2 | **进入成本**：英文教材；做练习需基础代数与微积分。<br>**吸收与边界**：按需补数学，验收是能返回当前模型或公式，不是读完全书。 |

## L1–L3：论文阅读与科研能力

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [The Turing Way](https://github.com/the-turing-way/the-turing-way)<br>L0–L3 | **进入成本**：开放在线手册并提供多语言入口；按章阅读通常无需安装，实践章节分别涉及 Git、环境、数据或协作工具。<br>**吸收与边界**：按当前缺口学习可复现研究、项目设计、沟通、协作和伦理；开放共享仍需服从权限、同意和机构政策。 |
| [Learning Research](https://github.com/pengsida/learning_research)<br>L1–L3 | **进入成本**：中文经验可直接读；执行课程或代码需按方向另备环境、数据和算力。<br>**吸收与边界**：吸收“广度—深度—独立研究”、记录和展示思路；3D Vision 与实验室路线需自行适配。 |
| [Papers We Love](https://github.com/papers-we-love/papers-we-love)<br>L1–L3 | **进入成本**：英文目录；论文语言、开放获取和知识前置随条目变化。<br>**吸收与边界**：选读并讨论与当前问题相关的论文，不把集合当成必读书单。 |
| [How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)<br>L1–L3 | **进入成本**：中文指南；真实检索可能受机构订阅、登录和数据库变化影响。<br>**吸收与边界**：学习分层检索与阅读，只精读核心论文；重要表述回到原文。 |
| [Annotated Deep Learning](https://github.com/labmlai/annotated_deep_learning_paper_implementations)<br>L2–L3 | **进入成本**：英文解释与 PyTorch 代码；需能读公式、张量和训练代码。<br>**吸收与边界**：建立论文—公式—实现映射；教学实现不等于论文官方复现。 |

## L2–L3：复现、实验与研究工程

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Tuning Playbook](https://github.com/google-research/tuning_playbook)<br>L2–L3 | **进入成本**：英文方法手册；需已有稳定 baseline、训练管线、指标和预算。<br>**吸收与边界**：学习变量、实验轮次和诊断；baseline 未跑通前不做大规模调参。 |
| [MLflow](https://github.com/mlflow/mlflow)<br>L2–L3 | **进入成本**：英文文档；本地记录需 Python，多人服务另需存储、权限与运维。<br>**吸收与边界**：在 run 数量难以手工比较后记录参数、指标、代码版本和 artifact；追踪平台不自动保证公平实验、科学解释或备份。 |
| [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)<br>L2–L3 | **进入成本**：英文指南；需已有代码和结果，能够核对依赖、许可证、权重与命令。<br>**吸收与边界**：检查发布完整性；README 外观不能代替真实复现。 |
| [Made With ML](https://github.com/GokuMohandas/Made-With-ML)<br>L1–L3 | **进入成本**：英文课程；需基本 Python 与 ML 概念，官方提供个人电脑路径。<br>**吸收与边界**：从可运行工作负载渐进到脚本、测试和追踪；集群与生产化不是首次闭环前置。 |
| [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)<br>L2–L3 | **进入成本**：英文文档；生成项目需本地 Python 与命令行。<br>**吸收与边界**：参考数据、代码、模型与报告分离；没有重复运行或协作需求时保持最小目录。 |
| [Lightning Hydra Template](https://github.com/ashleve/lightning-hydra-template)<br>L2–L3 | **进入成本**：英文文档；需熟悉 Python、PyTorch、配置和命令行。<br>**吸收与边界**：参考配置化实验和日志；先能解释普通训练循环，再迁移复杂框架。 |

## 科研流程与 AI 辅助

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)<br>L1–L3 | **进入成本**：中英文说明；实际调用需受支持的 AI 编程客户端与模型访问，部分导出另需本地工具。<br>**吸收与边界**：按当前阶段参考一项调研、写作或审查技能；不一次加载全部流程。 |
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)<br>L1–L3 | **进入成本**：中文 handbook 可直接读；调用 skills 需受支持的 AI 客户端和自己的研究材料。<br>**吸收与边界**：参考问题澄清、计划和反馈结构；不能替代真实导师与领域判断。 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)<br>L2–L3 | **进入成本**：多语言说明；完整运行需 Python、OpenClaw、模型访问与任务执行环境。<br>**吸收与边界**：借鉴阶段产物、检查点和归档；自动生成的研究内容不能视为已经验证。 |
| [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure)<br>L2–L3 | **进入成本**：中英文模板；skill 需 Claude Code 或 Codex，出图还需图像模型或绘图工具。<br>**吸收与边界**：参考示意图结构；必须核对变量、关系和来源并保留可编辑源文件。 |

## L2–L3：LLM、Agent 与 RAG 评测

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)<br>L2–L3 | **进入成本**：英文文档；需 Python、模型/API 凭据和任务所需环境，部分评测涉及费用与安全边界。<br>**吸收与边界**：用 dataset、solver、scorer 和日志组织 LLM/Agent 评测；预置 eval 和框架本身不能证明模型安全。 |
| [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)<br>L2–L3 | **进入成本**：英文文档；不同后端需额外安装 Torch、GPU 推理栈或 API 依赖。<br>**吸收与边界**：共享标准或自定义 YAML 任务，并固定 commit、模型参数和解析；公共 benchmark 不代表真实任务，不同后端结果需核验。 |
| [RAGChecker](https://github.com/amazon-science/RAGChecker)<br>L2–L3 | **进入成本**：中英文教程；需 Python、RAG 结果和支持的模型/凭据，先建立可解释检索 baseline。<br>**吸收与边界**：分别诊断检索器和生成器；自动 claim-level 指标必须用人工小集校准，不能只报综合分数。 |

## 如何吸收一个外部项目

不要复制整个仓库的目录或 README。先填写下面六项：

```text
当前阻塞：它解决我的哪个具体问题？
适用阶段：L0 / L1 / L2 / L3？
最小入口：先运行哪一课、哪条命令或哪份模板？
进入成本：主要语言、前置能力、账号、依赖、算力和可能费用是什么？
验收产物：代码、阅读卡、配置、日志还是报告？
重要边界：领域、维护、许可证、费用或自动化风险是什么？
停止条件：什么情况下不再继续投入？
```

如果不能回答“下一项可验收产物是什么”，先不要把它加入主学习路线。

## 发现更多资源

[Awesome Machine Learning Resources](https://github.com/ZhiningLiu1998/awesome-machine-learning-resources)可用于发现方向型资源，并为长期不活跃的条目标记状态。此类聚合目录只负责发现候选；是否采用仍要回到原项目核对维护状态、许可证、前置能力和最小产物。
