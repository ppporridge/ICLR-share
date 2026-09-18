#!/usr/bin/env python3
"""Propose two-atom splits for explicit visual changes with completion deadlines."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/home/zhou/ICLR-share/atom_results")
REVIEWS = ROOT / "full_reviews"
OUT = ROOT / "resplit_review" / "timed_change_proposals.jsonl"
AUDIT = ROOT / "resplit_review" / "timed_change_proposals_audit.tsv"

ALLOWED = {"change", "transform", "render", "shift", "apply", "convert"}
LABELS = {
    "change": ("change", "变化"),
    "transform": ("transformation", "转换"),
    "render": ("rendering", "渲染"),
    "shift": ("change", "变化"),
    "apply": ("application", "效果应用"),
    "convert": ("conversion", "转换"),
}
TIME_EN_RE = re.compile(
    r" within ((?:the next )?(?:[0-9.]+|one|two|three|four|five|six|seven|eight|nine|ten) seconds?)\?$"
)
TIME_ZH_RE = re.compile(r"在\s*([0-9.]+)\s*秒内")
START_RE = re.compile(r"^(?:Starting at|At) [0-9.]+ seconds, ", re.I)


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    rows: list[dict] = []
    for path in sorted(REVIEWS.glob("*.jsonl")):
        rows.extend(load(path))

    proposals: list[dict] = []
    audit_lines = ["global_index\tedit_id\tverb\toriginal_en\tresult_zh\ttime_zh"]
    for row in sorted(rows, key=lambda item: item["global_index"]):
        if row.get("mode") != "single":
            continue
        instruction = START_RE.sub("", row["original_en"])
        verb = instruction.split(maxsplit=1)[0].lower()
        if verb not in ALLOWED:
            continue

        atom_en = row["atoms_en"][0]
        atom_zh = row["atoms_zh"][0]
        match_en = TIME_EN_RE.search(atom_en)
        match_zh = TIME_ZH_RE.search(atom_zh)
        if not match_en or not match_zh:
            continue

        base_en = TIME_EN_RE.sub("?", atom_en)
        base_zh = TIME_ZH_RE.sub("", atom_zh, count=1)
        time_en = match_en.group(1)
        time_zh = match_zh.group(1)
        label_en, label_zh = LABELS[verb]
        proposal = {
            "global_index": row["global_index"],
            "decision": "split",
            "source": "codex_rereview_timed_change",
            "atoms_en": [base_en, f"Is the {label_en} completed within {time_en}?"],
            "atoms_zh": [base_zh, f"该{label_zh}是否在 {time_zh} 秒内完成？"],
        }
        proposals.append(proposal)
        audit_lines.append(
            "\t".join(
                [
                    str(row["global_index"]),
                    row["edit_id"],
                    verb,
                    row["original_en"].replace("\t", " "),
                    base_zh,
                    proposal["atoms_zh"][1],
                ]
            )
        )

    OUT.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in proposals),
        encoding="utf-8",
    )
    AUDIT.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")
    print(f"proposals={len(proposals)}")
    print(f"jsonl={OUT}")
    print(f"audit={AUDIT}")


if __name__ == "__main__":
    main()
