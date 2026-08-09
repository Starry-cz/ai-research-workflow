"""验证文档链接、索引和根 README 的维护约束。"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


class ValidationError(RuntimeError):
    """表示仓库文档不满足已声明的维护规则。"""


def configure_stdio() -> None:
    """固定 UTF-8，保证 Windows 与 CI 输出一致。"""
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def github_slug(text: str) -> str:
    """生成适用于本仓库普通中英文标题的 GitHub 风格锚点。"""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text).casefold().strip()
    text = re.sub(r"[^\w\-\s\u4e00-\u9fff]", "", text)
    return re.sub(r"\s+", "-", text)


def heading_anchors(path: Path) -> set[str]:
    counts: dict[str, int] = {}
    anchors: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        base = github_slug(match.group(1))
        index = counts.get(base, 0)
        anchor = base if index == 0 else f"{base}-{index}"
        counts[base] = index + 1
        anchors.add(anchor)
    return anchors


def validate_links(markdown_files: list[Path]) -> None:
    anchor_cache = {path: heading_anchors(path) for path in markdown_files}
    errors: list[str] = []

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue

            path_text, separator, anchor = target.partition("#")
            target_path = source if not path_text else (source.parent / unquote(path_text)).resolve()
            if not target_path.exists():
                errors.append(f"{source.relative_to(REPOSITORY_ROOT)} -> 文件不存在：{target}")
                continue
            if separator and anchor:
                decoded_anchor = unquote(anchor).casefold()
                target_anchors = anchor_cache.get(target_path)
                if target_anchors is None and target_path.suffix.casefold() == ".md":
                    target_anchors = heading_anchors(target_path)
                    anchor_cache[target_path] = target_anchors
                if target_anchors is not None and decoded_anchor not in target_anchors:
                    errors.append(f"{source.relative_to(REPOSITORY_ROOT)} -> 锚点不存在：{target}")

    if errors:
        raise ValidationError("Markdown 链接检查失败：\n" + "\n".join(errors))


def validate_fences(markdown_files: list[Path]) -> None:
    errors: list[str] = []
    for path in markdown_files:
        open_fence: str | None = None
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = FENCE.match(line)
            if not match:
                continue
            marker = match.group(1)
            if open_fence is None:
                open_fence = marker
            elif marker == open_fence:
                open_fence = None
        if open_fence is not None:
            errors.append(str(path.relative_to(REPOSITORY_ROOT)))
    if errors:
        raise ValidationError("以下文件存在未闭合代码块：\n" + "\n".join(errors))


def validate_root_readme() -> None:
    path = REPOSITORY_ROOT / "README.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) > 600:
        raise ValidationError(f"README.md 有 {len(lines)} 行，超过 600 行维护上限")

    for line_number, line in enumerate(lines, start=1):
        if not (line.startswith("|") and line.endswith("|")):
            continue
        column_count = len(re.findall(r"(?<!\\)\|", line)) - 1
        if column_count > 2:
            raise ValidationError(f"README.md:{line_number} 表格有 {column_count} 列，超过两列")


def validate_index(index_path: Path, members: list[Path], label: str) -> None:
    index_text = index_path.read_text(encoding="utf-8")
    missing = [member.name for member in members if f"({member.name})" not in index_text]
    if missing:
        raise ValidationError(f"{label}缺少条目：{missing}")


def main() -> None:
    markdown_files = sorted(REPOSITORY_ROOT.rglob("*.md"))
    validate_links(markdown_files)
    validate_fences(markdown_files)
    validate_root_readme()

    docs = sorted(path for path in (REPOSITORY_ROOT / "docs").glob("*.md") if path.name != "README.md")
    templates = sorted(
        path for path in (REPOSITORY_ROOT / "templates").glob("*.md") if path.name != "README.md"
    )
    validate_index(REPOSITORY_ROOT / "docs" / "README.md", docs, "docs/README.md ")
    validate_index(REPOSITORY_ROOT / "templates" / "README.md", templates, "templates/README.md ")

    print(f"PASS：已检查 {len(markdown_files)} 个 Markdown 文件。")
    print("相对链接与锚点、代码块、README 两列表格与长度、指南索引、模板索引均通过。")


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except ValidationError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
