# 运行交接与冷启动复查审计（2026-08-09）

## 当前问题

仓库已经要求保存 `run_id—commit—config—日志—结果—决定`，但“信息存在”不等于“另一人能够接手”。原流程没有指定接收者、交接深度、资产权限、指标重算命令、产物保留状态和冷启动结果。导师可能看懂周报，却仍需作者口头解释本地路径；tracker 页面也可能因账号、artifact store 或过期产物无法复查。

## 经验帖对照

| 经验材料 | 暴露的问题与本仓库吸收的内容 |
| --- | --- |
| [研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e) | 日常记录容易碎片化，结果未及时聚合，汇报时才集中整理。本仓库吸收“项目级入口与及时决定”，不把作者使用的软件和周频率规定为通用标准。页面可能需要登录。 |
| [科研习惯分享（三）：一次实验我写 3 份记录](https://www.xiaohongshu.com/explore/6612bab8000000001b013f7e) | 正文反映随手纸记录会导致事后细节不清，讨论也显示个人记录与组会表达面向不同对象。本仓库用唯一来源加不同用途的链接解决，不要求所有人维护三份重复记录。页面可能需要登录。 |
| [接手师兄烂摊子，实验记录像天书](https://www.xiaohongshu.com/explore/6a5831f5000000000103163d) | 建议交接提前开始、跟随完整流程、记录隐性参数和资产位置，并使用清单。该内容来自湿实验场景；本仓库只迁移“提前走一次全流程、显式记录隐性依赖与资产”的原则，用空目录复跑和权限清单替代仪器盘点或签字要求。页面可能需要登录。 |
| [研一暑假做实验才发现，数据管理比调参更重要](https://www.xiaohongshu.com/explore/6a5f37be00000000110120f5) | 数据 revision、处理、split、标签、训练设置和指标所用样本若未绑定，重跑后比较可能失效。本仓库把这些身份集中到交接映射中，不采用任何单一文件命名习惯作为强制标准。页面可能需要登录。 |
| [如何科学地进行实验设计和记录](https://zhuanlan.zhihu.com/p/69353695) | 个人经验回顾了漏记细节、过后无法理解自己实验的问题，并强调每次实验应产生信息和下一步计划。本仓库吸收足够上下文与决策闭环，不把具体笔记软件设为要求。 |

## 规范与项目对照

| 规范或项目 | 对本仓库的约束 |
| --- | --- |
| [The Turing Way：可复现与协作项目](https://book.the-turing-way.org/project-design/pd-overview/pd-overview-repro/) | 可复现与协作相互关联；README 应让新参与者理解当前状态、开发和未来计划。 |
| [Good Enough Practices：协作](https://carpentries-lab.github.io/good-enough-practices/04-collaboration.html) | 即使个人项目也应为未来的合作者和未来的自己提供入口、依赖、示例和目录说明。 |
| [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/)与 [W&B Runs](https://docs.wandb.ai/models/runs) | run 应绑定稳定 ID、配置、代码、状态、指标和产物；团队复查仍取决于后端、账号和资产访问。 |
| [DVC Collaborative Experiments](https://dvc.org/blog/collaborative-experiments/) | 跨机器恢复实验需要共享代码、数据、配置与产物的远端和权限，不能只共享实验名称。 |
| [Reproducibility checklist](https://ropensci-archive.github.io/reproducibility-guide/sections/checklist/) | 起始入口、输入来源、软件版本、随机性、最新代码 / 数据和特定重复运行都应可定位。 |
| [Sustainable Research Software Hand-Over](https://arxiv.org/abs/1909.09469) | 研究人员变动会使软件和隐性知识流失；交接清单应按项目规模采用。 |

## 适用边界

本轮规则主要面向有代码、数据、配置和运行产物的 AI / 计算机研究。理论研究、纯定性工作或受机构控制的平台不必生成同样文件，但仍需定义入口、权限和验收。交接深度按用途选择，不强制每次完整训练；跨硬件不保证逐位一致，容差应由任务和环境预先定义。受限数据和匿名材料不得为“方便交接”而上传，合法的 `REVIEW_ONLY` 必须明确不能验证的步骤。

## 采取行动

1. 新增[运行交接与冷启动复查](../docs/RUN_HANDOFF_REPLAY.md)，定义 H0–H3 深度、唯一入口字段、空目录复查和五种状态；
2. 新增[运行交接卡](../templates/16-run-handoff.md)，把代码、环境、数据、配置、运行、产物、指标、权限和决定集中映射到主要来源；
3. 为[第一次工作流演练](../examples/first-workflow-drill/run-handoff.md)填写 H2 示例，并将已有产物核验与重新运行分开；
4. 更新首页、核心工作流、真实项目接入、周会模板和索引，让交接只在关键运行、迁移或负责人变化时触发。

## 冷启动验证

- 源代码身份：commit `ad6538378ff9c15a744d13ecfd9c17e1afc9de15`；
- 测试方式：从该 commit 导出 `examples/first-workflow-drill` 到 Windows 临时空目录，不使用工作区结果；
- 执行内容：分别运行 debug、baseline 和 candidate 配置到三个新目录，再运行 `verify.py`；
- 结果：临时副本路径检查通过；三组计划运行均完成；验收输出 `PASS`；重算 baseline accuracy 均值 `0.840000`、candidate `0.966667`；三组运行加验收约 1.129 秒；临时目录已在路径校验后清理；
- 判定：`HANDOFF_READY`。该状态只覆盖本教学演练的 H2 最小复跑，不证明真实论文、外部数据或完整训练已经可交接。

## 状态

指南、模板和已填写交接卡已建立，教学演练 H2 冷启动已通过；仓库级文档与索引状态由本轮质量检查和 GitHub Actions 继续验证。
