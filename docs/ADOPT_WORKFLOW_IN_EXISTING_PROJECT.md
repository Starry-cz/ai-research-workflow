# 把科研工作流接入真实代码库

这份指南用于你已经拿到导师项目、实验室仓库或论文官方代码，准备把本仓库的方法接进去时。目标不是重排别人的目录，也不是复制全部模板，而是在不破坏原项目的前提下建立最短证据链。

开始前先完成[第一项导师任务授权边界](FIRST_MENTOR_TASK_BOUNDARY.md)。仓库、服务器或文件对你可见，不代表本次任务允许修改、上传、删除、公开或调用外部服务。

```text
识别仓库身份与权限
  → 盘点现有记录
  → 为关键字段指定唯一来源
  → 只补当前阶段缺口
  → 跑一次最小命令
  → 连接 commit、config、run_id、日志和决定
```

## 第一原则：先映射，不先搬家

真实项目通常已经有 README、配置、日志目录、实验平台或课题组表格。先回答“需要的信息现在在哪里”，再决定是否新增文件。

| 需要回答的问题 | 可以复用的现有位置 |
| --- | --- |
| 项目做什么、当前做到哪里 | 根 README、Wiki、项目看板或课题组文档 |
| 如何安装和运行 | README、环境文件、脚本帮助信息或容器配置 |
| 数据来自哪里、如何划分 | dataset card、data README、manifest 或数据平台记录 |
| 哪次运行产生哪个结果 | 现有 tracker、CSV、数据库、日志目录或实验表 |
| 为什么保留或放弃某个方案 | Issue、实验记录、决策日志或组会记录 |

同一事实只指定一个主要来源，其他位置只链接过去。例如环境版本以锁定文件为准，研究 README 只写路径和最后核验时间；不要在三张表里手工复制同一组依赖。

## 1. 判断你属于哪种接入场景

### 场景 A：实验室已有成熟仓库

遵循现有目录、分支、日志和协作规则。把本仓库模板当作字段检查表：现有记录已经覆盖的字段标记为“见路径 / 链接”，只补缺失项。不要为了使用本工作流再建立第二套实验表。

### 场景 B：复现公开论文仓库

优先 fork，并保留原作者仓库为 `upstream`。本地改动放在独立分支；先保存未修改代码的预训练评测或最小运行结果，再开始复现修订和研究改动。

```bash
git remote -v
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPO.git
git fetch upstream
git switch -c research/reproduce-baseline
```

如果 `upstream` 已存在，不要重复添加。实际分支名应符合课题组规范。同步上游前先检查当前分支和未提交修改，不使用强制覆盖命令处理不理解的冲突。

### 场景 C：不能修改上游或只能读取服务器目录

建立一个私有的伴随记录位置，保存上游 URL、commit、许可证、环境、补丁 / diff、运行命令和结果索引；不要复制整个上游源码后丢失来源关系。涉及未公开代码、匿名审稿材料或受限数据时，先确认允许保存和同步到哪里。

### 场景 D：只有一个 Notebook

可以先保留 Notebook。至少固定数据版本、环境、seed、输入输出路径和执行顺序，并清空后从头运行一次。只有当同一逻辑需要重复运行、比较多组配置、自动评测或多人协作时，才把数据处理、训练和评价逐步拆成脚本。

### 场景 E：全新项目

从[渐进式项目结构](PROJECT_STRUCTURE.md)的 L0–L1 骨架开始，不需要先创建论文、投稿、模型仓库和复杂流水线。

## 2. 十五分钟只读盘点

在改文件前完成以下检查：

1. **身份**：论文版本、官方 / 第三方仓库、当前 commit、许可证和上游地址；
2. **授权**：谁负责本次任务，哪些分支与目录允许写，数据、权重、日志和配置能否提交、上传或交给外部服务，哪些决定要再次确认；
3. **入口**：安装、预训练评测、训练和评价命令分别在哪里；
4. **状态**：当前分支、未提交修改、已有实验和最后可信结果；
5. **产物**：配置、日志、指标、checkpoint 与逐样本预测实际写到哪里；
6. **风险**：密钥、个人路径、私有数据、大文件、自动下载和覆盖输出；
7. **现有台账**：README、Issue、tracker、表格和组会记录各自负责什么。

盘点阶段只读。不要让 AI 先“整理目录”、升级依赖或批量格式化代码；这些动作会扩大 diff，也可能破坏上游复现条件。

## 3. 建立单一来源映射

在现有 README 或一个很短的 `research/README.md` 中记录映射，不复制正文：

```text
当前问题：
当前阶段与唯一任务：
任务负责人 / 决定负责人：
允许读取 / 写入 / 运行 / 分享 / 付费的范围：
待确认、禁止和升级项：
上游论文 / 仓库 / commit：
本地分支 / commit：
环境来源：
数据身份与 split 来源：
配置来源：
实验索引或 tracker：
最新可信 run_id：
结果与图表来源：
风险 / 阻塞：
下一步及通过条件：
```

如果根 README 已经清楚说明这些内容，只增加“当前研究状态”小节或链接。`research/README.md` 只是上游 README 不宜改动时的可选位置，不是强制目录。

## 4. 只启用当前阶段的一组最小记录

| 当前状态 | 只补这一类记录 |
| --- | --- |
| 还没确定是否值得投入 | [baseline 准入卡](../templates/11-first-baseline-gate.md) |
| 已选定论文、准备跑代码 | [复现规划](../templates/03-reproduction-plan.md) |
| 正在运行正式比较 | [实验卡](../templates/04-experiment-card.md)与已冻结的[评价协议](../templates/14-evaluation-spec.md) |
| 已完成结果、准备写结论 | [结果—主张审计](../templates/15-result-claim-audit.md) |

