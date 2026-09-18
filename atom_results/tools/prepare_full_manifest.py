#!/usr/bin/env python3
"""Build a deterministic manifest for the 3,000-record atomization review."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "atom_results" / "full_manifest.jsonl"
SOURCE_FILES = [
    "embodied_edit_records_test_100.md",
    "human_edit_records_test_100.md",
    "object_edit_records_test_100.md",
    "process_edit_records_test_100.md",
    "scene_edit_records_test_100.md",
    "syn_embodied_edit_records.md",
    "syn_human_edit_records.md",
    "syn_object_edit_records.md",
    "syn_process_edit_records.md",
    "syn_scene_edit_records.md",
]


def records(path: Path):
    text = path.read_text(encoding="utf-8")
    for block in re.findall(r"```json\s*(\{.*?\})\s*```", text, re.S):
        yield json.loads(block)


def main() -> None:
    rows = []
    global_index = 0
    for source in SOURCE_FILES:
        for source_index, record in enumerate(records(ROOT / source), start=1):
            global_index += 1
            rows.append(
                {
                    "global_index": global_index,
                    "source_file": source,
                    "source_index": source_index,
                    "video_id": record["video_id"],
                    "edit_id": record["edit_id"],
                    "original_en": record["instruction"],
                    "review_status": "pending",
                }
            )

    if global_index != 3000:
        raise RuntimeError(f"Expected 3000 records, found {global_index}")

    OUT.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(f"wrote {global_index} records to {OUT}")


if __name__ == "__main__":
    main()
