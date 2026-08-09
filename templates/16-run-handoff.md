# Run Handoff Card

仅在关键运行需要交给导师、合作者、另一台机器或未来的自己复查时使用。填写前阅读[运行交接与冷启动复查](../docs/RUN_HANDOFF_REPLAY.md)；已有实验室平台覆盖的字段直接链接，不重复抄写。

## 1. 交接范围

- 项目与唯一入口：
- 交接人 / 接收者：
- 日期与用途：
- 声明深度：H0_LOCATE / H1_VERIFY / H2_REPLAY / H3_TAKEOVER
- 当前一句话结论：
- 当前决定：PROCEED / REFINE / PIVOT / STOP / 其他
- 未解决问题与主张边界：

## 2. 主要来源映射

| 对象 | 唯一来源或稳定 ID | 身份 / 版本 | 访问状态与负责人 |
| --- | --- | --- | --- |
| 代码 |  | branch / commit / dirty diff |  |
| 环境 |  | lock / Python / CUDA / OS |  |
| 数据与 split |  | revision / checksum |  |
| 配置 |  | path / fingerprint |  |
| 关键运行 |  | run ID / state |  |
| 日志 |  | run ID / date |  |
| 产物 |  | hash / size / retention |  |
| 指标与图表 |  | evaluator / version |  |
| 决策记录 |  | date / owner |  |

不要填写密钥。受限资产只写访问范围、申请方式和负责人。

- 产物生命周期指南：[EXPERIMENT_ARTIFACT_LIFECYCLE.md](../docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)
- 平台 TTL / 账号或服务器回收日：
- 生命周期决定：KEEP_ACTIVE / ARCHIVE_IMMUTABLE / PRUNE_BINARY_KEEP_RECORD / HOLD_RESTRICTED / REVIEW_REQUIRED
- 若已清理，墓碑记录与替代入口：

## 3. 最小复查入口

- 起始目录：
- 检出命令：
- 安装 / 环境命令：
- 获取允许共享资产的方式：
- 最快检查命令与预期信号：
- 指标重算命令：
- 预期值、统计单位与容差：
- 最小复跑命令、预算与停止条件：
- 已知平台差异或失败项：

## 4. 接收者冷启动记录

- 实际目录 / 机器：
- 实际 commit 与环境：
- 是否依赖交接人口头修正：是 / 否
- H0 查找结果：通过 / 失败 / 不适用
- H1 指标核验：通过 / 失败 / 不适用
- H2 最小复跑：通过 / 失败 / 不适用
- H3 接管准备：通过 / 失败 / 不适用
- 实际值与差异：
- 实际耗时和资源：
- 缺失入口、权限或过期引用：
- 复查日志与新产物位置：

## 5. 交接决定

- 最终状态：HANDOFF_READY / REVIEW_ONLY / NEEDS_ACCESS / STALE_REFERENCE / REPLAY_FAILED
- 状态证据：
- 需要修正的唯一来源：
- 责任人与截止时间：
- 下一次复查触发条件：
