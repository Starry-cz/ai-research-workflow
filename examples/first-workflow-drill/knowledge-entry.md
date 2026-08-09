# KNOW-DEMO-001：非空输出目录触发 FileExistsError 是防覆盖设计

- 类型：`FAILURE_PATTERN` + `PROTOCOL_GUARDRAIL`
- 状态：`ACTIVE_LOCAL`
- 负责人、创建日、最后核验日：仓库维护者；2026-08-09；2026-08-09
- 验证与共享：V2 `AUDITABLE_RESULT`；S3 `PUBLIC_VIEWABLE`
- 检索标签：stage=`training`；component=`prepare_output`；symptom=`FileExistsError / 输出目录非空 / 拒绝覆盖`；scope=`examples/first-workflow-drill`
- 原始来源：[上游路由记录](upstream-routing.md)、[运行说明](README.md)、[`train.py`](train.py)

## 可复用结论

在当前教学脚本中，如果 `--output-dir` 已存在且包含文件，`prepare_output` 会在写入结果前主动抛出 `FileExistsError`。这是一项防覆盖规则，不是“训练代码无法运行”的充分证据，也不需要仅凭该异常提交上游 Issue。

## 适用范围

只有以下条件同时满足时，才可以使用这条经验：

- 当前代码仍包含相同的 `prepare_output` 非空目录检查；
- 异常发生在准备输出目录阶段；
- 目标目录确实已经包含旧结果；
- README 仍要求为个人重跑创建新的 `results/my-*` 目录。

以下情况不得直接套用：目标目录为空；异常来自权限、磁盘、路径编码或并发问题；代码 / 文档已改变；错误发生在其他项目。相同异常类型不证明根因相同。

## 已验证诊断与动作

1. 核对当前 commit 和 `prepare_output` 代码；
2. 查看命令中的 `--output-dir`，确认目录是否非空；
3. 核对 README 的防覆盖与新目录规则；
4. 不删除仓库保存的 `*-recorded` 证据；
5. 改用新的个人输出目录执行最小调试命令；
6. 如果新目录仍失败，保留新的完整 traceback，并重新进行问题路由。

## 证据与反例

- 已实际观察：向已有 `results/debug-recorded` 写入时，命令以 `FileExistsError` 非零退出；
- 代码证据：`train.py` 在目录存在且非空时明确拒绝覆盖；
- 文档证据：README 要求新运行使用新的 `results/my-*` 目录；
- 已排除：该次异常不是训练循环、数据生成或评价阶段产生；
- 未证明：所有 `FileExistsError` 都属于用户命令问题，或当前错误消息无需改进。

## 决定、后果与重开

- 复用决定：`APPLY_WITHIN_SCOPE`；
- 原决定：`LOCAL_USAGE_RESOLVED`，不创建上游 Issue，不修改防覆盖代码；
- 后果：保留旧证据目录，个人重跑使用新目录；
- 重开触发：空目录仍报同类错误、不同平台偏离文档、代码 / README 改变，或错误发生阶段不同；
- supersede 规则：新证据改变根因或推荐动作时，新建知识条目并将本条目标为 `SUPERSEDED`。

## 复用记录

### 2026-08-09 / `REUSE-DEMO-001`

- 当前身份与症状：当前教学脚本；非空 `debug-recorded`；`FileExistsError`；
- 决定与动作：`APPLY_WITHIN_SCOPE`；保留旧目录并使用新个人目录；
- 结果：路由结论与代码、README 一致；
- 状态影响：`ACTIVE_LOCAL`；尚未形成跨环境 `CONFIRMED_REUSE`；
- 证据：[上游路由记录](upstream-routing.md)。

### 2026-08-09 / `REUSE-DEMO-002`

- 当前身份与症状：当前教学脚本；从“输出目录非空”和错误签名检索；含两个教学干扰项；
- 决定与动作：`APPLY_WITHIN_SCOPE`；核对 CLI、来源和新临时目录运行；
- 结果：正式条目适用；过期 / 权限候选被排除；
- 状态影响：保持 `ACTIVE_LOCAL`；这是维护者复核，不是陌生成员验证；
- 证据：[知识检索结果](knowledge-retrieval-result.md)。

本条目只提供检索和限定诊断入口。实际命令、异常、代码与目录状态以原始来源为准。
