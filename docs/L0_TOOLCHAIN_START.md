# L0 工具链最小起步指南

这份指南只解决第一次科研实践所需的最小工具链：确认 Git 和 Python、创建项目独立环境、运行仓库内演练、保存环境信息并完成第一次 Git 提交。它不替代完整的 Python、Shell 或 Git 课程。

遇到 `origin`、分支、commit、解释器或虚拟环境等陌生词时，只查看[零基础默认路径术语速查](BEGINNER_GLOSSARY.md)的对应条目再返回本页，不需要先学完整 Git 或 Python 课程。

完成后你应能展示五项产物：

```text
 Git 与 Python 版本
  → 指向项目 .venv 的解释器路径
  → 一条实际成功的运行命令
  → 环境说明与依赖快照
  → 位于个人练习分支、可以查看 diff 的第一次本地 commit
```

## 1. 只选择与你系统一致的命令

- Windows：优先使用 PowerShell，本页 Windows 命令不与 Bash 命令混用；
- macOS / Linux：使用系统终端和对应 shell；
- 学校服务器：先确认登录节点、计算节点、模块系统和存储规则，不在登录节点启动训练。

先检查工具是否可用。

Windows PowerShell：

```powershell
git --version
py -3 --version
```

macOS / Linux：

```bash
git --version
python3 --version
```

