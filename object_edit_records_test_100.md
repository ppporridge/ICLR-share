# Object Real-Video Edit Records - Balanced 100-Video Test Subset

This test document is derived from `object_edit_records.md`. Every selected source video retains its complete E1, E2A, and E2B branch-edit records verbatim.

Selection is performed at video level. Primary and secondary taxonomy counts are exact halves when the full count is even and one of the two nearest integers when it is odd.

`instruction` contains only temporal placement, the explicit target, and one edit operation. Preservation requirements remain in structured fields.

- Source collection: 200 videos / 600 edit records
- Test subset: 100 videos / 300 edit records
- Branches: `E1: A_to_B`, `E2A: A_to_D`, `E2B: B_to_C`
- Selection unit: one complete video with all three edits
- Source coverage: 10 videos selected from each consecutive 20-video block
- Selection manifest: `four_category_test_100_selection.json`
- Status: complete

## Test-Subset Primary-Type Counts

| Primary type | Full count | Exact half | Test count | Complement count |
|---|---:|---:|---:|---:|
| Attribute | 150 | 75 | 75 | 75 |
| Camera | 40 | 20 | 20 | 20 |
| Composition | 90 | 45 | 45 | 45 |
| Motion | 170 | 85 | 85 | 85 |
| Spatial | 75 | 37.5 | 37 | 38 |
| Style | 45 | 22.5 | 23 | 22 |
| Temporal | 30 | 15 | 15 | 15 |

## Test-Subset Secondary-Type Counts

| Primary / Secondary type | Full count | Exact half | Test count | Complement count |
|---|---:|---:|---:|---:|
| Attribute / Appearance | 75 | 37.5 | 37 | 38 |
| Attribute / Environment Object | 25 | 12.5 | 12 | 13 |
| Attribute / Illumination | 10 | 5 | 5 | 5 |
| Attribute / Physical State | 35 | 17.5 | 18 | 17 |
| Attribute / Weather | 5 | 2.5 | 3 | 2 |
| Camera / Camera Movement | 25 | 12.5 | 12 | 13 |
| Camera / Framing/Zoom | 15 | 7.5 | 8 | 7 |
| Composition / Entity Addition | 30 | 15 | 15 | 15 |
| Composition / Entity Removal | 30 | 15 | 15 | 15 |
| Composition / Entity Replacement | 30 | 15 | 15 | 15 |
| Motion / Kinematic Adjustment | 50 | 25 | 25 | 25 |
| Motion / New/Changed Motion | 50 | 25 | 25 | 25 |
| Motion / Object Interaction | 50 | 25 | 25 | 25 |
| Motion / Supporting/Environment Motion | 20 | 10 | 10 | 10 |
| Spatial / Absolute Position | 25 | 12.5 | 12 | 13 |
| Spatial / Multi-object Relationship | 35 | 17.5 | 17 | 18 |
| Spatial / Orientation | 15 | 7.5 | 8 | 7 |
| Style / Background-local Style | 7 | 3.5 | 4 | 3 |
| Style / Core Object-local Style | 7 | 3.5 | 4 | 3 |
| Style / Global Art/Rendering Style | 8 | 4 | 4 | 4 |
| Style / Global Color/Tone/Graphic Texture | 8 | 4 | 4 | 4 |
| Style / Global Media/Era Style | 8 | 4 | 4 | 4 |
| Style / Specified Auxiliary Object-local Style | 7 | 3.5 | 3 | 4 |
| Temporal / Multi-process Ordering | 7 | 3.5 | 4 | 3 |
| Temporal / Pause/Resume/Reverse | 8 | 4 | 4 | 4 |
| Temporal / Progress Speed | 15 | 7.5 | 7 | 8 |

## Records

## object_001

### object_001_E1

