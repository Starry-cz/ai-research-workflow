# baseline 复现到首次改进审计（2026-08-09）

## 审计问题

仓库已经要求先复现 baseline、再做单变量改动，但运行前检查仍只有“baseline 已复现或差异已解释”。该表述没有回答：

- 论文报告值、本地官方代码结果和候选改动结果是否被区分；
- “差异已解释”需要什么证据，残余差距是否会与改动混杂；
- pilot / 小数据上涨后，何时能够升级到代表性规模；
- 无法复现原文时应继续诊断、只作有限对照，还是更换 baseline；
- AI 写出的改动怎样先验证实现，再评价 idea。

## 经验材料中的真实阻塞

| 经验材料 | 暴露的问题与本仓库处理 |
| --- | --- |
| [什么时候对 baseline 进行改进](https://www.xiaohongshu.com/explore/6a27a897000000001702e3d0) | 正文提出先测试官方权重、完成训练并理解数据流，再做单模块改动；评论集中询问“本地改进但仍低于论文结果”“小数据有效、full data 失效”“issue 中多人无法复现”“提升一点是否算有效”。本仓库吸收这些问题，不把评论中的单句判断当通用准则；页面可能需要登录。 |
| [把 idea 变成可靠的代码的工作流](https://www.xiaohongshu.com/explore/6a1a82e400000000380345ea) | 正文强调理解、规划、最小实现和逐步验证；评论反映“AI 找的创新点效果差”“代码跑通但不理解公式”“结果不涨时不知是代码还是 idea”。本仓库采用可审计 diff 和分层验证，但对于会改变方法的公式与假设，要求理解变量、shape、优化作用和代码映射；页面可能需要登录。 |
| [从小白到读懂并复现机器学习论文](https://www.zhihu.com/question/659628177/answer/2002333417153513369) | 个人经验采用“跑通 baseline 后做简单改进”的学习顺序。它适合建立实践感，但“跑通”不足以支持科研比较；本仓库增加稳定性、差距和规模升级门。 |

## GitHub 与官方依据

| 依据 | 可迁移规则与边界 |
| --- | --- |
| [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook) | 使用简单、低成本的初始配置；区分科学超参数与干扰超参数；让比较双方获得公平调参机会；查看训练曲线和搜索边界；保存 study、配置、运行数、最佳 checkpoint 与复现命令。其建议主要面向监督或相近深度学习任务，不是所有研究类型的固定配方。 |
| [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code) | 依赖、训练代码、评价代码、预训练权重和精确结果命令是判断复现入口是否完整的核心证据；完整性不保证结果真实或适合当前设备。 |
| [PyTorch Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html) | 相同 seed 也不保证跨版本、平台、CPU / GPU 完全一致；确定性设置可能降低性能。复现容差必须结合锁定环境和任务波动，而不是要求任意设备逐位相同。 |
| [Lightning-Hydra-Template](https://github.com/ashleve/lightning-hydra-template) | 配置化实验、独立输出目录、多 seed、checkpoint 恢复和冒烟测试可作为工程参考；其 README 也明确通用测试多为“不报错”检查，不能证明论文结果成立。 |
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) | 主要实验需要说明训练设置、数据、超参数选择和不确定性。投稿清单定义报告责任，不会替代当前项目的 baseline 验收。 |

## 新门控结论

进入方法改进前必须分开保存“论文目标值—本地锁定 baseline—候选方法”，并从以下四种状态中选择：

1. `READY_FOR_CHANGE`：本地 baseline 稳定，达到容差或残余差距已被限定且不破坏比较；
2. `REPRODUCTION_ONLY`：差距仍可能来自实现、数据、评价或选择规则，只继续诊断；
3. `COMPARATOR_ONLY`：只允许当前协议内的有限对照，不得声称复现或超过论文；
4. `REPLACE_BASELINE`：关键入口不可得、差距不可控制或资源不匹配，切换备选。

同时新增 pilot 到代表性规模的升级检查。小数据上涨、单 seed 最优值和“来自新顶会的模块”都不能单独成为改进证据或新颖性依据。

## 落地文件

- [从 baseline 复现到首次改进](../docs/BASELINE_STABILIZATION_GATE.md)；
- [首篇 baseline 准入卡](../templates/11-first-baseline-gate.md)；
- [论文复现规划](../templates/03-reproduction-plan.md)；
- [实验卡](../templates/04-experiment-card.md)；
- [核心科研工作流](../docs/CORE_RESEARCH_WORKFLOW.md)。
