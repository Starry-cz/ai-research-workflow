# 已填写示例：第一次知识检索与安全复用

> 这是仓库维护者对教学夹具的答案，不是陌生新手可用性测试结果。它记录当前仓库中的实际搜索、代码检查和运行验证。

## 1. 原始症状与边界

- 当前任务：重跑教学 debug 配置；
- 预期：在个人新目录生成四类产物；
- 实际：写入已有记录目录时，训练开始前出现“输出目录非空，拒绝覆盖”和 `FileExistsError`；
- 听到的建议：删除旧目录，或使用未经核验的 overwrite 选项；
- 当前权限：读取、查看帮助、在临时新目录运行；不得删除记录结果或修改脚本；
- 初始假设：未知。先检索，不把“权限”“脚本 bug”或“应该覆盖”写成事实。

## 2. 查询记录

- Q0：`git grep -n -E "输出目录|拒绝覆盖"`
  - 命中正式知识条目、上游路由记录、README、代码、练习文本和两个教学候选；
  - 结论：召回充分，但候选仍混杂，不能执行第一条建议。
- Q1：`git grep -n "FileExistsError"`
  - 命中当前 `train.py`、正式知识条目、路由记录和教学材料；
  - 结论：异常类型与正式条目的症状匹配，权限候选缺少对应签名。
- Q2：`git grep -n -E "prepare_output|overwrite|output-dir" -- examples/first-workflow-drill`
  - 命中 `prepare_output`、合法的 `--output-dir`、正式条目和教学干扰项；
  - 结论：需要用当前命令帮助区分“文字命中”和“真实 CLI”。

## 3. 候选比较

### 保留：KNOW-DEMO-001

- 状态为 `ACTIVE_LOCAL`，属于正式教学知识；
- 错误类型、阶段、`prepare_output` 和非空目录均匹配；
- 能链接到 `train.py`、README 和实际路由记录；
- 推荐动作是保留旧证据并使用新目录，符合当前授权。

### 排除：FIXTURE-OLD-001

- 明确标为 `SUPERSEDED_TEACHING_FIXTURE`，不在正式索引；
- 没有 commit、代码、文档或运行来源；
- `python train.py --help` 没有 overwrite 选项；
- 删除或覆盖记录目录具有破坏性，也超出当前授权。

### 排除：FIXTURE-NEAR-001

- 明确标为 `PROVISIONAL_TEACHING_FIXTURE`，没有实际运行；
- 当前异常是 `FileExistsError`，没有 `PermissionError`；
- 当前目标目录已非空，不满足“空目录但无写权限”的假设。

## 4. 最小验证

- 命令帮助包含 `--output-dir`，不包含 overwrite 选项；
- 当前 `prepare_output` 在目标目录存在且非空时主动抛出 `FileExistsError`；
- 对仓库保存的 `results/debug-recorded` 运行会稳定出现同一防覆盖异常；
- 使用临时新目录运行同一 debug 配置能够完成，并生成 `config.snapshot.json`、`environment.json`、`metrics.json` 和 `run.log`；
- 本验证没有删除、覆盖或修改仓库证据。

## 5. 决定与写回

- 复用决定：`APPLY_WITHIN_SCOPE`；
- 实际动作：保留记录目录，个人重跑使用新目录；
- 排除范围：不推广到空目录、权限错误、其他仓库或代码已经改变的情况；
- 知识状态：保持 `ACTIVE_LOCAL`，这次由仓库维护者复核，仍不构成陌生成员或跨环境的 `CONFIRMED_REUSE`；
- 检索改进：保留“训练未开始”“结果目录”“删旧目录”“overwrite”等用户语言和误导建议，用于未来候选排除；
- 证据位置：[正式知识条目](knowledge-entry.md)、[上游路由记录](upstream-routing.md)、[`train.py`](train.py)和本页。

## 6. 结论边界

这次结果证明当前教学材料可以支持一次受控的候选检索、排除和验证，不证明零基础读者无需提示就能完成，也不证明所有类似异常都应使用同一动作。真实可用性需要观察未参与编写的读者完成任务。
