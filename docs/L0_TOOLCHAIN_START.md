# L0 工具链最小起步指南

这份指南只解决第一次科研实践所需的最小工具链：确认 Git 和 Python、创建项目独立环境、运行仓库内演练、保存环境信息并完成第一次 Git 提交。它不替代完整的 Python、Shell 或 Git 课程。

完成后你应能展示五项产物：

```text
Git 与 Python 版本
  → 指向项目 .venv 的解释器路径
  → 一条实际成功的运行命令
  → 环境说明与依赖快照
  → 可以查看 diff 的第一次 commit
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

## 2. 配置 Git 身份并检查隐私

Git 提交会永久记录作者姓名和邮箱。先在 GitHub 的 Email 设置中确认用于提交的已验证邮箱；希望隐藏私人邮箱时，使用 GitHub 提供的 `noreply` 地址。

```text
git config --global user.name "你的显示名称"
git config --global user.email "你确认用于提交的邮箱"
git config --global init.defaultBranch main
git config --list --show-origin
```

上面的命令在 PowerShell、macOS 和 Linux 终端中都可使用。不要照抄示例身份；提交前用 `git config user.name` 和 `git config user.email` 再次核对。

## 3. 用 clone 保留仓库历史

`Download ZIP` 只得到文件快照，不包含完整 Git 历史。练习版本控制时使用 HTTPS clone：

```text
git clone https://github.com/Starry-cz/ai-research-workflow.git
cd ai-research-workflow
git rev-parse --show-toplevel
git status
git log -1 --oneline
```

第一次只需理解：仓库是带历史的项目目录；commit 是一次可定位的版本；`status` 告诉你哪些文件发生变化；`diff` 展示尚未提交的内容。认证、分支和协作流程可以在完成本指南后再学。

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

不要一开始使用 `git add .`。先查看并明确暂存的文件：

```text
git status
git diff
git add README.md .gitignore environment
git diff --cached
git commit -m "chore: initialize research environment"
git log -1 --oneline
```

如果文件名与示例不同，只添加你确认过的路径。虚拟环境、数据和密钥不应出现在 `git diff --cached` 中。是否 push 到远程取决于仓库权限和数据合规；完成本地 commit 已经满足本指南的版本控制验收。

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
- [ ] Git 姓名和邮箱已经核对，私人邮箱不会被意外公开
- [ ] `sys.executable` 指向当前项目的 `.venv`
- [ ] 安装和运行始终使用同一个解释器的 `-m pip`
- [ ] 仓库内调试演练生成四类可检查产物
- [ ] `.venv`、密钥、数据和大结果没有进入暂存区
- [ ] 环境说明和依赖快照已保存，并写明局限
- [ ] 第一次 commit 可以通过 `git log -1 --oneline` 找到

完成后回到[零基础科研准备检查表](../templates/00-readiness-checklist.md)，再决定需要补 Python、数据处理还是 PyTorch。
