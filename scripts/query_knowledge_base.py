"""按问题、阶段和启用时机查询零基础科研知识库。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE_PATH = REPOSITORY_ROOT / "knowledge-base.json"


def configure_stdio() -> None:
    """统一 Windows 与 CI 的中文输出编码。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="查询 AI 科研入门方法与工具知识库")
    parser.add_argument("--list", action="store_true", help="列出全部知识卡")
    parser.add_argument("--query", help="按问题、方法、工具或边界搜索")
    parser.add_argument("--level", choices=["L0", "L1", "L2", "L3"], help="筛选能力等级")
    parser.add_argument(
        "--activation",
        choices=["立即", "规模增长后", "专项研究"],
        help="筛选启用时机",
    )
    args = parser.parse_args()
    if not any([args.list, args.query, args.level, args.activation]):
        parser.error("至少提供 --list、--query、--level 或 --activation 之一")
    return args


def load_entries() -> list[dict[str, Any]]:
    """读取结构化知识库；格式错误直接失败，避免静默返回空结果。"""
    data = json.loads(KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8"))
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise ValueError("knowledge-base.json 缺少 entries 列表")
    return entries


def searchable_text(entry: dict[str, Any]) -> str:
    """将知识卡中允许检索的字段合并为统一文本。"""
    fields = [
        entry["id"],
        entry["question"],
        entry["stage"],
        entry["method"],
        entry["minimum_output"],
        entry["verification"],
        entry["boundary"],
        " ".join(entry["tool_ids"]),
    ]
    return "\n".join(fields).casefold()


def matches(entry: dict[str, Any], args: argparse.Namespace) -> bool:
    """组合查询条件；不同条件之间使用 AND。"""
    if args.query and args.query.casefold() not in searchable_text(entry):
        return False
    if args.level and args.level not in entry["level"]:
        return False
    if args.activation and args.activation != entry["activation"]:
        return False
    return True


def print_entry(entry: dict[str, Any]) -> None:
    """输出适合终端阅读和复制到任务卡的紧凑结果。"""
    print(f"[{entry['id']}] {entry['question']}")
    print(f"阶段：{entry['stage']} | 等级：{', '.join(entry['level'])} | 启用：{entry['activation']}")
    print(f"方法：{entry['method']}")
    print(f"最小产物：{entry['minimum_output']}")
    print(f"验证：{entry['verification']}")
    print(f"边界：{entry['boundary']}")
    print(f"工具 ID：{', '.join(entry['tool_ids'])}")
    print(f"仓库指南：{entry['guide']}")
    print(f"官方来源：{', '.join(entry['source_urls'])}")


def main() -> None:
    args = parse_args()
    entries = [entry for entry in load_entries() if matches(entry, args)]
    if not entries:
        raise SystemExit("没有匹配的知识卡；请缩短关键词或调整等级/启用时机。")
    for index, entry in enumerate(entries):
        if index:
            print()
        print_entry(entry)


if __name__ == "__main__":
    configure_stdio()
    main()
