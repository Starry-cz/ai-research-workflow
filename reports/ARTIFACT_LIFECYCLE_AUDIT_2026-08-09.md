# 实验产物生命周期审计（2026-08-09）

## 当前问题

仓库要求保存失败运行、checkpoint、日志和结果位置，但没有回答“保存多久、谁复查、什么可以清理、清理后保留什么”。失败实验可能因结果不好被删除；相反，大量可重建缓存和中间 checkpoint 也可能无限堆积。交接卡即使记录了 artifact URI，平台 TTL、账号回收或垃圾回收仍可能让入口失效。

## 经验帖对照

| 经验材料 | 暴露的问题与本仓库吸收的内容 |
| --- | --- |
| [研一暑假做实验才发现，数据管理比调参更重要](https://www.xiaohongshu.com/explore/6a5f37be00000000110120f5) | 数据版本、split、标签处理、训练设置和指标范围缺失会迫使已有实验重新核验；笔记还强调实验记录比单一权重更重要。本仓库吸收“先保留身份与解释链”，不把个人命名方式设为标准。页面可能需要登录。 |
| [接手师兄烂摊子，实验记录像天书](https://www.xiaohongshu.com/explore/6a5831f5000000000103163d) | 资产位置和隐性参数未在日常过程记录，离开前突击交接仍会丢信息。内容来自湿实验；本仓库迁移为从项目开始维护产物负责人、到期与交接入口，不采用仪器盘点和签字作为 AI 项目通用要求。页面可能需要登录。 |
| [毕业季，实验室最头疼的问题来了](https://zhuanlan.zhihu.com/p/2056073543717336306) | 文章指出原始文件、统计过程、失败 / 异常和重复实验散落于个人设备，毕业后难以复核。该内容来自商业 ELN 服务商与湿实验场景；本仓库只把它作为保留失败证据和日常归档的痛点材料，不采用其产品结论或“所有原始文件永久保存”的隐含做法。 |
| [实验记录需要注意的关键点](https://zhuanlan.zhihu.com/p/534204566) | 文章强调无效数据也应保留并说明原因，避免重复无意义实验。其规则面向更强审计的实验室记录；本仓库转换为“所有运行保留可解释元数据，是否保留大二进制按证据与政策决定”。 |

## 规范与项目对照

| 规范或项目 | 对本仓库的约束 |
| --- | --- |
| [The Turing Way：Data Management Plan](https://book.the-turing-way.org/reproducible-research/rdm/rdm-dmp/) | 项目应持续记录输出生成、大小、存储、备份、访问、项目后保存、仓库政策和成本；具体年限服从国家、机构和资助方政策。 |
| [The Turing Way：Data Storage and Organisation](https://book.the-turing-way.org/reproducible-research/rdm/rdm-storage.html) | 重要数据需要多副本、不同介质 / 位置与自动备份；大规模数据可按标准选择备份，而不是默认全量永久复制。 |
| [GitHub Actions artifact 与日志保留期](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization) | CI 产物默认会在保留期后删除，组织策略还可改变范围；CI URL 不能作为长期证据仓库。 |
| [W&B artifact TTL](https://docs.wandb.ai/models/artifacts/ttl) | artifact version 可配置 TTL，且编辑能力受团队权限控制；项目必须知道谁能改变策略。 |
| [MLflow CLI `gc`](https://mlflow.org/docs/latest/api_reference/cli.html) | `gc` 会永久删除 deleted run 的元数据和 artifact，且不会因 UI pin、注册模型或标签自动保护，清理前必须独立检查引用。 |
| [DVC garbage collection](https://dvc.org/doc/command-reference/gc) | GC 的保留范围取决于 workspace、分支、标签或提交选择；未推送或未正确引用的对象可能永久丢失。 |

## 适用边界

本轮规则面向会产生代码、日志、模型、预测和数据产物的 AI / 计算机研究。它不是法律保存期限；机构、伦理、资助方、合同、数据提供方和 venue 规则具有更高优先级。备份不等于长期保存，平台 pin 不等于删除保护，可重建也不等于低成本。跨平台恢复只需达到项目预设容差，不要求二进制逐位相同。敏感数据可能依法需要删除，不能借“可复现”无限期保留。

## 采取行动

1. 新增[实验产物保留、归档与安全清理](../docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)，按临时、恢复、证据、归档和受限五类管理，而不按结果好坏删除；
2. 定义从主张反查资产、最小生命周期台账、清理前八项检查、墓碑记录和五种生命周期决定；
3. 将分类、负责人、大小、到期、平台 TTL 和清理状态加入实验卡、交接卡、投稿归档卡与项目结构；
4. 新增[教学演练生命周期台账](../examples/first-workflow-drill/artifact-lifecycle.md)，明确三组记录结果为何保留、个人输出为何不能由仓库自动清理；
5. 在持续改进记录中新增 I-040，并把下一轮审计转向“导师反馈是否真正转成修改与再验收”。

## 本地验证

- Git 跟踪检查：三组 `*-recorded` 共 12 个配置、环境、指标和日志文件全部由 Git 跟踪；
- 隔离检查：`results/my-lifecycle-check/metrics.json` 命中演练目录 `.gitignore` 的 `results/*` 规则，个人输出不会被误加入仓库；
- 仓库质量检查：已检查 56 个 Markdown 文件；相对链接与锚点、代码块、README 约束、指南 / 模板索引和 51 个工具条目全部通过；
- 说明：本轮只执行只读盘点，没有运行任何远端 GC、批量删除或保留策略变更。

## 状态

文档、已填写生命周期台账和本地检查均已完成；线上状态以对应提交的 GitHub Actions 为准。
