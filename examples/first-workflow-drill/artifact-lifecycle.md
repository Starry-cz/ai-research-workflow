# 教学演练产物生命周期台账

这是一份已填写示例，用于说明“失败记录要保留”和“所有二进制永久保存”并不是同一要求。本演练没有 checkpoint、外部数据或受限资产。

| 资产或集合 | run / claim 引用 | 分类 | 唯一位置与身份 | 大小 | 负责人 | 复查日 / 到期 | 决定与证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 脚本与配置 | 三组教学运行 | `A3_ARCHIVE` | Git commit `ad6538378ff9c15a744d13ecfd9c17e1afc9de15` | 小型文本 | 仓库维护者 | 相关文件变化时 | `ARCHIVE_IMMUTABLE`；是复跑入口 |
| 记录的三组结果 | 实验卡、结果—主张审计、交接卡 | `E2_EVIDENCE` | `results/*-recorded/` | 小型文本 | 仓库维护者 | 相关脚本或配置变化时 | `ARCHIVE_IMMUTABLE`；自动验收直接读取 |
| 用户自己的 `results/my-*` | 个人练习 | `R1_RECOVERY` → `T0_TRANSIENT` | 被本目录 `.gitignore` 排除 | 依运行而定 | 运行者 | 完成验收和记录决定后 | `REVIEW_REQUIRED`；由运行者确认无引用后决定，不由仓库自动删除 |
| 合成输入数据 | 由训练脚本即时生成 | `T0_TRANSIENT` | 没有独立文件；生成逻辑见 `train.py` | 180 条样本 | 仓库维护者 | 代码变化时 | 不单独归档；代码、配置与数据卡足以重建 |
| 冷启动临时副本 | H2 交接验证 | `T0_TRANSIENT` | 系统临时目录，完成后按精确路径清理 | 小型 | 仓库维护者 | 同次验证结束 | 已通过复跑并在审计报告留下结果；不作为唯一证据 |

## 主张反向检查

```text
“教学证据链完整”
  → verify.py 的 PASS
  → 三组 metrics.json 与 config.snapshot.json
  → 全部 seed 状态、数据身份和唯一主要变量检查
  → train.py、configs/*.json 与锁定 commit
```

三组 `*-recorded` 结果仍被自动验收和已填写示例引用，因此不能把它们当作普通缓存清理。个人练习目录未进入仓库主张链，仍需运行者先记录结果与决定，再按[产物生命周期指南](../../docs/EXPERIMENT_ARTIFACT_LIFECYCLE.md)复查。
