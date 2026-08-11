"""验证知识检索教学材料与当前脚本仍然一致。"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORDED_OUTPUT = ROOT / "results" / "debug-recorded"
EXPECTED_ARTIFACTS = {
    "config.snapshot.json",
    "environment.json",
    "metrics.json",
    "run.log",
}


class RetrievalDrillError(RuntimeError):
    """表示检索演练的夹具、答案或运行证据已经失配。"""


def configure_stdio() -> None:
    """固定校验脚本自身输出为 UTF-8，便于 Windows 终端和 CI 留存日志。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def read_required(name: str) -> str:
    """读取教学文件，并在缺失时给出单一明确错误。"""
    path = ROOT / name
    if not path.is_file():
        raise RetrievalDrillError(f"缺少教学文件：{name}")
    return path.read_text(encoding="utf-8")


def run_command(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    """在演练目录运行命令并保留可审计文本输出。"""
    environment = os.environ.copy()
    # 子进程和捕获端统一使用 UTF-8，不能依赖 runner 的区域代码页。
    environment["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=environment,
    )


def validate_documents() -> None:
    """检查正式条目、教学干扰项和已填写答案的关键边界。"""
    entry = read_required("knowledge-entry.md")
    fixtures = read_required("knowledge-retrieval-fixtures.md")
    result = read_required("knowledge-retrieval-result.md")

    for marker in ("ACTIVE_LOCAL", "FileExistsError", "prepare_output", "原始来源"):
        if marker not in entry:
            raise RetrievalDrillError(f"正式知识条目缺少：{marker}")

    for marker in (
        "TEACHING_FIXTURE",
        "SUPERSEDED_TEACHING_FIXTURE",
        "PROVISIONAL_TEACHING_FIXTURE",
        "不是历史实验",
    ):
        if marker not in fixtures:
            raise RetrievalDrillError(f"教学候选夹具缺少边界标记：{marker}")

    for marker in (
        "Q0",
        "Q1",
        "Q2",
        "APPLY_WITHIN_SCOPE",
        "排除：FIXTURE-OLD-001",
        "排除：FIXTURE-NEAR-001",
        "不构成陌生成员",
    ):
        if marker not in result:
            raise RetrievalDrillError(f"已填写检索结果缺少：{marker}")


def validate_current_cli() -> None:
    """确认合法参数和防覆盖实现没有与教学答案漂移。"""
    help_result = run_command([sys.executable, "train.py", "--help"])
    if help_result.returncode != 0:
        raise RetrievalDrillError("train.py --help 运行失败")
    if "--output-dir" not in help_result.stdout:
        raise RetrievalDrillError("当前 CLI 缺少 --output-dir")
    if "--overwrite" in help_result.stdout:
        raise RetrievalDrillError("当前 CLI 已出现 --overwrite，需要重新审计教学干扰项")

    source = read_required("train.py")
    for marker in ("FileExistsError", "输出目录非空，拒绝覆盖", "prepare_output"):
        if marker not in source:
            raise RetrievalDrillError(f"当前防覆盖实现缺少：{marker}")


def validate_failure_and_safe_route() -> None:
    """实际核验旧目录失败与新临时目录成功，两边都不改仓库证据。"""
    blocked = run_command(
        [
            sys.executable,
            "train.py",
            "--config",
            "configs/debug.json",
            "--output-dir",
            str(RECORDED_OUTPUT),
        ]
    )
    blocked_text = blocked.stdout + blocked.stderr
    if blocked.returncode == 0 or "FileExistsError" not in blocked_text:
        raise RetrievalDrillError("非空记录目录没有稳定触发预期防覆盖异常")

    with tempfile.TemporaryDirectory(prefix="knowledge-reuse-drill-") as temporary_directory:
        fresh_output = Path(temporary_directory) / "fresh-debug"
        completed = run_command(
            [
                sys.executable,
                "train.py",
                "--config",
                "configs/debug.json",
                "--output-dir",
                str(fresh_output),
            ]
        )
        if completed.returncode != 0:
            raise RetrievalDrillError(
                "新临时目录运行失败：" + (completed.stdout + completed.stderr).strip()
            )
        produced = {path.name for path in fresh_output.iterdir() if path.is_file()}
        if produced != EXPECTED_ARTIFACTS:
            raise RetrievalDrillError(
                f"新目录产物不完整：期望 {sorted(EXPECTED_ARTIFACTS)}，实际 {sorted(produced)}"
            )


def main() -> None:
    validate_documents()
    validate_current_cli()
    validate_failure_and_safe_route()
    print("PASS：知识检索夹具、候选排除、当前 CLI 与防覆盖运行证据一致。")
    print("边界：自动检查不证明陌生新手已经掌握检索与适用性判断。")


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except RetrievalDrillError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
