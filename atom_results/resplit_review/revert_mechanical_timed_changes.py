#!/usr/bin/env python3
"""Revert the mechanically proposed timed-change batch from canonical reviews."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/home/zhou/ICLR-share/atom_results")
REVIEWS_DIR = ROOT / "full_reviews"
PROPOSALS = ROOT / "resplit_review" / "timed_change_proposals.jsonl"


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def restore_atoms(proposal: dict) -> tuple[list[str], list[str]]:
    base_en, deadline_en = proposal["atoms_en"]
    base_zh, deadline_zh = proposal["atoms_zh"]
    match_en = re.fullmatch(r"Is the .+ completed within (.+ seconds?)\?", deadline_en)
    match_zh = re.fullmatch(r"该.+是否在 ([0-9.]+) 秒内完成？", deadline_zh)
    if not match_en or not match_zh:
        raise ValueError(f"Cannot reconstruct global_index={proposal['global_index']}")
    original_en = base_en[:-1] + " within " + match_en.group(1) + "?"
    original_zh = base_zh.replace("是否", f"是否在 {match_zh.group(1)} 秒内", 1)
    return [original_en], [original_zh]


def main() -> None:
    proposals = {row["global_index"]: row for row in load(PROPOSALS)}
    if len(proposals) != 505:
        raise ValueError(f"Expected 505 mechanical proposals, found {len(proposals)}")

    seen: set[int] = set()
    reverted = 0
    for path in sorted(REVIEWS_DIR.glob("*.jsonl")):
        rows = load(path)
        changed = False
        for row in rows:
            index = row["global_index"]
            if index not in proposals:
                continue
            seen.add(index)
            proposal = proposals[index]
            if row.get("mode") != "split":
                raise ValueError(f"global_index={index} is no longer a split record")
            if row.get("atoms_en") != proposal["atoms_en"] or row.get("atoms_zh") != proposal["atoms_zh"]:
                raise ValueError(f"global_index={index} changed after the mechanical proposal was applied")
            atoms_en, atoms_zh = restore_atoms(proposal)
            row["atoms_en"] = atoms_en
            row["atoms_zh"] = atoms_zh
            row["mode"] = "single"
            row["review_status"] = "reviewed"
            reverted += 1
            changed = True
        if changed:
            path.write_text(
                "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
                encoding="utf-8",
            )

    missing = sorted(set(proposals) - seen)
    if missing:
        raise ValueError(f"Mechanical proposals missing from canonical reviews: {missing}")
    print(f"reverted={reverted}")


if __name__ == "__main__":
    main()
