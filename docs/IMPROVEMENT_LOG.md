# 持续改进记录

本文件记录仓库发现的问题、对照材料、适用边界和实际修改。主 README 保持专业、简洁；平台经验贴主要用于发现新手的真实困难，不能单独作为技术结论。

采用以下证据原则：

1. 每个问题必须有可访问的对照材料；
2. 优先使用 GitHub 原项目、官方文档或结构完整的公开指南；
3. 小红书、知乎等经验贴用于补充真实使用场景，并与结构化资料交叉验证；
4. 只吸收可迁移的方法，不复制个人经历、宣传语或未经验证的结论；
5. 每次修改都写明落地文件和完成状态。

## 2026-08-09：零基础可执行性审计

### I-001：所有核心论文都采用同一种精读方式，时间成本过高

- **当前问题**：README 已有三轮精读法，但没有先区分“扫描、定向阅读、核心精读”，新手容易把每篇检索结果都从头读到尾。
- **经验对照**：
  - [How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)区分泛读和精读，并建议先筛选再多次深入；
  - [本科生 0 基础 DIY 一篇 CCF-C（读论文工作流篇）](https://www.xiaohongshu.com/explore/69ecdfa30000000036003779)指出，并非每篇论文都需要完整精读，应根据用途决定阅读部分（访问可能需要登录）。
- **适用边界**：快速扫描只能用于筛选，不足以支持对方法、实验和结论的确定表述。
- **采取行动**：在 README 的论文阅读阶段增加 T0 扫描、T1 定向阅读、T2 核心精读三级投入规则。
- **状态**：已完成。

### I-002：首次复现缺少“小规模跑通”和 AI 改动审计

- **当前问题**：原流程强调官方权重和单批次训练，但没有把“通读 README—小数据冒烟测试—扩大规模”写成新手第一条路径，也没有专门记录 AI 修改了什么。
- **经验对照**：
  - [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)强调依赖、训练、评测、权重和准确命令的完整性；
  - [研 0 第一次复现实验问题实录](https://www.xiaohongshu.com/explore/6a4f6056000000001603ed70)记录了跳过项目说明、数据下载与目录差异、CPU/GPU 修改，以及“代码跑通不等于完整复现”等实际困难（访问可能需要登录）。
- **适用边界**：小数据或 CPU 冒烟测试只能验证链路，不能代替论文完整数据、设置和指标。
- **采取行动**：新增首次复现最小闭环，并在复现模板中增加 AI 辅助改动审计字段。
- **状态**：已完成。

### I-003：研究想法仍可能停留在“加一个方案”，缺少闭环与范围控制

- **当前问题**：README 已要求可证伪假设，但新手仍可能从 solution 出发，不先说明场景、缺口、机制和可观察预测；项目也容易过早扩展。
- **经验对照**：
  - [Learning Research](https://github.com/pengsida/learning_research)将寻找重要问题、提出方案、实验、写作和展示视为连续能力；
  - [科研入门建议](https://www.xiaohongshu.com/explore/69fd6029000000001e00f40a)强调 idea 需要形成闭环、先完成核心验证，并在编码前写清想法与实验计划（访问可能需要登录）。
- **适用边界**：一句话叙事用于暴露逻辑缺口，不能代替文献新颖性核验和正式实验。
- **采取行动**：增加“场景—缺口—机制—最小改动—预测—否定条件”闭环，要求先做 0 到 1，并提前建立 `research_story.md`。
- **状态**：已完成。

### I-004：周报偏个人复盘，缺少明确求助和会后行动闭环

- **当前问题**：原周报模板记录证据与决策，但没有要求在组会前写出一句话结论、具体求助问题，也没有系统记录反馈、责任人和截止时间。
- **经验对照**：
  - [weekly-report](https://github.com/SuDIS-ZJU/weekly-report)要求一句话结论、关键产物、未完成事项、阻塞风险和带优先级的下周计划；
  - [每周组会怎样汇报更高效且清晰](https://zhuanlan.zhihu.com/p/2028528459249459729)建议先说明研究问题、当前卡点和希望获得的帮助，并在会后整理反馈。
- **适用边界**：汇报格式需要适配具体课题组，模板不能替代导师已有要求。
- **采取行动**：新增“周会、导师与协作沟通”章节，并升级每周复盘模板，补充开场结论、证据、阻塞、请求、反馈和行动项。
- **状态**：已完成。

## 2026-08-09：日级可执行性审计

### I-005：八周路线缺少一次科研会话的任务粒度

- **当前问题**：README 已有八周阶段产物，但“第 3 周学习 PyTorch”仍可能被理解成观看课程或长时间自由探索。新手没有统一方法把阶段目标缩成当天可结束、可检查的工作，也缺少卡住后的停止规则。
- **经验对照**：
  - [ML Study Plan](https://github.com/patrickloeber/ml-study-plan)要求课程学习同时留下笔记、练习、独立重写和项目实践，并建议在理论尚未全部完成时开始小项目；
  - [Top2 AI 研 0｜入门 MLLM Day 4：继续跑通 CLIP](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)把一天的学习限定为运行一个 demo、检查关键张量、完成五组测试并总结能力边界，体现了“对象—操作—证据—结论”的可验收任务结构（访问可能需要登录）；
  - [考研需要知道什么？](https://www.zhihu.com/question/305966486/answer/1456645815)中的计划经验建议先制定带机动时间的周任务，再拆到每日时间段，并根据实际完成量修正未来估时。虽然场景是备考，但任务限量和容量校准可迁移到科研入门。
- **适用边界**：科研结果具有不确定性，时间盒约束的是任务范围和记录责任，不保证在限定时间内得到正向结果；不同用户不应照抄相同工时。
- **采取行动**：新增“把八周路线变成今天的任务”章节，提供 30 / 60 / 120 分钟任务粒度示例；新增原子科研任务卡，要求写明唯一主任务、产物、验收、最大范围、停止条件和下一次最小动作。
- **状态**：已完成。

## 2026-08-09：文献发现可追踪性审计

### I-006：检索要求存在，但关键词、去重和停止过程无法实际复查

- **当前问题**：README 已要求记录检索式和去重方式，但没有定义关键词如何迭代、同一论文的预印本与正式版如何归并、每篇论文来自哪次查询，以及什么时候可以停止当前检索轮。新手仍可能反复下载同一工作，把收藏数量误当成领域覆盖度。
- **经验对照**：
  - [How to Search and Read a Paper](https://github.com/qiyuangong/How_to_Search_and_Read_a_Paper)把英文关键词积累、论文分类、参考文献追踪和论文提醒视为长期循环，并提醒不分类会让论文集合快速失控；
  - [大二科研经验和工具使用详细分享（文献篇）](https://www.xiaohongshu.com/explore/68cbd6850000000012021069)记录了从只读导师给定论文，到建立关键词、会议检索、滚雪球追踪、Zotero 分类和领域统计的实际转变；评论中的新手仍集中询问关键词如何确定、检索结果是否都要阅读，说明工具清单不能替代筛选协议（访问可能需要登录）；
  - [科研入门指南：找文献篇](https://www.zhihu.com/tardis/bd/art/660258901)依次介绍关键词定位、参考文献追踪和会议 / 期刊扫描，适合作为多路径检索的经验对照；
  - [Zotero 重复项说明](https://www.zotero.org/support/duplicate_detection)使用标题、DOI、ISBN，并结合年份和作者判断候选重复项，且建议合并而不是删除，以保留分类和标签；[ASReview](https://github.com/asreview/asreview)则展示了导入、去重、分阶段筛选和保存人工判断的结构化流程。
- **适用边界**：本仓库面向小型代表性文献集合，不把探索性调研包装成系统综述。阶段性停止条件只是当前问题下的饱和判断；若要声称“系统检索”或“查全”，仍需使用适用领域的正式检索与报告规范。
- **采取行动**：重写 README 的文献发现阶段，增加关键词账本、查询 ID、DOI / arXiv / 标题作者年份去重、版本链归并、领域地图和阶段性停止条件；新增文献检索账本与领域地图模板，并让论文阅读卡记录论文 ID、查询来源和其他版本。
- **状态**：已完成。

## 2026-08-09：算力、数据与环境迁移审计

### I-007：算力预算只有估算值，缺少可迁移、可恢复和可止损的运行协议

- **当前问题**：README 原先只要求估算显存、时间、数据体积和费用，并在完整训练时保存 checkpoint。它没有要求新手区分临时盘与持久盘、规划数据与缓存路径、在干净环境中重建依赖、主动测试断点恢复，也没有把短试跑结果转换成总时长和费用上限。迁移到实验室服务器或云 GPU 后，仍可能在计费环境中反复配依赖、因路径写死重新传数据，或在实例释放时丢失训练状态。
- **经验对照**：
  - [Python 环境要配死了](https://www.xiaohongshu.com/explore/68a2ff42000000001b01e5b5)记录了本科生接到论文复现任务后，从下午到晚上仍未完成环境配置的真实阻塞，说明“导出一个环境文件”尚不足以指导干净重建（访问可能需要登录）；
  - [跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)集中提到 PyTorch、CUDA 和依赖版本不兼容，数据预处理缺失，单卡显存与论文多卡配置不匹配，以及 I/O 导致 GPU 利用率低等问题（访问可能需要登录）；
  - [学生党租 GPU 跑深度学习 tips](https://www.xiaohongshu.com/explore/685e24a2000000000d025557)提到临时算力断连、数据盘容量、上传速度、镜像匹配、后台运行和训练完成后的结果下载。该材料来自算力服务方，因此只用于识别用户痛点，不采纳其平台推荐、赠送额度或价格结论（访问可能需要登录）；
  - [为什么说大模型训练很难？](https://www.zhihu.com/question/498271491/answer/3175728305)把网络中断、设备故障、checkpoint 存储和训练参数试错成本列为长期训练的现实问题；其大模型场景不能直接等同于新手单卡实验，但“故障一定会发生、恢复能力需要预先设计”可以迁移；
  - [PyTorch 通用 checkpoint 教程](https://docs.pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html)说明续训需要保存模型之外的优化器、epoch 等状态；[PyTorch 可复现性说明](https://docs.pytorch.org/docs/stable/notes/randomness.html)明确不同版本、平台及 CPU / GPU 之间不保证完全一致；
  - [pip 可重复安装说明](https://pip.pypa.io/en/stable/topics/repeatable-installs/)区分版本锁定、哈希校验和离线安装包；[Hugging Face 缓存说明](https://huggingface.co/docs/datasets/cache)区分数据处理缓存和 Hub 下载缓存，说明只修改一个缓存变量可能不足；
  - [GitHub 大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)、[Git LFS](https://git-lfs.com/)与 [DVC](https://github.com/iterative/dvc)共同支持“Git 保存代码与元数据，大文件放在外部存储并保留版本关联”的结构。
- **适用边界**：本仓库不维护云平台价格、镜像、促销、国内镜像或可用区排行榜，因为这些信息变化快且与地区、账户和日期相关。依赖锁定不能消除操作系统、架构、驱动和框架差异；checkpoint 内容与间隔也必须根据框架、训练时长、存储吞吐和可接受损失确定。Git LFS 与 DVC 是规模增长后的可选工具，不是零基础首个小实验的前置条件。
- **采取行动**：在代码复现阶段新增供应商无关的迁移预检，要求分离 Git 内容与大体积产物，采用“干净安装—冒烟—短试跑—主动中断—恢复—成本外推—完整训练”的升级顺序；新增算力、数据与环境迁移清单，升级复现规划、模板索引、项目结构和机器可读工具表。
- **状态**：已完成。

## 2026-08-09：投稿、评审与版本链审计

### I-008：投稿检查止于格式与事实，缺少规则卡、送审冻结和评审问题矩阵

- **当前问题**：README 原有三层投稿检查和项目结束归档，但没有记录当前 venue 的回复限制，也没有冻结实际送审的 PDF、代码、配置和数据版本。收到评审后，新手仍可能逐段即兴回复，无法区分会导致结论失效的问题、影响录用判断的问题和局部表达问题；拒稿后也可能直接换模板转投，覆盖失败实验与旧版本。
- **经验对照**：
  - [Rebuttal 心得](https://www.xiaohongshu.com/explore/675973800000000002026fc8)把内容限定于 AAAI、IJCAI 等计算机会议的个人实践，并提醒学生作者与导师共同决策；评论讨论也显示，有无 rebuttal、是否需要升级沟通会随会议流程而异。因此该材料只用于识别“先核验 venue 规则”和“共同复核”的需求，不作为通用会议规则。
  - [论文审稿意见回复（干货）](https://www.xiaohongshu.com/explore/6906b6970000000003023c70)及其读者反馈显示，第一次进入回复期的学生需要可直接执行的结构化提示；该笔记主要为图片经验内容，因此只用于确认真实使用场景，不单独支持技术性结论。
  - [How to write a rebuttal for an academic paper?](https://www.zhihu.com/en/answer/187612713)区分“原文没有写清楚”和“工作本身没有完成”，建议针对事实与问题作答；[另一则作者回复经验](https://www.zhihu.com/en/answer/1932804322)强调 rebuttal 用于澄清误解和回答问题，而不是情绪宣泄。这些经验支持先分类、再回应，但不覆盖具体会议限制。
- **规范对照**：
  - [ICML 2026 Reviewer Instructions](https://icml.cc/Conferences/2026/ReviewerInstructions)说明多轮作者—评审讨论、字符限制和问题编号等机制；[ICML 2026 Peer Review FAQ](https://icml.cc/Conferences/2026/PeerReviewFAQ)明确原投稿不能在讨论期内被修订。
  - [ICLR 2026 Author Guide](https://iclr.cc/Conferences/2026/AuthorGuide)则允许讨论期修订论文，但要求清楚说明变化，并强调双盲、公开讨论和伦理沟通边界。二者差异证明不能把某一会议的 rebuttal 规则写成通用常识。
  - [CVPR Author Kit 的 rebuttal 模板](https://github.com/cvpr-org/author-kit/blob/main/rebuttal.tex)将回复限定为纠正事实错误或补充评审要求的信息，并限制新增贡献与实验；[Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)要求依赖、训练、评测、权重和精确命令完整，适合作为投稿代码快照的最低完整性对照。
  - [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)基于 tag 标记仓库历史中的特定点并提供源代码归档；[Zenodo DOI Versioning](https://zenodo.org/help/versioning)区分特定版本 DOI 与覆盖全部版本的 Concept DOI，支持对准确研究版本进行长期引用。
- **适用边界**：作者回复是否可选、是否公开、是否允许修订 PDF、补实验、外部链接或附件，必须逐年核对官方规则。Git tag 和 Release 适合标记代码状态，但不能自动包含外部数据、未跟踪产物或全部 Git LFS 内容；需要长期引用时仍应检查归档文件、元数据和许可证。负面结果只有在数据、实现和评价流程可信后，才能被解释为假设被否定或适用边界，而不是把运行失败包装成研究发现。
- **采取行动**：扩展 README 的投稿章节，增加 venue 规则卡、送审快照、P0/P1/P2 评审问题分级、证据式回复、补实验约束、拒稿与负面结果分类、转投门槛和版本归档；新增 `09-submission-review-archive.md`，并更新模板索引和推荐项目结构。
- **状态**：已完成。

## 2026-08-09：README 窄屏排版审计

### I-009：三列表格仍会压缩短字段，排版约束没有进入维护规范

- **当前问题**：仓库此前已经把最宽的五列表格改成两列，但能力分级、八周路线和变量分类仍使用三列。在手机宽度下，浏览器会压缩“等级”“周次”等列，产生逐字换行；后续贡献者也可能再次新增独立的 Star、阶段或编号窄列。
- **使用反馈对照**：本仓库使用者在 GitHub 实际预览中先后发现“第 1 周”和“Star 快照 / 适合阶段”等短字段被拆成多行，说明语法正确不等于窄屏可读。GitHub 社区的[自定义 CSS 讨论](https://github.com/orgs/community/discussions/22728)记录了 README 中 `style` 属性会被移除的实际限制，因此不能依赖自定义列宽或媒体查询修复仓库首页。
- **结构化对照**：[GitHub Flavored Markdown 表格规范](https://github.github.com/gfm/#tables-extension-)只定义表格的行、列和对齐语法，不提供响应式列宽控制；一则[响应式表格实践](https://slibbe.github.io/docs/pages/responsive-tables/)记录了普通 Markdown 表格在移动端因自动内容宽度而溢出或显示不佳，需要额外站点样式才能改成卡片，但这类样式不适用于 GitHub README。社区关于[移动端大型表格](https://www.reddit.com/r/webdev/comments/1lnmssn/what_is_the_best_way_to_display_large_tables_on/)的讨论通常建议横向滚动或按行转卡片；本仓库无法控制 GitHub 页面 CSS，因此选择在源 Markdown 层面减少列数。
- **适用边界**：两列表格不是所有 Markdown 文档的通用上限。需要精确横向比较的数据表可以保留多列并接受滚动，或移到支持响应式样式的文档站点；但主 README 面向零基础读者，导航和路线信息不应依赖横向滚动。375 px 是维护检查宽度，不代表所有设备和 GitHub 客户端的固定断点。
- **采取行动**：把能力分级、八周路线和变量分类三处表格改为两列，用“当前 / 下一步”“产物 / 完成”标签在单元格内分层；在贡献指南中新增两列表格上限、窄列合并、禁止依赖自定义 CSS 和 375 px 窄屏检查规则。
- **状态**：已完成。

## 2026-08-09：首次访问路径审计

### I-010：首屏有统一起步清单，但不同能力层缺少直接分流

- **当前问题**：README 已经说明目标读者、完整闭环和第一次使用的五件事，但 L0、L1、L2 以及正在投稿的读者仍共用一条线性入口。已经会 Python 的读者可能重复补基础，完全零基础的读者也可能过早进入论文复现；长目录不能替代“我现在应该点哪里”的明确选择。
- **经验对照**：
  - [Learning Research](https://github.com/pengsida/learning_research)明确面向实验室新人，并把科研入门、能力培养、项目执行和论文写作拆为不同入口，同时提醒经验需要在实践和交流中学习、未必适用于所有实验室。这支持按状态导航，而不是假定所有读者从同一章节开始。
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)在长课程目录之前提供 Getting Started 和面向学生的逐步使用方式，要求 fork、clone、完成活动与作业并留下产物；课程允许整体或按需使用，说明大型入门资源需要明确起点和可跳过边界。
  - [本科生 0 基础 DIY 一篇 CCF-C（读论文工作流篇）](https://www.xiaohongshu.com/explore/69ecdfa30000000036003779)按阅读目的区分投入深度；[入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)把一天任务缩成 demo、检查和结果总结。两类经验共同表明，新手更需要与当前状态匹配的下一步，而不是先消化完整资料库（访问可能需要登录）。
- **规范对照**：[GitHub 的 README 说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)将“项目做什么、为什么有用、如何开始、在哪里获得帮助”列为典型 README 信息，并建议主 README 保留开始使用和贡献所需内容。Microsoft 的一份[入门仓库升级计划](https://github.com/microsoft/Generative-AI-for-beginners-dotnet/blob/main/MAF-V1-UPGRADE-PLAN.md)也把面向绝对新手的 Start Here 与多条学习路线列为根 README 的改进项。
- **适用边界**：L0–L2 是本仓库用于选择入口的操作性分级，不是对研究能力的正式评价。读者可以跳过已掌握章节，但不能跳过环境文件、实验日志等阶段产物；正在选题或投稿者仍需遵循所在课题组和目标 venue 的具体要求。
- **采取行动**：在首次使用章节顶部新增“30 秒选择入口”，分别为 L0、L1、L2 和投稿阶段提供直达模板、章节与周次；明确无法判断时从检查表开始，已掌握内容可以跳过但必须提供对应产物；在贡献指南中加入一分钟找到起点的首屏验收规则。
- **状态**：已完成。

## 2026-08-09：调试与求助路径审计

### I-011：复现流程记录了报错，但缺少最小复现、求助路由和仓库 Issue 入口

- **当前问题**：复现规划已经记录原始报错和 AI 修改，但 README 没有告诉新手如何把问题缩成别人能够运行的样例，也没有区分“本仓库文档问题、第三方项目 bug、自己的代码问题和研究协议问题”。仓库还没有 SUPPORT 文件或 Issue 表单，求助时容易遗漏完整命令、commit、配置、环境、预期行为和首个关键报错。
- **经验对照**：
  - [Python 环境要配死了](https://www.xiaohongshu.com/explore/68a2ff42000000001b01e5b5)与[跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)显示，新手的“代码跑不起来”往往混合了环境、CUDA、预处理、显存和 I/O 等多类原因；只给最后一行报错无法判断问题边界（访问可能需要登录）。
  - Transformers 的一个[实际 Issue #33405](https://github.com/huggingface/transformers/issues/33405)提供了 traceback，却没有清楚说明具体模型和上游集成边界，维护者因此无法判断模型并将问题指向 LangChain。该案例说明完整报错仍不能替代最小复现和正确路由。
  - [Stack Overflow 最小可复现样例指南](https://stackoverflow.com/help/minimal-reproducible-example)把可回答的问题概括为最小、完整、可复现，并要求说明预期、实际和精确错误；代码应使用可复制文本而不是截图。
- **规范与项目对照**：[PyTorch Bug Report](https://github.com/pytorch/pytorch/blob/main/.github/ISSUE_TEMPLATE/bug-report.yml)要求自包含的精简代码、实际与预期结果、完整 traceback 和环境采集；[Transformers Bug Report](https://github.com/huggingface/transformers/blob/main/.github/ISSUE_TEMPLATE/bug-report.yml)要求系统信息、问题来源、配置、复现代码和预期行为，并提示模型仓库问题应联系模型作者。[GitHub Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)用于引导贡献者提交高质量问题。
- **适用边界**：最小复现适合调试可公开的技术问题，不能要求用户泄露私有数据、密钥、内网信息、未公开论文或匿名评审材料。研究假设、实验公平性和结论边界不能仅靠上游软件 Issue 解决；如果问题只在私有数据上出现，应使用合成或脱敏数据尝试复现，并在获授权的私密渠道继续排查。
- **采取行动**：新增 README“卡住时如何求助”章节、`10-debug-help-request.md`、`SUPPORT.md` 和仓库 Issue Form；统一记录目标、预期、实际、完整命令、commit、配置、环境、最小复现、已尝试排查和具体请求，并明确本仓库、第三方上游、导师协作与私密渠道的分工。
- **状态**：已完成。

## 下一轮优先审计

- 仓库的许可证、引用、版本发布和长期维护信息是否完整，能否让他人合法复用并准确引用本仓库。
