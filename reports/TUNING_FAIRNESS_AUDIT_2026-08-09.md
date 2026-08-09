# 调参公平性与多重尝试审计（2026-08-09）

## 审计目标

检查仓库是否能阻止两类常见假提升：候选方法获得更多调参机会而 baseline 只使用默认配置；尝试许多组合后只报告最好一次，却不披露搜索规模、失败和选择过程。

## 发现

审计前，实验卡只有“调参预算与各组公平性”一个空白字段，评价协议只有一行“超参数选择规则”。这些字段能提醒读者，却不能回答以下问题：

- 什么是本轮科学变量，什么只是需要被优化掉的干扰超参数；
- baseline 和候选是否需要相同 trial 数，或如何解释不同参数空间；
- pilot、短训练、失败、剪枝和人工看曲线后的调整是否计入尝试；
- 何时停止探索、冻结配置并进入确认性实验；
- 看过测试结果后继续调参，证据应如何降级；
- 多个 trial 中选出的最好验证结果为什么不能直接作为方法结论。

## 经验问题对照

- [什么时候对 baseline 进行改进](https://www.xiaohongshu.com/explore/6a27a897000000001702e3d0)及评论出现“baseline 参数要不要调”“小数据有效但完整数据失效”“本地改进仍低于论文结果”等具体困惑。它证明新手会在复现、调参与方法改进之间混淆；个人回复不作为统一技术规则。
- [把 idea 变成可靠的代码的工作流](https://www.xiaohongshu.com/explore/6a1a82e400000000380345ea)强调最小修改和逐步验证，评论反映反复改代码后难以判断收益来自想法还是实现。它支持保留每轮改动与验证轨迹，但不能规定公平预算。
- 知乎文章[点积 vs. MLP：推荐模型到底用哪个更好？](https://www.zhihu.com/tardis/zm/art/143161957)通过具体论文比较展示：即使实验设置表面相同，不同参数化、搜索范围和比较口径仍会改变结论。它作为案例用于发现“设置相同不等于比较公平”，不作为跨任务调参配方。
- 知乎关于[是否报告最高准确率](https://www.zhihu.com/en/answer/3249240394)和[如何选择最终结果](https://www.zhihu.com/en/answer/2229914309)的讨论说明读者确实会困惑于 best run、平均值和结果选择；最终规则仍需由预先冻结的评价协议与领域规范确定。

## 规范与项目对照

- [Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook)把研究对象定义为科学超参数，把为公平比较需要优化的设置定义为干扰超参数；study 由搜索空间、trial 数与搜索算法组成。它明确要求在有限预算下平衡科学变量覆盖、搜索范围和采样密度，并检查边界、失败 trial 和训练曲线。
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)要求披露训练细节、超参数选择、计算资源和实验不确定性，支持把调参过程作为实验方法的一部分，而非隐藏准备工作。
- [PyTorch Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html)说明跨版本、平台与设备不能保证完全一致，且确定性可能降低性能；因此公平比较需要固定环境和随机性边界，但不能承诺逐位复现。
- [Releasing Research Code](https://github.com/paperswithcode/releasing-research-code)要求提供依赖、训练、评价、预训练模型和精确结果命令；[Lightning-Hydra-Template](https://github.com/ashleve/lightning-hydra-template)展示配置化运行、独立日志、多 seed 与 sweep。两者提供工程记录方式，但不能替代研究者设计公平 study。

## 结论与修改

新增 `docs/FAIR_TUNING_BUDGET.md`，把公平调参拆成变量分类、三类预算、三种比较方案、trial 台账、验证选择、pilot / 剪枝规则、确认性准入和最低披露。同步升级实验卡、评价协议卡与结果—主张审计卡，并把指南接入首页、核心工作流和指南索引。

本次没有增加新的自动调参工具条目。当前缺口是协议而非软件；过早增加 Optuna、Weights & Biases 或其他平台，会让新手误以为启动 sweep 就等于完成公平比较。

## 适用边界

本审计面向需要训练、验证和比较的 AI / ML 实验。理论工作、纯定性研究或不可重复的昂贵单次实验需要改写预算形式。公平不等于所有方法完全相同的参数空间或精确 trial 数；方法特有参数可以不同，但机会、理由、成本和限制必须透明。任何固定的 trial 数都不适用于所有任务。

