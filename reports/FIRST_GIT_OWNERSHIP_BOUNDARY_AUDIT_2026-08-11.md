# 首次 Git 所有权与发布边界审计（2026-08-11）

## 审计结论

原 L0 指南能让读者完成 commit，但操作顺序会让零基础读者在克隆作者仓库前修改全局 Git 身份，并在上游 `main` 上直接提交；它没有把“本地提交”“向远程发布”和“拥有远程写权限”分开。当前版本已改为：

```text
clone 作者仓库
  → 用 remote -v 确认所有者
  → 创建 learning/first-run 本地分支
  → 仅配置当前仓库身份
  → 只暂存 environment/README.md
  → 完成本地 commit
  → 到此停止，不向作者 origin 推送
```

## 问题与经验对照

- 小红书笔记[新手必看！代码传上 GitHub 竟然花了我 1 小时](https://www.xiaohongshu.com/explore/691c7015000000000d00df18)记录了换设备后同步代码、反复尝试 push，最后才意识到应先 clone 的实际摩擦。它是单人经验，只用于确认 clone、push 与同步顺序会成为新手卡点，不定义正确命令或权限规则。
- 知乎问题[Why pull request not push request?](https://www.zhihu.com/en/answer/275753841)中的多条个人回答把“没有他人仓库写权限—fork—向自己的分支 push—发起 PR”作为核心解释。它支持权限概念容易混淆这一观察，但回答年代和上下文不同，具体流程以 GitHub 官方文档为准。
- 知乎文章[CS 系新生实用工具科普](https://zhuanlan.zhihu.com/p/1889106039556767985)尝试区分本地版本控制工具 Git 与在线托管平台 GitHub，也说明两者常被新手合并理解。它属于个人教程，不作为权限、安全或配置作用域的规范依据。

## 官方与项目对照

- [GitHub：设置 Git 用户名](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git)明确区分全局配置与单仓库配置，单仓库配置不会影响其他仓库；本指南因此使用 `git config --local`。
- [GitHub：设置 commit 邮箱](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)说明单仓库邮箱会覆盖当前仓库中的全局值，并支持 GitHub 提供的 `noreply` 地址；本指南保留隐私核对，但不要求修改整台电脑的配置。
- [GitHub：克隆仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)将 clone 定义为创建完整本地副本；[远程仓库说明](https://docs.github.com/en/get-started/git-basics/about-remote-repositories)把远程 URL 与本地仓库分开。能读取并 clone 公共仓库不等于拥有向该 URL push 的权限。
- [GitHub：向项目贡献](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)对无直接写权限的项目给出 fork、个人分支、push 和 Pull Request 顺序；[GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github)也以“创建分支—提交文件—打开 PR—合并”为零基础练习顺序。

## 采取的修改

- 将 clone 移到身份配置之前，并增加 `git remote -v` 与所有者解释；
- 在任何修改前创建 `learning/first-run`，避免在克隆得到的上游 `main` 上练习；
- 删除 `user.name`、`user.email` 和 `init.defaultBranch` 的全局修改，改为当前仓库级姓名与邮箱；
- 第一次提交只暂存新建的 `environment/README.md`，提交前检查分支、状态与暂存 diff；
- 明确本地 commit 不需要 GitHub 写权限、不会自动公开，也不应直接 push 到 `Starry-cz` 的 `origin`；
- 把 fork、认证、push 和 PR 延后到真正需要公开贡献时，并按个人仓库、公开上游与团队仓库分流；
- 在仓库验证脚本中固定上述必需片段，并拒绝重新引入全局身份修改或宽范围暂存命令。

## 适用边界

- `learning/first-run` 是本仓库教学分支名，不替代团队已有的分支规范；
- 单仓库身份适合隔离第一次练习，不表示全局配置永远不应使用；同一设备只服务单一身份时，全局配置可以是个人选择；
- 本次不测试 GitHub 登录、HTTPS token、SSH key、fork 创建、branch protection 或 PR 审查；这些都不是第一次本地 commit 的完成条件；
- 本地 commit 仍会写入姓名和邮箱。若未来发布，必须先检查作者信息、敏感文件、目标 remote 与仓库权限；
- 已获得团队写权限也不等于可以向默认分支直接 push，仍应遵守团队保护规则和任务授权边界。

## 验收标准

- 指南不含 `git config --global user.name`、`git config --global user.email` 或全局默认分支修改；
- 新克隆中的第一次练习 commit 位于 `learning/first-run`；
- commit 只包含明确创建的环境记录，`origin/main` 保持不变；
- 不配置 GitHub 凭据、不执行 push 也能完成全部首次 Git 验收；
- 仓库质量检查能阻止后续文档重新混淆本地提交与远程发布。

当前状态：已在 Windows 临时克隆中实际创建 `learning/first-run`、写入单仓库身份并完成一次仅含 `environment/README.md` 的本地 commit；`origin/main` 提交值前后相同，练习分支没有上游跟踪分支，全程未配置 GitHub 凭据或执行 push。仓库质量检查覆盖 90 份 Markdown、L0 Git 边界与 51 个工具条目并通过；首次运行、三组比较、知识检索、无命中交接和特殊路径回归也通过。真人是否能独立理解 remote、branch、commit 与 push 的差异，仍待首次使用观察，不能仅凭脚本宣称通过。