如果命令不存在，分别从 [Git 官方下载页](https://git-scm.com/downloads)和 [Python 官方下载页](https://www.python.org/downloads/)开始，并阅读对应系统说明。不要先从网盘下载安装包，也不要根据旧教程盲目改系统 Python、PATH、软链接或注册表。

## 2. 用 clone 保留历史并确认远程所有者

`Download ZIP` 只得到文件快照，不包含完整 Git 历史。练习版本控制时使用 HTTPS clone：

```text
git clone https://github.com/Starry-cz/ai-research-workflow.git
cd ai-research-workflow
git rev-parse --show-toplevel
git remote -v
git status
git log -1 --oneline
```

`git remote -v` 应显示 `origin` 指向 `Starry-cz/ai-research-workflow`。这说明你克隆的是作者仓库的本地副本，不说明你拥有向作者仓库推送的权限。第一次只需理解：仓库是带历史的项目目录；commit 是一次可定位的本地版本；`status` 告诉你哪些文件发生变化；`diff` 展示尚未提交的内容。

## 3. 创建个人练习分支并只配置当前仓库身份

先离开上游默认分支，在本地创建练习分支：

```text
git switch -c learning/first-run
git branch --show-current
```

第二条命令应输出 `learning/first-run`。Git 提交会永久记录作者姓名和邮箱；先在 GitHub 的 Email 设置中确认用于提交的已验证邮箱，希望隐藏私人邮箱时使用 GitHub 提供的 `noreply` 地址。然后只为当前仓库设置身份：

```text
git config --local user.name "你的显示名称"
git config --local user.email "你确认用于提交的邮箱"
git config --local --list --show-origin
```

不要照抄示例身份。提交前再运行 `git config user.name` 和 `git config user.email` 核对。这里使用 `--local`，设置只影响当前练习仓库；本指南不要求修改计算机上的全局 Git 身份或默认分支。已有团队配置时，先遵守团队身份与签名规则。

## 4. 创建项目独立环境

每个项目使用独立环境，不在系统 Python、conda base 或另一个项目的环境中连续安装依赖。以下路径直接调用 `.venv` 中的解释器，因此即使没有激活环境，也不会把包装到错误的 Python。

Windows PowerShell：

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

macOS / Linux：

```bash
python3 -m venv .venv
./.venv/bin/python --version
./.venv/bin/python -m pip --version
./.venv/bin/python -c "import sys; print(sys.executable)"
```

最后一条输出必须指向当前仓库中的 `.venv`。在 Notebook 或 IDE 中也要选择同一解释器；“已经安装但 import 失败”时，先比较运行代码的 `sys.executable` 与执行 `-m pip` 的解释器。

如果 PowerShell 阻止激活脚本，不需要为了本指南降低系统执行策略，继续使用 `.\.venv\Scripts\python.exe` 即可。真实论文仓库如果提供 conda、uv、Poetry、容器或其他官方环境文件，应选择项目指定的一种方式，不要把多个环境管理器嵌套使用。

## 5. 先运行零依赖演练

仓库内演练只使用 Python 标准库，不需要安装 PyTorch 或其他包。输出目录必须使用新名称。

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe examples\first-workflow-drill\train.py `
  --config examples\first-workflow-drill\configs\debug.json `
  --output-dir examples\first-workflow-drill\results\my-first-debug
```

macOS / Linux：

```bash
./.venv/bin/python examples/first-workflow-drill/train.py \
  --config examples/first-workflow-drill/configs/debug.json \
  --output-dir examples/first-workflow-drill/results/my-first-debug
```

验收不是“终端没有红字”，而是输出目录中存在配置快照、环境、日志和指标四类文件，并能说明它们由哪条命令生成。

这条命令已经是“第一次工作流演练”的调试运行。进入[演练页](../examples/first-workflow-drill/README.md)后继续使用根目录的同一个 `.venv`，不要在 `examples/first-workflow-drill/` 中再创建环境，也不要覆盖 `my-first-debug`；直接运行单目录验收，看到第一个 `PASS` 后再决定是否进入三组比较。

### 本仓库实际验证到哪里

| 范围 | 当前证据与边界 |
| --- | --- |
| 零依赖首次演练 | GitHub Actions 已配置为使用 Python 3.11，在 Windows、Ubuntu 与 macOS runner 上执行同一训练和验收流程；对应 job 通过后才形成远端证据，另有含中文与空格路径的自动检查。 |
| 个人环境与真实项目 | CI 不验证你的 IDE、shell 激活、WSL、代理、学校服务器、CUDA、GPU 驱动或论文依赖；这些必须在目标机器按项目官方说明核验。 |

直接调用 `.venv` 解释器是为了明确“哪一个 Python 在运行”，不是要求关闭环境激活。[Python `venv` 文档](https://docs.python.org/3/library/venv.html)也说明激活并非使用虚拟环境的必要条件；如果出现“明明安装却无法导入”，先比较 `sys.executable` 与 `python -m pip --version` 指向的位置。含空格或中文的路径应作为一个完整参数传入；在 Python 代码中处理路径时优先使用 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html)，但它不能修复错误解释器、缺失文件或权限问题。

## 6. 安装真实项目依赖时使用同一解释器

只有项目 README 明确要求时，才执行对应安装命令。例如项目确实提供 `requirements.txt` 时：

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

macOS / Linux：

```bash
./.venv/bin/python -m pip install -r requirements.txt
```

不要把未知教程中的包版本、CUDA 命令或镜像设置混入论文官方环境。涉及 PyTorch、CUDA、编译器和 GPU 驱动时，先核对项目支持矩阵、框架官方安装说明和服务器驱动；记录完整命令与报错，再做单变量修改。不要使用 `sudo pip install` 或管理员终端掩盖环境边界问题。

## 7. 在第一次提交前建立忽略规则

至少在项目 `.gitignore` 中加入：

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
```

再按项目实际情况决定数据、checkpoint、日志和大结果的外部存储。不要提交访问令牌、密码、个人信息、受限数据或未公开材料；即使文件随后被删除，敏感内容仍可能留在 Git 历史中。

## 8. 保存环境说明与依赖快照

在编辑器中创建 `environment/README.md`，至少记录：

```markdown
# 环境记录

- 操作系统与版本：
- Python 版本：
- 项目解释器绝对路径：
- 环境创建命令：
- 依赖安装命令：
- 最小验证命令与结果位置：
- GPU、驱动、CUDA 与框架版本：不适用 / 待真实项目填写
- 最后核验日期：
```

安装真实依赖后，可以额外保存当前环境快照：

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe -m pip freeze > environment\requirements-freeze.txt
```

macOS / Linux：

```bash
./.venv/bin/python -m pip freeze > environment/requirements-freeze.txt
```

`pip freeze` 记录当前环境中已安装的版本，但不自动解释哪些是直接依赖，也不保证跨操作系统、GPU 和 Python 版本完全可重建。真实项目应优先保留其官方环境文件，并同时记录系统、驱动、框架和安装命令。

## 9. 完成第一次可检查提交

不要一开始使用 `git add .`，也不要把仓库中原有且没有修改的文件列入命令。只暂存第 8 步新建并确认不含敏感信息的环境记录：

```text
git branch --show-current
git status --short
git add environment/README.md
git diff --cached
git commit -m "chore: initialize research environment"
git log -1 --oneline
git status
```

提交前，分支必须仍为 `learning/first-run`；`git diff --cached` 应只显示你主动填写的环境记录，虚拟环境、数据、密钥和演练结果不应出现。如果你还修改了其他文件，先不要一起提交，保留 `git status --short` 并逐项确认。

到这里已经完成本指南的版本控制验收。这个 commit 只存在于你的电脑：它不需要 GitHub 写权限、不会自动公开，也不会改变作者仓库。**不要运行 `git push origin main`，也不要把练习分支直接推送到当前 `origin`**。

以后确实需要公开或贡献时，再根据仓库所有权选择流程：

| 场景 | 进入远程协作前的动作 |
| --- | --- |
| 向本仓库等公开项目贡献 | 先在 GitHub fork 到自己的账号，在个人副本创建并推送分支，再向上游发起 Pull Request。 |
| 自己拥有的仓库 | 确认 `git remote -v` 指向自己的账号，再按仓库规则推送当前分支。 |
| 导师或团队仓库 | 先确认写权限、目标 remote、分支命名、敏感数据和审查规则，不因“能 clone”推断“能 push”。 |

Fork、认证、push 和 Pull Request 不属于第一次本地提交的前置条件。准备贡献时再进入[第一次向开源上游求助与贡献](UPSTREAM_HELP_AND_CONTRIBUTION.md)，不要在本轮同时排查账号、令牌、SSH 和分支保护。

## 10. 最小日常循环

以后每次科研会话只需重复：

```text
开始前：git status → 确认分支、旧改动和当前任务
执行中：保存命令、配置、日志和 run_id
结束前：运行检查 → git diff → 精确暂存 → git diff --cached
验收后：commit → 在实验卡中记录 commit 与产物位置
```

不要在不理解差异时使用强制覆盖、清空历史或递归删除命令。遇到冲突或陌生 Git 状态时，先保存 `git status` 和完整提示，再查官方文档或使用[调试与求助卡](../templates/10-debug-help-request.md)。

## 完成检查

- [ ] Git 与 Python 命令来自当前系统的正确入口
- [ ] `git remote -v` 已确认远程所有者，当前分支是 `learning/first-run`
- [ ] 当前仓库的 Git 姓名和邮箱已经核对，私人邮箱不会被意外公开
- [ ] `sys.executable` 指向当前项目的 `.venv`
- [ ] 安装和运行始终使用同一个解释器的 `-m pip`
- [ ] 仓库内调试演练生成四类可检查产物
- [ ] `.venv`、密钥、数据和大结果没有进入暂存区
- [ ] 环境说明和依赖快照已保存，并写明局限
- [ ] 第一次本地 commit 可以通过 `git log -1 --oneline` 找到，且没有误推送到作者仓库

完成后回到[零基础科研准备检查表](../templates/00-readiness-checklist.md)，再决定需要补 Python、数据处理还是 PyTorch。
