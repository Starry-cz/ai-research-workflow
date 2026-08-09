"""按日期审计 tools.yml 中的外部 URL，不把动态结果当成永久质量结论。"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import socket
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "ai-research-workflow-url-audit/1.0 (+https://github.com/Starry-cz/ai-research-workflow)"


@dataclass(frozen=True)
class UrlTarget:
    tool_id: str
    field: str
    url: str


@dataclass(frozen=True)
class UrlResult:
    tool_id: str
    field: str
    url: str
    category: str
    status_code: int | None
    final_url: str | None
    detail: str


def configure_stdio() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="动态检查 tools.yml 的外部 URL")
    parser.add_argument("--timeout", type=float, default=12.0, help="单个请求超时秒数")
    parser.add_argument("--workers", type=int, default=8, help="并发请求数量")
    return parser.parse_args()


def load_targets() -> list[UrlTarget]:
    targets: list[UrlTarget] = []
    current_id: str | None = None
    for line in (REPOSITORY_ROOT / "tools.yml").read_text(encoding="utf-8").splitlines():
        if line.startswith("  - id: "):
            current_id = line.removeprefix("  - id: ").strip()
            continue
        if current_id is None:
            continue
        for field in ("url", "web_url"):
            prefix = f"    {field}: "
            if line.startswith(prefix):
                targets.append(UrlTarget(current_id, field, line.removeprefix(prefix).strip()))
    return targets


def classify_status(status_code: int) -> str:
    if 200 <= status_code < 400:
        return "reachable"
    if status_code in {401, 403, 429}:
        return "restricted"
    if status_code in {404, 410}:
        return "not_found"
    if 500 <= status_code < 600:
        return "transient"
    return "attention"


def check_url(target: UrlTarget, timeout: float) -> UrlResult:
    # 只读取一个字节，确认入口响应与最终地址，不下载页面正文。
    request = urllib.request.Request(
        target.url,
        headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response.read(1)
            status_code = response.status
            return UrlResult(
                target.tool_id,
                target.field,
                target.url,
                classify_status(status_code),
                status_code,
                response.geturl(),
                "",
            )
    except urllib.error.HTTPError as error:
        return UrlResult(
            target.tool_id,
            target.field,
            target.url,
            classify_status(error.code),
            error.code,
            error.geturl(),
            error.reason if isinstance(error.reason, str) else repr(error.reason),
        )
    except (urllib.error.URLError, TimeoutError, socket.timeout, ssl.SSLError) as error:
        return UrlResult(
            target.tool_id,
            target.field,
            target.url,
            "network_error",
            None,
            None,
            str(error),
        )


def main() -> None:
    args = parse_args()
    targets = load_targets()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(check_url, target, args.timeout) for target in targets]
        results = [future.result() for future in futures]

    results.sort(key=lambda item: (item.category, item.tool_id, item.field))
    payload = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "timeout_seconds": args.timeout,
        "target_count": len(targets),
        "category_counts": {
            category: sum(result.category == category for result in results)
            for category in sorted({result.category for result in results})
        },
        "results": [asdict(result) for result in results],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    configure_stdio()
    main()
