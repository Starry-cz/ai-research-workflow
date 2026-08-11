"""验证检索无命中后的求助、回复验证与知识回流演练。"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_ARTIFACTS = {
    "config.snapshot.json",
    "environment.json",
    "metrics.json",
    "run.log",
}


class NoMatchHandoffError(RuntimeError):
    """表示无命中交接材料或当前脚本已经失配。"""


def configure_stdio() -> None:
    """固定校验脚本输出编码，便于 Windows 与 CI 保存中文日志。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def read_required(name: str) -> str:
    """读取演练文件，并在缺失时给出明确错误。"""
    path = ROOT / name
    if not path.is_file():
        raise NoMatchHandoffError(f"缺少演练文件：{name}")
    return path.read_text(encoding="utf-8")


def run_command(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    """在演练目录执行命令并保留退出码与文本输出。"""
    environment = os.environ.copy()
    # 子进程和捕获端统一使用 UTF-8，避免 Windows runner 的英文代码页破坏中文异常。
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


def validate_record() -> None:
    """检查记录包含无命中、交接、回复验证和知识回流边界。"""
    record = read_required("knowledge-no-match-handoff.md")
    required_markers = (
        "NO_MATCH",
        "FileNotFoundError",
        "无死路交接包",
        "唯一希望对方判断的问题",
        "TEACHING_RESPONSE_FIXTURE",
        "ANSWER_CANDIDATE",
        "VERIFIED_WITHIN_SCOPE",
        "SELF_RESOLVED_NO_ARTICLE",
        "IMPROVE_FINDABILITY",
        "不提交 Issue",
        "不创建 PR",
        "不证明零基础读者",
    )
    for marker in required_markers:
        if marker not in record:
            raise NoMatchHandoffError(f"无命中交接记录缺少：{marker}")

    knowledge_index = read_required("knowledge-index.md")
    if "FileNotFoundError" in knowledge_index:
        raise NoMatchHandoffError("正式知识索引已出现 FileNotFoundError，需要重新审计 NO_MATCH 结论")


def validate_no_match_failure() -> None:
    """实际确认不存在的配置在创建输出目录前稳定失败。"""
    with tempfile.TemporaryDirectory(prefix="no-match-failure-") as temporary_directory:
        output_path = Path(temporary_directory) / "should-not-exist"
        failed = run_command(
            [
                sys.executable,
                "train.py",
                "--config",
                "configs/does-not-exist.json",
                "--output-dir",
                str(output_path),
            ]
        )
        failed_text = failed.stdout + failed.stderr
        if failed.returncode == 0 or "FileNotFoundError" not in failed_text:
            raise NoMatchHandoffError("不存在的配置没有稳定触发 FileNotFoundError")
        if output_path.exists():
            raise NoMatchHandoffError("配置读取失败前不应创建输出目录")


def validate_response_candidate() -> None:
    """用现有配置和新临时目录验证回复候选，不触碰仓库记录。"""
    config_path = ROOT / "configs" / "debug.json"
    if not config_path.is_file():
        raise NoMatchHandoffError("回复候选依赖的 configs/debug.json 不存在")

    with tempfile.TemporaryDirectory(prefix="no-match-response-") as temporary_directory:
        output_path = Path(temporary_directory) / "verified-output"
        completed = run_command(
            [
                sys.executable,
                "train.py",
                "--config",
                "configs/debug.json",
                "--output-dir",
                str(output_path),
            ]
        )
        if completed.returncode != 0:
            raise NoMatchHandoffError(
                "回复候选验证失败：" + (completed.stdout + completed.stderr).strip()
            )
        produced = {path.name for path in output_path.iterdir() if path.is_file()}
        if produced != EXPECTED_ARTIFACTS:
            raise NoMatchHandoffError(
                f"验证产物不完整：期望 {sorted(EXPECTED_ARTIFACTS)}，实际 {sorted(produced)}"
            )


def main() -> None:
    validate_record()
    validate_no_match_failure()
    validate_response_candidate()
    print("PASS：无命中、上下文交接、回复候选验证与知识回流记录一致。")
    print("边界：自动检查不证明真人求助体验、响应质量或零基础可用性。")


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except NoMatchHandoffError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
