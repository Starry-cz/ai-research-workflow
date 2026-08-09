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

## 2026-08-09：许可、引用与发布审计

### I-012：公开仓库缺少许可证、机器可读引用和面向读者的版本记录

- **当前问题**：仓库已经公开并允许贡献，但根目录没有 `LICENSE`、`CITATION.cff` 或 `CHANGELOG.md`。读者无法判断能否复制、修改和再分发原创说明与模板，也没有稳定方法引用某个具体版本；维护者新增流程时也缺少面向读者的变更摘要。
- **经验对照**：[如何选择 GitHub 开源许可证](https://www.zhihu.com/en/article/694255272)按广泛复用、衍生作品开放要求和专利条款区分 MIT、GPL、Apache 等选择，说明许可证不是装饰文件，而是作者对复用边界的决定。该经验只用于识别决策维度，具体法律效果仍以正式许可证文本和适用法律为准。
- **规范对照**：[GitHub 许可证说明](https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)明确，没有许可证时默认版权法生效，其他人不能当然复制、分发或创建衍生作品；[GitHub CITATION 说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)说明根目录的 `CITATION.cff` 会生成“Cite this repository”入口；[CFF 1.2 schema guide](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md)要求作者、标题、版本等机器可读字段。GitHub Release 基于 tag 指向特定历史点，适合与版本引用对应。
- **适用边界**：许可证选择会改变他人使用、修改和分发本仓库内容的权利，不能根据“公开仓库”或常见项目惯例替作者决定。仓库含原创文字、模板和外部链接说明，是否采用单一许可证或为文档与代码/模板分别授权需要作者确认；CITATION 中的姓名、ORCID 和版本号也应由作者确认，不能从账号名推断真实身份。
- **采取行动**：新增 `CHANGELOG.md`，在 README 中明确当前默认版权状态、临时引用方式和外部资源独立许可；贡献指南要求面向读者的变化同步更新变更记录。`LICENSE`、`CITATION.cff` 和首个 Release 保留为作者确认后的下一步，不擅自选择。
- **状态**：部分完成，等待作者确认许可与引用信息。

## 2026-08-09：首次完整演练与结果可信性审计

### I-013：模板之间没有完整可运行示例，固定 seed 也可能被误解为结果可靠

- **当前问题**：仓库已经提供研究简报、复现规划和实验卡，但新手看不到一次运行如何把问题、配置、命令、环境、日志、全部重复实验、汇总指标和结论边界连起来。README 原先要求固定或运行多个随机种子，却没有明确区分“固定 seed 便于调试”和“重复运行用于描述结果波动”；读者仍可能只保留最好一次，或把单次可重复误写成方法普遍可靠。
- **经验对照**：
  - [第一篇论文复现](https://www.xiaohongshu.com/explore/67cfb412000000002a00c7e8)记录了首次复现耗时约一周、代码多次无法运行，最终定位到环境与依赖版本；评论中的新手还会询问是否必须从头写代码。这说明仅给检查项不足以消除“先做什么、留下什么”的不确定性，访问可能需要登录；
  - [研究生读了一年才把论文复现整明白](https://www.xiaohongshu.com/explore/6a3bcaa0000000000f0150e8)把目标指标、资源审计、预训练评测、单批次测试、证据标签和多 seed 汇总组织成阶段化路径。该内容带有自动化工具推广，因此本仓库只用它识别用户痛点和流程结构，不采信“一句话自动完成研究”等效果承诺；
  - 知乎关于[是否能报告最高准确率](https://www.zhihu.com/en/answer/3249240394)、[最终结果如何取值](https://www.zhihu.com/en/answer/2229914309)和[相同 seed 结果不同能否选最好一次](https://www.zhihu.com/en/answer/3031680072)的讨论反复出现“固定 seed、最好一次、均值与波动”的混淆。回答质量不一，因此这些讨论只用于证明困惑真实存在，不作为统计规范。
- **规范与项目对照**：
  - [Made With ML](https://github.com/GokuMohandas/Made-With-ML)先用交互式完整示例建立端到端理解，再把同一工作负载拆成脚本并用 run ID 跟踪训练、调参与评估，支持“先展示一条完整路径，再介绍抽象模板”的教学顺序；
  - [PyTorch Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html)明确说明跨版本、平台和 CPU / GPU 无法保证完全一致，控制随机性有助于调试和比较，但确定性操作可能降低性能；
  - [Tuning Playbook](https://github.com/google-research/tuning_playbook)区分科学变量与干扰变量，要求为公平比较规划调参预算、搜索空间、试验和停止决策；
  - [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)要求在适用时给主要实验提供误差条、置信区间或统计检验，说明变异来源与计算方式，并报告每次运行和总计算量。这些要求支持披露不确定性，但不规定所有任务使用同一种汇总指标。
- **适用边界**：仓库内演练使用合成数据和纯 Python 小模型，只用于训练证据链，不能替代论文复现或支持算法优越性。调试运行可以使用单一固定 seed；支持科研结论时需要多少次运行、采用标准差还是区间、以什么为统计单位，应结合任务波动、预算和目标 venue 预先确定，不能把本示例的五个 seed 当成通用规则。资源不足时可以报告试运行，但必须收缩主张并披露限制。
- **采取行动**：新增 `examples/first-workflow-drill/`，提供可在 CPU 上运行的脚本、两份单变量配置、已填写实验卡和真实生成的配置快照、环境、日志与全部运行指标；在 README 增加首次演练入口和“调试模式 / 证据模式”规则；升级实验卡，记录运行模式、预先计划的 seed、调参预算、选择与排除规则、波动来源和结论边界；在贡献指南中禁止编造示例结果或只展示最好一次。
- **状态**：已完成。

## 2026-08-09：首篇真实 baseline 准入审计

### I-014：筛选表只有偏好项，缺少低成本预检、停止门槛和备选候选

- **当前问题**：README 原先建议优先正式论文、官方代码、训练与评测入口，但读者仍可能看到热门或高 Star 项目就直接投入，只在配置数天后才发现数据不可用、训练入口缺失、指标无法对应或完整训练远超预算。现有筛选表也没有区分“官方权重跑通、短训练跑通、完整协议复现”三个不同层级，失败时缺少退出条件和备选候选。
- **经验对照**：
  - [研 0 第一次复现实验问题实录](https://www.xiaohongshu.com/explore/6a4f6056000000001603ed70)记录了跳过 README、数据目录和 CPU / GPU 差异后反复报错，以及“代码运行不等于完整复现”的实际困惑；[第一篇论文复现](https://www.xiaohongshu.com/explore/67cfb412000000002a00c7e8)则把首次复现中最耗时的问题定位到环境和依赖版本。这些材料支持先做低成本预检，访问可能需要登录；
  - 知乎回答[怎么样从小白自学到能读懂机器学习的论文并复现](https://www.zhihu.com/question/659628177/answer/2002333417153513369)建议先找开源代码、搭建对应环境并从经典小任务开始。其“优先 Star 多”等说法只反映个人筛选经验，本仓库不把 Star 设为准入条件，而用可核验的训练、评测、数据和资源证据替代。
- **规范与项目对照**：
  - [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)把依赖、训练代码、评测代码、预训练模型，以及能够生成主要结果的精确命令列为代码完整性的五项核心内容；这些项目侧信息可以反向用于判断一篇论文是否适合作为首个复现对象；
  - [ML Reproducibility Challenge 2022 任务说明](https://paperswithcode.com/rc2022/task)明确指出，仅重新运行代码不构成复现研究，还需要批判性检查实现是否对应论文以及实验是否足以支持原主张；
  - [IJCAI-ECAI 2022 Reproducibility Guidelines](https://ijcai-22.org/reproducibility/index.html)区分不可复现、可信和有说服力的可复现程度，并将算法、数据、实验细节、硬件和环境作为不同证据组成；
  - [MICCAI Reproducibility Checklist](https://github.com/JunMa11/MICCAI-Reproducibility-Checklist)进一步列出数据、预处理、训练、评测、环境、停止和模型选择等领域化信息，说明“有仓库链接”不能代表复现入口完整。
- **适用边界**：准入门控只判断“是否适合作为当前读者的首篇 baseline”，不评价论文质量，也不要求所有理论研究或闭源数据工作提供相同产物。只有推理代码仍可用于功能演示和代码阅读，第三方实现也可用于实现研究；但如果目标是完整训练复现，应改变交付名称或选择资料更完整的候选。项目由导师指定时，可以保留 `REFINE`，同时记录额外支持、缺失证据和调整后的里程碑。
- **采取行动**：重写 README 的首篇 baseline 筛选段落，增加两到三个候选、准入条件、加分项、低成本预检、`PROCEED / REFINE / STOP` 和 M0–M3 分层里程碑；新增 `11-first-baseline-gate.md`，记录目标结果、官方关系、数据与许可证、依赖、精确训练评测命令、权重、算力外推、失败退出和备选候选；同步更新研究简报、模板索引、推荐项目结构和教学演练的真实项目入口。
- **状态**：已完成。

## 2026-08-09：L0 工具链起步审计

### I-015：能力清单要求会 Git 和环境，但没有跨系统的第一条可执行路径

- **当前问题**：README 已把终端、Git、Python 和独立环境列为最低能力，却只告诉 L0 读者“安装并学会”，没有说明 Windows 与 macOS/Linux 的命令差异、如何确认 `pip` 和运行代码属于同一解释器、为什么 clone 与 ZIP 不同，以及第一次 commit 前如何排除虚拟环境和密钥。读者需要先到多个教程拼接步骤，容易在开始科研前形成全局环境污染或无法追踪版本的项目。
- **经验对照**：
  - [Python 环境要配死了](https://www.xiaohongshu.com/explore/68a2ff42000000001b01e5b5)、[跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)和[第一篇论文复现](https://www.xiaohongshu.com/explore/67cfb412000000002a00c7e8)共同暴露了 Python、CUDA、依赖版本和环境边界是首次复现的主要阻塞之一，访问可能需要登录；
  - 知乎的[安装了库却找不到](https://www.zhihu.com/tardis/bd/art/677085682)把高频问题归因于安装包的 `pip` 与运行代码的 Python 不属于同一环境，并建议核对 `sys.executable`。该内容只用于确认真实困惑，具体操作以 Python 官方指南为准；
  - 一些中文环境教程同时建议管理员安装、永久换源、修改系统 Python 或建立“万能环境”。这些做法会随系统和网络条件变化，且可能扩大权限或污染全局环境，因此本仓库没有把它们写成默认方案。
- **规范与项目对照**：
  - [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)分别给出 Windows 的 `py -m venv` 与 Unix/macOS 的 `python3 -m venv`，要求将 `.venv` 排除在版本控制外，并核对解释器位置；
  - [Python 安装包指南](https://packaging.python.org/en/latest/tutorials/installing-packages/)建议使用虚拟环境和 `python -m pip`，并提醒不要用 `sudo` 修改系统管理的 Python；
  - [Git First-Time Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)说明姓名和邮箱会写入每次 commit，并提供配置来源检查；[GitHub clone 文档](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)说明 clone 包含仓库的文件与版本历史；[GitHub 邮箱说明](https://docs.github.com/en/account-and-profile/concepts/email-addresses)提供 `noreply` 地址以避免公开私人邮箱；
  - [Missing Semester](https://missing.csail.mit.edu/)把 shell、版本控制、调试和数据整理视为可在实际任务中训练的工具能力，支持用一个有产物的短闭环作为入口，而不是先完成整套课程。
- **适用边界**：`venv + pip` 是为了提供零依赖、跨系统的第一条路径，不宣称优于 conda、uv、Poetry、容器或实验室模块系统。真实论文仓库应优先遵循其官方环境文件和硬件支持矩阵；`pip freeze` 只是当前环境快照，不是跨平台锁文件。学校集群还需遵守登录节点、调度器、存储与软件模块规则，不能直接套用个人电脑训练命令。
- **采取行动**：新增 `docs/L0_TOOLCHAIN_START.md`，分别给出 Windows 与 macOS/Linux 的版本检查、独立 `.venv`、直接解释器调用、仓库内调试演练、`.gitignore`、环境记录和第一次精确暂存/commit；明确不用降低 PowerShell 策略、管理员权限或 `sudo pip` 绕过环境问题；在 README 的 L0 入口、第一次执行和工具导航中直达该指南，并让准备检查表记录解释器、pip 和 commit 证据。
- **状态**：已完成。

## 2026-08-09：第一个机器学习闭环审计

### I-016：课程清单与论文复现之间缺少数据角色、训练循环和泄漏的最小桥接

- **当前问题**：README 要求 L1 读者理解数据划分、loss、指标和训练循环，也推荐多套完整课程，但没有用仓库内同一个例子把样本、模型、优化、训练 / 验证 / 测试职责和指标证据串起来。新手可能会运行 Notebook，却仍不知道预处理应在哪个 split 上拟合、验证集用于什么、为什么不能反复看测试集，以及 loss 下降为什么不等于研究结论成立。
- **经验对照**：
  - 知乎关于[训练 / 验证 / 测试集划分](https://www.zhihu.com/tardis/bd/art/486396145)和[机器学习自学](https://www.zhihu.com/question/7859966761/answer/1999896259041989042)的内容显示，新手通常先通过“小项目完整跑一遍”理解数据划分、训练和评价，但经验文中的固定比例或反复重划分建议不适合直接作为通用规范；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)把一天任务缩成 demo、检查与结果总结，说明初学者需要小闭环和明确产物，而不是先完成全部理论课程，访问可能需要登录；
  - 本仓库此前的教学演练已经保存训练、验证和测试结果，但没有专门解释各 split 的权限，实际可运行产物还没有转化为概念理解。
- **规范与项目对照**：
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)采用从小到大的项目式课程，每课包含知识检查、活动和作业，支持“概念必须落到可运行产物”的教学方式；
  - [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)把数据、DataLoader、模型、自动微分、优化和保存组织成完整工作流；[Datasets & DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)明确一个 batch 包含 features 和 labels，并给出 shape；
  - [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)要求先切分数据，只在训练集上 `fit` 预处理和特征选择，并说明测试信息泄漏会造成过于乐观的估计；
  - 前一轮采用的 [Tuning Playbook](https://github.com/google-research/tuning_playbook)进一步支持用验证数据进行选择、冻结协议后再形成测试证据，而不是根据最终结果反向修改方案。
- **适用边界**：仓库演练是固定合成二分类任务，手写梯度且没有 mini-batch，不能替代真实数据、PyTorch 或领域评价。数据比例、划分单位、交叉验证和指标必须按样本依赖、时间、主体、类别和目标场景确定；本指南只规定三类数据的权限和可审计性，不给出通用比例。PyTorch 官方基础教程主要用于学习 API，其数据组织也不能直接视为所有科研项目的评价协议。
- **采取行动**：新增 `docs/ML_FIRST_LOOP.md`，用现有真实运行脚本逐项映射样本、参数、前向、loss、优化、epoch、指标和 seed；明确训练 / 验证 / 测试权限、最小泄漏检查、指标边界、口头复盘、单变量练习和迁移到 PyTorch 的验收；为教学脚本增加必要中文注释，并在 README 的 L1 入口、首次演练和工具导航以及准备检查表中建立直达路径。
- **状态**：已完成。

## 2026-08-09：按任务补数学路径审计

### I-017：数学资源存在，但没有任务触发、学习深度和代码验收

- **当前问题**：README 已推荐 Mathematics for Machine Learning、Pumpkin Book 和 Zero to Hero，也提醒读者按需补数学，但没有说明什么问题应触发哪类数学、公式至少读到哪一层、何时可以暂缓证明，以及如何用 shape、玩具数值和代码检查验收。新手容易走向两个极端：认为“数学没学完就不能开始科研”，或完全跳过公式、只根据库调用和运行结果判断方法。
- **经验对照**：
  - 知乎关于[从小白到读懂并复现机器学习论文](https://www.zhihu.com/question/659628177/answer/2002333417153513369)的经验强调理解梯度下降等概念的实际意义，并把数学与小项目结合；关于[机器学习自学路线](https://www.zhihu.com/question/7859966761/answer/1999896259041989042)的讨论也反映出初学者常在“先补全部数学”和“先跑项目”之间摇摆。两者都是个人经验，本仓库只吸收任务驱动和实践核对的思路，不采用固定课时或统一先后顺序。
  - [Pumpkin Book](https://github.com/datawhalechina/pumpkin-book)明确定位为《西瓜书》公式推导的补充，建议在特定推导阻塞时结合原书查阅，支持“遇到当前公式再定向补”的使用方式，而不是把补充推导当成开始实验前必须通读的课程。
- **规范与项目对照**：
  - [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io)把线性代数、几何、矩阵分解、微积分、概率和优化与具体机器学习方法分开组织，适合作为按概念定位的基础参考；
  - [Dive into Deep Learning 数学附录](https://www.d2l.ai/chapter_appendix-mathematics-for-deep-learning/index.html)说明很多深度学习实践可以在不掌握完整数学体系时开始，同时指出理解梯度、损失假设、概率与信息论会需要更深数学；
  - [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)从 micrograd 和反向传播的手写实现进入神经网络，并配有练习，适合建立公式、计算图与代码之间的映射；
  - 当前论文原文和官方代码仍是定义、符号约定与实际实现的最终核验入口，教学项目和第三方解释不能替代版本对应关系。
- **适用边界**：“按需补”不等于不学数学。修改 loss、归一化、注意力、采样、优化与统计分析，或提出理论、复杂度、因果和显著性主张时，必须理解会改变实现与结论的假设。玩具数值、有限差分和自动微分可以发现实现错误，但不是理论证明；统计方法还需要遵守任务领域和目标 venue 的评价规范。
- **采取行动**：新增 `docs/MATH_ON_DEMAND.md`，建立“阻塞—定位—符号与 shape—假设—玩具数值—代码核对—返回任务”的闭环，并区分可暂缓内容与不能跳过的场景；新增 `12-math-concept-card.md`，把公式位置、变量、数据流、假设、边界、数值例子、代码 commit 和验收写入同一张卡；同步更新 README 的最低产物、论文阅读、工具导航、模板索引、项目结构和准备检查表。
- **状态**：已完成。

## 2026-08-09：数据准入、版本与泄漏审计

### I-018：数据记录分散，无法证明使用权、具体版本和测试独立性

- **当前问题**：README 和复现模板会记录数据来源、许可证、版本与划分，但缺少一张贯穿下载、内容、处理和评价的数据卡。读者仍可能把“文件能下载”理解为“允许训练和上传”，使用同名但不同版本的数据，逐行随机切分同一主体的相关样本，先对全量数据做插补或特征选择，再用测试集反复选择方案。现有 `data/README.md` 一行说明无法让协作者重建数据，也不能证明测试指标来自真正未见数据。
- **经验对照**：
  - [跑 baseline 常见的坑](https://www.xiaohongshu.com/explore/6925b658000000001d03acfb)和[研 0 第一次复现实验问题实录](https://www.xiaohongshu.com/explore/6a4f6056000000001603ed70)把数据目录、预处理、训练 / 测试入口混入同一类“代码跑不起来”问题，说明新手常在环境排错时忽略数据协议；这些笔记访问可能需要登录，本仓库只用其确认真实困惑，不据此制定数据规范；
  - 知乎的[训练 / 验证 / 测试集划分](https://www.zhihu.com/tardis/bd/art/486396145)给出多个固定比例，并建议结果差异较大时重新划分；关于[缺失值处理](https://www.zhihu.com/question/268540071)的讨论甚至把训练集和测试集共同拟合变换描述为某些条件下近似可用。这些观点表明固定比例、重划分和预处理泄漏的误解真实存在，但它们不能作为执行依据，本仓库用官方文档明确更保守的评价边界。
- **规范与项目对照**：
  - [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)要求从动机、组成、收集、处理、用途、分发和维护记录数据生命周期，避免数据使用者只看到文件而看不到形成背景；
  - [Hugging Face Dataset Card Guide](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md)覆盖结构、字段、split、来源、标注、个人敏感信息、偏差、限制、许可证和引用，并允许对未知项明确写待补信息；
  - [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)要求先划分数据，只在训练集上拟合预处理和特征选择；[grouped cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data)要求同一主体或 group 不跨训练与评价集合；[TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)避免用未来数据训练后评价过去；
  - [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)要求说明外部资产版本、许可证和条款，并在涉及人的数据时讨论同意、可识别信息和风险。
- **适用边界**：本仓库提供的是通用最低审计，不能替代医疗、教育、生物、金融、未成年人或机构内部数据的伦理、法律和安全流程。校验值只证明文件身份，不证明数据正确、合法、无偏或无泄漏；随机划分、group 划分和时间划分都不是普遍最优，必须与真实泛化目标对应。引用上游数据卡时应区分“上游声明”和“本地已验证”。
- **采取行动**：新增 `docs/DATASET_FIRST_AUDIT.md`，建立 D0–D4 数据准入门，说明数据身份、样本单位、group / 时间划分、重复与处理泄漏、质量报告、原始与处理数据分离以及特殊数据追加规则；新增 `13-dataset-card.md`，统一记录来源与权利、revision、manifest、schema、采样、标注、split、质量、泄漏、处理版本链和准入决定；为仓库内合成演练新增真实填写的数据卡和本地核验统计；同步更新 README 的复现流程、工具导航、模板索引、项目结构、误区、准备检查表、研究简报与复现规划。
- **状态**：已完成。

## 2026-08-09：评价协议与统计单位审计

### I-019：指标字段只有名称，无法约束实现、选择与结论边界

- **当前问题**：README 和实验卡要求记录主指标、波动与统计方案，但读者仍可只写 `F1`、`AUC` 或 `accuracy` 后开始运行，没有固定正类、macro / micro 聚合、阈值、实现版本、异常输出、统计单位和实际意义门槛。测试结果出来后再选择最好 seed、子集、阈值或更有利的指标，会让测试集参与方案设计。人工评价与模型评审也缺少 rubric、盲法、样本分配、分歧处理和校准要求。
- **经验对照**：
  - 知乎关于[从小白到论文复现](https://www.zhihu.com/question/659628177/answer/2002333417153513369)把 accuracy、precision、recall、F1 和 ROC/AUC 列为“常用指标”，关于[如何选择模型性能评估标准](https://zhuanlan.zhihu.com/p/59306053)则分别解释分类、回归和排序指标。这些材料说明新手首先接触的是指标名称与公式，但仅认识名称仍不足以重建论文的 aggregation、阈值和实现；
  - 知乎对[能否报告最高准确率](https://www.zhihu.com/en/answer/3249240394)、[最终结果如何取值](https://www.zhihu.com/en/answer/2229914309)和[相同 seed 是否选最好一次](https://www.zhihu.com/en/answer/3031680072)的讨论反复出现“最好一次、均值、标准差和固定 seed”的混淆。回答质量不一，本仓库只用这些讨论确认困惑存在，统计规则以实验设计和 venue 规范为准。
- **规范与项目对照**：
  - [scikit-learn Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)说明二分类指标扩展到多分类 / 多标签时需要明确 positive label 和 macro、micro、weighted、samples 等聚合，同名 F1 并不天然等价；
  - [Google Classification Metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)把 accuracy、precision 和 recall 与类别不平衡、阈值及误报 / 漏报代价联系，说明指标必须从任务决策而非排行榜习惯出发；
  - [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)要求主要实验在适用时报告误差条、置信区间或统计检验，并解释变异来源和计算方法；[ACL-IJCNLP Reproducibility Checklist](https://2021.aclweb.org/calls/reproducibility-checklist/)要求清楚定义评价统计量、运行次数、选择标准和汇总统计；
  - [Twenty Years of Confusion in Human Evaluation](https://aclanthology.org/2020.inlg-1.23/)发现 NLG 人工评价构念与报告方式长期不统一，削弱跨论文比较和复现；[ACL Ethics：Researchers](https://ethics.aclweb.org/roles/researchers/)要求提供评价者完整说明、招募、同意、报酬和伦理信息。
- **适用边界**：本指南不为所有任务指定 accuracy、F1、显著性水平、区间方法或固定重复次数。统计单位、检验、bootstrap、实际意义和人工评价设计必须适配数据依赖、主张、目标领域与 venue；资源不足时可以报告描述性结果，但应降低主张强度。模型评审可以扩展人工评价，却不能因输出像评分就自动替代人工校准和偏差审查。
- **采取行动**：新增 `docs/EVALUATION_FIRST_SPEC.md`，从决策与错误代价进入主指标，区分训练 loss、选择指标、主测试指标和辅助指标，规定实现、聚合、阈值、统计单位、不确定性、人工评价、模型评审和效率测量的冻结要求；新增 `14-evaluation-spec.md`；为合成演练新增已填写 Eval Spec，明确 accuracy、交叉熵、阈值、seed 汇总和总体标准差的含义及其非置信区间边界；同步更新 README、准备检查表、实验卡、模板索引、项目结构和误区。
- **状态**：已完成。

## 2026-08-09：结果到主张的证据链审计

### I-020：声明—证据台账只有字段，没有配对错误、图表来源和主张强度门控

- **当前问题**：README 已要求建立声明—证据台账，但没有给出可直接填写的模板，也没有要求从逐样本 / group 预测检查“候选修复”和“候选破坏”、区分预设分析与看完结果后的探索性切片，或为每张结果图表记录输入文件和生成命令。新手仍可能把平均分提高直接解释为机制成立、普遍泛化或方法有效，再挑选几个成功案例配图。
- **经验对照**：
  - 知乎的[高水平论文写作经验](https://www.zhihu.com/tardis/zm/art/596042829)强调研究问题、假设、实验、结果和含义需要形成逻辑链，每个图表还应有结果和反常结果的解释；[如何高效读论文](https://www.zhihu.com/tardis/zm/art/35170379)指出只展示图表而不分析就直接进入结论是常见缺口。这些内容主要是写作经验，本仓库吸收“图表服务问题和解释”的结构，不采用其中的固定表达模板或发表承诺；
  - [第一次复现](https://www.xiaohongshu.com/explore/67cfb412000000002a00c7e8)和[研究生读了一年才把论文复现整明白](https://www.xiaohongshu.com/explore/6a3bcaa0000000000f0150e8)反映出新手通常先关注结果是否接近论文，再逐渐意识到失败样本、协议层级和证据标签的重要性；这些笔记访问可能需要登录，且后者带有工具推广，因此只用于确认分析痛点。
- **规范与项目对照**：
  - [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)要求摘要和引言中的主张与理论、实验结果的范围一致，并披露重要假设与限制；
  - [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/)展示 held-out accuracy 仍可能遗漏关键行为失败，支持按能力、测试类型和具体反例补充平均指标；
  - [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)要求提供训练与评测代码，以及生成主要结果的精确命令；[ACM Artifact Evaluation 示例规则](https://sigsim.acm.org/conf/pads/2024/blog/artifact-evaluation/)进一步要求产物有文档、与论文一致、可执行，并为待复现图表提供脚本；
  - [NeurIPS LLM Checklist Assistant 实验](https://blog.neurips.cc/2024/12/10/results-of-the-neurips-2024-experiment-on-the-usefulness-of-llms-as-an-author-checklist-assistant-for-scientific-papers/)在人工检查中发现模型会补写原文不存在的硬件描述和占位 URL，说明 AI 生成的结果解释和证据位置必须回到原始材料核验。
- **适用边界**：不同任务的错误单位、切片、行为测试和机制证据不同；本指南不要求所有论文使用同一种 taxonomy。逐样本错误分析不能替代统计评价，消融通常也不能单独证明因果或唯一机制。受限数据无法公开时仍应在授权环境保留内部来源链，并用可公开的脱敏说明交代缺失范围。
- **采取行动**：新增 `docs/RESULT_TO_CLAIM.md`，建立“冻结输入—完整性—配对错误—探索 / 确认—替代解释—主张分级—图表来源”的分析闭环；新增 `15-result-claim-audit.md`，统一记录逐样本 / group 错误、反证、figure / table 生成链和 `verified / qualified / pending / rejected` 主张；为教学演练新增已填写审计，明确哪些工作流观察成立、为什么“学习率普遍更优”必须拒绝，以及缺少逐样本预测造成的分析边界；同步更新 README、实验卡、模板索引和项目结构。
- **状态**：已完成。

## 2026-08-09：模板认知负担审计

### I-021：专业模板持续增加，但没有最小包和触发边界

- **当前问题**：经过数据、评价和结果审计后，主 README 已有 1125 行，`templates/` 有 16 张业务模板。虽然每张表单各自有用途，但“可直接复用”列表容易让零基础读者误以为要按编号全部填完，或在尚未取得数据和结果时提前猜测字段。工具库如果只持续增加清单而不控制激活范围，会从降低门槛变成新的流程负担。
- **经验对照**：
  - 知乎关于[计算机公开课资源](https://www.zhihu.com/question/38335108/answer/1993372768251687650)直接指出资源已经多到难以选择，核心问题是判断哪些值得投入；另一篇[入门经验](https://www.zhihu.com/tardis/landing/yidian/ans/2046292839185606022)也概括了“收藏夹教程越多，越不知道从哪一块开始”的困惑。这些内容可能带有课程或服务推荐，本仓库只吸收“选择成本是真实阻塞”的观察；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)把一天限制为 demo、检查和总结，体现单次只激活当前任务所需产物；访问可能需要登录，其固定任务数量不作为通用规范；
  - [Learning Research](https://github.com/pengsida/learning_research)明确其经验需要结合实践、交流和具体实验室情境使用，而不是把全部建议视为普遍清单。
- **规范与项目对照**：
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)采用从小到复杂的项目式课程，每课配有活动、检查与作业，并明确课程可以整体或按部分使用；这支持“当前阶段完成一个可运行产物”而不是一次加载全部内容；
  - 本仓库已有的原子任务规则和 L0–L3 分流也表明，阶段产物应该由当前阻塞与升级条件触发，不能因模板存在就默认必填。
- **适用边界**：减少认知负担不等于删除高风险门控。真实数据进入项目前仍需数据卡，正式比较前仍需评价协议，写论文结论前仍需结果—主张审计；区别在于它们按阶段触发。导师或实验室已有等价台账时应复用并补缺，不维护两套重复记录。
- **采取行动**：在 README 首屏入口后新增 L0 工具起步、L1 选方向、L2 做复现和 L3 做实验四个最小模板包及升级条件；把周会、原子任务、算力迁移、调试、数学和投稿卡改为事件触发；明确同一时间只维护一个阶段门控、一个当前任务 / 实验记录和最多一个按需卡；重写模板索引的最短路径；在贡献指南中要求新模板说明所属阶段、触发条件和现有模板不能覆盖的原因。
- **状态**：已完成。

## 2026-08-09：README 信息架构审计

### I-022：首页同时承担入口、教程和规范手册，零基础读者无法快速建立全局地图

- **当前问题**：主 README 在连续增加数据、评价和结果协议后达到 1142 行。“30 秒入口”和八周路线在前部，但完整工作流又用近 600 行展开九个阶段，后面才出现工具、资源和模板导航。内容本身有用，组织方式却让第一次访问者难以判断哪些必须现在阅读、哪些只在对应阶段查阅，也增加了维护重复规则和失效锚点的风险。
- **经验对照**：
  - 知乎关于[计算机公开课资源](https://www.zhihu.com/question/38335108/answer/1993372768251687650)和[入门教程收藏负担](https://www.zhihu.com/tardis/landing/yidian/ans/2046292839185606022)反映出，新手的阻塞往往不是没有材料，而是无法从大量入口中确定当前动作；这些内容可能包含课程或服务推荐，本仓库只用来确认选择成本；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)用一天一个小任务和明确产物降低启动成本，说明首页应该先给行动粒度，再提供扩展材料；该笔记可能要求登录，其固定天数和任务不作为通用路线。
- **规范与项目对照**：
  - [Learning Research](https://github.com/pengsida/learning_research)的根 README 交代目标、适用边界和能力框架，再把 3D Vision 入门与进阶能力拆到 `getting_started_in_research.md`、`getting_advanced_in_research.md`；这种分层让概览和操作细节各自承担单一职责，但其中领域课程和实验室协作方式不能直接泛化到所有 AI 方向；
  - [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)在 README 展示快速入口、阶段组、产物和关键门控，并把配置、23 阶段细节、恢复和排错放到独立集成指南。可借鉴的是“阶段产物—检查点—详细手册”的信息结构，不是“一句话自动产出论文”的承诺；对零基础科研，本仓库保留人工审核并明确不自动批准数据、实验和结论；
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)将总览与逐课内容分离，每课仍给目标、活动和作业，说明下沉细节时首页不能只留下模糊的“查看更多”，还要保留可验收的下一步。
- **适用边界**：缩短 README 不等于删除关键规范，也不能把所有内容拆成大量孤立页面。读者选择起点所需的定位、分级、路线、阶段地图和资源导航应保留在首页；执行细节应集中进入少量稳定文档，并维持从阶段到产物的直接链接。自动研究系统的检查点可用来设计人工门控，但其生成文本、代码、实验和引用仍需独立核验。
- **采取行动**：新增 `docs/CORE_RESEARCH_WORKFLOW.md`，以九个阶段、四个质量门控和一次项目最短闭环集中保存执行规则；将主 README 的近 600 行详细流程替换为两列阶段地图、停止检查点和五个按需文档入口，行数从 1142 降至约 580；修正 baseline 筛选锚点；在贡献指南中增加“首页负责选择、docs 负责执行”的维护规则，同时要求首页保留下一动作和通过条件。
- **状态**：已完成。

## 2026-08-09：资源导航与动态信息审计

### I-023：任务导航、高 Star 表和推荐组合重复，热度快照被误放在决策路径中

- **当前问题**：首页在 L0–L3 分流后，又用“工具与入口导航”“可参考的 GitHub 入门资源”和四个“推荐组合”重复组织同一批课程与项目。读者可能在能力等级、任务类别、Star 顺序和组合编号之间反复选择。2026-08-07 的 Star 快照还需要持续更新，却不改变资源是否适合当前阻塞，维护成本高于决策价值。
- **经验对照**：
  - 知乎关于[计算机公开课资源](https://www.zhihu.com/question/38335108/answer/1993372768251687650)和[教程收藏负担](https://www.zhihu.com/tardis/landing/yidian/ans/2046292839185606022)共同反映“资源足够但不会选”的问题，因此再增加一种排序维度不会自然降低门槛；经验帖只用来识别选择困难，不用于判断项目质量；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)以当前任务和当天产物组织行动，而不是要求先比较所有课程热度；访问可能需要登录，具体日程不作为本仓库统一要求。
- **规范与项目对照**：
  - [Awesome Machine Learning Resources](https://github.com/ZhiningLiu1998/awesome-machine-learning-resources)按主题汇总大量二级目录，并单独标记长期不活跃项目，适合做“发现候选”的目录；其规模也说明聚合目录不宜直接承担零基础主路线；
  - [nature-skills](https://github.com/Yuan1z0825/nature-skills)明确将 README 定位为帮助用户快速判断适配任务、输入、输出与边界的入口，把复杂规则、教程和索引下沉；本仓库吸收这种职责分离，不吸收其特定技能安装方式；
  - [Learning Research](https://github.com/pengsida/learning_research)用阶段目标和实践任务组织路线，而不是按外部项目热度给出学习顺序，也支持以当前能力和产物作为选择依据。
- **适用边界**：高 Star 可以帮助发现经过广泛传播的候选，不能单独证明正确性、维护状态、许可证兼容或适合零基础。资源目录仍应保留低 Star 但能解决明确问题的官方指南。首页可以出现同一资源一次，详细目录可以再次说明边界，但不能同时维护多套互相竞争的学习顺序。
- **采取行动**：新增 `docs/GITHUB_RESOURCE_CATALOG.md`，把课程和项目按 L0–L3、工具基础、机器学习、论文阅读、实验工程和 AI 辅助分类，并为每项保留建议吸收内容与使用边界；增加六问吸收协议和聚合目录的发现边界；从首页删除 Star 快照表与四个重复推荐组合，只保留“按当前任务选择一个入口”的两列导航；同步更新贡献规范，禁止用 Star 决定排序或推荐等级。
- **状态**：已完成。

## 2026-08-09：起步工程复杂度审计

### I-024：首页展示全部模板和完整项目树，容易让 L0–L1 把“先搭工程”误认为科研起点

- **当前问题**：虽然首页已经提供最小模板包，后部仍完整列出 16 张模板和包含 `papers/`、`analysis/`、`artifacts/`、`submissions/` 等目录的成熟项目树。零基础读者可能在没有真实数据、实验或投稿任务时先复制全部表单和空目录，随后维护两个索引和大量猜测字段；这与“只启用当前阶段”的原则冲突。
- **经验对照**：
  - 知乎关于[教程收藏负担](https://www.zhihu.com/tardis/landing/yidian/ans/2046292839185606022)反映出准备材料不断增加会推迟真正动手；本仓库只吸收“起步动作必须有限”的观察，不采用其中的课程推荐；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)用 demo、检查和总结构成单日闭环，[第一次复现](https://www.xiaohongshu.com/explore/67cfb412000000002a00c7e8)也把注意力放在跑通与定位差异。这些笔记可能要求登录，只用于确认新手先需要可运行闭环，而非完整研究工程。
- **规范与项目对照**：
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)强调课程项目从小到复杂，并允许按部分使用；每课有活动、检查和作业，而不是先要求学习者建立全课程级工程；
  - [Made With ML：Moving from Notebooks to Scripts](https://madewithml.com/courses/mlops/scripting/)把从 Notebook 迁移到脚本和目录组织作为后续演进，说明结构应随复用、测试和运行需求增长；
  - [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science)提供成熟数据科学项目结构，适合在数据处理、模型、报告和协作增多时参考，但完整模板不是第一个 CPU 实验的必要条件。
- **适用边界**：最小骨架不能成为长期混乱的理由。进入真实 baseline 后仍需保存环境、数据版本、配置、日志和结果；出现多个数据版本、运行、图表、投稿或协作者时应及时升级。已有成熟且可复现的实验室结构无需为了本仓库重排，只补充缺失索引与证据。
- **采取行动**：新增 `docs/PROJECT_STRUCTURE.md`，提供七项 L0–L1 最小骨架、七类升级触发事件、L2–L3 完整参考树和目录设计检查；首页用最小骨架替换完整工程树，并把 16 项模板总表缩为“最小包—模板目录—已填写演练”三个入口；同步更新贡献规范，要求模板与目录由真实事件触发，不创建空目录或重复台账。
- **状态**：已完成。

## 2026-08-09：学习节奏与阶段决策审计

### I-025：八周虽被声明为参考，周次编号仍暗示按日历自动升级

- **当前问题**：路线说明允许延长，但八行都以“第 1 周”到“第 8 周”命名，后文也用“第 6 周仍未复现成功”判断进度。基础差异、课程考试、算力等待和 baseline 难度会显著改变耗时；读者可能为了跟上表格而跳过验收，或把合理延期误解为个人失败。周会模板也只有“采用、放弃、推迟”，无法记录暂停、停留和求助后的恢复条件。
- **经验对照**：
  - 知乎关于[从小白到论文复现](https://www.zhihu.com/question/659628177/answer/2002333417153513369)把打基础描述为可能持续数月的渐进过程，并强调先复现再创新；该回答带有培训经验和课程推荐，本仓库只吸收“个体节奏差异与阶段先后”的观察；
  - [入门 MLLM Day 4](https://www.xiaohongshu.com/explore/6a3cd57f0000000011019ccd)把一天绑定到 demo、检查和总结产物，支持用完成证据而非日期评价进度；其日程仅是个人记录，不能外推为统一工期。
- **规范与项目对照**：
  - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)虽以 12 周组织课程，但明确允许整体或部分使用，项目从小到复杂，并用活动、知识检查和作业承载学习结果；
  - [Learning Research](https://github.com/pengsida/learning_research)把成长分为广度学习、深度参与和独立项目，并说明独立研究难以有固定路线、依赖实践与交流；其 3D Vision 课程安排不能直接作为通用工期；
  - [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)的阶段检查点与 `PROCEED / REFINE / PIVOT` 表明流水线应按产物和决策推进。本仓库只借鉴状态机结构，关键科研判断仍由人完成。
- **适用边界**：时间盒和目标日期仍有价值，可用于资源安排、导师沟通和防止无限拖延；问题在于日期不能替代通过条件。课程、资助和投稿有硬截止时，应调整研究范围、证据强度和备选方案，不能删除必要核验或伪造完成状态。
- **采取行动**：把“可调节的八周路线”改为 M1–M8 八个能力里程碑，允许每项按一周估时但只按产物升级；增加 `PASS / STAY / PAUSE / PIVOT / ASK` 五种复盘状态及下一步定义；把“第 6 周失败”改成 M6 门控；同步更新周会模板，记录当前里程碑、唯一实际状态、恢复条件、备选路径和求助对象。
- **状态**：已完成。

## 下一轮优先审计

- 等待作者确认许可证、引用署名和首个版本号，再完成 `LICENSE`、`CITATION.cff` 与首个 GitHub Release。
- 审计首次访问路径是否缺少“完成 M1–M3 后如何选择具体 AI 研究方向”的决策树，避免新手在 CV、NLP、多模态、推荐、图学习等方向列表中再次失去起点。
