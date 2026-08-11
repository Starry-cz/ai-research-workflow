"""在当前系统验证首次演练的路径处理、证据产物和防覆盖行为。"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TRAIN_SCRIPT = ROOT / "train.py"
DEBUG_CONFIG = ROOT / "configs" / "debug.json"
EXPECTED_ARTIFACTS = {
    "config.snapshot.json",
    "environment.json",
    "metrics.json",
    "run.log",
}


def configure_stdio() -> None:
    """统一 Windows 与 CI 中的中文检查输出编码。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def run_training(output_dir: Path) -> subprocess.CompletedProcess[str]:
    """使用参数列表调用当前解释器，避免把路径交给 shell 再次拆分。"""
    command = [
        sys.executable,
        str(TRAIN_SCRIPT),
        "--config",
        str(DEBUG_CONFIG),
        "--output-dir",
        str(output_dir),
    ]
    environment = os.environ.copy()
    # 固定被捕获输出的编码，避免不同 runner 的终端代码页影响错误核验。
    environment["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        check=False,
        encoding="utf-8",
        env=environment,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    configure_stdio()
    require(sys.version_info >= (3, 10), "本演练要求 Python 3.10 或更高版本")

    with tempfile.TemporaryDirectory(prefix="first-workflow-") as temp_dir:
        # 同时包含非 ASCII 字符和空格，覆盖新手常见的本地目录形态。
        output_dir = Path(temp_dir) / "AI 科研 path with spaces" / "首次运行"
        first_run = run_training(output_dir)
        require(
            first_run.returncode == 0,
            f"含中文与空格路径的首次运行失败：\n{first_run.stderr}",
        )

        actual_artifacts = {path.name for path in output_dir.iterdir() if path.is_file()}
        require(actual_artifacts == EXPECTED_ARTIFACTS, "首次运行没有生成预期的四项产物")

        environment = json.loads(
            (output_dir / "environment.json").read_text(encoding="utf-8")
        )
        require(environment.get("python"), "environment.json 缺少 Python 身份")
        require(environment.get("platform"), "environment.json 缺少平台身份")
        recorded_command = environment.get("command", "")
        require("--output-dir" in recorded_command, "environment.json 未记录输出参数")
        require("AI 科研 path with spaces" in recorded_command, "命令记录丢失特殊路径")

        metrics = json.loads((output_dir / "metrics.json").read_text(encoding="utf-8"))
        require(metrics.get("status") == "completed", "特殊路径运行状态不是 completed")

        second_run = run_training(output_dir)
        require(second_run.returncode != 0, "重复运行意外覆盖了已有证据目录")
        require("FileExistsError" in second_run.stderr, "重复运行没有触发防覆盖异常")

    print("PASS：当前 Python、跨平台路径、四项产物与防覆盖行为一致。")
    print(
        "BOUNDARY：本检查不覆盖 IDE、shell 激活、CUDA、GPU 驱动、WSL、"
        "私有网络、服务器策略或真实论文依赖。"
    )


if __name__ == "__main__":
    main()
