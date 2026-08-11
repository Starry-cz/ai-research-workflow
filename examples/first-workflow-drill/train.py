"""用纯 Python 演示可审计的多次运行与结果归档。"""

from __future__ import annotations

import argparse
import json
import math
import platform
import random
import shlex
import statistics
import sys
from pathlib import Path


def configure_stdio() -> None:
    """固定中文帮助与异常输出编码，避免 Windows 英文代码页写出失败。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="运行零依赖二分类工作流演练")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    required = {"experiment_id", "learning_rate", "epochs", "seeds"}
    missing = required.difference(config)
    if missing:
        raise ValueError(f"配置缺少字段：{sorted(missing)}")
    if not config["seeds"]:
        raise ValueError("seeds 不能为空")
    return config


def build_dataset() -> tuple[list[tuple[float, float, int]], ...]:
    """生成固定数据，并按固定索引切分，避免隐式数据变化。"""
    rows: list[tuple[float, float, int]] = []
    for index in range(180):
        x1 = ((index * 37 + 11) % 101) / 100
        x2 = ((index * 53 + 17) % 103) / 102
        label = int(1.35 * x1 - 0.9 * x2 + 0.08 > 0.28)
        rows.append((x1, x2, label))
    return rows[:120], rows[120:150], rows[150:]


def sigmoid(value: float) -> float:
    if value >= 0:
        return 1 / (1 + math.exp(-value))
    exp_value = math.exp(value)
    return exp_value / (1 + exp_value)


def evaluate(
    rows: list[tuple[float, float, int]], weights: list[float]
) -> dict[str, float]:
    """只读取已训练权重，计算损失和准确率，不更新模型。"""
    losses: list[float] = []
    correct = 0
    for x1, x2, label in rows:
        probability = sigmoid(weights[0] * x1 + weights[1] * x2 + weights[2])
        clipped = min(max(probability, 1e-12), 1 - 1e-12)
        losses.append(-(label * math.log(clipped) + (1 - label) * math.log(1 - clipped)))
        correct += int((probability >= 0.5) == bool(label))
    return {
        "loss": sum(losses) / len(losses),
        "accuracy": correct / len(rows),
    }


def train_once(
    train_rows: list[tuple[float, float, int]],
    validation_rows: list[tuple[float, float, int]],
    test_rows: list[tuple[float, float, int]],
    learning_rate: float,
    epochs: int,
    seed: int,
) -> dict:
    """使用训练集更新参数，再分别读取验证集和测试集。"""
    # seed 只控制参数初始化；固定 seed 便于调试，不代表结果没有不确定性。
    generator = random.Random(seed)
    weights = [generator.uniform(-0.05, 0.05) for _ in range(3)]

    for _ in range(epochs):
        gradients = [0.0, 0.0, 0.0]
        # 每个 epoch 都只遍历 train_rows，验证与测试标签不参与梯度更新。
        for x1, x2, label in train_rows:
            probability = sigmoid(weights[0] * x1 + weights[1] * x2 + weights[2])
            error = probability - label
            gradients[0] += error * x1
            gradients[1] += error * x2
            gradients[2] += error
        for position in range(3):
            weights[position] -= learning_rate * gradients[position] / len(train_rows)

    return {
        "seed": seed,
        "status": "completed",
        "validation": evaluate(validation_rows, weights),
        "test": evaluate(test_rows, weights),
        "weights": weights,
    }


def summarize(runs: list[dict], split: str, metric: str) -> dict[str, float]:
    """汇总全部预先计划的运行，不挑选单个最好 seed。"""
    values = [run[split][metric] for run in runs]
    return {
        "mean": statistics.fmean(values),
        "population_std": statistics.pstdev(values),
        "minimum": min(values),
        "maximum": max(values),
    }


def prepare_output(path: Path) -> None:
    """拒绝覆盖旧目录，使每次运行都有独立证据位置。"""
    if path.exists() and any(path.iterdir()):
        raise FileExistsError(f"输出目录非空，拒绝覆盖：{path}")
    path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    prepare_output(args.output_dir)

    train_rows, validation_rows, test_rows = build_dataset()
    runs = [
        train_once(
            train_rows,
            validation_rows,
            test_rows,
            config["learning_rate"],
            config["epochs"],
            seed,
        )
        for seed in config["seeds"]
    ]

    metrics = {
        "experiment_id": config["experiment_id"],
        "status": "completed",
        "dataset": {
            "type": "deterministic synthetic binary classification",
            "train_samples": len(train_rows),
            "validation_samples": len(validation_rows),
            "test_samples": len(test_rows),
        },
        "runs": runs,
        "summary": {
            "validation_accuracy": summarize(runs, "validation", "accuracy"),
            "validation_loss": summarize(runs, "validation", "loss"),
            "test_accuracy": summarize(runs, "test", "accuracy"),
            "test_loss": summarize(runs, "test", "loss"),
        },
        "claim_boundary": "教学演练；不能作为真实任务或方法优越性的证据。",
    }
    command = " ".join(shlex.quote(part) for part in sys.argv)
    environment = {
        "python": sys.version,
        "platform": platform.platform(),
        "command": command,
    }

    (args.output_dir / "config.snapshot.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "environment.json").write_text(
        json.dumps(environment, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    log_lines = [
        f"experiment_id={config['experiment_id']}",
        f"command={command}",
        f"planned_seeds={config['seeds']}",
    ]
    log_lines.extend(
        f"seed={run['seed']} status={run['status']} "
        f"val_accuracy={run['validation']['accuracy']:.6f} "
        f"test_accuracy={run['test']['accuracy']:.6f}"
        for run in runs
    )
    log_lines.append(
        "test_accuracy_mean="
        f"{metrics['summary']['test_accuracy']['mean']:.6f} "
        "test_accuracy_population_std="
        f"{metrics['summary']['test_accuracy']['population_std']:.6f}"
    )
    (args.output_dir / "run.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    print("\n".join(log_lines))


if __name__ == "__main__":
    configure_stdio()
    main()
