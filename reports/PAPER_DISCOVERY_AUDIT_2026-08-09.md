# 论文发现平台与原文回溯审计（2026-08-09）

## 审计目的

本报告检查仓库中的论文入口能否帮助零基础用户完成“发现候选—确认书目—定位原文版本—核验官方代码”，并据此确定各平台在工作流中的职责。

检查采用公开首页、当前可见检索界面、官方帮助或 GitHub README。它不是覆盖率基准测试，也不以一次页面结果推断长期完整性。页面数量、功能和维护状态会变化，使用时应再次核验。

## 主要发现

| 入口 | 观察、建议角色与边界 |
| --- | --- |
| [Google Scholar](https://scholar.google.com/) | 支持相关性 / 日期排序、`Cited by`、相关论文和其他版本，适合广泛发现与引文追踪。官方帮助同时提示具体来源覆盖不保证持续完整，记录更新可能滞后；不能把结果数当作查全率。 |
| [DBLP](https://dblp.org/) | 提供计算机科学论文、作者和 venue 的书目元数据以及电子版链接，适合建立书目主记录；它不是全文证据库，不能替代原文、录用状态或实验核验。 |
| [arXiv](https://arxiv.org/) | 适合获取预印本正文与版本历史。官方说明每个版本永久保留，替换会增加版本号，标题、作者和正文可能变化；复现和精确引用应记录版本号与访问日期。 |
| [OpenReview](https://openreview.net/) | 对采用该平台且公开相应内容的 venue，可核对投稿版本、评审、回复和决定；不同 venue 的公开范围不同，不代表全部评审事实。 |
| [Cool Papers](https://papers.cool/) | 页面声明同步 arXiv，并对部分会议论文进行人工收录；可见 venue 集合有限且接受遗漏反馈。适合发现、趋势和 venue 浏览，不承担完整覆盖或正式版本判断。 |
| [CosmosPaper](https://www.cosmospapers.com/) | 检查时页面加载后显示 54,599 条记录，结果可直达 DOI；[公开仓库](https://github.com/ulairii/cosmospaper)声明覆盖 15+ 会议、2022–2026，并提供语义搜索、趋势和自带 API key 的 AI 功能。适合部分 AI / ML / CV / 图形 / 安全 venue 的发现，不外推到全部 AI / CS；摘要与 BibTeX 回 DOI 或原文核验。 |
| [Paper Copilot](https://papercopilot.com/) | 页面说明数据来自 OpenReview、官网与社区，包含多个 AI 方向和不同年份的会议入口；覆盖跨度不均。适合论文发现和公开评审上下文，论文数、录用和评审状态回官方来源核验。 |
| [CV Paper Portal](https://github.com/hongsong-wang/CV_Paper_Portal) | README 明确列出 CVPR、ICCV、ECCV 等 venue 与年份并持续更新，也说明大量摘要来自 arXiv。适合视觉方向的 venue 浏览；摘要、版本和完整覆盖需要回到原文与会议页。 |
| [AI arXiv Paper Portal](https://github.com/hongsong-wang/AI_arXiv_Portal) | 以维护者选择的主题词组织近期 arXiv 论文，并通过 issue 扩展主题。适合主题跟踪和生成种子，不代表全部 AI 主题或正式发表版本。 |
| [AI Conferences Info](https://github.com/george-gca/ai_conferences_info) | 仓库提供部分 venue / 年份的标题、摘要、作者和 URL 字段；原演示检索站当前已失效。适合使用仓库数据做有限筛选，不应继续宣传已失效的在线检索能力。 |
| [Hugging Face Trending Papers](https://huggingface.co/papers/trending) | 适合观察社区近期关注并发现候选。趋势不是任务榜单、覆盖率或质量结论，代码和数据仍需回官方项目核验。 |

## GitHub 工作流项目对照

本轮另外检查了高关注度项目中可迁移的文献工作流。Star 只用于发现候选，不作为质量、正确性或新手适配性的判断依据。

| 项目 | 可吸收内容与不采用部分 |
| --- | --- |
| [Hermes Agent](https://github.com/nousresearch/hermes-agent/blob/main/skills/research/research-paper-writing/SKILL.md) | 吸收“先建立种子论文，再做结构化搜索、引文扩展和引用核验”的顺序。自动生成研究文本不替代原文阅读、实验或作者判断。 |
| [DeerFlow systematic-literature-review skill](https://github.com/bytedance/deer-flow/blob/main/skills/public/systematic-literature-review/SKILL.md) | 吸收检索、筛选、综合和引用输出分阶段记录的设计。其系统综述能力不等于本仓库的小型代表性文献集合，也不允许据此声称查全。 |
| [ASReview](https://github.com/asreview/asreview) | 吸收导入、去重、保存筛选决定和可审计流程。首轮只有数篇候选时无需引入主动学习筛选系统。 |
| [Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 大规模技能库展示了分任务封装检索和分析方法的可能性，但范围偏经验社会科学且许可证需要单独判断，不作为 AI 零基础的默认依赖。 |

## 经验内容对照

- [计算机科研新手快速入门](https://www.xiaohongshu.com/explore/6a55f71400000000170282b1)把近期、开源、框架相对清楚且算力可承受的论文作为第一次深入对象，并强调先测试官方模型再进入训练。这里只吸收“缩小首篇候选范围”的经验，不采用其商业产品推荐，也不把个人路径写成通用规律；
- [大二科研经验和工具使用详细分享（文献篇）](https://www.xiaohongshu.com/explore/68cbd6850000000012021069)呈现了从导师给定论文转向关键词、venue、引文追踪和文献管理的过程；评论中的关键词与阅读范围问题说明平台清单必须配查询和停止协议；
- [科研入门指南：找文献篇](https://www.zhihu.com/tardis/bd/art/660258901)使用关键词、参考文献和会议 / 期刊扫描组织检索；
- [文献检索的五种常用方式](https://www.zhihu.com/tardis/bd/art/5273768340)进一步展示了种子论文和正反向引文追踪。经验文章用于识别新手操作问题，具体元数据和版本规则仍以官方来源为准。

## 结论与落地

没有一个平台能够同时可靠完成四层职责。原仓库把多个入口并列展示，虽然提供了选择，却仍可能让新手把聚合摘要当成论文证据，或为了“覆盖”重复搜索所有网站。

本轮采取以下行动：

1. 新增[零基础论文发现与原文回溯](../docs/PAPER_DISCOVERY_FIRST_PASS.md)，把首轮搜索限制为一个最小来源组合；
2. 扩展[文献检索账本](../templates/07-literature-search-log.md)，分开记录发现 URL、书目身份、原文版本和官方代码；
3. 为 `tools.yml` 的论文入口增加 `research_role`，机器目录可按来源职责筛选；
4. 更新 CosmosPaper 的规范仓库、实际范围与 BYOK 边界；
5. 首页只提供任务入口，不重复展开平台清单。

后续抽查聚合平台时，需要固定查询、日期、venue / 年份范围、可见结果、抽样原文和第二来源；未完成这样的测试前，不给出“覆盖度评分”或“最全”结论。
