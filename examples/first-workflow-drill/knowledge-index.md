# 教学演练研究知识索引

本页演示薄索引如何帮助未来读者按症状找到已核验经验。它不复制配置、命令、异常全文和结果数字；这些事实仍保存在链接的原始记录中。

| 条目 | 检索与状态 |
| --- | --- |
| [KNOW-DEMO-001：非空输出目录触发 FileExistsError 是防覆盖设计](knowledge-entry.md) | `FAILURE_PATTERN` + `PROTOCOL_GUARDRAIL`；stage=`training`；component=`prepare_output`；symptom=`FileExistsError / 输出目录非空 / 拒绝覆盖`；scope=`first-workflow-drill`；状态=`ACTIVE_LOCAL`；最后核验=`2026-08-09`。 |

## 如何检索

在仓库根目录可以使用：

```powershell
rg -n "FileExistsError|输出目录非空|prepare_output" examples/first-workflow-drill
```

搜索结果应同时指向知识条目、原始路由记录、README 使用规则和代码位置。知识条目负责告诉读者先看哪里；最终判断仍回到当前 commit、当前目录状态和原始证据。

## 索引边界

- 当前只有一条已填写教学知识，不代表真实项目应为每次报错建卡；
- 本索引公开可见，但仓库尚未确认许可证，公开不等于允许任意再分发；
- 新证据改变含义时，应创建替代条目并在这里标记 supersede，不静默重写历史原因；
- 涉及私有代码、受限数据或匿名材料时，索引位置和可见字段必须服从 S0–S3 共享边界。
