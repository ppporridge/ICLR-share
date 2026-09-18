# `atom_results` 文件夹使用说明

更新时间：2026-09-19

## 1. 这个文件夹是什么

本目录保存 3000 条视频编辑指令的原子化判定结果。原始数据包含 10 份编辑文档，每份对应 100 个视频；每个视频有 `E1`、`E2A`、`E2B` 三条具体编辑指令，因此每份文档最终包含 300 条指令。

每条指令已经由 Codex 逐条阅读和人工审核，并被改写为 1–4 个可以直接回答“是/否”的视觉判定问题。自动工具只用于最终格式排版和结构校验，没有用于决定如何拆解指令。

拆解原则和时间处理规则见 [`README.md`](README.md)。

## 2. 最快使用方式

根据用途选择入口：

| 使用目的 | 应查看的位置 | 说明 |
|---|---|---|
| 人工阅读中文结果 | [`full_zh/`](full_zh/) | 推荐入口；10 个 Markdown 文件，每个文件 300 条 |
| 程序读取或构建评测 | [`full_reviews/`](full_reviews/) | 唯一权威主数据；JSONL 格式，共 3000 行 |
| 阅读英文结果 | [`full_en/`](full_en/) | 与中文结果逐条对应的英文 Markdown |
| 理解拆解标准 | [`README.md`](README.md) | 原子化、时间换算、保底机制和最多四条等规则 |
| 查询原始数据索引 | [`full_manifest.jsonl`](full_manifest.jsonl) | 初始清单，不是最终审核结果 |

如果只是检查或使用中文原子问题，直接进入 `full_zh/` 即可。

如果需要训练、评测、转换格式或精确定位某条记录，应读取 `full_reviews/*.jsonl`。不要从 Markdown 反向解析主数据。

## 3. 目录结构与用途

```text
atom_results/
├── README.md                 # 原子化拆解规则
├── USAGE.md                  # 本使用说明
├── full_reviews/             # 权威主数据：逐条人工审核后的 JSONL
├── full_zh/                  # 由主数据排版得到的中文 Markdown
├── full_en/                  # 由主数据排版得到的英文 Markdown
├── full_manifest.jsonl       # 3000 条原始指令的初始索引清单
├── 01_atomization_test_100_zh.md
│                             # 早期 100 条试验稿，仅供参考
├── tools/
│   ├── prepare_full_manifest.py
│   └── render_full_reviews.py
│                             # 清单准备和纯格式渲染工具
└── resplit_review/           # 历史候选、评语和旧脚本，不是最终结果
```

各目录的优先级为：

1. `full_reviews/`：唯一事实来源和唯一应直接修改的位置。
2. `full_zh/`、`full_en/`：面向阅读的派生结果。
3. `README.md`：当前有效规则。
4. `full_manifest.jsonl`：只用于查询来源和初始编号。
5. `resplit_review/` 与 `01_atomization_test_100_zh.md`：历史材料，不应作为最终答案使用。

## 4. 十份结果文件的对应关系

| 全局编号 | 原始文档 | 中文最终结果 |
|---|---|---|
| 1–300 | `embodied_edit_records_test_100.md` | `full_zh/embodied_edit_records_test_100_atomized_zh.md` |
| 301–600 | `human_edit_records_test_100.md` | `full_zh/human_edit_records_test_100_atomized_zh.md` |
| 601–900 | `object_edit_records_test_100.md` | `full_zh/object_edit_records_test_100_atomized_zh.md` |
| 901–1200 | `process_edit_records_test_100.md` | `full_zh/process_edit_records_test_100_atomized_zh.md` |
| 1201–1500 | `scene_edit_records_test_100.md` | `full_zh/scene_edit_records_test_100_atomized_zh.md` |
| 1501–1800 | `syn_embodied_edit_records.md` | `full_zh/syn_embodied_edit_records_atomized_zh.md` |
| 1801–2100 | `syn_human_edit_records.md` | `full_zh/syn_human_edit_records_atomized_zh.md` |
| 2101–2400 | `syn_object_edit_records.md` | `full_zh/syn_object_edit_records_atomized_zh.md` |
| 2401–2700 | `syn_process_edit_records.md` | `full_zh/syn_process_edit_records_atomized_zh.md` |
| 2701–3000 | `syn_scene_edit_records.md` | `full_zh/syn_scene_edit_records_atomized_zh.md` |

