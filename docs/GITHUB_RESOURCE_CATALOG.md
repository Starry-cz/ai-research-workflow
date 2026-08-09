# 可参考的 GitHub 科研入门资源

这份目录用于扩展学习，不是必须全部完成的书单。先从根目录 README 的 L0–L3 入口判断当前阶段，每次只选择一个主资源，并留下可运行作业、阅读卡、复现记录或实验报告。

Star、Fork 和榜单位置会变化，只能表示社区可见度，不能证明内容正确、适合当前任务或仍被维护。本目录不按 Star 排名；使用前请重新核对项目 README、许可证、依赖、最近更新和 Issue。

## L0–L1：工具与计算机基础

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Missing Semester](https://github.com/missing-semester/missing-semester)<br>L0–L1 | 补 Shell、Git、调试和数据整理能力。把工具学习嵌入实际项目，不要求先完成全部课程。 |
| [CS 自学指南](https://github.com/PKUFlyingPig/cs-self-learning)<br>L0–L2 | 用于筛选课程、了解作业和安排先修关系。一次只推进与当前阻塞相关的一门课。 |
| [OSSU Computer Science](https://github.com/ossu/computer-science)<br>L0–L1 | 参考完整 CS 能力地图、先修关系和项目式学习。它是长期课程体系，不是开始科研前的必修清单。 |

## L0–L2：机器学习与深度学习

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)<br>L0–L1 | 用回归、分类、聚类、NLP 和时间序列练习建立基础。至少运行并修改一个作业，不只阅读课程文字。 |
| [动手学深度学习](https://github.com/d2l-ai/d2l-zh)<br>L1–L2 | 学习中文、可运行的深度学习知识和代码。先掌握数据、训练循环和评价，再进入复杂模型。 |
| [PyTorch Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning)<br>L1–L2 | 学习张量、数据管线、训练流程和项目式实践。不能用套用高层 API 替代对 shape 与梯度的解释。 |
| [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)<br>L1–L2 | 练习反向传播、梯度、训练诊断和小型模型实现。应完成代码练习，而不是只观看视频。 |
| [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)<br>L0–L1 | 为机器学习公式提供推导和中文说明。围绕当前任务查阅，并用数值和代码核对。 |
| [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io)<br>L0–L2 | 按需补线性代数、微积分、概率和优化。数学学习的验收是能返回当前模型或公式，不是读完全书。 |

## L1–L3：论文阅读与科研能力

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Learning Research](https://github.com/pengsida/learning_research)<br>L1–L3 | 吸收“广度打底—深度项目—独立研究”、实验记录和交流展示思路。部分路线面向 3D Vision 和具体实验室环境，需要按方向与指导条件调整。 |
| [Papers We Love](https://github.com/papers-we-love/papers-we-love)<br>L1–L3 | 阅读和讨论经典计算机论文，建立技术品味。它是选读集合，不是必须全部完成的论文清单。 |
| [How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)<br>L1–L3 | 学习分层检索和阅读，只对核心论文做高投入精读。重要表述仍需回到论文原文。 |
| [Annotated Deep Learning](https://github.com/labmlai/annotated_deep_learning_paper_implementations)<br>L2–L3 | 建立论文解释、公式和 PyTorch 实现的并排映射。教学实现不能直接视为论文官方复现。 |

## L2–L3：复现、实验与研究工程

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Tuning Playbook](https://github.com/google-research/tuning_playbook)<br>L2–L3 | 学习科学变量、干扰变量、实验轮次、预算和训练诊断。baseline 未跑通前不要直接进入大规模调参。 |
| [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)<br>L2–L3 | 检查依赖、训练、评测、权重和结果命令是否完整。README 外观不能代替真正的可复现性。 |
| [Made With ML](https://github.com/GokuMohandas/Made-With-ML)<br>L1–L3 | 学习从可运行 Notebook 到脚本、测试、追踪和部署的渐进组织。生产化内容不是首个科研闭环的强制要求。 |
| [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)<br>L2–L3 | 参考数据、代码、模型和报告分离的项目结构。首个小实验应保留最小目录，不要过早复制完整工程层。 |
| [Lightning Hydra Template](https://github.com/ashleve/lightning-hydra-template)<br>L2–L3 | 参考配置化实验、日志和模块化项目。先能解释普通 PyTorch 训练循环，再迁移复杂框架。 |

## 科研流程与 AI 辅助

| 资源与适用阶段 | 建议吸收的内容与使用边界 |
| --- | --- |
| [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)<br>L1–L3 | 参考调研、写作、审稿和投稿清单。启用与当前阶段相关的技能，不一次加载全部流程。 |
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)<br>L1–L3 | 参考研究问题澄清、计划和反馈结构。导师式输出不能替代真实导师、领域专家和作者判断。 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)<br>L2–L3 | 借鉴阶段产物、检查点、预算、恢复、证据核验和版本归档。自动生成的文献、代码、实验和论文不能视为已经验证的研究。 |
| [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure)<br>L2–L3 | 参考论文示意图结构和视觉表达。生成图必须核对变量、关系、数据来源并保留可编辑源文件。 |

## 如何吸收一个外部项目

不要复制整个仓库的目录或 README。先填写下面六项：

```text
当前阻塞：它解决我的哪个具体问题？
适用阶段：L0 / L1 / L2 / L3？
最小入口：先运行哪一课、哪条命令或哪份模板？
验收产物：代码、阅读卡、配置、日志还是报告？
重要边界：领域、维护、许可证、费用或自动化风险是什么？
停止条件：什么情况下不再继续投入？
```

如果不能回答“下一项可验收产物是什么”，先不要把它加入主学习路线。

## 发现更多资源

[Awesome Machine Learning Resources](https://github.com/ZhiningLiu1998/awesome-machine-learning-resources)可用于发现方向型资源，并为长期不活跃的条目标记状态。此类聚合目录只负责发现候选；是否采用仍要回到原项目核对维护状态、许可证、前置能力和最小产物。
