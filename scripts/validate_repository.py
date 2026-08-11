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
TOOL_START = re.compile(r"^  - id:\s*([a-z0-9][a-z0-9-]*)\s*$")
TOOL_FIELD = re.compile(r"^    ([a-z][a-z0-9_]*):\s*(.+?)\s*$")
LITERATURE_TOOL_IDS = {
    "ai-arxiv-portal",
    "ai-conferences-info",
    "arxiv",
    "best-papers-top-venues",
    "cool-papers",
    "cosmos-paper",
    "cv-paper-portal",
    "dblp",
    "google-scholar",
    "huggingface-trending-papers",
    "openreview",
    "paper-copilot",
}
ALLOWED_RESEARCH_ROLES = {
    "bibliographic-record",
    "citation-tracing",
    "discovery",
    "primary-paper",
    "review-context",
    "review-record",
    "trend-monitoring",
    "venue-index",
    "version-history",
}
CURATED_GITHUB_RESOURCE_IDS = {
    "annotated-deep-learning-paper-implementations",
    "ars",
    "autoresearchclaw",
    "ccf-figure",
    "cookiecutter-data-science",
    "cs-self-learning",
    "d2l-zh",
    "how-to-search-and-read-a-paper",
    "learning-research",
    "lightning-hydra-template",
    "made-with-ml",
    "mathematics-for-machine-learning",
    "missing-semester",
    "ml-for-beginners",
    "nn-zero-to-hero",
    "ossu-computer-science",
    "papers-we-love",
    "pumpkin-book",
    "pytorch-deep-learning",
    "releasing-research-code",
    "supervisor-skills",
    "tuning-playbook",
}
ALLOWED_PRIMARY_LANGUAGES = {"en", "multilingual", "zh"}


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

    quick_start_heading = "## 第一次来：默认从这里开始"
    toc_heading = "## 目录"
    if quick_start_heading not in lines:
        raise ValidationError("README.md 缺少零基础默认入口")
    if toc_heading not in lines:
        raise ValidationError("README.md 缺少目录")

    quick_start_index = lines.index(quick_start_heading)
    toc_index = lines.index(toc_heading)
    if quick_start_index >= toc_index:
        raise ValidationError("零基础默认入口必须出现在目录之前")

    # 首页入口必须在首屏给出起点、产物、时间、完成标志和求助出口。
    quick_start_text = "\n".join(lines[quick_start_index:toc_index])
    required_fragments = {
        "准备检查表": "零基础准备检查表",
        "L0 指南": "L0 工具链指南",
        "可运行演练": "第一次可审计实验演练",
        "时间预期": "建议时间",
        "完成标志": "完成标志",
        "求助出口": "调试与求助卡",
    }
    missing_fragments = [
        label for label, fragment in required_fragments.items() if fragment not in quick_start_text
    ]
    if missing_fragments:
        raise ValidationError(f"零基础默认入口缺少：{missing_fragments}")


def validate_beginner_feedback_form() -> None:
    """确保首次使用反馈保持低负担，并与正式文档问题表单分工。"""
    path = REPOSITORY_ROOT / ".github" / "ISSUE_TEMPLATE" / "beginner-first-use.yml"
    if not path.exists():
        raise ValidationError("缺少零基础首次使用反馈表单")

    text = path.read_text(encoding="utf-8")
    required_fragments = {
        "起始状态": "id: starting_point",
        "任务结果": "id: outcome",
        "首次动作": "id: first_action",
        "首次卡点": "id: first_friction",
        "帮助来源": "id: help_source",
        "公开安全提示": "GitHub Issue 是公开页面",
        "不要求解决方案": "不要求你提出解决方案",
    }
    missing = [label for label, fragment in required_fragments.items() if fragment not in text]
    if missing:
        raise ValidationError(f"零基础首次使用反馈表单缺少：{missing}")

    # 正式文档改进需要证据；首次体验只收集行为，不能把维护责任转给新手。
    forbidden_required_ids = {"expected", "evidence"}
    for field_id in forbidden_required_ids:
        if re.search(
            rf"id:\s*{field_id}\b[\s\S]*?validations:\s*\n\s+required:\s*true",
            text,
        ):
            raise ValidationError(f"零基础首次使用反馈不应必填 {field_id}")