每个 Markdown 文件内部重新使用 `001–300` 的源内序号；跨文件定位时应使用 JSONL 中唯一的 `global_index` 或 `edit_id`。

## 5. `full_reviews` 主数据格式

`full_reviews/` 按连续编号分成多个 JSONL 文件。每一行是一个完整 JSON 对象，例如：

```json
{
  "global_index": 2602,
  "edit_id": "synthetic_process_068_E1",
  "original_en": "Starting at 15.0 seconds, rotate the four foreground fruits a quarter-turn in alternating directions over five seconds.",
  "original_zh": "从第 15.0 秒开始，在五秒内让前景中的四个果实以交替方向各旋转四分之一圈。",
  "atoms_en": [
    "Do all four foreground fruits rotate?",
    "Does each fruit rotate by a quarter-turn?",
    "Do adjacent fruits rotate in alternating directions?",
    "Are the rotations completed within five seconds?"
  ],
  "atoms_zh": [
    "前景中的四个果实是否全部旋转？",
    "每个果实是否各旋转四分之一圈？",
    "相邻果实的旋转方向是否交替？",
    "这些旋转是否在 5 秒内完成？"
  ],
  "mode": "split",
  "review_status": "reviewed"
}
```

字段含义：

| 字段 | 含义 |
|---|---|
| `global_index` | 1–3000 的全局唯一编号 |
| `edit_id` | 指令唯一标识；通常由视频 ID 和 `E1`、`E2A`、`E2B` 组成 |
| `original_en` | 原始英文编辑指令，保留原始绝对时间 |
| `original_zh` | 对应中文翻译 |
| `atoms_en` | 英文原子判定问题列表 |
| `atoms_zh` | 中文原子判定问题列表，与 `atoms_en` 等长且逐项对应 |
| `mode` | 当前指令的拆解类型，见下节 |
| `review_status` | `reviewed` 表示已经完成人工审核 |

## 6. `mode` 的含义

当前主数据使用三种模式：

- `split`：原指令被拆为两个或更多原子判定问题。
- `single`：原指令本身只有一个不可继续拆分的核心要求，因此保留为一个判定问题。
- `fallback`：指令含有难以可靠继续细拆的比例、平滑程度等要求，但整条指令仍能形成明确的是/否问题，因此采用单条保底，而不是拒绝。

`fallback` 不表示数据无效，也不表示审核未完成。它仍是一个需要整体判断的是/否问题。

当前 3000 条记录全部为已接受、已审核结果，没有待审核记录：

| 类型 | 条数 |
|---|---:|
| `split` | 2710 |
| `single` | 251 |
| `fallback` | 39 |
| 合计 | 3000 |

按原子问题数量统计：

| 每条指令包含的原子问题数 | 指令条数 |
|---|---:|
| 1 条 | 290 |
| 2 条 | 1467 |
| 3 条 | 947 |
| 4 条 | 296 |
| 超过 4 条 | 0 |

## 7. 如何用这些原子问题评测视频

对于一条编辑指令：

1. 找到对应的 `edit_id`。
2. 按列表顺序逐项查看 `atoms_zh` 或 `atoms_en`。
3. 对每个问题独立回答“是”或“否”。
4. 如果任务要求整条编辑指令完全成功，通常只有全部原子问题均为“是”时才算通过。
5. 对 `fallback` 记录，直接对唯一的完整问题作整体判断，不要自行再次拆分或删除其中难判断的限定词。

