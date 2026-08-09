"""验收第一次工作流演练的三组输出是否完整且可公平比较。"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = {
    "config.snapshot.json",
    "environment.json",
    "metrics.json",
    "run.log",
}
SUMMARY_FIELDS = {
    "validation_accuracy": ("validation", "accuracy"),
    "validation_loss": ("validation", "loss"),
    "test_accuracy": ("test", "accuracy"),
    "test_loss": ("test", "loss"),
}


class VerificationError(RuntimeError):
    """表示产物不满足演练预先声明的验收规则。"""


def configure_stdio() -> None:
    """固定为 UTF-8，避免 Windows 终端与日志采集器解码不一致。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="验收三组演练输出")
    parser.add_argument("--debug-dir", type=Path, required=True)
    parser.add_argument("--baseline-dir", type=Path, required=True)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as file:
            value = json.load(file)
    except json.JSONDecodeError as error:
        raise VerificationError(f"JSON 无法解析：{path}（{error}）") from error
    require(isinstance(value, dict), f"JSON 顶层必须是对象：{path}")
    return value


def verify_summary(metrics: dict[str, Any], directory: Path) -> None:
    runs = metrics["runs"]
    summary = metrics.get("summary")
    require(isinstance(summary, dict), f"缺少 summary：{directory}")

    for summary_name, (split, metric) in SUMMARY_FIELDS.items():
        recorded = summary.get(summary_name)
        require(isinstance(recorded, dict), f"缺少汇总项 {summary_name}：{directory}")
        values = [run[split][metric] for run in runs]
        expected = {
            "mean": statistics.fmean(values),
            "population_std": statistics.pstdev(values),
            "minimum": min(values),
            "maximum": max(values),
        }
        for field, expected_value in expected.items():
            actual_value = recorded.get(field)
            require(
                isinstance(actual_value, (int, float))
                and math.isclose(actual_value, expected_value, rel_tol=1e-12, abs_tol=1e-12),
                f"{summary_name}.{field} 与 runs 重新计算结果不一致：{directory}",
            )


def verify_directory(directory: Path, role: str) -> tuple[dict[str, Any], dict[str, Any]]:
    require(directory.is_dir(), f"{role} 输出目录不存在：{directory}")
    missing_files = sorted(name for name in REQUIRED_FILES if not (directory / name).is_file())
    require(not missing_files, f"{role} 缺少文件：{missing_files}")

    config = load_json(directory / "config.snapshot.json")
    metrics = load_json(directory / "metrics.json")
    environment = load_json(directory / "environment.json")
    run_log = (directory / "run.log").read_text(encoding="utf-8")

    require(metrics.get("experiment_id") == config.get("experiment_id"), f"{role} 实验 ID 不一致")
    require(metrics.get("status") == "completed", f"{role} 顶层状态不是 completed")
    require(bool(metrics.get("claim_boundary")), f"{role} 缺少结论边界")
    require(bool(environment.get("python")), f"{role} 缺少 Python 环境记录")
    require(bool(environment.get("platform")), f"{role} 缺少平台记录")
    require(bool(environment.get("command")), f"{role} 缺少执行命令")

    planned_seeds = config.get("seeds")
    runs = metrics.get("runs")
    require(isinstance(planned_seeds, list) and planned_seeds, f"{role} 配置 seeds 无效")
    require(isinstance(runs, list) and runs, f"{role} runs 无效")
    actual_seeds = [run.get("seed") for run in runs]
    require(actual_seeds == planned_seeds, f"{role} 实际 seed 与配置不一致")
    require(all(run.get("status") == "completed" for run in runs), f"{role} 存在未完成运行")

    experiment_id = config["experiment_id"]
    require(f"experiment_id={experiment_id}" in run_log, f"{role} 日志缺少实验 ID")
    for seed in planned_seeds:
        require(f"seed={seed} status=completed" in run_log, f"{role} 日志缺少 seed={seed}")

    verify_summary(metrics, directory)
    return config, metrics


def changed_fields(left: dict[str, Any], right: dict[str, Any]) -> set[str]:
    keys = set(left) | set(right)
    return {key for key in keys if left.get(key) != right.get(key)}


def main() -> None:
    args = parse_args()
    debug_config, debug_metrics = verify_directory(args.debug_dir, "debug")
    baseline_config, baseline_metrics = verify_directory(args.baseline_dir, "baseline")
    candidate_config, candidate_metrics = verify_directory(args.candidate_dir, "candidate")

    # 正式比较只能改变实验身份和本轮科学变量 learning_rate。
    differences = changed_fields(baseline_config, candidate_config)
    require(
        differences == {"experiment_id", "learning_rate"},
        f"baseline 与 candidate 的差异字段必须恰为 experiment_id、learning_rate，实际为：{sorted(differences)}",
    )
    require(
        baseline_config["seeds"] == candidate_config["seeds"],
        "baseline 与 candidate 必须使用同一 seed 集合",
    )
    require(
        baseline_metrics.get("dataset") == candidate_metrics.get("dataset"),
        "baseline 与 candidate 的数据记录不一致",
    )

    # 调试运行必须比正式运行更小，且不能冒充确认性证据。
    require(len(debug_config["seeds"]) < len(baseline_config["seeds"]), "debug seed 数量必须更少")
    require(debug_config["epochs"] < baseline_config["epochs"], "debug epoch 数量必须更少")
    require(debug_metrics.get("dataset") == baseline_metrics.get("dataset"), "debug 使用的数据记录不一致")

    baseline_mean = baseline_metrics["summary"]["test_accuracy"]["mean"]
    candidate_mean = candidate_metrics["summary"]["test_accuracy"]["mean"]
    print("PASS：三组产物完整，全部计划运行完成，正式比较只改变 learning_rate。")
    print(f"baseline_test_accuracy_mean={baseline_mean:.6f}")
    print(f"candidate_test_accuracy_mean={candidate_mean:.6f}")
    print("结论边界：验收通过只证明教学证据链完整，不证明候选设置或方法普遍更优。")


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except VerificationError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
