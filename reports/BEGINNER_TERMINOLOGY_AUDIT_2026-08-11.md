# 零基础默认路径术语审计（2026-08-11）

## 审计结论

仓库已经把第一次行动缩短为“检查工具—运行一次—验收四项产物”，但首屏、L0 和演练页仍在定义前反复使用 `commit`、`origin`、`seed`、`run_id`、`baseline`、`PASS` 等词。对熟悉工程与机器学习的读者，这些词能压缩表达；对目标读者，它们会把“执行命令”变成“先搜索黑话”。原仓库没有统一术语入口，搜索到的个人解释又可能脱离当前任务或过度概括。

当前版本采用两层解释：少量、低频词在第一次出现处用通俗中文解释；跨页面重复出现的词进入[零基础默认路径术语速查](../docs/BEGINNER_GLOSSARY.md)。每个条目同时说明通俗含义、现在要做什么和不能推出什么，并链接原始定义来源。

## 经验帖对照

- 小红书笔记[研0 暑期科研词汇扫盲！开学再也不怕导师问](https://www.xiaohongshu.com/explore/68a42843000000001d001383)以“研 0”和“词汇扫盲”为标题组织内容，说明术语理解本身是新入学读者主动寻找的帮助类型。它主要通过图片呈现，当前审计只使用可见标题确认需求，不据此复述或采纳具体定义。
- 小红书笔记[老师默认你知道的科研黑话！科研名词扫盲！](https://www.xiaohongshu.com/explore/6880ab74000000000d025d60)尝试解释论文、检索系统、期刊分区、DOI 和开放获取等词，同时把若干复杂制度压缩为宽泛经验判断。该笔记只支持“默认知识会阻碍新手”和“个人词汇帖需要交叉核验”，不作为出版、评价或开放获取规则来源。
- 知乎问题[机器学习中的 baseline 是什么](https://www.zhihu.com/en/answer/1163052504)直接由初学者询问 baseline 含义，回答也随课程作业、论文比较等场景给出不同例子，说明一个中文翻译不足以确定研究中的比较对象。它是个人问答，只用于识别上下文缺失问题。
- 知乎文章[Random Seed](https://www.zhihu.com/en/article/514821697)讨论何时固定随机种子，反映 seed 不只是“填一个数字”，还涉及复现与实验目的。文章观点不替代框架文档、具体算法或硬件确定性说明。

## 正式规范与 GitHub 项目对照

- [Google Technical Writing：Words](https://developers.google.com/tech-writing/one/words)要求定义或链接陌生术语，并在术语较多时建立 glossary；它同时强调同一概念应保持一致命名。
- [GitHub Docs 内容模板](https://docs.github.com/en/contributing/writing-for-github-docs/templates)给出实用分流：反复使用的技术词进入 key terms / glossary，低频词在上下文解释，并要求使用简单语言、避免未解释的术语和缩写。本仓库将其迁移为“跨页面高频词进速查，少量词原地解释”。
- [Microsoft LangChain4j for Beginners Glossary](https://github.com/microsoft/LangChain4j-for-Beginners/blob/main/docs/GLOSSARY.md)把课程词汇按核心概念、AI/ML、RAG、Agent 和开发测试分组，并回链相应模块，证明面向新手的 GitHub 教程可以提供集中速查而不把全部定义塞进首页。本仓库吸收“按任务分组和回到教程”，不收录与默认路径无关的 LLM 专项词。
- Git 术语以 [GitHub Glossary](https://docs.github.com/en/get-started/learning-about-github/github-glossary)和 [Pro Git](https://git-scm.com/book/en/v2)为基础；Python 环境以 [`venv`](https://docs.python.org/3/library/venv.html)和 [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)为基础。
- 实验记录关系参考 [MLflow Tracking Concepts](https://mlflow.org/docs/latest/ml/tracking/)；seed 的可重复性边界参考 [scikit-learn `random_state`](https://scikit-learn.org/stable/glossary.html#term-random_state)；epoch 与 loss 参考 [PyTorch 优化教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)。引用这些项目只用于统一概念，不要求新手安装对应平台或框架。

## 采取的修改

- 新增默认路径术语速查，按“路线状态—Git—Python 环境—一次实验”组织，而不是按学科堆叠黑话；
- 每项固定包含通俗含义、当前动作和不可推出的结论，防止“记住词义但继续误操作”；
- 首页在目录前提供术语出口，并把首次出现的 baseline、commit 与 PASS 补成中英对应和行为解释；
- L0、首次演练和指南索引提供按需链接，不要求读者先完整阅读术语页；
- 贡献规范要求低频词原地解释、高频词才进入术语表，定义必须来自官方文档、原始项目或正式规范；
- 仓库质量脚本检查术语文件、首页可发现性、核心条目、逐项行动与结论边界，防止后续退化为只有一句翻译的词表。

## 适用边界

- 这份速查只覆盖默认路径中的操作词，不覆盖所有 AI 子领域、数学符号、论文写作、期刊分区或投稿制度；
- 词条是本仓库上下文中的操作性解释，不替代 Git、Python、框架、论文、数据集、目标会议或团队的完整规范；
- glossary 能降低查找成本，但不能证明陌生读者实际理解。是否能在不提示情况下把词对应到命令和文件，仍需真人可用性观察；
- 不为追求“完整”收录尚未在主路径出现的流行术语，也不把频繁变化的模型、产品规格和价格写入稳定词条；
- 中文翻译和类比不能替代技术边界，例如 commit 不是发布、固定 seed 不是完全确定、PASS 不是研究结论、baseline 也不是固定等于某类模型。

## 验收标准

- 新读者在首页目录之前能够找到术语入口；
- 默认路径的高频 Git、Python 与实验词都有通俗含义、当前动作和不可推出项；
- 术语页所有外部定义指向官方文档或原始项目，经验帖只保留在问题审计中；
- README 不新增宽表，术语页不成为默认路径的必读前置；
- 自动检查能拒绝删除核心词、行动项、边界项或首页入口。

当前状态：26 个术语条目、按需入口与自动回归规则已完成。仓库质量检查覆盖 92 份 Markdown、术语可发现性、两类索引和 51 个工具条目并通过；负向测试删除一个条目的“现在要做什么”后被检查脚本准确拒绝，恢复后重新通过。首次单配置、三组公平比较、知识检索、无命中交接和特殊路径回归均通过。真人理解仍为待观察项，不能宣称“已经通过零基础用户验证”。