def validate_first_drill_progression() -> None:
    """保证首次 PASS 先于公平比较，且不会重新创建第二个环境。"""
    readme_path = REPOSITORY_ROOT / "examples" / "first-workflow-drill" / "README.md"
    verifier_path = readme_path.parent / "verify_first_run.py"
    workflow_path = REPOSITORY_ROOT / ".github" / "workflows" / "first-workflow-drill.yml"
    require_files = [readme_path, verifier_path, workflow_path]
    missing_files = [str(path.relative_to(REPOSITORY_ROOT)) for path in require_files if not path.exists()]
    if missing_files:
        raise ValidationError(f"首次运行分层缺少文件：{missing_files}")

    text = readme_path.read_text(encoding="utf-8")
    first_heading = "## 第一次只完成到第一个 PASS"
    second_heading = "## 第二轮：从一次运行升级到公平比较"
    if first_heading not in text or second_heading not in text:
        raise ValidationError("第一次演练缺少首次 PASS 或第二轮比较入口")
    first_start = text.index(first_heading)
    second_start = text.index(second_heading)
    if first_start >= second_start:
        raise ValidationError("首次 PASS 必须出现在三组公平比较之前")

    first_section = text[first_start:second_start]
    required_fragments = [
        "verify_first_run.py",
        "config.snapshot.json",
        "environment.json",
        "metrics.json",
        "run.log",
        "不要在本目录再创建第二个环境",
    ]
    missing_fragments = [fragment for fragment in required_fragments if fragment not in first_section]
    if missing_fragments:
        raise ValidationError(f"首次 PASS 路径缺少：{missing_fragments}")
    if "baseline.json" in first_section or "candidate.json" in first_section:
        raise ValidationError("首次 PASS 路径不应提前运行 baseline 或 candidate")

    workflow_text = workflow_path.read_text(encoding="utf-8")
    if "python verify_first_run.py --run-dir results/ci-debug" not in workflow_text:
        raise ValidationError("First workflow drill CI 缺少首次单配置验收")


def validate_l0_git_boundary() -> None:
    """保证首次 Git 练习不修改全局身份，也不暗示可推送到上游仓库。"""
    path = REPOSITORY_ROOT / "docs" / "L0_TOOLCHAIN_START.md"
    text = path.read_text(encoding="utf-8")
    required_fragments = {
        "远程所有者检查": "git remote -v",
        "个人练习分支": "git switch -c learning/first-run",
        "仓库级姓名": 'git config --local user.name "你的显示名称"',
        "仓库级邮箱": 'git config --local user.email "你确认用于提交的邮箱"',
        "精确暂存": "git add environment/README.md",
        "暂存区复查": "git diff --cached",
        "本地提交边界": "这个 commit 只存在于你的电脑",
        "禁止误推上游": "不要运行 `git push origin main`",
        "后续贡献入口": "先在 GitHub fork 到自己的账号",
    }
    missing = [label for label, fragment in required_fragments.items() if fragment not in text]
    if missing:
        raise ValidationError(f"L0 Git 所有权边界缺少：{missing}")

    forbidden_fragments = {
        "全局姓名修改": "git config --global user.name",
        "全局邮箱修改": "git config --global user.email",
        "全局默认分支修改": "git config --global init.defaultBranch",
        "宽范围暂存": "git add README.md .gitignore environment",
    }
    present = [label for label, fragment in forbidden_fragments.items() if fragment in text]
    if present:
        raise ValidationError(f"L0 Git 练习仍包含高影响命令：{present}")


