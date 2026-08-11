# 首次运行跨平台证据审计

- 审计日期：2026-08-11
- 审计对象：`Starry-cz/ai-research-workflow`
- 问题编号：I-049
- 结论：原文分别给出 Windows 与 macOS/Linux 命令，但自动检查只运行在 Ubuntu，且验收命令使用 Bash 续行符，不能据此声称跨平台持续可用。本轮改为 Windows、Ubuntu、macOS 矩阵并新增特殊路径检查；首次远端运行进一步发现 Windows 英文代码页无法输出中文 `--help`，统一 UTF-8 后重新验证。CI 仍不能替代个人 IDE、GPU、服务器和论文依赖核验。

## 1. 当前问题

“文档提供多系统命令”和“相同提交在多系统持续通过”是两种不同证据。此前 `First workflow drill` 只使用 `ubuntu-latest`，其中 `verify.py` 还使用反斜杠续行；切换到 Windows 默认 PowerShell 后该写法不能直接复用。首次演练 README 中的一次 Windows 运行耗时也只是历史人工记录，没有覆盖 macOS、特殊字符路径或后续提交。

这会造成两个新手风险：一是把绿色 Ubuntu CI 理解成自己的 Windows / macOS 一定可用；二是本机失败时同时更换 shell、解释器、路径写法和依赖，最后无法判断真正原因。

## 2. 经验帖对照

- [“我明明 pip install 了啊！”](https://www.xiaohongshu.com/explore/67bb262f000000000603ba8b)记录命令行已经安装、PyCharm 仍报 `ModuleNotFoundError` 的解释器错位。它确认虚拟环境与 IDE 身份是常见摩擦，但属于 IDE 场景个人教程，不能证明所有导入失败都由环境错位造成；
- [Python 读取文件：路径存在特殊字符](https://www.xiaohongshu.com/explore/677b47f60000000014020670)展示 Windows 路径字面量中的反斜杠可能被解释为 `\t`、`\r` 等转义。它只支持“路径语法需要检查”，不能把所有 CLI、权限或文件不存在问题归因于特殊字符；
- [cmd 运行 Python 无法打开（已设置 PATH）](https://www.xiaohongshu.com/explore/663adfb3000000001e037a77)呈现 Windows 应用执行别名、PATH 与多个 Python 入口混淆的个案。本仓库据此要求记录真实解释器，不把修改注册表、卸载版本或关闭别名设为通用步骤；
- [Python 环境要配死了](https://www.xiaohongshu.com/explore/68a2ff42000000001b01e5b5)把 Python、CUDA 和路径配置混杂造成的入门阻塞集中呈现。它用于确认痛点，不作为版本组合或安装命令来源；
- 知乎文章[Python3 安装后崩溃？新手必看的 10 大解决方案](https://www.zhihu.com/tardis/bd/art/30868245301)列出 PATH、权限、虚拟环境、多版本和系统差异。它属于汇总型个人文章，只用于补充症状；其中管理员运行、卸载和系统别名调整都不能在未定位根因时直接采用。

## 3. GitHub 项目与正式文档对照

- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)给出 `matrix` 在多个操作系统组合上创建 job 的正式语法；因此仓库以实际矩阵 job 代替文字性兼容声明；
- [GitHub：Building and testing Python](https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-python)建议用 `setup-python` 固定 Python，并展示跨操作系统矩阵；[actions/setup-python](https://github.com/actions/setup-python)提供 runner 上的 Python 版本配置，但不代表个人机器的 PATH 或 IDE 已正确设置；
- [actions/runner-images](https://github.com/actions/runner-images)公开 GitHub 托管 runner 镜像及其状态。矩阵通过只证明相应 runner 镜像与当前提交，不证明所有 Windows、Linux 发行版或 macOS 版本；
- [Python `venv`](https://docs.python.org/3/library/venv.html)说明不同平台的激活命令不同，且激活不是使用虚拟环境的必要条件；因此入门命令直接调用 `.venv` 解释器，减少 shell 状态歧义；
- [Python `pathlib`](https://docs.python.org/3/library/pathlib.html)提供面向不同系统的路径对象；本仓库用它处理本地路径，同时通过真实子进程验证特殊字符路径，而不是只做字符串检查；
- [The Turing Way：Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv/)强调每台机器的操作系统、软件和版本共同构成环境。由此可知，多系统 CI 是证据增量，不是“在任何机器都能复现”的证明。

## 4. 采取行动

- 将 `First workflow drill` 从单一 `ubuntu-latest` 改为 `windows-latest`、`ubuntu-latest`、`macos-latest`，固定 Python 3.11，并设置 `fail-fast: false` 以保留各系统结果；
- 将只适用于 Bash 的多行验收命令改成各 runner shell 都能直接执行的单行命令；
- 新增 `verify_cross_platform.py`：使用当前解释器和参数列表，在含中文与空格的临时目录真实运行 `train.py`，核对四项产物、环境身份、完成状态和防覆盖异常；
- 根据首次远端矩阵失败，将 `train.py` 的标准输出、标准错误以及知识检索 / 无命中脚本启动的子进程统一固定为 UTF-8，不再依赖 Windows runner 的区域代码页；
- 在首页、L0 指南和演练 README 中分开写明“持续验证范围”与“不在验证范围内的本机因素”。

## 5. 验证边界

本轮矩阵覆盖 GitHub 托管 runner 上的标准库脚本、Python 3.11、参数传递、特殊路径、产物生成和防覆盖行为。它不覆盖：

- Windows `cmd`、所有 PowerShell 执行策略或任意第三方终端编码；
- IDE、Notebook kernel、conda、uv、Poetry 与多环境切换；
- WSL、学校集群、容器、代理、私有网络和挂载盘权限；
- PyTorch、CUDA、GPU 驱动、编译器、真实数据与论文仓库依赖；
- 不同操作系统下的逐位数值一致性或真实论文复现。

## 6. 当前验证状态

- 本地 Windows：特殊路径检查、三组实验验收、知识检索演练、无命中交接演练均已通过；仓库质量检查已检查 93 份 Markdown 和 52 个工具条目并通过；
- GitHub Actions 首次矩阵：Ubuntu 与 macOS 通过，Windows 在知识检索步骤暴露 `train.py --help` 中文输出编码问题；修复提交 `a79df02` 的 [First workflow drill](https://github.com/Starry-cz/ai-research-workflow/actions/runs/31456892728)中 Windows、Ubuntu、macOS 三个 Python 3.11 job 及全部教学步骤均通过，远端矩阵闭环完成；
- 真人可用性：尚未由未参与编写的零基础读者执行，不能表述为“零基础用户已验证”。
