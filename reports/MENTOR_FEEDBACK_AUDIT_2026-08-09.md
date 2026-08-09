# 导师与组会反馈闭环审计（2026-08-09）

## 当前问题

README 和每周复盘已经要求记录反馈、责任人、截止与下一步，但“收到建议”到“研究状态改变”之间仍缺少原始语义、目标对象、类型、是否事后、处理决定、验收证据和关闭 / 重开条件。新手可能把导师一句“再看看这个问题”直接扩成大实验，也可能每周重复写同一建议，却无法证明它已落实、合理延期或有证据地不采纳。

## 经验帖对照

| 经验材料 | 暴露的问题与本仓库吸收的内容 |
| --- | --- |
| [研究生的实验记录该怎么记，以结果为导向](https://www.xiaohongshu.com/explore/696fa4fb000000001a02bc8e) | 按天记录容易碎片化，结果和决定未及时聚合，汇报前才集中整理。本仓库把关键反馈归到项目问题与证据，不按会议次数堆流水账。页面可能需要登录。 |
| [科研习惯分享（三）：一次实验我写 3 份记录](https://www.xiaohongshu.com/explore/6612bab8000000001b013f7e) | 随手记录会让细节事后不清，个人记录与组会表达又面向不同对象。本仓库采用唯一来源与反馈 ID 链接，不要求维护三份同义笔记。页面可能需要登录。 |
| [作为研究生新手，应该如何和导师沟通](https://zhuanlan.zhihu.com/p/2033116043812532613) | 文章指出学生常讲过程，而导师更需要问题、证据和可选决策；建议会前准备障碍和希望获得的反馈。它由科研服务机构发布，本仓库只吸收结构化问题与选项，不采用固定话术和时间安排。 |
| [你们实验室的例会制度是怎样的](https://www.zhihu.com/question/322279340) | 回答反映有些组会沦为轮流汇报、比较进度，未产生可执行研究建议。讨论是匿名个体经验，只用于确认“开会频率不等于反馈有效”，不用于评价任何课题组。 |

## 规范与项目对照

| 规范或项目 | 对本仓库的约束 |
| --- | --- |
| [Learning Research](https://github.com/pengsida/learning_research) | 通过每周 meet PPT、实验记录、失败分析和真实项目训练研究能力；作者明确经验来自特定实验室，不能把周频率和 3D Vision 路线外推为通则。 |
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 把科研评价、写作和审查经验结构化为指南与 AI skills，并强调万能 Prompt 不能替代判断力；本仓库吸收“建议结构化与证据门控”，不把 AI 输出记作导师已确认。 |
| [Building and sustaining mentor interactions as a mentee](https://pmc.ncbi.nlm.nih.gov/articles/PMC8490489/) | 导师与学生应共同确认目标、议程、反馈方式和下一步，并用行动项提升会议效率。其主要语境为早期职业医学研究者，具体频率需因团队而定。 |
| [The Science of Effective Mentorship in STEMM](https://www.ncbi.nlm.nih.gov/books/NBK552762/) | 书面目标、行动和里程碑需要定期检查；仅采用表格或 compact 不保证关系和结果有效。 |
| [Ten Simple Rules for Getting Involved in Your Scientific Community](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002232) | 行动项应具体，并给每项任务一个负责人和截止；该文面向科研社区协作，不直接规定导师权力关系。 |
| [GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues) | assignee 明确负责人，分支 / PR 可与 Issue 关联并在合并后关闭；工具状态只能证明工程动作，科研问题仍需证据验收。 |

## 适用边界

本指南处理科研任务反馈，不试图标准化所有师生关系，也不适用于用流程掩盖骚扰、歧视、署名争议、伦理违规或权力滥用；这些问题应使用学校、伦理或申诉渠道。导师拥有最终项目决策权的范围因课题、资助和实验室而异，学生不能用模板单方面改变权限。反馈闭环也不能把探索性建议伪装成预注册协议，或用“导师要求”绕过数据、伦理和评价门控。

## 采取行动

1. 新增[导师与组会反馈闭环](../docs/MENTOR_FEEDBACK_LOOP.md)，把关键建议转换为“捕获—确认—决定—行动—证据—再验收—关闭 / 重开”；
2. 定义七类反馈、六种处理决定和六种最终状态，并单独处理事后协议变化与多方冲突；
3. 升级每周复盘、原子任务卡、研究简报和 README，使接受项必须有负责人、产物、验收与关闭证据；
4. 新增[已填写反馈闭环示例](../examples/first-workflow-drill/feedback-loop.md)，用真实冷启动审计和主张收缩演示 `CLOSED_EVIDENCE / CLOSED_SCOPE`；
5. 持续改进记录新增 I-041，并将下一轮重点转向零基础读者能否在首次导师任务中正确识别权限、非目标和升级路径。

## 本地验证

- 示例链接：反馈示例中的运行交接审计、交接卡、主张审计和两份指南均通过相对链接与锚点检查；
- 仓库质量：已检查 59 个 Markdown 文件，代码块、指南 / 模板索引和 51 个工具条目全部通过；
- 首页约束：README 共 488 行，仍低于 600 行限制，根 README 表格继续保持最多两列；
- Git 差异：`git diff --check` 通过，没有空白错误。

## 状态

文档、示例和本地质量检查已完成；线上状态以对应提交的 GitHub Actions 为准。
