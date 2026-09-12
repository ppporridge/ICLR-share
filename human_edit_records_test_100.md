# Human Real-Video Edit Records - Balanced 100-Video Test Subset

This test document is derived from `human_edit_records.md`. Every selected source video retains its complete E1, E2A, and E2B branch-edit records verbatim.

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
| Attribute | 120 | 60 | 60 | 60 |
| Camera | 60 | 30 | 30 | 30 |
| Composition | 90 | 45 | 45 | 45 |
| Motion | 180 | 90 | 90 | 90 |
| Spatial | 90 | 45 | 45 | 45 |
| Style | 45 | 22.5 | 22 | 23 |
| Temporal | 15 | 7.5 | 8 | 7 |

## Test-Subset Secondary-Type Counts

| Primary / Secondary type | Full count | Exact half | Test count | Complement count |
|---|---:|---:|---:|---:|
| Attribute / Accessories | 13 | 6.5 | 7 | 6 |
| Attribute / Body/Skin Appearance | 7 | 3.5 | 3 | 4 |
| Attribute / Clothing | 25 | 12.5 | 13 | 12 |
| Attribute / Environment Object | 25 | 12.5 | 13 | 12 |
| Attribute / Facial Appearance | 15 | 7.5 | 7 | 8 |
| Attribute / Hair | 20 | 10 | 10 | 10 |
| Attribute / Illumination | 10 | 5 | 5 | 5 |
| Attribute / Weather | 5 | 2.5 | 2 | 3 |
| Camera / Camera Movement | 25 | 12.5 | 12 | 13 |
| Camera / Framing/Zoom | 15 | 7.5 | 8 | 7 |
| Camera / Perspective Transfer | 20 | 10 | 10 | 10 |
| Composition / Environment Object | 30 | 15 | 15 | 15 |
| Composition / Person | 30 | 15 | 15 | 15 |
| Composition / Person-related Object | 30 | 15 | 15 | 15 |
| Motion / Face/Expression | 35 | 17.5 | 18 | 17 |
| Motion / Full-body Action | 30 | 15 | 15 | 15 |
| Motion / Hand/Arm | 35 | 17.5 | 18 | 17 |
| Motion / Head/Gaze | 18 | 9 | 9 | 9 |
| Motion / Multi-person/Group Motion | 25 | 12.5 | 12 | 13 |
| Motion / Object Motion | 15 | 7.5 | 7 | 8 |
| Motion / Upper-body/Posture | 22 | 11 | 11 | 11 |
| Spatial / Object-Object | 25 | 12.5 | 12 | 13 |
| Spatial / Person-Environment | 42 | 21 | 21 | 21 |
| Spatial / Person-Person | 23 | 11.5 | 12 | 11 |
| Style / Background-local Style | 7 | 3.5 | 3 | 4 |
| Style / Global Art/Rendering Style | 8 | 4 | 4 | 4 |
| Style / Global Color/Tone/Graphic Texture | 8 | 4 | 4 | 4 |
| Style / Global Media/Era Style | 8 | 4 | 4 | 4 |
| Style / Person-local Style | 7 | 3.5 | 4 | 3 |
| Style / Specified Object-local Style | 7 | 3.5 | 3 | 4 |
| Temporal / Onset/Early Termination | 4 | 2 | 2 | 2 |
| Temporal / Pause/Reverse | 5 | 2.5 | 3 | 2 |
| Temporal / Progress Speed | 6 | 3 | 3 | 3 |

## Records

## human_001

### human_001_E1

