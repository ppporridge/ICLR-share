#!/usr/bin/env python3
"""Validate and render the 100 single-to-multi review candidates."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path("/home/zhou/ICLR-share/atom_results")
REVIEWS_DIR = ROOT / "full_reviews"
CANDIDATES_PATH = ROOT / "resplit_review" / "candidates_100.jsonl"
OUTPUT_PATH = ROOT / "resplit_review" / "single_to_multi_candidates_100_zh.md"


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: JSON 解析失败: {exc}") from exc
    return rows


def main() -> None:
    review_rows: list[dict] = []
    for path in sorted(REVIEWS_DIR.glob("*.jsonl")):
        review_rows.extend(load_jsonl(path))
    reviews = {row["global_index"]: row for row in review_rows}
    if len(reviews) != 3000:
        raise ValueError(f"正式结果应有 3000 条，实际读取到 {len(reviews)} 条")

    candidates = load_jsonl(CANDIDATES_PATH)
    if len(candidates) != 100:
        raise ValueError(f"候选应有 100 条，实际读取到 {len(candidates)} 条")

    ranks = [row["rank"] for row in candidates]
    if ranks != list(range(1, 101)):
        raise ValueError("候选 rank 必须严格连续为 1—100")

    indexes = [row["global_index"] for row in candidates]
    if len(indexes) != len(set(indexes)):
        raise ValueError("候选 global_index 存在重复")

    source_counts = Counter((index - 1) // 300 + 1 for index in indexes)
    if source_counts != Counter({bucket: 10 for bucket in range(1, 11)}):
        raise ValueError(f"每个来源应抽取 10 条，实际分布为 {dict(source_counts)}")

    for candidate in candidates:
        index = candidate["global_index"]
        if index not in reviews:
            raise ValueError(f"找不到正式结果 global_index={index}")
        review = reviews[index]
        if review.get("mode") != "single" or len(review.get("atoms_zh", [])) != 1:
            raise ValueError(f"global_index={index} 不是常规单项结果")
        atoms = candidate.get("proposed_atoms_zh")
        if not isinstance(atoms, list) or not 2 <= len(atoms) <= 5:
            raise ValueError(f"global_index={index} 的建议拆分必须包含 2—5 个原子问题")
        if any(not isinstance(atom, str) or not atom.strip() for atom in atoms):
            raise ValueError(f"global_index={index} 含空白建议问题")
        if not candidate.get("mechanism", "").strip():
            raise ValueError(f"global_index={index} 缺少候选拆分机制")

    lines = [
        "# 单项判定句二次拆分候选（100 条）",
        "",
        "> 本文档用于收集拆分规则反馈；当前 3000 条正式结果尚未因本轮候选而改动。",
        "",
        "## 填写说明",
        "",
        "- 100 条均来自当前的常规单项结果，十个来源各抽取 10 条。",
        "- 请逐条勾选一个结论，并在“你的评语”下写明判断依据或修改方案。",
        "- 重点请判断：建议拆出的每个问题能否独立通过画面回答“是/否”，以及拆分是否遗漏原动作、结果、时序或范围。",
        "- 你可以直接修改建议句；若认为仍应保持单项，也请说明哪些成分不能独立判定。",
        "",
    ]

    for candidate in candidates:
        review = reviews[candidate["global_index"]]
        rank = candidate["rank"]
        lines.extend(
            [
                "---",
                "",
                f"## {rank:03d} / 100 — 全局 {review['global_index']:04d} — `{review['edit_id']}`",
                "",
                f"**原始英文指令：** {review['original_en']}",
                "",
                f"**中文翻译：** {review['original_zh']}",
                "",
                "**当前单项判定句：**",
                "",
                f"1. {review['atoms_zh'][0]}",
                "",
                f"**候选拆分机制：** {candidate['mechanism']}",
                "",
                "**建议拆分：**",
                "",
            ]
        )
        for atom_number, atom in enumerate(candidate["proposed_atoms_zh"], 1):
            lines.append(f"{atom_number}. {atom}")
        lines.extend(
            [
                "",
                "**你的结论（勾选一项）：**",
                "",
                "- [ ] 保留单项",
                "- [ ] 采用建议拆分",
                "- [ ] 调整后拆分",
                "- [ ] 不适合／其他",
                "",
                "**你的评语：**",
                "",
                "> ",
                "",
            ]
        )

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    atom_counts = Counter(len(row["proposed_atoms_zh"]) for row in candidates)
    print(f"validated_candidates={len(candidates)}")
    print(f"source_distribution={dict(sorted(source_counts.items()))}")
    print(f"proposed_atom_counts={dict(sorted(atom_counts.items()))}")
    print(f"output={OUTPUT_PATH}")


if __name__ == "__main__":
    main()