```json
{
  "video_id": "object_001",
  "edit_id": "object_001_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_adult_rabbit_fur",
    "target_description": "the adult rabbit's fur",
    "source_state": "The adult rabbit has mottled gray-brown fur.",
    "desired_change": "The adult rabbit's fur becomes pale cream."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the adult rabbit's fur from mottled gray-brown to pale cream over the next two seconds.",
  "expected_result": {
    "description": "The adult rabbit's fur becomes pale cream.",
    "target_phrase": "adult rabbit with pale-cream fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_001_E2A

```json
{
  "video_id": "object_001",
  "edit_id": "object_001_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_adult_rabbit",
    "target_description": "the adult rabbit",
    "source_state": "The adult rabbit stands over the nursing kits and makes only small head movements.",
    "desired_change": "The adult rabbit lowers its head and gently nuzzles the visible kits twice."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the adult rabbit lower its head and gently nuzzle the visible kits twice.",
  "expected_result": {
    "description": "The adult rabbit lowers its head and gently nuzzles the visible kits twice.",
    "target_phrase": "adult rabbit nuzzling the visible kits"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_001_E2B

```json
{
  "video_id": "object_001",
  "edit_id": "object_001_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_001_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "one_additional_light_brown_rabbit_kit",
    "target_description": "one additional light-brown rabbit kit",
    "source_state": "No light-brown kit is present at the outer right edge of the nursing cluster.",
    "desired_change": "One additional light-brown rabbit kit appears at the outer right edge of the nursing cluster."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one light-brown rabbit kit at the outer right edge of the nursing cluster.",
  "expected_result": {
    "description": "One additional light-brown rabbit kit appears at the outer right edge of the nursing cluster.",
    "target_phrase": "additional light-brown rabbit kit"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_001_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_001_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one additional light-brown rabbit kit on B independently of E1's change to the adult rabbit's fur; both edit results must coexist in C."
  }
}
```

## object_004

### object_004_E1

```json
{
  "video_id": "object_004",
  "edit_id": "object_004_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_004.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Plumage Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_peacock_neck_plumage",
    "target_description": "the peacock's neck plumage",
    "source_state": "The peacock has vivid blue neck plumage.",
    "desired_change": "The peacock's neck plumage becomes emerald green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the peacock's neck plumage from vivid blue to emerald green over the next two seconds.",
  "expected_result": {
    "description": "The peacock's neck plumage becomes emerald green.",
    "target_phrase": "peacock with emerald-green neck"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_004_E2A

```json
{
  "video_id": "object_004",
  "edit_id": "object_004_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_004.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_peacock_and_the_nearest_dark_guinea_fowl",
    "target_description": "the peacock and the nearest dark guinea fowl",
    "source_state": "The peacock and guinea fowl move in a loose changing group.",
    "desired_change": "The peacock and the nearest dark guinea fowl stand side by side on the path."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the peacock and the nearest dark guinea fowl side by side on the path.",
  "expected_result": {
    "description": "The peacock and the nearest dark guinea fowl stand side by side on the path.",
    "target_phrase": "peacock and guinea fowl side by side"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_004_E2B

```json
{
  "video_id": "object_004",
  "edit_id": "object_004_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_004_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_peacock",
    "target_description": "the peacock",
    "source_state": "The peacock walks with its long tail folded.",
    "desired_change": "The peacock fans its tail and shakes the feathers twice."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the peacock fan its tail and shake the feathers twice.",
  "expected_result": {
    "description": "The peacock fans its tail and shakes the feathers twice.",
    "target_phrase": "peacock fanning and shaking its tail"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_004_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_004_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the peacock on B independently of E1's change to the peacock's neck plumage; both edit results must coexist in C."
  }
}
```

## object_008

### object_008_E1

```json
{
  "video_id": "object_008",
  "edit_id": "object_008_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_008.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_larger_boar_coat",
    "target_description": "the larger boar's coat",
    "source_state": "The larger boar has a mottled brown bristled coat.",
    "desired_change": "The larger boar's coat becomes dark charcoal."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the larger boar's mottled brown coat to dark charcoal over the next two seconds.",
  "expected_result": {
    "description": "The larger boar's coat becomes dark charcoal.",
    "target_phrase": "larger boar with dark-charcoal coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_008_E2A

```json
{
  "video_id": "object_008",
  "edit_id": "object_008_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_008.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_boars",
    "target_description": "the two boars",
    "source_state": "The two boars repeatedly overlap while foraging on the slope.",
    "desired_change": "The two boars stand side by side with one body width between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the two boars side by side with one body width between them.",
  "expected_result": {
    "description": "The two boars stand side by side with one body width between them.",
    "target_phrase": "two boars one body width apart"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_008_E2B

```json
{
  "video_id": "object_008",
  "edit_id": "object_008_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_008_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_smaller_uphill_boar",
    "target_description": "the smaller uphill boar",
    "source_state": "A smaller boar is visible uphill from the larger boar.",
    "desired_change": "The smaller uphill boar is removed from the scene."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the smaller boar positioned uphill from the larger boar.",
  "expected_result": {
    "description": "The smaller uphill boar is removed from the scene.",
    "target_phrase": "slope with only the larger boar"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_008_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_008_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the smaller uphill boar on B independently of E1's change to the larger boar's coat; both edit results must coexist in C."
  }
}
```

## object_011

### object_011_E1

```json
{
  "video_id": "object_011",
  "edit_id": "object_011_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_011.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Surface Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_dry_training_ground_surface",
    "target_description": "the dry training-ground surface",
    "source_state": "The training-ground surface is dry and pale brown.",
    "desired_change": "The training-ground surface becomes damp dark brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the dry pale-brown training-ground surface to damp dark brown over the next two seconds.",
  "expected_result": {
    "description": "The training-ground surface becomes damp dark brown.",
    "target_phrase": "damp dark-brown training ground"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_011_E2A

```json
{
  "video_id": "object_011",
  "edit_id": "object_011_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_011.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Changed Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_foremost_tracked_vehicle",
    "target_description": "the foremost tracked vehicle",
    "source_state": "The foremost tracked vehicle advances along a mostly straight route.",
    "desired_change": "The foremost tracked vehicle makes a wide right turn while advancing."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the foremost tracked vehicle execute a wide right turn while advancing for five seconds.",
  "expected_result": {
    "description": "The foremost tracked vehicle makes a wide right turn while advancing.",
    "target_phrase": "tracked vehicle making wide right turn"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_011_E2B

```json
{
  "video_id": "object_011",
  "edit_id": "object_011_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_011_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_smaller_box_shaped_support_vehicle",
    "target_description": "the smaller box-shaped support vehicle",
    "source_state": "A smaller box-shaped support vehicle follows behind the tracked vehicles.",
    "desired_change": "The smaller support vehicle is removed from the formation."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the smaller box-shaped support vehicle from the formation.",
  "expected_result": {
    "description": "The smaller support vehicle is removed from the formation.",
    "target_phrase": "formation without smaller support vehicle"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_011_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_011_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the smaller box-shaped support vehicle on B independently of E1's change to the dry training-ground surface; both edit results must coexist in C."
  }
}
```

## object_013

### object_013_E1

```json
{
  "video_id": "object_013",
  "edit_id": "object_013_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Amplitude Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_flag",
    "target_description": "the flag",
    "source_state": "The flag flaps with large rapid folds in strong wind.",
    "desired_change": "The flag ripples with half its original amplitude."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 14.0 seconds, make the flag ripple with half its original amplitude for five seconds.",
  "expected_result": {
    "description": "The flag ripples with half its original amplitude.",
    "target_phrase": "flag rippling at half amplitude"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_013_E2A

```json
{
  "video_id": "object_013",
  "edit_id": "object_013_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The close framing shows the flag and only part of the pole.",
    "desired_change": "The framing widens to include the full flagpole and more surrounding sky."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly to include the full flagpole and more surrounding sky over four seconds.",
  "expected_result": {
    "description": "The framing widens to include the full flagpole and more surrounding sky.",
    "target_phrase": "wide view of full flagpole"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_013_E2B

```json
{
  "video_id": "object_013",
  "edit_id": "object_013_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_013_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_blue_pennant",
    "target_description": "one small plain blue pennant",
    "source_state": "No second pole or plain pennant is present to the right of the existing flag.",
    "desired_change": "A small plain blue pennant appears on a separate pole to the right."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add a small plain blue pennant on a separate pole to the right of the existing flag.",
  "expected_result": {
    "description": "A small plain blue pennant appears on a separate pole to the right.",
    "target_phrase": "small blue pennant on separate pole"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_013_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_013_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain blue pennant on B independently of E1's change to the flag; both edit results must coexist in C."
  }
}
```

## object_014

### object_014_E1

```json
{
  "video_id": "object_014",
  "edit_id": "object_014_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_014.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_rolling_water_bottle",
    "target_description": "the rolling water bottle",
    "source_state": "The water bottle rolls downhill with only small lateral deviations.",
    "desired_change": "The water bottle follows a wide S-shaped rolling path."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 20,
    "evaluation_window_sec": [
      13,
      22
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 14.0 seconds, make the water bottle follow a wide S-shaped rolling path for six seconds.",
  "expected_result": {
    "description": "The water bottle follows a wide S-shaped rolling path.",
    "target_phrase": "water bottle rolling along S-shaped path"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      22
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_014_E2A

```json
{
  "video_id": "object_014",
  "edit_id": "object_014_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_014.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Overhead Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld camera follows the bottle from a shaky rear-oblique angle.",
    "desired_change": "The camera tracks the bottle smoothly from directly overhead."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the rolling water bottle smoothly from directly overhead for five seconds.",
  "expected_result": {
    "description": "The camera tracks the bottle smoothly from directly overhead.",
    "target_phrase": "smooth overhead bottle tracking"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_014_E2B

```json
{
  "video_id": "object_014",
  "edit_id": "object_014_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_014_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "High-contrast Monochrome Grade",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The road footage has a natural low-saturation color grade.",
    "desired_change": "The full frame uses a crisp high-contrast monochrome grade."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, apply a crisp high-contrast monochrome grade to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a crisp high-contrast monochrome grade.",
    "target_phrase": "high-contrast monochrome road footage"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_014_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_014_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the rolling water bottle; both edit results must coexist in C."
  }
}
```

## object_015

### object_015_E1

```json
{
  "video_id": "object_015",
  "edit_id": "object_015_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Surface Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_central_tree_trunk",
    "target_description": "the central tree trunk",
    "source_state": "The central tree trunk has natural medium-brown bark.",
    "desired_change": "The central tree trunk's bark becomes pale gray."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.0 seconds, change the central tree trunk's bark from medium brown to pale gray over the next two seconds.",
  "expected_result": {
    "description": "The central tree trunk's bark becomes pale gray.",
    "target_phrase": "central tree trunk with pale-gray bark"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 20.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_015_E2A

```json
{
  "video_id": "object_015",
  "edit_id": "object_015_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_lower_panda_second_climb",
    "target_description": "the lower panda's second climb",
    "source_state": "The lower panda begins climbing the central trunk again after resting on the platform.",
    "desired_change": "The lower panda's second climb pauses for three seconds and then resumes."
  },
  "timing": {
    "edit_point_sec": 34.0,
    "effect_start_sec": 34.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      33.0,
      39.0
    ],
    "temporal_behavior": "temporary process pause"
  },
  "instruction": "Starting at 34.0 seconds, pause the lower panda's second climb for three seconds before it resumes.",
  "expected_result": {
    "description": "The lower panda's second climb pauses for three seconds and then resumes.",
    "target_phrase": "three-second pause in second panda climb"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_015_E2B

```json
{
  "video_id": "object_015",
  "edit_id": "object_015_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_015_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_lower_panda",
    "target_description": "the lower panda",
    "source_state": "The lower panda climbs close to the upper panda on the same trunk.",
    "desired_change": "The lower panda reaches one forepaw toward the upper panda twice."
  },
  "timing": {
    "edit_point_sec": 35,
    "effect_start_sec": 35,
    "effect_end_sec": 39,
    "evaluation_window_sec": [
      34,
      41
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 35.0 seconds, make the lower panda reach one forepaw toward the upper panda twice.",
  "expected_result": {
    "description": "The lower panda reaches one forepaw toward the upper panda twice.",
    "target_phrase": "lower panda reaching toward upper panda"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_015_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34,
      41
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 35.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_015_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the lower panda on B independently of E1's change to the central tree trunk; both edit results must coexist in C."
  }
}
```

## object_017

### object_017_E1

```json
{
  "video_id": "object_017",
  "edit_id": "object_017_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_spotted_cat_base_coat",
    "target_description": "the spotted cat's base coat",
    "source_state": "The spotted cat has a golden-tan base coat with dark markings.",
    "desired_change": "The base coat becomes cool pale gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the spotted cat's base coat from golden-tan to cool pale gray over the next two seconds.",
  "expected_result": {
    "description": "The base coat becomes cool pale gray.",
    "target_phrase": "spotted cat with cool-gray coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_017_E2A

```json
{
  "video_id": "object_017",
  "edit_id": "object_017_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_spotted_cat",
    "target_description": "the spotted cat",
    "source_state": "The spotted cat walks along the middle of the muddy bank.",
    "desired_change": "The spotted cat is positioned at the waterline along the bank."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the spotted cat at the waterline along the muddy bank.",
  "expected_result": {
    "description": "The spotted cat is positioned at the waterline along the bank.",
    "target_phrase": "spotted cat at waterline"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_017_E2B

```json
{
  "video_id": "object_017",
  "edit_id": "object_017_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_017_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_shallow_water_at_the_bank",
    "target_description": "the shallow water at the bank",
    "source_state": "The shallow water beside the bank has small subdued ripples.",
    "desired_change": "The shallow water laps against the bank in larger repeated ripples."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the shallow water lap against the bank in larger repeated ripples for five seconds.",
  "expected_result": {
    "description": "The shallow water laps against the bank in larger repeated ripples.",
    "target_phrase": "larger ripples lapping against bank"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_017_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_017_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the shallow water at the bank on B independently of E1's change to the spotted cat's base coat; both edit results must coexist in C."
  }
}
```

## object_019

### object_019_E1

```json
{
  "video_id": "object_019",
  "edit_id": "object_019_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Weather Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_cloudy_sky",
    "target_description": "the cloudy sky",
    "source_state": "The jet flies against a blue-gray sky with extensive cloud cover.",
    "desired_change": "The sky becomes clear blue with only sparse clouds."
  },
  "timing": {
    "edit_point_sec": 16,
    "effect_start_sec": 16,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      15,
      21
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 16.0 seconds, change the cloudy blue-gray sky to clear blue with sparse clouds over the next three seconds.",
  "expected_result": {
    "description": "The sky becomes clear blue with only sparse clouds.",
    "target_phrase": "clear blue sky with sparse clouds"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      15,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 16.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_019_E2A

```json
{
  "video_id": "object_019",
  "edit_id": "object_019_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_jet",
    "target_description": "the jet",
    "source_state": "The jet is banked while turning away from the camera.",
    "desired_change": "The jet is oriented with its wings level."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the jet so its wings are level while it continues away from the camera.",
  "expected_result": {
    "description": "The jet is oriented with its wings level.",
    "target_phrase": "departing jet with level wings"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_019_E2B

```json
{
  "video_id": "object_019",
  "edit_id": "object_019_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_019_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_departing_jet",
    "target_description": "the departing jet",
    "source_state": "The jet follows a steady departure path after its turn.",
    "desired_change": "The departing jet performs two shallow wing rocks."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      30.0,
      37.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 31.0 seconds, make the departing jet perform two shallow wing rocks.",
  "expected_result": {
    "description": "The departing jet performs two shallow wing rocks.",
    "target_phrase": "departing jet making two wing rocks"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_019_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_019_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the departing jet on B independently of E1's change to the cloudy sky; both edit results must coexist in C."
  }
}
```

## object_020

### object_020_E1

```json
{
  "video_id": "object_020",
  "edit_id": "object_020_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Surface State Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "dry_soil_beneath_the_deer",
    "target_description": "the dry exposed soil beneath and immediately ahead of the deer",
    "source_state": "The exposed soil beneath the deer is dry and pale brown.",
    "desired_change": "The exposed soil beneath the deer becomes visibly wet and dark brown."
  },
  "timing": {
    "edit_point_sec": 14.0,
    "effect_start_sec": 14.0,
    "effect_end_sec": 16.0,
    "evaluation_window_sec": [
      13.0,
      18.0
    ],
    "temporal_behavior": "gradual persistent change",
    "source_stage_at_edit": "dog and deer interaction over exposed soil"
  },
  "instruction": "Starting at 14.0 seconds, change the dry exposed soil beneath the deer to visibly wet dark-brown soil over the next two seconds.",
  "expected_result": {
    "description": "The exposed soil beneath and immediately ahead of the deer appears wet and dark brown.",
    "target_phrase": "wet dark-brown soil beneath the deer"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.0,
      18.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Dry exposed soil is visible beneath the dog and deer throughout this interaction segment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_020_E2A

```json
{
  "video_id": "object_020",
  "edit_id": "object_020_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_antlered_deer",
    "target_description": "the antlered deer",
    "source_state": "The antlered deer mostly stands and turns to track the dog.",
    "desired_change": "The antlered deer stamps one front hoof twice."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the antlered deer stamp one front hoof twice.",
  "expected_result": {
    "description": "The antlered deer stamps one front hoof twice.",
    "target_phrase": "deer stamping front hoof twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_020_E2B

```json
{
  "video_id": "object_020",
  "edit_id": "object_020_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_020_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_dog",
    "target_description": "the dog",
    "source_state": "The dog makes repeated partial arcs around the deer.",
    "desired_change": "The dog completes one full circle around the deer."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the dog complete one full circle around the antlered deer.",
  "expected_result": {
    "description": "The dog completes one full circle around the deer.",
    "target_phrase": "dog completing full circle around deer"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_020_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_020_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dog on B independently of E1's wet-soil change beneath the deer; both edit results must coexist in C."
  }
}
```

## object_022

### object_022_E1

```json
{
  "video_id": "object_022",
  "edit_id": "object_022_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_022.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_white_rabbit",
    "target_description": "the white rabbit",
    "source_state": "The white rabbit repeatedly nudges the black-and-white soccer ball from changing sides.",
    "desired_change": "The rabbit pushes the soccer ball through one tight clockwise circle."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the white rabbit push the soccer ball through one tight clockwise circle.",
  "expected_result": {
    "description": "The rabbit pushes the soccer ball through one tight clockwise circle.",
    "target_phrase": "rabbit pushing ball in clockwise circle"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_022_E2A

```json
{
  "video_id": "object_022",
  "edit_id": "object_022_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_022.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_black_and_white_soccer_ball",
    "target_description": "the black-and-white soccer ball",
    "source_state": "The soccer ball follows short irregular paths after each nudge.",
    "desired_change": "The soccer ball rolls along a clear zigzag path after the rabbit nudges it."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the soccer ball roll along a clear zigzag path after the rabbit nudges it.",
  "expected_result": {
    "description": "The soccer ball rolls along a clear zigzag path after the rabbit nudges it.",
    "target_phrase": "soccer ball rolling in zigzag path"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_022_E2B

```json
{
  "video_id": "object_022",
  "edit_id": "object_022_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_022_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Colored-pencil Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_garden_background",
    "target_description": "the garden background",
    "source_state": "The garden background has a realistic grass, soil, and timber appearance.",
    "desired_change": "The garden background is rendered as a colored-pencil illustration."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the garden background as a colored-pencil illustration over the next two seconds.",
  "expected_result": {
    "description": "The garden background is rendered as a colored-pencil illustration.",
    "target_phrase": "colored-pencil garden background"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_022_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_022_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the garden background on B independently of E1's change to the white rabbit; both edit results must coexist in C."
  }
}
```

## object_023

### object_023_E1

```json
{
  "video_id": "object_023",
  "edit_id": "object_023_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_round_silver_fuel_tank_cap",
    "target_description": "the round silver fuel-tank cap on top of the red tank",
    "source_state": "A round silver fuel-tank cap is attached to the top of the red tank.",
    "desired_change": "The round silver fuel-tank cap is removed from the red tank."
  },
  "timing": {
    "edit_point_sec": 14.0,
    "effect_start_sec": 14.0,
    "effect_end_sec": 15.0,
    "evaluation_window_sec": [
      13.5,
      17.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "close view of the red tank and its round silver cap"
  },
  "instruction": "At 14.0 seconds, remove the round silver fuel-tank cap from the top of the red tank.",
  "expected_result": {
    "description": "The red fuel tank remains visible without its round silver cap.",
    "target_phrase": "red fuel tank without its silver cap"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.5,
      17.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The round silver cap becomes clearly visible on top of the red fuel tank around 14 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_023_E2A

```json
{
  "video_id": "object_023",
  "edit_id": "object_023_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Low Orbit",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld camera tours the motorcycle from varying standing height.",
    "desired_change": "The camera orbits clockwise around the motorcycle at wheel height."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, orbit clockwise around the motorcycle at wheel height for five seconds.",
  "expected_result": {
    "description": "The camera orbits clockwise around the motorcycle at wheel height.",
    "target_phrase": "clockwise wheel-height motorcycle orbit"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_023_E2B

```json
{
  "video_id": "object_023",
  "edit_id": "object_023_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_023_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_red_sedan_behind_the_motorcycle",
    "target_description": "the red sedan parked behind the motorcycle",
    "source_state": "A red sedan is parked behind the motorcycle.",
    "desired_change": "The red sedan parked behind the motorcycle is removed from the parking area."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the red sedan parked behind the motorcycle.",
  "expected_result": {
    "description": "The red sedan parked behind the motorcycle is removed from the parking area.",
    "target_phrase": "parking area without the red sedan"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_023_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The red sedan is clearly visible behind the motorcycle around the 29-second edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_023_E1",
    "must_preserve_e1_result": true,
    "description": "This edit removes the red sedan on B while preserving E1's removal of the round silver fuel-tank cap; both edit results must coexist in C."
  }
}
```

## object_024

### object_024_E1

```json
{
  "video_id": "object_024",
  "edit_id": "object_024_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_024.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Surface State Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_oval_dirt_road",
    "target_description": "the oval dirt road",
    "source_state": "The oval dirt road is dry and pale brown.",
    "desired_change": "The oval dirt road becomes damp dark brown."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.0 seconds, change the dry pale-brown dirt road to damp dark brown over the next two seconds.",
  "expected_result": {
    "description": "The oval dirt road becomes damp dark brown.",
    "target_phrase": "damp dark-brown dirt road"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 20.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_024_E2A

```json
{
  "video_id": "object_024",
  "edit_id": "object_024_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_024.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Process Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_main_tank_entry_into_the_narrow_corridor",
    "target_description": "the main tank's entry into the narrow corridor",
    "source_state": "The main tank enters the narrow obstacle corridor and progressively slows.",
    "desired_change": "The remaining corridor-entry process progresses at twice its original speed."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 38.0,
    "evaluation_window_sec": [
      30.0,
      40.0
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 31.0 seconds, make the main tank's remaining corridor-entry process progress at twice its original speed.",
  "expected_result": {
    "description": "The remaining corridor-entry process progresses at twice its original speed.",
    "target_phrase": "tank corridor entry at double speed"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      40.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_024_E2B

```json
{
  "video_id": "object_024",
  "edit_id": "object_024_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_024_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_dust_behind_the_distant_tank",
    "target_description": "the dust behind the distant tank",
    "source_state": "A low dust plume trails behind the distant tank.",
    "desired_change": "The dust rises into a higher rolling plume behind the tank."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 39.0,
    "effect_end_sec": 43.0,
    "evaluation_window_sec": [
      34.0,
      45.0
    ],
    "temporal_behavior": "bounded motion modification",
    "source_stage_at_edit": "main tank slowing among obstacles before the distant tank and dust become visible"
  },
  "instruction": "At 35.0 seconds, make the dust behind the distant tank rise into a higher rolling plume when that tank appears at 39.0 seconds.",
  "expected_result": {
    "description": "When the distant tank enters at 39.0 seconds, its dust rises into a higher rolling plume for four seconds.",
    "target_phrase": "higher rolling dust plume behind the distant tank"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_024_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      45.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The distant tank and its dust become visible around 39 seconds and remain observable through the late segment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_024_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dust behind the distant tank on B independently of E1's change to the oval dirt road; both edit results must coexist in C."
  }
}
```

## object_026

### object_026_E1

```json
{
  "video_id": "object_026",
  "edit_id": "object_026_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Body Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_horned_chameleon_yellow_green_side",
    "target_description": "the horned chameleon's yellow-green side",
    "source_state": "The horned chameleon has a muted yellow-green side region.",
    "desired_change": "The side region becomes vivid golden yellow."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the horned chameleon's yellow-green side region to vivid golden yellow over the next two seconds.",
  "expected_result": {
    "description": "The side region becomes vivid golden yellow.",
    "target_phrase": "horned chameleon with golden-yellow side"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_026_E2A

```json
{
  "video_id": "object_026",
  "edit_id": "object_026_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_chameleons",
    "target_description": "the two chameleons",
    "source_state": "The two chameleons face each other on the horizontal branch.",
    "desired_change": "Both chameleons face toward the left end of the branch."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient both chameleons to face the left end of the horizontal branch.",
  "expected_result": {
    "description": "Both chameleons face toward the left end of the branch.",
    "target_phrase": "both chameleons facing left"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_026_E2B

```json
{
  "video_id": "object_026",
  "edit_id": "object_026_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_026_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_horizontal_branch",
    "target_description": "the horizontal branch",
    "source_state": "The two chameleons stand on a pale natural branch.",
    "desired_change": "The horizontal branch is replaced by a thick cork perch of the same length."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the horizontal branch with a thick cork perch of the same length.",
  "expected_result": {
    "description": "The horizontal branch is replaced by a thick cork perch of the same length.",
    "target_phrase": "thick cork perch"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_026_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_026_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the horizontal branch on B independently of E1's change to the horned chameleon's yellow-green side; both edit results must coexist in C."
  }
}
```

## object_027

### object_027_E1

```json
{
  "video_id": "object_027",
  "edit_id": "object_027_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Exterior Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_main_bus_black_body_panels",
    "target_description": "the main bus's black body panels",
    "source_state": "The main bus has black body panels with red accent areas.",
    "desired_change": "The black body panels become deep navy blue."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the main bus's black body panels to deep navy blue over the next two seconds.",
  "expected_result": {
    "description": "The black body panels become deep navy blue.",
    "target_phrase": "main bus with navy-blue panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_027_E2A

```json
{
  "video_id": "object_027",
  "edit_id": "object_027_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Viewpoint Shift",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_viewpoint",
    "target_description": "the camera viewpoint",
    "source_state": "The camera follows the main bus from an offset moving-vehicle viewpoint.",
    "desired_change": "The camera moves to a centered view directly behind the main bus."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, move the camera to a centered view directly behind the main bus over four seconds.",
  "expected_result": {
    "description": "The camera moves to a centered view directly behind the main bus.",
    "target_phrase": "centered view behind main bus"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_027_E2B

```json
{
  "video_id": "object_027",
  "edit_id": "object_027_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_027_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path and Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_main_bus",
    "target_description": "the main bus",
    "source_state": "The main bus follows the winding road with noticeable lateral shifts.",
    "desired_change": "The main bus follows shallower curves at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the main bus follow shallower curves at half its original speed for six seconds.",
  "expected_result": {
    "description": "The main bus follows shallower curves at half its original speed.",
    "target_phrase": "bus following shallower slower curves"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_027_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_027_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the main bus on B independently of E1's change to the main bus's black body panels; both edit results must coexist in C."
  }
}
```

## object_031

### object_031_E1

```json
{
  "video_id": "object_031",
  "edit_id": "object_031_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Stroke and Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_frog",
    "target_description": "the frog",
    "source_state": "The frog alternates small paddles with a short burst of rapid kicks.",
    "desired_change": "The frog swims with slower, longer hind-leg strokes."
  },
  "timing": {
    "edit_point_sec": 17,
    "effect_start_sec": 17,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      16,
      24
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 17.0 seconds, make the frog swim with slower and longer hind-leg strokes for five seconds.",
  "expected_result": {
    "description": "The frog swims with slower, longer hind-leg strokes.",
    "target_phrase": "frog swimming with slower longer strokes"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      16,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 17.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_031_E2A

```json
{
  "video_id": "object_031",
  "edit_id": "object_031_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Overhead Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld camera follows the frog with an oblique pan across the pond.",
    "desired_change": "The camera tracks the frog smoothly from directly overhead."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      31.0,
      39.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 32.0 seconds, track the frog smoothly from directly overhead for five seconds.",
  "expected_result": {
    "description": "The camera tracks the frog smoothly from directly overhead.",
    "target_phrase": "smooth overhead frog tracking"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_031_E2B

```json
{
  "video_id": "object_031",
  "edit_id": "object_031_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_031_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Teal High-contrast Grade",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The pond footage has a muted natural yellow-green color grade.",
    "desired_change": "The full frame uses a vivid teal high-contrast grade."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      31.0,
      36.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 32.0 seconds, apply a vivid teal high-contrast grade to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a vivid teal high-contrast grade.",
    "target_phrase": "teal high-contrast pond footage"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_031_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_031_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the frog; both edit results must coexist in C."
  }
}
```

## object_032

### object_032_E1

```json
{
  "video_id": "object_032",
  "edit_id": "object_032_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_032.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Shell Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_main_crab_shell",
    "target_description": "the main crab's shell",
    "source_state": "The main crab has a blue-green shell with dark markings.",
    "desired_change": "The main crab's shell becomes vivid red."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the main crab's blue-green shell to vivid red over the next two seconds.",
  "expected_result": {
    "description": "The main crab's shell becomes vivid red.",
    "target_phrase": "main crab with vivid-red shell"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_032_E2A

```json
{
  "video_id": "object_032",
  "edit_id": "object_032_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_032.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_main_crab",
    "target_description": "the main crab",
    "source_state": "The main crab side-steps across the tank at a slow uneven rate.",
    "desired_change": "The main crab side-steps at twice its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the main crab side-step at twice its original speed for five seconds.",
  "expected_result": {
    "description": "The main crab side-steps at twice its original speed.",
    "target_phrase": "crab side-stepping twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_032_E2B

```json
{
  "video_id": "object_032",
  "edit_id": "object_032_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_032_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "one_smaller_blue_green_crab",
    "target_description": "one smaller blue-green crab",
    "source_state": "No smaller blue-green crab is present behind the close main crab.",
    "desired_change": "One smaller blue-green crab appears behind the main crab."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one smaller blue-green crab behind the main crab.",
  "expected_result": {
    "description": "One smaller blue-green crab appears behind the main crab.",
    "target_phrase": "smaller crab behind main crab"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_032_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_032_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one smaller blue-green crab on B independently of E1's change to the main crab's shell; both edit results must coexist in C."
  }
}
```

## object_033

### object_033_E1

```json
{
  "video_id": "object_033",
  "edit_id": "object_033_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Underwater Illumination Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_underwater_illumination",
    "target_description": "the underwater illumination",
    "source_state": "The reef is lit by diffuse cool blue underwater light.",
    "desired_change": "The underwater illumination becomes brighter cyan with visible sun shafts."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the diffuse blue underwater illumination to brighter cyan light with visible sun shafts over the next two seconds.",
  "expected_result": {
    "description": "The underwater illumination becomes brighter cyan with visible sun shafts.",
    "target_phrase": "bright cyan underwater sun shafts"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_033_E2A

```json
{
  "video_id": "object_033",
  "edit_id": "object_033_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_shark",
    "target_description": "the shark",
    "source_state": "The shark follows broad level turns above the reef.",
    "desired_change": "The shark performs one gentle body roll while swimming forward."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the shark perform one gentle body roll while swimming forward.",
  "expected_result": {
    "description": "The shark performs one gentle body roll while swimming forward.",
    "target_phrase": "shark performing gentle body roll"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_033_E2B

```json
{
  "video_id": "object_033",
  "edit_id": "object_033_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_033_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_nearest_dark_reef_formation",
    "target_description": "the nearest dark reef formation",
    "source_state": "A dark irregular reef formation occupies the nearest seabed.",
    "desired_change": "The nearest dark reef formation is replaced by a pale sand mound of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the nearest dark reef formation with a pale sand mound of the same size.",
  "expected_result": {
    "description": "The nearest dark reef formation is replaced by a pale sand mound of the same size.",
    "target_phrase": "pale sand mound on seabed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_033_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_033_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the nearest dark reef formation on B independently of E1's change to the underwater illumination; both edit results must coexist in C."
  }
}
```

## object_039

### object_039_E1

```json
{
  "video_id": "object_039",
  "edit_id": "object_039_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_cats",
    "target_description": "the two cats",
    "source_state": "The black cat and orange-white cat repeatedly approach and touch around the head and neck.",
    "desired_change": "The two cats touch noses twice."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      13,
      19
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the black cat and the orange-white cat touch noses twice.",
  "expected_result": {
    "description": "The two cats touch noses twice.",
    "target_phrase": "two cats touching noses twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_039_E2A

```json
{
  "video_id": "object_039",
  "edit_id": "object_039_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_orange_and_white_cat",
    "target_description": "the orange-and-white cat",
    "source_state": "The orange-and-white cat circles the black cat with short variable steps.",
    "desired_change": "The orange-and-white cat circles at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the orange-and-white cat circle the black cat at half its original speed for five seconds.",
  "expected_result": {
    "description": "The orange-and-white cat circles at half its original speed.",
    "target_phrase": "orange-white cat circling at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_039_E2B

```json
{
  "video_id": "object_039",
  "edit_id": "object_039_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_039_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1990s Camcorder Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The lawn footage has a modern digital-video appearance.",
    "desired_change": "The full frame resembles a 1990s consumer-camcorder recording."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full frame into a 1990s consumer-camcorder recording over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1990s consumer-camcorder recording.",
    "target_phrase": "1990s cat camcorder footage"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_039_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_039_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the two cats; both edit results must coexist in C."
  }
}
```

## object_040

### object_040_E1

```json
{
  "video_id": "object_040",
  "edit_id": "object_040_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Surface Wetness Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_foreground_horizontal_log",
    "target_description": "the foreground horizontal log",
    "source_state": "The foreground horizontal log has a dry, pale-brown surface.",
    "desired_change": "The log surface becomes visibly wet and slightly darker while retaining its bark texture."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the foreground horizontal log from dry to visibly wet with a slightly darker surface.",
  "expected_result": {
    "description": "The foreground horizontal log appears visibly wet and slightly darker while retaining its bark texture.",
    "target_phrase": "visibly wet foreground log"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_040_E2A

```json
{
  "video_id": "object_040",
  "edit_id": "object_040_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Core Object and Environment"
  },
  "target": {
    "target_id": "the_black_cat_forepaws",
    "target_description": "the black cat's forepaws",
    "source_state": "The black cat's forepaws rest together on one side of the tree fork.",
    "desired_change": "The forepaws are positioned symmetrically on opposite sides of the tree fork."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the black cat's forepaws symmetrically on opposite sides of the tree fork.",
  "expected_result": {
    "description": "The forepaws are positioned symmetrically on opposite sides of the tree fork.",
    "target_phrase": "forepaws on opposite sides of tree fork"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_040_E2B

```json
{
  "video_id": "object_040",
  "edit_id": "object_040_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_040_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_rear_horizontal_wooden_pole",
    "target_description": "the rear horizontal wooden pole",
    "source_state": "A separate horizontal wooden pole crosses the rear enclosure behind the black cat.",
    "desired_change": "The rear horizontal wooden pole is removed from the enclosure."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the rear horizontal wooden pole from behind the black cat.",
  "expected_result": {
    "description": "The rear horizontal wooden pole is removed from the enclosure.",
    "target_phrase": "enclosure without rear horizontal pole"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_040_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_040_E1",
    "must_preserve_e1_result": true,
    "description": "This edit removes the rear horizontal wooden pole on B while preserving E1's visibly wet, slightly darker foreground log; both edit results must coexist in C."
  }
}
```

## object_041

### object_041_E1

```json
{
  "video_id": "object_041",
  "edit_id": "object_041_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_041.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Weather Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_outdoor_weather_around_the_zoo_building",
    "target_description": "the outdoor weather around the zoo building",
    "source_state": "The grass and building are lit by direct sunshine.",
    "desired_change": "The outdoor weather becomes lightly overcast with soft diffuse daylight."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the sunny outdoor weather to lightly overcast conditions over the next two seconds.",
  "expected_result": {
    "description": "The outdoor weather becomes lightly overcast with soft diffuse daylight.",
    "target_phrase": "lightly overcast zoo enclosure"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_041_E2A

```json
{
  "video_id": "object_041",
  "edit_id": "object_041_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_041.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_silverback_gorillas",
    "target_description": "the two silverback gorillas",
    "source_state": "The two gorillas occupy changing foreground and background positions.",
    "desired_change": "The two gorillas are positioned side by side with one body width between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the two silverback gorillas side by side with one body width between them.",
  "expected_result": {
    "description": "The two gorillas are positioned side by side with one body width between them.",
    "target_phrase": "two gorillas standing one body width apart"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_041_E2B

```json
{
  "video_id": "object_041",
  "edit_id": "object_041_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_041_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_gorilla_nearest_the_grass_slope",
    "target_description": "the gorilla nearest the grass slope",
    "source_state": "The nearer gorilla continues knuckle-walking across the grass.",
    "desired_change": "The nearer gorilla beats its chest twice while standing on the grass."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the gorilla nearest the grass slope stand and beat its chest twice.",
  "expected_result": {
    "description": "The nearer gorilla beats its chest twice while standing on the grass.",
    "target_phrase": "nearer gorilla beating its chest twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_041_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_041_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the gorilla nearest the grass slope on B independently of E1's change to the outdoor weather around the zoo building; both edit results must coexist in C."
  }
}
```

## object_042

### object_042_E1

```json
{
  "video_id": "object_042",
  "edit_id": "object_042_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_042.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_black_white_and_brown_puppy",
    "target_description": "the black-white-and-brown puppy",
    "source_state": "The puppy approaches, retreats, and crouches while watching its reflection.",
    "desired_change": "The puppy performs three consecutive play bows toward the mirror."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      13,
      20
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the black-white-and-brown puppy perform three consecutive play bows toward the mirror.",
  "expected_result": {
    "description": "The puppy performs three consecutive play bows toward the mirror.",
    "target_phrase": "puppy performing three play bows"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      20
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_042_E2A

```json
{
  "video_id": "object_042",
  "edit_id": "object_042_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_042.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_puppy_and_its_synchronized_reflection",
    "target_description": "the puppy and its synchronized reflection",
    "source_state": "The puppy moves through changing positions immediately in front of the mirror.",
    "desired_change": "The puppy stands at the center of the carpet one body length from the mirror, with its reflection synchronized."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the puppy at the center of the carpet one body length from the mirror.",
  "expected_result": {
    "description": "The puppy stands at the center of the carpet one body length from the mirror, with its reflection synchronized.",
    "target_phrase": "puppy centered one body length from mirror"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_042_E2B

```json
{
  "video_id": "object_042",
  "edit_id": "object_042_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_042_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Paper-collage Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_puppy_and_mirror_scene",
    "target_description": "the full puppy-and-mirror scene",
    "source_state": "The bedroom and mirrored view have a realistic digital-video appearance.",
    "desired_change": "The full scene and its mirrored view are rendered as layered paper collage."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full puppy-and-mirror scene into a layered paper-collage style over the next two seconds.",
  "expected_result": {
    "description": "The full scene and its mirrored view are rendered as layered paper collage.",
    "target_phrase": "layered paper-collage mirror scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_042_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_042_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full puppy-and-mirror scene on B independently of E1's change to the black-white-and-brown puppy; both edit results must coexist in C."
  }
}
```

## object_045

### object_045_E1

```json
{
  "video_id": "object_045",
  "edit_id": "object_045_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Coat Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_larger_ring_tailed_animal_coat",
    "target_description": "the larger ring-tailed animal's coat",
    "source_state": "The larger animal has a coarse gray-black coat and a ringed tail.",
    "desired_change": "The larger animal's gray-black coat becomes warm brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the larger ring-tailed animal's gray-black coat to warm brown over the next two seconds.",
  "expected_result": {
    "description": "The larger animal's gray-black coat becomes warm brown.",
    "target_phrase": "larger animal with warm-brown coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_045_E2A

```json
{
  "video_id": "object_045",
  "edit_id": "object_045_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The fixed framing closely contains the two interacting animals and part of the rock enclosure.",
    "desired_change": "The framing widens to show both animals and the complete enclosure floor."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to show both animals and the complete enclosure floor.",
  "expected_result": {
    "description": "The framing widens to show both animals and the complete enclosure floor.",
    "target_phrase": "wider view of both animals and enclosure"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_045_E2B

```json
{
  "video_id": "object_045",
  "edit_id": "object_045_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_045_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_protruding_rock_pillar_on_the_left",
    "target_description": "the protruding rock pillar on the left",
    "source_state": "A rough pale rock pillar protrudes from the left enclosure wall.",
    "desired_change": "The protruding rock pillar is replaced by a vertical weathered log of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the protruding rock pillar on the left with a vertical weathered log of the same size.",
  "expected_result": {
    "description": "The protruding rock pillar is replaced by a vertical weathered log of the same size.",
    "target_phrase": "vertical weathered log on left"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_045_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_045_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the protruding rock pillar on the left on B independently of E1's change to the larger ring-tailed animal's coat; both edit results must coexist in C."
  }
}
```

## object_046

### object_046_E1

```json
{
  "video_id": "object_046",
  "edit_id": "object_046_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Coat Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_polar_bear_lying_in_the_foreground_snow_pit",
    "target_description": "the polar bear lying in the foreground snow pit",
    "source_state": "The foreground bear has a cream-white coat.",
    "desired_change": "The foreground bear's coat becomes pale golden beige."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.0 seconds, change the foreground polar bear's cream-white coat to pale golden beige over the next two seconds.",
  "expected_result": {
    "description": "The foreground bear's coat becomes pale golden beige.",
    "target_phrase": "foreground bear with pale-golden coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 20.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_046_E2A

```json
{
  "video_id": "object_046",
  "edit_id": "object_046_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_polar_bear_lying_in_the_foreground",
    "target_description": "the polar bear lying in the foreground",
    "source_state": "The lying bear occupies the lower-center snow pit.",
    "desired_change": "The lying bear is positioned on the right side of the same snow pit."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the lying foreground polar bear on the right side of the same snow pit.",
  "expected_result": {
    "description": "The lying bear is positioned on the right side of the same snow pit.",
    "target_phrase": "lying bear on right side of snow pit"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_046_E2B

```json
{
  "video_id": "object_046",
  "edit_id": "object_046_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_046_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_standing_polar_bear_farthest_behind_the_snow_pit",
    "target_description": "the standing polar bear farthest behind the snow pit",
    "source_state": "A standing polar bear is visible far behind the foreground snow pit.",
    "desired_change": "The farthest standing polar bear is removed from the enclosure."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 39.0,
    "effect_end_sec": 40.0,
    "evaluation_window_sec": [
      34.0,
      44.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "foreground bear alone shortly before the standing bears enter"
  },
  "instruction": "At 35.0 seconds, remove the standing polar bear farthest behind the snow pit when it enters the view at 39.0 seconds.",
  "expected_result": {
    "description": "The farthest standing polar bear is removed from the enclosure.",
    "target_phrase": "enclosure without farthest standing bear"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_046_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      44.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Standing polar bears enter the view from about 39 seconds, making the farthest individual identifiable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_046_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the standing polar bear farthest behind the snow pit on B independently of E1's change to the polar bear lying in the foreground snow pit; both edit results must coexist in C."
  }
}
```

## object_047

### object_047_E1

```json
{
  "video_id": "object_047",
  "edit_id": "object_047_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_black_rabbit_and_the_rainbow_colored_ball",
    "target_description": "the black rabbit and the rainbow-colored ball",
    "source_state": "The rabbit pushes the ball in irregular short contacts.",
    "desired_change": "The rabbit makes three deliberate nose pushes against the ball."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      13,
      20
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the black rabbit push the rainbow-colored ball three times with its nose.",
  "expected_result": {
    "description": "The rabbit makes three deliberate nose pushes against the ball.",
    "target_phrase": "rabbit making three nose pushes"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      20
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_047_E2A

```json
{
  "video_id": "object_047",
  "edit_id": "object_047_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Rolling Speed Change",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_rainbow_colored_ball",
    "target_description": "the rainbow-colored ball",
    "source_state": "The ball rolls shorter distances after entering the long-pile rug.",
    "desired_change": "The ball rolls across the rug at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the rainbow-colored ball roll across the rug at half its original speed for five seconds.",
  "expected_result": {
    "description": "The ball rolls across the rug at half its original speed.",
    "target_phrase": "ball rolling at half speed on rug"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_047_E2B

```json
{
  "video_id": "object_047",
  "edit_id": "object_047_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_047_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Colored-pencil Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_room_background_outside_the_rabbit_and_ball",
    "target_description": "the room background outside the rabbit and ball",
    "source_state": "The room background has a realistic indoor-video appearance.",
    "desired_change": "The room background is rendered as a colored-pencil illustration."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the room background as a colored-pencil illustration over the next two seconds.",
  "expected_result": {
    "description": "The room background is rendered as a colored-pencil illustration.",
    "target_phrase": "colored-pencil room background"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_047_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_047_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the room background outside the rabbit and ball on B independently of E1's change to the black rabbit and the rainbow-colored ball; both edit results must coexist in C."
  }
}
```

## object_049

### object_049_E1

```json
{
  "video_id": "object_049",
  "edit_id": "object_049_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Deployment State Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_golf_cart_transparent_windshield",
    "target_description": "the golf cart's transparent windshield",
    "source_state": "The transparent windshield stands upright above the front of the golf cart.",
    "desired_change": "The transparent windshield becomes fully folded down."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the golf cart's transparent windshield from upright to fully folded down.",
  "expected_result": {
    "description": "The transparent windshield becomes fully folded down.",
    "target_phrase": "golf cart with folded windshield"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_049_E2A

```json
{
  "video_id": "object_049",
  "edit_id": "object_049_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Core Object and Environment"
  },
  "target": {
    "target_id": "the_raccoon_and_the_golf_cart",
    "target_description": "the raccoon and the golf cart",
    "source_state": "The raccoon moves between the cart interior, grass, and path.",
    "desired_change": "The raccoon is positioned beside the golf cart's front wheel."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the raccoon beside the golf cart's front wheel.",
  "expected_result": {
    "description": "The raccoon is positioned beside the golf cart's front wheel.",
    "target_phrase": "raccoon beside golf-cart front wheel"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_049_E2B

```json
{
  "video_id": "object_049",
  "edit_id": "object_049_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_049_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_white_cup_mounted_on_the_golf_cart",
    "target_description": "the white cup mounted on the golf cart",
    "source_state": "A white cup is mounted on the golf cart.",
    "desired_change": "The white cup is replaced by a plain red thermos of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the white cup mounted on the golf cart with a plain red thermos of the same size.",
  "expected_result": {
    "description": "The white cup is replaced by a plain red thermos of the same size.",
    "target_phrase": "plain red thermos on golf cart"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_049_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_049_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the white cup mounted on the golf cart on B independently of E1's change to the golf cart's transparent windshield; both edit results must coexist in C."
  }
}
```

## object_053

### object_053_E1

```json
{
  "video_id": "object_053",
  "edit_id": "object_053_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_053.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_heron_beak_and_the_dark_fish",
    "target_description": "the heron's beak and the dark fish",
    "source_state": "The heron repeatedly changes its grip on the fish at irregular intervals.",
    "desired_change": "The heron repositions the fish in its beak three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the heron reposition the dark fish in its beak three times.",
  "expected_result": {
    "description": "The heron repositions the fish in its beak three times.",
    "target_phrase": "heron repositioning fish three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_053_E2A

```json
{
  "video_id": "object_053",
  "edit_id": "object_053_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_053.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_gray_heron",
    "target_description": "the gray heron",
    "source_state": "The heron mainly raises and lowers its head while holding the fish.",
    "desired_change": "The heron takes four deliberate steps through the grass while holding the fish."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the gray heron take four deliberate steps through the grass while holding the fish.",
  "expected_result": {
    "description": "The heron takes four deliberate steps through the grass while holding the fish.",
    "target_phrase": "heron taking four steps with fish"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_053_E2B

```json
{
  "video_id": "object_053",
  "edit_id": "object_053_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_053_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Ink-wash Rendering",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_gray_heron",
    "target_description": "the gray heron",
    "source_state": "The gray heron has a realistic photographic appearance.",
    "desired_change": "The gray heron is rendered as a monochrome ink-wash painting."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the gray heron as a monochrome ink-wash painting over the next two seconds.",
  "expected_result": {
    "description": "The gray heron is rendered as a monochrome ink-wash painting.",
    "target_phrase": "ink-wash gray heron"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_053_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_053_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the gray heron on B independently of E1's change to the heron's beak and the dark fish; both edit results must coexist in C."
  }
}
```

## object_054

### object_054_E1

```json
{
  "video_id": "object_054",
  "edit_id": "object_054_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Surface Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_pale_brown_climbing_rock_wall",
    "target_description": "the pale-brown climbing rock wall",
    "source_state": "The climbing wall has a dry pale-brown rock surface.",
    "desired_change": "The rock wall surface becomes dark slate gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the pale-brown climbing rock wall to dark slate gray over the next two seconds.",
  "expected_result": {
    "description": "The rock wall surface becomes dark slate gray.",
    "target_phrase": "dark slate-gray rock wall"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_054_E2A

```json
{
  "video_id": "object_054",
  "edit_id": "object_054_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_bear_progress_from_the_vertical_wall_to_the_upper_ledge",
    "target_description": "the bear's progress from the vertical wall to the upper ledge",
    "source_state": "The bear reaches the upper ledge after a slow multi-stage climb.",
    "desired_change": "The same climbing progress unfolds at twice its original rate."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "local process retiming"
  },
  "instruction": "Starting at 29.0 seconds, accelerate the bear's climbing progress toward the upper ledge to twice its original rate for six seconds.",
  "expected_result": {
    "description": "The same climbing progress unfolds at twice its original rate.",
    "target_phrase": "bear climbing progress at double speed"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_054_E2B

```json
{
  "video_id": "object_054",
  "edit_id": "object_054_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_054_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_black_bear",
    "target_description": "the black bear",
    "source_state": "The bear climbs mostly upward with small lateral adjustments.",
    "desired_change": "The bear climbs along a wider left-right zigzag route."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the black bear climb along a wider left-right zigzag route for six seconds.",
  "expected_result": {
    "description": "The bear climbs along a wider left-right zigzag route.",
    "target_phrase": "bear climbing along wider zigzag"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_054_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_054_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the black bear on B independently of E1's change to the pale-brown climbing rock wall; both edit results must coexist in C."
  }
}
```

## object_056

### object_056_E1

```json
{
  "video_id": "object_056",
  "edit_id": "object_056_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path and Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_opossum",
    "target_description": "the opossum",
    "source_state": "The opossum changes from slow walking to a rapid direct chase.",
    "desired_change": "The opossum follows a wider arc at half its original speed."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 14.0 seconds, make the opossum follow a wider arc at half its original speed for five seconds.",
  "expected_result": {
    "description": "The opossum follows a wider arc at half its original speed.",
    "target_phrase": "opossum moving in wider slower arc"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_056_E2A

```json
{
  "video_id": "object_056",
  "edit_id": "object_056_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_opossum_and_the_leashed_dog",
    "target_description": "the opossum and the leashed dog",
    "source_state": "The two animals approach, retreat, and later move in a chase formation.",
    "desired_change": "The opossum and the dog circle each other once without contact."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the opossum and the leashed dog circle each other once without contact.",
  "expected_result": {
    "description": "The opossum and the dog circle each other once without contact.",
    "target_phrase": "opossum and dog circling once"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_056_E2B

```json
{
  "video_id": "object_056",
  "edit_id": "object_056_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_056_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Cel-shaded Rendering",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_dog_blue_harness",
    "target_description": "the dog's blue harness",
    "source_state": "The dog's blue harness has a realistic fabric appearance.",
    "desired_change": "The blue harness is rendered as a cel-shaded game asset."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the dog's blue harness as a cel-shaded game asset over the next two seconds.",
  "expected_result": {
    "description": "The blue harness is rendered as a cel-shaded game asset.",
    "target_phrase": "cel-shaded blue dog harness"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_056_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_056_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dog's blue harness on B independently of E1's change to the opossum; both edit results must coexist in C."
  }
}
```

## object_059

### object_059_E1

```json
{
  "video_id": "object_059",
  "edit_id": "object_059_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_059.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Vegetation Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_yellow_brown_kelp_bed",
    "target_description": "the yellow-brown kelp bed",
    "source_state": "The kelp bed is predominantly yellow-brown.",
    "desired_change": "The kelp bed becomes deep green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the yellow-brown kelp bed to deep green over the next two seconds.",
  "expected_result": {
    "description": "The kelp bed becomes deep green.",
    "target_phrase": "deep-green kelp bed"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_059_E2A

```json
{
  "video_id": "object_059",
  "edit_id": "object_059_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_059.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_kelp_fronds_beneath_the_shark",
    "target_description": "the kelp fronds beneath the shark",
    "source_state": "The kelp fronds sway gently beneath the passing shark.",
    "desired_change": "The kelp fronds sway strongly toward the right."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the kelp fronds beneath the shark sway strongly toward the right for five seconds.",
  "expected_result": {
    "description": "The kelp fronds sway strongly toward the right.",
    "target_phrase": "kelp fronds swaying strongly right"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_059_E2B

```json
{
  "video_id": "object_059",
  "edit_id": "object_059_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_059_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_small_companion_fish_beneath_the_shark",
    "target_description": "the small companion fish beneath the shark",
    "source_state": "A small companion fish swims closely beneath the shark's belly.",
    "desired_change": "The small companion fish is removed from beneath the shark."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the small companion fish swimming beneath the shark's belly.",
  "expected_result": {
    "description": "The small companion fish is removed from beneath the shark.",
    "target_phrase": "shark without companion fish below"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_059_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_059_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the small companion fish beneath the shark on B independently of E1's change to the yellow-brown kelp bed; both edit results must coexist in C."
  }
}
```

## object_062

### object_062_E1

```json
{
  "video_id": "object_062",
  "edit_id": "object_062_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Package State Change",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "central_large_display_box_lid",
    "target_description": "the lid of the central large display box",
    "source_state": "The central large display box is closed during the middle display scan.",
    "desired_change": "The central large display box is changed from closed to fully hinged open."
  },
  "timing": {
    "edit_point_sec": 20.0,
    "effect_start_sec": 20.0,
    "effect_end_sec": 21.0,
    "evaluation_window_sec": [
      19.0,
      25.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "middle scan across the large display boxes"
  },
  "instruction": "At 20.0 seconds, change the central large display box from closed to fully hinged open.",
  "expected_result": {
    "description": "The central large display box is shown with its lid fully hinged open.",
    "target_phrase": "central display box hinged open"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.0,
      25.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Large display boxes are clearly visible during the middle horizontal scan, unlike the later front-row blister packs."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_062_E2A

```json
{
  "video_id": "object_062",
  "edit_id": "object_062_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_three_orange_blister_packs",
    "target_description": "the three orange blister packs",
    "source_state": "The three orange blister packs occupy slightly staggered positions near the front row.",
    "desired_change": "The three orange blister packs form one evenly spaced horizontal row."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the three orange blister packs into one evenly spaced horizontal row.",
  "expected_result": {
    "description": "The three orange blister packs form one evenly spaced horizontal row.",
    "target_phrase": "three blister packs in even row"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_062_E2B

```json
{
  "video_id": "object_062",
  "edit_id": "object_062_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_062_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_front_left_silver_package",
    "target_description": "the front-left silver package",
    "source_state": "A small silver package lies at the front-left edge of the display.",
    "desired_change": "The front-left silver package is removed from the display."
  },
  "timing": {
    "edit_point_sec": 35,
    "effect_start_sec": 35,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      34,
      38
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 35.0 seconds, remove the small silver package at the front-left edge of the display.",
  "expected_result": {
    "description": "The front-left silver package is removed from the display.",
    "target_phrase": "display without front-left silver package"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_062_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 35.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_062_E1",
    "must_preserve_e1_result": true,
    "description": "This edit removes the front-left silver package on B independently of E1's opened central display box; both edit results must coexist in C."
  }
}
```

## object_064

### object_064_E1

```json
{
  "video_id": "object_064",
  "edit_id": "object_064_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Body Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_jumping_spider_abdomen",
    "target_description": "the jumping spider's abdomen",
    "source_state": "The jumping spider has a brown-orange abdomen with darker markings.",
    "desired_change": "The abdomen becomes vivid turquoise with the darker markings retained."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the jumping spider's brown-orange abdomen to vivid turquoise over the next two seconds.",
  "expected_result": {
    "description": "The abdomen becomes vivid turquoise with the darker markings retained.",
    "target_phrase": "jumping spider with turquoise abdomen"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_064_E2A

```json
{
  "video_id": "object_064",
  "edit_id": "object_064_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_jumping_spider",
    "target_description": "the jumping spider",
    "source_state": "The jumping spider initially faces toward the camera on the curved white rail.",
    "desired_change": "The jumping spider faces left along the top of the curved rail."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the jumping spider to face left along the top of the curved white rail.",
  "expected_result": {
    "description": "The jumping spider faces left along the top of the curved rail.",
    "target_phrase": "spider facing left along rail"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_064_E2B

```json
{
  "video_id": "object_064",
  "edit_id": "object_064_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_064_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_green_leaf",
    "target_description": "one small green leaf",
    "source_state": "No green leaf lies on the curved white rail beside the spider.",
    "desired_change": "One small green leaf appears on the rail beside the spider."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small green leaf on the curved white rail beside the jumping spider.",
  "expected_result": {
    "description": "One small green leaf appears on the rail beside the spider.",
    "target_phrase": "green leaf beside jumping spider"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_064_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_064_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small green leaf on B independently of E1's change to the jumping spider's abdomen; both edit results must coexist in C."
  }
}
```

## object_066

### object_066_E1

```json
{
  "video_id": "object_066",
  "edit_id": "object_066_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_066.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Pattern Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_foreground_giraffe_dark_patches",
    "target_description": "the foreground giraffe's dark patches",
    "source_state": "The foreground giraffe has dark-brown polygonal patches.",
    "desired_change": "The dark-brown patches become deep burgundy."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the foreground giraffe's dark-brown patches to deep burgundy over the next two seconds.",
  "expected_result": {
    "description": "The dark-brown patches become deep burgundy.",
    "target_phrase": "giraffe with deep-burgundy patches"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_066_E2A

```json
{
  "video_id": "object_066",
  "edit_id": "object_066_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_066.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_foreground_giraffe_and_the_spiral_horned_antelope",
    "target_description": "the foreground giraffe and the spiral-horned antelope",
    "source_state": "The antelope stands close to the giraffe's head, chest, and folded legs.",
    "desired_change": "The two animals stand side by side with one body width between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the foreground giraffe and the spiral-horned antelope side by side with one body width between them.",
  "expected_result": {
    "description": "The two animals stand side by side with one body width between them.",
    "target_phrase": "giraffe and antelope side by side"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_066_E2B

```json
{
  "video_id": "object_066",
  "edit_id": "object_066_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_066_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_background_giraffe_farthest_from_the_foreground_pair",
    "target_description": "the background giraffe farthest from the foreground pair",
    "source_state": "A distant giraffe stands far behind the foreground animals.",
    "desired_change": "The farthest background giraffe is removed from the grassland."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 36.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      28.0,
      40.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "foreground animals leaving shortly before the distant giraffe becomes isolated"
  },
  "instruction": "At 29.0 seconds, remove the background giraffe farthest from the foreground pair when it becomes isolated at 36.0 seconds.",
  "expected_result": {
    "description": "The farthest background giraffe is removed from the grassland.",
    "target_phrase": "grassland without farthest background giraffe"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_066_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      40.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The foreground pair runs out while the distant background giraffe becomes clearly isolated from about 36 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_066_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the background giraffe farthest from the foreground pair on B independently of E1's change to the foreground giraffe's dark patches; both edit results must coexist in C."
  }
}
```

## object_068

### object_068_E1

```json
{
  "video_id": "object_068",
  "edit_id": "object_068_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_frog_and_the_black_hand_brush",
    "target_description": "the frog and the black hand brush",
    "source_state": "The brush makes irregular approaches and brief contacts around the frog.",
    "desired_change": "The brush touches the frog's back lightly three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the black hand brush touch the frog's back lightly three times.",
  "expected_result": {
    "description": "The brush touches the frog's back lightly three times.",
    "target_phrase": "brush touching frog three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_068_E2A

```json
{
  "video_id": "object_068",
  "edit_id": "object_068_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_yellow_brown_frog",
    "target_description": "the small yellow-brown frog",
    "source_state": "The frog makes short avoidance steps and small hops.",
    "desired_change": "The frog performs two long forward jumps across the mat."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the small yellow-brown frog perform two long forward jumps across the mat.",
  "expected_result": {
    "description": "The frog performs two long forward jumps across the mat.",
    "target_phrase": "frog making two long jumps"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_068_E2B

```json
{
  "video_id": "object_068",
  "edit_id": "object_068_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_068_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Clay-animation Rendering",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_black_hand_brush",
    "target_description": "the black hand brush",
    "source_state": "The black hand brush has a realistic plastic-and-bristle appearance.",
    "desired_change": "The black hand brush is rendered as a clay-animation prop."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the black hand brush as a clay-animation prop over the next two seconds.",
  "expected_result": {
    "description": "The black hand brush is rendered as a clay-animation prop.",
    "target_phrase": "clay-animation black hand brush"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_068_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_068_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the black hand brush on B independently of E1's change to the frog and the black hand brush; both edit results must coexist in C."
  }
}
```

## object_069

### object_069_E1

```json
{
  "video_id": "object_069",
  "edit_id": "object_069_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_069.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Hull Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_ferry_red_upper_panels",
    "target_description": "the ferry's red upper panels",
    "source_state": "The high-speed ferry has bright red upper panels above its black-and-white hull.",
    "desired_change": "The red upper panels become cobalt blue."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the ferry's red upper panels to cobalt blue over the next two seconds.",
  "expected_result": {
    "description": "The red upper panels become cobalt blue.",
    "target_phrase": "ferry with cobalt-blue upper panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_069_E2A

```json
{
  "video_id": "object_069",
  "edit_id": "object_069_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_069.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The long-lens framing centers the approaching ferry and crops part of its expanding wake.",
    "desired_change": "The framing widens to show the entire ferry and its full V-shaped wake."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to show the entire ferry and its full V-shaped wake.",
  "expected_result": {
    "description": "The framing widens to show the entire ferry and its full V-shaped wake.",
    "target_phrase": "wide ferry view with full wake"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_069_E2B

```json
{
  "video_id": "object_069",
  "edit_id": "object_069_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_069_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "one_small_white_sailboat",
    "target_description": "one small white sailboat",
    "source_state": "No sailboat is visible on the water to the ferry's left.",
    "desired_change": "One small white sailboat appears on the water to the ferry's left."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small white sailboat on the water to the left of the approaching ferry.",
  "expected_result": {
    "description": "One small white sailboat appears on the water to the ferry's left.",
    "target_phrase": "white sailboat left of ferry"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_069_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_069_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small white sailboat on B independently of E1's change to the ferry's red upper panels; both edit results must coexist in C."
  }
}
```

## object_070

### object_070_E1

```json
{
  "video_id": "object_070",
  "edit_id": "object_070_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_070.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Closure State Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_black_laptop_computer",
    "target_description": "the black laptop computer",
    "source_state": "The black laptop computer is partly open while standing nearly vertical.",
    "desired_change": "The laptop computer becomes fully closed in the same standing position."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the black laptop computer from partly open to fully closed.",
  "expected_result": {
    "description": "The laptop computer becomes fully closed in the same standing position.",
    "target_phrase": "fully closed upright laptop computer"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_070_E2A

```json
{
  "video_id": "object_070",
  "edit_id": "object_070_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_070.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_upright_laptop_computer",
    "target_description": "the upright laptop computer",
    "source_state": "The upright laptop computer remains nearly motionless at the table gap.",
    "desired_change": "The upright laptop computer rocks gently left and right while remaining supported on the table edges."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the upright laptop computer rock gently left and right while remaining supported on the table edges for five seconds.",
  "expected_result": {
    "description": "The upright laptop computer rocks gently left and right while remaining supported on the table edges.",
    "target_phrase": "upright laptop computer rocking gently"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_070_E2B

```json
{
  "video_id": "object_070",
  "edit_id": "object_070_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_070_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_multicolored_bag_below_the_table",
    "target_description": "the multicolored bag below the table",
    "source_state": "A multicolored patterned bag sits below the table gap.",
    "desired_change": "The multicolored bag is replaced by a plain brown cardboard box of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the multicolored bag below the table with a plain brown cardboard box of the same size.",
  "expected_result": {
    "description": "The multicolored bag is replaced by a plain brown cardboard box of the same size.",
    "target_phrase": "plain cardboard box below table"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_070_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_070_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the multicolored bag below the table on B independently of E1's change to the black laptop computer; both edit results must coexist in C."
  }
}
```

## object_071

### object_071_E1

```json
{
  "video_id": "object_071",
  "edit_id": "object_071_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_white_fawn_coat",
    "target_description": "the white fawn's coat",
    "source_state": "The first fawn outside the shelter has an almost uniformly white coat.",
    "desired_change": "The white coat becomes pale silver gray."
  },
  "timing": {
    "edit_point_sec": 19,
    "effect_start_sec": 19,
    "effect_end_sec": 21,
    "evaluation_window_sec": [
      18,
      23
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 19.0 seconds, change the white fawn's coat to pale silver gray over the next two seconds.",
  "expected_result": {
    "description": "The white coat becomes pale silver gray.",
    "target_phrase": "fawn with pale silver-gray coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      18,
      23
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 19.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_071_E2A

```json
{
  "video_id": "object_071",
  "edit_id": "object_071_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Event Reordering",
    "scope": "Multiple Processes"
  },
  "target": {
    "target_id": "the_spotted_fawn_exit_and_the_white_fawn_next_head_lowering",
    "target_description": "the spotted fawn's exit and the white fawn's next head-lowering",
    "source_state": "The spotted fawn crosses the threshold while the white fawn continues lowering and raising its head outside.",
    "desired_change": "The spotted fawn completes its exit before the white fawn next lowers its head."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "relative event reordering"
  },
  "instruction": "Starting at 29.0 seconds, make the spotted fawn complete its exit before the white fawn next lowers its head.",
  "expected_result": {
    "description": "The spotted fawn completes its exit before the white fawn next lowers its head.",
    "target_phrase": "spotted fawn exits before white fawn lowers head"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_071_E2B

```json
{
  "video_id": "object_071",
  "edit_id": "object_071_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_071_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_pale_silver_gray_fawn_and_the_spotted_fawn_outside",
    "target_description": "the pale-silver-gray fawn and the spotted fawn outside",
    "source_state": "The pale-silver-gray fawn produced by E1 and the spotted fawn approach and lower their heads near one another.",
    "desired_change": "The two outside fawns touch noses twice."
  },
  "timing": {
    "edit_point_sec": 34.0,
    "effect_start_sec": 34.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      33.0,
      39.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 34.0 seconds, make the pale-silver-gray fawn and the spotted fawn outside touch noses twice.",
  "expected_result": {
    "description": "The two outside fawns touch noses twice.",
    "target_phrase": "two outside fawns touching noses"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_071_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_071_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the two outside fawns on B while preserving E1's pale-silver-gray coat on the formerly white fawn; both edit results must coexist in C."
  }
}
```

## object_072

### object_072_E1

```json
{
  "video_id": "object_072",
  "edit_id": "object_072_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_072.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Material Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_blue_character_model",
    "target_description": "the blue character model",
    "source_state": "The blue character has a hard painted model surface.",
    "desired_change": "The blue character becomes a soft felt model."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the blue character model from hard painted material to soft felt over the next two seconds.",
  "expected_result": {
    "description": "The blue character becomes a soft felt model.",
    "target_phrase": "blue character made of soft felt"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_072_E2A

```json
{
  "video_id": "object_072",
  "edit_id": "object_072_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_072.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_smaller_gray_purple_character",
    "target_description": "the smaller gray-purple character",
    "source_state": "The smaller gray-purple character remains motionless while facing the blue character.",
    "desired_change": "The smaller gray-purple character waves one forelimb twice."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the smaller gray-purple character wave one forelimb twice.",
  "expected_result": {
    "description": "The smaller gray-purple character waves one forelimb twice.",
    "target_phrase": "smaller character waving twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_072_E2B

```json
{
  "video_id": "object_072",
  "edit_id": "object_072_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_072_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_smaller_gray_purple_character",
    "target_description": "the smaller gray-purple character",
    "source_state": "A smaller gray-purple character faces the blue model in the third shot.",
    "desired_change": "The smaller gray-purple character is removed from the third shot."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the smaller gray-purple character facing the blue model.",
  "expected_result": {
    "description": "The smaller gray-purple character is removed from the third shot.",
    "target_phrase": "blue model alone in third shot"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_072_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_072_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the smaller gray-purple character on B independently of E1's change to the blue character model; both edit results must coexist in C."
  }
}
```

## object_074

### object_074_E1

```json
{
  "video_id": "object_074",
  "edit_id": "object_074_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Operating State Change",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_silver_sedan_headlights",
    "target_description": "the silver sedan's headlights",
    "source_state": "The silver sedan's headlights are switched off.",
    "desired_change": "The headlights become switched on."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the silver sedan's headlights from switched off to switched on.",
  "expected_result": {
    "description": "The headlights become switched on.",
    "target_phrase": "silver sedan with headlights on"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_074_E2A

```json
{
  "video_id": "object_074",
  "edit_id": "object_074_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path and Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_silver_sedan",
    "target_description": "the silver sedan",
    "source_state": "The sedan follows a broad, slow route through the traffic cones.",
    "desired_change": "The sedan follows a tighter curve at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the silver sedan follow a tighter curve at half its original speed for six seconds.",
  "expected_result": {
    "description": "The sedan follows a tighter curve at half its original speed.",
    "target_phrase": "sedan following tighter slower curve"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_074_E2B

```json
{
  "video_id": "object_074",
  "edit_id": "object_074_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_074_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_nearest_orange_traffic_cone",
    "target_description": "the nearest orange traffic cone",
    "source_state": "An orange traffic cone stands nearest the sedan along the marked route.",
    "desired_change": "The nearest orange cone is replaced by a plain blue cone of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the nearest orange traffic cone beside the sedan with a plain blue cone of the same size.",
  "expected_result": {
    "description": "The nearest orange cone is replaced by a plain blue cone of the same size.",
    "target_phrase": "plain blue cone beside sedan"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_074_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_074_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the nearest orange traffic cone on B independently of E1's change to the silver sedan's headlights; both edit results must coexist in C."
  }
}
```

## object_076

### object_076_E1

```json
{
  "video_id": "object_076",
  "edit_id": "object_076_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_076.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_monkey_and_the_small_puppy",
    "target_description": "the monkey and the small puppy",
    "source_state": "The monkey grooms the puppy with irregular hand movements.",
    "desired_change": "The monkey brushes the puppy's back with both hands four times."
  },
  "timing": {
    "edit_point_sec": 12.0,
    "effect_start_sec": 12.0,
    "effect_end_sec": 14.0,
    "evaluation_window_sec": [
      10.0,
      14.5
    ],
    "temporal_behavior": "bounded action",
    "source_stage_at_edit": "end of the first monkey grooming segment before it jumps down"
  },
  "instruction": "Starting at 12.0 seconds, make the monkey brush the small puppy's back with both hands four times.",
  "expected_result": {
    "description": "The monkey brushes the puppy's back with both hands four times.",
    "target_phrase": "monkey brushing puppy four times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      10.0,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The monkey remains beside the puppy and actively grooms it until about 14 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_076_E2A

```json
{
  "video_id": "object_076",
  "edit_id": "object_076_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_076.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_monkey_renewed_grooming_of_the_puppy",
    "target_description": "the monkey's renewed grooming of the puppy",
    "source_state": "The monkey resumes grooming the resting puppy during the final stage.",
    "desired_change": "The renewed grooming pauses for three seconds and then resumes."
  },
  "timing": {
    "edit_point_sec": 36.0,
    "effect_start_sec": 36.0,
    "effect_end_sec": 40.0,
    "evaluation_window_sec": [
      35.0,
      42.0
    ],
    "temporal_behavior": "local pause and resume"
  },
  "instruction": "At 36.0 seconds, pause the monkey's renewed grooming of the puppy for three seconds, then resume it.",
  "expected_result": {
    "description": "The renewed grooming pauses for three seconds and then resumes.",
    "target_phrase": "grooming paused for three seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      35.0,
      42.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_076_E2B

```json
{
  "video_id": "object_076",
  "edit_id": "object_076_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_076_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Muted Pastel Grade",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_monkey_and_puppy_scene",
    "target_description": "the full monkey-and-puppy scene",
    "source_state": "The scene has ordinary digital-video colors and texture.",
    "desired_change": "The full frame receives muted pastel colors and fine paper grain."
  },
  "timing": {
    "edit_point_sec": 27.0,
    "effect_start_sec": 27.0,
    "effect_end_sec": 29.0,
    "evaluation_window_sec": [
      26.0,
      31.0
    ],
    "temporal_behavior": "gradual persistent change",
    "source_stage_at_edit": "continuous monkey-and-puppy platform scene"
  },
  "instruction": "Starting at 27.0 seconds, apply muted pastel colors and fine paper grain to the full monkey-and-puppy scene over the next two seconds.",
  "expected_result": {
    "description": "The full frame receives muted pastel colors and fine paper grain.",
    "target_phrase": "muted pastel scene with paper grain"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_076_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.0,
      31.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The same monkey-and-puppy platform scene remains visible and suitable for a global color treatment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_076_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full monkey-and-puppy scene on B independently of E1's change to the monkey and the small puppy; both edit results must coexist in C."
  }
}
```

## object_083

### object_083_E1

```json
{
  "video_id": "object_083",
  "edit_id": "object_083_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Coat Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_deer_red_brown_coat",
    "target_description": "the deer's red-brown coat",
    "source_state": "The deer has a red-brown coat with a pale rump patch.",
    "desired_change": "The red-brown coat becomes cool gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the deer's red-brown coat to cool gray over the next two seconds.",
  "expected_result": {
    "description": "The red-brown coat becomes cool gray.",
    "target_phrase": "deer with cool-gray coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_083_E2A

```json
{
  "video_id": "object_083",
  "edit_id": "object_083_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_deer",
    "target_description": "the deer",
    "source_state": "The deer stands in the narrow grass strip outside the wooden fence.",
    "desired_change": "The deer is positioned at the center of the gravel shoulder beside the fence."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the deer at the center of the gravel shoulder beside the wooden fence.",
  "expected_result": {
    "description": "The deer is positioned at the center of the gravel shoulder beside the fence.",
    "target_phrase": "deer centered on gravel shoulder"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_083_E2B

```json
{
  "video_id": "object_083",
  "edit_id": "object_083_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_083_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_deer",
    "target_description": "the deer",
    "source_state": "The deer walks, pauses, and probes the fence openings.",
    "desired_change": "The deer makes two short backward hops away from the fence."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the deer perform two short backward hops away from the wooden fence.",
  "expected_result": {
    "description": "The deer makes two short backward hops away from the fence.",
    "target_phrase": "deer making two backward hops"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_083_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_083_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the deer on B independently of E1's change to the deer's red-brown coat; both edit results must coexist in C."
  }
}
```

## object_084

### object_084_E1

```json
{
  "video_id": "object_084",
  "edit_id": "object_084_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Vegetation Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_green_lakeside_grass",
    "target_description": "the green lakeside grass",
    "source_state": "The lakeside grass is medium green.",
    "desired_change": "The lakeside grass becomes deep emerald green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the medium-green lakeside grass to deep emerald green over the next two seconds.",
  "expected_result": {
    "description": "The lakeside grass becomes deep emerald green.",
    "target_phrase": "deep emerald-green lakeside grass"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_084_E2A

```json
{
  "video_id": "object_084",
  "edit_id": "object_084_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_foreground_adult_swan_and_the_nearby_gray_cygnets",
    "target_description": "the foreground adult swan and the nearby gray cygnets",
    "source_state": "The cygnets cluster loosely behind and beside the adult swan.",
    "desired_change": "The cygnets form one evenly spaced row behind the adult swan."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the nearby gray cygnets into one evenly spaced row behind the foreground adult swan.",
  "expected_result": {
    "description": "The cygnets form one evenly spaced row behind the adult swan.",
    "target_phrase": "cygnets aligned behind adult swan"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_084_E2B

```json
{
  "video_id": "object_084",
  "edit_id": "object_084_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_084_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_large_gray_stone_nearest_the_pond_edge",
    "target_description": "the large gray stone nearest the pond edge",
    "source_state": "A large gray stone lies nearest the pond edge behind the foreground swans.",
    "desired_change": "The large gray stone is removed from the lakeside grass."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the large gray stone nearest the pond edge behind the foreground swans.",
  "expected_result": {
    "description": "The large gray stone is removed from the lakeside grass.",
    "target_phrase": "lakeside grass without nearest gray stone"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_084_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_084_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large gray stone nearest the pond edge on B independently of E1's change to the green lakeside grass; both edit results must coexist in C."
  }
}
```

## object_085

### object_085_E1

```json
{
  "video_id": "object_085",
  "edit_id": "object_085_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_active_lion_and_the_small_dark_ball",
    "target_description": "the active lion and the small dark ball",
    "source_state": "The active lion paws and noses the small dark ball near the left side of the enclosure.",
    "desired_change": "The active lion rolls the small dark ball steadily forward with its nose for five seconds."
  },
  "timing": {
    "edit_point_sec": 12.0,
    "effect_start_sec": 12.0,
    "effect_end_sec": 17.0,
    "evaluation_window_sec": [
      11.0,
      18.0
    ],
    "temporal_behavior": "bounded action",
    "source_stage_at_edit": "end of the active lion's interaction with the small dark ball"
  },
  "instruction": "Starting at 12.0 seconds, make the active lion roll the small dark ball steadily forward with its nose for five seconds.",
  "expected_result": {
    "description": "The active lion rolls the small dark ball steadily forward with its nose for five seconds.",
    "target_phrase": "lion steadily rolling small dark ball"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.0,
      18.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The active lion and small dark ball are clearly identifiable at the edit point, and the continuous fixed-camera view supports evaluating the extended five-second interaction."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_085_E2A

```json
{
  "video_id": "object_085",
  "edit_id": "object_085_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_lion_resting_beside_the_left_wall",
    "target_description": "the lion resting beside the left wall",
    "source_state": "The left lion remains side-lying with only small head and paw movements.",
    "desired_change": "The resting lion stretches both forelegs forward twice."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the lion resting beside the left wall stretch both forelegs forward twice.",
  "expected_result": {
    "description": "The resting lion stretches both forelegs forward twice.",
    "target_phrase": "resting lion stretching forelegs twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_085_E2B

```json
{
  "video_id": "object_085",
  "edit_id": "object_085_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_085_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Charcoal-sketch Rendering",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_lion_resting_beside_the_left_wall",
    "target_description": "the lion resting beside the left wall",
    "source_state": "The resting lion has a realistic fur appearance.",
    "desired_change": "The resting lion is rendered as a charcoal sketch."
  },
  "timing": {
    "edit_point_sec": 27.0,
    "effect_start_sec": 27.0,
    "effect_end_sec": 29.0,
    "evaluation_window_sec": [
      26.0,
      31.0
    ],
    "temporal_behavior": "gradual persistent change",
    "source_stage_at_edit": "active lion approaching the pale ball while the resting lion remains at the wall"
  },
  "instruction": "Starting at 27.0 seconds, render the lion resting beside the left wall as a charcoal sketch over the next two seconds.",
  "expected_result": {
    "description": "The resting lion is rendered as a charcoal sketch.",
    "target_phrase": "charcoal-sketch resting lion"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_085_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.0,
      31.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The resting lion remains visible beside the left wall throughout this interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_085_E1",
    "must_preserve_e1_result": true,
    "description": "This edit renders the lion resting beside the left wall on B while preserving E1's active lion rolling the small dark ball forward with its nose; both edit results must coexist in C."
  }
}
```

## object_088

### object_088_E1

```json
{
  "video_id": "object_088",
  "edit_id": "object_088_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_088.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_black_and_white_cat_black_fur",
    "target_description": "the black-and-white cat's black fur",
    "source_state": "The right cat has black fur across its back and tail with a white chest and paws.",
    "desired_change": "The black fur becomes medium gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the black-and-white cat's black fur to medium gray over the next two seconds.",
  "expected_result": {
    "description": "The black fur becomes medium gray.",
    "target_phrase": "cat with medium-gray and white fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_088_E2A

```json
{
  "video_id": "object_088",
  "edit_id": "object_088_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_088.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_black_and_white_cat",
    "target_description": "the black-and-white cat",
    "source_state": "The black-and-white cat faces the white cat at close range.",
    "desired_change": "The black-and-white cat faces directly away from the white cat."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the black-and-white cat to face directly away from the white cat.",
  "expected_result": {
    "description": "The black-and-white cat faces directly away from the white cat.",
    "target_phrase": "black-white cat facing away from white cat"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_088_E2B

```json
{
  "video_id": "object_088",
  "edit_id": "object_088_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_088_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_white_cat",
    "target_description": "the white cat",
    "source_state": "The white cat remains seated with only small head and ear movements.",
    "desired_change": "The white cat turns in one complete circle on the ground."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the white cat turn in one complete circle on the ground.",
  "expected_result": {
    "description": "The white cat turns in one complete circle on the ground.",
    "target_phrase": "white cat turning one complete circle"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_088_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_088_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the white cat on B independently of E1's change to the black-and-white cat's black fur; both edit results must coexist in C."
  }
}
```

## object_090

### object_090_E1

```json
{
  "video_id": "object_090",
  "edit_id": "object_090_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Water Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_shallow_river_water",
    "target_description": "the shallow river water",
    "source_state": "The shallow river water is muted gray-brown.",
    "desired_change": "The river water becomes clear blue-green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the shallow river water from muted gray-brown to clear blue-green over the next two seconds.",
  "expected_result": {
    "description": "The river water becomes clear blue-green.",
    "target_phrase": "clear blue-green shallow river"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_090_E2A

```json
{
  "video_id": "object_090",
  "edit_id": "object_090_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_elephant_group_convergence_around_the_smaller_elephant",
    "target_description": "the elephant group's convergence around the smaller elephant",
    "source_state": "The adult elephants have begun moving closer around the smaller elephant but have not yet formed the surrounding group.",
    "desired_change": "The convergence proceeds at twice its original rate, with the adult elephants forming a close group around the smaller elephant by 27 seconds."
  },
  "timing": {
    "edit_point_sec": 23.0,
    "effect_start_sec": 23.0,
    "effect_end_sec": 27.0,
    "evaluation_window_sec": [
      22.0,
      30.0
    ],
    "temporal_behavior": "local process retiming",
    "source_stage_at_edit": "adult elephants beginning to converge around the smaller elephant"
  },
  "instruction": "Starting at 23.0 seconds, accelerate the adult elephants' convergence to twice its original rate, forming a close group around the smaller elephant by 27.0 seconds.",
  "expected_result": {
    "description": "The adult elephants converge at twice the original rate and form a close group around the smaller elephant by 27 seconds.",
    "target_phrase": "accelerated convergence around the smaller elephant"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22.0,
      30.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "From about 22 seconds, the adult elephants visibly begin closing in, and by about 29 seconds they surround the smaller elephant."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_090_E2B

```json
{
  "video_id": "object_090",
  "edit_id": "object_090_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_090_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_water_splashes_around_the_smaller_elephant",
    "target_description": "the water splashes around the smaller elephant",
    "source_state": "The smaller elephant's movements create irregular low splashes in the shallow water.",
    "desired_change": "The splashes spread outward in three broad rings."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the water splashes around the smaller elephant spread outward in three broad rings.",
  "expected_result": {
    "description": "The splashes spread outward in three broad rings.",
    "target_phrase": "three broad splash rings around smaller elephant"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_090_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_090_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the water splashes around the smaller elephant on B independently of E1's change to the shallow river water; both edit results must coexist in C."
  }
}
```

## object_093

### object_093_E1

```json
{
  "video_id": "object_093",
  "edit_id": "object_093_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_093.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_helicopter_landing_skid_and_the_traffic_cone",
    "target_description": "the helicopter's landing skid and the traffic cone",
    "source_state": "The landing skid lifts the traffic cone once during the source operation.",
    "desired_change": "The landing skid lifts the traffic cone twice in separate contacts."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      13,
      24
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the helicopter's landing skid lift the traffic cone twice in separate contacts.",
  "expected_result": {
    "description": "The landing skid lifts the traffic cone twice in separate contacts.",
    "target_phrase": "landing skid lifting cone twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_093_E2A

```json
{
  "video_id": "object_093",
  "edit_id": "object_093_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_093.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_helicopter_cone_transport_and_release",
    "target_description": "the helicopter's remaining transport and release of the traffic cone",
    "source_state": "The helicopter has already lifted the traffic cone and is beginning to transport it before returning it to the grass.",
    "desired_change": "The remaining transport and release proceeds at twice its original rate, with the traffic cone returned to the grass by 34 seconds."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "local process retiming",
    "source_stage_at_edit": "traffic cone already lifted and entering the transport phase"
  },
  "instruction": "Starting at 29.0 seconds, accelerate the helicopter's remaining transport and release of the traffic cone to twice its original rate, returning it to the grass by 34.0 seconds.",
  "expected_result": {
    "description": "The helicopter transports and releases the already-lifted traffic cone at twice the original rate, returning it to the grass by 34 seconds.",
    "target_phrase": "accelerated cone transport and release"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "At 29 seconds the cone is already lifted; the remaining visible process consists of transport followed by release back onto the grass."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_093_E2B

```json
{
  "video_id": "object_093",
  "edit_id": "object_093_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_093_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1960s Aviation-film Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_helicopter_field_scene",
    "target_description": "the full helicopter field scene",
    "source_state": "The helicopter footage has a modern digital-video appearance.",
    "desired_change": "The full frame resembles a 1960s color aviation film."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full helicopter field scene into a 1960s color aviation film over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1960s color aviation film.",
    "target_phrase": "1960s color aviation film"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_093_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_093_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full helicopter field scene on B independently of E1's change to the helicopter's landing skid and the traffic cone; both edit results must coexist in C."
  }
}
```

## object_094

### object_094_E1

```json
{
  "video_id": "object_094",
  "edit_id": "object_094_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_094.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fuselage Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_helicopter_red_fuselage_panels",
    "target_description": "the helicopter's red fuselage panels",
    "source_state": "The aerobatic helicopter has bright red fuselage panels with black-and-white markings.",
    "desired_change": "The red fuselage panels become emerald green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the helicopter's red fuselage panels to emerald green over the next two seconds.",
  "expected_result": {
    "description": "The red fuselage panels become emerald green.",
    "target_phrase": "helicopter with emerald-green panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_094_E2A

```json
{
  "video_id": "object_094",
  "edit_id": "object_094_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_094.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Side Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_aerial_camera_trajectory",
    "target_description": "the aerial camera trajectory",
    "source_state": "The handheld camera follows the aerobatic helicopter with rapid changes in angle and zoom.",
    "desired_change": "The camera tracks the helicopter smoothly from a constant side angle."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the aerobatic helicopter smoothly from a constant side angle for five seconds.",
  "expected_result": {
    "description": "The camera tracks the helicopter smoothly from a constant side angle.",
    "target_phrase": "smooth side tracking of aerobatic helicopter"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_094_E2B

```json
{
  "video_id": "object_094",
  "edit_id": "object_094_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_094_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_large_white_cloud_behind_the_helicopter",
    "target_description": "the large white cloud behind the helicopter",
    "source_state": "A large dense white cloud lies behind the helicopter's flight path.",
    "desired_change": "The dense cloud is replaced by a thin elongated cloud in the same location."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the large dense cloud behind the helicopter with a thin elongated cloud.",
  "expected_result": {
    "description": "The dense cloud is replaced by a thin elongated cloud in the same location.",
    "target_phrase": "thin elongated cloud behind helicopter"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_094_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_094_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large white cloud behind the helicopter on B independently of E1's change to the helicopter's red fuselage panels; both edit results must coexist in C."
  }
}
```

## object_095

### object_095_E1

```json
{
  "video_id": "object_095",
  "edit_id": "object_095_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_dog_white_coat",
    "target_description": "the dog's white coat",
    "source_state": "The long-haired dog has a predominantly white coat.",
    "desired_change": "The white coat becomes pale golden cream."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the long-haired dog's white coat to pale golden cream over the next two seconds.",
  "expected_result": {
    "description": "The white coat becomes pale golden cream.",
    "target_phrase": "dog with pale-golden coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_095_E2A

```json
{
  "video_id": "object_095",
  "edit_id": "object_095_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_dogs_final_run_toward_the_snow_edge",
    "target_description": "the dog's final run from sitting toward the snow edge",
    "source_state": "After rising from sitting, the dog runs toward the snow edge at its original pace.",
    "desired_change": "The dog's final run progresses at twice its original rate and reaches the snow edge by 44.0 seconds."
  },
  "timing": {
    "edit_point_sec": 42.0,
    "effect_start_sec": 42.0,
    "effect_end_sec": 44.0,
    "evaluation_window_sec": [
      41.0,
      45.5
    ],
    "temporal_behavior": "local pause and resume",
    "source_stage_at_edit": "dog rising from sitting and beginning its final run toward the snow edge"
  },
  "instruction": "Starting at 42.0 seconds, make the dog's final run toward the snow edge progress at twice its original rate, reaching the edge by 44.0 seconds.",
  "expected_result": {
    "description": "The dog completes its final run from sitting to the snow edge at twice the original rate and reaches the edge by 44.0 seconds.",
    "target_phrase": "dog reaching the snow edge by 44 seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      41.0,
      45.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dog rises near 42 seconds and begins the final running segment toward the snow edge before the video ends."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_095_E2B

```json
{
  "video_id": "object_095",
  "edit_id": "object_095_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_095_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path and Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_leashed_dog",
    "target_description": "the leashed dog",
    "source_state": "The dog follows short direct paths across the snow-covered road.",
    "desired_change": "The dog follows a wider zigzag route at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the leashed dog follow a wider zigzag route at half its original speed for six seconds.",
  "expected_result": {
    "description": "The dog follows a wider zigzag route at half its original speed.",
    "target_phrase": "dog moving in wider slower zigzag"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_095_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_095_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the leashed dog on B independently of E1's change to the dog's white coat; both edit results must coexist in C."
  }
}
```

## object_096

### object_096_E1

```json
{
  "video_id": "object_096",
  "edit_id": "object_096_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Surface Wetness Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_capuchin_monkeys_fur",
    "target_description": "the capuchin monkey's visible fur",
    "source_state": "The capuchin monkey's fur is dry, with individually visible strands.",
    "desired_change": "The monkey's fur becomes visibly wet, with lightly clumped strands."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the capuchin monkey's dry fur to visibly wet fur with lightly clumped strands over the next two seconds.",
  "expected_result": {
    "description": "The capuchin monkey's fur appears visibly wet, with lightly clumped strands.",
    "target_phrase": "capuchin monkey with visibly wet fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.0,
      18.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The close view clearly shows the capuchin monkey's head, chest, and arm fur throughout the selected interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_096_E2A

```json
{
  "video_id": "object_096",
  "edit_id": "object_096_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_seated_monkey",
    "target_description": "the seated monkey",
    "source_state": "The monkey sits left of center on the wooden table.",
    "desired_change": "The monkey is positioned at the center of the wooden table."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the seated monkey at the center of the wooden table.",
  "expected_result": {
    "description": "The monkey is positioned at the center of the wooden table.",
    "target_phrase": "monkey centered on wooden table"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_096_E2B

```json
{
  "video_id": "object_096",
  "edit_id": "object_096_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_096_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "one_red_apple",
    "target_description": "one red apple",
    "source_state": "No red apple is present beside the banana pieces on the table.",
    "desired_change": "One red apple appears beside the banana pieces."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one red apple beside the banana pieces on the wooden table.",
  "expected_result": {
    "description": "One red apple appears beside the banana pieces.",
    "target_phrase": "red apple beside banana pieces"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_096_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_096_E1",
    "must_preserve_e1_result": true,
    "description": "This edit adds one red apple beside the banana pieces on B while preserving E1's visibly wet, lightly clumped fur on the capuchin monkey; both edit results must coexist in C."
  }
}
```

## object_099

### object_099_E1

```json
{
  "video_id": "object_099",
  "edit_id": "object_099_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Stripe Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_adult_tiger_black_stripes",
    "target_description": "the adult tiger's black stripes",
    "source_state": "The adult tiger has black stripes over an orange coat.",
    "desired_change": "The black stripes become dark blue."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.0 seconds, change the adult tiger's black stripes to dark blue over the next two seconds.",
  "expected_result": {
    "description": "The black stripes become dark blue.",
    "target_phrase": "adult tiger with dark-blue stripes"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 20.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_099_E2A

```json
{
  "video_id": "object_099",
  "edit_id": "object_099_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The tracking view alternately crops members of the tiger family and the waiting vehicles.",
    "desired_change": "The framing widens to show the adult tiger, both cubs, and both waiting vehicles together."
  },
  "timing": {
    "edit_point_sec": 38.0,
    "effect_start_sec": 38.0,
    "effect_end_sec": 42.0,
    "evaluation_window_sec": [
      37.0,
      44.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 38.0 seconds, zoom out smoothly over four seconds to show the adult tiger, both cubs, and both waiting vehicles.",
  "expected_result": {
    "description": "The framing widens to show the adult tiger, both cubs, and both waiting vehicles together.",
    "target_phrase": "wide view of tiger family and vehicles"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      37.0,
      44.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_099_E2B

```json
{
  "video_id": "object_099",
  "edit_id": "object_099_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_099_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_dry_leaves_behind_the_crossing_tigers",
    "target_description": "the dry leaves behind the crossing tigers",
    "source_state": "The dry leaves shift only slightly as the tigers cross the road edge.",
    "desired_change": "The dry leaves rise and swirl behind the tiger family."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 38.0,
    "effect_end_sec": 43.0,
    "evaluation_window_sec": [
      34.0,
      45.0
    ],
    "temporal_behavior": "bounded environmental motion",
    "source_stage_at_edit": "tiger family nearing the road before the crossing begins"
  },
  "instruction": "At 35.0 seconds, make the dry leaves behind the tiger family rise and swirl when the road crossing begins at 38.0 seconds.",
  "expected_result": {
    "description": "The dry leaves rise and swirl behind the tiger family.",
    "target_phrase": "dry leaves swirling behind tiger family"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_099_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      45.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tiger family begins crossing the road around 38 seconds with dry leaves visible behind its route."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_099_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dry leaves behind the crossing tigers on B independently of E1's change to the adult tiger's black stripes; both edit results must coexist in C."
  }
}
```

## object_101

### object_101_E1

```json
{
  "video_id": "object_101",
  "edit_id": "object_101_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_101.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Operating State Change",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_all_terrain_vehicle_headlights",
    "target_description": "the all-terrain vehicle's headlights",
    "source_state": "The all-terrain vehicle's headlights are switched off.",
    "desired_change": "The headlights become switched on."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the all-terrain vehicle's headlights from switched off to switched on.",
  "expected_result": {
    "description": "The headlights become switched on.",
    "target_phrase": "ATV with headlights switched on"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_101_E2A

```json
{
  "video_id": "object_101",
  "edit_id": "object_101_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_101.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_all_terrain_vehicle",
    "target_description": "the all-terrain vehicle",
    "source_state": "The vehicle travels around changing parts of the dirt circuit.",
    "desired_change": "The vehicle is positioned directly before the central dirt ramp."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the all-terrain vehicle directly before the central dirt ramp.",
  "expected_result": {
    "description": "The vehicle is positioned directly before the central dirt ramp.",
    "target_phrase": "ATV directly before central ramp"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_101_E2B

```json
{
  "video_id": "object_101",
  "edit_id": "object_101_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_101_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_plain_blue_traffic_cone",
    "target_description": "one plain blue traffic cone",
    "source_state": "No blue traffic cone stands beside the central dirt ramp.",
    "desired_change": "One plain blue traffic cone appears beside the central dirt ramp."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one plain blue traffic cone beside the central dirt ramp.",
  "expected_result": {
    "description": "One plain blue traffic cone appears beside the central dirt ramp.",
    "target_phrase": "blue cone beside central dirt ramp"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_101_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_101_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one plain blue traffic cone on B independently of E1's change to the all-terrain vehicle's headlights; both edit results must coexist in C."
  }
}
```

## object_102

### object_102_E1

```json
{
  "video_id": "object_102",
  "edit_id": "object_102_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_102.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_squirrel_and_the_long_haired_cat",
    "target_description": "the squirrel and the long-haired cat",
    "source_state": "The squirrel makes irregular paw contacts with the cat's neck and back fur.",
    "desired_change": "The squirrel pats the cat's upper back four times with both forepaws."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the squirrel pat the long-haired cat's upper back four times with both forepaws.",
  "expected_result": {
    "description": "The squirrel pats the cat's upper back four times with both forepaws.",
    "target_phrase": "squirrel patting cat four times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_102_E2A

```json
{
  "video_id": "object_102",
  "edit_id": "object_102_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_102.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_squirrel_and_the_cat",
    "target_description": "the squirrel and the cat",
    "source_state": "The squirrel moves through changing positions along the cat's back.",
    "desired_change": "The squirrel is positioned at the center of the cat's back."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the squirrel at the center of the long-haired cat's back.",
  "expected_result": {
    "description": "The squirrel is positioned at the center of the cat's back.",
    "target_phrase": "squirrel centered on cat back"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_102_E2B

```json
{
  "video_id": "object_102",
  "edit_id": "object_102_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_102_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Watercolor Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_office_background_outside_the_cat_and_squirrel",
    "target_description": "the office background outside the cat and squirrel",
    "source_state": "The office background has a realistic digital-video appearance.",
    "desired_change": "The office background is rendered as a soft watercolor painting."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the office background as a soft watercolor painting over the next two seconds.",
  "expected_result": {
    "description": "The office background is rendered as a soft watercolor painting.",
    "target_phrase": "watercolor office background"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_102_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_102_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the office background outside the cat and squirrel on B independently of E1's change to the squirrel and the long-haired cat; both edit results must coexist in C."
  }
}
```

## object_104

### object_104_E1

```json
{
  "video_id": "object_104",
  "edit_id": "object_104_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_104.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Coat Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_buffalo_dark_coat",
    "target_description": "the buffalo's dark coat",
    "source_state": "The buffalo has a dark black-brown coat.",
    "desired_change": "The dark coat becomes pale ash gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the buffalo's dark black-brown coat to pale ash gray over the next two seconds.",
  "expected_result": {
    "description": "The dark coat becomes pale ash gray.",
    "target_phrase": "buffalo with pale ash-gray coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_104_E2A

```json
{
  "video_id": "object_104",
  "edit_id": "object_104_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_104.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_buffalo_and_the_two_nearest_lions",
    "target_description": "the buffalo and the two nearest lions",
    "source_state": "The lions pursue from changing rear and side-rear positions.",
    "desired_change": "The two nearest lions are positioned side by side two body lengths behind the buffalo."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the two nearest lions side by side two body lengths behind the buffalo.",
  "expected_result": {
    "description": "The two nearest lions are positioned side by side two body lengths behind the buffalo.",
    "target_phrase": "two lions aligned behind buffalo"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_104_E2B

```json
{
  "video_id": "object_104",
  "edit_id": "object_104_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_104_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_palm_shaped_shrub_nearest_the_chase_path",
    "target_description": "the palm-shaped shrub nearest the chase path",
    "source_state": "A palm-shaped shrub stands nearest the chase path.",
    "desired_change": "The palm-shaped shrub is replaced by a gray boulder of similar size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the palm-shaped shrub nearest the chase path with a gray boulder of similar size.",
  "expected_result": {
    "description": "The palm-shaped shrub is replaced by a gray boulder of similar size.",
    "target_phrase": "gray boulder beside chase path"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_104_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_104_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the palm-shaped shrub nearest the chase path on B independently of E1's change to the buffalo's dark coat; both edit results must coexist in C."
  }
}
```

## object_106

### object_106_E1

```json
{
  "video_id": "object_106",
  "edit_id": "object_106_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_106.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_peacock_and_the_brown_red_chicken",
    "target_description": "the peacock and the brown-red chicken",
    "source_state": "The two birds make irregular close approaches and wing movements.",
    "desired_change": "The peacock and the chicken touch their extended wing tips three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the peacock and the brown-red chicken touch their extended wing tips three times.",
  "expected_result": {
    "description": "The peacock and the chicken touch their extended wing tips three times.",
    "target_phrase": "birds touching wing tips three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_106_E2A

```json
{
  "video_id": "object_106",
  "edit_id": "object_106_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_106.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_peacock_and_the_chicken",
    "target_description": "the peacock and the chicken",
    "source_state": "The birds alternate between following, side-by-side movement, and separation.",
    "desired_change": "The two birds stand side by side with two body lengths between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the peacock and the chicken side by side with two body lengths between them.",
  "expected_result": {
    "description": "The two birds stand side by side with two body lengths between them.",
    "target_phrase": "birds standing two body lengths apart"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_106_E2B

```json
{
  "video_id": "object_106",
  "edit_id": "object_106_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_106_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Oil-painting Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_grassland_bird_scene",
    "target_description": "the full grassland bird scene",
    "source_state": "The grassland footage has a realistic wildlife-video appearance.",
    "desired_change": "The full scene is rendered as a textured oil painting."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full grassland bird scene into a textured oil-painting style over the next two seconds.",
  "expected_result": {
    "description": "The full scene is rendered as a textured oil painting.",
    "target_phrase": "oil-painted grassland bird scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_106_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_106_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full grassland bird scene on B independently of E1's change to the peacock and the brown-red chicken; both edit results must coexist in C."
  }
}
```

## object_107

### object_107_E1

```json
{
  "video_id": "object_107",
  "edit_id": "object_107_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_107.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Skin Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_rhinoceros_gray_brown_skin",
    "target_description": "the rhinoceros's gray-brown skin",
    "source_state": "The rhinoceros has gray-brown skin under warm grassland light.",
    "desired_change": "The skin becomes cool slate gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the rhinoceros's gray-brown skin to cool slate gray over the next two seconds.",
  "expected_result": {
    "description": "The skin becomes cool slate gray.",
    "target_phrase": "rhinoceros with slate-gray skin"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_107_E2A

```json
{
  "video_id": "object_107",
  "edit_id": "object_107_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_107.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_rhinoceros",
    "target_description": "the rhinoceros",
    "source_state": "The rhinoceros gradually turns from a side view toward a side-rear heading.",
    "desired_change": "The rhinoceros faces directly away from the camera."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the rhinoceros to face directly away from the camera.",
  "expected_result": {
    "description": "The rhinoceros faces directly away from the camera.",
    "target_phrase": "rhinoceros facing directly away"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_107_E2B

```json
{
  "video_id": "object_107",
  "edit_id": "object_107_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_107_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_isolated_tall_grass_clump_directly_before_the_rhinoceros",
    "target_description": "the isolated tall grass clump directly before the rhinoceros",
    "source_state": "An isolated tall grass clump stands directly before the rhinoceros's route.",
    "desired_change": "The isolated grass clump is removed from the route."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the isolated tall grass clump directly before the rhinoceros.",
  "expected_result": {
    "description": "The isolated grass clump is removed from the route.",
    "target_phrase": "route without isolated grass clump"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_107_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_107_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the isolated tall grass clump directly before the rhinoceros on B independently of E1's change to the rhinoceros's gray-brown skin; both edit results must coexist in C."
  }
}
```

## object_110

### object_110_E1

```json
{
  "video_id": "object_110",
  "edit_id": "object_110_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_110.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Vegetation Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_seagrass_on_the_seabed",
    "target_description": "the seagrass on the seabed",
    "source_state": "The seabed vegetation is muted green-brown.",
    "desired_change": "The seagrass becomes deep emerald green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the muted green-brown seagrass to deep emerald green over the next two seconds.",
  "expected_result": {
    "description": "The seagrass becomes deep emerald green.",
    "target_phrase": "deep emerald-green seagrass"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_110_E2A

```json
{
  "video_id": "object_110",
  "edit_id": "object_110_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_110.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Turn Rate Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_submerged_hippo",
    "target_description": "the submerged hippo",
    "source_state": "The hippo turns from a frontal approach into a rearward departure at a slow rate.",
    "desired_change": "The hippo turns at half its original rate."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the submerged hippo turn at half its original rate for five seconds.",
  "expected_result": {
    "description": "The hippo turns at half its original rate.",
    "target_phrase": "submerged hippo turning at half rate"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_110_E2B

```json
{
  "video_id": "object_110",
  "edit_id": "object_110_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_110_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_submerged_hippo",
    "target_description": "the submerged hippo",
    "source_state": "The hippo follows a broad gradual path away from the camera.",
    "desired_change": "The hippo follows a tighter clockwise arc above the seabed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the submerged hippo follow a tighter clockwise arc above the seabed for six seconds.",
  "expected_result": {
    "description": "The hippo follows a tighter clockwise arc above the seabed.",
    "target_phrase": "hippo following tighter clockwise arc"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_110_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_110_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the submerged hippo on B independently of E1's change to the seagrass on the seabed; both edit results must coexist in C."
  }
}
```

## object_112

### object_112_E1

```json
{
  "video_id": "object_112",
  "edit_id": "object_112_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_112.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_tabby_kitten_and_the_yellow_feather_toy",
    "target_description": "the tabby kitten and the yellow feather toy",
    "source_state": "The kitten makes rapid irregular paw contacts with the moving feather.",
    "desired_change": "The kitten bats the yellow feather four times with alternating forepaws."
  },
  "timing": {
    "edit_point_sec": 14.0,
    "effect_start_sec": 14.0,
    "effect_end_sec": 19.0,
    "evaluation_window_sec": [
      13.0,
      21.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the tabby kitten bat the yellow feather four times with alternating forepaws.",
  "expected_result": {
    "description": "The kitten bats the yellow feather four times with alternating forepaws.",
    "target_phrase": "kitten batting feather four times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.0,
      21.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_112_E2A

```json
{
  "video_id": "object_112",
  "edit_id": "object_112_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_112.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tabby_kitten",
    "target_description": "the tabby kitten",
    "source_state": "The kitten crouches, turns, and makes short pounces toward the feather.",
    "desired_change": "The kitten rolls over twice beside the red flower-shaped toys."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the tabby kitten roll over twice beside the red flower-shaped toys.",
  "expected_result": {
    "description": "The kitten rolls over twice beside the red flower-shaped toys.",
    "target_phrase": "kitten rolling over twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_112_E2B

```json
{
  "video_id": "object_112",
  "edit_id": "object_112_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_112_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Clay-animation Rendering",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_yellow_feather_toy",
    "target_description": "the yellow feather toy",
    "source_state": "The yellow feather toy has a realistic soft feather appearance.",
    "desired_change": "The yellow feather is rendered as a clay-animation prop."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the yellow feather toy as a clay-animation prop over the next two seconds.",
  "expected_result": {
    "description": "The yellow feather is rendered as a clay-animation prop.",
    "target_phrase": "clay-animation yellow feather toy"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_112_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_112_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the yellow feather toy on B independently of E1's change to the tabby kitten and the yellow feather toy; both edit results must coexist in C."
  }
}
```

## object_113

### object_113_E1

```json
{
  "video_id": "object_113",
  "edit_id": "object_113_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_113.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Wing Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_stunt_kite_yellow_green_wing_panels",
    "target_description": "the stunt kite's yellow-green wing panels",
    "source_state": "The stunt kite has yellow-green wing panels with dark borders.",
    "desired_change": "The yellow-green panels become bright cyan."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the stunt kite's yellow-green wing panels to bright cyan over the next two seconds.",
  "expected_result": {
    "description": "The yellow-green panels become bright cyan.",
    "target_phrase": "stunt kite with bright-cyan panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_113_E2A

```json
{
  "video_id": "object_113",
  "edit_id": "object_113_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_113.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Moving Subject Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_tracking_trajectory",
    "target_description": "the camera movement tracking the stunt kite",
    "source_state": "The handheld camera follows the stunt kite with uneven framing as the kite changes direction.",
    "desired_change": "The camera moves smoothly with the stunt kite and keeps it within the central region of the frame for five seconds."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, move the camera smoothly to follow the stunt kite, keeping it within the central region of the frame for five seconds.",
  "expected_result": {
    "description": "The moving camera tracks the stunt kite smoothly and keeps it within the central region of the frame for five seconds.",
    "target_phrase": "smooth centered tracking of the stunt kite"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stunt kite remains visible while changing position and direction, providing a clear subject for continuous moving-camera tracking."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_113_E2B

```json
{
  "video_id": "object_113",
  "edit_id": "object_113_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_113_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_stunt_kite",
    "target_description": "the stunt kite",
    "source_state": "The kite alternates broad dives, climbs, and turns.",
    "desired_change": "The kite follows four compact alternating zigzags."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the stunt kite follow four compact alternating zigzags over six seconds.",
  "expected_result": {
    "description": "The kite follows four compact alternating zigzags.",
    "target_phrase": "kite following four compact zigzags"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_113_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_113_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the stunt kite on B independently of E1's change to the stunt kite's yellow-green wing panels; both edit results must coexist in C."
  }
}
```

## object_117

### object_117_E1

```json
{
  "video_id": "object_117",
  "edit_id": "object_117_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_117.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Deployment State Change",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_robot_toy_two_back_wing_panels",
    "target_description": "the robot toy's two back wing panels",
    "source_state": "The robot toy's two back wing panels are folded against its body.",
    "desired_change": "Both back wing panels become fully extended."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the robot toy's two back wing panels from folded to fully extended.",
  "expected_result": {
    "description": "Both back wing panels become fully extended.",
    "target_phrase": "robot toy with extended back wings"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_117_E2A

```json
{
  "video_id": "object_117",
  "edit_id": "object_117_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_117.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_expanded_robot_form_turntable_rotation",
    "target_description": "the expanded robot form's turntable rotation",
    "source_state": "The expanded robot form rotates continuously on its display stand.",
    "desired_change": "The turntable rotation pauses for three seconds and then resumes."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "local pause and resume"
  },
  "instruction": "At 29.0 seconds, pause the expanded robot form's turntable rotation for three seconds, then resume it.",
  "expected_result": {
    "description": "The turntable rotation pauses for three seconds and then resumes.",
    "target_phrase": "robot display rotation paused three seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_117_E2B

```json
{
  "video_id": "object_117",
  "edit_id": "object_117_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_117_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_expanded_robot_toy_arms",
    "target_description": "the expanded robot toy's arms",
    "source_state": "The expanded robot toy rotates with its arm joints largely fixed.",
    "desired_change": "The robot swings both arms outward twice."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the expanded robot toy swing both arms outward twice.",
  "expected_result": {
    "description": "The robot swings both arms outward twice.",
    "target_phrase": "expanded robot swinging arms twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_117_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_117_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the expanded robot toy's arms on B independently of E1's change to the robot toy's two back wing panels; both edit results must coexist in C."
  }
}
```

## object_120

### object_120_E1

```json
{
  "video_id": "object_120",
  "edit_id": "object_120_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_120.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Lighting Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_overcast_marine_illumination",
    "target_description": "the overcast marine illumination",
    "source_state": "The passenger ship is lit by flat cool overcast daylight.",
    "desired_change": "Warm low-angle light illuminates the ship and wave crests."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the flat cool marine light to warm low-angle illumination over the next two seconds.",
  "expected_result": {
    "description": "Warm low-angle light illuminates the ship and wave crests.",
    "target_phrase": "passenger ship in warm low-angle light"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_120_E2A

```json
{
  "video_id": "object_120",
  "edit_id": "object_120_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_120.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The long-lens framing centers the approaching ship while cropping parts of the rough surrounding sea.",
    "desired_change": "The framing widens to show the entire ship and both sides of its bow wake."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to show the entire ship and both sides of its bow wake.",
  "expected_result": {
    "description": "The framing widens to show the entire ship and both sides of its bow wake.",
    "target_phrase": "wide passenger ship and bow wake view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_120_E2B

```json
{
  "video_id": "object_120",
  "edit_id": "object_120_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_120_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Pitch Amplitude Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_passenger_ship",
    "target_description": "the passenger ship",
    "source_state": "The passenger ship pitches noticeably over the rough wave crests.",
    "desired_change": "The ship pitches with half its original vertical amplitude."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the passenger ship pitch with half its original vertical amplitude for six seconds.",
  "expected_result": {
    "description": "The ship pitches with half its original vertical amplitude.",
    "target_phrase": "ship pitching at half amplitude"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_120_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_120_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the passenger ship on B independently of E1's change to the overcast marine illumination; both edit results must coexist in C."
  }
}
```

## object_121

### object_121_E1

```json
{
  "video_id": "object_121",
  "edit_id": "object_121_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_121.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_adult_tigers",
    "target_description": "the two adult tigers",
    "source_state": "The two tigers make brief irregular nose and face contact beside the fence.",
    "desired_change": "The two tigers touch noses and alternately tap each other's foreleg three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the two adult tigers touch noses and alternately tap each other's foreleg three times.",
  "expected_result": {
    "description": "The two tigers touch noses and alternately tap each other's foreleg three times.",
    "target_phrase": "tigers touching noses and tapping forelegs"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_121_E2A

```json
{
  "video_id": "object_121",
  "edit_id": "object_121_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_121.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_adult_tigers",
    "target_description": "the two adult tigers",
    "source_state": "The tigers repeatedly overlap and change their relative positions along the fence.",
    "desired_change": "The tigers are positioned side by side with one body width between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the two adult tigers side by side with one body width between them.",
  "expected_result": {
    "description": "The tigers are positioned side by side with one body width between them.",
    "target_phrase": "tigers standing one body width apart"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_121_E2B

```json
{
  "video_id": "object_121",
  "edit_id": "object_121_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_121_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Colored-pencil Rendering",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_two_adult_tigers",
    "target_description": "the two adult tigers",
    "source_state": "The two tigers have a realistic wildlife-video appearance.",
    "desired_change": "The two tigers are rendered as detailed colored-pencil illustrations."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the two adult tigers as detailed colored-pencil illustrations over the next two seconds.",
  "expected_result": {
    "description": "The two tigers are rendered as detailed colored-pencil illustrations.",
    "target_phrase": "colored-pencil adult tigers"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_121_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_121_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the two adult tigers on B independently of E1's change to the two adult tigers; both edit results must coexist in C."
  }
}
```

## object_122

### object_122_E1

```json
{
  "video_id": "object_122",
  "edit_id": "object_122_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_122.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Skin Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_shark_light_gray_dorsal_skin",
    "target_description": "the small shark's light-gray dorsal skin",
    "source_state": "The small shark has light-gray-brown dorsal skin with darker fin tips.",
    "desired_change": "The dorsal skin becomes pale blue-gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the small shark's light-gray dorsal skin to pale blue-gray over the next two seconds.",
  "expected_result": {
    "description": "The dorsal skin becomes pale blue-gray.",
    "target_phrase": "small shark with pale-blue-gray dorsal skin"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_122_E2A

```json
{
  "video_id": "object_122",
  "edit_id": "object_122_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_122.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_shark",
    "target_description": "the small shark",
    "source_state": "The shark cruises through changing positions above the white sand.",
    "desired_change": "The shark is positioned at the center of the clear sandy channel."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the small shark at the center of the clear sandy channel.",
  "expected_result": {
    "description": "The shark is positioned at the center of the clear sandy channel.",
    "target_phrase": "small shark centered over sandy channel"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_122_E2B

```json
{
  "video_id": "object_122",
  "edit_id": "object_122_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_122_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_shark",
    "target_description": "the small shark",
    "source_state": "The shark follows broad gentle curves through the shallow water.",
    "desired_change": "The shark follows a tighter clockwise arc."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the small shark follow a tighter clockwise arc through the shallow water for six seconds.",
  "expected_result": {
    "description": "The shark follows a tighter clockwise arc.",
    "target_phrase": "small shark following tighter clockwise arc"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_122_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_122_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the small shark on B independently of E1's change to the small shark's light-gray dorsal skin; both edit results must coexist in C."
  }
}
```

## object_123

### object_123_E1

```json
{
  "video_id": "object_123",
  "edit_id": "object_123_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_123.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_adult_zebras",
    "target_description": "the two adult zebras",
    "source_state": "The zebras rear and make irregular foreleg contact around each other's shoulders.",
    "desired_change": "The zebras rear together and place both forelegs across each other's shoulders twice."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      11.0,
      19.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 13.0 seconds, make the two adult zebras rear together and place both forelegs across each other's shoulders twice.",
  "expected_result": {
    "description": "The zebras rear together and place both forelegs across each other's shoulders twice.",
    "target_phrase": "zebras rearing and placing forelegs together"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.0,
      19.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_123_E2A

```json
{
  "video_id": "object_123",
  "edit_id": "object_123_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_123.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_adult_zebras",
    "target_description": "the two adult zebras",
    "source_state": "The zebras remain close and repeatedly overlap while changing positions.",
    "desired_change": "The zebras face each other with one body length between them."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the two adult zebras facing each other with one body length between them.",
  "expected_result": {
    "description": "The zebras face each other with one body length between them.",
    "target_phrase": "zebras facing one body length apart"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_123_E2B

```json
{
  "video_id": "object_123",
  "edit_id": "object_123_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_123_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Oil-painting Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_zebra_enclosure_scene",
    "target_description": "the full zebra enclosure scene",
    "source_state": "The enclosure footage has a realistic wildlife-video appearance.",
    "desired_change": "The full scene is rendered as a textured oil painting."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 28.0 seconds, transform the full zebra enclosure scene into a textured oil-painting style over the next two seconds.",
  "expected_result": {
    "description": "The full scene is rendered as a textured oil painting.",
    "target_phrase": "oil-painted zebra enclosure scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_123_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_123_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full zebra enclosure scene on B independently of E1's change to the two adult zebras; both edit results must coexist in C."
  }
}
```

## object_125

### object_125_E1

```json
{
  "video_id": "object_125",
  "edit_id": "object_125_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_125.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_squirrel_gray_brown_dorsal_fur",
    "target_description": "the squirrel's gray-brown dorsal fur",
    "source_state": "The squirrel has gray-brown dorsal fur and a pale underside.",
    "desired_change": "The dorsal fur becomes warm reddish brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the squirrel's gray-brown dorsal fur to warm reddish brown over the next two seconds.",
  "expected_result": {
    "description": "The dorsal fur becomes warm reddish brown.",
    "target_phrase": "squirrel with reddish-brown dorsal fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_125_E2A

```json
{
  "video_id": "object_125",
  "edit_id": "object_125_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_125.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_squirrel",
    "target_description": "the squirrel",
    "source_state": "The squirrel explores changing positions between the wall, snow, and exposed ground.",
    "desired_change": "The squirrel is positioned beside the base of the black container."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the squirrel beside the base of the black container near the wall.",
  "expected_result": {
    "description": "The squirrel is positioned beside the base of the black container.",
    "target_phrase": "squirrel beside black container"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_125_E2B

```json
{
  "video_id": "object_125",
  "edit_id": "object_125_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_125_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_pine_cone",
    "target_description": "one small plain pine cone",
    "source_state": "No pine cone is present beside the squirrel on the exposed ground.",
    "desired_change": "One small plain pine cone appears beside the squirrel."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain pine cone on the exposed ground beside the squirrel.",
  "expected_result": {
    "description": "One small plain pine cone appears beside the squirrel.",
    "target_phrase": "small pine cone beside squirrel"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_125_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_125_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain pine cone on B independently of E1's change to the squirrel's gray-brown dorsal fur; both edit results must coexist in C."
  }
}
```

## object_127

### object_127_E1

```json
{
  "video_id": "object_127",
  "edit_id": "object_127_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_127.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_active_opossum_and_the_supine_opossum",
    "target_description": "the active opossum and the supine opossum",
    "source_state": "The active opossum makes irregular nose and paw contact with the supine opossum.",
    "desired_change": "The active opossum gently touches the supine opossum's shoulder twice with its nose and forepaw."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the active opossum gently touch the supine opossum's shoulder twice with its nose and forepaw.",
  "expected_result": {
    "description": "The active opossum gently touches the supine opossum's shoulder twice with its nose and forepaw.",
    "target_phrase": "active opossum touching supine opossum"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_127_E2A

```json
{
  "video_id": "object_127",
  "edit_id": "object_127_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_127.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_active_opossum",
    "target_description": "the active opossum",
    "source_state": "The active opossum walks away briefly and later returns from an irregular route.",
    "desired_change": "The active opossum circles the supine opossum once."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the active opossum circle the supine opossum once over five seconds.",
  "expected_result": {
    "description": "The active opossum circles the supine opossum once.",
    "target_phrase": "active opossum circling supine opossum"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_127_E2B

```json
{
  "video_id": "object_127",
  "edit_id": "object_127_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_127_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Surface Wetness Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_dry_grass_surrounding_the_two_opossums",
    "target_description": "the dry pale grass immediately surrounding the two opossums",
    "source_state": "The grass immediately surrounding the two opossums is dry and pale.",
    "desired_change": "The grass immediately surrounding the two opossums becomes visibly wet and darker."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "wide view of both opossums on dry pale grass"
  },
  "instruction": "Starting at 29.0 seconds, change the dry pale grass around the two opossums to visibly wet, darker grass over the next two seconds.",
  "expected_result": {
    "description": "The grass immediately surrounding the two opossums appears visibly wet and darker.",
    "target_phrase": "wet darker grass around the two opossums"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_127_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A wide, unobstructed area of dry pale grass surrounds both opossums throughout the selected interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_127_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the grass on B while preserving E1's two gentle touches between the active and supine opossums; both edit results must coexist in C."
  }
}
```

## object_128

### object_128_E1

```json
{
  "video_id": "object_128",
  "edit_id": "object_128_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_128.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Transparency State Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_curved_transparent_container_wall",
    "target_description": "the curved transparent container wall",
    "source_state": "The curved container wall is transparent and reveals the substrate behind it.",
    "desired_change": "The curved wall becomes evenly frosted and translucent."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.0 seconds, change the curved transparent container wall to evenly frosted translucent plastic over the next two seconds.",
  "expected_result": {
    "description": "The curved wall becomes evenly frosted and translucent.",
    "target_phrase": "frosted translucent container wall"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 20.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_128_E2A

```json
{
  "video_id": "object_128",
  "edit_id": "object_128_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_128.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tiny_red_brown_arachnid",
    "target_description": "the tiny red-brown arachnid",
    "source_state": "The arachnid crawls through changing positions on the wall, gravel, and liner.",
    "desired_change": "The arachnid is positioned at the center of the white liner."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 35.0,
    "effect_end_sec": 36.0,
    "evaluation_window_sec": [
      34.0,
      38.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 35.0 seconds, reposition the tiny red-brown arachnid at the center of the white liner.",
  "expected_result": {
    "description": "The arachnid is positioned at the center of the white liner.",
    "target_phrase": "arachnid centered on white liner"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      38.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_128_E2B

```json
{
  "video_id": "object_128",
  "edit_id": "object_128_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_128_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tiny_red_brown_arachnid",
    "target_description": "the tiny red-brown arachnid",
    "source_state": "The arachnid crawls continuously with all legs close to the surface.",
    "desired_change": "The arachnid raises its front pair of legs three times."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 35.0,
    "effect_end_sec": 39.0,
    "evaluation_window_sec": [
      34.0,
      41.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 35.0 seconds, make the tiny red-brown arachnid raise its front pair of legs three times.",
  "expected_result": {
    "description": "The arachnid raises its front pair of legs three times.",
    "target_phrase": "arachnid raising front legs three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_128_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      41.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_128_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tiny red-brown arachnid on B independently of E1's change to the curved transparent container wall; both edit results must coexist in C."
  }
}
```

## object_130

### object_130_E1

```json
{
  "video_id": "object_130",
  "edit_id": "object_130_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_130.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Water Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_shallow_wetland_channel",
    "target_description": "the shallow wetland channel",
    "source_state": "The shallow channel has muted green-brown water with reflected vegetation.",
    "desired_change": "The channel water becomes clear turquoise."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the shallow wetland channel from muted green-brown to clear turquoise over the next two seconds.",
  "expected_result": {
    "description": "The channel water becomes clear turquoise.",
    "target_phrase": "clear turquoise wetland channel"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_130_E2A

```json
{
  "video_id": "object_130",
  "edit_id": "object_130_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_130.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_lions_separation_into_the_water_and_grass_routes",
    "target_description": "the lions' separation into the water and grass routes",
    "source_state": "The two lions separate gradually as one enters water and the other moves across grass.",
    "desired_change": "The same separation progress unfolds at twice its original rate."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "local process retiming"
  },
  "instruction": "Starting at 29.0 seconds, accelerate the lions' separation into the water and grass routes to twice its original rate for six seconds.",
  "expected_result": {
    "description": "The same separation progress unfolds at twice its original rate.",
    "target_phrase": "lion separation progress at double speed"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_130_E2B

```json
{
  "video_id": "object_130",
  "edit_id": "object_130_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_130_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_isolated_tall_grass_clump_nearest_the_water_channel",
    "target_description": "the isolated tall grass clump nearest the water channel",
    "source_state": "An isolated tall grass clump stands nearest the water channel beside the lions.",
    "desired_change": "The grass clump is replaced by a gray boulder of similar size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the isolated tall grass clump nearest the water channel with a gray boulder of similar size.",
  "expected_result": {
    "description": "The grass clump is replaced by a gray boulder of similar size.",
    "target_phrase": "gray boulder beside water channel"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_130_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_130_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the isolated tall grass clump nearest the water channel on B independently of E1's change to the shallow wetland channel; both edit results must coexist in C."
  }
}
```

## object_135

### object_135_E1

```json
{
  "video_id": "object_135",
  "edit_id": "object_135_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_135.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Pattern Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_monitor_lizard_pale_dorsal_spots",
    "target_description": "the monitor lizard's pale dorsal spots",
    "source_state": "The monitor lizard has pale gray spots and bands over dark skin.",
    "desired_change": "The pale markings become muted gold."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the monitor lizard's pale dorsal spots and bands to muted gold over the next two seconds.",
  "expected_result": {
    "description": "The pale markings become muted gold.",
    "target_phrase": "monitor lizard with muted-gold markings"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_135_E2A

```json
{
  "video_id": "object_135",
  "edit_id": "object_135_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_135.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed and Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_monitor_lizard",
    "target_description": "the monitor lizard",
    "source_state": "The monitor lizard walks slowly through changing curves around people's feet.",
    "desired_change": "The monitor lizard follows a wider curve at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the monitor lizard follow a wider curve at half its original speed for six seconds.",
  "expected_result": {
    "description": "The monitor lizard follows a wider curve at half its original speed.",
    "target_phrase": "monitor lizard taking wider slower curve"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_135_E2B

```json
{
  "video_id": "object_135",
  "edit_id": "object_135_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_135_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Charcoal-sketch Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_indoor_floor_and_surrounding_background_outside_the_monitor_lizard",
    "target_description": "the indoor floor and surrounding background outside the monitor lizard",
    "source_state": "The indoor background has a realistic digital-video appearance.",
    "desired_change": "The background is rendered as a soft charcoal sketch."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the indoor background outside the monitor lizard as a soft charcoal sketch over the next two seconds.",
  "expected_result": {
    "description": "The background is rendered as a soft charcoal sketch.",
    "target_phrase": "charcoal-sketch background around monitor lizard"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_135_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_135_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the indoor floor and surrounding background outside the monitor lizard on B independently of E1's change to the monitor lizard's pale dorsal spots; both edit results must coexist in C."
  }
}
```

## object_138

### object_138_E1

```json
{
  "video_id": "object_138",
  "edit_id": "object_138_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_138.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_two_orange_white_fish_and_the_fallen_red_container",
    "target_description": "the two orange-white fish and the fallen red container",
    "source_state": "The two orange-white fish pass the fallen red container along irregular routes.",
    "desired_change": "The two orange-white fish circle the fallen red container once in opposite directions."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the two orange-white fish circle the fallen red container once in opposite directions.",
  "expected_result": {
    "description": "The two orange-white fish circle the fallen red container once in opposite directions.",
    "target_phrase": "orange-white fish circling red container"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_138_E2A

```json
{
  "video_id": "object_138",
  "edit_id": "object_138_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_138.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Object Motion",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_white_tubular_tool",
    "target_description": "the white tubular tool",
    "source_state": "The white tubular tool enters from outside the frame and moves irregularly through the water.",
    "desired_change": "The white tubular tool traces three slow circles above the substrate."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded supporting motion"
  },
  "instruction": "Starting at 29.0 seconds, make the white tubular tool trace three slow circles above the aquarium substrate.",
  "expected_result": {
    "description": "The white tubular tool traces three slow circles above the substrate.",
    "target_phrase": "white tube tracing three slow circles"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_138_E2B

```json
{
  "video_id": "object_138",
  "edit_id": "object_138_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_138_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_white_tubular_tool",
    "target_description": "the white tubular tool",
    "source_state": "A white tubular tool extends into the aquarium from outside the frame.",
    "desired_change": "The white tubular tool is removed from the aquarium."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the white tubular tool extending into the aquarium from outside the frame.",
  "expected_result": {
    "description": "The white tubular tool is removed from the aquarium.",
    "target_phrase": "aquarium without white tubular tool"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_138_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_138_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the white tubular tool on B independently of E1's change to the two orange-white fish and the fallen red container; both edit results must coexist in C."
  }
}
```

## object_140

### object_140_E1

```json
{
  "video_id": "object_140",
  "edit_id": "object_140_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_140.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Operating State Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_nearest_illuminated_courtyard_lamp",
    "target_description": "the nearest illuminated courtyard lamp",
    "source_state": "The nearest courtyard lamp is switched on and emits warm light.",
    "desired_change": "The lamp becomes switched off."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the nearest illuminated courtyard lamp from switched on to switched off.",
  "expected_result": {
    "description": "The lamp becomes switched off.",
    "target_phrase": "nearest courtyard lamp switched off"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_140_E2A

```json
{
  "video_id": "object_140",
  "edit_id": "object_140_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_140.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The handheld framing frequently crops parts of the wall, path, and grass while following the fox.",
    "desired_change": "The framing widens to include the fox, paved path, low wall, and raised grass together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to show the fox, paved path, low wall, and raised grass together.",
  "expected_result": {
    "description": "The framing widens to include the fox, paved path, low wall, and raised grass together.",
    "target_phrase": "wide fox courtyard view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_140_E2B

```json
{
  "video_id": "object_140",
  "edit_id": "object_140_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_140_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_fox",
    "target_description": "the red fox",
    "source_state": "The fox walks along the wall at a variable natural speed.",
    "desired_change": "The fox walks at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the red fox walk along the low wall at half its original speed for six seconds.",
  "expected_result": {
    "description": "The fox walks at half its original speed.",
    "target_phrase": "red fox walking at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_140_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_140_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red fox on B independently of E1's change to the nearest illuminated courtyard lamp; both edit results must coexist in C."
  }
}
```

## object_144

### object_144_E1

```json
{
  "video_id": "object_144",
  "edit_id": "object_144_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_144.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_small_puppy_and_the_pink_plush_toy",
    "target_description": "the small puppy and the pink plush toy",
    "source_state": "The puppy pulls, paws, and bites the soft toy with irregular repetitions.",
    "desired_change": "The puppy pins the pink plush toy with both forepaws and shakes it from side to side three times."
  },
  "timing": {
    "edit_point_sec": 19.0,
    "effect_start_sec": 19.0,
    "effect_end_sec": 24.0,
    "evaluation_window_sec": [
      18.0,
      26.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 19.0 seconds, make the small puppy pin the pink plush toy with both forepaws and shake it from side to side three times.",
  "expected_result": {
    "description": "The puppy pins the pink plush toy with both forepaws and shakes it from side to side three times.",
    "target_phrase": "puppy pinning and shaking plush toy"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      18.0,
      26.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_144_E2A

```json
{
  "video_id": "object_144",
  "edit_id": "object_144_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_144.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_small_puppy_and_the_pink_plush_toy",
    "target_description": "the small puppy and the pink plush toy",
    "source_state": "The toy changes position beside and beneath the puppy during play.",
    "desired_change": "The toy is positioned between the puppy's two forepaws."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the pink plush toy between the small puppy's two forepaws.",
  "expected_result": {
    "description": "The toy is positioned between the puppy's two forepaws.",
    "target_phrase": "plush toy between puppy forepaws"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_144_E2B

```json
{
  "video_id": "object_144",
  "edit_id": "object_144_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_144_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Felt-stop-motion Rendering",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_puppy",
    "target_description": "the small puppy",
    "source_state": "The puppy has a realistic short-haired appearance.",
    "desired_change": "The puppy is rendered as a handcrafted felt stop-motion character."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, render the small puppy as a handcrafted felt stop-motion character over the next two seconds.",
  "expected_result": {
    "description": "The puppy is rendered as a handcrafted felt stop-motion character.",
    "target_phrase": "felt stop-motion puppy"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_144_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_144_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the small puppy on B independently of E1's change to the small puppy and the pink plush toy; both edit results must coexist in C."
  }
}
```

## object_145

### object_145_E1

```json
{
  "video_id": "object_145",
  "edit_id": "object_145_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_145.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Moisture State Change",
    "scope": "Core Object Surface"
  },
  "target": {
    "target_id": "the_wet_mud_coating_the_elephant_calf",
    "target_description": "the wet mud coating the elephant calf",
    "source_state": "The calf's lower body is coated with dark wet mud.",
    "desired_change": "The mud coating becomes dry and lightly cracked."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the wet mud coating the elephant calf to dry lightly cracked mud over the next two seconds.",
  "expected_result": {
    "description": "The mud coating becomes dry and lightly cracked.",
    "target_phrase": "calf coated with dry cracked mud"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_145_E2A

```json
{
  "video_id": "object_145",
  "edit_id": "object_145_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_145.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_elephant_calf_and_the_three_surrounding_adult_elephants",
    "target_description": "the elephant calf and the three surrounding adult elephants",
    "source_state": "The calf remains in a low central pit while the adults change their surrounding positions.",
    "desired_change": "The calf is centered between the three adult elephants with equal spacing to each adult."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the elephant calf centrally between the three adult elephants with equal spacing to each adult.",
  "expected_result": {
    "description": "The calf is centered between the three adult elephants with equal spacing to each adult.",
    "target_phrase": "calf centered between three adult elephants"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_145_E2B

```json
{
  "video_id": "object_145",
  "edit_id": "object_145_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_145_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_elephant_calf_trunk",
    "target_description": "the elephant calf's trunk",
    "source_state": "The calf extends and curls its trunk irregularly while attempting to move.",
    "desired_change": "The calf lifts and curls its trunk overhead three times."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the elephant calf lift and curl its trunk overhead three times.",
  "expected_result": {
    "description": "The calf lifts and curls its trunk overhead three times.",
    "target_phrase": "elephant calf curling trunk overhead"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_145_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_145_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the elephant calf's trunk on B independently of E1's change to the wet mud coating the elephant calf; both edit results must coexist in C."
  }
}
```

## object_147

### object_147_E1

```json
{
  "video_id": "object_147",
  "edit_id": "object_147_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_147.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Exterior Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_locomotive_unmarked_black_hood_panels",
    "target_description": "the locomotive's unmarked black hood panels",
    "source_state": "The locomotive has black hood panels surrounding protected white markings.",
    "desired_change": "The unmarked black hood panels become deep forest green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the locomotive's unmarked black hood panels to deep forest green over the next two seconds.",
  "expected_result": {
    "description": "The unmarked black hood panels become deep forest green.",
    "target_phrase": "locomotive with forest-green hood panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_147_E2A

```json
{
  "video_id": "object_147",
  "edit_id": "object_147_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_147.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_diesel_locomotive",
    "target_description": "the diesel locomotive",
    "source_state": "The locomotive remains in a broad side view along the parallel railway.",
    "desired_change": "The locomotive faces directly to the right along the far track."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the diesel locomotive to face directly right along the far parallel track.",
  "expected_result": {
    "description": "The locomotive faces directly to the right along the far track.",
    "target_phrase": "locomotive facing right along track"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_147_E2B

```json
{
  "video_id": "object_147",
  "edit_id": "object_147_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_147_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_foreground_grass_beside_the_parallel_railway",
    "target_description": "the foreground grass beside the parallel railway",
    "source_state": "The foreground grass blurs laterally with limited independent movement.",
    "desired_change": "The foreground grass forms two broad bending waves as the train passes."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the foreground grass beside the parallel railway form two broad bending waves as the train passes.",
  "expected_result": {
    "description": "The foreground grass forms two broad bending waves as the train passes.",
    "target_phrase": "foreground grass forming two bending waves"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_147_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_147_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the foreground grass beside the parallel railway on B independently of E1's change to the locomotive's unmarked black hood panels; both edit results must coexist in C."
  }
}
```

## object_148

### object_148_E1

```json
{
  "video_id": "object_148",
  "edit_id": "object_148_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_148.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cat_orange_fur",
    "target_description": "the cat's orange fur",
    "source_state": "The cat has warm orange short fur and a darker tail.",
    "desired_change": "The orange fur becomes pale cream."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the orange cat's fur to pale cream over the next two seconds.",
  "expected_result": {
    "description": "The orange fur becomes pale cream.",
    "target_phrase": "cat with pale-cream fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_148_E2A

```json
{
  "video_id": "object_148",
  "edit_id": "object_148_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_148.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Stabilized Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld long-lens camera follows the cat with abrupt pans and occasional loss of focus.",
    "desired_change": "The camera tracks the cat smoothly from a constant elevated side angle."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the cat smoothly from a constant elevated side angle for five seconds.",
  "expected_result": {
    "description": "The camera tracks the cat smoothly from a constant elevated side angle.",
    "target_phrase": "smooth elevated side tracking of cat"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_148_E2B

```json
{
  "video_id": "object_148",
  "edit_id": "object_148_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_148_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_isolated_reddish_brown_branch_in_the_lower_foreground",
    "target_description": "the isolated reddish-brown branch in the lower foreground",
    "source_state": "An isolated reddish-brown branch enters the lower foreground over the grass.",
    "desired_change": "The isolated branch is removed from the foreground."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the isolated reddish-brown branch from the lower foreground of the grass scene.",
  "expected_result": {
    "description": "The isolated branch is removed from the foreground.",
    "target_phrase": "grass foreground without reddish branch"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_148_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_148_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the isolated reddish-brown branch in the lower foreground on B independently of E1's change to the cat's orange fur; both edit results must coexist in C."
  }
}
```

## object_153

### object_153_E1

```json
{
  "video_id": "object_153",
  "edit_id": "object_153_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_153.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Jaw State Change",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_crocodile_jaws",
    "target_description": "the crocodile's jaws",
    "source_state": "The crocodile's jaws are closed while it lies in the shallow water.",
    "desired_change": "The jaws become half open."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the crocodile's jaws from closed to a half-open state.",
  "expected_result": {
    "description": "The jaws become half open.",
    "target_phrase": "crocodile with half-open jaws"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_153_E2A

```json
{
  "video_id": "object_153",
  "edit_id": "object_153_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_153.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Event Reordering",
    "scope": "Multiple Processes"
  },
  "target": {
    "target_id": "the_lionesses_encirclement_and_the_crocodile_defensive_twist",
    "target_description": "the lionesses' encirclement and the crocodile's defensive twist",
    "source_state": "The lionesses close in while the crocodile's defensive motion begins with partial overlap.",
    "desired_change": "All three lionesses complete the encirclement before the crocodile begins its next defensive twist."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "local event reordering"
  },
  "instruction": "Starting at 29.0 seconds, reorder the actions so all three lionesses encircle the crocodile before its next defensive twist begins.",
  "expected_result": {
    "description": "All three lionesses complete the encirclement before the crocodile begins its next defensive twist.",
    "target_phrase": "encirclement completed before defensive twist"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_153_E2B

```json
{
  "video_id": "object_153",
  "edit_id": "object_153_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_153_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_isolated_gray_riverbank_rock_nearest_the_crocodile",
    "target_description": "the isolated gray riverbank rock nearest the crocodile",
    "source_state": "An isolated gray rock lies on the muddy bank nearest the crocodile.",
    "desired_change": "The rock is replaced by a pale driftwood log of similar size."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the isolated gray riverbank rock nearest the crocodile with pale driftwood of similar size.",
  "expected_result": {
    "description": "The rock is replaced by a pale driftwood log of similar size.",
    "target_phrase": "pale driftwood beside crocodile"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_153_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_153_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the isolated gray riverbank rock nearest the crocodile on B independently of E1's change to the crocodile's jaws; both edit results must coexist in C."
  }
}
```

## object_154

### object_154_E1

```json
{
  "video_id": "object_154",
  "edit_id": "object_154_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_154.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Airframe Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_aircraft_unmarked_white_fuselage_panels",
    "target_description": "the aircraft's unmarked white fuselage panels",
    "source_state": "The aircraft has white fuselage panels around small protected markings.",
    "desired_change": "The unmarked white panels become bright silver."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the aircraft's unmarked white fuselage panels to bright silver over the next two seconds.",
  "expected_result": {
    "description": "The unmarked white panels become bright silver.",
    "target_phrase": "aircraft with bright-silver fuselage panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_154_E2A

```json
{
  "video_id": "object_154",
  "edit_id": "object_154_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_154.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Low-angle Side Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The distant camera follows the taxiing aircraft from changing elevated angles.",
    "desired_change": "The camera tracks the aircraft smoothly from a constant low side angle."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the taxiing aircraft smoothly from a constant low side angle for five seconds.",
  "expected_result": {
    "description": "The camera tracks the aircraft smoothly from a constant low side angle.",
    "target_phrase": "low side tracking of taxiing aircraft"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_154_E2B

```json
{
  "video_id": "object_154",
  "edit_id": "object_154_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_154_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_isolated_dry_grass_clump_nearest_the_taxiway",
    "target_description": "the isolated dry grass clump nearest the taxiway",
    "source_state": "An isolated dry grass clump stands nearest the edge of the taxiway.",
    "desired_change": "The grass clump is replaced by a low gray boulder of similar size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the isolated dry grass clump nearest the taxiway with a low gray boulder of similar size.",
  "expected_result": {
    "description": "The grass clump is replaced by a low gray boulder of similar size.",
    "target_phrase": "low gray boulder beside taxiway"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_154_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_154_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the isolated dry grass clump nearest the taxiway on B independently of E1's change to the aircraft's unmarked white fuselage panels; both edit results must coexist in C."
  }
}
```

## object_157

### object_157_E1

```json
{
  "video_id": "object_157",
  "edit_id": "object_157_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_157.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Vegetation Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_bright_green_seedlings_outside_the_railing",
    "target_description": "the bright-green seedlings outside the railing",
    "source_state": "The seedlings have bright-green leaves across the soil bed.",
    "desired_change": "The leaves become muted purple-red."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the bright-green seedling leaves outside the railing to muted purple-red over the next two seconds.",
  "expected_result": {
    "description": "The leaves become muted purple-red.",
    "target_phrase": "seedlings with purple-red leaves"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_157_E2A

```json
{
  "video_id": "object_157",
  "edit_id": "object_157_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_157.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Event Reordering",
    "scope": "Multiple Processes"
  },
  "target": {
    "target_id": "the_second_monkey_approach_and_the_seated_monkey_leaf_contact",
    "target_description": "the second monkey's approach and the seated monkey's leaf contact",
    "source_state": "The second monkey approaches while the seated monkey is already touching the leaves.",
    "desired_change": "The approaching monkey reaches the seated monkey before the seated monkey touches the leaves."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "local event reordering"
  },
  "instruction": "Starting at 29.0 seconds, reorder the actions so the approaching monkey reaches the seated monkey before the seated monkey touches the green leaves.",
  "expected_result": {
    "description": "The approaching monkey reaches the seated monkey before the seated monkey touches the leaves.",
    "target_phrase": "monkey approach completed before leaf contact"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_157_E2B

```json
{
  "video_id": "object_157",
  "edit_id": "object_157_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_157_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_red_ball",
    "target_description": "one small plain red ball",
    "source_state": "No red ball is present on the soil beside the muted purple-red seedlings produced by E1.",
    "desired_change": "One small plain red ball appears on the soil beside the muted purple-red seedlings."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain red ball on the soil beside the muted purple-red seedlings.",
  "expected_result": {
    "description": "One small plain red ball appears on the soil beside the muted purple-red seedlings.",
    "target_phrase": "small red ball beside purple-red seedlings"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_157_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The seedling patch remains a stable placement reference around 29 seconds and carries E1's muted purple-red color in B."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_157_E1",
    "must_preserve_e1_result": true,
    "description": "This edit adds one small plain red ball beside the seedlings on B while preserving E1's muted purple-red seedling color; both edit results must coexist in C."
  }
}
```

## object_158

### object_158_E1

```json
{
  "video_id": "object_158",
  "edit_id": "object_158_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_158.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_jaguar_golden_tan_base_coat",
    "target_description": "the jaguar's golden-tan base coat",
    "source_state": "The jaguar has a golden-tan base coat with dark rosettes.",
    "desired_change": "The base coat becomes pale silver."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the rosetted jaguar's golden-tan base coat to pale silver over the next two seconds.",
  "expected_result": {
    "description": "The base coat becomes pale silver.",
    "target_phrase": "jaguar with pale-silver base coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_158_E2A

```json
{
  "video_id": "object_158",
  "edit_id": "object_158_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_158.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_adult_jaguar",
    "target_description": "the adult jaguar",
    "source_state": "The jaguar walks toward the vegetation at a steady natural speed.",
    "desired_change": "The jaguar walks at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the adult jaguar walk toward the vegetation at half its original speed for six seconds.",
  "expected_result": {
    "description": "The jaguar walks at half its original speed.",
    "target_phrase": "jaguar walking at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_158_E2B

```json
{
  "video_id": "object_158",
  "edit_id": "object_158_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_158_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_green_shrub",
    "target_description": "one small green shrub",
    "source_state": "No small shrub stands on the open sand immediately before the forest edge.",
    "desired_change": "One small green shrub appears on the open sand near the forest edge."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small green shrub on the open sand near the forest edge behind the jaguar.",
  "expected_result": {
    "description": "One small green shrub appears on the open sand near the forest edge.",
    "target_phrase": "small shrub near forest edge"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_158_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_158_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small green shrub on B independently of E1's change to the jaguar's golden-tan base coat; both edit results must coexist in C."
  }
}
```

## object_159

### object_159_E1

```json
{
  "video_id": "object_159",
  "edit_id": "object_159_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_159.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Water Transparency Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_slightly_cloudy_aquarium_water",
    "target_description": "the slightly cloudy aquarium water",
    "source_state": "The aquarium water is slightly cloudy with suspended particles.",
    "desired_change": "The water becomes fully clear."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the slightly cloudy aquarium water to fully clear water over the next two seconds.",
  "expected_result": {
    "description": "The water becomes fully clear.",
    "target_phrase": "aquarium with fully clear water"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_159_E2A

```json
{
  "video_id": "object_159",
  "edit_id": "object_159_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_159.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_central_green_aquatic_plant",
    "target_description": "the central green aquatic plant",
    "source_state": "The aquatic leaves show only slight irregular movement in the water.",
    "desired_change": "The aquatic leaves sway left and right three times."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the central green aquatic plant sway left and right three times.",
  "expected_result": {
    "description": "The aquatic leaves sway left and right three times.",
    "target_phrase": "aquatic plant swaying three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_159_E2B

```json
{
  "video_id": "object_159",
  "edit_id": "object_159_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_159_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_largest_flat_gray_stone_beside_the_aquatic_plant",
    "target_description": "the largest flat gray stone beside the aquatic plant",
    "source_state": "A large flat gray stone lies beside the central aquatic plant.",
    "desired_change": "The stone is replaced by a plain white shell of similar size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the largest flat gray stone beside the aquatic plant with a plain white shell of similar size.",
  "expected_result": {
    "description": "The stone is replaced by a plain white shell of similar size.",
    "target_phrase": "white shell beside aquatic plant"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_159_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_159_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the largest flat gray stone beside the aquatic plant on B independently of E1's change to the slightly cloudy aquarium water; both edit results must coexist in C."
  }
}
```

## object_160

### object_160_E1

```json
{
  "video_id": "object_160",
  "edit_id": "object_160_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_160.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Lighting Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_hard_direct_sunlight_on_the_toad_and_asphalt",
    "target_description": "the hard direct sunlight on the toad and asphalt",
    "source_state": "Hard direct sunlight creates a sharply defined shadow beside the toad.",
    "desired_change": "Soft diffuse daylight illuminates the toad and road surface."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the hard direct sunlight on the toad and asphalt to soft diffuse daylight over the next two seconds.",
  "expected_result": {
    "description": "Soft diffuse daylight illuminates the toad and road surface.",
    "target_phrase": "toad under soft diffuse daylight"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_160_E2A

```json
{
  "video_id": "object_160",
  "edit_id": "object_160_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_160.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_brown_toad",
    "target_description": "the brown toad",
    "source_state": "The toad makes short low crawling movements with long pauses.",
    "desired_change": "The toad lifts its front body with both forelegs twice."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the brown toad lift its front body with both forelegs twice over five seconds.",
  "expected_result": {
    "description": "The toad lifts its front body with both forelegs twice.",
    "target_phrase": "toad lifting front body twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_160_E2B

```json
{
  "video_id": "object_160",
  "edit_id": "object_160_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_160_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_brown_toad",
    "target_description": "the brown toad",
    "source_state": "The toad crawls forward through short movements at a slow variable speed.",
    "desired_change": "The toad crawls at twice its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the brown toad crawl forward at twice its original speed for six seconds.",
  "expected_result": {
    "description": "The toad crawls at twice its original speed.",
    "target_phrase": "toad crawling at double speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_160_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_160_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the brown toad on B independently of E1's change to the hard direct sunlight on the toad and asphalt; both edit results must coexist in C."
  }
}
```

## object_161

### object_161_E1

```json
{
  "video_id": "object_161",
  "edit_id": "object_161_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_161.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Deployment State Change",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_raised_top_sensor_on_the_robot_vacuum",
    "target_description": "the raised top sensor on the robot vacuum",
    "source_state": "The robot vacuum has a raised oval sensor structure on its top surface.",
    "desired_change": "The top sensor becomes flush with the surrounding housing."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      13,
      17
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.0 seconds, change the robot vacuum's raised top sensor to a flush position within the surrounding housing.",
  "expected_result": {
    "description": "The top sensor becomes flush with the surrounding housing.",
    "target_phrase": "robot vacuum with flush top sensor"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_161_E2A

```json
{
  "video_id": "object_161",
  "edit_id": "object_161_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_161.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_robot_vacuum",
    "target_description": "the robot vacuum",
    "source_state": "The robot vacuum moves through changing positions between the wood floor and dark floor area.",
    "desired_change": "The robot vacuum is positioned at the center of the dark floor area."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the robot vacuum at the center of the dark floor area.",
  "expected_result": {
    "description": "The robot vacuum is positioned at the center of the dark floor area.",
    "target_phrase": "robot vacuum centered on dark floor"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_161_E2B

```json
{
  "video_id": "object_161",
  "edit_id": "object_161_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_161_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_orange_traffic_cone",
    "target_description": "one small plain orange traffic cone",
    "source_state": "No orange traffic cone stands beside the white cabinet near the robot's route.",
    "desired_change": "One small plain orange traffic cone appears beside the cabinet."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain orange traffic cone beside the white cabinet near the robot vacuum.",
  "expected_result": {
    "description": "One small plain orange traffic cone appears beside the cabinet.",
    "target_phrase": "orange cone beside white cabinet"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_161_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_161_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain orange traffic cone on B independently of E1's change to the raised top sensor on the robot vacuum; both edit results must coexist in C."
  }
}
```

## object_162

### object_162_E1

```json
{
  "video_id": "object_162",
  "edit_id": "object_162_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_162.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_fox_red_brown_dorsal_fur",
    "target_description": "the fox's red-brown dorsal fur",
    "source_state": "The fox has red-brown dorsal fur with darker legs and a bushy tail.",
    "desired_change": "The dorsal fur becomes pale silver-gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the fox's red-brown dorsal fur to pale silver-gray over the next two seconds.",
  "expected_result": {
    "description": "The dorsal fur becomes pale silver-gray.",
    "target_phrase": "fox with pale-silver-gray dorsal fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_162_E2A

```json
{
  "video_id": "object_162",
  "edit_id": "object_162_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_162.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_fox_and_the_standing_adult",
    "target_description": "the fox and the standing adult",
    "source_state": "The fox circles the adult at changing distances beside the parked vehicle.",
    "desired_change": "The fox is positioned one meter directly in front of the adult."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the fox one meter directly in front of the standing adult beside the parked vehicle.",
  "expected_result": {
    "description": "The fox is positioned one meter directly in front of the adult.",
    "target_phrase": "fox one meter in front of adult"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_162_E2B

```json
{
  "video_id": "object_162",
  "edit_id": "object_162_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_162_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_pale_silver_gray_fox",
    "target_description": "the pale-silver-gray fox",
    "source_state": "The pale-silver-gray fox produced by E1 walks, pauses, and turns on all four feet around the adult.",
    "desired_change": "The pale-silver-gray fox sits and raises one forepaw twice."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the pale-silver-gray fox sit and raise one forepaw twice over five seconds.",
  "expected_result": {
    "description": "The pale-silver-gray fox sits and raises one forepaw twice.",
    "target_phrase": "pale-silver-gray fox raising one forepaw"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_162_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_162_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the pale-silver-gray fox on B while preserving E1's pale-silver-gray fur; both edit results must coexist in C."
  }
}
```

## object_165

### object_165_E1

```json
{
  "video_id": "object_165",
  "edit_id": "object_165_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_165.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Lighting Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_blue_green_underwater_illumination",
    "target_description": "the blue-green underwater illumination",
    "source_state": "The cephalopod and seabed are lit by cool blue-green underwater light.",
    "desired_change": "Warm neutral underwater light illuminates the scene."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the cool blue-green underwater light to warm neutral illumination over the next two seconds.",
  "expected_result": {
    "description": "Warm neutral underwater light illuminates the scene.",
    "target_phrase": "cephalopod under warm neutral light"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_165_E2A

```json
{
  "video_id": "object_165",
  "edit_id": "object_165_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_165.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cephalopod",
    "target_description": "the cephalopod",
    "source_state": "The cephalopod glides through changing positions above sand, stones, and coral.",
    "desired_change": "The cephalopod is positioned above the center of the pale rippled sand patch."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the cephalopod above the center of the pale rippled sand patch.",
  "expected_result": {
    "description": "The cephalopod is positioned above the center of the pale rippled sand patch.",
    "target_phrase": "cephalopod centered above rippled sand"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_165_E2B

```json
{
  "video_id": "object_165",
  "edit_id": "object_165_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_165_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Path Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cephalopod",
    "target_description": "the cephalopod",
    "source_state": "The cephalopod follows broad irregular curves beside the seabed rocks.",
    "desired_change": "The cephalopod follows a tighter clockwise arc."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the cephalopod follow a tighter clockwise arc above the seabed for six seconds.",
  "expected_result": {
    "description": "The cephalopod follows a tighter clockwise arc.",
    "target_phrase": "cephalopod following tighter clockwise arc"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_165_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_165_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the cephalopod on B independently of E1's change to the blue-green underwater illumination; both edit results must coexist in C."
  }
}
```

## object_168

### object_168_E1

```json
{
  "video_id": "object_168",
  "edit_id": "object_168_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_168.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_opossum_like_animal_gray_white_dorsal_fur",
    "target_description": "the opossum-like animal's gray-white dorsal fur",
    "source_state": "The animal has coarse gray-white dorsal fur and a paler face.",
    "desired_change": "The dorsal fur becomes warm reddish brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the opossum-like animal's gray-white dorsal fur to warm reddish brown over the next two seconds.",
  "expected_result": {
    "description": "The dorsal fur becomes warm reddish brown.",
    "target_phrase": "opossum-like animal with reddish-brown fur"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_168_E2A

```json
{
  "video_id": "object_168",
  "edit_id": "object_168_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_168.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_opossum_like_animal",
    "target_description": "the opossum-like animal",
    "source_state": "The animal gradually changes from a low side heading to a near-frontal pose.",
    "desired_change": "The animal faces directly toward the camera."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the opossum-like animal to face directly toward the camera.",
  "expected_result": {
    "description": "The animal faces directly toward the camera.",
    "target_phrase": "opossum-like animal facing camera"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_168_E2B

```json
{
  "video_id": "object_168",
  "edit_id": "object_168_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_168_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_opossum_like_animal_forepaws",
    "target_description": "the opossum-like animal's forepaws",
    "source_state": "The animal stands low and makes limited forepaw movement while facing the camera.",
    "desired_change": "The animal raises both forepaws together twice."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the opossum-like animal raise both forepaws together twice over five seconds.",
  "expected_result": {
    "description": "The animal raises both forepaws together twice.",
    "target_phrase": "opossum-like animal raising forepaws"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_168_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_168_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the opossum-like animal's forepaws on B independently of E1's change to the opossum-like animal's gray-white dorsal fur; both edit results must coexist in C."
  }
}
```

## object_169

### object_169_E1

```json
{
  "video_id": "object_169",
  "edit_id": "object_169_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_169.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_black_jumping_spider_and_the_gray_brown_jumping_spider",
    "target_description": "the black jumping spider and the gray-brown jumping spider",
    "source_state": "The two spiders make brief irregular foreleg contact after approaching each other.",
    "desired_change": "The two jumping spiders touch their raised front legs three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the black and gray-brown jumping spiders touch their raised front legs three times.",
  "expected_result": {
    "description": "The two jumping spiders touch their raised front legs three times.",
    "target_phrase": "jumping spiders touching raised front legs"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_169_E2A

```json
{
  "video_id": "object_169",
  "edit_id": "object_169_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_169.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Stabilized Macro Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld macro camera changes distance and focus while following the two spiders.",
    "desired_change": "The camera tracks the two spiders smoothly from a constant overhead distance."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the two jumping spiders smoothly from a constant overhead distance for five seconds.",
  "expected_result": {
    "description": "The camera tracks the two spiders smoothly from a constant overhead distance.",
    "target_phrase": "smooth overhead tracking of jumping spiders"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_169_E2B

```json
{
  "video_id": "object_169",
  "edit_id": "object_169_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_169_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Ink-wash Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_jumping_spider_scene",
    "target_description": "the full jumping-spider scene",
    "source_state": "The macro footage has a realistic digital-video appearance.",
    "desired_change": "The full scene is rendered as a detailed ink-wash illustration."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full jumping-spider scene into a detailed ink-wash illustration over the next two seconds.",
  "expected_result": {
    "description": "The full scene is rendered as a detailed ink-wash illustration.",
    "target_phrase": "ink-wash jumping-spider scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_169_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_169_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full jumping-spider scene on B independently of E1's change to the black jumping spider and the gray-brown jumping spider; both edit results must coexist in C."
  }
}
```

## object_170

### object_170_E1

```json
{
  "video_id": "object_170",
  "edit_id": "object_170_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_170.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Vegetation Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_surrounding_green_grass_blades",
    "target_description": "the surrounding green grass blades",
    "source_state": "The grass around the seed heads is medium green.",
    "desired_change": "The surrounding grass becomes pale blue-green."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the surrounding green grass blades to pale blue-green over the next two seconds.",
  "expected_result": {
    "description": "The surrounding grass becomes pale blue-green.",
    "target_phrase": "pale-blue-green grass around seed heads"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_170_E2A

```json
{
  "video_id": "object_170",
  "edit_id": "object_170_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_170.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_four_flower_and_seed_head_stems",
    "target_description": "the four flower and seed-head stems",
    "source_state": "The stems sway gently with irregular timing and amplitude in the breeze.",
    "desired_change": "The four stems sway together in three synchronized waves."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the four flower and seed-head stems sway together in three synchronized waves.",
  "expected_result": {
    "description": "The four stems sway together in three synchronized waves.",
    "target_phrase": "four stems swaying in synchronized waves"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_170_E2B

```json
{
  "video_id": "object_170",
  "edit_id": "object_170_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_170_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_smaller_white_seed_head",
    "target_description": "one smaller white seed head",
    "source_state": "Three white seed heads and one brown closed flower head are present.",
    "desired_change": "One smaller white seed head appears behind the central brown flower head."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one smaller white seed head behind the central brown flower head.",
  "expected_result": {
    "description": "One smaller white seed head appears behind the central brown flower head.",
    "target_phrase": "additional small white seed head"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_170_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_170_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one smaller white seed head on B independently of E1's change to the surrounding green grass blades; both edit results must coexist in C."
  }
}
```

## object_171

### object_171_E1

```json
{
  "video_id": "object_171",
  "edit_id": "object_171_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_171.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Skin Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tree_frog_bright_green_dorsal_skin",
    "target_description": "the tree frog's bright-green dorsal skin",
    "source_state": "The tree frog has bright-green dorsal skin with red eyes and orange toes.",
    "desired_change": "The dorsal skin becomes deep turquoise."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the tree frog's bright-green dorsal skin to deep turquoise over the next two seconds.",
  "expected_result": {
    "description": "The dorsal skin becomes deep turquoise.",
    "target_phrase": "tree frog with turquoise dorsal skin"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_171_E2A

```json
{
  "video_id": "object_171",
  "edit_id": "object_171_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_171.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The close macro framing crops parts of the frog, supporting leaf, and nearby trunk.",
    "desired_change": "The framing widens to include the full frog, supporting leaf, and adjacent tree trunk."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to include the full tree frog, supporting leaf, and adjacent trunk.",
  "expected_result": {
    "description": "The framing widens to include the full frog, supporting leaf, and adjacent tree trunk.",
    "target_phrase": "wide frog leaf and trunk view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_171_E2B

```json
{
  "video_id": "object_171",
  "edit_id": "object_171_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_171_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tree_frog",
    "target_description": "the tree frog",
    "source_state": "The tree frog begins climbing toward the leaf edge and trunk at a slow variable rate.",
    "desired_change": "The tree frog climbs at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the tree frog climb toward the adjacent trunk at half its original speed for six seconds.",
  "expected_result": {
    "description": "The tree frog climbs at half its original speed.",
    "target_phrase": "tree frog climbing at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_171_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_171_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tree frog on B independently of E1's change to the tree frog's bright-green dorsal skin; both edit results must coexist in C."
  }
}
```

## object_173

### object_173_E1

```json
{
  "video_id": "object_173",
  "edit_id": "object_173_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_173.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Skin Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_juvenile_rhinoceros_gray_skin",
    "target_description": "the juvenile rhinoceros's gray skin",
    "source_state": "The juvenile rhinoceros has medium-gray folded skin.",
    "desired_change": "The skin becomes cool blue-gray."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the juvenile rhinoceros's gray skin to cool blue-gray over the next two seconds.",
  "expected_result": {
    "description": "The skin becomes cool blue-gray.",
    "target_phrase": "juvenile rhinoceros with blue-gray skin"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_173_E2A

```json
{
  "video_id": "object_173",
  "edit_id": "object_173_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_173.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Progress Acceleration",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_rhinoceros_approach_touch_depart_interaction_cycle",
    "target_description": "the rhinoceros's approach-touch-depart interaction cycle",
    "source_state": "Each approach, brief touch, and departure cycle unfolds at its original rate.",
    "desired_change": "The same interaction cycle unfolds at twice its original rate."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "local process retiming"
  },
  "instruction": "Starting at 29.0 seconds, accelerate the juvenile rhinoceros's approach-touch-depart interaction cycle to twice its original rate for six seconds.",
  "expected_result": {
    "description": "The same interaction cycle unfolds at twice its original rate.",
    "target_phrase": "rhinoceros interaction cycle at double speed"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_173_E2B

```json
{
  "video_id": "object_173",
  "edit_id": "object_173_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_173_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_blue_rubber_ball",
    "target_description": "one small plain blue rubber ball",
    "source_state": "No blue ball is present on the concrete floor inside the red railing.",
    "desired_change": "One small plain blue rubber ball appears inside the enclosure."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain blue rubber ball on the concrete floor inside the red railing.",
  "expected_result": {
    "description": "One small plain blue rubber ball appears inside the enclosure.",
    "target_phrase": "blue ball inside rhinoceros enclosure"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_173_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_173_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain blue rubber ball on B independently of E1's change to the juvenile rhinoceros's gray skin; both edit results must coexist in C."
  }
}
```

## object_174

### object_174_E1

```json
{
  "video_id": "object_174",
  "edit_id": "object_174_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_174.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_stag_yellow_brown_coat",
    "target_description": "the stag's yellow-brown coat",
    "source_state": "The stag has a yellow-brown coat with a pale underside.",
    "desired_change": "The coat becomes deep chestnut brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the stag's yellow-brown coat to deep chestnut brown over the next two seconds.",
  "expected_result": {
    "description": "The coat becomes deep chestnut brown.",
    "target_phrase": "stag with chestnut-brown coat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_174_E2A

```json
{
  "video_id": "object_174",
  "edit_id": "object_174_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_174.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed and Path Change",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_small_gray_brown_dog",
    "target_description": "the small gray-brown dog",
    "source_state": "The dog runs through quick irregular arcs around the stag.",
    "desired_change": "The dog follows a wider arc at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the small gray-brown dog follow a wider arc around the stag at half its original speed for six seconds.",
  "expected_result": {
    "description": "The dog follows a wider arc at half its original speed.",
    "target_phrase": "dog circling stag in wider slower arc"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_174_E2B

```json
{
  "video_id": "object_174",
  "edit_id": "object_174_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_174_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_circular_ground_facility_cover",
    "target_description": "the circular ground facility cover",
    "source_state": "A circular green-gray facility cover lies in the grass near the two animals.",
    "desired_change": "The facility cover is replaced by a flat gray stone of similar size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the circular ground facility cover with a flat gray stone of similar size.",
  "expected_result": {
    "description": "The facility cover is replaced by a flat gray stone of similar size.",
    "target_phrase": "flat gray stone in grass"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_174_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_174_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the circular ground facility cover on B independently of E1's change to the stag's yellow-brown coat; both edit results must coexist in C."
  }
}
```

## object_175

### object_175_E1

```json
{
  "video_id": "object_175",
  "edit_id": "object_175_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_175.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_dark_horse_and_the_zebra",
    "target_description": "the dark horse and the zebra",
    "source_state": "The horse and zebra make irregular head, neck, and foreleg contact.",
    "desired_change": "The horse and zebra raise their forequarters and press their forelegs together twice."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 20,
    "evaluation_window_sec": [
      13,
      22
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the dark horse and zebra raise their forequarters and press their forelegs together twice.",
  "expected_result": {
    "description": "The horse and zebra raise their forequarters and press their forelegs together twice.",
    "target_phrase": "horse and zebra pressing raised forelegs"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      22
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_175_E2A

```json
{
  "video_id": "object_175",
  "edit_id": "object_175_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_175.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Side Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The handheld camera follows the two animals with uneven lateral movement and zoom changes.",
    "desired_change": "The camera tracks the horse and zebra smoothly from a constant side angle."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the dark horse and zebra smoothly from a constant side angle for five seconds.",
  "expected_result": {
    "description": "The camera tracks the horse and zebra smoothly from a constant side angle.",
    "target_phrase": "smooth side tracking of horse and zebra"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_175_E2B

```json
{
  "video_id": "object_175",
  "edit_id": "object_175_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_175_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1970s Nature-film Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_hillside_horse_and_zebra_scene",
    "target_description": "the full hillside horse-and-zebra scene",
    "source_state": "The pasture footage has a modern digital-video appearance.",
    "desired_change": "The full frame resembles a 1970s color nature documentary."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full horse-and-zebra pasture scene into a 1970s color nature documentary over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1970s color nature documentary.",
    "target_phrase": "1970s horse-and-zebra documentary"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_175_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_175_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full hillside horse-and-zebra scene on B independently of E1's change to the dark horse and the zebra; both edit results must coexist in C."
  }
}
```

## object_181

### object_181_E1

```json
{
  "video_id": "object_181",
  "edit_id": "object_181_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_181.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Airframe Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_micro_drone_unmarked_dark_frame_arms",
    "target_description": "the micro drone's unmarked dark frame arms",
    "source_state": "The micro drone has dark frame arms around its protected indicator lights.",
    "desired_change": "The unmarked frame arms become bright silver."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the micro drone's unmarked dark frame arms to bright silver over the next two seconds.",
  "expected_result": {
    "description": "The unmarked frame arms become bright silver.",
    "target_phrase": "micro drone with silver frame arms"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_181_E2A

```json
{
  "video_id": "object_181",
  "edit_id": "object_181_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_181.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_micro_quadrotor",
    "target_description": "the micro quadrotor",
    "source_state": "The quadrotor moves through changing positions near the door, walls, and upper opening.",
    "desired_change": "The quadrotor is positioned directly below the spherical chandelier."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the micro quadrotor directly below the spherical chandelier in the entrance hall.",
  "expected_result": {
    "description": "The quadrotor is positioned directly below the spherical chandelier.",
    "target_phrase": "quadrotor directly below chandelier"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_181_E2B

```json
{
  "video_id": "object_181",
  "edit_id": "object_181_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_181_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_blue_landing_pad",
    "target_description": "one small plain blue landing pad",
    "source_state": "No blue landing pad is present on the entrance-hall floor beneath the drone.",
    "desired_change": "One small plain blue landing pad appears on the floor."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain blue landing pad on the entrance-hall floor beneath the drone.",
  "expected_result": {
    "description": "One small plain blue landing pad appears on the floor.",
    "target_phrase": "blue landing pad beneath drone"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_181_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_181_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain blue landing pad on B independently of E1's change to the micro drone's unmarked dark frame arms; both edit results must coexist in C."
  }
}
```

## object_185

### object_185_E1

```json
{
  "video_id": "object_185",
  "edit_id": "object_185_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_185.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_brown_bear_and_the_fish",
    "target_description": "the brown bear and the fish",
    "source_state": "The bear makes irregular paw and mouth contact while holding the fish on the rock.",
    "desired_change": "The bear presses the fish with one forepaw and pulls it upward with its mouth three times."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the brown bear press the fish with one forepaw and pull it upward with its mouth three times.",
  "expected_result": {
    "description": "The bear presses the fish with one forepaw and pulls it upward with its mouth three times.",
    "target_phrase": "bear pressing and pulling fish"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_185_E2A

```json
{
  "video_id": "object_185",
  "edit_id": "object_185_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_185.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_brown_bear_and_the_fish",
    "target_description": "the brown bear and the fish",
    "source_state": "The fish lies at changing angles near and between the bear's forepaws.",
    "desired_change": "The fish is positioned centrally between the bear's two forepaws."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reposition the fish centrally between the brown bear's two forepaws on the mossy rock.",
  "expected_result": {
    "description": "The fish is positioned centrally between the bear's two forepaws.",
    "target_phrase": "fish centered between bear forepaws"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_185_E2B

```json
{
  "video_id": "object_185",
  "edit_id": "object_185_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_185_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1970s Nature-film Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_bear_and_river_scene",
    "target_description": "the full bear-and-river scene",
    "source_state": "The wildlife footage has a modern digital-video appearance.",
    "desired_change": "The full frame resembles a 1970s color nature documentary."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, transform the full bear-and-river scene into a 1970s color nature documentary over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1970s color nature documentary.",
    "target_phrase": "1970s bear-and-river documentary"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_185_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_185_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full bear-and-river scene on B independently of E1's change to the brown bear and the fish; both edit results must coexist in C."
  }
}
```

## object_187

### object_187_E1

```json
{
  "video_id": "object_187",
  "edit_id": "object_187_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_187.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Pattern Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_monitor_lizard_pale_body_markings",
    "target_description": "the monitor lizard's pale body markings",
    "source_state": "The monitor lizard has pale gray spots and bands over dark wet scales.",
    "desired_change": "The pale markings become muted gold."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the monitor lizard's pale body spots and bands to muted gold over the next two seconds.",
  "expected_result": {
    "description": "The pale markings become muted gold.",
    "target_phrase": "monitor lizard with muted-gold markings"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_187_E2A

```json
{
  "video_id": "object_187",
  "edit_id": "object_187_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_187.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_monitor_lizard",
    "target_description": "the monitor lizard",
    "source_state": "The lizard changes heading while swimming and attempting to climb different wall sections.",
    "desired_change": "The lizard faces directly toward the far bathtub rim."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, reorient the monitor lizard to face directly toward the far bathtub rim.",
  "expected_result": {
    "description": "The lizard faces directly toward the far bathtub rim.",
    "target_phrase": "monitor lizard facing far rim"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_187_E2B

```json
{
  "video_id": "object_187",
  "edit_id": "object_187_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_187_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_metal_bathtub_faucet",
    "target_description": "the metal bathtub faucet",
    "source_state": "A metal faucet is fixed above the bathtub beside the climbing route.",
    "desired_change": "The metal faucet is replaced by a matte-black faucet of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the metal bathtub faucet with a matte-black faucet of the same size.",
  "expected_result": {
    "description": "The metal faucet is replaced by a matte-black faucet of the same size.",
    "target_phrase": "matte-black bathtub faucet"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_187_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_187_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the metal bathtub faucet on B independently of E1's change to the monitor lizard's pale body markings; both edit results must coexist in C."
  }
}
```

## object_188

### object_188_E1

```json
{
  "video_id": "object_188",
  "edit_id": "object_188_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_188.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Damage State Change",
    "scope": "Core Object Surface"
  },
  "target": {
    "target_id": "the_lower_left_red_race_cars_dented_front_panel",
    "target_description": "the dented front panel of the red race car in the lower-left area with yellow-and-green graphics",
    "source_state": "The red race car in the lower-left area has a visibly dented front panel and yellow-and-green graphics on its body.",
    "desired_change": "The car's dented front panel becomes smooth and undented while its existing body graphics remain unchanged."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the dented front panel of the red race car in the lower-left area with yellow-and-green graphics to a smooth undented state over the next two seconds.",
  "expected_result": {
    "description": "The red race car in the lower-left area has a smooth, undented front panel while retaining its yellow-and-green body graphics.",
    "target_phrase": "lower-left red race car with repaired front panel"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.0,
      18.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "At 14 seconds, the red race car with yellow-and-green body graphics is clearly identifiable in the lower-left area, and its damaged front panel is visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_188_E2A

```json
{
  "video_id": "object_188",
  "edit_id": "object_188_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_188.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Overhead Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The high wide camera observes multiple moving cars from a mostly fixed position after the hard cut.",
    "desired_change": "The camera tracks the leading visible moving car smoothly from directly above."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the leading visible moving race car smoothly from directly above for five seconds.",
  "expected_result": {
    "description": "The camera tracks the leading visible moving car smoothly from directly above.",
    "target_phrase": "overhead tracking of leading moving race car"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_188_E2B

```json
{
  "video_id": "object_188",
  "edit_id": "object_188_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_188_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Environmental Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_dust_plume_behind_the_moving_race_cars",
    "target_description": "the dust plume behind the moving race cars",
    "source_state": "Dust rises and spreads irregularly behind cars across the dirt corner.",
    "desired_change": "The dust plume drifts strongly toward the inside of the track."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded environmental motion"
  },
  "instruction": "Starting at 29.0 seconds, make the dust plume behind the moving race cars drift strongly toward the inside of the track for five seconds.",
  "expected_result": {
    "description": "The dust plume drifts strongly toward the inside of the track.",
    "target_phrase": "race-car dust drifting inward"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_188_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_188_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dust plume behind the moving race cars on B independently of E1's repaired front panel on the lower-left red race car with yellow-and-green graphics; both edit results must coexist in C."
  }
}
```

## object_190

### object_190_E1

```json
{
  "video_id": "object_190",
  "edit_id": "object_190_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_190.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Exterior Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_robot_unmarked_yellow_body_panels",
    "target_description": "the robot's unmarked yellow body panels",
    "source_state": "The robot has yellow body panels surrounding protected lights and markings.",
    "desired_change": "The unmarked yellow panels become bright red."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the robot's unmarked yellow body panels to bright red over the next two seconds.",
  "expected_result": {
    "description": "The unmarked yellow panels become bright red.",
    "target_phrase": "robot with bright-red body panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_190_E2A

```json
{
  "video_id": "object_190",
  "edit_id": "object_190_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_190.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Core Process"
  },
  "target": {
    "target_id": "the_tracked_robot_dance_sequence",
    "target_description": "the tracked robot's dance sequence",
    "source_state": "The robot continues its combined turning and arm-motion sequence without a deliberate pause.",
    "desired_change": "The dance sequence pauses for three seconds and then resumes."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "local pause and resume"
  },
  "instruction": "At 29.0 seconds, pause the tracked robot's combined turning and arm-motion sequence for three seconds, then resume it.",
  "expected_result": {
    "description": "The dance sequence pauses for three seconds and then resumes.",
    "target_phrase": "robot dance paused three seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_190_E2B

```json
{
  "video_id": "object_190",
  "edit_id": "object_190_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_190_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "one_small_plain_blue_cube",
    "target_description": "one small plain blue cube",
    "source_state": "No blue cube is present on the open wooden floor beside the robot.",
    "desired_change": "One small plain blue cube appears beside the robot."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, add one small plain blue cube on the wooden floor beside the tracked robot.",
  "expected_result": {
    "description": "One small plain blue cube appears beside the robot.",
    "target_phrase": "small blue cube beside robot"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_190_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_190_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small plain blue cube on B independently of E1's change to the robot's unmarked yellow body panels; both edit results must coexist in C."
  }
}
```

## object_194

### object_194_E1

```json
{
  "video_id": "object_194",
  "edit_id": "object_194_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_194.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Ground Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_pale_gravel_forest_road",
    "target_description": "the pale gravel forest road",
    "source_state": "The forest road has a pale tan-gray gravel surface.",
    "desired_change": "The gravel surface becomes deep reddish brown."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the pale tan-gray gravel forest road to deep reddish brown over the next two seconds.",
  "expected_result": {
    "description": "The gravel surface becomes deep reddish brown.",
    "target_phrase": "deep reddish-brown forest road"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_194_E2A

```json
{
  "video_id": "object_194",
  "edit_id": "object_194_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_194.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Event Reordering",
    "scope": "Multiple Processes"
  },
  "target": {
    "target_id": "the_three_boars_road_crossings",
    "target_description": "the three boars' road crossings",
    "source_state": "The adult crosses first and the two smaller boars follow with partly variable spacing.",
    "desired_change": "The adult completes its crossing before the first smaller boar crosses, followed by the second smaller boar."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 36.0,
    "evaluation_window_sec": [
      28.0,
      38.0
    ],
    "temporal_behavior": "local event reordering"
  },
  "instruction": "Starting at 29.0 seconds, reorder the crossings so the adult boar finishes first, followed by the first smaller boar and then the second.",
  "expected_result": {
    "description": "The adult completes its crossing before the first smaller boar crosses, followed by the second smaller boar.",
    "target_phrase": "adult followed by two sequential smaller boars"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      38.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_194_E2B

```json
{
  "video_id": "object_194",
  "edit_id": "object_194_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_194_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Related Objects"
  },
  "target": {
    "target_id": "the_two_smaller_boars",
    "target_description": "the two smaller boars",
    "source_state": "The two smaller boars walk and make short quick steps while following the adult.",
    "desired_change": "Each smaller boar hops once over the road edge."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make each of the two smaller boars hop once over the forest-road edge.",
  "expected_result": {
    "description": "Each smaller boar hops once over the road edge.",
    "target_phrase": "two smaller boars hopping over road edge"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_194_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_194_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the two smaller boars on B independently of E1's change to the pale gravel forest road; both edit results must coexist in C."
  }
}
```

## object_195

### object_195_E1

```json
{
  "video_id": "object_195",
  "edit_id": "object_195_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_195.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Weather Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_weather_above_the_railway",
    "target_description": "the weather above the railway",
    "source_state": "The passenger train travels under overcast conditions without visible precipitation.",
    "desired_change": "A light rain shower begins above the railway."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the weather above the railway to a light rain shower over the next two seconds.",
  "expected_result": {
    "description": "A light rain shower begins above the railway.",
    "target_phrase": "passenger train traveling through light rain"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_195_E2A

```json
{
  "video_id": "object_195",
  "edit_id": "object_195_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_195.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Parallel Side Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_trajectory",
    "target_description": "the camera trajectory",
    "source_state": "The moving camera follows the train with uneven vehicle vibration and changing lateral offset.",
    "desired_change": "The camera tracks the locomotive smoothly from a constant parallel side distance."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, track the passenger locomotive smoothly from a constant parallel side distance for five seconds.",
  "expected_result": {
    "description": "The camera tracks the locomotive smoothly from a constant parallel side distance.",
    "target_phrase": "smooth parallel tracking of locomotive"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_195_E2B

```json
{
  "video_id": "object_195",
  "edit_id": "object_195_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_195_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Core Object Component"
  },
  "target": {
    "target_id": "the_blue_striped_emblem_on_the_locomotives_side_panel",
    "target_description": "the blue striped emblem on the locomotive's side panel",
    "source_state": "A blue striped emblem is applied to the side panel of the passing locomotive.",
    "desired_change": "The blue striped emblem is removed, leaving the underlying side panel plain."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, remove the blue striped emblem from the side panel of the passing locomotive.",
  "expected_result": {
    "description": "The locomotive's side panel remains visible without the blue striped emblem.",
    "target_phrase": "locomotive side panel without blue striped emblem"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_195_E1",
      "adjacent locomotive lettering, numbers, and non-target paintwork"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, overlay logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "At 29 seconds, the blue striped emblem is large, unobstructed, and clearly localized on the locomotive side panel below the adjacent lettering."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_195_E1",
    "must_preserve_e1_result": true,
    "description": "This edit removes the blue striped locomotive emblem on B independently of E1's light rain above the railway; both edit results must coexist in C."
  }
}
```

## object_198

### object_198_E1

```json
{
  "video_id": "object_198",
  "edit_id": "object_198_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_198.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_juvenile_hippo_and_the_two_larger_hippos",
    "target_description": "the juvenile hippo and the two larger hippos",
    "source_state": "The juvenile makes irregular side and muzzle contact while joining the larger hippos.",
    "desired_change": "The juvenile hippo gently touches each larger hippo's muzzle twice."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      13,
      21
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the juvenile hippo gently touch each larger hippo's muzzle twice.",
  "expected_result": {
    "description": "The juvenile hippo gently touches each larger hippo's muzzle twice.",
    "target_phrase": "juvenile hippo touching larger hippos"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_198_E2A

```json
{
  "video_id": "object_198",
  "edit_id": "object_198_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_198.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_juvenile_hippo",
    "target_description": "the juvenile hippo",
    "source_state": "The juvenile swims and floats with irregular small vertical changes.",
    "desired_change": "The juvenile hippo surfaces twice beside the larger hippos."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the juvenile hippo surface twice beside the two larger hippos.",
  "expected_result": {
    "description": "The juvenile hippo surfaces twice beside the larger hippos.",
    "target_phrase": "juvenile hippo surfacing twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_198_E2B

```json
{
  "video_id": "object_198",
  "edit_id": "object_198_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_198_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Cool Film Color Grade",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_three_hippo_pool_scene",
    "target_description": "the full three-hippo pool scene",
    "source_state": "The pool footage has ordinary modern digital color and texture.",
    "desired_change": "The full frame receives a cool natural-film color grade and fine grain."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.0 seconds, apply a cool natural-film color grade and fine grain to the full three-hippo pool scene over the next two seconds.",
  "expected_result": {
    "description": "The full frame receives a cool natural-film color grade and fine grain.",
    "target_phrase": "cool film-grade hippo pool scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of object_198_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_198_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full three-hippo pool scene on B independently of E1's change to the juvenile hippo and the two larger hippos; both edit results must coexist in C."
  }
}
```

## object_199

### object_199_E1

```json
{
  "video_id": "object_199",
  "edit_id": "object_199_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_199.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Skin Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_gecko_pale_cream_base_skin",
    "target_description": "the gecko's pale cream base skin",
    "source_state": "The gecko has pale cream skin with dark brown spots and bands.",
    "desired_change": "The pale base skin becomes muted turquoise."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the gecko's pale cream base skin to muted turquoise over the next two seconds.",
  "expected_result": {
    "description": "The pale base skin becomes muted turquoise.",
    "target_phrase": "gecko with muted-turquoise base skin"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_199_E2A

```json
{
  "video_id": "object_199",
  "edit_id": "object_199_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_199.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "New Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_leopard_gecko_thick_tail",
    "target_description": "the leopard gecko's thick tail",
    "source_state": "The gecko's thick tail makes small irregular movements during its approach.",
    "desired_change": "The gecko waves its thick tail from side to side three times."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the leopard gecko wave its thick tail from side to side three times.",
  "expected_result": {
    "description": "The gecko waves its thick tail from side to side three times.",
    "target_phrase": "gecko waving thick tail three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_199_E2B

```json
{
  "video_id": "object_199",
  "edit_id": "object_199_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_199_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_plain_pink_circular_dish",
    "target_description": "the plain pink circular dish",
    "source_state": "A plain pink circular dish lies on the substrate beside the gecko.",
    "desired_change": "The pink dish is replaced by a plain blue dish of the same size."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.0 seconds, replace the plain pink circular dish beside the gecko with a plain blue dish of the same size.",
  "expected_result": {
    "description": "The pink dish is replaced by a plain blue dish of the same size.",
    "target_phrase": "plain blue dish beside gecko"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of object_199_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_199_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the plain pink circular dish on B independently of E1's change to the gecko's pale cream base skin; both edit results must coexist in C."
  }
}
```

## object_200

### object_200_E1

```json
{
  "video_id": "object_200",
  "edit_id": "object_200_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/object_200.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Lighting Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_hard_sunlight_on_the_alligator_like_animal_and_fairway",
    "target_description": "the hard sunlight on the alligator-like animal and fairway",
    "source_state": "Hard direct sunlight creates strong highlights and defined shadows across the fairway.",
    "desired_change": "Soft diffuse overcast light illuminates the scene."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.0 seconds, change the hard direct sunlight on the alligator-like animal and fairway to soft diffuse overcast illumination over the next two seconds.",
  "expected_result": {
    "description": "Soft diffuse overcast light illuminates the scene.",
    "target_phrase": "alligator-like animal under diffuse light"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 14.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### object_200_E2A

```json
{
  "video_id": "object_200",
  "edit_id": "object_200_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/object_200.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing",
    "target_description": "the camera framing",
    "source_state": "The tracking view alternately crops the animal, the distant adult, and sections of the sand bunker.",
    "desired_change": "The framing widens to include the full animal, the distant adult, and the sand bunker together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 29.0 seconds, zoom out smoothly over four seconds to show the full alligator-like animal, distant adult, and sand bunker together.",
  "expected_result": {
    "description": "The framing widens to include the full animal, the distant adult, and the sand bunker together.",
    "target_phrase": "wide animal adult and bunker view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### object_200_E2B

```json
{
  "video_id": "object_200",
  "edit_id": "object_200_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/object_200_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_alligator_like_animal",
    "target_description": "the alligator-like animal",
    "source_state": "The animal walks steadily across the fairway at a slow natural speed.",
    "desired_change": "The animal walks at half its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      28.0,
      37.0
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 29.0 seconds, make the alligator-like animal walk across the fairway at half its original speed for six seconds.",
  "expected_result": {
    "description": "The animal walks at half its original speed.",
    "target_phrase": "alligator-like animal walking at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of object_200_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target and its source state remain identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "object_200_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the alligator-like animal on B independently of E1's change to the hard sunlight on the alligator-like animal and fairway; both edit results must coexist in C."
  }
}
```