def validate_beginner_glossary() -> None:
    """确保零基础术语入口可发现，且每个核心词同时给出行动与结论边界。"""
    glossary_path = REPOSITORY_ROOT / "docs" / "BEGINNER_GLOSSARY.md"
    if not glossary_path.exists():
        raise ValidationError("缺少零基础默认路径术语速查")

    glossary_text = glossary_path.read_text(encoding="utf-8")
    required_terms = [
        "### L0、L1、L2、L3",
        "### PASS",
        "### 仓库（repository / repo）",
        "### origin 与 upstream",
        "### commit",
        "### Python 解释器",
        "### 虚拟环境与 `.venv`",
        "### 运行与 `run_id`",
        "### 随机种子（seed）",
        "### 基线与候选（baseline / candidate）",
        "### CI 与 GitHub Actions",
    ]
    missing_terms = [term for term in required_terms if term not in glossary_text]
    if missing_terms:
        raise ValidationError(f"零基础术语速查缺少核心词：{missing_terms}")

    entry_count = len(re.findall(r"^### ", glossary_text, flags=re.MULTILINE))
    action_count = glossary_text.count("- **现在要做什么**：")
    boundary_count = glossary_text.count("- **不能推出什么**：")
    if action_count != entry_count or boundary_count != entry_count:
        raise ValidationError(
            "术语条目必须逐项包含“现在要做什么”和“不能推出什么”"
        )

    forbidden_sources = ["小红书认为", "知乎认为", "AI 认为", "搜索摘要认为"]
    present_sources = [source for source in forbidden_sources if source in glossary_text]
    if present_sources:
        raise ValidationError(f"术语定义不应以经验平台或 AI 作为规范来源：{present_sources}")

    readme_path = REPOSITORY_ROOT / "README.md"
    readme_lines = readme_path.read_text(encoding="utf-8").splitlines()
    quick_start = readme_lines.index("## 第一次来：默认从这里开始")
    toc = readme_lines.index("## 目录")
    quick_start_text = "\n".join(readme_lines[quick_start:toc])
    if "(docs/BEGINNER_GLOSSARY.md)" not in quick_start_text:
        raise ValidationError("首页默认入口缺少零基础术语速查链接")


def validate_index(index_path: Path, members: list[Path], label: str) -> None:
    index_text = index_path.read_text(encoding="utf-8")
    missing = [member.name for member in members if f"({member.name})" not in index_text]
    if missing:
        raise ValidationError(f"{label}缺少条目：{missing}")


