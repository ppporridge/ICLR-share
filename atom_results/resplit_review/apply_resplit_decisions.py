#!/usr/bin/env python3
"""Apply manually reviewed single-to-multi decisions to canonical review JSONL files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/home/zhou/ICLR-share/atom_results")
REVIEWS_DIR = ROOT / "full_reviews"
DECISION_PATHS = [
    ROOT / "resplit_review" / "resplit_decisions.jsonl",
]


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return rows


def main() -> None:
    decisions_list: list[dict] = []
    for path in DECISION_PATHS:
        decisions_list.extend(load_jsonl(path))
    decisions: dict[int, dict] = {}
    for decision in decisions_list:
        index = decision["global_index"]
        if index in decisions:
            raise ValueError(f"duplicate decision for global_index={index}")
        if decision.get("decision") != "split":
            raise ValueError(f"unsupported decision for global_index={index}")
        atoms_en = decision.get("atoms_en")
        atoms_zh = decision.get("atoms_zh")
        if not isinstance(atoms_en, list) or not isinstance(atoms_zh, list):
            raise ValueError(f"missing atom lists for global_index={index}")
        if len(atoms_en) != len(atoms_zh) or len(atoms_en) < 2:
            raise ValueError(f"atom count mismatch for global_index={index}")
        if any(not atom.strip() for atom in atoms_en + atoms_zh):
            raise ValueError(f"blank atom for global_index={index}")
        decisions[index] = decision

    seen: set[int] = set()
    changed = 0
    already_applied = 0
    for path in sorted(REVIEWS_DIR.glob("*.jsonl")):
        rows = load_jsonl(path)
        file_changed = False
        for row in rows:
            index = row["global_index"]
            if index not in decisions:
                continue
            seen.add(index)
            decision = decisions[index]
            desired_en = decision["atoms_en"]
            desired_zh = decision["atoms_zh"]
            if row.get("mode") == "split" and row.get("atoms_en") == desired_en and row.get("atoms_zh") == desired_zh:
                already_applied += 1
                continue
            if row.get("mode") != "single" or len(row.get("atoms_en", [])) != 1 or len(row.get("atoms_zh", [])) != 1:
                raise ValueError(
                    f"global_index={index} is not an unapplied single and does not match the desired result"
                )
            row["atoms_en"] = desired_en
            row["atoms_zh"] = desired_zh
            row["mode"] = "split"
            row["review_status"] = "reviewed"
            changed += 1
            file_changed = True
        if file_changed:
            path.write_text(
                "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows),
                encoding="utf-8",
            )

    missing = sorted(set(decisions) - seen)
    if missing:
        raise ValueError(f"decisions not found in canonical reviews: {missing}")
    print(f"validated_decisions={len(decisions)}")
    print(f"changed={changed}")
    print(f"already_applied={already_applied}")


if __name__ == "__main__":
    main()