时间判断时必须注意：

- `original_en` 和 `original_zh` 保留的是原视频绝对时间。
- 评测片段从原指令开头的 `At XX seconds` 或 `Starting at XX seconds` 处直接截取，所以原子问题不会重复这个起始时间。
- 原指令中后续出现的新绝对时间已经换算为相对片段起点的时长。
- “持续”但没有给出终点时，按“持续到视频结束”判断。
- 延迟要求只检查动作是否在延迟结束后完成，不额外检查延迟期间是否一直没有发生。

完整时间规则以 [`README.md`](README.md) 第 4、5 节为准。

## 8. 查找具体记录

按 `edit_id` 查找主数据：

```bash
rg 'synthetic_process_068_E1' full_reviews
```

按全局编号查找：

```bash
rg '"global_index":2602' full_reviews
```

在最终中文文档中查找：

```bash
rg -n 'synthetic_process_068_E1' full_zh
```

## 9. 修改结果时的规范流程

如后续确需修订某条指令，必须遵守以下顺序：

1. 先完整阅读原始英文指令、中文翻译和 [`README.md`](README.md)。
2. 由审核者亲自判断该条应该如何拆解，不能用关键词、正则表达式或模型批处理自动决定语义。
3. 只修改 `full_reviews/` 中对应的 JSONL 行。
4. 同步修改 `atoms_en` 和 `atoms_zh`，确保两边数量和含义逐项一致。
5. 保持 `global_index`、`edit_id` 和原始指令不变，除非确认源数据本身有误。
6. 非必要不得超过四个原子问题；不得为了增加拆分数量而制造重复判定。
7. 完成人工审核后，将 `review_status` 保持为 `reviewed`。
8. 最后再运行纯格式渲染，将主数据同步到 Markdown。

渲染命令：

```bash
python3 tools/render_full_reviews.py
```

该命令只读取 `full_reviews/*.jsonl` 并覆盖生成 `full_zh/*.md` 和 `full_en/*.md`，不会判断或改变原子拆分内容。不要直接修改 `full_zh/` 或 `full_en/`，因为下次渲染会覆盖这些手工改动。

验证某个 JSONL 文件能否正常解析：

```bash
python3 -m json.tool --json-lines full_reviews/文件名.jsonl >/dev/null
```

## 10. 不应作为最终结果使用的内容

### `full_manifest.jsonl`

这是从原始文档生成的初始索引清单。其中的 `review_status` 仍可能写为 `pending`，不能用它判断最终审核状态。最终状态以 `full_reviews/` 为准。

### `resplit_review/`

这里保存早期候选抽样、用户评语、阶段性决策和旧的辅助脚本。它们用于追踪审核过程，但其中部分候选或提案已经被后续人工审核覆盖。

不要把该目录中的 JSONL、TSV 或 Markdown 当作最终结果，也不要重新运行其中的批量提案、应用或回滚脚本。尤其不要使用这些脚本覆盖 `full_reviews/`。

### `01_atomization_test_100_zh.md`

这是规则形成阶段的 100 条试验稿。最终 3000 条结果已经吸收后续反馈并经过重新审核，应以 `full_reviews/` 和 `full_zh/` 为准。

### `tools/prepare_full_manifest.py`

该工具只用于从原始文档重新建立初始清单。日常查看和使用结果不需要运行它，也不能用它替代人工审核后的主数据。

## 11. 当前完整性状态

截至 2026-09-19：

- `full_reviews/` 共 3000 行，`global_index` 从 1 连续到 3000，无缺失和重复。
- 3000 条记录的 `review_status` 均为 `reviewed`。
- 每条记录的中英文原子问题数量一致。
- 每条指令包含 1–4 个原子问题，没有超过四条的记录。
- `full_zh/` 和 `full_en/` 各有 10 个最终文档，每个文档包含 300 条指令。

后续若修改任何主数据，应重新执行上述结构校验并更新本节统计。
