# 检索无命中后的求助、验证与回流记录

> 本页是教学项目内的已填写记录。命令和运行结果由仓库脚本实际校验；“回复候选”明确标记为 `TEACHING_RESPONSE_FIXTURE`，用于练习回复后的验证，不冒充真实导师、同伴或维护者答复。

## 1. 原始问题

- 当前任务：运行调试配置，并把结果写入一个新目录；
- 预期：生成 `config.snapshot.json`、`environment.json`、`metrics.json` 和 `run.log`；
- 实际：训练开始前非零退出，没有创建输出目录；
- 第一个关键报错：`FileNotFoundError: [Errno 2] No such file or directory: 'configs/does-not-exist.json'`；
- 完整命令：

```bash
python train.py --config configs/does-not-exist.json --output-dir results/no-match-observation
```

- 当前身份：仓库内公开教学脚本；当前 commit；合成数据；
- 当前权限：允许只读检查、本地运行和新建临时输出；不允许删除记录目录、覆盖旧证据或把问题直接定性为上游缺陷。

## 2. 自助检索轨迹

- Q0：`配置文件找不到`、`训练没开始就退出`；
- Q1：`FileNotFoundError configs/does-not-exist.json`；
- Q2：`FileNotFoundError load_config --config`；
- 打开的候选：`knowledge-index.md`、`train.py`、本演练 README 的常见失败段落和 `python train.py --help`；
- 正式知识索引结果：`NO_MATCH`。索引只有非空输出目录的 `FileExistsError` 条目，没有当前 `FileNotFoundError` 的正式条目；
- 已排除：`KNOW-DEMO-001` 的阶段、异常类型和组件均不匹配，不能把“换输出目录”当作当前修复；
- 负面发现：当前 CLI 没有生成默认配置的参数，`--config` 为必填；失败发生在 `load_config`，早于输出目录准备。

`NO_MATCH` 只表示当前索引没有可直接复用的正式条目，不表示问题没有原因，也不表示必须新建 Issue 或知识卡。

## 3. 无死路交接包

- 当前搜索结果：`NO_MATCH`；
- 已完成的最小观察：核对 CLI、配置目录、异常位置和正式索引；
- 下一位问题所有者：本地项目使用支持者，例如当前项目同伴、教学负责人或导师；
- 暂不选择的渠道：第三方上游 Issue。当前证据还没有越过本仓库的命令与文件路径；
- 唯一希望对方判断的问题：在当前 commit 中，`--config` 是否必须指向已经存在的 JSON 文件，还是脚本应在路径不存在时生成默认配置？
- 可安全分享：命令、异常类型、相对路径、当前 commit、公开脚本和合成数据；
- 不分享：个人绝对路径、账号信息，以及任何真实项目的受限数据或未公开配置；
- 如果仍无法区分：请对方只指出下一项有区分度的只读检查，不请求其直接修改、删除或覆盖文件。

这份交接包应附在原调试记录中，而不是重新发送一句“跑不起来”。原始查询、已开候选和负面发现随问题一起移动。

## 4. 回复只是候选

- 回复来源：`TEACHING_RESPONSE_FIXTURE`，不是实际人员回复；
- 回复内容：先查看 `configs/` 中是否存在目标文件；当前脚本不会自动生成配置，应改用仓库内已有配置后在新临时目录重跑；
- 回复初始状态：`ANSWER_CANDIDATE`；
- 需要核验的前提：目标配置确实存在，脚本成功读取它，且运行不触碰旧结果；
- 禁止动作：不创建伪造配置、不删除已有结果、不添加未经设计的兜底行为。

## 5. 本地验证

先确认 `configs/debug.json` 存在，再运行：

```bash
python train.py --config configs/debug.json --output-dir <新的临时目录>
```

实际校验结果：命令正常退出，新目录包含四个预期产物。由此只能确认“当前失败来自不存在的配置路径，已有配置可正常运行”适用于本次教学事件；不能推出所有 `FileNotFoundError` 都是用户输入问题。

## 6. 关闭与知识回流

- 当前路由状态：`SELF_RESOLVED_NO_ARTICLE`；
- 回复验证状态：`VERIFIED_WITHIN_SCOPE`；
- 上游动作：不提交 Issue，不创建 PR；
- 知识回流：`IMPROVE_FINDABILITY`，在演练 README 的常见失败中补充“配置文件不存在 / 路径拼错”及只读检查；
- 不新建正式知识条目的理由：问题由一次直接的命令路径错误引起，当前文档与代码足以定位，尚无跨运行重复、隐含协议或高成本诊断证据；
- 重开条件：使用存在的配置、当前支持的命令和新目录仍出现同一阶段失败，或文档与 CLI 对配置生成行为产生冲突。

自动校验只证明这条教学路径仍与脚本一致，不证明真实同伴会及时回复，也不证明零基础读者无需提示就能完成交接。