```json
{
  "video_id": "human_001",
  "edit_id": "human_001_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "green_fortress_toy",
    "target_description": "the green fortress toy",
    "source_state": "The fortress toy is green.",
    "desired_change": "The fortress toy becomes stone gray."
  },
  "timing": {
    "edit_point_sec": 16,
    "effect_start_sec": 16,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      15,
      20
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 16.0 seconds, change the green fortress toy from green to stone gray over the next two seconds.",
  "expected_result": {
    "description": "The fortress toy becomes stone gray.",
    "target_phrase": "stone-gray fortress toy"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      15,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_001_E2A

```json
{
  "video_id": "human_001",
  "edit_id": "human_001_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "two_beast_toys",
    "target_description": "the two beast toys",
    "source_state": "The two beast toys are displayed side by side.",
    "desired_change": "The two beast toys face each other at close range."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      30.0,
      34.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.0 seconds, reposition the two beast toys so they face each other at close range.",
  "expected_result": {
    "description": "The two beast toys face each other at close range.",
    "target_phrase": "two beast toys facing each other"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_001_E2B

```json
{
  "video_id": "human_001",
  "edit_id": "human_001_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_001_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "right_hand_beast_toy",
    "target_description": "the right-hand beast toy",
    "source_state": "The right-hand beast toy is held in a stable display position.",
    "desired_change": "The right-hand beast toy nods its head twice."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      30.0,
      35.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 31.0 seconds, make the right-hand beast toy nod its head twice.",
  "expected_result": {
    "description": "The right-hand beast toy nods its head twice.",
    "target_phrase": "right-hand beast toy nodding twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of human_001_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_001_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the right-hand beast toy on B independently of E1's change to the green fortress toy; both edit results must coexist in C."
  }
}
```

## human_002

### human_002_E1

```json
{
  "video_id": "human_002",
  "edit_id": "human_002_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_002.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_hair",
    "target_description": "the woman's hair",
    "source_state": "The woman has long brown hair.",
    "desired_change": "The woman's hair becomes dark auburn."
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
  "instruction": "Starting at 14.0 seconds, change the woman's hair from brown to dark auburn over the next two seconds.",
  "expected_result": {
    "description": "The woman's hair becomes dark auburn.",
    "target_phrase": "dark-auburn hair"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_002_E2A

```json
{
  "video_id": "human_002",
  "edit_id": "human_002_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_002.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman alternates her gaze between the phone and the camera.",
    "desired_change": "The woman looks up from the phone and nods twice toward the camera."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the woman look up from her phone and nod twice toward the camera.",
  "expected_result": {
    "description": "The woman looks up from the phone and nods twice toward the camera.",
    "target_phrase": "looks up and nods twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_002_E2B

```json
{
  "video_id": "human_002",
  "edit_id": "human_002_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_002_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "red_hair_clip",
    "target_description": "a red hair clip",
    "source_state": "No hair clip is visible above the woman's left ear.",
    "desired_change": "A small red hair clip appears above the woman's left ear."
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
  "instruction": "At 29.0 seconds, add a small red hair clip above the woman's left ear.",
  "expected_result": {
    "description": "A small red hair clip appears above the woman's left ear.",
    "target_phrase": "small red hair clip"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_002_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_002_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a red hair clip on B independently of E1's change to the woman's hair; both edit results must coexist in C."
  }
}
```

## human_007

### human_007_E1

```json
{
  "video_id": "human_007",
  "edit_id": "human_007_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_007.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_beard",
    "target_description": "the man's beard",
    "source_state": "The man has a short dark beard.",
    "desired_change": "The man's beard becomes a narrow moustache."
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
  "instruction": "Starting at 14.0 seconds, change the man's short beard to a narrow moustache over the next two seconds.",
  "expected_result": {
    "description": "The man's beard becomes a narrow moustache.",
    "target_phrase": "narrow moustache"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_007_E2A

```json
{
  "video_id": "human_007",
  "edit_id": "human_007_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_007.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a neutral expression.",
    "desired_change": "The man smiles broadly while speaking."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the man smile broadly while speaking.",
  "expected_result": {
    "description": "The man smiles broadly while speaking.",
    "target_phrase": "smiles broadly"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_007_E2B

```json
{
  "video_id": "human_007",
  "edit_id": "human_007_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_007_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The speaker is shown from an external close view.",
    "desired_change": "The room is shown from the speaker's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the speaker's first-person perspective over the next three seconds.",
  "expected_result": {
    "description": "The room is shown from the speaker's first-person viewpoint.",
    "target_phrase": "speaker's first-person room view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_007_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_007_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the man's beard; both edit results must coexist in C."
  }
}
```

## human_012

### human_012_E1

```json
{
  "video_id": "human_012",
  "edit_id": "human_012_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_012.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "red_hand_gripper",
    "target_description": "the red hand gripper",
    "source_state": "The hand gripper is red.",
    "desired_change": "The hand gripper becomes matte black."
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
  "instruction": "Starting at 14.0 seconds, change the red hand gripper to matte black over the next two seconds.",
  "expected_result": {
    "description": "The hand gripper becomes matte black.",
    "target_phrase": "matte-black hand gripper"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_012_E2A

```json
{
  "video_id": "human_012",
  "edit_id": "human_012_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_012.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_holding_blue_gripper",
    "target_description": "the man holding the blue gripper",
    "source_state": "The man holds the blue gripper while explaining it.",
    "desired_change": "The man squeezes the blue gripper three times."
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
  "instruction": "Starting at 29.0 seconds, make the man squeeze the blue hand gripper three times.",
  "expected_result": {
    "description": "The man squeezes the blue gripper three times.",
    "target_phrase": "squeezes the blue gripper three times"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_012_E2B

```json
{
  "video_id": "human_012",
  "edit_id": "human_012_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_012_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The man and hand gripper are shown from an external view.",
    "desired_change": "The gripper is shown from the man's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the man's first-person perspective toward the hand gripper over three seconds.",
  "expected_result": {
    "description": "The gripper is shown from the man's first-person viewpoint.",
    "target_phrase": "first-person view of hand gripper"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_012_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_012_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the red hand gripper; both edit results must coexist in C."
  }
}
```

## human_013

### human_013_E1

```json
{
  "video_id": "human_013",
  "edit_id": "human_013_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "main_performer",
    "target_description": "the main performer",
    "source_state": "The main performer stands on the dark stage.",
    "desired_change": "The main performer walks continuously across the stage toward the right for four seconds."
  },
  "timing": {
    "edit_point_sec": 19,
    "effect_start_sec": 19,
    "effect_end_sec": 23,
    "evaluation_window_sec": [
      18,
      25
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 19.0 seconds, make the main performer walk continuously across the stage toward the right for four seconds.",
  "expected_result": {
    "description": "The main performer walks continuously across the stage toward the right for four seconds.",
    "target_phrase": "continuous rightward stage walk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      18,
      25
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_013_E2A

```json
{
  "video_id": "human_013",
  "edit_id": "human_013_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "main_performer_and_nearest_photographer",
    "target_description": "the main performer and the nearest photographer",
    "source_state": "The performer and nearest photographer occupy separated stage areas.",
    "desired_change": "The nearest photographer stands directly to the performer's right."
  },
  "timing": {
    "edit_point_sec": 24.0,
    "effect_start_sec": 24.0,
    "effect_end_sec": 25.0,
    "evaluation_window_sec": [
      23.0,
      27.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.0 seconds, reposition the nearest photographer directly to the right of the main performer.",
  "expected_result": {
    "description": "The nearest photographer stands directly to the performer's right.",
    "target_phrase": "photographer right of performer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.0,
      27.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_013_E2B

```json
{
  "video_id": "human_013",
  "edit_id": "human_013_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_013_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Removal",
    "scope": "Background Person"
  },
  "target": {
    "target_id": "background_photographer",
    "target_description": "the background photographer",
    "source_state": "A photographer is visible among the people behind the performer.",
    "desired_change": "The background photographer is removed from the scene."
  },
  "timing": {
    "edit_point_sec": 34.0,
    "effect_start_sec": 34.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      33.0,
      37.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 34.0 seconds, remove the background photographer from the scene.",
  "expected_result": {
    "description": "The background photographer is removed from the scene.",
    "target_phrase": "background photographer removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_013_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_013_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the background photographer on B independently of E1's change to the main performer; both edit results must coexist in C."
  }
}
```

## human_015

### human_015_E1

```json
{
  "video_id": "human_015",
  "edit_id": "human_015_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "singer",
    "target_description": "the singer",
    "source_state": "The singer faces the microphone while performing.",
    "desired_change": "The singer briefly looks upward while singing."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the singer briefly look upward while singing.",
  "expected_result": {
    "description": "The singer briefly looks upward while singing.",
    "target_phrase": "singer looking upward"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_015_E2A

```json
{
  "video_id": "human_015",
  "edit_id": "human_015_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "singer_and_nearest_audience_member",
    "target_description": "the singer and the nearest audience member",
    "source_state": "The singer and nearest audience member are separated by the stage edge.",
    "desired_change": "The nearest audience member is positioned directly in front of the singer."
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
  "instruction": "At 29.0 seconds, reposition the nearest audience member directly in front of the singer.",
  "expected_result": {
    "description": "The nearest audience member is positioned directly in front of the singer.",
    "target_phrase": "audience member in front of singer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_015_E2B

```json
{
  "video_id": "human_015",
  "edit_id": "human_015_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_015_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The singer is shown from the audience's external viewpoint.",
    "desired_change": "The audience is shown from the singer's first-person stage viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the singer's first-person perspective toward the audience over three seconds.",
  "expected_result": {
    "description": "The audience is shown from the singer's first-person stage viewpoint.",
    "target_phrase": "singer's first-person audience view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_015_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_015_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the singer; both edit results must coexist in C."
  }
}
```

## human_017

### human_017_E1

```json
{
  "video_id": "human_017",
  "edit_id": "human_017_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "seated_red_clothed_character",
    "target_description": "the seated red-clothed character",
    "source_state": "The seated character performs dialogue gestures on the sofa.",
    "desired_change": "The seated character gives an exaggerated shoulder shrug."
  },
  "timing": {
    "edit_point_sec": 20.0,
    "effect_start_sec": 20.0,
    "effect_end_sec": 22.0,
    "evaluation_window_sec": [
      19.5,
      22.6
    ],
    "temporal_behavior": "bounded action",
    "source_stage_at_edit": "the red-clothed seated participant has reappeared after the standing-role shot"
  },
  "instruction": "Starting at 20.0 seconds, make the seated participant in red raise one hand and hold it overhead for two seconds.",
  "expected_result": {
    "description": "The seated character gives an exaggerated shoulder shrug.",
    "target_phrase": "exaggerated shoulder shrug"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.5,
      22.6
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The seated participant in red reappears around 19.6 seconds and remains visible through this short segment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_017_E2A

```json
{
  "video_id": "human_017",
  "edit_id": "human_017_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "standing_character",
    "target_description": "the standing character",
    "source_state": "The standing character is positioned near the center of the plain-wall setting.",
    "desired_change": "The standing character is positioned closer to the left side of the frame."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      30.0,
      34.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.0 seconds, reposition the standing character closer to the left side of the frame.",
  "expected_result": {
    "description": "The standing character is positioned closer to the left side of the frame.",
    "target_phrase": "standing character on the left"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_017_E2B

```json
{
  "video_id": "human_017",
  "edit_id": "human_017_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_017_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Object-local Style",
    "operation": "Clay-animation Rendering",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "standing_character_curved_handled_cane",
    "target_description": "the standing character's curved-handled cane",
    "source_state": "The curved-handled cane has a realistic solid appearance.",
    "desired_change": "The curved-handled cane is rendered as a clay-animation prop."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      30.0,
      35.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31.0 seconds, render the standing character's curved-handled cane as a clay-animation prop over the next two seconds.",
  "expected_result": {
    "description": "The curved-handled cane is rendered as a clay-animation prop.",
    "target_phrase": "clay-animation curved cane"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_017_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_017_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the standing character's curved-handled cane on B independently of E1's change to the seated red-clothed character; both edit results must coexist in C."
  }
}
```

## human_018

### human_018_E1

```json
{
  "video_id": "human_018",
  "edit_id": "human_018_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_018.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Reverse",
    "operation": "Temporary Pause",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "ingredient_assembly_process",
    "target_description": "the ingredient-assembly process",
    "source_state": "The ingredient assembly progresses continuously.",
    "desired_change": "The assembly process pauses for three seconds and then continues."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 23,
    "evaluation_window_sec": [
      19,
      25
    ],
    "temporal_behavior": "temporary semantic pause"
  },
  "instruction": "Starting at 20.0 seconds, pause the ingredient-assembly process for three seconds before it continues.",
  "expected_result": {
    "description": "The assembly process pauses for three seconds and then continues.",
    "target_phrase": "three-second ingredient-assembly pause"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      25
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_018_E2A

```json
{
  "video_id": "human_018",
  "edit_id": "human_018_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_018.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "cook_blue_apron",
    "target_description": "the blue apron on the cook's visible torso",
    "source_state": "The cook wears a blue apron over the visible torso.",
    "desired_change": "The blue apron is removed from the cook's visible torso."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      30.0,
      34.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "pouring chopped green onions while the blue apron remains visible"
  },
  "instruction": "At 31.0 seconds, remove the blue apron from the cook's visible torso.",
  "expected_result": {
    "description": "The blue apron is absent from the cook's visible torso.",
    "target_phrase": "cook without the blue apron"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The blue apron is clearly visible on the cook's torso while chopped green onions are poured into the mixing bowl."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_018_E2B

```json
{
  "video_id": "human_018",
  "edit_id": "human_018_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_018_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Visible Hands"
  },
  "target": {
    "target_id": "hand_holding_small_bowl_of_chopped_green_onions",
    "target_description": "the hand holding the small glass bowl of chopped green onions",
    "source_state": "The cook holds the small glass bowl of chopped green onions above the mixing bowl before pouring.",
    "desired_change": "The cook rotates the small glass bowl once toward the camera for display before pouring its contents."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "continuous action",
    "source_stage_at_edit": "holding the small glass bowl of chopped green onions above the mixing bowl"
  },
  "instruction": "Starting at 29.0 seconds, make the cook rotate the small glass bowl of chopped green onions once toward the camera before pouring.",
  "expected_result": {
    "description": "The cook presents the small glass bowl by rotating it once toward the camera before pouring the chopped green onions.",
    "target_phrase": "small bowl rotated once for display"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of human_018_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "At 29 seconds, the right hand clearly holds a small glass bowl containing chopped green onions above the mixing bowl."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_018_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the bowl-display hand motion on B independently of E1's temporary pause in ingredient assembly; both results must coexist in C."
  }
}
```

## human_019

### human_019_E1

```json
{
  "video_id": "human_019",
  "edit_id": "human_019_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "printer_and_nearest_onlooker",
    "target_description": "the printer and the nearest onlooker",
    "source_state": "The printer and nearest onlooker stand apart around the press.",
    "desired_change": "The nearest onlooker stands directly to the printer's left."
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
  "instruction": "At 14.0 seconds, reposition the nearest onlooker directly to the left of the printer.",
  "expected_result": {
    "description": "The nearest onlooker stands directly to the printer's left.",
    "target_phrase": "onlooker left of printer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_019_E2A

```json
{
  "video_id": "human_019",
  "edit_id": "human_019_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Addition",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "apprentice_printer",
    "target_description": "an apprentice printer",
    "source_state": "No apprentice stands beside the printing press.",
    "desired_change": "An apprentice printer appears beside the press."
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
  "instruction": "At 29.0 seconds, add an apprentice printer beside the printing press.",
  "expected_result": {
    "description": "An apprentice printer appears beside the press.",
    "target_phrase": "apprentice printer"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_019_E2B

```json
{
  "video_id": "human_019",
  "edit_id": "human_019_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_019_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Dolly In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed side view of the man and printing press.",
    "desired_change": "The camera moves closer to the printing surface."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, move the camera slowly toward the printing surface for four seconds.",
  "expected_result": {
    "description": "The camera moves closer to the printing surface.",
    "target_phrase": "camera moving toward the printing surface"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_019_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_019_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the printer and the nearest onlooker; both edit results must coexist in C."
  }
}
```

## human_020

### human_020_E1

```json
{
  "video_id": "human_020",
  "edit_id": "human_020_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "purple_shelf_lamp",
    "target_description": "the purple shelf lamp",
    "source_state": "A purple ambient lamp illuminates the shelving unit.",
    "desired_change": "The purple shelf lamp is removed."
  },
  "timing": {
    "edit_point_sec": 17,
    "effect_start_sec": 17,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      16,
      20
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 17.0 seconds, remove the purple ambient lamp from the shelving unit.",
  "expected_result": {
    "description": "The purple shelf lamp is removed.",
    "target_phrase": "purple shelf lamp removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      16,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_020_E2A

```json
{
  "video_id": "human_020",
  "edit_id": "human_020_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "microphone",
    "target_description": "the microphone",
    "source_state": "The microphone occupies the left foreground beside the speaker.",
    "desired_change": "The microphone is positioned in the right foreground beside the speaker."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      31.0,
      35.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32.0 seconds, reposition the microphone in the right foreground beside the speaker.",
  "expected_result": {
    "description": "The microphone is positioned in the right foreground beside the speaker.",
    "target_phrase": "microphone in the right foreground"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_020_E2B

```json
{
  "video_id": "human_020",
  "edit_id": "human_020_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_020_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1980s Home-video Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The studio monologue has a modern digital-video appearance.",
    "desired_change": "The full frame resembles an authenticated 1980s home-video recording."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      31.0,
      36.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 32.0 seconds, transform the full frame into an authentic 1980s home-video recording over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles an authenticated 1980s home-video recording.",
    "target_phrase": "1980s home-video recording"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_020_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_020_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the purple shelf lamp; both edit results must coexist in C."
  }
}
```

## human_023

### human_023_E1

```json
{
  "video_id": "human_023",
  "edit_id": "human_023_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Body/Skin Appearance",
    "operation": "Body-shape Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "inverted_athlete_visible_arms",
    "target_description": "the inverted athlete's visible arms",
    "source_state": "The athlete has a lean arm build.",
    "desired_change": "His visible arm muscles become more defined."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 12,
    "evaluation_window_sec": [
      9.0,
      14.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12.0 seconds, make the inverted athlete's visible arm muscles more defined over the next two seconds.",
  "expected_result": {
    "description": "His visible arm muscles become more defined.",
    "target_phrase": "more defined arm muscles"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      9.0,
      14.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_023_E2A

```json
{
  "video_id": "human_023",
  "edit_id": "human_023_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "inverted_athlete",
    "target_description": "the inverted athlete",
    "source_state": "The athlete holds a stable wall-supported handstand.",
    "desired_change": "The athlete performs a controlled leg split while inverted."
  },
  "timing": {
    "edit_point_sec": 28.0,
    "effect_start_sec": 28.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      27.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 28.0 seconds, make the inverted athlete perform a controlled leg split.",
  "expected_result": {
    "description": "The athlete performs a controlled leg split while inverted.",
    "target_phrase": "controlled inverted leg split"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_023_E2B

```json
{
  "video_id": "human_023",
  "edit_id": "human_023_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_023_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Lateral Move",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed wide view of the athlete and coach.",
    "desired_change": "The camera moves slowly to the right while observing both people."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      27.0,
      34.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 27.0 seconds, move the camera slowly to the right for four seconds while viewing both people.",
  "expected_result": {
    "description": "The camera moves slowly to the right while observing both people.",
    "target_phrase": "slow rightward camera move"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_023_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_023_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the inverted athlete's visible arms; both edit results must coexist in C."
  }
}
```

## human_026

### human_026_E1

```json
{
  "video_id": "human_026",
  "edit_id": "human_026_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "leading_runner_red_jersey",
    "target_description": "the leading runner's red jersey",
    "source_state": "The leading runner wears a red jersey.",
    "desired_change": "The leading runner's jersey becomes bright yellow."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 12,
    "evaluation_window_sec": [
      9.0,
      14.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12.0 seconds, change the leading runner's red jersey to bright yellow over the next two seconds.",
  "expected_result": {
    "description": "The leading runner's jersey becomes bright yellow.",
    "target_phrase": "bright-yellow running jersey"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      9.0,
      14.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_026_E2A

```json
{
  "video_id": "human_026",
  "edit_id": "human_026_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "nearest_trailing_runner",
    "target_description": "the nearest trailing runner",
    "source_state": "The nearest trailing runner runs at a steady cadence.",
    "desired_change": "The runner performs a high-knee sprint for four seconds."
  },
  "timing": {
    "edit_point_sec": 28.0,
    "effect_start_sec": 28.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      27.0,
      34.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 28.0 seconds, make the nearest trailing runner perform a high-knee sprint for four seconds.",
  "expected_result": {
    "description": "The runner performs a high-knee sprint for four seconds.",
    "target_phrase": "four-second high-knee sprint"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_026_E2B

```json
{
  "video_id": "human_026",
  "edit_id": "human_026_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_026_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Addition",
    "scope": "Background Person"
  },
  "target": {
    "target_id": "additional_runner",
    "target_description": "an additional runner",
    "source_state": "The outermost visible lane has no nearby runner.",
    "desired_change": "An additional runner appears in the outermost visible lane."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      27.0,
      31.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 27.0 seconds, add another runner to the outermost visible lane.",
  "expected_result": {
    "description": "An additional runner appears in the outermost visible lane.",
    "target_phrase": "additional runner in the outer lane"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_026_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      31.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_026_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes an additional runner on B independently of E1's change to the leading runner's red jersey; both edit results must coexist in C."
  }
}
```

## human_027

### human_027_E1

```json
{
  "video_id": "human_027",
  "edit_id": "human_027_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_tied_back_blond_hair",
    "target_description": "the woman's tied-back blond hair",
    "source_state": "The woman's blond hair is tied back.",
    "desired_change": "Her hair becomes loose and shoulder length."
  },
  "timing": {
    "edit_point_sec": 15,
    "effect_start_sec": 15,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      14,
      19
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 15.0 seconds, change the woman's tied-back blond hair to loose shoulder-length hair over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes loose and shoulder length.",
    "target_phrase": "loose shoulder-length blond hair"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      14,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 15.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_027_E2A

```json
{
  "video_id": "human_027",
  "edit_id": "human_027_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman speaks with a thoughtful interview expression.",
    "desired_change": "The woman smiles warmly toward the interviewer."
  },
  "timing": {
    "edit_point_sec": 30.0,
    "effect_start_sec": 30.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      29.0,
      35.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 30.0 seconds, make the woman smile warmly toward the interviewer.",
  "expected_result": {
    "description": "The woman smiles warmly toward the interviewer.",
    "target_phrase": "warm smile toward the interviewer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_027_E2B

```json
{
  "video_id": "human_027",
  "edit_id": "human_027_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_027_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The woman is shown from an external interview view.",
    "desired_change": "The interviewer is shown from the woman's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      29.0,
      35.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 30.0 seconds, change the view to the woman's first-person perspective toward the interviewer over three seconds.",
  "expected_result": {
    "description": "The interviewer is shown from the woman's first-person viewpoint.",
    "target_phrase": "woman's first-person interview view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_027_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_027_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the woman's tied-back blond hair; both edit results must coexist in C."
  }
}
```

## human_028

### human_028_E1

```json
{
  "video_id": "human_028",
  "edit_id": "human_028_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_028.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "green_electric_guitar",
    "target_description": "the green electric guitar",
    "source_state": "The electric guitar is green.",
    "desired_change": "The electric guitar becomes a sunburst brown finish."
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
  "instruction": "Starting at 14.0 seconds, change the green electric guitar to a sunburst brown finish over the next two seconds.",
  "expected_result": {
    "description": "The electric guitar becomes a sunburst brown finish.",
    "target_phrase": "sunburst brown guitar"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_028_E2A

```json
{
  "video_id": "human_028",
  "edit_id": "human_028_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_028.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "guitarist_strumming_hand",
    "target_description": "the guitarist's strumming hand",
    "source_state": "The guitarist plucks and strums near the guitar body.",
    "desired_change": "The guitarist uses alternating up-and-down strums."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "continuous action"
  },
  "instruction": "Starting at 29.0 seconds, make the guitarist use alternating up-and-down strums.",
  "expected_result": {
    "description": "The guitarist uses alternating up-and-down strums.",
    "target_phrase": "alternating up-and-down strums"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_028_E2B

```json
{
  "video_id": "human_028",
  "edit_id": "human_028_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_028_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Woodcut Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "performance_background",
    "target_description": "the performance background",
    "source_state": "The performance background has a realistic photographic appearance.",
    "desired_change": "The performance background is rendered in a carved woodcut style."
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
  "instruction": "Starting at 29.0 seconds, render the performance background in a carved woodcut style over the next two seconds.",
  "expected_result": {
    "description": "The performance background is rendered in a carved woodcut style.",
    "target_phrase": "woodcut performance background"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_028_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_028_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the performance background on B independently of E1's change to the green electric guitar; both edit results must coexist in C."
  }
}
```

## human_029

### human_029_E1

```json
{
  "video_id": "human_029",
  "edit_id": "human_029_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_029.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Body/Skin Appearance",
    "operation": "Skin-detail Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_visible_forearm_skin",
    "target_description": "the man's visible forearm skin",
    "source_state": "The man's visible forearm skin has an even appearance.",
    "desired_change": "Light freckles appear across the visible forearm skin."
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
  "instruction": "Starting at 14.0 seconds, add light freckles across the man's visible forearm skin over the next two seconds.",
  "expected_result": {
    "description": "Light freckles appear across the visible forearm skin.",
    "target_phrase": "light freckles on forearm"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_029_E2A

```json
{
  "video_id": "human_029",
  "edit_id": "human_029_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_029.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a neutral expression.",
    "desired_change": "The man puffs out both cheeks and raises his eyebrows."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "bounded expression"
  },
  "instruction": "Starting at 29.0 seconds, make the man puff out both cheeks and raise his eyebrows.",
  "expected_result": {
    "description": "The man puffs out both cheeks and raises his eyebrows.",
    "target_phrase": "puffed cheeks and raised eyebrows"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_029_E2B

```json
{
  "video_id": "human_029",
  "edit_id": "human_029_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_029_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands to the left of the world-map decoration.",
    "desired_change": "The man stands at the center of the world-map decoration."
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
  "instruction": "At 29.0 seconds, reposition the man at the center of the world-map decoration.",
  "expected_result": {
    "description": "The man stands at the center of the world-map decoration.",
    "target_phrase": "man centered on the map"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_029_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_029_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man on B independently of E1's change to the man's visible forearm skin; both edit results must coexist in C."
  }
}
```

## human_031

### human_031_E1

```json
{
  "video_id": "human_031",
  "edit_id": "human_031_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "red_storage_cabinet",
    "target_description": "the red storage cabinet",
    "source_state": "A red storage cabinet is visible in the dense room background.",
    "desired_change": "The storage cabinet becomes teal."
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
  "instruction": "Starting at 14.0 seconds, change the red storage cabinet in the background to teal over the next two seconds.",
  "expected_result": {
    "description": "The storage cabinet becomes teal.",
    "target_phrase": "teal storage cabinet"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_031_E2A

```json
{
  "video_id": "human_031",
  "edit_id": "human_031_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man looks mainly toward the camera.",
    "desired_change": "The man looks over his left shoulder."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the man look over his left shoulder.",
  "expected_result": {
    "description": "The man looks over his left shoulder.",
    "target_phrase": "looks over his left shoulder"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_031_E2B

```json
{
  "video_id": "human_031",
  "edit_id": "human_031_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_031_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Leftward Slide",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed view of the man and dense room.",
    "desired_change": "The camera slides smoothly left across the tabletop and room."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, slide the camera smoothly left across the tabletop and room for three seconds.",
  "expected_result": {
    "description": "The camera slides smoothly left across the tabletop and room.",
    "target_phrase": "smooth leftward camera slide"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_031_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_031_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the red storage cabinet; both edit results must coexist in C."
  }
}
```

## human_033

### human_033_E1

```json
{
  "video_id": "human_033",
  "edit_id": "human_033_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "displayed_football_jersey",
    "target_description": "the displayed football jersey",
    "source_state": "The jersey is held close to the camera for inspection.",
    "desired_change": "The jersey sways gently from left to right twice."
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
  "instruction": "Starting at 14.0 seconds, make the displayed football jersey sway gently from left to right twice.",
  "expected_result": {
    "description": "The jersey sways gently from left to right twice.",
    "target_phrase": "jersey swaying twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_033_E2A

```json
{
  "video_id": "human_033",
  "edit_id": "human_033_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "displayed_jersey",
    "target_description": "the displayed jersey",
    "source_state": "The displayed jersey overlaps the hanging shirts behind it.",
    "desired_change": "The displayed jersey is centered between the two nearest background shirts."
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
  "instruction": "At 29.0 seconds, reposition the displayed jersey between the two nearest background shirts.",
  "expected_result": {
    "description": "The displayed jersey is centered between the two nearest background shirts.",
    "target_phrase": "jersey between two background shirts"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_033_E2B

```json
{
  "video_id": "human_033",
  "edit_id": "human_033_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_033_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "jersey_hanger",
    "target_description": "the jersey hanger",
    "source_state": "The football jersey hangs from a plain hanger.",
    "desired_change": "The plain hanger is replaced with a dark wooden hanger."
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
  "instruction": "At 29.0 seconds, replace the jersey's plain hanger with a dark wooden hanger.",
  "expected_result": {
    "description": "The plain hanger is replaced with a dark wooden hanger.",
    "target_phrase": "dark wooden hanger"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_033_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_033_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the jersey hanger on B independently of E1's change to the displayed football jersey; both edit results must coexist in C."
  }
}
```

## human_034

### human_034_E1

```json
{
  "video_id": "human_034",
  "edit_id": "human_034_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_034.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Onset/Early Termination",
    "operation": "Earlier Termination",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "transition_from_spray_gun_treatment_to_black_pickup_cleaning",
    "target_description": "the transition from spray-gun treatment to the black-pickup cleaning stage",
    "source_state": "The spray-gun treatment continues until the video cuts to black-pickup cleaning near 30.3 seconds.",
    "desired_change": "The spray-gun treatment ends at 24.0 seconds and the black-pickup cleaning stage begins immediately."
  },
  "timing": {
    "edit_point_sec": 19.0,
    "effect_start_sec": 19.0,
    "effect_end_sec": 24.0,
    "evaluation_window_sec": [
      18.0,
      29.0
    ],
    "temporal_behavior": "advanced stage onset",
    "source_stage_at_edit": "ongoing spray-gun treatment before the transition to black-pickup cleaning"
  },
  "instruction": "At 19.0 seconds, end the spray-gun treatment at 24.0 seconds and begin the black-pickup cleaning stage immediately.",
  "expected_result": {
    "description": "The spray-gun treatment ends at 24.0 seconds, followed immediately by the black-pickup cleaning stage.",
    "target_phrase": "black-pickup cleaning beginning at 24 seconds"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      18.0,
      29.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The source shows continuous spray-gun treatment before cutting to black-pickup cleaning near 30.3 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_034_E2A

```json
{
  "video_id": "human_034",
  "edit_id": "human_034_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_034.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "yellow_cloth_and_truck_tail_light",
    "target_description": "the yellow cloth and the truck tail light",
    "source_state": "The yellow cloth is held near the black truck's rear panel.",
    "desired_change": "The yellow cloth is positioned directly below the tail light."
  },
  "timing": {
    "edit_point_sec": 34.0,
    "effect_start_sec": 34.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      33.0,
      37.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 34.0 seconds, position the yellow cloth directly below the truck's tail light.",
  "expected_result": {
    "description": "The yellow cloth is positioned directly below the tail light.",
    "target_phrase": "yellow cloth below the tail light"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_034_E2B

```json
{
  "video_id": "human_034",
  "edit_id": "human_034_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_034_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "blue_spray_bottle",
    "target_description": "a blue spray bottle",
    "source_state": "No blue spray bottle is visible beside the man and black truck.",
    "desired_change": "A blue spray bottle appears beside the man near the black truck."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      33.0,
      37.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 34.0 seconds, add a blue spray bottle beside the man near the black truck.",
  "expected_result": {
    "description": "A blue spray bottle appears beside the man near the black truck.",
    "target_phrase": "blue spray bottle beside the man"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_034_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      37.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_034_E1",
    "must_preserve_e1_result": true,
    "description": "This edit adds a blue spray bottle during the black-pickup stage on B after E1 advances that stage to 24.0 seconds; both results must coexist in C."
  }
}
```

## human_039

### human_039_E1

```json
{
  "video_id": "human_039",
  "edit_id": "human_039_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "microphone_arm_and_microphone",
    "target_description": "the microphone arm and microphone",
    "source_state": "The adjustable arm enters from the upper left toward the central microphone.",
    "desired_change": "The microphone arm is positioned directly above the central microphone."
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
  "instruction": "At 14.0 seconds, reposition the adjustable microphone arm directly above the central microphone.",
  "expected_result": {
    "description": "The microphone arm is positioned directly above the central microphone.",
    "target_phrase": "microphone arm above the microphone"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_039_E2A

```json
{
  "video_id": "human_039",
  "edit_id": "human_039_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_headphones",
    "target_description": "the man's headphones",
    "source_state": "The man wears dark over-ear headphones.",
    "desired_change": "The dark headphones are replaced with silver over-ear headphones."
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
  "instruction": "At 29.0 seconds, replace the man's dark headphones with silver over-ear headphones.",
  "expected_result": {
    "description": "The dark headphones are replaced with silver over-ear headphones.",
    "target_phrase": "silver over-ear headphones"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_039_E2B

```json
{
  "video_id": "human_039",
  "edit_id": "human_039_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_039_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The podcast speaker is shown from an external frontal view.",
    "desired_change": "The microphone and studio are shown from the speaker's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the podcast speaker's first-person perspective over three seconds.",
  "expected_result": {
    "description": "The microphone and studio are shown from the speaker's first-person viewpoint.",
    "target_phrase": "podcast speaker's first-person view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_039_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_039_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the microphone arm and microphone; both edit results must coexist in C."
  }
}
```

## human_040

### human_040_E1

```json
{
  "video_id": "human_040",
  "edit_id": "human_040_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands or walks slowly near the panoramic camera.",
    "desired_change": "The man walks steadily across the snow toward the nearest birch trunk for four seconds."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      11.0,
      18.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 13.0 seconds, make the man walk steadily across the snow toward the nearest birch trunk for four seconds.",
  "expected_result": {
    "description": "The man walks steadily across the snow toward the nearest birch trunk for four seconds.",
    "target_phrase": "steady walk toward birch trunk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.0,
      18.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_040_E2A

```json
{
  "video_id": "human_040",
  "edit_id": "human_040_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands among several birch trees.",
    "desired_change": "The man stands directly beside the nearest birch trunk."
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
  "instruction": "At 29.0 seconds, reposition the man directly beside the nearest birch trunk.",
  "expected_result": {
    "description": "The man stands directly beside the nearest birch trunk.",
    "target_phrase": "man beside the birch trunk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_040_E2B

```json
{
  "video_id": "human_040",
  "edit_id": "human_040_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_040_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Addition",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "second_hiker",
    "target_description": "a second hiker",
    "source_state": "Only one hiker is visible in the snowy woodland.",
    "desired_change": "A second hiker appears beside the man."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      28.0,
      32.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 28.0 seconds, add a second hiker beside the man in the snowy woodland.",
  "expected_result": {
    "description": "A second hiker appears beside the man.",
    "target_phrase": "second woodland hiker"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_040_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_040_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a second hiker on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_045

### human_045_E1

```json
{
  "video_id": "human_045",
  "edit_id": "human_045_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "transparent_storage_bin_lid",
    "target_description": "the transparent storage-bin lid",
    "source_state": "The storage-bin lid is clear and colorless.",
    "desired_change": "The storage-bin lid becomes translucent blue."
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
  "instruction": "Starting at 14.0 seconds, change the clear storage-bin lid to translucent blue over the next two seconds.",
  "expected_result": {
    "description": "The storage-bin lid becomes translucent blue.",
    "target_phrase": "translucent-blue bin lid"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_045_E2A

```json
{
  "video_id": "human_045",
  "edit_id": "human_045_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man points toward the blocks while explaining them.",
    "desired_change": "The man lifts a handful of blocks and releases them into the bin."
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
  "instruction": "Starting at 29.0 seconds, make the man lift a handful of blocks and release them into the bin.",
  "expected_result": {
    "description": "The man lifts a handful of blocks and releases them into the bin.",
    "target_phrase": "blocks released into the bin"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_045_E2B

```json
{
  "video_id": "human_045",
  "edit_id": "human_045_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_045_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "storage_bin",
    "target_description": "the storage bin",
    "source_state": "The storage bin rests to the left side of the work surface.",
    "desired_change": "The storage bin is centered on the green cutting mat."
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
  "instruction": "At 29.0 seconds, reposition the storage bin at the center of the green cutting mat.",
  "expected_result": {
    "description": "The storage bin is centered on the green cutting mat.",
    "target_phrase": "storage bin centered on the mat"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_045_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_045_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the storage bin on B independently of E1's change to the transparent storage-bin lid; both edit results must coexist in C."
  }
}
```

## human_046

### human_046_E1

```json
{
  "video_id": "human_046",
  "edit_id": "human_046_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "middle_singer_short_hair",
    "target_description": "the middle singer's short hair",
    "source_state": "The middle singer has short hair.",
    "desired_change": "Her hair becomes shoulder-length braids."
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
  "instruction": "Starting at 14.0 seconds, change the middle singer's short hair to shoulder-length braids over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes shoulder-length braids.",
    "target_phrase": "shoulder-length braids"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_046_E2A

```json
{
  "video_id": "human_046",
  "edit_id": "human_046_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "three_performers",
    "target_description": "the three performers",
    "source_state": "The three performers sing while making small individual movements.",
    "desired_change": "The three performers nod together twice in rhythm."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 29.0 seconds, make the three performers nod together twice in rhythm.",
  "expected_result": {
    "description": "The three performers nod together twice in rhythm.",
    "target_phrase": "three synchronized nods"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_046_E2B

```json
{
  "video_id": "human_046",
  "edit_id": "human_046_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_046_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "left_singer_phone",
    "target_description": "the left singer's phone",
    "source_state": "The left singer holds a phone.",
    "desired_change": "The phone is replaced with a small egg shaker."
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
  "instruction": "At 29.0 seconds, replace the phone in the left singer's hand with a small egg shaker.",
  "expected_result": {
    "description": "The phone is replaced with a small egg shaker.",
    "target_phrase": "small egg shaker"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_046_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_046_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the left singer's phone on B independently of E1's change to the middle singer's short hair; both edit results must coexist in C."
  }
}
```

## human_047

### human_047_E1

```json
{
  "video_id": "human_047",
  "edit_id": "human_047_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Weather Change",
    "scope": "Background"
  },
  "target": {
    "target_id": "courtyard_weather",
    "target_description": "the courtyard weather",
    "source_state": "The courtyard is brightly sunlit under clear conditions.",
    "desired_change": "The courtyard becomes lightly overcast."
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
  "instruction": "Starting at 16.0 seconds, change the sunny courtyard to lightly overcast conditions over the next three seconds.",
  "expected_result": {
    "description": "The courtyard becomes lightly overcast.",
    "target_phrase": "lightly overcast courtyard"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      15,
      21
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_047_E2A

```json
{
  "video_id": "human_047",
  "edit_id": "human_047_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman holds or points toward the long pineapple leaves.",
    "desired_change": "The woman gently separates two overlapping pineapple leaves."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      30.0,
      36.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 31.0 seconds, make the woman gently separate two overlapping pineapple leaves.",
  "expected_result": {
    "description": "The woman gently separates two overlapping pineapple leaves.",
    "target_phrase": "separates two pineapple leaves"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_047_E2B

```json
{
  "video_id": "human_047",
  "edit_id": "human_047_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_047_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Clockwise Orbit",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera looks down at the central pineapple plant.",
    "desired_change": "The camera moves in a clockwise arc around the central plant."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      30.0,
      36.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 31.0 seconds, move the camera in a clockwise arc around the central pineapple plant for three seconds.",
  "expected_result": {
    "description": "The camera moves in a clockwise arc around the central plant.",
    "target_phrase": "clockwise orbit around pineapple"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_047_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_047_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the courtyard weather; both edit results must coexist in C."
  }
}
```

## human_048

### human_048_E1

```json
{
  "video_id": "human_048",
  "edit_id": "human_048_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_048.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "older_man_red_suspenders",
    "target_description": "the older man's red suspenders",
    "source_state": "The older man wears red suspenders.",
    "desired_change": "The suspenders become navy blue."
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
  "instruction": "Starting at 14.0 seconds, change the older man's red suspenders to navy blue over the next two seconds.",
  "expected_result": {
    "description": "The suspenders become navy blue.",
    "target_phrase": "navy-blue suspenders"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_048_E2A

```json
{
  "video_id": "human_048",
  "edit_id": "human_048_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_048.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_men",
    "target_description": "the two men",
    "source_state": "The two men alternate between talking and looking at the tabletop model.",
    "desired_change": "The two men lean toward the tabletop model together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 29.0 seconds, make the two men lean toward the tabletop model together.",
  "expected_result": {
    "description": "The two men lean toward the tabletop model together.",
    "target_phrase": "two men leaning toward the model"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_048_E2B

```json
{
  "video_id": "human_048",
  "edit_id": "human_048_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_048_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Object-local Style",
    "operation": "Low-poly Rendering",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "tabletop_miniature_model",
    "target_description": "the tabletop miniature model",
    "source_state": "The tabletop model has a realistic handcrafted appearance.",
    "desired_change": "The tabletop model is rendered in a low-poly style."
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
  "instruction": "Starting at 29.0 seconds, render the tabletop miniature model in a low-poly style over the next two seconds.",
  "expected_result": {
    "description": "The tabletop model is rendered in a low-poly style.",
    "target_phrase": "low-poly miniature model"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_048_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_048_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tabletop miniature model on B independently of E1's change to the older man's red suspenders; both edit results must coexist in C."
  }
}
```

## human_049

### human_049_E1

```json
{
  "video_id": "human_049",
  "edit_id": "human_049_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "russian_representative_navy_tie",
    "target_description": "the Russian representative's navy tie",
    "source_state": "The Russian representative wears a navy tie.",
    "desired_change": "The tie becomes burgundy red."
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
  "instruction": "Starting at 20.0 seconds, change the Russian representative's navy tie to burgundy red over the next two seconds.",
  "expected_result": {
    "description": "The tie becomes burgundy red.",
    "target_phrase": "burgundy-red tie"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_049_E2A

```json
{
  "video_id": "human_049",
  "edit_id": "human_049_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "opposing_front_row_representatives",
    "target_description": "the two front-row representatives on opposite sides of the meeting table",
    "source_state": "The two front-row representatives sit across the table in the meeting-wide shot.",
    "desired_change": "The two representatives turn toward each other and nod together."
  },
  "timing": {
    "edit_point_sec": 38.0,
    "effect_start_sec": 38.0,
    "effect_end_sec": 40.0,
    "evaluation_window_sec": [
      37.0,
      41.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 38.0 seconds, make the two front-row representatives on opposite sides of the meeting table turn toward each other and nod together.",
  "expected_result": {
    "description": "The two front-row representatives turn toward each other and nod together.",
    "target_phrase": "opposing representatives turn and nod together"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      37.0,
      41.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_049_E2B

```json
{
  "video_id": "human_049",
  "edit_id": "human_049_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_049_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Person and Environment Object"
  },
  "target": {
    "target_id": "lower_left_flower_arrangement_and_russian_representative",
    "target_description": "the flower arrangement in the lower-left corner and the Russian representative",
    "source_state": "The flower arrangement remains in the lower-left corner, separated from the Russian representative's clasped hands.",
    "desired_change": "The flower arrangement is repositioned beside the Russian representative's clasped hands."
  },
  "timing": {
    "edit_point_sec": 30.0,
    "effect_start_sec": 30.0,
    "effect_end_sec": 30.0,
    "evaluation_window_sec": [
      29.0,
      33.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "close-up of the Russian representative with the flower arrangement visible in the lower-left corner"
  },
  "instruction": "At 30.0 seconds, reposition the flower arrangement from the lower-left corner beside the Russian representative's clasped hands.",
  "expected_result": {
    "description": "The flower arrangement appears beside the Russian representative's clasped hands.",
    "target_phrase": "flower arrangement beside clasped hands"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_049_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "At 30 seconds, the flower arrangement is clearly visible in the lower-left corner while the Russian representative's clasped hands remain visible near the lower center."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_049_E1",
    "must_preserve_e1_result": true,
    "description": "This edit repositions the flower arrangement on B independently of E1's burgundy-red tie; both edit results must coexist in C."
  }
}
```

## human_050

### human_050_E1

```json
{
  "video_id": "human_050",
  "edit_id": "human_050_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_050.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "shoe_red_orange_laces",
    "target_description": "the shoe's red-orange laces",
    "source_state": "The displayed shoe has red-orange laces.",
    "desired_change": "The shoe laces become bright blue."
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
  "instruction": "Starting at 14.0 seconds, change the shoe's red-orange laces to bright blue over the next two seconds.",
  "expected_result": {
    "description": "The shoe laces become bright blue.",
    "target_phrase": "bright-blue shoe laces"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_050_E2A

```json
{
  "video_id": "human_050",
  "edit_id": "human_050_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_050.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "Motion Modification",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "displayed_shoe",
    "target_description": "the displayed shoe",
    "source_state": "The man rotates the shoe to show different surfaces.",
    "desired_change": "The shoe rotates until its sole faces the camera."
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
  "instruction": "Starting at 29.0 seconds, make the displayed shoe rotate until its sole faces the camera.",
  "expected_result": {
    "description": "The shoe rotates until its sole faces the camera.",
    "target_phrase": "shoe sole facing the camera"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_050_E2B

```json
{
  "video_id": "human_050",
  "edit_id": "human_050_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_050_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_blue_polo_shirt",
    "target_description": "the man's blue polo shirt",
    "source_state": "The man wears a blue polo shirt while displaying the shoe.",
    "desired_change": "The blue polo shirt is replaced with a gray outdoor jacket."
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
  "instruction": "At 29.0 seconds, replace the man's blue polo shirt with a gray outdoor jacket.",
  "expected_result": {
    "description": "The blue polo shirt is replaced with a gray outdoor jacket.",
    "target_phrase": "gray outdoor jacket"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_050_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_050_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man's blue polo shirt on B independently of E1's change to the shoe's red-orange laces; both edit results must coexist in C."
  }
}
```

## human_054

### human_054_E1

```json
{
  "video_id": "human_054",
  "edit_id": "human_054_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "soldier",
    "target_description": "the soldier",
    "source_state": "The soldier speaks with a composed expression.",
    "desired_change": "The soldier smiles broadly while speaking."
  },
  "timing": {
    "edit_point_sec": 10.0,
    "effect_start_sec": 10.0,
    "effect_end_sec": 13.0,
    "evaluation_window_sec": [
      9.0,
      15.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 10.0 seconds, make the soldier smile broadly while speaking.",
  "expected_result": {
    "description": "The soldier smiles broadly while speaking.",
    "target_phrase": "soldier smiling broadly"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      9.0,
      15.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_054_E2A

```json
{
  "video_id": "human_054",
  "edit_id": "human_054_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "soldier_chair_and_rectangular_studio_light",
    "target_description": "the soldier's chair and the rectangular studio light",
    "source_state": "The chair is offset from the rectangular studio light.",
    "desired_change": "The chair is centered directly beneath the studio light."
  },
  "timing": {
    "edit_point_sec": 24.0,
    "effect_start_sec": 24.0,
    "effect_end_sec": 25.0,
    "evaluation_window_sec": [
      23.0,
      27.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.0 seconds, reposition the soldier's chair directly beneath the rectangular studio light.",
  "expected_result": {
    "description": "The chair is centered directly beneath the studio light.",
    "target_phrase": "chair beneath studio light"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.0,
      27.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_054_E2B

```json
{
  "video_id": "human_054",
  "edit_id": "human_054_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_054_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "camouflage_service_cap",
    "target_description": "a camouflage service cap",
    "source_state": "No service cap is visible on the soldier's lap.",
    "desired_change": "A camouflage service cap appears on the soldier's lap."
  },
  "timing": {
    "edit_point_sec": 24.0,
    "effect_start_sec": 24.0,
    "effect_end_sec": 25.0,
    "evaluation_window_sec": [
      23.0,
      27.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.0 seconds, add a camouflage service cap to the soldier's lap.",
  "expected_result": {
    "description": "A camouflage service cap appears on the soldier's lap.",
    "target_phrase": "service cap on the soldier's lap"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_054_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.0,
      27.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_054_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a camouflage service cap on B independently of E1's change to the soldier; both edit results must coexist in C."
  }
}
```

## human_056

### human_056_E1

```json
{
  "video_id": "human_056",
  "edit_id": "human_056_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "boy",
    "target_description": "the boy",
    "source_state": "The boy looks between the food and the camera.",
    "desired_change": "The boy smiles toward the camera."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      11.0,
      17.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 13.0 seconds, make the boy smile toward the camera.",
  "expected_result": {
    "description": "The boy smiles toward the camera.",
    "target_phrase": "boy smiling at the camera"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.0,
      17.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_056_E2A

```json
{
  "video_id": "human_056",
  "edit_id": "human_056_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "food_bag_on_boy_lap",
    "target_description": "the food bag on the boy's lap",
    "source_state": "A food bag rests on the boy's lap.",
    "desired_change": "The food bag is replaced with a blue lunchbox."
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
  "instruction": "At 29.0 seconds, replace the food bag on the boy's lap with a blue lunchbox.",
  "expected_result": {
    "description": "The food bag is replaced with a blue lunchbox.",
    "target_phrase": "blue lunchbox on the boy's lap"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_056_E2B

```json
{
  "video_id": "human_056",
  "edit_id": "human_056_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_056_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Onset/Early Termination",
    "operation": "Early Termination",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "boy_snack_eating_process",
    "target_description": "the boy's snack-eating process",
    "source_state": "The boy continues eating the snack beyond the selected interval.",
    "desired_change": "The boy stops eating the snack at video time 34.0 seconds instead of continuing beyond that point."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "early semantic termination"
  },
  "instruction": "Starting at 28.0 seconds, end the boy's snack-eating process at video time 34.0 seconds instead of letting it continue.",
  "expected_result": {
    "description": "The boy stops eating the snack at video time 34.0 seconds.",
    "target_phrase": "snack eating terminates at 34 seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of human_056_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_056_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the boy's snack-eating process on B independently of E1's change to the boy; both edit results must coexist in C."
  }
}
```

## human_057

### human_057_E1

```json
{
  "video_id": "human_057",
  "edit_id": "human_057_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_057.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker maintains a serious lecture expression.",
    "desired_change": "The speaker frowns deeply while addressing the camera."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 14.0 seconds, make the speaker frown deeply while addressing the camera.",
  "expected_result": {
    "description": "The speaker frowns deeply while addressing the camera.",
    "target_phrase": "deep lecture frown"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_057_E2A

```json
{
  "video_id": "human_057",
  "edit_id": "human_057_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_057.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker is centered within the red program frame.",
    "desired_change": "The speaker is positioned slightly left within the red program frame."
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
  "instruction": "At 29.0 seconds, reposition the speaker slightly left within the red program frame.",
  "expected_result": {
    "description": "The speaker is positioned slightly left within the red program frame.",
    "target_phrase": "speaker positioned slightly left"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_057_E2B

```json
{
  "video_id": "human_057",
  "edit_id": "human_057_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_057_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Person-local Style",
    "operation": "Ink-illustration Rendering",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker has a realistic photographic appearance.",
    "desired_change": "The speaker is rendered as a detailed ink illustration."
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
  "instruction": "Starting at 29.0 seconds, render the speaker as a detailed ink illustration over the next two seconds.",
  "expected_result": {
    "description": "The speaker is rendered as a detailed ink illustration.",
    "target_phrase": "ink-illustration speaker"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_057_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_057_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the speaker on B independently of E1's change to the speaker; both edit results must coexist in C."
  }
}
```

## human_060

### human_060_E1

```json
{
  "video_id": "human_060",
  "edit_id": "human_060_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_060.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman's face is centered in the tight frame.",
    "desired_change": "The woman's face is positioned slightly to the right of center."
  },
  "timing": {
    "edit_point_sec": 17,
    "effect_start_sec": 17,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      16,
      20
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 17.0 seconds, reposition the woman's face slightly to the right of center.",
  "expected_result": {
    "description": "The woman's face is positioned slightly to the right of center.",
    "target_phrase": "face right of center"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      16,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_060_E2A

```json
{
  "video_id": "human_060",
  "edit_id": "human_060_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_060.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_three_earrings",
    "target_description": "the woman's three earrings",
    "source_state": "The woman wears three earrings.",
    "desired_change": "The three earrings are removed from her ear."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      31.0,
      35.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32.0 seconds, remove the three earrings from the woman's ear.",
  "expected_result": {
    "description": "The three earrings are removed from her ear.",
    "target_phrase": "three earrings removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_060_E2B

```json
{
  "video_id": "human_060",
  "edit_id": "human_060_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_060_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Reverse",
    "operation": "Temporary Pause",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "facial_cleansing_process",
    "target_description": "the facial-cleansing process",
    "source_state": "The woman continuously cleans different areas of her face.",
    "desired_change": "The facial-cleansing process pauses for three seconds before resuming."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      31.0,
      37.0
    ],
    "temporal_behavior": "paused semantic process"
  },
  "instruction": "Starting at 32.0 seconds, pause the facial-cleansing process for three seconds before resuming it.",
  "expected_result": {
    "description": "The facial-cleansing process pauses for three seconds before resuming.",
    "target_phrase": "facial cleansing paused for three seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of human_060_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_060_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the facial-cleansing process on B independently of E1's change to the woman; both edit results must coexist in C."
  }
}
```

## human_061

### human_061_E1

```json
{
  "video_id": "human_061",
  "edit_id": "human_061_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_061.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "trainer_red_sports_top",
    "target_description": "the trainer's red sports top",
    "source_state": "The trainer wears a red sports top.",
    "desired_change": "The trainer's sports top becomes turquoise."
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
  "instruction": "Starting at 14.0 seconds, change the trainer's red sports top to turquoise over the next two seconds.",
  "expected_result": {
    "description": "The trainer's sports top becomes turquoise.",
    "target_phrase": "turquoise sports top"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_061_E2A

```json
{
  "video_id": "human_061",
  "edit_id": "human_061_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_061.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "trainer",
    "target_description": "the trainer",
    "source_state": "The trainer performs forward walking lunges.",
    "desired_change": "The trainer performs one controlled reverse lunge."
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
  "instruction": "Starting at 29.0 seconds, make the trainer perform one controlled reverse lunge.",
  "expected_result": {
    "description": "The trainer performs one controlled reverse lunge.",
    "target_phrase": "one controlled reverse lunge"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_061_E2B

```json
{
  "video_id": "human_061",
  "edit_id": "human_061_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_061_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "trainer",
    "target_description": "the trainer",
    "source_state": "The trainer demonstrates lunges near the center of the training area.",
    "desired_change": "The trainer is positioned on the left side of the training area."
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
  "instruction": "At 29.0 seconds, reposition the trainer on the left side of the training area.",
  "expected_result": {
    "description": "The trainer is positioned on the left side of the training area.",
    "target_phrase": "trainer on the left side"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_061_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_061_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the trainer on B independently of E1's change to the trainer's red sports top; both edit results must coexist in C."
  }
}
```

## human_062

### human_062_E1

```json
{
  "video_id": "human_062",
  "edit_id": "human_062_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Material and Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "square_wooden_board",
    "target_description": "the square wooden board",
    "source_state": "A natural-wood square board sits on the workbench.",
    "desired_change": "The square board becomes matte black composite material."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      12.5,
      15.5
    ],
    "temporal_behavior": "gradual persistent change",
    "source_stage_at_edit": "late board-facing segment before the shot change"
  },
  "instruction": "Starting at 13.5 seconds, change the visible board surface to a pale green finish over the next two seconds.",
  "expected_result": {
    "description": "The square board becomes matte black composite material.",
    "target_phrase": "matte-black square board"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12.5,
      15.5
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The board remains visible until the shot change near 15.5 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_062_E2A

```json
{
  "video_id": "human_062",
  "edit_id": "human_062_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "square_board",
    "target_description": "the square board",
    "source_state": "The square board rests flat on the workbench.",
    "desired_change": "The square board lifts and remains held at a steep, clearly visible angle."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, lift the square board from the workbench and hold it at a steep visible angle for two seconds.",
  "expected_result": {
    "description": "The square board is lifted and held at a steep visible angle.",
    "target_phrase": "square board held at a steep angle"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_062_E2B

```json
{
  "video_id": "human_062",
  "edit_id": "human_062_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_062_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "blue_bucket",
    "target_description": "the blue bucket",
    "source_state": "A blue bucket stands near the workbench.",
    "desired_change": "The blue bucket is replaced with a red metal bucket."
  },
  "timing": {
    "edit_point_sec": 28.5,
    "effect_start_sec": 28.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      27.5,
      31.5
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "later presenter segment after the shot change"
  },
  "instruction": "Starting at 28.5 seconds, make the presenter point toward the lower-left part of the board for two seconds.",
  "expected_result": {
    "description": "The blue bucket is replaced with a red metal bucket.",
    "target_phrase": "red metal bucket"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_062_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.5,
      31.5
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The presenter and board are both visible during the later segment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_062_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the blue bucket on B independently of E1's change to the square wooden board; both edit results must coexist in C."
  }
}
```

## human_063

### human_063_E1

```json
{
  "video_id": "human_063",
  "edit_id": "human_063_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_063.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_yellow_striped_hat",
    "target_description": "the man's yellow striped hat",
    "source_state": "The man wears a yellow striped knit hat.",
    "desired_change": "The hat becomes solid orange."
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
  "instruction": "Starting at 14.0 seconds, change the man's yellow striped hat to solid orange over the next two seconds.",
  "expected_result": {
    "description": "The hat becomes solid orange.",
    "target_phrase": "solid-orange knit hat"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_063_E2A

```json
{
  "video_id": "human_063",
  "edit_id": "human_063_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_063.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man looks downward and toward both sides while speaking.",
    "desired_change": "The man looks at the camera and nods three times."
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
  "instruction": "Starting at 29.0 seconds, make the man look at the camera and nod three times.",
  "expected_result": {
    "description": "The man looks at the camera and nods three times.",
    "target_phrase": "looks at camera and nods three times"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_063_E2B

```json
{
  "video_id": "human_063",
  "edit_id": "human_063_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_063_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The man is shown from an external frontal view.",
    "desired_change": "The surrounding scene is shown from the man's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the man's first-person perspective over three seconds.",
  "expected_result": {
    "description": "The surrounding scene is shown from the man's first-person viewpoint.",
    "target_phrase": "man's first-person scene view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_063_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_063_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the man's yellow striped hat; both edit results must coexist in C."
  }
}
```

## human_064

### human_064_E1

```json
{
  "video_id": "human_064",
  "edit_id": "human_064_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_short_beard",
    "target_description": "the man's short beard",
    "source_state": "The man has a short beard.",
    "desired_change": "His beard becomes a pointed goatee."
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
  "instruction": "Starting at 14.0 seconds, change the man's short beard to a pointed goatee over the next two seconds.",
  "expected_result": {
    "description": "His beard becomes a pointed goatee.",
    "target_phrase": "pointed goatee"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_064_E2A

```json
{
  "video_id": "human_064",
  "edit_id": "human_064_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits facing forward during the interview.",
    "desired_change": "The man rotates his torso left and crosses both forearms over his chest."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the man rotate his torso left and cross both forearms over his chest.",
  "expected_result": {
    "description": "The man rotates his torso left and crosses both forearms over his chest.",
    "target_phrase": "left-turned crossed-arm posture"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_064_E2B

```json
{
  "video_id": "human_064",
  "edit_id": "human_064_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_064_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Halftone Texture",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The retail interview has a clean photographic texture.",
    "desired_change": "The full frame uses a fine halftone print texture."
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
  "instruction": "Starting at 29.0 seconds, apply a fine halftone print texture to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a fine halftone print texture.",
    "target_phrase": "fine halftone print texture"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_064_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_064_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man's short beard; both edit results must coexist in C."
  }
}
```

## human_067

### human_067_E1

```json
{
  "video_id": "human_067",
  "edit_id": "human_067_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_067.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Color-temperature Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "kitchen_lighting",
    "target_description": "the kitchen lighting",
    "source_state": "The kitchen has neutral indoor lighting.",
    "desired_change": "The kitchen lighting becomes warm golden light."
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
  "instruction": "Starting at 14.0 seconds, change the kitchen lighting from neutral light to warm golden light over the next two seconds.",
  "expected_result": {
    "description": "The kitchen lighting becomes warm golden light.",
    "target_phrase": "warm golden kitchen lighting"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_067_E2A

```json
{
  "video_id": "human_067",
  "edit_id": "human_067_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_067.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a composed expression.",
    "desired_change": "The man smiles warmly toward the camera."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the man smile warmly toward the camera.",
  "expected_result": {
    "description": "The man smiles warmly toward the camera.",
    "target_phrase": "warm camera-facing smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_067_E2B

```json
{
  "video_id": "human_067",
  "edit_id": "human_067_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_067_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The kitchen is shown from an external view facing the man.",
    "desired_change": "The kitchen is shown from the man's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the man's first-person perspective over the next two seconds.",
  "expected_result": {
    "description": "The kitchen is shown from the man's first-person viewpoint.",
    "target_phrase": "man's first-person kitchen view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_067_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_067_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the kitchen lighting; both edit results must coexist in C."
  }
}
```

## human_068

### human_068_E1

```json
{
  "video_id": "human_068",
  "edit_id": "human_068_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Color-temperature Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "bar_lighting",
    "target_description": "the bar lighting",
    "source_state": "The bar has neutral indoor lighting.",
    "desired_change": "The bar lighting becomes rich amber light."
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
  "instruction": "Starting at 14.0 seconds, change the bar lighting from neutral light to rich amber light over the next two seconds.",
  "expected_result": {
    "description": "The bar lighting becomes rich amber light.",
    "target_phrase": "rich amber bar lighting"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_068_E2A

```json
{
  "video_id": "human_068",
  "edit_id": "human_068_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "bartender",
    "target_description": "the bartender",
    "source_state": "The bartender handles cups and ingredients behind the bar.",
    "desired_change": "The bartender lifts the red cup and swirls it twice."
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
  "instruction": "Starting at 29.0 seconds, make the bartender lift the red cup and swirl it twice.",
  "expected_result": {
    "description": "The bartender lifts the red cup and swirls it twice.",
    "target_phrase": "red cup swirled twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_068_E2B

```json
{
  "video_id": "human_068",
  "edit_id": "human_068_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_068_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Acceleration",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "remaining_cocktail_preparation_process",
    "target_description": "the remaining cocktail-preparation process",
    "source_state": "The bartender completes several remaining garnish and presentation steps.",
    "desired_change": "The remaining cocktail-preparation process progresses twice as fast."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 39.0,
    "evaluation_window_sec": [
      28.0,
      41.0
    ],
    "temporal_behavior": "accelerated semantic process"
  },
  "instruction": "Starting at 29.0 seconds, make the remaining cocktail-preparation process progress twice as fast.",
  "expected_result": {
    "description": "The remaining cocktail-preparation process progresses twice as fast.",
    "target_phrase": "cocktail preparation progressing twice as fast"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of human_068_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      41.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_068_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the remaining cocktail-preparation process on B independently of E1's change to the bar lighting; both edit results must coexist in C."
  }
}
```

## human_071

### human_071_E1

```json
{
  "video_id": "human_071",
  "edit_id": "human_071_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Color-temperature Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "studio_lighting",
    "target_description": "the studio lighting",
    "source_state": "The studio has warm neutral lighting.",
    "desired_change": "The studio lighting becomes cool blue light."
  },
  "timing": {
    "edit_point_sec": 18,
    "effect_start_sec": 18,
    "effect_end_sec": 20,
    "evaluation_window_sec": [
      17,
      22
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 18.0 seconds, change the studio lighting from warm neutral light to cool blue light over the next two seconds.",
  "expected_result": {
    "description": "The studio lighting becomes cool blue light.",
    "target_phrase": "cool blue studio lighting"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      17,
      22
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 18.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_071_E2A

```json
{
  "video_id": "human_071",
  "edit_id": "human_071_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "guest_and_host",
    "target_description": "the guest and host",
    "source_state": "The guest and host converse from the sofa and desk.",
    "desired_change": "The guest and host exchange one high-five across the desk."
  },
  "timing": {
    "edit_point_sec": 33.0,
    "effect_start_sec": 33.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      32.0,
      37.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 33.0 seconds, make the guest and host exchange one high-five across the desk.",
  "expected_result": {
    "description": "The guest and host exchange one high-five across the desk.",
    "target_phrase": "guest and host high-five"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_071_E2B

```json
{
  "video_id": "human_071",
  "edit_id": "human_071_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_071_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The guest and host are shown from an external studio view.",
    "desired_change": "The host is shown from the guest's first-person viewpoint."
  },
  "timing": {
    "edit_point_sec": 33.0,
    "effect_start_sec": 33.0,
    "effect_end_sec": 36.0,
    "evaluation_window_sec": [
      32.0,
      38.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 33.0 seconds, change the view to the guest's first-person perspective toward the host over three seconds.",
  "expected_result": {
    "description": "The host is shown from the guest's first-person viewpoint.",
    "target_phrase": "guest's first-person host view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_071_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32.0,
      38.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_071_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the studio lighting; both edit results must coexist in C."
  }
}
```

## human_074

### human_074_E1

```json
{
  "video_id": "human_074",
  "edit_id": "human_074_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman sits in a relaxed posture at the table.",
    "desired_change": "The woman straightens her back and leans toward the table."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      13.5,
      15.7
    ],
    "temporal_behavior": "bounded action",
    "source_stage_at_edit": "last close presenter view before the overhead table cut"
  },
  "instruction": "At 14.5 seconds, reposition the woman's face slightly toward frame-left within the close view.",
  "expected_result": {
    "description": "The woman straightens her back and leans toward the table.",
    "target_phrase": "upright forward-leaning posture"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.5,
      15.7
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The woman's face remains visible until the overhead table cut near 15.7 seconds."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_074_E2A

```json
{
  "video_id": "human_074",
  "edit_id": "human_074_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "crystal",
    "target_description": "the crystal",
    "source_state": "The crystal rests among several tabletop ritual objects.",
    "desired_change": "The crystal is positioned midway between the two nearest candles."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      31.0,
      35.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32.0 seconds, reposition the crystal midway between the two nearest candles.",
  "expected_result": {
    "description": "The crystal is positioned midway between the two nearest candles.",
    "target_phrase": "crystal between two candles"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_074_E2B

```json
{
  "video_id": "human_074",
  "edit_id": "human_074_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_074_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "nearest_table_candle",
    "target_description": "the nearest table candle",
    "source_state": "Several candles are arranged on the table.",
    "desired_change": "The nearest candle is removed from the table."
  },
  "timing": {
    "edit_point_sec": 29.5,
    "effect_start_sec": 29.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      29.3,
      34.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "second overhead table segment with the candle visible"
  },
  "instruction": "At 29.5 seconds, move the candle closer to the nearest plate in the overhead table view.",
  "expected_result": {
    "description": "The nearest candle is removed from the table.",
    "target_phrase": "nearest table candle removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_074_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.3,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The second overhead table view begins around 29.3 seconds with the candle and plate visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_074_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the nearest table candle on B independently of E1's change to the woman; both edit results must coexist in C."
  }
}
```

## human_077

### human_077_E1

```json
{
  "video_id": "human_077",
  "edit_id": "human_077_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_077.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_women",
    "target_description": "the two women",
    "source_state": "The two women hold and eat separate pizza slices.",
    "desired_change": "The two women raise their pizza slices together in a toast."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 14.0 seconds, make the two women raise their pizza slices together in a toast.",
  "expected_result": {
    "description": "The two women raise their pizza slices together in a toast.",
    "target_phrase": "pizza-slice toast"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_077_E2A

```json
{
  "video_id": "human_077",
  "edit_id": "human_077_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_077.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_women",
    "target_description": "the two women",
    "source_state": "The two women sit apart at the dining table.",
    "desired_change": "The two women sit closer together."
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
  "instruction": "At 29.0 seconds, reposition the two women at the dining table closer together.",
  "expected_result": {
    "description": "The two women sit closer together.",
    "target_phrase": "two women sitting closer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_077_E2B

```json
{
  "video_id": "human_077",
  "edit_id": "human_077_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_077_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Watercolor Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The dining footage has a realistic photographic appearance.",
    "desired_change": "The full frame is rendered as a hand-painted watercolor scene."
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into a hand-painted watercolor scene over the next two seconds.",
  "expected_result": {
    "description": "The full frame is rendered as a hand-painted watercolor scene.",
    "target_phrase": "watercolor dining scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_077_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_077_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the two women; both edit results must coexist in C."
  }
}
```

## human_078

### human_078_E1

```json
{
  "video_id": "human_078",
  "edit_id": "human_078_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_078.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a neutral outdoor expression.",
    "desired_change": "The man squints briefly and smiles toward the camera."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "bounded expression"
  },
  "instruction": "Starting at 14.0 seconds, make the man squint briefly and smile toward the camera.",
  "expected_result": {
    "description": "The man squints briefly and smiles toward the camera.",
    "target_phrase": "brief squint and smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_078_E2A

```json
{
  "video_id": "human_078",
  "edit_id": "human_078_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_078.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands in the sunlit roadside area.",
    "desired_change": "The man is removed from the roadside."
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
  "instruction": "At 29.0 seconds, remove the man from the sunlit roadside area.",
  "expected_result": {
    "description": "The man is removed from the roadside.",
    "target_phrase": "man removed from roadside"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_078_E2B

```json
{
  "video_id": "human_078",
  "edit_id": "human_078_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_078_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "High-contrast Tone",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The roadside footage has a conventional photographic contrast range.",
    "desired_change": "The full frame uses a crisp high-contrast tone."
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
  "instruction": "Starting at 29.0 seconds, apply a crisp high-contrast tone to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a crisp high-contrast tone.",
    "target_phrase": "crisp high-contrast tone"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_078_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_078_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_082

### human_082_E1

```json
{
  "video_id": "human_082",
  "edit_id": "human_082_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_082.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "warning_striped_vehicle",
    "target_description": "the warning-striped vehicle",
    "source_state": "A warning-striped vehicle is parked behind the officers.",
    "desired_change": "The vehicle's main body becomes matte white."
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
  "instruction": "Starting at 14.0 seconds, change the warning-striped vehicle's main body to matte white over the next two seconds.",
  "expected_result": {
    "description": "The vehicle's main body becomes matte white.",
    "target_phrase": "matte-white vehicle body"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_082_E2A

```json
{
  "video_id": "human_082",
  "edit_id": "human_082_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_082.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "three_officers_behind_speaker",
    "target_description": "the three officers behind the speaker",
    "source_state": "The officers behind the speaker stand with small posture changes.",
    "desired_change": "The three officers raise a salute together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 29.0 seconds, make the three officers behind the speaker raise a salute together.",
  "expected_result": {
    "description": "The three officers raise a salute together.",
    "target_phrase": "three officers saluting together"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_082_E2B

```json
{
  "video_id": "human_082",
  "edit_id": "human_082_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_082_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Addition",
    "scope": "Background Person"
  },
  "target": {
    "target_id": "additional_uniformed_officer",
    "target_description": "an additional uniformed officer",
    "source_state": "There is open space at the rear left of the group.",
    "desired_change": "An additional uniformed officer appears at the rear left of the group."
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
  "instruction": "At 29.0 seconds, add another uniformed officer at the rear left of the group.",
  "expected_result": {
    "description": "An additional uniformed officer appears at the rear left of the group.",
    "target_phrase": "additional officer at rear left"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_082_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_082_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes an additional uniformed officer on B independently of E1's change to the warning-striped vehicle; both edit results must coexist in C."
  }
}
```

## human_083

### human_083_E1

```json
{
  "video_id": "human_083",
  "edit_id": "human_083_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_light_beard",
    "target_description": "the man's light beard",
    "source_state": "The man has a light-colored beard.",
    "desired_change": "His beard becomes a dark pointed goatee."
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
  "instruction": "Starting at 14.0 seconds, change the man's light beard to a dark pointed goatee over the next two seconds.",
  "expected_result": {
    "description": "His beard becomes a dark pointed goatee.",
    "target_phrase": "dark pointed goatee"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_083_E2A

```json
{
  "video_id": "human_083",
  "edit_id": "human_083_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "walking_man",
    "target_description": "the walking man",
    "source_state": "The man walks forward through the narrow street.",
    "desired_change": "The man stops walking for three seconds."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "temporary motion stop"
  },
  "instruction": "Starting at 29.0 seconds, make the walking man stop for three seconds.",
  "expected_result": {
    "description": "The man stops walking for three seconds.",
    "target_phrase": "walking stopped for three seconds"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_083_E2B

```json
{
  "video_id": "human_083",
  "edit_id": "human_083_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_083_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Backward Tracking",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The handheld camera moves with irregular walking motion in front of the man.",
    "desired_change": "The camera tracks backward smoothly in front of the man."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, make the camera track backward smoothly in front of the man for five seconds.",
  "expected_result": {
    "description": "The camera tracks backward smoothly in front of the man.",
    "target_phrase": "smooth backward tracking"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_083_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_083_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the man's light beard; both edit results must coexist in C."
  }
}
```

## human_084

### human_084_E1

```json
{
  "video_id": "human_084",
  "edit_id": "human_084_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Color-temperature Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "snowy_woodland_lighting",
    "target_description": "the snowy woodland lighting",
    "source_state": "The snowy woodland has cool diffuse light.",
    "desired_change": "The woodland lighting becomes warm late-afternoon light."
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
  "instruction": "Starting at 14.0 seconds, change the cool woodland lighting to warm late-afternoon light over the next two seconds.",
  "expected_result": {
    "description": "The woodland lighting becomes warm late-afternoon light.",
    "target_phrase": "warm late-afternoon woodland light"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_084_E2A

```json
{
  "video_id": "human_084",
  "edit_id": "human_084_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "interviewed_man",
    "target_description": "the interviewed man",
    "source_state": "The man speaks with a composed expression.",
    "desired_change": "The man smiles broadly while speaking."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the interviewed man smile broadly while speaking.",
  "expected_result": {
    "description": "The man smiles broadly while speaking.",
    "target_phrase": "man smiling broadly"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_084_E2B

```json
{
  "video_id": "human_084",
  "edit_id": "human_084_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_084_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Watercolor Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "snowy_forest_background",
    "target_description": "the snowy forest background",
    "source_state": "The snowy forest has a realistic photographic appearance.",
    "desired_change": "The snowy forest is rendered as a watercolor painting."
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
  "instruction": "Starting at 29.0 seconds, render the snowy forest background in a watercolor style over the next two seconds.",
  "expected_result": {
    "description": "The snowy forest is rendered as a watercolor painting.",
    "target_phrase": "watercolor snowy forest"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_084_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_084_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the snowy forest background on B independently of E1's change to the snowy woodland lighting; both edit results must coexist in C."
  }
}
```

## human_085

### human_085_E1

```json
{
  "video_id": "human_085",
  "edit_id": "human_085_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Pattern Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "host_patterned_shirt",
    "target_description": "the host's patterned shirt",
    "source_state": "The host wears a light patterned short-sleeve shirt.",
    "desired_change": "The host's shirt becomes solid pale blue."
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
  "instruction": "Starting at 14.0 seconds, change the host's patterned shirt to solid pale blue over the next two seconds.",
  "expected_result": {
    "description": "The host's shirt becomes solid pale blue.",
    "target_phrase": "solid pale-blue shirt"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_085_E2A

```json
{
  "video_id": "human_085",
  "edit_id": "human_085_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_men",
    "target_description": "the two men",
    "source_state": "The two men sit on stools and exchange conversational gestures.",
    "desired_change": "The two men point toward the small table together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 29.0 seconds, make the two men point toward the small table together.",
  "expected_result": {
    "description": "The two men point toward the small table together.",
    "target_phrase": "two men pointing at the table"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_085_E2B

```json
{
  "video_id": "human_085",
  "edit_id": "human_085_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_085_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_men",
    "target_description": "the two men",
    "source_state": "The two men sit apart with the small table between them.",
    "desired_change": "The two men sit closer to each other while remaining on opposite sides of the table."
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
  "instruction": "At 29.0 seconds, reposition the two men closer together on opposite sides of the table.",
  "expected_result": {
    "description": "The two men sit closer to each other while remaining on opposite sides of the table.",
    "target_phrase": "two men sitting closer"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_085_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_085_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the two men on B independently of E1's change to the host's patterned shirt; both edit results must coexist in C."
  }
}
```

## human_086

### human_086_E1

```json
{
  "video_id": "human_086",
  "edit_id": "human_086_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_086.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Color-temperature Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "classroom_lighting",
    "target_description": "the classroom lighting",
    "source_state": "The classroom has neutral lighting.",
    "desired_change": "The classroom lighting becomes warm daylight."
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
  "instruction": "Starting at 14.0 seconds, change the classroom lighting from neutral light to warm daylight over the next two seconds.",
  "expected_result": {
    "description": "The classroom lighting becomes warm daylight.",
    "target_phrase": "warm classroom daylight"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_086_E2A

```json
{
  "video_id": "human_086",
  "edit_id": "human_086_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_086.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "teacher",
    "target_description": "the teacher",
    "source_state": "The teacher stands before the large blackboard.",
    "desired_change": "The teacher walks steadily toward the left cube drawing for four seconds."
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
  "instruction": "Starting at 29.0 seconds, make the teacher walk steadily toward the left cube drawing for four seconds.",
  "expected_result": {
    "description": "The teacher walks steadily toward the left cube drawing for four seconds.",
    "target_phrase": "steady walk toward left cube"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_086_E2B

```json
{
  "video_id": "human_086",
  "edit_id": "human_086_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_086_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "wooden_chalk_tray",
    "target_description": "the wooden chalk tray",
    "source_state": "A light wooden chalk tray runs beneath the blackboard.",
    "desired_change": "The wooden chalk tray is replaced with a silver metal tray."
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
  "instruction": "At 29.0 seconds, replace the wooden chalk tray beneath the blackboard with a silver metal tray.",
  "expected_result": {
    "description": "The wooden chalk tray is replaced with a silver metal tray.",
    "target_phrase": "silver metal chalk tray"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_086_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_086_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the wooden chalk tray on B independently of E1's change to the classroom lighting; both edit results must coexist in C."
  }
}
```

## human_090

### human_090_E1

```json
{
  "video_id": "human_090",
  "edit_id": "human_090_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Visible Hands"
  },
  "target": {
    "target_id": "hand_knife_and_chopped_onion",
    "target_description": "the hand using the knife beside the chopped onion",
    "source_state": "The visible hand uses the knife beside the pile of chopped onion.",
    "desired_change": "The visible hand pokes the chopped onion pile twice with the tip of the knife."
  },
  "timing": {
    "edit_point_sec": 17.0,
    "effect_start_sec": 17.0,
    "effect_end_sec": 19.0,
    "evaluation_window_sec": [
      16.0,
      20.0
    ],
    "temporal_behavior": "continuous action",
    "source_stage_at_edit": "onion-handling stage with the chopped onion pile and knife tip clearly visible"
  },
  "instruction": "Starting at 17.0 seconds, make the visible hand poke the chopped onion pile twice with the tip of the knife.",
  "expected_result": {
    "description": "The visible hand pokes the chopped onion pile twice with the knife tip.",
    "target_phrase": "knife tip poking chopped onion twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      16.0,
      20.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "At 17 seconds, the chopped onion pile, knife tip, and operating hand are all clearly visible in the continuous overhead shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_090_E2A

```json
{
  "video_id": "human_090",
  "edit_id": "human_090_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Reverse",
    "operation": "Short Reverse",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "tomato_dicing_process",
    "target_description": "the tomato-dicing process",
    "source_state": "The tomato is progressively diced into smaller pieces.",
    "desired_change": "The dicing process reverses by one completed cutting step."
  },
  "timing": {
    "edit_point_sec": 34.0,
    "effect_start_sec": 34.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      33.0,
      39.0
    ],
    "temporal_behavior": "short semantic reverse"
  },
  "instruction": "Starting at 34.0 seconds, reverse the tomato-dicing process by one completed cutting step over three seconds.",
  "expected_result": {
    "description": "The dicing process reverses by one completed cutting step.",
    "target_phrase": "one-step reversal of tomato dicing"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_090_E2B

```json
{
  "video_id": "human_090",
  "edit_id": "human_090_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_090_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Material Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "wooden_cutting_board",
    "target_description": "the wooden cutting board",
    "source_state": "The cutting board has a natural wooden surface.",
    "desired_change": "The cutting board becomes polished white marble."
  },
  "timing": {
    "edit_point_sec": 32.0,
    "effect_start_sec": 32.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      31.0,
      35.0
    ],
    "temporal_behavior": "gradual persistent change",
    "source_stage_at_edit": "late onion-transfer stage with the wooden cutting board clearly visible"
  },
  "instruction": "Starting at 32.0 seconds, change the wooden cutting board to polished white marble over the next two seconds.",
  "expected_result": {
    "description": "The cutting board becomes polished white marble.",
    "target_phrase": "polished white-marble cutting board"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of human_090_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "At 32 seconds, the wooden cutting board remains clearly visible throughout the continuous overhead food-preparation shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_090_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the wooden cutting board on B independently of E1's two knife-tip pokes into the chopped onion pile; both results must coexist in C."
  }
}
```

## human_095

### human_095_E1

```json
{
  "video_id": "human_095",
  "edit_id": "human_095_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "seated_couple",
    "target_description": "the seated couple",
    "source_state": "The couple talks while holding separate prompt boards.",
    "desired_change": "The couple exchanges one high-five above the prompt boards."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.0 seconds, make the seated couple exchange one high-five above the prompt boards.",
  "expected_result": {
    "description": "The couple exchanges one high-five above the prompt boards.",
    "target_phrase": "couple high-five"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_095_E2A

```json
{
  "video_id": "human_095",
  "edit_id": "human_095_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "seated_couple",
    "target_description": "the seated couple",
    "source_state": "The man and woman sit close together on the sofa.",
    "desired_change": "The man and woman sit farther apart on the sofa."
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
  "instruction": "At 29.0 seconds, reposition the man and woman farther apart on the sofa.",
  "expected_result": {
    "description": "The man and woman sit farther apart on the sofa.",
    "target_phrase": "couple sitting farther apart"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_095_E2B

```json
{
  "video_id": "human_095",
  "edit_id": "human_095_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_095_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The couple is shown in a wide sofa view.",
    "desired_change": "The framing becomes a tighter upper-body two-shot."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom in to a tighter upper-body view of the couple over three seconds.",
  "expected_result": {
    "description": "The framing becomes a tighter upper-body two-shot.",
    "target_phrase": "tighter upper-body two-shot"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_095_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_095_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the seated couple; both edit results must coexist in C."
  }
}
```

## human_096

### human_096_E1

```json
{
  "video_id": "human_096",
  "edit_id": "human_096_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "guitarist_picking_hand",
    "target_description": "the guitarist's picking hand",
    "source_state": "The guitarist uses continuous fingerpicking patterns.",
    "desired_change": "The guitarist performs a rapid tremolo pattern."
  },
  "timing": {
    "edit_point_sec": 18,
    "effect_start_sec": 18,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      17,
      24
    ],
    "temporal_behavior": "continuous action"
  },
  "instruction": "Starting at 18.0 seconds, make the guitarist perform a rapid tremolo picking pattern.",
  "expected_result": {
    "description": "The guitarist performs a rapid tremolo pattern.",
    "target_phrase": "rapid tremolo picking"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      17,
      24
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 18.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_096_E2A

```json
{
  "video_id": "human_096",
  "edit_id": "human_096_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "guitarist",
    "target_description": "the guitarist",
    "source_state": "The guitarist sits near the beach while playing.",
    "desired_change": "The guitarist is removed from the beach scene."
  },
  "timing": {
    "edit_point_sec": 33.0,
    "effect_start_sec": 33.0,
    "effect_end_sec": 34.0,
    "evaluation_window_sec": [
      32.0,
      36.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 33.0 seconds, remove the seated guitarist from the beach scene.",
  "expected_result": {
    "description": "The guitarist is removed from the beach scene.",
    "target_phrase": "guitarist removed from beach"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_096_E2B

```json
{
  "video_id": "human_096",
  "edit_id": "human_096_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_096_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Left Orbit",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The returning seaside shot holds a fixed frontal view.",
    "desired_change": "The camera moves in a slow leftward arc around the guitarist."
  },
  "timing": {
    "edit_point_sec": 33.0,
    "effect_start_sec": 33.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      32.0,
      39.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 33.0 seconds, move the camera in a slow leftward arc around the guitarist for four seconds.",
  "expected_result": {
    "description": "The camera moves in a slow leftward arc around the guitarist.",
    "target_phrase": "leftward camera arc"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_096_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_096_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the guitarist's picking hand; both edit results must coexist in C."
  }
}
```

## human_098

### human_098_E1

```json
{
  "video_id": "human_098",
  "edit_id": "human_098_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_098.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a serious explanatory expression.",
    "desired_change": "The man briefly opens his eyes wide in surprise."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "bounded expression"
  },
  "instruction": "Starting at 14.0 seconds, make the man open his eyes wide in surprise.",
  "expected_result": {
    "description": "The man briefly opens his eyes wide in surprise.",
    "target_phrase": "wide-eyed surprised expression"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_098_E2A

```json
{
  "video_id": "human_098",
  "edit_id": "human_098_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_098.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits on the gray sofa.",
    "desired_change": "The man is removed from the sofa."
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
  "instruction": "At 29.0 seconds, remove the man seated on the gray sofa.",
  "expected_result": {
    "description": "The man is removed from the sofa.",
    "target_phrase": "man removed from sofa"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_098_E2B

```json
{
  "video_id": "human_098",
  "edit_id": "human_098_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_098_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Person-local Style",
    "operation": "Oil-painting Rendering",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man has a realistic photographic appearance.",
    "desired_change": "The man is rendered as an oil-painted portrait."
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
  "instruction": "Starting at 29.0 seconds, render the man as an oil-painted portrait over the next two seconds.",
  "expected_result": {
    "description": "The man is rendered as an oil-painted portrait.",
    "target_phrase": "oil-painted portrait"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_098_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_098_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_099

### human_099_E1

```json
{
  "video_id": "human_099",
  "edit_id": "human_099_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits on the right side of the garage view.",
    "desired_change": "The man sits slightly farther left, revealing more of the engine bay."
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
  "instruction": "At 14.0 seconds, reposition the man slightly farther left to reveal more of the engine bay.",
  "expected_result": {
    "description": "The man sits slightly farther left, revealing more of the engine bay.",
    "target_phrase": "man positioned farther left"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_099_E2A

```json
{
  "video_id": "human_099",
  "edit_id": "human_099_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Removal",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits beside the open engine bay.",
    "desired_change": "The man is removed from the garage scene."
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
  "instruction": "At 29.0 seconds, remove the man seated beside the open engine bay.",
  "expected_result": {
    "description": "The man is removed from the garage scene.",
    "target_phrase": "man removed from garage"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_099_E2B

```json
{
  "video_id": "human_099",
  "edit_id": "human_099_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_099_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The man and open engine bay share a wide garage view.",
    "desired_change": "The framing moves closer to the open engine bay."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom in on the open engine bay over three seconds.",
  "expected_result": {
    "description": "The framing moves closer to the open engine bay.",
    "target_phrase": "close-up of engine bay"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_099_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_099_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_104

### human_104_E1

```json
{
  "video_id": "human_104",
  "edit_id": "human_104_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_104.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Body/Skin Appearance",
    "operation": "Body-shape Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "nearest_athlete_build",
    "target_description": "the nearest athlete's build",
    "source_state": "The nearest athlete has a lean athletic build.",
    "desired_change": "His build becomes broader and more muscular."
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
  "instruction": "Starting at 14.0 seconds, make the nearest athlete's build broader and more muscular over the next two seconds.",
  "expected_result": {
    "description": "His build becomes broader and more muscular.",
    "target_phrase": "broader athletic build"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_104_E2A

```json
{
  "video_id": "human_104",
  "edit_id": "human_104_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_104.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "nearest_athlete",
    "target_description": "the nearest athlete",
    "source_state": "The nearest athlete stands among the team.",
    "desired_change": "The nearest athlete moves continuously along the award line toward the nearest teammate for four seconds."
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
  "instruction": "Starting at 29.0 seconds, make the nearest athlete move continuously along the award line toward the nearest teammate for four seconds.",
  "expected_result": {
    "description": "The nearest athlete moves continuously along the award line toward the nearest teammate for four seconds.",
    "target_phrase": "continuous movement along award line"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_104_E2B

```json
{
  "video_id": "human_104",
  "edit_id": "human_104_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_104_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "Vintage-film Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The celebration has a modern digital sports-video appearance.",
    "desired_change": "The full frame is rendered as vintage color sports film."
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into vintage color sports film over the next two seconds.",
  "expected_result": {
    "description": "The full frame is rendered as vintage color sports film.",
    "target_phrase": "vintage sports film"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_104_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_104_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the nearest athlete's build; both edit results must coexist in C."
  }
}
```

## human_105

### human_105_E1

```json
{
  "video_id": "human_105",
  "edit_id": "human_105_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_105.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_white_hair",
    "target_description": "the man's white hair",
    "source_state": "The man has white hair around the sides of his head.",
    "desired_change": "The man's hair becomes light blond."
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
  "instruction": "Starting at 14.0 seconds, change the man's white hair to light blond over the next two seconds.",
  "expected_result": {
    "description": "The man's hair becomes light blond.",
    "target_phrase": "light-blond hair"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_105_E2A

```json
{
  "video_id": "human_105",
  "edit_id": "human_105_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_105.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a serious commentary expression.",
    "desired_change": "The man smiles warmly while speaking."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the man smile warmly while speaking.",
  "expected_result": {
    "description": "The man smiles warmly while speaking.",
    "target_phrase": "warm smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_105_E2B

```json
{
  "video_id": "human_105",
  "edit_id": "human_105_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_105_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man is centered in front of the bookcase.",
    "desired_change": "The man is positioned slightly left, revealing more of the bookcase."
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
  "instruction": "At 29.0 seconds, reposition the man slightly left to reveal more of the bookcase.",
  "expected_result": {
    "description": "The man is positioned slightly left, revealing more of the bookcase.",
    "target_phrase": "man positioned left"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_105_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_105_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man on B independently of E1's change to the man's white hair; both edit results must coexist in C."
  }
}
```

## human_106

### human_106_E1

```json
{
  "video_id": "human_106",
  "edit_id": "human_106_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_106.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Material Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "metal_cooking_pot",
    "target_description": "the metal cooking pot",
    "source_state": "The cooking pot has a bare metallic finish.",
    "desired_change": "The cooking pot becomes blue enameled cookware."
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
  "instruction": "Starting at 14.0 seconds, change the metal cooking pot to blue enameled cookware over the next two seconds.",
  "expected_result": {
    "description": "The cooking pot becomes blue enameled cookware.",
    "target_phrase": "blue enameled pot"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_106_E2A

```json
{
  "video_id": "human_106",
  "edit_id": "human_106_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_106.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Visible Hands"
  },
  "target": {
    "target_id": "stirring_hand",
    "target_description": "the stirring hand",
    "source_state": "The hand stirs the pot with repeated circular movements.",
    "desired_change": "The hand stirs the mixture in a figure-eight pattern."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "continuous action"
  },
  "instruction": "Starting at 29.0 seconds, make the stirring hand use a figure-eight pattern.",
  "expected_result": {
    "description": "The hand stirs the mixture in a figure-eight pattern.",
    "target_phrase": "figure-eight stirring"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_106_E2B

```json
{
  "video_id": "human_106",
  "edit_id": "human_106_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_106_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "cook",
    "target_description": "the cook",
    "source_state": "A person in black clothing works at the granite counter.",
    "desired_change": "The cook is replaced with a chef wearing a blue apron."
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
  "instruction": "At 29.0 seconds, replace the cook at the granite counter with a chef wearing a blue apron.",
  "expected_result": {
    "description": "The cook is replaced with a chef wearing a blue apron.",
    "target_phrase": "chef in blue apron"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_106_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_106_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the cook on B independently of E1's change to the metal cooking pot; both edit results must coexist in C."
  }
}
```

## human_107

### human_107_E1

```json
{
  "video_id": "human_107",
  "edit_id": "human_107_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_107.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "artwork_red_band",
    "target_description": "the artwork's red band",
    "source_state": "The artwork contains a red color band.",
    "desired_change": "The red band becomes cobalt blue."
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
  "instruction": "Starting at 14.0 seconds, change the artwork's red band to cobalt blue over the next two seconds.",
  "expected_result": {
    "description": "The red band becomes cobalt blue.",
    "target_phrase": "cobalt-blue band"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_107_E2A

```json
{
  "video_id": "human_107",
  "edit_id": "human_107_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_107.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Visible Hands"
  },
  "target": {
    "target_id": "painting_hand",
    "target_description": "the painting hand",
    "source_state": "The hand uses short brush strokes on small colored areas.",
    "desired_change": "The hand applies a repeating stippling motion with the brush."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 33.0,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "continuous action"
  },
  "instruction": "Starting at 29.0 seconds, make the painting hand apply a repeating stippling motion.",
  "expected_result": {
    "description": "The hand applies a repeating stippling motion with the brush.",
    "target_phrase": "repeating stippling motion"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_107_E2B

```json
{
  "video_id": "human_107",
  "edit_id": "human_107_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_107_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Brush Tracking",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed view of the artwork.",
    "desired_change": "The camera tracks the brush tip across the active color region."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, track the brush tip across the active color region for three seconds.",
  "expected_result": {
    "description": "The camera tracks the brush tip across the active color region.",
    "target_phrase": "camera tracking brush tip"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_107_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_107_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the artwork's red band; both edit results must coexist in C."
  }
}
```

## human_108

### human_108_E1

```json
{
  "video_id": "human_108",
  "edit_id": "human_108_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_108.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle and Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_long_black_hair",
    "target_description": "the woman's long black hair",
    "source_state": "The woman has long black hair.",
    "desired_change": "Her hair becomes short copper curls."
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
  "instruction": "Starting at 14.0 seconds, change the woman's long black hair to short copper curls over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes short copper curls.",
    "target_phrase": "short copper curls"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_108_E2A

```json
{
  "video_id": "human_108",
  "edit_id": "human_108_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_108.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "seated_couple",
    "target_description": "the seated couple",
    "source_state": "The couple alternates speaking and smiling at each other.",
    "desired_change": "The couple exchanges one high-five."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the seated couple exchange one high-five.",
  "expected_result": {
    "description": "The couple exchanges one high-five.",
    "target_phrase": "couple high-five"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_108_E2B

```json
{
  "video_id": "human_108",
  "edit_id": "human_108_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_108_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Person-local Style",
    "operation": "Colored-pencil Rendering",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "seated_couple",
    "target_description": "the seated couple",
    "source_state": "The couple has a realistic photographic appearance.",
    "desired_change": "The couple is rendered as a colored-pencil portrait."
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
  "instruction": "Starting at 29.0 seconds, render the seated couple as a colored-pencil portrait over the next two seconds.",
  "expected_result": {
    "description": "The couple is rendered as a colored-pencil portrait.",
    "target_phrase": "colored-pencil couple portrait"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_108_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_108_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the seated couple on B independently of E1's change to the woman's long black hair; both edit results must coexist in C."
  }
}
```

## human_110

### human_110_E1

```json
{
  "video_id": "human_110",
  "edit_id": "human_110_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_110.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle and Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "singer_long_black_hair",
    "target_description": "the singer's long black hair",
    "source_state": "The singer has long black hair.",
    "desired_change": "Her hair becomes a platinum-blond bob."
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
  "instruction": "Starting at 14.0 seconds, change the singer's long black hair to a platinum-blond bob over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes a platinum-blond bob.",
    "target_phrase": "platinum-blond bob"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_110_E2A

```json
{
  "video_id": "human_110",
  "edit_id": "human_110_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_110.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "singer_and_guitarist",
    "target_description": "the singer and guitarist",
    "source_state": "The singer and guitarist perform with separate head movements.",
    "desired_change": "The singer and guitarist look at each other and nod together."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 29.0 seconds, make the singer and guitarist look at each other and nod together.",
  "expected_result": {
    "description": "The singer and guitarist look at each other and nod together.",
    "target_phrase": "performers nodding together"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_110_E2B

```json
{
  "video_id": "human_110",
  "edit_id": "human_110_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_110_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "guitarist_necklace",
    "target_description": "the guitarist's necklace",
    "source_state": "The guitarist wears a necklace.",
    "desired_change": "The necklace is replaced with a red neck scarf."
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
  "instruction": "At 29.0 seconds, replace the guitarist's necklace with a red neck scarf.",
  "expected_result": {
    "description": "The necklace is replaced with a red neck scarf.",
    "target_phrase": "red neck scarf"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_110_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_110_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the guitarist's necklace on B independently of E1's change to the singer's long black hair; both edit results must coexist in C."
  }
}
```

## human_112

### human_112_E1

```json
{
  "video_id": "human_112",
  "edit_id": "human_112_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_112.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_black_curly_hair",
    "target_description": "the woman's black curly hair",
    "source_state": "The woman has dense black curly hair.",
    "desired_change": "The woman's hair becomes chestnut brown."
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
  "instruction": "Starting at 14.0 seconds, change the woman's black curly hair to chestnut brown over the next two seconds.",
  "expected_result": {
    "description": "The woman's hair becomes chestnut brown.",
    "target_phrase": "chestnut-brown curly hair"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_112_E2A

```json
{
  "video_id": "human_112",
  "edit_id": "human_112_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_112.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman sits facing forward.",
    "desired_change": "The woman turns her shoulders to the right and leans forward."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the woman turn her shoulders to the right and lean forward.",
  "expected_result": {
    "description": "The woman turns her shoulders to the right and leans forward.",
    "target_phrase": "right-turned forward lean"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_112_E2B

```json
{
  "video_id": "human_112",
  "edit_id": "human_112_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_112_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Object-local Style",
    "operation": "Paper-cut Rendering",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "white_wardrobe",
    "target_description": "the white wardrobe",
    "source_state": "The white wardrobe has a realistic painted appearance.",
    "desired_change": "The white wardrobe is rendered as layered paper-cut artwork."
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
  "instruction": "Starting at 29.0 seconds, render the white wardrobe as layered paper-cut artwork over the next two seconds.",
  "expected_result": {
    "description": "The white wardrobe is rendered as layered paper-cut artwork.",
    "target_phrase": "paper-cut white wardrobe"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_112_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_112_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the white wardrobe on B independently of E1's change to the woman's black curly hair; both edit results must coexist in C."
  }
}
```

## human_115

### human_115_E1

```json
{
  "video_id": "human_115",
  "edit_id": "human_115_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_115.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "comedian",
    "target_description": "the comedian",
    "source_state": "The comedian makes small movements within the stage area.",
    "desired_change": "The comedian walks continuously toward the left side of the stage for four seconds."
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
  "instruction": "Starting at 14.0 seconds, make the comedian walk continuously toward the left side of the stage for four seconds.",
  "expected_result": {
    "description": "The comedian walks continuously toward the left side of the stage for four seconds.",
    "target_phrase": "continuous leftward stage walk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_115_E2A

```json
{
  "video_id": "human_115",
  "edit_id": "human_115_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_115.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "comedian_and_circular_stage_fan",
    "target_description": "the comedian and the large circular stage fan",
    "source_state": "The comedian stands near the large circular fan in the dark stage background.",
    "desired_change": "The comedian stands directly to the left of the circular fan, leaving the full fan visible."
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
  "instruction": "At 29.0 seconds, reposition the comedian directly to the left of the large circular stage fan, leaving the full fan visible.",
  "expected_result": {
    "description": "The comedian stands directly left of the circular fan and leaves the full fan visible.",
    "target_phrase": "comedian left of circular stage fan"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_115_E2B

```json
{
  "video_id": "human_115",
  "edit_id": "human_115_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_115_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The comedian is shown in a medium-long stage view.",
    "desired_change": "The framing becomes an upper-body view of the comedian."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom in to an upper-body view of the comedian over three seconds.",
  "expected_result": {
    "description": "The framing becomes an upper-body view of the comedian.",
    "target_phrase": "upper-body comedian view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_115_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_115_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the comedian; both edit results must coexist in C."
  }
}
```

## human_119

### human_119_E1

```json
{
  "video_id": "human_119",
  "edit_id": "human_119_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_119.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "microphone",
    "target_description": "the microphone",
    "source_state": "The standing microphone is in front of the singer.",
    "desired_change": "The microphone is positioned closer to the singer's mouth."
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
  "instruction": "At 14.0 seconds, reposition the microphone closer to the singer's mouth.",
  "expected_result": {
    "description": "The microphone is positioned closer to the singer's mouth.",
    "target_phrase": "microphone closer to singer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_119_E2A

```json
{
  "video_id": "human_119",
  "edit_id": "human_119_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_119.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "male_singer",
    "target_description": "the male singer",
    "source_state": "A male singer performs with the wooden guitar.",
    "desired_change": "The male singer is replaced with a female singer."
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
  "instruction": "At 29.0 seconds, replace the male singer holding the wooden guitar with a female singer.",
  "expected_result": {
    "description": "The male singer is replaced with a female singer.",
    "target_phrase": "female singer with guitar"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_119_E2B

```json
{
  "video_id": "human_119",
  "edit_id": "human_119_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_119_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Right Orbit",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed frontal view of the singer.",
    "desired_change": "The camera moves in a slow rightward orbit around the singer."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28.0,
      35.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, move the camera in a slow rightward orbit around the singer for four seconds.",
  "expected_result": {
    "description": "The camera moves in a slow rightward orbit around the singer.",
    "target_phrase": "slow rightward orbit"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_119_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_119_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the microphone; both edit results must coexist in C."
  }
}
```

## human_120

### human_120_E1

```json
{
  "video_id": "human_120",
  "edit_id": "human_120_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_120.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a neutral expression.",
    "desired_change": "The man opens his eyes wide in surprise."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      13,
      18
    ],
    "temporal_behavior": "bounded expression"
  },
  "instruction": "Starting at 14.0 seconds, make the neutrally speaking man open his eyes wide in surprise.",
  "expected_result": {
    "description": "The man opens his eyes wide in surprise.",
    "target_phrase": "wide-eyed surprise"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_120_E2A

```json
{
  "video_id": "human_120",
  "edit_id": "human_120_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_120.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man is centered against the cabinet doors.",
    "desired_change": "The man is positioned slightly left of center."
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
  "instruction": "At 29.0 seconds, reposition the man slightly left of center.",
  "expected_result": {
    "description": "The man is positioned slightly left of center.",
    "target_phrase": "man left of center"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_120_E2B

```json
{
  "video_id": "human_120",
  "edit_id": "human_120_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_120_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "small_potted_plant",
    "target_description": "a small potted plant",
    "source_state": "No potted plant is visible beside the cabinet.",
    "desired_change": "A small potted plant appears beside the cabinet."
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
  "instruction": "At 29.0 seconds, add a small potted plant beside the cabinet.",
  "expected_result": {
    "description": "A small potted plant appears beside the cabinet.",
    "target_phrase": "small plant beside cabinet"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_120_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_120_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a small potted plant on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_121

### human_121_E1

```json
{
  "video_id": "human_121",
  "edit_id": "human_121_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_121.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Temporary Slowdown",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "sleeve_rolling_process",
    "target_description": "the ongoing sleeve-rolling process",
    "source_state": "The hands continue folding and tightening the camouflage sleeve at the original pace.",
    "desired_change": "The sleeve-rolling process proceeds at half speed from 14.0 to 20.0 seconds before returning to its original pace."
  },
  "timing": {
    "edit_point_sec": 14.0,
    "effect_start_sec": 14.0,
    "effect_end_sec": 20.0,
    "evaluation_window_sec": [
      13.0,
      22.0
    ],
    "temporal_behavior": "temporary slowdown",
    "source_stage_at_edit": "continuous cuff-folding and tightening stage"
  },
  "instruction": "Starting at 14.0 seconds, slow the sleeve-rolling process to half speed for six seconds.",
  "expected_result": {
    "description": "The hands continue the same sleeve-rolling steps at half speed from 14.0 to 20.0 seconds, then resume the original pace.",
    "target_phrase": "sleeve rolling at half speed"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.0,
      22.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The fixed overhead view continuously shows both hands folding and tightening the cuff throughout the selected interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_121_E2A

```json
{
  "video_id": "human_121",
  "edit_id": "human_121_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_121.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Pattern-color Change",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "camouflage_sleeve",
    "target_description": "the camouflage sleeve",
    "source_state": "The sleeve has a green-and-brown camouflage pattern.",
    "desired_change": "The camouflage pattern becomes gray and black."
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
  "instruction": "Starting at 29.0 seconds, change the sleeve's green-and-brown camouflage pattern to gray and black over the next two seconds.",
  "expected_result": {
    "description": "The camouflage pattern becomes gray and black.",
    "target_phrase": "gray-and-black camouflage"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_121_E2B

```json
{
  "video_id": "human_121",
  "edit_id": "human_121_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_121_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Visible Hands"
  },
  "target": {
    "target_id": "two_hands",
    "target_description": "the two hands",
    "source_state": "The hands press and tighten the rolled cuff.",
    "desired_change": "The hands flip the rolled cuff outward once."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the two hands flip the rolled cuff outward once.",
  "expected_result": {
    "description": "The hands flip the rolled cuff outward once.",
    "target_phrase": "cuff flipped outward once"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of human_121_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_121_E1",
    "must_preserve_e1_result": true,
    "description": "This edit makes the two hands flip the cuff outward on B after E1's temporary sleeve-rolling slowdown; both results must coexist in C."
  }
}
```

## human_124

### human_124_E1

```json
{
  "video_id": "human_124",
  "edit_id": "human_124_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_124.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_light_purple_tie",
    "target_description": "the man's light-purple tie",
    "source_state": "The man wears a light-purple tie.",
    "desired_change": "The tie becomes emerald green."
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
  "instruction": "Starting at 14.0 seconds, change the man's light-purple tie to emerald green over the next two seconds.",
  "expected_result": {
    "description": "The tie becomes emerald green.",
    "target_phrase": "emerald-green tie"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_124_E2A

```json
{
  "video_id": "human_124",
  "edit_id": "human_124_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_124.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a composed interview expression.",
    "desired_change": "The man smiles warmly while speaking."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the interviewed man smile warmly while he continues speaking.",
  "expected_result": {
    "description": "The man smiles warmly while speaking.",
    "target_phrase": "warm smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_124_E2B

```json
{
  "video_id": "human_124",
  "edit_id": "human_124_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_124_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1980s Public-service Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The public-service interview has a modern digital-video appearance.",
    "desired_change": "The full frame resembles a 1980s public-service television interview."
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into a 1980s public-service television interview over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1980s public-service television interview.",
    "target_phrase": "1980s public-service interview"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_124_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_124_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man's light-purple tie; both edit results must coexist in C."
  }
}
```

## human_125

### human_125_E1

```json
{
  "video_id": "human_125",
  "edit_id": "human_125_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_125.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "older_man_green_bow_tie",
    "target_description": "the older man's green bow tie",
    "source_state": "The older man wears a green bow tie.",
    "desired_change": "The bow tie becomes burgundy red."
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
  "instruction": "Starting at 14.0 seconds, change the older man's green bow tie to burgundy red over the next two seconds.",
  "expected_result": {
    "description": "The bow tie becomes burgundy red.",
    "target_phrase": "burgundy-red bow tie"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_125_E2A

```json
{
  "video_id": "human_125",
  "edit_id": "human_125_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_125.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "older_man",
    "target_description": "the older man",
    "source_state": "The older man looks toward the nearby interviewer.",
    "desired_change": "The older man looks over his left shoulder."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the older man look over his left shoulder.",
  "expected_result": {
    "description": "The older man looks over his left shoulder.",
    "target_phrase": "looks over left shoulder"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_125_E2B

```json
{
  "video_id": "human_125",
  "edit_id": "human_125_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_125_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "older_man_and_nearest_suited_attendee",
    "target_description": "the older man and the nearest suited attendee",
    "source_state": "The older man and nearest suited attendee stand apart in the event hall.",
    "desired_change": "The suited attendee stands directly to the older man's left."
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
  "instruction": "At 29.0 seconds, reposition the nearest suited attendee directly to the older man's left.",
  "expected_result": {
    "description": "The suited attendee stands directly to the older man's left.",
    "target_phrase": "attendee left of older man"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_125_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_125_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the older man and the nearest suited attendee on B independently of E1's change to the older man's green bow tie; both edit results must coexist in C."
  }
}
```

## human_126

### human_126_E1

```json
{
  "video_id": "human_126",
  "edit_id": "human_126_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_126.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_pink_headscarf",
    "target_description": "the woman's pink headscarf",
    "source_state": "The woman wears a pink headscarf.",
    "desired_change": "The headscarf becomes teal."
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
  "instruction": "Starting at 14.0 seconds, change the woman's pink headscarf to teal over the next two seconds.",
  "expected_result": {
    "description": "The headscarf becomes teal.",
    "target_phrase": "teal headscarf"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_126_E2A

```json
{
  "video_id": "human_126",
  "edit_id": "human_126_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_126.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman walks forward along the supermarket aisle.",
    "desired_change": "The woman walks continuously backward along the supermarket aisle for four seconds."
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
  "instruction": "Starting at 29.0 seconds, make the woman walk continuously backward along the supermarket aisle for four seconds.",
  "expected_result": {
    "description": "The woman walks continuously backward along the supermarket aisle for four seconds.",
    "target_phrase": "continuous backward aisle walk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_126_E2B

```json
{
  "video_id": "human_126",
  "edit_id": "human_126_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_126_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "reusable_shopping_basket",
    "target_description": "a reusable shopping basket",
    "source_state": "The woman carries no shopping basket.",
    "desired_change": "A reusable shopping basket appears in the woman's left hand."
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
  "instruction": "At 29.0 seconds, add a reusable shopping basket to the woman's left hand.",
  "expected_result": {
    "description": "A reusable shopping basket appears in the woman's left hand.",
    "target_phrase": "reusable shopping basket"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_126_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_126_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a reusable shopping basket on B independently of E1's change to the woman's pink headscarf; both edit results must coexist in C."
  }
}
```

## human_127

### human_127_E1

```json
{
  "video_id": "human_127",
  "edit_id": "human_127_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_127.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "older_man_facial_hair",
    "target_description": "the older man's facial hair",
    "source_state": "The older man has no prominent moustache.",
    "desired_change": "A neatly trimmed gray moustache appears on his face."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 12,
    "evaluation_window_sec": [
      9.0,
      14.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12.0 seconds, add a neatly trimmed gray moustache to the older man's face over the next two seconds.",
  "expected_result": {
    "description": "A neatly trimmed gray moustache appears on his face.",
    "target_phrase": "trimmed gray moustache"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      9.0,
      14.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_127_E2A

```json
{
  "video_id": "human_127",
  "edit_id": "human_127_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_127.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "interviewer_and_older_man",
    "target_description": "the interviewer and the older man",
    "source_state": "The interviewer stands beside the older man during the interview.",
    "desired_change": "The interviewer and the older man exchange one handshake."
  },
  "timing": {
    "edit_point_sec": 28.0,
    "effect_start_sec": 28.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      27.0,
      33.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 28.0 seconds, make the interviewer and the older man exchange one handshake.",
  "expected_result": {
    "description": "The interviewer and the older man exchange one handshake.",
    "target_phrase": "interview handshake"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_127_E2B

```json
{
  "video_id": "human_127",
  "edit_id": "human_127_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_127_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Widening Reposition",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The handheld camera mainly frames the older man.",
    "desired_change": "The camera moves to a wider position that includes both speakers."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      27.0,
      33.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 27.0 seconds, move the camera to a wider two-person view over three seconds.",
  "expected_result": {
    "description": "The camera moves to a wider position that includes both speakers.",
    "target_phrase": "wider two-person view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_127_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_127_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the older man's facial hair; both edit results must coexist in C."
  }
}
```

## human_130

### human_130_E1

```json
{
  "video_id": "human_130",
  "edit_id": "human_130_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_130.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_tied_up_hair",
    "target_description": "the woman's tied-up hair",
    "source_state": "The woman's hair is tied up.",
    "desired_change": "Her hair becomes loose shoulder-length waves."
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
  "instruction": "Starting at 14.0 seconds, change the woman's tied-up hair to loose shoulder-length waves over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes loose shoulder-length waves.",
    "target_phrase": "loose shoulder-length waves"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_130_E2A

```json
{
  "video_id": "human_130",
  "edit_id": "human_130_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_130.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_right_hand",
    "target_description": "the woman's right hand",
    "source_state": "The woman gestures with her empty right hand while speaking.",
    "desired_change": "The woman counts three points with three distinct finger gestures."
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
  "instruction": "Starting at 29.0 seconds, make the woman count three points with three distinct finger gestures using her right hand.",
  "expected_result": {
    "description": "The woman counts three points with three distinct right-hand finger gestures.",
    "target_phrase": "three distinct counting gestures"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_130_E2B

```json
{
  "video_id": "human_130",
  "edit_id": "human_130_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_130_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "small_tabletop_mirror",
    "target_description": "a small tabletop mirror",
    "source_state": "No small mirror is visible on the sofa arm.",
    "desired_change": "A small tabletop mirror appears on the sofa arm."
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
  "instruction": "At 29.0 seconds, add a small tabletop mirror to the sofa arm.",
  "expected_result": {
    "description": "A small tabletop mirror appears on the sofa arm.",
    "target_phrase": "small tabletop mirror"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_130_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_130_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a small tabletop mirror on B independently of E1's change to the woman's tied-up hair; both edit results must coexist in C."
  }
}
```

## human_134

### human_134_E1

```json
{
  "video_id": "human_134",
  "edit_id": "human_134_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_134.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man speaks with a composed interview expression.",
    "desired_change": "The man smiles broadly toward the interviewer."
  },
  "timing": {
    "edit_point_sec": 15,
    "effect_start_sec": 15,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      14,
      20
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 15.0 seconds, make the man smile broadly toward the interviewer.",
  "expected_result": {
    "description": "The man smiles broadly toward the interviewer.",
    "target_phrase": "broad interview smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      14,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 15.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_134_E2A

```json
{
  "video_id": "human_134",
  "edit_id": "human_134_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_134.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits near the center of the windowed composition.",
    "desired_change": "The man sits to the left of the large window."
  },
  "timing": {
    "edit_point_sec": 30.0,
    "effect_start_sec": 30.0,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      29.0,
      33.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30.0 seconds, reposition the man to the left of the large window.",
  "expected_result": {
    "description": "The man sits to the left of the large window.",
    "target_phrase": "man left of the window"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_134_E2B

```json
{
  "video_id": "human_134",
  "edit_id": "human_134_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_134_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "small_potted_plant",
    "target_description": "a small potted plant",
    "source_state": "No plant is visible on the window sill.",
    "desired_change": "A small potted plant appears on the window sill."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 31.0,
    "evaluation_window_sec": [
      29.0,
      33.0
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30.0 seconds, add a small potted plant to the window sill.",
  "expected_result": {
    "description": "A small potted plant appears on the window sill.",
    "target_phrase": "potted plant on window sill"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_134_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.0,
      33.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_134_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a small potted plant on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_136

### human_136_E1

```json
{
  "video_id": "human_136",
  "edit_id": "human_136_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_136.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "performer",
    "target_description": "the performer",
    "source_state": "The performer holds and demonstrates two wooden bars.",
    "desired_change": "The performer crosses the two wooden bars above the music stand."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      11.0,
      16.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 13.0 seconds, make the performer cross the two wooden bars above the music stand.",
  "expected_result": {
    "description": "The performer crosses the two wooden bars above the music stand.",
    "target_phrase": "wooden bars crossed"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.0,
      16.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_136_E2A

```json
{
  "video_id": "human_136",
  "edit_id": "human_136_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_136.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "male_performer",
    "target_description": "the male performer",
    "source_state": "A male performer stands behind the music stand.",
    "desired_change": "The male performer is replaced with a female percussionist."
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
  "instruction": "At 29.0 seconds, replace the male performer behind the music stand with a female percussionist.",
  "expected_result": {
    "description": "The male performer is replaced with a female percussionist.",
    "target_phrase": "female percussionist"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_136_E2B

```json
{
  "video_id": "human_136",
  "edit_id": "human_136_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_136_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The performer is shown from an audience-facing third-person view.",
    "desired_change": "The stage is shown from the performer's first-person viewpoint toward the audience."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 28.0 seconds, change the view to the performer's first-person perspective over the next two seconds.",
  "expected_result": {
    "description": "The stage is shown from the performer's first-person viewpoint toward the audience.",
    "target_phrase": "performer's first-person stage view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_136_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_136_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the performer; both edit results must coexist in C."
  }
}
```

## human_138

### human_138_E1

```json
{
  "video_id": "human_138",
  "edit_id": "human_138_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_138.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "left_boxing_demonstrator",
    "target_description": "the left boxing demonstrator",
    "source_state": "The left demonstrator faces the partner in a boxing stance.",
    "desired_change": "The left demonstrator maintains a continuous leftward defensive shuffle for three seconds."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 23,
    "evaluation_window_sec": [
      19,
      25
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 20.0 seconds, make the left boxing demonstrator maintain a continuous leftward defensive shuffle for three seconds.",
  "expected_result": {
    "description": "The left demonstrator maintains a continuous leftward defensive shuffle for three seconds.",
    "target_phrase": "continuous leftward defensive shuffle"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      25
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_138_E2A

```json
{
  "video_id": "human_138",
  "edit_id": "human_138_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_138.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Replacement",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "nearest_assisting_boxer",
    "target_description": "the nearest assisting boxer",
    "source_state": "A boxer assists the main demonstrator near the heavy bag.",
    "desired_change": "The assisting boxer is replaced with a kickboxer."
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
  "instruction": "At 35.0 seconds, replace the nearest assisting boxer with a kickboxer.",
  "expected_result": {
    "description": "The assisting boxer is replaced with a kickboxer.",
    "target_phrase": "kickboxer assistant"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      38.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_138_E2B

```json
{
  "video_id": "human_138",
  "edit_id": "human_138_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_138_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Comic-book Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The boxing tutorial has a realistic video appearance.",
    "desired_change": "The full frame is rendered in a bold comic-book style."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 35.0,
    "effect_end_sec": 37.0,
    "evaluation_window_sec": [
      34.0,
      39.0
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 35.0 seconds, transform the full frame into a bold comic-book style over the next two seconds.",
  "expected_result": {
    "description": "The full frame is rendered in a bold comic-book style.",
    "target_phrase": "comic-book boxing scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_138_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      39.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_138_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the left boxing demonstrator; both edit results must coexist in C."
  }
}
```

## human_139

### human_139_E1

```json
{
  "video_id": "human_139",
  "edit_id": "human_139_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_139.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands beside the illuminated pinball machine.",
    "desired_change": "The man stands directly behind the pinball machine."
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
  "instruction": "At 14.0 seconds, reposition the man directly behind the illuminated pinball machine.",
  "expected_result": {
    "description": "The man stands directly behind the pinball machine.",
    "target_phrase": "man behind pinball machine"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_139_E2A

```json
{
  "video_id": "human_139",
  "edit_id": "human_139_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_139.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "male_presenter",
    "target_description": "the male presenter",
    "source_state": "A male presenter stands beside the pinball machine.",
    "desired_change": "The male presenter is replaced with a female pinball player."
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
  "instruction": "At 29.0 seconds, replace the male presenter beside the pinball machine with a female pinball player.",
  "expected_result": {
    "description": "The male presenter is replaced with a female pinball player.",
    "target_phrase": "female pinball player"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_139_E2B

```json
{
  "video_id": "human_139",
  "edit_id": "human_139_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_139_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Dolly In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed view of the pinball machine.",
    "desired_change": "The camera moves smoothly closer to the pinball playfield."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, move the camera smoothly closer to the pinball playfield over three seconds.",
  "expected_result": {
    "description": "The camera moves smoothly closer to the pinball playfield.",
    "target_phrase": "smooth dolly toward pinball playfield"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_139_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_139_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_141

### human_141_E1

```json
{
  "video_id": "human_141",
  "edit_id": "human_141_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_141.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker_magenta_shirt",
    "target_description": "the speaker's magenta shirt",
    "source_state": "The speaker wears a magenta shirt beneath a blue tie.",
    "desired_change": "The speaker's shirt becomes deep green."
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
  "instruction": "Starting at 14.0 seconds, change the speaker's magenta shirt to deep green over the next two seconds.",
  "expected_result": {
    "description": "The speaker's shirt becomes deep green.",
    "target_phrase": "deep-green shirt"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_141_E2A

```json
{
  "video_id": "human_141",
  "edit_id": "human_141_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_141.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker faces the camera in front of the climate imagery.",
    "desired_change": "The speaker turns toward the inset climate footage and nods twice."
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
  "instruction": "Starting at 29.0 seconds, make the speaker turn toward the inset climate footage and nod twice.",
  "expected_result": {
    "description": "The speaker turns toward the inset climate footage and nods twice.",
    "target_phrase": "turns toward inset and nods twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_141_E2B

```json
{
  "video_id": "human_141",
  "edit_id": "human_141_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_141_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker occupies the center of the orange studio composition.",
    "desired_change": "The speaker is positioned on the left side of the frame beside the inset footage."
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
  "instruction": "At 29.0 seconds, reposition the speaker on the left side of the frame beside the inset footage.",
  "expected_result": {
    "description": "The speaker is positioned on the left side of the frame beside the inset footage.",
    "target_phrase": "speaker beside inset footage"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_141_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_141_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the speaker on B independently of E1's change to the speaker's magenta shirt; both edit results must coexist in C."
  }
}
```

## human_144

### human_144_E1

```json
{
  "video_id": "human_144",
  "edit_id": "human_144_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_144.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "green_novelty_coin_bank",
    "target_description": "the green novelty coin bank",
    "source_state": "The novelty coin bank has a green box body.",
    "desired_change": "The coin bank's box body becomes cobalt blue."
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
  "instruction": "Starting at 14.0 seconds, change the green coin-bank body to cobalt blue over the next two seconds.",
  "expected_result": {
    "description": "The coin bank's box body becomes cobalt blue.",
    "target_phrase": "cobalt-blue coin bank"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_144_E2A

```json
{
  "video_id": "human_144",
  "edit_id": "human_144_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_144.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "coin_bank_white_paw",
    "target_description": "the coin bank's white paw",
    "source_state": "The white paw extends briefly to collect a coin.",
    "desired_change": "The white paw extends and waves twice above the box."
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
  "instruction": "Starting at 29.0 seconds, make the coin bank's white paw extend and wave twice above the box.",
  "expected_result": {
    "description": "The white paw extends and waves twice above the box.",
    "target_phrase": "white paw waving twice"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_144_E2B

```json
{
  "video_id": "human_144",
  "edit_id": "human_144_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_144_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Clay-animation Rendering",
    "scope": "Background"
  },
  "target": {
    "target_id": "tabletop_background",
    "target_description": "the tabletop background",
    "source_state": "The tabletop background has a realistic indoor appearance.",
    "desired_change": "The tabletop background is rendered in a clay-animation style."
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
  "instruction": "Starting at 29.0 seconds, render the tabletop background in a clay-animation style over the next two seconds.",
  "expected_result": {
    "description": "The tabletop background is rendered in a clay-animation style.",
    "target_phrase": "clay-animation tabletop background"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_144_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_144_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tabletop background on B independently of E1's change to the green novelty coin bank; both edit results must coexist in C."
  }
}
```

## human_146

### human_146_E1

```json
{
  "video_id": "human_146",
  "edit_id": "human_146_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_146.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "right_panelist_gray_cap",
    "target_description": "the right panelist's gray cap",
    "source_state": "The right panelist wears a gray cap.",
    "desired_change": "The cap becomes navy blue."
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
  "instruction": "Starting at 14.0 seconds, change the right panelist's gray cap to navy blue over the next two seconds.",
  "expected_result": {
    "description": "The cap becomes navy blue.",
    "target_phrase": "navy-blue cap"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_146_E2A

```json
{
  "video_id": "human_146",
  "edit_id": "human_146_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_146.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "podium_speaker",
    "target_description": "the podium speaker",
    "source_state": "The podium speaker addresses the audience with a serious expression.",
    "desired_change": "The podium speaker smiles broadly while speaking."
  },
  "timing": {
    "edit_point_sec": 29.0,
    "effect_start_sec": 29.0,
    "effect_end_sec": 32.0,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 29.0 seconds, make the podium speaker smile broadly while speaking.",
  "expected_result": {
    "description": "The podium speaker smiles broadly while speaking.",
    "target_phrase": "broad podium smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_146_E2B

```json
{
  "video_id": "human_146",
  "edit_id": "human_146_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_146_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person",
    "operation": "Addition",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "second_stage_participant",
    "target_description": "a second stage participant",
    "source_state": "The podium speaker stands alone in the main stage footage.",
    "desired_change": "A second stage participant appears behind and to the right of the podium speaker."
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
  "instruction": "At 29.0 seconds, add a second stage participant behind and to the right of the podium speaker.",
  "expected_result": {
    "description": "A second stage participant appears behind and to the right of the podium speaker.",
    "target_phrase": "second stage participant"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_146_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_146_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a second stage participant on B independently of E1's change to the right panelist's gray cap; both edit results must coexist in C."
  }
}
```

## human_147

### human_147_E1

```json
{
  "video_id": "human_147",
  "edit_id": "human_147_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_147.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_beard",
    "target_description": "the man's beard",
    "source_state": "The man has a short full beard.",
    "desired_change": "His beard becomes a pointed goatee."
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
  "instruction": "Starting at 14.0 seconds, change the man's short full beard to a pointed goatee over the next two seconds.",
  "expected_result": {
    "description": "His beard becomes a pointed goatee.",
    "target_phrase": "pointed goatee"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_147_E2A

```json
{
  "video_id": "human_147",
  "edit_id": "human_147_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_147.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man faces forward near the office monitors.",
    "desired_change": "The man rotates his torso toward the monitors and leans closer."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 35.0,
    "effect_end_sec": 38.0,
    "evaluation_window_sec": [
      34.0,
      40.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 35.0 seconds, make the man rotate his torso toward the monitors and lean closer.",
  "expected_result": {
    "description": "The man rotates his torso toward the monitors and leans closer.",
    "target_phrase": "torso turned toward monitors"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      40.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_147_E2B

```json
{
  "video_id": "human_147",
  "edit_id": "human_147_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_147_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The man is shown in a medium office view.",
    "desired_change": "The framing widens to include both monitors and the man's hands."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom out to include both monitors and the man's hands over three seconds.",
  "expected_result": {
    "description": "The framing widens to include both monitors and the man's hands.",
    "target_phrase": "wide view of man and monitors"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_147_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_147_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the man's beard; both edit results must coexist in C."
  }
}
```

## human_152

### human_152_E1

```json
{
  "video_id": "human_152",
  "edit_id": "human_152_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_152.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_dark_beard",
    "target_description": "the man's dark beard",
    "source_state": "The man has a dark beard.",
    "desired_change": "The beard becomes auburn."
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
  "instruction": "Starting at 14.0 seconds, change the man's dark beard to auburn over the next two seconds.",
  "expected_result": {
    "description": "The beard becomes auburn.",
    "target_phrase": "auburn beard"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_152_E2A

```json
{
  "video_id": "human_152",
  "edit_id": "human_152_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_152.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits in a relaxed posture before the bookcase.",
    "desired_change": "The man straightens his torso and squares both shoulders."
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
  "instruction": "Starting at 29.0 seconds, make the man straighten his torso and square both shoulders.",
  "expected_result": {
    "description": "The man straightens his torso and squares both shoulders.",
    "target_phrase": "straight squared-shoulder posture"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_152_E2B

```json
{
  "video_id": "human_152",
  "edit_id": "human_152_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_152_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Paper Texture",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The indoor monologue has a clean digital photographic texture.",
    "desired_change": "The full frame uses a subtle fine-paper texture."
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
  "instruction": "Starting at 29.0 seconds, apply a subtle fine-paper texture to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a subtle fine-paper texture.",
    "target_phrase": "subtle fine-paper texture"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_152_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_152_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man's dark beard; both edit results must coexist in C."
  }
}
```

## human_153

### human_153_E1

```json
{
  "video_id": "human_153",
  "edit_id": "human_153_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_153.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "teacher",
    "target_description": "the teacher",
    "source_state": "The teacher stands close to the blackboard while drawing.",
    "desired_change": "The teacher walks steadily backward away from the blackboard for three seconds."
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
  "instruction": "Starting at 14.0 seconds, make the teacher walk steadily backward away from the blackboard for three seconds.",
  "expected_result": {
    "description": "The teacher walks steadily backward away from the blackboard for three seconds.",
    "target_phrase": "steady backward walk from blackboard"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_153_E2A

```json
{
  "video_id": "human_153",
  "edit_id": "human_153_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_153.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "teacher",
    "target_description": "the teacher",
    "source_state": "The teacher stands close to the center of the board diagram.",
    "desired_change": "The teacher stands to the left of the double-slit diagram."
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
  "instruction": "At 29.0 seconds, reposition the teacher to the left of the double-slit diagram.",
  "expected_result": {
    "description": "The teacher stands to the left of the double-slit diagram.",
    "target_phrase": "teacher left of diagram"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_153_E2B

```json
{
  "video_id": "human_153",
  "edit_id": "human_153_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_153_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "wooden_ruler",
    "target_description": "a wooden ruler",
    "source_state": "No ruler is visible on the chalk tray.",
    "desired_change": "A wooden ruler appears on the chalk tray."
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
  "instruction": "At 29.0 seconds, add a wooden ruler to the chalk tray.",
  "expected_result": {
    "description": "A wooden ruler appears on the chalk tray.",
    "target_phrase": "wooden ruler on chalk tray"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_153_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_153_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a wooden ruler on B independently of E1's change to the teacher; both edit results must coexist in C."
  }
}
```

## human_154

### human_154_E1

```json
{
  "video_id": "human_154",
  "edit_id": "human_154_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_154.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "speaker",
    "target_description": "the speaker",
    "source_state": "The speaker addresses the audience with a composed expression.",
    "desired_change": "The speaker smiles broadly toward the audience."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      13,
      19
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 14.0 seconds, make the speaker smile broadly toward the audience.",
  "expected_result": {
    "description": "The speaker smiles broadly toward the audience.",
    "target_phrase": "broad audience-facing smile"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_154_E2A

```json
{
  "video_id": "human_154",
  "edit_id": "human_154_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_154.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "two_microphones",
    "target_description": "the two microphones",
    "source_state": "The two microphones sit at unequal distances from the speaker.",
    "desired_change": "The microphones are positioned symmetrically on either side of the speaker."
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
  "instruction": "At 29.0 seconds, reposition the two microphones symmetrically on either side of the speaker.",
  "expected_result": {
    "description": "The microphones are positioned symmetrically on either side of the speaker.",
    "target_phrase": "symmetrical microphones"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_154_E2B

```json
{
  "video_id": "human_154",
  "edit_id": "human_154_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_154_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "flower_arrangement",
    "target_description": "the flower arrangement",
    "source_state": "A large yellow-and-white flower arrangement stands before the speaker.",
    "desired_change": "The flower arrangement is replaced with a green fern."
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
  "instruction": "At 29.0 seconds, replace the yellow-and-white flower arrangement with a green fern.",
  "expected_result": {
    "description": "The flower arrangement is replaced with a green fern.",
    "target_phrase": "green fern"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_154_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_154_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the flower arrangement on B independently of E1's change to the speaker; both edit results must coexist in C."
  }
}
```

## human_155

### human_155_E1

```json
{
  "video_id": "human_155",
  "edit_id": "human_155_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_155.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "walking_man",
    "target_description": "the walking man",
    "source_state": "The man walks along the rural road at a steady pace.",
    "desired_change": "The walking man accelerates into a sustained brisk walk along the road for four seconds."
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
  "instruction": "Starting at 14.0 seconds, make the walking man accelerate into a sustained brisk walk along the road for four seconds.",
  "expected_result": {
    "description": "The walking man accelerates into a sustained brisk walk along the road for four seconds.",
    "target_phrase": "sustained brisk road walk"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      20
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_155_E2A

```json
{
  "video_id": "human_155",
  "edit_id": "human_155_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_155.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "walking_man",
    "target_description": "the walking man",
    "source_state": "The man occupies the center of the road-facing selfie frame.",
    "desired_change": "The man is positioned on the right side of the road-facing frame."
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
  "instruction": "At 29.0 seconds, reposition the walking man on the right side of the road-facing frame.",
  "expected_result": {
    "description": "The man is positioned on the right side of the road-facing frame.",
    "target_phrase": "man on right side of road frame"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_155_E2B

```json
{
  "video_id": "human_155",
  "edit_id": "human_155_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_155_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Backward Tracking",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The handheld camera moves with the walking man at arm's length.",
    "desired_change": "The camera tracks smoothly backward ahead of the walking man."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, make the camera track smoothly backward ahead of the walking man for five seconds.",
  "expected_result": {
    "description": "The camera tracks smoothly backward ahead of the walking man.",
    "target_phrase": "smooth backward tracking shot"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_155_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_155_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the walking man; both edit results must coexist in C."
  }
}
```

## human_157

### human_157_E1

```json
{
  "video_id": "human_157",
  "edit_id": "human_157_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_157.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Multi-person/Group Motion",
    "operation": "New Motion",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_women",
    "target_description": "the two women",
    "source_state": "The two women sit beside each other at the kitchen table.",
    "desired_change": "The two women exchange one high-five above the table."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      13,
      19
    ],
    "temporal_behavior": "coordinated action"
  },
  "instruction": "Starting at 14.0 seconds, make the two women exchange one high-five above the table.",
  "expected_result": {
    "description": "The two women exchange one high-five above the table.",
    "target_phrase": "one high-five above table"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_157_E2A

```json
{
  "video_id": "human_157",
  "edit_id": "human_157_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_157.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_women",
    "target_description": "the two women",
    "source_state": "The two women sit with a visible gap between them.",
    "desired_change": "The two women sit closer together with their shoulders nearly touching."
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
  "instruction": "At 29.0 seconds, reposition the two women closer together with their shoulders nearly touching.",
  "expected_result": {
    "description": "The two women sit closer together with their shoulders nearly touching.",
    "target_phrase": "women seated closer together"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_157_E2B

```json
{
  "video_id": "human_157",
  "edit_id": "human_157_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_157_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Watercolor Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The two-person kitchen footage has a realistic photographic appearance.",
    "desired_change": "The full frame is rendered as a detailed watercolor painting."
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into a detailed watercolor painting over the next two seconds.",
  "expected_result": {
    "description": "The full frame is rendered as a detailed watercolor painting.",
    "target_phrase": "watercolor kitchen conversation"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_157_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_157_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the two women; both edit results must coexist in C."
  }
}
```

## human_159

### human_159_E1

```json
{
  "video_id": "human_159",
  "edit_id": "human_159_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_159.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "k_shaped_ornament_and_white_tabletop",
    "target_description": "the K-shaped ornament on the background shelf and the white tabletop behind the woman",
    "source_state": "The K-shaped ornament rests on the shelving unit at the right side of the background.",
    "desired_change": "The K-shaped ornament is repositioned onto the white tabletop behind the woman."
  },
  "timing": {
    "edit_point_sec": 20.0,
    "effect_start_sec": 20.0,
    "effect_end_sec": 21.0,
    "evaluation_window_sec": [
      19.0,
      24.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "continuous beauty-display view with the K-shaped ornament and white tabletop visible"
  },
  "instruction": "At 20.0 seconds, reposition the K-shaped ornament from the background shelf onto the white tabletop behind the woman.",
  "expected_result": {
    "description": "The K-shaped ornament rests on the white tabletop behind the woman.",
    "target_phrase": "K-shaped ornament on white tabletop"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.0,
      24.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "Around 20 seconds, the K-shaped ornament is visible on the right background shelf and the white tabletop remains visible behind the woman."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### human_159_E2A

```json
{
  "video_id": "human_159",
  "edit_id": "human_159_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_159.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "pink_hair_clip",
    "target_description": "a pink hair clip",
    "source_state": "No hair clip is visible in the woman's black hair.",
    "desired_change": "A pink hair clip appears above the woman's left ear."
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
  "instruction": "At 35.0 seconds, add a pink hair clip above the woman's left ear.",
  "expected_result": {
    "description": "A pink hair clip appears above the woman's left ear.",
    "target_phrase": "pink hair clip"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      38.0
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_159_E2B

```json
{
  "video_id": "human_159",
  "edit_id": "human_159_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_159_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The woman presents the gel containers in a medium close view.",
    "desired_change": "The framing moves closer to the two gel containers."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 35.0,
    "effect_end_sec": 38.0,
    "evaluation_window_sec": [
      34.0,
      40.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 35.0 seconds, zoom in on the two gel containers over three seconds.",
  "expected_result": {
    "description": "The framing moves closer to the two gel containers.",
    "target_phrase": "close-up of gel containers"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_159_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34.0,
      40.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_159_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes camera framing on B independently of E1's repositioning of the K-shaped ornament onto the white tabletop; both results must coexist in C."
  }
}
```

## human_164

### human_164_E1

```json
{
  "video_id": "human_164",
  "edit_id": "human_164_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_164.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_braided_hair",
    "target_description": "the woman's braided hair",
    "source_state": "The woman's hair is braided.",
    "desired_change": "Her hair becomes loose curls."
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
  "instruction": "Starting at 14.0 seconds, change the woman's braided hair to loose curls over the next two seconds.",
  "expected_result": {
    "description": "Her hair becomes loose curls.",
    "target_phrase": "loose curly hair"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_164_E2A

```json
{
  "video_id": "human_164",
  "edit_id": "human_164_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_164.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman gestures near her chest while standing in the garden.",
    "desired_change": "The woman stretches both arms upward above her head."
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
  "instruction": "Starting at 29.0 seconds, make the woman stretch both arms upward above her head.",
  "expected_result": {
    "description": "The woman stretches both arms upward above her head.",
    "target_phrase": "both arms stretched overhead"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_164_E2B

```json
{
  "video_id": "human_164",
  "edit_id": "human_164_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_164_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman stands centered in front of the trimmed hedge.",
    "desired_change": "The woman stands beside the stone path on the right."
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
  "instruction": "At 29.0 seconds, reposition the woman beside the stone path on the right.",
  "expected_result": {
    "description": "The woman stands beside the stone path on the right.",
    "target_phrase": "woman beside right stone path"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_164_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_164_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the woman on B independently of E1's change to the woman's braided hair; both edit results must coexist in C."
  }
}
```

## human_165

### human_165_E1

```json
{
  "video_id": "human_165",
  "edit_id": "human_165_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_165.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Facial Appearance",
    "operation": "Facial-hair Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "presenter_gray_white_beard",
    "target_description": "the presenter's gray-white beard",
    "source_state": "The presenter has a full gray-white beard.",
    "desired_change": "His beard becomes a short salt-and-pepper goatee."
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
  "instruction": "Starting at 20.0 seconds, change the presenter's full gray-white beard to a short salt-and-pepper goatee over the next two seconds.",
  "expected_result": {
    "description": "His beard becomes a short salt-and-pepper goatee.",
    "target_phrase": "short salt-and-pepper goatee"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_165_E2A

```json
{
  "video_id": "human_165",
  "edit_id": "human_165_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_165.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Person-related Object"
  },
  "target": {
    "target_id": "red_promotional_card",
    "target_description": "the red promotional card",
    "source_state": "The presenter holds the red promotional card toward the camera.",
    "desired_change": "The red promotional card rotates through one full turn in the presenter's hand."
  },
  "timing": {
    "edit_point_sec": 37.0,
    "effect_start_sec": 37.0,
    "effect_end_sec": 40.0,
    "evaluation_window_sec": [
      36.0,
      42.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 37.0 seconds, make the red promotional card rotate through one full turn in the presenter's hand.",
  "expected_result": {
    "description": "The red promotional card rotates through one full turn in the presenter's hand.",
    "target_phrase": "red card rotating one full turn"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      36.0,
      42.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_165_E2B

```json
{
  "video_id": "human_165",
  "edit_id": "human_165_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_165_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "presenter_and_woman_at_booth",
    "target_description": "the presenter and the woman standing at the exhibition booth",
    "source_state": "The woman stands on the left side of the presenter at the exhibition booth.",
    "desired_change": "The woman stands directly to the right of the presenter."
  },
  "timing": {
    "edit_point_sec": 27.0,
    "effect_start_sec": 27.0,
    "effect_end_sec": 28.0,
    "evaluation_window_sec": [
      26.0,
      30.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "continuous booth view with the presenter and woman visible together"
  },
  "instruction": "At 27.0 seconds, reposition the woman from the left side of the booth directly to the presenter's right.",
  "expected_result": {
    "description": "The woman stands directly to the right of the presenter at the exhibition booth.",
    "target_phrase": "woman standing to presenter's right"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_165_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.0,
      30.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "At 27 seconds, the woman and presenter are both clearly visible, with the woman standing on the left side of the booth."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_165_E1",
    "must_preserve_e1_result": true,
    "description": "This edit repositions the woman relative to the presenter on B while preserving E1's salt-and-pepper goatee on the presenter; both edit results must coexist in C."
  }
}
```

## human_166

### human_166_E1

```json
{
  "video_id": "human_166",
  "edit_id": "human_166_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_166.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_bright_blue_jacket",
    "target_description": "the man's bright-blue jacket",
    "source_state": "The man wears a bright-blue outdoor jacket.",
    "desired_change": "The jacket becomes brick red."
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
  "instruction": "Starting at 20.0 seconds, change the man's bright-blue jacket to brick red over the next two seconds.",
  "expected_result": {
    "description": "The jacket becomes brick red.",
    "target_phrase": "brick-red outdoor jacket"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      24
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_166_E2A

```json
{
  "video_id": "human_166",
  "edit_id": "human_166_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_166.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "walking_man",
    "target_description": "the walking man",
    "source_state": "The man walks along the wooded path while filming himself.",
    "desired_change": "The man steps over one fallen branch on the path."
  },
  "timing": {
    "edit_point_sec": 38.0,
    "effect_start_sec": 38.0,
    "effect_end_sec": 41.0,
    "evaluation_window_sec": [
      37.0,
      43.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 38.0 seconds, make the walking man step over one fallen branch on the wooded path.",
  "expected_result": {
    "description": "The man steps over one fallen branch on the path.",
    "target_phrase": "steps over fallen branch"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      37.0,
      43.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_166_E2B

```json
{
  "video_id": "human_166",
  "edit_id": "human_166_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_166_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Addition",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "tan_hiking_backpack",
    "target_description": "a tan hiking backpack",
    "source_state": "The man carries no visible backpack.",
    "desired_change": "A tan hiking backpack appears on the man's back."
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
  "instruction": "At 35.0 seconds, add a tan hiking backpack to the walking man's back.",
  "expected_result": {
    "description": "A tan hiking backpack appears on the man's back.",
    "target_phrase": "tan hiking backpack"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_166_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      34,
      38
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The documented target was reviewed as visible and trackable around the 35.0-second placement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_166_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a tan hiking backpack on B independently of E1's change to the man's bright-blue jacket; both edit results must coexist in C."
  }
}
```

## human_168

### human_168_E1

```json
{
  "video_id": "human_168",
  "edit_id": "human_168_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_168.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Color Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "khaki_diaper_bag",
    "target_description": "the khaki diaper bag",
    "source_state": "The open diaper bag is khaki colored.",
    "desired_change": "The diaper bag becomes forest green."
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
  "instruction": "Starting at 14.0 seconds, change the khaki diaper bag to forest green over the next two seconds.",
  "expected_result": {
    "description": "The diaper bag becomes forest green.",
    "target_phrase": "forest-green diaper bag"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_168_E2A

```json
{
  "video_id": "human_168",
  "edit_id": "human_168_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_168.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "green_cylindrical_wipes_container",
    "target_description": "the green cylindrical wipes container",
    "source_state": "The green cylindrical wipes container sits among the unpacked items beside the open bag.",
    "desired_change": "The woman lifts the green wipes container above the bag and rotates it continuously for three seconds."
  },
  "timing": {
    "edit_point_sec": 37.0,
    "effect_start_sec": 37.0,
    "effect_end_sec": 40.0,
    "evaluation_window_sec": [
      36.0,
      42.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 37.0 seconds, make the woman lift the green cylindrical wipes container above the open bag and rotate it continuously for three seconds.",
  "expected_result": {
    "description": "The woman holds the green wipes container above the bag while rotating it continuously.",
    "target_phrase": "green wipes container rotating above bag"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      36.0,
      42.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_168_E2B

```json
{
  "video_id": "human_168",
  "edit_id": "human_168_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_168_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Acceleration",
    "scope": "Ongoing Process"
  },
  "target": {
    "target_id": "ongoing_diaper_bag_sorting_process",
    "target_description": "the ongoing diaper-bag sorting process",
    "source_state": "The woman sorts the diaper-bag contents at the original pace.",
    "desired_change": "The sorting process progresses at twice its original speed."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 36.0,
    "evaluation_window_sec": [
      28.0,
      38.0
    ],
    "temporal_behavior": "accelerated semantic process"
  },
  "instruction": "Starting at 29.0 seconds, make the ongoing diaper-bag sorting process progress at twice its original speed until 36.0 seconds.",
  "expected_result": {
    "description": "The sorting process progresses at twice its original speed.",
    "target_phrase": "diaper-bag sorting at twice speed"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of human_168_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      38.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_168_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the ongoing diaper-bag sorting process on B independently of E1's change to the khaki diaper bag; both edit results must coexist in C."
  }
}
```

## human_170

### human_170_E1

```json
{
  "video_id": "human_170",
  "edit_id": "human_170_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_170.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_red_shirt",
    "target_description": "the man's red shirt",
    "source_state": "The man wears a red shirt.",
    "desired_change": "The shirt becomes turquoise."
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
  "instruction": "Starting at 14.0 seconds, change the man's red shirt to turquoise over the next two seconds.",
  "expected_result": {
    "description": "The shirt becomes turquoise.",
    "target_phrase": "turquoise shirt"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_170_E2A

```json
{
  "video_id": "human_170",
  "edit_id": "human_170_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_170.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "clear_drinking_glass_in_right_hand",
    "target_description": "the clear drinking glass in the man's right hand",
    "source_state": "The man holds the clear drinking glass near chest height in his right hand.",
    "desired_change": "The man raises the clear drinking glass above his head and holds it there."
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
  "instruction": "Starting at 29.0 seconds, make the man raise the clear drinking glass in his right hand above his head and hold it there.",
  "expected_result": {
    "description": "The man holds the clear drinking glass above his head in his right hand.",
    "target_phrase": "clear glass held above head"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_170_E2B

```json
{
  "video_id": "human_170",
  "edit_id": "human_170_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_170_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "clear_glass_pitcher",
    "target_description": "a clear glass pitcher",
    "source_state": "No glass pitcher is visible on the table.",
    "desired_change": "A clear glass pitcher appears on the table beside the bottles."
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
  "instruction": "At 29.0 seconds, add a clear glass pitcher to the table beside the bottles.",
  "expected_result": {
    "description": "A clear glass pitcher appears on the table beside the bottles.",
    "target_phrase": "clear glass pitcher"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_170_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
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
    "description": "The new target is absent in the source, while its intended placement anchor remains identifiable around the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_170_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes a clear glass pitcher on B independently of E1's change to the man's red shirt; both edit results must coexist in C."
  }
}
```

## human_171

### human_171_E1

```json
{
  "video_id": "human_171",
  "edit_id": "human_171_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_171.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_red_cap",
    "target_description": "the man's red cap",
    "source_state": "The man wears a red cap.",
    "desired_change": "The cap becomes dark green."
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
  "instruction": "Starting at 14.0 seconds, change the man's red cap to dark green over the next two seconds.",
  "expected_result": {
    "description": "The cap becomes dark green.",
    "target_phrase": "dark-green cap"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_171_E2A

```json
{
  "video_id": "human_171",
  "edit_id": "human_171_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_171.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man faces the camera and gestures near his torso.",
    "desired_change": "The man turns his torso toward the shelves and points with both hands."
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
  "instruction": "Starting at 29.0 seconds, make the man turn his torso toward the shelves and point with both hands.",
  "expected_result": {
    "description": "The man turns his torso toward the shelves and points with both hands.",
    "target_phrase": "turns and points toward shelves"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_171_E2B

```json
{
  "video_id": "human_171",
  "edit_id": "human_171_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_171_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Perspective Transfer",
    "operation": "Third-to-First Person",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "viewpoint",
    "target_description": "the viewpoint",
    "source_state": "The man is shown from a third-person frontal view in the stockroom.",
    "desired_change": "The stockroom is shown from the man's first-person perspective toward the packed shelving."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      28.0,
      33.0
    ],
    "temporal_behavior": "viewpoint transition"
  },
  "instruction": "Starting at 29.0 seconds, change the view to the man's first-person perspective toward the packed shelving over the next two seconds.",
  "expected_result": {
    "description": "The stockroom is shown from the man's first-person perspective toward the packed shelving.",
    "target_phrase": "first-person view toward packed shelving"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_171_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_171_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the viewpoint on B independently of E1's change to the man's red cap; both edit results must coexist in C."
  }
}
```

## human_173

### human_173_E1

```json
{
  "video_id": "human_173",
  "edit_id": "human_173_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_173.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "performer",
    "target_description": "the performer",
    "source_state": "The performer leans and gestures while addressing the audience.",
    "desired_change": "The performer leans forward and opens both arms wide toward the audience."
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
  "instruction": "Starting at 14.0 seconds, make the performer lean forward and open both arms wide toward the audience.",
  "expected_result": {
    "description": "The performer leans forward and opens both arms wide toward the audience.",
    "target_phrase": "leans forward with arms open"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_173_E2A

```json
{
  "video_id": "human_173",
  "edit_id": "human_173_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_173.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "performer_and_nearest_front_row_audience_member",
    "target_description": "the performer and the nearest front-row audience member",
    "source_state": "The performer and front-row audience member are separated by the stage edge.",
    "desired_change": "The nearest audience member sits directly in front of the performer."
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
  "instruction": "At 29.0 seconds, reposition the nearest front-row audience member directly in front of the performer.",
  "expected_result": {
    "description": "The nearest audience member sits directly in front of the performer.",
    "target_phrase": "audience member in front of performer"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_173_E2B

```json
{
  "video_id": "human_173",
  "edit_id": "human_173_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_173_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "pink_paper_on_wall",
    "target_description": "the pink paper on the wall",
    "source_state": "A pink sheet of paper is attached to the wall.",
    "desired_change": "The pink sheet of paper is removed from the wall."
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
  "instruction": "At 29.0 seconds, remove the pink sheet of paper from the wall.",
  "expected_result": {
    "description": "The pink sheet of paper is removed from the wall.",
    "target_phrase": "pink wall paper removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_173_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_173_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the pink paper on the wall on B independently of E1's change to the performer; both edit results must coexist in C."
  }
}
```

## human_175

### human_175_E1

```json
{
  "video_id": "human_175",
  "edit_id": "human_175_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_175.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The presenter and several cameras are shown in a wide outdoor view.",
    "desired_change": "The framing moves closer to the medium-format camera on the tripod."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 24,
    "evaluation_window_sec": [
      19,
      26
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 20.0 seconds, zoom in on the medium-format camera mounted on the tripod over four seconds.",
  "expected_result": {
    "description": "The framing moves closer to the medium-format camera on the tripod.",
    "target_phrase": "close view of tripod camera"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19,
      26
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_175_E2A

```json
{
  "video_id": "human_175",
  "edit_id": "human_175_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_175.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Motion",
    "operation": "New Motion",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "medium_format_camera",
    "target_description": "the medium-format camera",
    "source_state": "The presenter turns the camera to show several sides.",
    "desired_change": "The camera rotates through one full turn in the presenter's hands."
  },
  "timing": {
    "edit_point_sec": 31.0,
    "effect_start_sec": 31.0,
    "effect_end_sec": 35.0,
    "evaluation_window_sec": [
      30.0,
      37.0
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 31.0 seconds, make the medium-format camera rotate through one full turn in the presenter's hands.",
  "expected_result": {
    "description": "The camera rotates through one full turn in the presenter's hands.",
    "target_phrase": "camera rotating one full turn"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.0,
      37.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_175_E2B

```json
{
  "video_id": "human_175",
  "edit_id": "human_175_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_175_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Object-Object",
    "operation": "Relational Repositioning",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "frontmost_right_black_equipment_bag",
    "target_description": "the frontmost black equipment bag on the right side of the tripod",
    "source_state": "The frontmost black equipment bag rests on the right side of the camera tripod in the wide equipment view.",
    "desired_change": "The equipment bag is repositioned onto the left side of the tripod."
  },
  "timing": {
    "edit_point_sec": 35.0,
    "effect_start_sec": 36.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      35.0,
      41.0
    ],
    "temporal_behavior": "instant persistent change",
    "source_stage_at_edit": "immediately before the wide equipment view returns"
  },
  "instruction": "At 35.0 seconds, reposition the frontmost black equipment bag from the tripod's right side to its left when the wide view returns at 36.5 seconds.",
  "expected_result": {
    "description": "The frontmost black equipment bag rests on the left side of the camera tripod in the wide equipment view.",
    "target_phrase": "black equipment bag left of tripod"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_175_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      35.0,
      41.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The wide view returns around 36.5 seconds with the tripod and the cluster of black equipment bags clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_175_E1",
    "must_preserve_e1_result": true,
    "description": "This edit repositions one black equipment bag on B independently of E1's camera-framing change; both edit results must coexist in C."
  }
}
```

## human_176

### human_176_E1

```json
{
  "video_id": "human_176",
  "edit_id": "human_176_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_176.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "sign_language_presenter",
    "target_description": "the sign-language presenter",
    "source_state": "The presenter signs with a composed expression.",
    "desired_change": "The presenter smiles warmly while continuing to sign."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      13,
      19
    ],
    "temporal_behavior": "sustained expression"
  },
  "instruction": "Starting at 14.0 seconds, make the sign-language presenter smile warmly.",
  "expected_result": {
    "description": "The presenter smiles warmly while continuing to sign.",
    "target_phrase": "warm smile while signing"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_176_E2A

```json
{
  "video_id": "human_176",
  "edit_id": "human_176_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_176.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "brown_yellow_paper_texture_background",
    "target_description": "the brown-yellow paper-texture background",
    "source_state": "A brown-yellow paper-texture background fills the composition behind the presenter and overlays.",
    "desired_change": "The brown-yellow background is replaced with a muted green plaster wall."
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
  "instruction": "At 29.0 seconds, replace the brown-yellow paper-texture background with a muted green plaster wall.",
  "expected_result": {
    "description": "The brown-yellow background is replaced with a muted green plaster wall.",
    "target_phrase": "muted green plaster wall"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_176_E2B

```json
{
  "video_id": "human_176",
  "edit_id": "human_176_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_176_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The presenter and sculpture share a balanced composite view.",
    "desired_change": "The framing moves closer to the sign-language presenter's upper body and hands."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom in on the sign-language presenter's upper body and hands over three seconds.",
  "expected_result": {
    "description": "The framing moves closer to the sign-language presenter's upper body and hands.",
    "target_phrase": "close view of presenter and hands"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_176_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_176_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the sign-language presenter; both edit results must coexist in C."
  }
}
```

## human_180

### human_180_E1

```json
{
  "video_id": "human_180",
  "edit_id": "human_180_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_180.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "woman_and_man",
    "target_description": "the woman and the man",
    "source_state": "The two presenters sit side by side with a visible gap.",
    "desired_change": "The two presenters sit closer together with their shoulders nearly touching."
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
  "instruction": "At 14.0 seconds, reposition the two presenters closer together with their shoulders nearly touching.",
  "expected_result": {
    "description": "The two presenters sit closer together with their shoulders nearly touching.",
    "target_phrase": "presenters seated closer together"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_180_E2A

```json
{
  "video_id": "human_180",
  "edit_id": "human_180_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_180.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "candle_behind_presenters",
    "target_description": "the candle behind the presenters",
    "source_state": "A decorative candle is visible among the objects behind the presenters.",
    "desired_change": "The decorative candle is removed from the background."
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
  "instruction": "At 29.0 seconds, remove the decorative candle from behind the presenters.",
  "expected_result": {
    "description": "The decorative candle is removed from the background.",
    "target_phrase": "background candle removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_180_E2B

```json
{
  "video_id": "human_180",
  "edit_id": "human_180_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_180_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Cut-paper Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The two-person discussion has a realistic photographic appearance.",
    "desired_change": "The full frame is rendered as layered cut-paper artwork."
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into layered cut-paper artwork over the next two seconds.",
  "expected_result": {
    "description": "The full frame is rendered as layered cut-paper artwork.",
    "target_phrase": "cut-paper discussion scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_180_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_180_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the woman and the man; both edit results must coexist in C."
  }
}
```

## human_181

### human_181_E1

```json
{
  "video_id": "human_181",
  "edit_id": "human_181_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_181.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_white_headphones",
    "target_description": "the man's white headphones",
    "source_state": "The man wears white over-ear headphones.",
    "desired_change": "The headphones become bright red."
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
  "instruction": "Starting at 14.0 seconds, change the man's white headphones to bright red over the next two seconds.",
  "expected_result": {
    "description": "The headphones become bright red.",
    "target_phrase": "bright-red headphones"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_181_E2A

```json
{
  "video_id": "human_181",
  "edit_id": "human_181_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_181.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man alternates his gaze between the camera and the car windows.",
    "desired_change": "The man turns toward the side window and nods twice."
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
  "instruction": "Starting at 29.0 seconds, make the man turn toward the side window and nod twice.",
  "expected_result": {
    "description": "The man turns toward the side window and nods twice.",
    "target_phrase": "turns toward window and nods"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_181_E2B

```json
{
  "video_id": "human_181",
  "edit_id": "human_181_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_181_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man occupies the center of the low-angle car interior frame.",
    "desired_change": "The man is positioned on the left side, revealing more of the steering wheel."
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
  "instruction": "At 29.0 seconds, reposition the man on the left side of the frame to reveal more of the steering wheel.",
  "expected_result": {
    "description": "The man is positioned on the left side, revealing more of the steering wheel.",
    "target_phrase": "man positioned left of steering wheel"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_181_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_181_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man on B independently of E1's change to the man's white headphones; both edit results must coexist in C."
  }
}
```

## human_184

### human_184_E1

```json
{
  "video_id": "human_184",
  "edit_id": "human_184_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_184.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_dark_red_top",
    "target_description": "the woman's dark-red top",
    "source_state": "The woman wears a dark-red long-sleeve top.",
    "desired_change": "The top becomes navy blue."
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
  "instruction": "Starting at 14.0 seconds, change the woman's dark-red top to navy blue over the next two seconds.",
  "expected_result": {
    "description": "The top becomes navy blue.",
    "target_phrase": "navy-blue top"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_184_E2A

```json
{
  "video_id": "human_184",
  "edit_id": "human_184_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_184.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "Motion Modification",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "guitarist",
    "target_description": "the guitarist",
    "source_state": "The guitarist strums steadily while singing.",
    "desired_change": "The guitarist switches to rapid fingerpicking."
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
  "instruction": "Starting at 29.0 seconds, make the guitarist switch to rapid fingerpicking for four seconds.",
  "expected_result": {
    "description": "The guitarist switches to rapid fingerpicking.",
    "target_phrase": "rapid guitar fingerpicking"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_184_E2B

```json
{
  "video_id": "human_184",
  "edit_id": "human_184_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_184_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman is centered in front of the vertical blinds.",
    "desired_change": "The woman is positioned on the left side, revealing more of the blinds."
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
  "instruction": "At 29.0 seconds, reposition the woman on the left side of the frame to reveal more of the vertical blinds.",
  "expected_result": {
    "description": "The woman is positioned on the left side, revealing more of the blinds.",
    "target_phrase": "woman positioned left of blinds"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_184_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_184_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the woman on B independently of E1's change to the woman's dark-red top; both edit results must coexist in C."
  }
}
```

## human_185

### human_185_E1

```json
{
  "video_id": "human_185",
  "edit_id": "human_185_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_185.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Pattern Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_gray_striped_shirt",
    "target_description": "the man's gray striped shirt",
    "source_state": "The man wears a gray striped long-sleeve shirt.",
    "desired_change": "The shirt becomes solid dark green."
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
  "instruction": "Starting at 14.0 seconds, change the man's gray striped shirt to solid dark green over the next two seconds.",
  "expected_result": {
    "description": "The shirt becomes solid dark green.",
    "target_phrase": "solid dark-green shirt"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_185_E2A

```json
{
  "video_id": "human_185",
  "edit_id": "human_185_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_185.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands facing forward beside the graphic area.",
    "desired_change": "The man rotates his torso toward the graphic area and leans sideways."
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
  "instruction": "Starting at 29.0 seconds, make the man rotate his torso toward the graphic area and lean sideways.",
  "expected_result": {
    "description": "The man rotates his torso toward the graphic area and leans sideways.",
    "target_phrase": "sideways lean toward graphic area"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_185_E2B

```json
{
  "video_id": "human_185",
  "edit_id": "human_185_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_185_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Absolute Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man stands near the center beside the exposure graphic area.",
    "desired_change": "The man stands on the left side beside the graphic area."
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
  "instruction": "At 29.0 seconds, reposition the man on the left side of the frame beside the exposure graphic area.",
  "expected_result": {
    "description": "The man stands on the left side beside the graphic area.",
    "target_phrase": "man left of graphic area"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of human_185_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_185_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the man on B independently of E1's change to the man's gray striped shirt; both edit results must coexist in C."
  }
}
```

## human_187

### human_187_E1

```json
{
  "video_id": "human_187",
  "edit_id": "human_187_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_187.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Hair",
    "operation": "Hairstyle Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_straight_bangs",
    "target_description": "the woman's straight bangs",
    "source_state": "The woman has straight bangs across her forehead.",
    "desired_change": "The bangs become side swept."
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
  "instruction": "Starting at 14.0 seconds, change the woman's straight bangs to side-swept bangs over the next two seconds.",
  "expected_result": {
    "description": "The bangs become side swept.",
    "target_phrase": "side-swept bangs"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_187_E2A

```json
{
  "video_id": "human_187",
  "edit_id": "human_187_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_187.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman maintains a stable forward-facing pose.",
    "desired_change": "The woman tilts her head left and right once."
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
  "instruction": "Starting at 29.0 seconds, make the woman tilt her head left and right once.",
  "expected_result": {
    "description": "The woman tilts her head left and right once.",
    "target_phrase": "one left-right head tilt"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_187_E2B

```json
{
  "video_id": "human_187",
  "edit_id": "human_187_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_187_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom Out",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera_framing",
    "target_description": "the camera framing",
    "source_state": "The woman is shown in a tight head-and-shoulders view.",
    "desired_change": "The framing widens to include the woman's upper torso."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      28.0,
      34.0
    ],
    "temporal_behavior": "gradual camera transition"
  },
  "instruction": "Starting at 29.0 seconds, zoom out to include the woman's upper torso over three seconds.",
  "expected_result": {
    "description": "The framing widens to include the woman's upper torso.",
    "target_phrase": "wider upper-torso view"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_187_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_187_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing on B independently of E1's change to the woman's straight bangs; both edit results must coexist in C."
  }
}
```

## human_190

### human_190_E1

```json
{
  "video_id": "human_190",
  "edit_id": "human_190_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_190.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Accessories",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_black_eyeglass_frames",
    "target_description": "the man's black eyeglass frames",
    "source_state": "The man wears black eyeglass frames.",
    "desired_change": "The frames become translucent amber."
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
  "instruction": "Starting at 14.0 seconds, change the man's black eyeglass frames to translucent amber over the next two seconds.",
  "expected_result": {
    "description": "The frames become translucent amber.",
    "target_phrase": "translucent-amber eyeglass frames"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_190_E2A

```json
{
  "video_id": "human_190",
  "edit_id": "human_190_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_190.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Upper-body/Posture",
    "operation": "Posture Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits upright behind the table.",
    "desired_change": "The man leans forward and then straightens his torso."
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
  "instruction": "Starting at 29.0 seconds, make the man lean forward and straighten his torso once.",
  "expected_result": {
    "description": "The man leans forward and then straightens his torso.",
    "target_phrase": "one forward lean and straighten"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_190_E2B

```json
{
  "video_id": "human_190",
  "edit_id": "human_190_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_190_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "large_lens_on_middle_shelf",
    "target_description": "the large lens on the middle shelf",
    "source_state": "A large camera lens sits on the middle shelf.",
    "desired_change": "The large lens is replaced with a compact film camera."
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
  "instruction": "At 29.0 seconds, replace the large lens on the middle shelf with a compact film camera.",
  "expected_result": {
    "description": "The large lens is replaced with a compact film camera.",
    "target_phrase": "compact film camera on shelf"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_190_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_190_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large lens on the middle shelf on B independently of E1's change to the man's black eyeglass frames; both edit results must coexist in C."
  }
}
```

## human_191

### human_191_E1

```json
{
  "video_id": "human_191",
  "edit_id": "human_191_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_191.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Weather Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "outdoor_platform_weather",
    "target_description": "the outdoor platform weather",
    "source_state": "The outdoor platform has dry weather.",
    "desired_change": "A gentle rain begins across the platform."
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
  "instruction": "Starting at 14.0 seconds, change the dry outdoor weather to gentle rain over the next two seconds.",
  "expected_result": {
    "description": "A gentle rain begins across the platform.",
    "target_phrase": "gentle outdoor rain"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_191_E2A

```json
{
  "video_id": "human_191",
  "edit_id": "human_191_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_191.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man holds the microphone near his chest while speaking.",
    "desired_change": "The man raises the microphone above his head with one hand."
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
  "instruction": "Starting at 29.0 seconds, make the man raise the microphone above his head with one hand.",
  "expected_result": {
    "description": "The man raises the microphone above his head with one hand.",
    "target_phrase": "microphone raised overhead"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      34.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_191_E2B

```json
{
  "video_id": "human_191",
  "edit_id": "human_191_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_191_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Dolly In",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "camera",
    "target_description": "the camera",
    "source_state": "The camera holds a fixed medium view of the seated man.",
    "desired_change": "The camera moves smoothly closer to the man's face and microphone."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      28.0,
      36.0
    ],
    "temporal_behavior": "continuous camera motion"
  },
  "instruction": "Starting at 29.0 seconds, move the camera smoothly closer to the man's face and microphone over five seconds.",
  "expected_result": {
    "description": "The camera moves smoothly closer to the man's face and microphone.",
    "target_phrase": "smooth dolly in toward speaker"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of human_191_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      36.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_191_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera on B independently of E1's change to the outdoor platform weather; both edit results must coexist in C."
  }
}
```

## human_192

### human_192_E1

```json
{
  "video_id": "human_192",
  "edit_id": "human_192_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_192.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Clothing",
    "operation": "Color Change",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_dark_outdoor_jacket",
    "target_description": "the man's dark outdoor jacket",
    "source_state": "The man wears a dark outdoor jacket.",
    "desired_change": "The jacket becomes burnt orange."
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
  "instruction": "Starting at 14.0 seconds, change the man's dark outdoor jacket to burnt orange over the next two seconds.",
  "expected_result": {
    "description": "The jacket becomes burnt orange.",
    "target_phrase": "burnt-orange outdoor jacket"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      18
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_192_E2A

```json
{
  "video_id": "human_192",
  "edit_id": "human_192_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_192.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Head/Gaze",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man faces forward with small head movements.",
    "desired_change": "The man looks over each shoulder in sequence."
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
  "instruction": "Starting at 29.0 seconds, make the man look over his left and right shoulders in sequence.",
  "expected_result": {
    "description": "The man looks over each shoulder in sequence.",
    "target_phrase": "looks over both shoulders"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      35.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_192_E2B

```json
{
  "video_id": "human_192",
  "edit_id": "human_192_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_192_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "1970s Nature-documentary Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The woodland explanation has a modern digital-video appearance.",
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
  "instruction": "Starting at 29.0 seconds, transform the full frame into a 1970s color nature documentary over the next two seconds.",
  "expected_result": {
    "description": "The full frame resembles a 1970s color nature documentary.",
    "target_phrase": "1970s woodland documentary"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_192_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_192_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man's dark outdoor jacket; both edit results must coexist in C."
  }
}
```

## human_193

### human_193_E1

```json
{
  "video_id": "human_193",
  "edit_id": "human_193_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_193.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Full-body Action",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man_in_light_jacket",
    "target_description": "the man in the light jacket",
    "source_state": "The man walks through the dense woodland while explaining the vegetation.",
    "desired_change": "The man ducks beneath one low branch while walking."
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
  "instruction": "Starting at 14.0 seconds, make the man in the light jacket duck beneath one low branch while walking.",
  "expected_result": {
    "description": "The man ducks beneath one low branch while walking.",
    "target_phrase": "ducks beneath low branch"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_193_E2A

```json
{
  "video_id": "human_193",
  "edit_id": "human_193_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_193.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Person",
    "operation": "Relational Repositioning",
    "scope": "Multiple People"
  },
  "target": {
    "target_id": "two_men_walking_through_woodland",
    "target_description": "the two men walking through the woodland",
    "source_state": "The two men walk at different depths in the woodland.",
    "desired_change": "The two men are positioned side by side on the woodland path."
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
  "instruction": "At 29.0 seconds, reposition the two men side by side on the woodland path.",
  "expected_result": {
    "description": "The two men are positioned side by side on the woodland path.",
    "target_phrase": "two men side by side"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_193_E2B

```json
{
  "video_id": "human_193",
  "edit_id": "human_193_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_193_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Environment Object",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "broad_leaf_plant_on_right",
    "target_description": "the broad-leaf plant on the right",
    "source_state": "A broad-leaf plant grows beside the walking route.",
    "desired_change": "The broad-leaf plant is replaced with a young conifer tree."
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
  "instruction": "At 29.0 seconds, replace the broad-leaf plant on the right with a young conifer tree.",
  "expected_result": {
    "description": "The broad-leaf plant is replaced with a young conifer tree.",
    "target_phrase": "young conifer tree"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of human_193_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_193_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the broad-leaf plant on the right on B independently of E1's change to the man in the light jacket; both edit results must coexist in C."
  }
}
```

## human_197

### human_197_E1

```json
{
  "video_id": "human_197",
  "edit_id": "human_197_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_197.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Hand/Arm",
    "operation": "New Motion",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man uses open comparative gestures while explaining grammar.",
    "desired_change": "The man counts three points with his right hand."
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
  "instruction": "Starting at 14.0 seconds, make the man count three points with his right hand.",
  "expected_result": {
    "description": "The man counts three points with his right hand.",
    "target_phrase": "counts three points"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_197_E2A

```json
{
  "video_id": "human_197",
  "edit_id": "human_197_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_197.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Person-Environment",
    "operation": "Relational Repositioning",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "man",
    "target_description": "the man",
    "source_state": "The man sits near the center of the red steps and stone wall.",
    "desired_change": "The man sits beside the red step on the right."
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
  "instruction": "At 29.0 seconds, reposition the man beside the red step on the right.",
  "expected_result": {
    "description": "The man sits beside the red step on the right.",
    "target_phrase": "man beside right red step"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_197_E2B

```json
{
  "video_id": "human_197",
  "edit_id": "human_197_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_197_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Duotone Color Grade",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "full_video_frame",
    "target_description": "the full video frame",
    "source_state": "The outdoor lesson uses a natural full-color photographic grade.",
    "desired_change": "The full frame uses a restrained teal-and-gold duotone grade."
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
  "instruction": "Starting at 29.0 seconds, apply a restrained teal-and-gold duotone grade to the full frame over the next two seconds.",
  "expected_result": {
    "description": "The full frame uses a restrained teal-and-gold duotone grade.",
    "target_phrase": "teal-and-gold duotone grade"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_197_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_197_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full video frame on B independently of E1's change to the man; both edit results must coexist in C."
  }
}
```

## human_198

### human_198_E1

```json
{
  "video_id": "human_198",
  "edit_id": "human_198_E1",
  "edge": "A_to_B",
  "source_video_path": "videos/human_198.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Face/Expression",
    "operation": "New Expression",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman speaks with animated facial expressions.",
    "desired_change": "The woman puffs out both cheeks and raises her eyebrows."
  },
  "timing": {
    "edit_point_sec": 14,
    "effect_start_sec": 14,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      13,
      19
    ],
    "temporal_behavior": "bounded expression"
  },
  "instruction": "Starting at 14.0 seconds, make the woman puff out both cheeks and raise her eyebrows.",
  "expected_result": {
    "description": "The woman puffs out both cheeks and raises her eyebrows.",
    "target_phrase": "puffed cheeks and raised eyebrows"
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
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      19
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
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

### human_198_E2A

```json
{
  "video_id": "human_198",
  "edit_id": "human_198_E2A",
  "edge": "A_to_D",
  "source_video_path": "videos/human_198.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Person-related Object",
    "operation": "Replacement",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman_wide_silver_necklace",
    "target_description": "the woman's wide silver necklace",
    "source_state": "The woman wears a wide silver necklace.",
    "desired_change": "The silver necklace is replaced with a red silk scarf."
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
  "instruction": "At 29.0 seconds, replace the woman's wide silver necklace with a red silk scarf.",
  "expected_result": {
    "description": "The silver necklace is replaced with a red silk scarf.",
    "target_phrase": "red silk scarf"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      32.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### human_198_E2B

```json
{
  "video_id": "human_198",
  "edit_id": "human_198_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/human_198_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Person-local Style",
    "operation": "Pop-art Rendering",
    "scope": "Main Person"
  },
  "target": {
    "target_id": "woman",
    "target_description": "the woman",
    "source_state": "The woman has a realistic on-camera appearance.",
    "desired_change": "The woman is rendered as a bold pop-art portrait."
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
  "instruction": "Starting at 29.0 seconds, render the woman as a bold pop-art portrait over the next two seconds.",
  "expected_result": {
    "description": "The woman is rendered as a bold pop-art portrait.",
    "target_phrase": "pop-art portrait"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of human_198_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, and handheld-card text"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.0,
      33.0
    ],
    "target_visible": true,
    "target_stability": "stable",
    "occlusion_level": "none or low",
    "shot_continuity": "continuous within the selected window",
    "description": "The selected target remains identifiable around the selected edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "human_198_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the woman on B independently of E1's change to the woman; both edit results must coexist in C."
  }
}
```
