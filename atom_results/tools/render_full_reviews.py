#!/usr/bin/env python3
"""Render manually reviewed canonical JSONL records into English and Chinese Markdown."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


RESULTS = Path(__file__).resolve().parents[1]
MANIFEST = RESULTS / "full_manifest.jsonl"
REVIEWS = RESULTS / "full_reviews"
OUT_EN = RESULTS / "full_en"
OUT_ZH = RESULTS / "full_zh"


def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> None:
    manifest = read_jsonl(MANIFEST)
    source_for_index = {row["global_index"]: row["source_file"] for row in manifest}
    expected_by_source = defaultdict(list)
    for row in manifest:
        expected_by_source[row["source_file"]].append(row["global_index"])

    reviewed = {}
    for path in sorted(REVIEWS.glob("*.jsonl")):
        for row in read_jsonl(path):
            index = row["global_index"]
            if index in reviewed:
                raise RuntimeError(f"Duplicate reviewed global_index: {index}")
            reviewed[index] = row

    OUT_EN.mkdir(parents=True, exist_ok=True)
    OUT_ZH.mkdir(parents=True, exist_ok=True)

    rendered = 0
    for source, indices in expected_by_source.items():
        if any(index not in reviewed for index in indices):
            continue

        stem = Path(source).stem
        en = [
            f"# Full Atomic Instruction Results — {source} — English\n",
            f"- Source records: {len(indices)}\n",
            "- All atomic criteria were manually reviewed under `atom_results/README.md`.\n",
            "- The source clip-start timestamp is omitted from atomic criteria; later timestamps are relative to the clip start.\n",
        ]
        zh = [
            f"# 全量编辑指令原子化结果——{source}——中文审阅版\n",
            f"- 源记录数：{len(indices)}\n",
            "- 所有原子判定句均依据 `atom_results/README.md` 逐条人工审核。\n",
            "- 原子判定句省略作为截取起点的绝对时间；后续时间点均已换算为片段内相对时间。\n",
        ]

        for source_number, index in enumerate(indices, start=1):
            row = reviewed[index]
            status_en = "Accepted (single-item fallback)" if row["mode"] == "fallback" else "Accepted"
            status_zh = "接受（单条保底）" if row["mode"] == "fallback" else "接受"

            en.extend(
                [
                    f"\n## {source_number:03d} — `{row['edit_id']}`\n",
                    f"**Original instruction:** {row['original_en']}\n",
                    f"**Status:** {status_en}\n",
                    "**Atomic criteria:**\n",
                ]
            )
            en.extend(f"{number}. {atom}\n" for number, atom in enumerate(row["atoms_en"], start=1))

            zh.extend(
                [
                    f"\n## {source_number:03d} — `{row['edit_id']}`\n",
                    f"**原始英文指令：** {row['original_en']}\n",
                    f"**中文翻译：** {row['original_zh']}\n",
                    f"**状态：** {status_zh}\n",
                    "**原子化判定句：**\n",
                ]
            )
            zh.extend(f"{number}. {atom}\n" for number, atom in enumerate(row["atoms_zh"], start=1))

        (OUT_EN / f"{stem}_atomized_en.md").write_text("\n".join(en), encoding="utf-8")
        (OUT_ZH / f"{stem}_atomized_zh.md").write_text("\n".join(zh), encoding="utf-8")
        rendered += 1

    print(f"rendered {rendered} complete source files")


if __name__ == "__main__":
    main()