def validate_tools_catalog() -> int:
    """按 tools.yml 当前的受限目录结构检查条目，不引入 YAML 依赖。"""
    path = REPOSITORY_ROOT / "tools.yml"
    text = path.read_text(encoding="utf-8")
    if "star_snapshot:" in text:
        raise ValidationError("tools.yml 不应保存动态 Star 快照")
    if not re.search(r'^version:\s*\d+\s*$', text, flags=re.MULTILINE):
        raise ValidationError("tools.yml 缺少整数 version")
    if not re.search(r'^last_verified:\s*"\d{4}-\d{2}-\d{2}"\s*$', text, flags=re.MULTILINE):
        raise ValidationError("tools.yml 缺少 YYYY-MM-DD 格式的 last_verified")

    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in text.splitlines():
        start_match = TOOL_START.match(line)
        if start_match:
            if current is not None:
                entries.append(current)
            current = {"id": start_match.group(1)}
            continue
        field_match = TOOL_FIELD.match(line)
        if current is not None and field_match:
            current[field_match.group(1)] = field_match.group(2)
    if current is not None:
        entries.append(current)

    require_fields = {
        "id",
        "name",
        "name_zh",
        "stage",
        "level",
        "type",
        "url",
        "summary",
        "recommended_output",
        "caveat",
    }
    ids: set[str] = set()
    urls: set[str] = set()
    for entry in entries:
        missing = sorted(require_fields - set(entry))
        if missing:
            raise ValidationError(f"tools.yml 条目 {entry['id']} 缺少字段：{missing}")
        if entry["id"] in ids:
            raise ValidationError(f"tools.yml 出现重复 id：{entry['id']}")
        if entry["url"] in urls:
            raise ValidationError(f"tools.yml 出现重复 url：{entry['url']}")
        if not entry["url"].startswith("https://"):
            raise ValidationError(f"tools.yml 条目 {entry['id']} 的 url 不是 HTTPS")
        levels = re.findall(r"L[0-3]", entry["level"])
        if not levels or entry["level"] != f"[{', '.join(levels)}]":
            raise ValidationError(f"tools.yml 条目 {entry['id']} 的 level 格式无效")
        if entry["id"] in LITERATURE_TOOL_IDS:
            role_field = entry.get("research_role")
            if role_field is None:
                raise ValidationError(f"tools.yml 文献条目 {entry['id']} 缺少 research_role")
            # 固定列表格式，避免后续筛选器把同一角色解析为不同值。
            roles = [role.strip() for role in role_field.strip("[]").split(",")]
            if not roles or role_field != f"[{', '.join(roles)}]":
                raise ValidationError(f"tools.yml 条目 {entry['id']} 的 research_role 格式无效")
            unknown_roles = sorted(set(roles) - ALLOWED_RESEARCH_ROLES)
            if unknown_roles:
                raise ValidationError(
                    f"tools.yml 条目 {entry['id']} 使用未知 research_role：{unknown_roles}"
                )
        if entry["id"] in CURATED_GITHUB_RESOURCE_IDS:
            resource_fields = {"primary_language", "entry_requirement"}
            missing_resource_fields = sorted(resource_fields - set(entry))
            if missing_resource_fields:
                raise ValidationError(
                    f"GitHub 入门资源 {entry['id']} 缺少进入成本字段：{missing_resource_fields}"
                )
            languages = [language.strip() for language in entry["primary_language"].strip("[]").split(",")]
            if entry["primary_language"] != f"[{', '.join(languages)}]":
                raise ValidationError(f"tools.yml 条目 {entry['id']} 的 primary_language 格式无效")
            unknown_languages = sorted(set(languages) - ALLOWED_PRIMARY_LANGUAGES)
            if unknown_languages:
                raise ValidationError(
                    f"tools.yml 条目 {entry['id']} 使用未知 primary_language：{unknown_languages}"
                )
            if len(entry["entry_requirement"]) < 20:
                raise ValidationError(f"tools.yml 条目 {entry['id']} 的 entry_requirement 过短")
        ids.add(entry["id"])
        urls.add(entry["url"])
    if not entries:
        raise ValidationError("tools.yml 没有工具条目")
    missing_curated_resources = sorted(CURATED_GITHUB_RESOURCE_IDS - ids)
    if missing_curated_resources:
        raise ValidationError(f"tools.yml 缺少 GitHub 入门资源：{missing_curated_resources}")

    # 人读目录与机器目录必须同步，避免新手点开后才发现语言、账号或算力门槛。
    catalog_text = (REPOSITORY_ROOT / "docs" / "GITHUB_RESOURCE_CATALOG.md").read_text(encoding="utf-8")
    entry_cost_count = catalog_text.count("**进入成本**：")
    if entry_cost_count != len(CURATED_GITHUB_RESOURCE_IDS):
        raise ValidationError(
            f"GitHub 资源目录有 {entry_cost_count} 条进入成本说明，预期 {len(CURATED_GITHUB_RESOURCE_IDS)} 条"
        )
    missing_catalog_urls = [
        entry["url"]
        for entry in entries
        if entry["id"] in CURATED_GITHUB_RESOURCE_IDS and entry["url"] not in catalog_text
    ]
    if missing_catalog_urls:
        raise ValidationError(f"GitHub 资源目录缺少 tools.yml 条目：{missing_catalog_urls}")
    return len(entries)


def main() -> None:
    markdown_files = sorted(REPOSITORY_ROOT.rglob("*.md"))
    validate_links(markdown_files)
    validate_fences(markdown_files)
    validate_root_readme()
    validate_beginner_feedback_form()
    validate_first_drill_progression()
    validate_l0_git_boundary()
    validate_beginner_glossary()

    docs = sorted(path for path in (REPOSITORY_ROOT / "docs").glob("*.md") if path.name != "README.md")
    templates = sorted(
        path for path in (REPOSITORY_ROOT / "templates").glob("*.md") if path.name != "README.md"
    )
    validate_index(REPOSITORY_ROOT / "docs" / "README.md", docs, "docs/README.md ")
    validate_index(REPOSITORY_ROOT / "templates" / "README.md", templates, "templates/README.md ")
    tool_count = validate_tools_catalog()

    print(f"PASS：已检查 {len(markdown_files)} 个 Markdown 文件。")
    print(
        f"相对链接与锚点、代码块、README 约束、首次使用反馈、演练分层、L0 Git 边界、零基础术语、GitHub 资源进入成本、两类索引和 {tool_count} 个工具条目均通过。"
    )


if __name__ == "__main__":
    configure_stdio()
    try:
        main()
    except ValidationError as error:
        print(f"FAIL：{error}", file=sys.stderr)
        raise SystemExit(1) from error