使用模板时有三种合法方式：

1. 现有记录已覆盖：写路径或链接，不再复制；
2. 只缺少少量字段：把字段加入现有台账；
3. 现有系统无法承载：才复制一张完整模板，并注明它替代哪个旧记录。

不要按编号从 `00` 填到 `15`。同一时间通常只维护一个阶段门控、一个当前运行记录，以及确有事件才启用的一张按需卡。

## 5. 跑通第一条证据链

第一次接入不追求完整训练，只验证记录能否连接：

```text
question
  → upstream_commit + local_commit
  → environment + data_revision
  → config + exact_command
  → run_id + log + metrics
  → decision + next_step
```

最低动作：

1. 从原项目 README 选择最小官方命令；
2. 在未改方法前运行，保留完整命令、时间、退出码和日志；
3. 给运行分配唯一 `run_id`，保存实际配置而非只写配置名称；
4. 确认输出没有覆盖旧结果，数据、权重、密钥和缓存没有误入 Git；
5. 用一次小而有意义的 commit 保存新增记录或最小修正；
6. 请另一人或隔天的自己只根据入口页找到该运行和结果；如果该运行将用于正式协作或迁移，继续按[运行交接与冷启动复查](RUN_HANDOFF_REPLAY.md)声明深度并执行空目录复查。

如果还不能运行，记录第一个关键错误和已排除原因，当前状态是 `BLOCKED_RUNTIME`，不是“接入完成”。需要向第三方项目反馈时，先按[第一次向开源上游求助与贡献](UPSTREAM_HELP_AND_CONTRIBUTION.md)确认支持范围、问题所有者和公开最小复现；论文结果不同不自动等于上游软件 bug。

接入完成后不要立刻让 AI 批量改代码。需要修复或尝试方法时，转入[第一次安全修改论文代码](SAFE_FIRST_CODE_CHANGE.md)，以当前证据链作为修改前 baseline，并把修复、重构和研究改动分开。

## 6. 什么时候才升级结构或工具

- 第二个以上配置出现：增加配置文件和实验索引；
- 多次运行难以手工比较：再引入 MLflow、DVC、Weights & Biases 或等价 tracker；
- 数据出现多个版本：增加 manifest、校验值和数据卡；
- Notebook 需要重复执行或进入批量实验：逐步拆出脚本和测试；
- 多人协作：增加贡献规则、Issue / PR 流程和决策日志；
- 关键运行需要他人复查、换机器或换负责人：增加唯一交接入口和冷启动记录；
- 进入写作：增加分析目录、图表生成链和主张审计；
- 进入投稿：冻结实际提交版本和外部依赖。

工具升级必须解决已经出现的查找、复现或协作问题。不要因为高 Star 项目使用某个平台，就在第一次复现前部署完整 MLOps 系统。

## 7. 接入结果只作一个决定

| 状态 | 含义与下一步 |
| --- | --- |
| `ADOPTED_MINIMAL` | 唯一来源和第一条证据链已建立，可以进入当前研究阶段。 |
| `USE_EXISTING_SYSTEM` | 实验室系统已覆盖需要，只补链接与缺失字段。 |
| `NEEDS_PERMISSION` | 代码、数据或记录位置权限不清；先向负责人确认。 |
| `POLICY_ESCALATION` | 伦理、隐私、安全、许可或机构规则存在风险；暂停相关动作并使用正式渠道。 |
| `BLOCKED_RUNTIME` | 最小官方命令尚未跑通；继续复现排障，不改方法。 |
| `RESTRUCTURE_LATER` | 当前能复查，但规模增长已触发结构升级；单独规划迁移。 |

## 验收清单

- [ ] 没有移动或重命名不理解的上游文件；
- [ ] 官方仓库、fork、上游 remote、本地分支和 commit 关系明确；
- [ ] 每类关键信息只有一个主要来源；
- [ ] 没有维护两套同义实验台账；
- [ ] 当前只启用必要模板，未知字段没有提前猜写；
- [ ] 第一条命令、配置、run_id、日志、指标和决定可以相互定位；
- [ ] 数据、权重、密钥、隐私材料和大文件没有误提交；
- [ ] 技术权限与本次任务授权已经分开记录，待确认项没有被默认为允许；
- [ ] 接入状态和下一步通过条件已经写明。

## AI 辅助边界

AI 可以只读扫描目录、解释入口、生成字段映射和检查遗漏。任何批量移动、依赖升级、格式化、删除、分支合并或自动提交前，必须先查看计划和 diff。AI 不能仅凭文件名判断数据可公开、结果可信或许可证允许再分发，也不能替你决定实验室的唯一台账。

## 依据与延伸阅读

- [Good Enough Practices in Scientific Computing](https://doi.org/10.1371/journal.pcbi.1005510)：面向科研计算新手的最低可采用实践，覆盖项目组织、数据、代码、协作和记录；
- [The Turing Way](https://github.com/the-turing-way/the-turing-way)与其[可复现项目模板](https://github.com/the-turing-way/reproducible-project-template)：README 作为入口，模板内容应按项目需要删除、修改或增加；
- [GitHub：Fork a repository](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)与[配置 upstream](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork)：公开上游与个人改动的关系；
- [Made With ML：Moving from Notebooks to Scripts](https://madewithml.com/courses/mlops/scripting/)：重复运行和工程需求出现后，再从 Notebook 逐步迁移到脚本；
- [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)：成熟项目结构参考，不是首次复现的强制目录。
