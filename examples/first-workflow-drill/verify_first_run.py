"""只验收第一次单配置运行，不提前要求完成方法比较。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from verify import VerificationError, configure_stdio, require, verify_directory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="验收第一次单配置演练输出")
    parser.add_argument("--run-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config, metrics = verify_directory(args.run_dir, "首次运行")

    # 首次成功只使用一个 seed，避免把完整比较协议塞进入门第一步。
    require(len(config["seeds"]) == 1, "首次运行配置必须只包含一个 seed")
    run = metrics["runs"][0]
    print("PASS：首次运行的配置、环境、指标和日志完整，计划运行均为 completed。")
    print(f"experiment_id={config['experiment_id']}")
    print(f"test_accuracy={run['test']['accuracy']:.6f}")
    print("下一步：先指出四项产物各自回答什么问题，再决定是否进入三组公平比较。")
    print("边界：本次 PASS 只证明一条教学运行可审计，不证明复现成功或方法更优。")


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except VerificationError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
