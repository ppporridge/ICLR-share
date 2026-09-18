#!/usr/bin/env python3
"""Propose result/deadline splits for the remaining explicit completion deadlines."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/home/zhou/ICLR-share/atom_results")
REVIEWS = ROOT / "full_reviews"
OUT = ROOT / "resplit_review" / "remaining_deadline_proposals.jsonl"
AUDIT = ROOT / "resplit_review" / "remaining_deadline_proposals_audit.tsv"
TIME_EN_RE = re.compile(
    r" within ((?:the next )?(?:[0-9.]+|one|two|three|four|five|six|seven|eight|nine|ten) seconds?)\?$"
)
TIME_ZH_RE = re.compile(r"在\s*([0-9.]+)\s*秒内")
START_RE = re.compile(r"^(?:(?:Starting|Beginning) at|At) [0-9.]+ seconds, ", re.I)

LABELS = {
    "make": ("result", "结果"),
    "remove": ("removal", "移除"),
    "zoom": ("zoom", "镜头变焦"),
    "move": ("movement", "移动"),
    "replace": ("replacement", "替换"),
    "slow": ("slowdown", "减速"),
    "add": ("addition", "添加"),
    "transition": ("transition", "转变"),
    "reduce": ("reduction", "降低"),
    "relight": ("relighting", "重新照明"),
    "darken": ("darkening", "变暗"),
    "give": ("change", "变化"),
    "develop": ("development", "形成"),
    "split": ("split", "分裂"),
    "tilt": ("tilt", "倾斜"),
    "merge": ("merge", "合并"),
    "freeze": ("freezing", "冻结"),
    "raise": ("raising", "升高"),
    "coat": ("coating", "涂覆"),
    "pan": ("pan", "平移"),
    "increase": ("increase", "增加"),
    "lower": ("lowering", "降低"),
    "bend": ("bend", "弯曲"),
    "illuminate": ("illumination", "照明"),
    "line": ("lining", "铺设"),
    "reverse": ("reversal", "反向处理"),
    "grade": ("grading", "调色"),
    "intensify": ("intensification", "增强"),
    "begin": ("action", "动作"),
    "rapidly": ("advance", "推进"),
    "cast": ("lighting", "光照添加"),
    "smoothly": ("zoom", "镜头变焦"),
    "thin": ("thinning", "变薄"),
    "rotate": ("rotation", "旋转"),
    "turn": ("turn", "转向"),
    "repair": ("repair", "修复"),
    "switch": ("switch", "切换"),
    "compress": ("compression", "压缩"),
    "beginning": ("camera movement", "镜头移动"),
    "dolly": ("camera movement", "镜头移动"),
    "advance": ("advance", "推进"),
}


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    rows: list[dict] = []
    for path in sorted(REVIEWS.glob("*.jsonl")):
        rows.extend(load(path))

    proposals: list[dict] = []
    audit = ["global_index\tedit_id\tverb\toriginal_en\tresult_zh\ttime_zh"]
    for row in sorted(rows, key=lambda item: item["global_index"]):
        if row.get("mode") != "single":
            continue
        atom_en = row["atoms_en"][0]
        atom_zh = row["atoms_zh"][0]
        match_en = TIME_EN_RE.search(atom_en)
        match_zh = TIME_ZH_RE.search(atom_zh)
        if not match_en or not match_zh:
            continue
        instruction = START_RE.sub("", row["original_en"])
        verb = instruction.split(maxsplit=1)[0].lower()
        if verb == "slow":
            # These records encode a delayed target state; they require a
            # record-specific time sentence rather than a generic slowdown deadline.
            continue
        if verb not in LABELS:
            raise ValueError(f"No label for verb={verb!r}, global_index={row['global_index']}")
        label_en, label_zh = LABELS[verb]
        base_en = TIME_EN_RE.sub("?", atom_en)
        base_zh = TIME_ZH_RE.sub("", atom_zh, count=1)
        time_en = match_en.group(1)
        time_zh = match_zh.group(1)
        if verb == "make":
            deadline_en = f"Is the result achieved within {time_en}?"
            deadline_zh = f"该结果是否在 {time_zh} 秒内实现？"
        else:
            deadline_en = f"Is the {label_en} completed within {time_en}?"
            deadline_zh = f"该{label_zh}是否在 {time_zh} 秒内完成？"
        proposal = {
            "global_index": row["global_index"],
            "decision": "split",
            "source": "codex_rereview_remaining_deadline",
            "atoms_en": [base_en, deadline_en],
            "atoms_zh": [base_zh, deadline_zh],
        }
        proposals.append(proposal)
        audit.append(
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
    AUDIT.write_text("\n".join(audit) + "\n", encoding="utf-8")
    print(f"proposals={len(proposals)}")


if __name__ == "__main__":
    main()
