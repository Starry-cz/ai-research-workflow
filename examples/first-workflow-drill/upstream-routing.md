# 已填写示例：这次报错需要提交上游 Issue 吗

> 本例来自对仓库教学脚本的一次实际命令检查。它演示“出现 traceback 不等于发现上游 bug”，不会真的创建 Issue。

## 1. 观察

- 命令：`python train.py --config configs/debug.json --output-dir results/debug-recorded`
- 代码身份：当前教学仓库未修改的 `train.py`
- 实际结果：命令以非零状态退出，首个关键异常为 `FileExistsError`
- 触发位置：`prepare_output(args.output_dir)`
- 当时输出目录：`results/debug-recorded`，已经包含仓库保存的记录结果

## 2. 对照文档与最小复查

- [演练 README](README.md)明确写明脚本拒绝覆盖非空输出目录；
- README 要求个人运行使用新的 `results/my-*` 目录；
- 该异常在写入训练结果前出现，保护已有证据不被覆盖；
- 改用新的输出目录是文档规定的使用方式，不需要修改脚本或评价协议。

## 3. 路由判断

- 是否偏离文档预期：否
- 是否证明上游缺陷：否
- 是否需要公开 Issue：否
- 是否需要 PR：否
- 类型：本地命令使用与输出路径冲突
- 当前状态：`LOCAL_USAGE_RESOLVED`

## 4. 正确下一步

沿用[演练 README](README.md)中对应系统的虚拟环境解释器，只把输出目录改为新的个人目录，例如：

```text
<虚拟环境解释器> train.py --config configs/debug.json --output-dir results/my-debug-02
```

如果新目录仍失败，再保留新的完整 traceback、解释器、commit 和命令，按[调试与求助卡](../../templates/10-debug-help-request.md)重新判断。不要删除 `debug-recorded` 来迁就命令，也不要提交“脚本不能运行”的上游 Issue。

## 5. 证据边界

本例只证明该次 `FileExistsError` 符合仓库防覆盖设计。它不证明所有 `FileExistsError` 都是用户问题，也不说明维护者永远不应改进错误消息。若文档未说明该行为、错误发生在空目录，或不同平台与文档不一致，应使用新证据重新路由。
