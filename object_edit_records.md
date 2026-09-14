# Synthetic Object Edit Records

This cumulative file uses one globally randomized, quota-exact taxonomy allocation across all 100 videos. The approved 001-020 pilot is frozen; later records are added only after full-video 1.0-second and 0.5-second review.

- Reviewed videos: 100/100
- Reviewed records: 300/300
- Command-time rule: every edit point is earlier than 37 seconds; effect and evaluation windows may extend beyond 37 seconds
- Branch rule: E1 occurs before 20 seconds, E2A/E2B occur at or after 20 seconds, and E1-to-E2B is at most 15 seconds
- Allocation scope: all 300 slots solved together; 20-video boundaries are review checkpoints only
- Global branch-to-primary Cramer's V: 0.0211

## Global Primary-Type Targets

| Primary type | Target |
|---|---|
| Motion | 85 |
| Attribute | 75 |
| Spatial | 38 |
| Composition | 45 |
| Camera | 20 |
| Style | 22 |
| Temporal | 15 |

## Records

## synthetic_object_001

### synthetic_object_001_E1

```json
{
  "video_id": "synthetic_object_001",
  "edit_id": "synthetic_object_001_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Colored-pencil Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_dog_and_frisbee_scene",
    "target_description": "the full dog-and-frisbee scene",
    "source_state": "The scene uses natural photographic rendering.",
    "desired_change": "The full scene is rendered as a colored-pencil animation."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 13.5,
    "evaluation_window_sec": [
      10.5,
      15.5
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 11.5 seconds, transform the full dog-and-frisbee scene into a colored-pencil animation over the next two seconds.",
  "expected_result": {
    "description": "The full scene is rendered as a colored-pencil animation.",
    "target_phrase": "dog-and-frisbee scene in colored-pencil animation"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      10.5,
      15.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dog, red frisbee, grass, trees, and curved path are all clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_001_E2A

```json
{
  "video_id": "synthetic_object_001",
  "edit_id": "synthetic_object_001_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_001.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Bounding-stride Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_dog_carrying_the_frisbee",
    "target_description": "the dog carrying the red frisbee",
    "source_state": "The dog runs along the curved paved path while carrying the frisbee.",
    "desired_change": "The dog performs two high bounding strides along the curved path."
  },
  "timing": {
    "edit_point_sec": 33.5,
    "effect_start_sec": 33.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      32.5,
      39.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 33.5 seconds, make the dog carrying the red frisbee perform two high bounding strides along the curved paved path.",
  "expected_result": {
    "description": "The dog performs two high bounding strides along the curved path.",
    "target_phrase": "dog performing two high bounding strides"
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
      32.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dog and carried red frisbee remain unobstructed on the curved path."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_001_E2B

```json
{
  "video_id": "synthetic_object_001",
  "edit_id": "synthetic_object_001_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_001_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Leap-and-Landing Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_dog_leap_and_landing_process",
    "target_description": "the dog's ongoing leap-and-landing process",
    "source_state": "The dog is airborne near the red frisbee and has not completed its landing.",
    "desired_change": "The leap-and-landing process advances faster, with all four paws on the grass by 26.5 seconds."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      23.5,
      28.5
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 24.5 seconds, accelerate the dog's ongoing leap and landing so all four paws return to the grass by 26.5 seconds.",
  "expected_result": {
    "description": "The leap-and-landing process advances faster, with all four paws on the grass by 26.5 seconds.",
    "target_phrase": "dog completing its landing by 26.5 seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of synthetic_object_001_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The airborne dog and the next landing phase are visible in one continuous shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_001_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dog's ongoing leap-and-landing process on B independently of E1's change to the full dog-and-frisbee scene; both edit results must coexist in C."
  }
}
```

## synthetic_object_002

### synthetic_object_002_E1

```json
{
  "video_id": "synthetic_object_002",
  "edit_id": "synthetic_object_002_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_002.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Dorsal Coat Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_fox_dorsal_coat",
    "target_description": "the fox's dorsal coat",
    "source_state": "The fox has a warm russet-brown dorsal coat with dark legs and a pale tail tip.",
    "desired_change": "The dorsal coat becomes silver-gray while the dark legs and pale tail tip remain distinct."
  },
  "timing": {
    "edit_point_sec": 8.5,
    "effect_start_sec": 8.5,
    "effect_end_sec": 10.5,
    "evaluation_window_sec": [
      7.5,
      12.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 8.5 seconds, change the fox's warm russet-brown dorsal coat to silver-gray over the next two seconds.",
  "expected_result": {
    "description": "The dorsal coat becomes silver-gray while the dark legs and pale tail tip remain distinct.",
    "target_phrase": "fox with a silver-gray dorsal coat"
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
      7.5,
      12.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The fox's full side profile and major coat regions are clearly visible against the snow."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_002_E2A

```json
{
  "video_id": "synthetic_object_002",
  "edit_id": "synthetic_object_002_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_002.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Low Clockwise Arc Movement",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_view_around_the_fox",
    "target_description": "the camera view around the fox",
    "source_state": "The camera follows the fox from a mostly fixed side view.",
    "desired_change": "The camera makes a low clockwise arc around the fox with visible snow-and-forest parallax."
  },
  "timing": {
    "edit_point_sec": 32.5,
    "effect_start_sec": 32.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      31.5,
      39.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 32.5 seconds, move the camera in a low smooth clockwise arc around the fox for five seconds.",
  "expected_result": {
    "description": "The camera makes a low clockwise arc around the fox with visible snow-and-forest parallax.",
    "target_phrase": "low clockwise camera arc around the fox"
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
      31.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The fox, snowy ground, branch, and distant forest provide stable depth references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_002_E2B

```json
{
  "video_id": "synthetic_object_002",
  "edit_id": "synthetic_object_002_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_002_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Snow-scraping Interaction",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_fox_and_snow",
    "target_description": "the fox and the snow beneath its forepaws",
    "source_state": "The fox stands and investigates the snow without a distinct digging stroke.",
    "desired_change": "The fox scrapes the snow twice with both forepaws."
  },
  "timing": {
    "edit_point_sec": 22,
    "effect_start_sec": 22,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      21,
      27.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 22.0 seconds, make the fox scrape the snow twice with both forepaws directly beneath its chest.",
  "expected_result": {
    "description": "The fox scrapes the snow twice with both forepaws.",
    "target_phrase": "fox scraping snow twice with both forepaws"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_002_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The fox's forelegs and the snow beneath its chest are visible near the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_002_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the fox and the snow beneath its forepaws on B independently of E1's change to the fox's dorsal coat; both edit results must coexist in C."
  }
}
```

## synthetic_object_003

### synthetic_object_003_E1

```json
{
  "video_id": "synthetic_object_003",
  "edit_id": "synthetic_object_003_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_003.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Soil-flinging Interaction",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_elephant_trunk_and_soil",
    "target_description": "the elephant's trunk and the loose soil mound",
    "source_state": "The elephant moves its trunk near loose soil without the requested repeated throwing action.",
    "desired_change": "The elephant sweeps its trunk through the mound and flings soil over its left shoulder twice."
  },
  "timing": {
    "edit_point_sec": 7,
    "effect_start_sec": 7,
    "effect_end_sec": 11,
    "evaluation_window_sec": [
      6,
      13
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 7.0 seconds, make the elephant sweep its trunk through the loose mound and fling soil over its left shoulder twice.",
  "expected_result": {
    "description": "The elephant sweeps its trunk through the mound and flings soil over its left shoulder twice.",
    "target_phrase": "elephant flinging soil over its left shoulder twice"
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
      6,
      13
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The trunk, loose soil, shoulder, and forefeet are visible in a stable side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_003_E2A

```json
{
  "video_id": "synthetic_object_003",
  "edit_id": "synthetic_object_003_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_003.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Soil Coating State Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_soil_on_the_elephant_upper_back",
    "target_description": "the loose soil coating on the elephant's upper back",
    "source_state": "The elephant's upper back carries a loose, dusty soil coating.",
    "desired_change": "The loose coating becomes a thin continuous crust of dried mud."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 36.5,
    "evaluation_window_sec": [
      33.5,
      38.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 34.5 seconds, change the loose soil coating on the elephant's upper back into a thin crust of dried mud.",
  "expected_result": {
    "description": "The loose coating becomes a thin continuous crust of dried mud.",
    "target_phrase": "thin dried-mud crust on the elephant's upper back"
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
      33.5,
      38.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The elephant's upper back is broad, exposed, and trackable in the selected window."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_003_E2B

```json
{
  "video_id": "synthetic_object_003",
  "edit_id": "synthetic_object_003_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_003_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Soil-mound Relational Repositioning",
    "scope": "Core Object and Related Object"
  },
  "target": {
    "target_id": "the_loose_soil_mound_relative_to_the_elephant",
    "target_description": "the loose soil mound relative to the elephant's right forefoot",
    "source_state": "The loose soil is spread irregularly beneath and around the elephant.",
    "desired_change": "The loose soil forms one mound half a trunk-length to the right of the elephant's right forefoot."
  },
  "timing": {
    "edit_point_sec": 21,
    "effect_start_sec": 21,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      20,
      24
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 21.0 seconds, place the loose soil mound half a trunk-length to the right of the elephant's right forefoot.",
  "expected_result": {
    "description": "The loose soil forms one mound half a trunk-length to the right of the elephant's right forefoot.",
    "target_phrase": "soil mound beside the elephant's right forefoot"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_003_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20,
      24
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The soil, both forefeet, and trunk are simultaneously visible at the selected moment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_003_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the loose soil mound relative to the elephant's right forefoot on B independently of E1's change to the elephant's trunk and the loose soil mound; both edit results must coexist in C."
  }
}
```

## synthetic_object_004

### synthetic_object_004_E1

```json
{
  "video_id": "synthetic_object_004",
  "edit_id": "synthetic_object_004_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_004.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Gait Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_horse_gait",
    "target_description": "the horse's forward gait",
    "source_state": "The horse advances at a relaxed walk along the beach.",
    "desired_change": "The horse changes from walking to a steady trot for five seconds."
  },
  "timing": {
    "edit_point_sec": 15.5,
    "effect_start_sec": 15.5,
    "effect_end_sec": 20.5,
    "evaluation_window_sec": [
      14.5,
      22.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 15.5 seconds, change the horse's relaxed walk into a steady trot along the beach for five seconds.",
  "expected_result": {
    "description": "The horse changes from walking to a steady trot for five seconds.",
    "target_phrase": "horse trotting steadily along the beach"
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
      14.5,
      22.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The horse's full body and all four legs are visible in continuous side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_004_E2A

```json
{
  "video_id": "synthetic_object_004",
  "edit_id": "synthetic_object_004_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_004.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Rim-light Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_light_on_the_horse",
    "target_description": "the illumination along the horse's silhouette",
    "source_state": "The horse is lit by neutral daylight without a strong rim highlight.",
    "desired_change": "A warm golden rim light appears along the horse's outer silhouette."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      27,
      32
    ],
    "temporal_behavior": "gradual persistent illumination change"
  },
  "instruction": "Starting at 28.0 seconds, add a warm golden rim light along the horse's visible outer silhouette over two seconds.",
  "expected_result": {
    "description": "A warm golden rim light appears along the horse's outer silhouette.",
    "target_phrase": "horse outlined by warm golden rim light"
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
      27,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The horse is fully separated from the bright beach and water background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_004_E2B

```json
{
  "video_id": "synthetic_object_004",
  "edit_id": "synthetic_object_004_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_004_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "16 mm Film Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_horse_beach_video",
    "target_description": "the full horse-on-beach video",
    "source_state": "The scene has clean contemporary digital-video imaging.",
    "desired_change": "The scene takes on a 16 mm film appearance with fine grain and restrained color response."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      23,
      28
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 24.0 seconds, convert the full horse-on-beach video to a restrained 16 mm film look over two seconds.",
  "expected_result": {
    "description": "The scene takes on a 16 mm film appearance with fine grain and restrained color response.",
    "target_phrase": "horse-on-beach scene with a 16 mm film look"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_004_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The horse, beach, surf, and horizon are continuously visible and support a global media treatment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_004_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full horse-on-beach video on B independently of E1's change to the horse's forward gait; both edit results must coexist in C."
  }
}
```

## synthetic_object_005

### synthetic_object_005_E1

```json
{
  "video_id": "synthetic_object_005",
  "edit_id": "synthetic_object_005_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_005.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Paw-tapping Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cat_front_paw",
    "target_description": "the cat's visible front paw",
    "source_state": "The cat balances on the shelving without a repeated paw-tapping action.",
    "desired_change": "The cat lifts one front paw and taps the right shelf edge twice."
  },
  "timing": {
    "edit_point_sec": 16.5,
    "effect_start_sec": 16.5,
    "effect_end_sec": 20,
    "evaluation_window_sec": [
      15.5,
      22
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 16.5 seconds, make the cat lift one front paw and tap the right shelf edge twice.",
  "expected_result": {
    "description": "The cat lifts one front paw and taps the right shelf edge twice.",
    "target_phrase": "cat tapping the right shelf edge twice"
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
      15.5,
      22
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cat and right shelf edge are both visible in the elevated shelving view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_005_E2A

```json
{
  "video_id": "synthetic_object_005",
  "edit_id": "synthetic_object_005_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_005.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_horizontal_book_stack",
    "target_description": "the horizontal stack of books on the shelf top",
    "source_state": "A horizontal stack of books occupies the top surface of the shelving unit.",
    "desired_change": "The entire horizontal stack of books is removed from the shelf top."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 25,
    "evaluation_window_sec": [
      23,
      27
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.0 seconds, remove the horizontal stack of books from the top surface of the shelving unit.",
  "expected_result": {
    "description": "The entire horizontal stack of books is removed from the shelf top.",
    "target_phrase": "shelf top without the horizontal book stack"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      27
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full horizontal book stack is visible above and to the right of the cat."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_005_E2B

```json
{
  "video_id": "synthetic_object_005",
  "edit_id": "synthetic_object_005_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_005_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_walking_cat",
    "target_description": "the walking orange cat",
    "source_state": "The orange cat walks across loose papers near the center-right of the frame.",
    "desired_change": "The cat is repositioned onto the uncovered carpet in the left third of the frame."
  },
  "timing": {
    "edit_point_sec": 29.5,
    "effect_start_sec": 29.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      28.5,
      32.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 29.5 seconds, move the walking orange cat onto the uncovered carpet in the left third of the frame.",
  "expected_result": {
    "description": "The cat is repositioned onto the uncovered carpet in the left third of the frame.",
    "target_phrase": "orange cat walking in the left third of the frame"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_005_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      28.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cat and open carpet destination left of the loose papers are clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_005_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the walking orange cat on B independently of E1's change to the cat's visible front paw; both edit results must coexist in C."
  }
}
```

## synthetic_object_006

### synthetic_object_006_E1

```json
{
  "video_id": "synthetic_object_006",
  "edit_id": "synthetic_object_006_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_006.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Side-band Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_chameleon_side_band",
    "target_description": "the chameleon's cyan side band",
    "source_state": "The chameleon has a bright cyan band along its side.",
    "desired_change": "The cyan side band becomes amber-gold while the green scales and dark stripes remain distinct."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      12.5,
      17.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 13.5 seconds, change the chameleon's cyan side band to amber-gold over the next two seconds.",
  "expected_result": {
    "description": "The cyan side band becomes amber-gold while the green scales and dark stripes remain distinct.",
    "target_phrase": "chameleon with an amber-gold side band"
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
      12.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The chameleon's side band is broad, unobstructed, and color-separable from its green scales."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_006_E2A

```json
{
  "video_id": "synthetic_object_006",
  "edit_id": "synthetic_object_006_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_006.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_chameleon_forward_step",
    "target_description": "the chameleon's forward-foot placement on the branch",
    "source_state": "The chameleon begins placing its raised forward foot onto the branch without pausing.",
    "desired_change": "The forward step pauses with the foot raised for three seconds and then resumes until the foot reaches the branch."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 39.5,
    "evaluation_window_sec": [
      33.5,
      41.5
    ],
    "temporal_behavior": "temporary process pause"
  },
  "instruction": "Starting at 34.5 seconds, pause the chameleon's forward step with its foot raised for three seconds, then resume placing it on the branch.",
  "expected_result": {
    "description": "The forward step pauses with the foot raised for three seconds and then resumes until the foot reaches the branch.",
    "target_phrase": "forward step paused and then resumed"
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
      33.5,
      41.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The raised forward foot and its destination on the branch remain visible within one continuous shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_006_E2B

```json
{
  "video_id": "synthetic_object_006",
  "edit_id": "synthetic_object_006_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_006_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_dark_long_legged_insect",
    "target_description": "the dark long-legged insect on the branch",
    "source_state": "A dark long-legged insect stands on the branch ahead of the chameleon.",
    "desired_change": "The dark insect is replaced by one small brown moth in the same position."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      26,
      30
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 27.0 seconds, replace the dark long-legged insect on the branch with one small brown moth.",
  "expected_result": {
    "description": "The dark insect is replaced by one small brown moth in the same position.",
    "target_phrase": "small brown moth on the branch"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_006_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26,
      30
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The insect is isolated on the branch and clearly separated from the chameleon's head."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_006_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dark long-legged insect on the branch on B independently of E1's change to the chameleon's cyan side band; both edit results must coexist in C."
  }
}
```

## synthetic_object_007

### synthetic_object_007_E1

```json
{
  "video_id": "synthetic_object_007",
  "edit_id": "synthetic_object_007_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_007.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Zoom In",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_framing_of_the_perched_owl",
    "target_description": "the framing around the perched owl",
    "source_state": "The owl occupies a moderate portion of the snowy landscape frame.",
    "desired_change": "The camera zooms in until the owl's spread wings nearly fill the frame."
  },
  "timing": {
    "edit_point_sec": 10,
    "effect_start_sec": 10,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      9,
      15
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 10.0 seconds, zoom in smoothly until the perched owl's spread wings nearly fill the frame.",
  "expected_result": {
    "description": "The camera zooms in until the owl's spread wings nearly fill the frame.",
    "target_phrase": "close framing on the owl's spread wings"
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
      9,
      15
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The perched owl and both extended wings are fully visible against the snow."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_007_E2A

```json
{
  "video_id": "synthetic_object_007",
  "edit_id": "synthetic_object_007_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_007.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Wingbeat-speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_owl_wingbeats",
    "target_description": "the owl's wingbeats during flight toward the far post",
    "source_state": "The owl flies toward the far post with a moderate wingbeat cadence.",
    "desired_change": "The owl's wingbeat cadence increases for three seconds along the same flight route."
  },
  "timing": {
    "edit_point_sec": 22.5,
    "effect_start_sec": 22.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      21.5,
      27.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 22.5 seconds, accelerate the owl's wingbeats during its flight toward the far post for three seconds.",
  "expected_result": {
    "description": "The owl's wingbeat cadence increases for three seconds along the same flight route.",
    "target_phrase": "owl flying with accelerated wingbeats"
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
      21.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The owl is airborne with both wings visible and the far post supplies a stable route reference."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_007_E2B

```json
{
  "video_id": "synthetic_object_007",
  "edit_id": "synthetic_object_007_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_007_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Flight-feather Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_owl_flight_feather_markings",
    "target_description": "the owl's dark gray flight-feather markings",
    "source_state": "The owl's extended flight feathers carry dark gray markings.",
    "desired_change": "The dark gray markings become warm brown across both visible wings."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      23.5,
      28.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 24.5 seconds, change the owl's dark gray flight-feather markings to warm brown over two seconds.",
  "expected_result": {
    "description": "The dark gray markings become warm brown across both visible wings.",
    "target_phrase": "owl with warm-brown flight-feather markings"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_007_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both wings are open and their feather markings are visible against the pale snow."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_007_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the owl's dark gray flight-feather markings on B independently of E1's change to the framing around the perched owl; both edit results must coexist in C."
  }
}
```

## synthetic_object_008

### synthetic_object_008_E1

```json
{
  "video_id": "synthetic_object_008",
  "edit_id": "synthetic_object_008_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_008.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Wingbeat-speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_hummingbird_wingbeats",
    "target_description": "the hummingbird's wingbeats",
    "source_state": "The hovering hummingbird beats its wings too rapidly for distinct downstrokes to remain visible.",
    "desired_change": "The wingbeats slow enough to show distinct downstrokes for four seconds."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      11.5,
      18.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 12.5 seconds, slow the hummingbird's wingbeats enough to show distinct downstrokes for four seconds.",
  "expected_result": {
    "description": "The wingbeats slow enough to show distinct downstrokes for four seconds.",
    "target_phrase": "hummingbird hovering with distinct downstrokes"
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
      11.5,
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The hovering bird and both blurred wings remain centered and unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_008_E2A

```json
{
  "video_id": "synthetic_object_008",
  "edit_id": "synthetic_object_008_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_008.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_hummingbird_beak_relative_to_the_flower",
    "target_description": "the hummingbird's beak tip relative to the red flower opening",
    "source_state": "The hummingbird hovers several beak-lengths away from the red flower opening.",
    "desired_change": "The beak tip is positioned one beak-length from the flower opening."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.0 seconds, position the hummingbird's beak tip one beak-length from the red flower opening.",
  "expected_result": {
    "description": "The beak tip is positioned one beak-length from the flower opening.",
    "target_phrase": "hummingbird beak one beak-length from the flower"
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
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bird, beak tip, and red tubular flower are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_008_E2B

```json
{
  "video_id": "synthetic_object_008",
  "edit_id": "synthetic_object_008_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_008_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Throat and Chest Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_hummingbird_throat_and_chest",
    "target_description": "the hummingbird's gray-white throat and chest",
    "source_state": "The hummingbird has a gray-white throat and chest.",
    "desired_change": "The throat and chest become iridescent violet."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 22.5,
    "evaluation_window_sec": [
      19.5,
      24.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 20.5 seconds, change the hummingbird's gray-white throat and chest to iridescent violet over two seconds.",
  "expected_result": {
    "description": "The throat and chest become iridescent violet.",
    "target_phrase": "hummingbird with an iridescent violet throat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_008_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.5,
      24.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The throat and chest are visible while the bird hovers beside the flowers."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_008_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the hummingbird's gray-white throat and chest on B independently of E1's change to the hummingbird's wingbeats; both edit results must coexist in C."
  }
}
```

## synthetic_object_009

### synthetic_object_009_E1

```json
{
  "video_id": "synthetic_object_009",
  "edit_id": "synthetic_object_009_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_009.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Head and Neck Feather Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_eagle_head_and_neck_feathers",
    "target_description": "the eagle's golden-brown head and neck feathers",
    "source_state": "The eagle's head and neck feathers are golden brown.",
    "desired_change": "The head and neck feathers become pale silver."
  },
  "timing": {
    "edit_point_sec": 9.5,
    "effect_start_sec": 9.5,
    "effect_end_sec": 11.5,
    "evaluation_window_sec": [
      8.5,
      13.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 9.5 seconds, change the eagle's golden-brown head and neck feathers to pale silver over two seconds.",
  "expected_result": {
    "description": "The head and neck feathers become pale silver.",
    "target_phrase": "eagle with pale-silver head and neck feathers"
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
      8.5,
      13.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The eagle's head and neck are large, sharply focused, and separated from the mountains."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_009_E2A

```json
{
  "video_id": "synthetic_object_009",
  "edit_id": "synthetic_object_009_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_009.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Neck-scratching Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_perched_eagle",
    "target_description": "the perched eagle",
    "source_state": "The eagle stands on both feet and makes only small posture adjustments.",
    "desired_change": "The eagle raises one foot and scratches the side of its neck twice."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28,
      35
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29.0 seconds, make the perched eagle raise one foot and scratch the side of its neck twice.",
  "expected_result": {
    "description": "The eagle raises one foot and scratches the side of its neck twice.",
    "target_phrase": "perched eagle scratching its neck twice"
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
      28,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The eagle's full body, feet, and neck are clearly visible on the rock ledge."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_009_E2B

```json
{
  "video_id": "synthetic_object_009",
  "edit_id": "synthetic_object_009_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_009_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "a_small_weathered_branch",
    "target_description": "one small weathered branch on the rock",
    "source_state": "No branch lies on the exposed rock immediately to the eagle's right.",
    "desired_change": "One small weathered branch appears on the rock immediately to the eagle's right."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 21,
    "evaluation_window_sec": [
      19,
      23
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 20.0 seconds, add one small weathered branch on the exposed rock immediately to the eagle's right.",
  "expected_result": {
    "description": "One small weathered branch appears on the rock immediately to the eagle's right.",
    "target_phrase": "small weathered branch beside the eagle"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_009_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
      23
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The open rock surface beside the eagle provides a stable, unoccupied placement area."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_009_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes one small weathered branch on the rock on B independently of E1's change to the eagle's golden-brown head and neck feathers; both edit results must coexist in C."
  }
}
```

## synthetic_object_010

### synthetic_object_010_E1

```json
{
  "video_id": "synthetic_object_010",
  "edit_id": "synthetic_object_010_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_010.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "a_rounded_pale_gray_rock",
    "target_description": "one rounded pale-gray rock on the ice",
    "source_state": "The open ice one body-length behind the penguin contains no separate rock.",
    "desired_change": "One rounded pale-gray rock appears on the ice one body-length behind the penguin."
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
  "instruction": "At 14.0 seconds, add one rounded pale-gray rock on the ice one body-length behind the penguin.",
  "expected_result": {
    "description": "One rounded pale-gray rock appears on the ice one body-length behind the penguin.",
    "target_phrase": "rounded pale-gray rock behind the penguin"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13,
      17
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The penguin and broad unoccupied ice surface behind it are both clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_010_E2A

```json
{
  "video_id": "synthetic_object_010",
  "edit_id": "synthetic_object_010_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_010.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Elevated Three-quarter Camera Move",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_view_of_the_penguin",
    "target_description": "the camera view of the penguin and ice edge",
    "source_state": "The penguin is observed from a mostly fixed side view near the water.",
    "desired_change": "The camera moves smoothly to a higher three-quarter view of the penguin and ice edge."
  },
  "timing": {
    "edit_point_sec": 33,
    "effect_start_sec": 33,
    "effect_end_sec": 38,
    "evaluation_window_sec": [
      32,
      40
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 33.0 seconds, move the camera smoothly to a higher three-quarter view of the penguin and ice edge.",
  "expected_result": {
    "description": "The camera moves smoothly to a higher three-quarter view of the penguin and ice edge.",
    "target_phrase": "higher three-quarter view of the penguin"
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
      32,
      40
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stationary penguin, ice edge, and water provide stable geometry for the viewpoint change."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_010_E2B

```json
{
  "video_id": "synthetic_object_010",
  "edit_id": "synthetic_object_010_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_010_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Beak-to-water Interaction",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_penguin_beak_and_water",
    "target_description": "the penguin's beak and the water below the ice edge",
    "source_state": "The penguin watches the water without making a clear beak contact.",
    "desired_change": "The penguin lowers its head and taps the water surface twice with its beak tip."
  },
  "timing": {
    "edit_point_sec": 26.5,
    "effect_start_sec": 26.5,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      25.5,
      32
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 26.5 seconds, make the penguin lower its head and tap the water surface twice with its beak tip.",
  "expected_result": {
    "description": "The penguin lowers its head and taps the water surface twice with its beak tip.",
    "target_phrase": "penguin tapping the water twice with its beak"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_010_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25.5,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The head, pointed beak, ice edge, and water surface are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_010_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the penguin's beak and the water below the ice edge on B independently of E1's change to one rounded pale-gray rock on the ice; both edit results must coexist in C."
  }
}
```

## synthetic_object_011

### synthetic_object_011_E1

```json
{
  "video_id": "synthetic_object_011",
  "edit_id": "synthetic_object_011_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_011.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Head and Neck Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_giraffe_head_and_neck_orientation",
    "target_description": "the giraffe's head and neck orientation",
    "source_state": "The giraffe's head and neck point mainly to the right in side profile.",
    "desired_change": "The giraffe turns its head and upper neck toward the camera while its body remains right-facing."
  },
  "timing": {
    "edit_point_sec": 16.5,
    "effect_start_sec": 16.5,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      15.5,
      20
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "Starting at 16.5 seconds, turn the giraffe's head and upper neck to face the camera over the next 1.5 seconds.",
  "expected_result": {
    "description": "The giraffe turns its head and upper neck toward the camera while its body remains right-facing.",
    "target_phrase": "giraffe looking toward the camera"
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
      15.5,
      20
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The giraffe's body, long neck, head, and right-facing body axis remain identifiable near the tree."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_011_E2A

```json
{
  "video_id": "synthetic_object_011",
  "edit_id": "synthetic_object_011_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_011.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Grass Color Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_grass_around_the_giraffe",
    "target_description": "the dry grass immediately around the giraffe",
    "source_state": "The grass immediately around the giraffe is dry yellow-brown.",
    "desired_change": "The local grass becomes fresh green while retaining its short grassy texture."
  },
  "timing": {
    "edit_point_sec": 35,
    "effect_start_sec": 35,
    "effect_end_sec": 37,
    "evaluation_window_sec": [
      34,
      39
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 35.0 seconds, change the dry grass immediately around the giraffe to fresh green over two seconds.",
  "expected_result": {
    "description": "The local grass becomes fresh green while retaining its short grassy texture.",
    "target_phrase": "fresh green grass around the giraffe"
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
      34,
      39
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The giraffe stands in an open patch where the surrounding grass is clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_011_E2B

```json
{
  "video_id": "synthetic_object_011",
  "edit_id": "synthetic_object_011_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_011_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_large_fallen_diagonal_branch",
    "target_description": "the large fallen diagonal branch left of the giraffe and tree",
    "source_state": "A large dark fallen branch lies diagonally across the ground left of the giraffe.",
    "desired_change": "The large fallen diagonal branch is removed from the scene."
  },
  "timing": {
    "edit_point_sec": 22,
    "effect_start_sec": 22,
    "effect_end_sec": 23,
    "evaluation_window_sec": [
      21,
      25
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 22.0 seconds, remove the large fallen diagonal branch lying left of the giraffe and tree.",
  "expected_result": {
    "description": "The large fallen diagonal branch is removed from the scene.",
    "target_phrase": "ground without the large fallen diagonal branch"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_011_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21,
      25
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The fallen branch is isolated against pale grass and remains distinct from the standing tree."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_011_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large fallen diagonal branch left of the giraffe and tree on B independently of E1's change to the giraffe's head and neck orientation; both edit results must coexist in C."
  }
}
```

## synthetic_object_012

### synthetic_object_012_E1

```json
{
  "video_id": "synthetic_object_012",
  "edit_id": "synthetic_object_012_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_012.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "a_small_blue_rubber_ball",
    "target_description": "one small blue rubber ball floating at the puddle's left edge",
    "source_state": "No ball is present at the left edge of the puddle.",
    "desired_change": "One small blue rubber ball floats at the puddle's left edge."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      10.5,
      14.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 11.5 seconds, add one small blue rubber ball floating at the left edge of the puddle.",
  "expected_result": {
    "description": "One small blue rubber ball floats at the puddle's left edge.",
    "target_phrase": "small blue rubber ball in the puddle"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      10.5,
      14.5
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The puddle, its left boundary, and the dog are all clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_012_E2A

```json
{
  "video_id": "synthetic_object_012",
  "edit_id": "synthetic_object_012_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_012.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Grass-scraping Interaction",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_dog_forepaw_and_grass",
    "target_description": "the dog's forepaw and the grass beneath it",
    "source_state": "The dog walks and sniffs the grass without a distinct scraping action.",
    "desired_change": "The dog scrapes the grass twice with one forepaw."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 39,
    "evaluation_window_sec": [
      34.5,
      41
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 35.5 seconds, make the dog scrape the grass twice with one visible forepaw.",
  "expected_result": {
    "description": "The dog scrapes the grass twice with one forepaw.",
    "target_phrase": "dog scraping the grass twice"
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
      34.5,
      41
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dog is fully visible on open grass with its forepaws unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_012_E2B

```json
{
  "video_id": "synthetic_object_012",
  "edit_id": "synthetic_object_012_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_012_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Low Side Tracking",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_beside_the_walking_dog",
    "target_description": "the camera trajectory beside the walking dog",
    "source_state": "The camera observes the walking dog from an offset roadside view.",
    "desired_change": "The camera tracks at a low side angle alongside the dog for five seconds."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      24.5,
      32.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 25.5 seconds, track alongside the walking dog from a low side angle for five seconds.",
  "expected_result": {
    "description": "The camera tracks at a low side angle alongside the dog for five seconds.",
    "target_phrase": "low side-tracking view of the walking dog"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_012_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The walking dog and parallel track edge provide continuous references for lateral camera travel."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_012_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera trajectory beside the walking dog on B independently of E1's change to one small blue rubber ball floating at the puddle's left edge; both edit results must coexist in C."
  }
}
```

## synthetic_object_013

### synthetic_object_013_E1

```json
{
  "video_id": "synthetic_object_013",
  "edit_id": "synthetic_object_013_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Fur Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_kangaroo_body_fur",
    "target_description": "the kangaroo's medium-brown body fur",
    "source_state": "The kangaroo has medium-brown body fur with a lighter underside.",
    "desired_change": "The body fur becomes sandy beige while retaining the lighter underside."
  },
  "timing": {
    "edit_point_sec": 16.5,
    "effect_start_sec": 16.5,
    "effect_end_sec": 18.5,
    "evaluation_window_sec": [
      15.5,
      20.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 16.5 seconds, change the kangaroo's medium-brown body fur to sandy beige over two seconds.",
  "expected_result": {
    "description": "The body fur becomes sandy beige while retaining the lighter underside.",
    "target_phrase": "kangaroo with sandy-beige body fur"
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
      15.5,
      20.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The kangaroo's side profile is unobstructed against the grassland background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_013_E2A

```json
{
  "video_id": "synthetic_object_013",
  "edit_id": "synthetic_object_013_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_013.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Bronze-sculpture Rendering",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_kangaroo_only",
    "target_description": "the kangaroo only",
    "source_state": "The kangaroo is rendered photographically like the surrounding grassland.",
    "desired_change": "Only the kangaroo is rendered as a bronze sculpture."
  },
  "timing": {
    "edit_point_sec": 35,
    "effect_start_sec": 35,
    "effect_end_sec": 37,
    "evaluation_window_sec": [
      34,
      39
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 35.0 seconds, render only the kangaroo as a bronze sculpture over the next two seconds.",
  "expected_result": {
    "description": "Only the kangaroo is rendered as a bronze sculpture.",
    "target_phrase": "bronze-sculpture kangaroo in a photographic grassland"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
      39
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The kangaroo is fully visible and well separated from the background for a local treatment."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_013_E2B

```json
{
  "video_id": "synthetic_object_013",
  "edit_id": "synthetic_object_013_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_013_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Hopping-speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_kangaroo_hopping_cadence",
    "target_description": "the kangaroo's hopping cadence",
    "source_state": "The kangaroo advances with a moderate hopping cadence.",
    "desired_change": "The hopping cadence accelerates into faster bounds for five seconds along the same route."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      29,
      37
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 30.0 seconds, accelerate the kangaroo's hopping cadence into faster bounds along the same route for five seconds.",
  "expected_result": {
    "description": "The hopping cadence accelerates into faster bounds for five seconds along the same route.",
    "target_phrase": "kangaroo making faster bounds"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_013_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full kangaroo and its ground trajectory are visible in a continuous tracking shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_013_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the kangaroo's hopping cadence on B independently of E1's change to the kangaroo's medium-brown body fur; both edit results must coexist in C."
  }
}
```

## synthetic_object_014

### synthetic_object_014_E1

```json
{
  "video_id": "synthetic_object_014",
  "edit_id": "synthetic_object_014_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_014.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Tail-swing Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_panda_tail",
    "target_description": "the red panda's long tail",
    "source_state": "The red panda climbs while its long tail follows with small passive movement.",
    "desired_change": "The red panda holds position and swings its tail through three broad side-to-side arcs."
  },
  "timing": {
    "edit_point_sec": 11,
    "effect_start_sec": 11,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      10,
      17
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 11.0 seconds, make the red panda hold position and swing its long tail through three broad side-to-side arcs.",
  "expected_result": {
    "description": "The red panda holds position and swings its tail through three broad side-to-side arcs.",
    "target_phrase": "red panda swinging its tail in three broad arcs"
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
      10,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The panda's long tail and the supporting trunk are visible against the pale background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_014_E2A

```json
{
  "video_id": "synthetic_object_014",
  "edit_id": "synthetic_object_014_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_014.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_thin_leafless_branch",
    "target_description": "the thin leafless branch rising behind the red panda",
    "source_state": "A thin leafless branch rises behind the red panda and main sloping branch.",
    "desired_change": "The leafless branch is replaced by a leafy green branch of the same size and position."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      30.5,
      34.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.5 seconds, replace the thin leafless branch rising behind the red panda with a leafy green branch.",
  "expected_result": {
    "description": "The leafless branch is replaced by a leafy green branch of the same size and position.",
    "target_phrase": "leafy green branch behind the red panda"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The thin branch is silhouetted against the pale sky and separable from the main support."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_014_E2B

```json
{
  "video_id": "synthetic_object_014",
  "edit_id": "synthetic_object_014_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_014_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Bark Surface State Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_main_sloping_branch_bark",
    "target_description": "the bark on the main sloping branch beneath the red panda",
    "source_state": "The bark on the main supporting branch is dry and matte.",
    "desired_change": "The bark becomes freshly wet, darker, and mildly reflective."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 22.5,
    "evaluation_window_sec": [
      19.5,
      24.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 20.5 seconds, change the dry bark beneath the red panda to a freshly wet darker state over two seconds.",
  "expected_result": {
    "description": "The bark becomes freshly wet, darker, and mildly reflective.",
    "target_phrase": "freshly wet dark bark beneath the red panda"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_014_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.5,
      24.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The main sloping branch is broad, exposed, and continuously supports the red panda."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_014_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the bark on the main sloping branch beneath the red panda on B independently of E1's change to the red panda's long tail; both edit results must coexist in C."
  }
}
```

## synthetic_object_015

### synthetic_object_015_E1

```json
{
  "video_id": "synthetic_object_015",
  "edit_id": "synthetic_object_015_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_floating_otter",
    "target_description": "the floating otter",
    "source_state": "The otter floats to the left-front side of the flat pale rock.",
    "desired_change": "The otter is repositioned to the rock's right side, one body-length away."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      11,
      15
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 12.0 seconds, move the floating otter to the right side of the flat pale rock, one body-length away.",
  "expected_result": {
    "description": "The otter is repositioned to the rock's right side, one body-length away.",
    "target_phrase": "otter floating one body-length right of the rock"
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
      11,
      15
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The otter, complete rock outline, and open water on both sides are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_015_E2A

```json
{
  "video_id": "synthetic_object_015",
  "edit_id": "synthetic_object_015_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_015.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Held-object Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_pale_rounded_object",
    "target_description": "the pale rounded object held near the otter's mouth",
    "source_state": "The rounded object is pale white with a faint pink edge.",
    "desired_change": "The rounded object becomes deep coral red."
  },
  "timing": {
    "edit_point_sec": 36.5,
    "effect_start_sec": 36.5,
    "effect_end_sec": 38.5,
    "evaluation_window_sec": [
      35.5,
      40.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 36.5 seconds, change the pale rounded object held near the otter's mouth to deep coral red over two seconds.",
  "expected_result": {
    "description": "The rounded object becomes deep coral red.",
    "target_phrase": "deep coral-red rounded object"
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
      35.5,
      40.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The otter holds the rounded object above water near its mouth and chest."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_015_E2B

```json
{
  "video_id": "synthetic_object_015",
  "edit_id": "synthetic_object_015_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_015_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Water-ripple Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_water_ripples_around_the_submerged_otter",
    "target_description": "the water ripples around the submerged otter",
    "source_state": "The water above the submerged otter has only weak irregular disturbance.",
    "desired_change": "Tight concentric ripples expand from the otter's submerged position for four seconds."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      23,
      30
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 24.0 seconds, make tight concentric ripples expand around the submerged otter for four seconds.",
  "expected_result": {
    "description": "Tight concentric ripples expand from the otter's submerged position for four seconds.",
    "target_phrase": "concentric ripples around the submerged otter"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_015_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      30
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The submerged body shadow and surrounding open water are visible near the edit point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_015_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the water ripples around the submerged otter on B independently of E1's change to the floating otter; both edit results must coexist in C."
  }
}
```

## synthetic_object_016

### synthetic_object_016_E1

```json
{
  "video_id": "synthetic_object_016",
  "edit_id": "synthetic_object_016_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_016.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_rounded_ochre_rock",
    "target_description": "the rounded ochre rock beside the animal's water entry point",
    "source_state": "A rounded ochre rock occupies the water beside the entry point and obscures part of the animal.",
    "desired_change": "The rounded ochre rock is removed, exposing continuous open water."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      12.5,
      16.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13.5 seconds, remove the rounded ochre rock beside the animal's water entry point.",
  "expected_result": {
    "description": "The rounded ochre rock is removed, exposing continuous open water.",
    "target_phrase": "open water without the rounded ochre rock"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rounded rock is large, isolated, and clearly outlined against the water."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_016_E2A

```json
{
  "video_id": "synthetic_object_016",
  "edit_id": "synthetic_object_016_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_016.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Circling Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_right_side_seal_shaped_animal",
    "target_description": "the seal-shaped animal on the right side of the rock",
    "source_state": "The right-side animal raises its head and swims slowly without circling the rock.",
    "desired_change": "The animal swims one tight clockwise circle around the rounded ochre rock."
  },
  "timing": {
    "edit_point_sec": 36.5,
    "effect_start_sec": 36.5,
    "effect_end_sec": 41,
    "evaluation_window_sec": [
      35.5,
      43
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 36.5 seconds, make the right-side seal-shaped animal swim one tight clockwise circle around the rounded ochre rock.",
  "expected_result": {
    "description": "The animal swims one tight clockwise circle around the rounded ochre rock.",
    "target_phrase": "seal-shaped animal circling the ochre rock"
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
      35.5,
      43
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right-side head, rounded rock, and surrounding water are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_016_E2B

```json
{
  "video_id": "synthetic_object_016",
  "edit_id": "synthetic_object_016_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_016_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Water-wake Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_wakes_behind_the_left_moving_animal",
    "target_description": "the water wakes behind the left-moving submerged animal",
    "source_state": "The left-moving submerged animal produces only a weak surface trace.",
    "desired_change": "Two broad trailing wakes form behind the animal for four seconds."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      23,
      30
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 24.0 seconds, create two broad trailing wakes behind the left-moving submerged animal for four seconds.",
  "expected_result": {
    "description": "Two broad trailing wakes form behind the animal for four seconds.",
    "target_phrase": "two broad wakes behind the submerged animal"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_016_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      30
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The long submerged body and open water behind its travel direction remain visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_016_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the water wakes behind the left-moving submerged animal on B independently of E1's change to the rounded ochre rock beside the animal's water entry point; both edit results must coexist in C."
  }
}
```

## synthetic_object_017

### synthetic_object_017_E1

```json
{
  "video_id": "synthetic_object_017",
  "edit_id": "synthetic_object_017_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Coat Wetness State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_goat_coat",
    "target_description": "the goat's dry gray-brown coat",
    "source_state": "The goat's coat is dry, full, and softly textured.",
    "desired_change": "The coat becomes visibly wet and flatter against the body."
  },
  "timing": {
    "edit_point_sec": 17,
    "effect_start_sec": 17,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      16,
      21
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 17.0 seconds, change the goat's dry gray-brown coat to a visibly wet flattened state over two seconds.",
  "expected_result": {
    "description": "The coat becomes visibly wet and flatter against the body.",
    "target_phrase": "goat with a wet flattened coat"
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
      16,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The goat's torso and coat texture are unobstructed against the mountain background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_017_E2A

```json
{
  "video_id": "synthetic_object_017",
  "edit_id": "synthetic_object_017_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_017.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Rearing Motion",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_mountain_goat",
    "target_description": "the mountain goat",
    "source_state": "The goat walks steadily on all four legs across the rock ledge.",
    "desired_change": "The goat rears once onto its hind legs and returns to the ledge."
  },
  "timing": {
    "edit_point_sec": 36,
    "effect_start_sec": 36,
    "effect_end_sec": 40,
    "evaluation_window_sec": [
      35,
      42
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 36.0 seconds, make the mountain goat rear once onto its hind legs and return to the rock ledge.",
  "expected_result": {
    "description": "The goat rears once onto its hind legs and returns to the ledge.",
    "target_phrase": "mountain goat rearing once"
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
      35,
      42
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The goat's full body and broad supporting rock ledge are clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_017_E2B

```json
{
  "video_id": "synthetic_object_017",
  "edit_id": "synthetic_object_017_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_017_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Gait Speed Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_goat_forward_gait",
    "target_description": "the goat's forward gait",
    "source_state": "The goat crosses the rock ledge at a steady walk.",
    "desired_change": "The goat changes from walking to a brisk trot for five seconds along the same ledge."
  },
  "timing": {
    "edit_point_sec": 22.5,
    "effect_start_sec": 22.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      21.5,
      29.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 22.5 seconds, change the goat's steady walk into a brisk trot along the same ledge for five seconds.",
  "expected_result": {
    "description": "The goat changes from walking to a brisk trot for five seconds along the same ledge.",
    "target_phrase": "goat trotting briskly along the ledge"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_017_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The goat's legs and continuous rock surface remain visible for gait evaluation."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_017_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the goat's forward gait on B independently of E1's change to the goat's dry gray-brown coat; both edit results must coexist in C."
  }
}
```

## synthetic_object_018

### synthetic_object_018_E1

```json
{
  "video_id": "synthetic_object_018",
  "edit_id": "synthetic_object_018_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_018.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_oval_gray_stone",
    "target_description": "the oval gray stone behind the rabbit",
    "source_state": "An oval gray stone rests behind the rabbit beside the hollow log.",
    "desired_change": "The oval gray stone is replaced by a small red rubber ball in the same position."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13.0 seconds, replace the oval gray stone behind the rabbit with a small red rubber ball.",
  "expected_result": {
    "description": "The oval gray stone is replaced by a small red rubber ball in the same position.",
    "target_phrase": "small red rubber ball behind the rabbit"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The oval stone is fully visible and spatially separated from the rabbit and hollow log."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_018_E2A

```json
{
  "video_id": "synthetic_object_018",
  "edit_id": "synthetic_object_018_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_018.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_white_rabbit",
    "target_description": "the white rabbit",
    "source_state": "The rabbit occupies the center-right area beneath the horizontal log.",
    "desired_change": "The rabbit is repositioned onto the open grass in the left third of the frame."
  },
  "timing": {
    "edit_point_sec": 33,
    "effect_start_sec": 33,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      32,
      36
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 33.0 seconds, move the white rabbit onto the open grass in the left third of the frame.",
  "expected_result": {
    "description": "The rabbit is repositioned onto the open grass in the left third of the frame.",
    "target_phrase": "white rabbit in the left third of the frame"
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
      32,
      36
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full rabbit and open grass destination to its left are clearly visible beneath the log."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_018_E2B

```json
{
  "video_id": "synthetic_object_018",
  "edit_id": "synthetic_object_018_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_018_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Inner-ear Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_rabbit_inner_ears",
    "target_description": "the rabbit's pink inner ears",
    "source_state": "The rabbit has pale pink inner ears.",
    "desired_change": "Both inner ears become pale blue."
  },
  "timing": {
    "edit_point_sec": 21,
    "effect_start_sec": 21,
    "effect_end_sec": 23,
    "evaluation_window_sec": [
      20,
      25
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 21.0 seconds, change both of the rabbit's pale pink inner ears to pale blue over two seconds.",
  "expected_result": {
    "description": "Both inner ears become pale blue.",
    "target_phrase": "rabbit with pale-blue inner ears"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_018_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20,
      25
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both upright ears and their pink inner surfaces are clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_018_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the rabbit's pink inner ears on B independently of E1's change to the oval gray stone behind the rabbit; both edit results must coexist in C."
  }
}
```

## synthetic_object_019

### synthetic_object_019_E1

```json
{
  "video_id": "synthetic_object_019",
  "edit_id": "synthetic_object_019_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Pause and Resume",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_hedgehog_curling_process",
    "target_description": "the hedgehog's upcoming curling process",
    "source_state": "The hedgehog begins curling around 21 seconds and continues directly into a compact ball.",
    "desired_change": "The process pauses halfway curled for three seconds and then resumes to completion."
  },
  "timing": {
    "edit_point_sec": 18.5,
    "effect_start_sec": 21,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      17.5,
      29
    ],
    "temporal_behavior": "temporary process pause"
  },
  "instruction": "Starting at 18.5 seconds, delay the hedgehog's upcoming curl halfway through for three seconds, then resume the same curling process.",
  "expected_result": {
    "description": "The process pauses halfway curled for three seconds and then resumes to completion.",
    "target_phrase": "hedgehog pausing halfway through curling"
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
      17.5,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The uncurling source posture, contraction, and compact-ball milestone occur continuously without a cut."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_019_E2A

```json
{
  "video_id": "synthetic_object_019",
  "edit_id": "synthetic_object_019_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_019.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_thin_foreground_twig",
    "target_description": "the thin twig crossing the foreground soil",
    "source_state": "A thin twig crosses the lower foreground in front of the hedgehog.",
    "desired_change": "The twig is moved to the upper-left edge of the visible soil patch."
  },
  "timing": {
    "edit_point_sec": 36.5,
    "effect_start_sec": 36.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      35.5,
      39.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 36.5 seconds, move the thin foreground twig to the upper-left edge of the visible soil patch.",
  "expected_result": {
    "description": "The twig is moved to the upper-left edge of the visible soil patch.",
    "target_phrase": "foreground twig at the upper-left soil edge"
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
      35.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete twig and destination soil edge are both visible around the expanded hedgehog."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_019_E2B

```json
{
  "video_id": "synthetic_object_019",
  "edit_id": "synthetic_object_019_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_019_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Spine Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_curled_hedgehog_spines",
    "target_description": "the curled hedgehog's brown spines",
    "source_state": "The curled hedgehog has brown spines with lighter tips.",
    "desired_change": "The spines become warm gray while retaining their lighter tips."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 33.5,
    "evaluation_window_sec": [
      30.5,
      35.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31.5 seconds, change the curled hedgehog's brown spines to warm gray over two seconds.",
  "expected_result": {
    "description": "The spines become warm gray while retaining their lighter tips.",
    "target_phrase": "curled hedgehog with warm-gray spines"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_019_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.5,
      35.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The compact curled body fills the frame and the spine field is unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_019_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the curled hedgehog's brown spines on B independently of E1's change to the hedgehog's upcoming curling process; both edit results must coexist in C."
  }
}
```

## synthetic_object_020

### synthetic_object_020_E1

```json
{
  "video_id": "synthetic_object_020",
  "edit_id": "synthetic_object_020_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Eyespot Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_peacock_tail_eyespots",
    "target_description": "the green-blue centers of the peacock's tail eyespots",
    "source_state": "The tail eyespots have green-blue centers across the open fan.",
    "desired_change": "The eyespot centers become copper-red across the full fan."
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
  "instruction": "Starting at 15.0 seconds, change the green-blue centers of the peacock's tail eyespots to copper-red over two seconds.",
  "expected_result": {
    "description": "The eyespot centers become copper-red across the full fan.",
    "target_phrase": "peacock fan with copper-red eyespot centers"
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
      14,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete open fan and repeated eyespot centers are clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_020_E2A

```json
{
  "video_id": "synthetic_object_020",
  "edit_id": "synthetic_object_020_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_020.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relational Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_gray_rock_relative_to_the_peacock_fan",
    "target_description": "the large gray rock relative to the peacock's tail fan",
    "source_state": "The large gray rock sits in the right background near the fan edge.",
    "desired_change": "The rock is moved to one peacock-width left of the tail fan while remaining fully visible."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      31,
      35
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32.0 seconds, move the large gray rock to a position one peacock-width left of the tail fan.",
  "expected_result": {
    "description": "The rock is moved to one peacock-width left of the tail fan while remaining fully visible.",
    "target_phrase": "gray rock one peacock-width left of the fan"
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
      31,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The entire fan, right-side rock, and open ground to the left are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_020_E2B

```json
{
  "video_id": "synthetic_object_020",
  "edit_id": "synthetic_object_020_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_020_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Matte-tone Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_peacock_scene",
    "target_description": "the full peacock display scene",
    "source_state": "The scene has crisp photographic contrast and naturally glossy feather rendering.",
    "desired_change": "The scene gains a soft matte finish with gently reduced contrast."
  },
  "timing": {
    "edit_point_sec": 22,
    "effect_start_sec": 22,
    "effect_end_sec": 24,
    "evaluation_window_sec": [
      21,
      26
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 22.0 seconds, give the full peacock display scene a soft matte finish with gently reduced contrast over two seconds.",
  "expected_result": {
    "description": "The scene gains a soft matte finish with gently reduced contrast.",
    "target_phrase": "soft matte peacock scene with reduced contrast"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_020_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21,
      26
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The peacock, open fan, forest floor, trees, and gray rock are all continuously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_020_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full peacock display scene on B independently of E1's change to the green-blue centers of the peacock's tail eyespots; both edit results must coexist in C."
  }
}
```

## synthetic_object_021

### synthetic_object_021_E1

```json
{
  "video_id": "synthetic_object_021",
  "edit_id": "synthetic_object_021_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_021.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_sports_car",
    "target_description": "the red sports car",
    "source_state": "The red sports car follows the wet mountain bend without a distinct lateral slide.",
    "desired_change": "The car performs one controlled fishtail through the bend and then straightens within its lane."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      10.5,
      17.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 11.5 seconds, make the red sports car perform one controlled fishtail through the wet bend before straightening.",
  "expected_result": {
    "description": "The car performs one controlled fishtail through the bend and then straightens within its lane.",
    "target_phrase": "one controlled fishtail through the bend"
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
      10.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The entire car, wet lane boundaries, and curved road are continuously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_021_E2A

```json
{
  "video_id": "synthetic_object_021",
  "edit_id": "synthetic_object_021_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_021.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Global Tone and Texture Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_wet_mountain_road_scene",
    "target_description": "the full wet mountain-road scene",
    "source_state": "The scene has natural cool daylight colors and neutral road reflections.",
    "desired_change": "The full scene acquires a cool cyan-and-silver cinematic grade with crisp wet-road reflections."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 31 seconds, grade the full wet mountain-road scene with cool cyan-and-silver tones over the next two seconds.",
  "expected_result": {
    "description": "The full scene acquires a cool cyan-and-silver cinematic grade with crisp wet-road reflections.",
    "target_phrase": "cool cyan-and-silver mountain-road scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The car, wet road, guardrails, trees, and distant hills are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_021_E2B

```json
{
  "video_id": "synthetic_object_021",
  "edit_id": "synthetic_object_021_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_021_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing_around_the_sports_car",
    "target_description": "the camera framing around the sports car",
    "source_state": "The sports car occupies roughly one third of the frame during the close front-side follow shot.",
    "desired_change": "The camera smoothly widens until the car occupies roughly one fifth of the frame."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      23.5,
      30.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 24.5 seconds, smoothly zoom out until the red sports car occupies roughly one fifth of the frame.",
  "expected_result": {
    "description": "The camera smoothly widens until the car occupies roughly one fifth of the frame.",
    "target_phrase": "sports car occupying one fifth of the frame"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_021_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The car is fully visible near frame center with ample road and forest surrounding it."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_021_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera framing around the sports car on B independently of E1's change to the red sports car; both edit results must coexist in C."
  }
}
```

## synthetic_object_022

### synthetic_object_022_E1

```json
{
  "video_id": "synthetic_object_022",
  "edit_id": "synthetic_object_022_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_022.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_off_road_vehicle_body_panels",
    "target_description": "the off-road vehicle body panels",
    "source_state": "The vehicle has saturated blue body panels with black trim.",
    "desired_change": "The blue body panels become deep forest green while the black trim remains distinct."
  },
  "timing": {
    "edit_point_sec": 10.5,
    "effect_start_sec": 10.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      9.5,
      14.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 10.5 seconds, change the off-road vehicle's blue body panels to deep forest green over two seconds.",
  "expected_result": {
    "description": "The blue body panels become deep forest green while the black trim remains distinct.",
    "target_phrase": "deep forest-green off-road vehicle"
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
      9.5,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The vehicle is fully visible in rear-side view against the pale hillside."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_022_E2A

```json
{
  "video_id": "synthetic_object_022",
  "edit_id": "synthetic_object_022_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_022.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_rear_mounted_spare_wheel",
    "target_description": "the rear-mounted spare wheel",
    "source_state": "A full-size spare wheel is mounted centrally on the rear door.",
    "desired_change": "The spare wheel is replaced by a dark rectangular expedition fuel canister of comparable size."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      30.5,
      34.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.5 seconds, replace the rear-mounted spare wheel with a dark rectangular expedition fuel canister of comparable size.",
  "expected_result": {
    "description": "The spare wheel is replaced by a dark rectangular expedition fuel canister of comparable size.",
    "target_phrase": "rear expedition fuel canister"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rear door and centrally mounted spare wheel are unobstructed in the selected view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_022_E2B

```json
{
  "video_id": "synthetic_object_022",
  "edit_id": "synthetic_object_022_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_022_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_off_road_vehicle",
    "target_description": "the off-road vehicle",
    "source_state": "The vehicle continues smoothly along the paired dirt tracks after cresting the hill.",
    "desired_change": "The vehicle makes one short suspension bounce over the next rise and continues forward."
  },
  "timing": {
    "edit_point_sec": 23.5,
    "effect_start_sec": 23.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      22.5,
      29.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 23.5 seconds, make the off-road vehicle perform one short suspension bounce over the next dirt-track rise.",
  "expected_result": {
    "description": "The vehicle makes one short suspension bounce over the next rise and continues forward.",
    "target_phrase": "one short suspension bounce"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_022_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full vehicle, wheels, paired tracks, and approaching rise remain visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_022_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the off-road vehicle on B independently of E1's change to the off-road vehicle body panels; both edit results must coexist in C."
  }
}
```

## synthetic_object_023

### synthetic_object_023_E1

```json
{
  "video_id": "synthetic_object_023",
  "edit_id": "synthetic_object_023_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Bus-door Opening Motion",
    "scope": "Core Object Components"
  },
  "target": {
    "target_id": "the_two_visible_closed_side_doors_on_the_bus",
    "target_description": "the two visible closed side doors on the bus",
    "source_state": "Both visible side doors are closed as the bus travels beside the platform.",
    "desired_change": "The two visible side doors swing fully open over two seconds."
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
  "instruction": "Starting at 14 seconds, make the two visible closed side doors on the bus swing fully open over the next two seconds.",
  "expected_result": {
    "description": "The two visible side doors swing fully open over two seconds.",
    "target_phrase": "two visible bus doors fully open"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "bus identity, body geometry, travel trajectory, and platform relationship"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
    "description": "The broadside bus view keeps both closed door assemblies continuously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_023_E2A

```json
{
  "video_id": "synthetic_object_023",
  "edit_id": "synthetic_object_023_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_023.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "License-plate Relational Repositioning",
    "scope": "Core Object Components"
  },
  "target": {
    "target_id": "the_yellow_rear_license_plate_relative_to_the_black_rear_panel",
    "target_description": "the yellow rear license plate relative to the black rear panel",
    "source_state": "The yellow license plate sits below the vertical center of the black rear panel.",
    "desired_change": "The license plate is moved upward until it is vertically centered within the black rear panel."
  },
  "timing": {
    "edit_point_sec": 21.5,
    "effect_start_sec": 21.5,
    "effect_end_sec": 22.5,
    "evaluation_window_sec": [
      20.5,
      24.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 21.5 seconds, move the yellow rear license plate upward to the vertical center of the black rear panel.",
  "expected_result": {
    "description": "The license plate is moved upward until it is vertically centered within the black rear panel.",
    "target_phrase": "yellow license plate centered in the black rear panel"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "target boundary: Only the yellow license plate's placement is editable; its existing characters and all other vehicle text remain protected."
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20.5,
      24.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The yellow plate and surrounding black rear panel are clearly separated in the stable rear view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_023_E2B

```json
{
  "video_id": "synthetic_object_023",
  "edit_id": "synthetic_object_023_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_023_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_around_the_stationary_bus",
    "target_description": "the camera path around the stationary bus",
    "source_state": "The camera holds a broad rear-side view while the bus remains stopped.",
    "desired_change": "The camera performs a smooth five-second dolly from the rear quarter toward the front doors."
  },
  "timing": {
    "edit_point_sec": 27.5,
    "effect_start_sec": 27.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      26.5,
      34.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 27.5 seconds, move the camera smoothly from the bus's rear quarter toward its front doors for five seconds.",
  "expected_result": {
    "description": "The camera performs a smooth five-second dolly from the rear quarter toward the front doors.",
    "target_phrase": "rear-to-front camera dolly along the bus"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_023_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stationary bus and long platform provide stable depth and trajectory references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_023_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera path around the stationary bus on B independently of E1's change to the two visible closed side doors on the bus; both edit results must coexist in C."
  }
}
```

## synthetic_object_024

### synthetic_object_024_E1

```json
{
  "video_id": "synthetic_object_024",
  "edit_id": "synthetic_object_024_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_024.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_motorcycle_fuel_tank",
    "target_description": "the motorcycle fuel tank",
    "source_state": "The motorcycle fuel tank is glossy black like the surrounding bodywork.",
    "desired_change": "The fuel tank becomes metallic burgundy while the remaining motorcycle stays black."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      11.5,
      16.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12.5 seconds, change the motorcycle's glossy black fuel tank to metallic burgundy over the next two seconds.",
  "expected_result": {
    "description": "The fuel tank becomes metallic burgundy while the remaining motorcycle stays black.",
    "target_phrase": "metallic burgundy motorcycle fuel tank"
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
      11.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tank is exposed between the rider and handlebars in a clear side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_024_E2A

```json
{
  "video_id": "synthetic_object_024",
  "edit_id": "synthetic_object_024_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_024.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Dust-to-motorcycle Interaction",
    "scope": "Core Object and Environment Material"
  },
  "target": {
    "target_id": "the_loose_yellow_roadside_dirt_and_the_motorcycle",
    "target_description": "the loose yellow roadside dirt and the motorcycle",
    "source_state": "Loose yellow dirt beside the motorcycle remains settled without striking the vehicle.",
    "desired_change": "A visible cloud of yellow dust rises from the roadside and blows against the motorcycle's lower side."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      29,
      37
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 30 seconds, make the loose yellow roadside dirt rise as dust and blow against the motorcycle's lower side for five seconds.",
  "expected_result": {
    "description": "A visible cloud of yellow dust rises from the roadside and blows against the motorcycle's lower side.",
    "target_phrase": "yellow roadside dust striking the motorcycle"
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
      29,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The motorcycle's lower side and the adjacent yellow dirt remain visible in the same continuous view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_024_E2B

```json
{
  "video_id": "synthetic_object_024",
  "edit_id": "synthetic_object_024_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_024_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_motorcycle_within_its_lane",
    "target_description": "the motorcycle within its lane",
    "source_state": "The motorcycle travels near the center of the coastal-road lane.",
    "desired_change": "The motorcycle is repositioned into the lane's inner half, one tire-width from the center line."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      23.5,
      27.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.5 seconds, reposition the motorcycle into the inner half of its lane, one tire-width from the center line.",
  "expected_result": {
    "description": "The motorcycle is repositioned into the lane's inner half, one tire-width from the center line.",
    "target_phrase": "motorcycle in the lane's inner half"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_024_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The motorcycle, center line, guardrail, and full lane width are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_024_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the motorcycle within its lane on B independently of E1's change to the motorcycle fuel tank; both edit results must coexist in C."
  }
}
```

## synthetic_object_025

### synthetic_object_025_E1

```json
{
  "video_id": "synthetic_object_025",
  "edit_id": "synthetic_object_025_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_025.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_articulated_tram_along_the_rails",
    "target_description": "the articulated tram along the rails",
    "source_state": "The articulated tram occupies a central position along the visible track segment.",
    "desired_change": "The tram is shifted one full car-length to the right along the same rails."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, shift the articulated tram one full car-length to the right along its current rails.",
  "expected_result": {
    "description": "The tram is shifted one full car-length to the right along the same rails.",
    "target_phrase": "tram shifted one car-length along the rails"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "wheel alignment with the current rails"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both articulated sections and a long uninterrupted rail segment are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_025_E2A

```json
{
  "video_id": "synthetic_object_025",
  "edit_id": "synthetic_object_025_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_025.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Tram-to-train Replacement",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_old_articulated_tram",
    "target_description": "the old articulated tram",
    "source_state": "An old articulated tram occupies the visible track beside the palace facades.",
    "desired_change": "The old articulated tram is replaced by a brand-new single-car high-speed train in the same track position and orientation."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      29,
      33
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30 seconds, replace the old articulated tram with a brand-new single-car high-speed train in the same track position.",
  "expected_result": {
    "description": "The old articulated tram is replaced by a brand-new single-car high-speed train in the same track position and orientation.",
    "target_phrase": "brand-new single-car high-speed train"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29,
      33
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete old tram and its rail placement are clearly visible against the palace background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_025_E2B

```json
{
  "video_id": "synthetic_object_025",
  "edit_id": "synthetic_object_025_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_025_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_front_pantograph_and_overhead_wire",
    "target_description": "the front pantograph and overhead wire",
    "source_state": "The front pantograph maintains steady contact with the overhead wire.",
    "desired_change": "The pantograph flexes downward and rebounds against the overhead wire twice while the tram continues forward."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      23.5,
      30.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 24.5 seconds, make the front pantograph flex downward and rebound against the overhead wire twice while moving.",
  "expected_result": {
    "description": "The pantograph flexes downward and rebounds against the overhead wire twice while the tram continues forward.",
    "target_phrase": "pantograph rebounding against the wire twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_025_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The articulated tram, front pantograph, and overhead wires are visible together."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_025_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the front pantograph and overhead wire on B independently of E1's change to the articulated tram along the rails; both edit results must coexist in C."
  }
}
```

## synthetic_object_026

### synthetic_object_026_E1

```json
{
  "video_id": "synthetic_object_026",
  "edit_id": "synthetic_object_026_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_freight_train",
    "target_description": "the freight train",
    "source_state": "The freight train advances continuously around the field-side curve.",
    "desired_change": "The freight train decelerates smoothly to a complete stop over four seconds."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 18.5,
    "evaluation_window_sec": [
      13.5,
      20.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.5 seconds, make the freight train decelerate smoothly to a complete stop along the curved track over four seconds.",
  "expected_result": {
    "description": "The freight train decelerates smoothly to a complete stop over four seconds.",
    "target_phrase": "freight train stopping on the curve"
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
      13.5,
      20.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The locomotive, several connected wagons, rails, and surrounding field are unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_026_E2A

```json
{
  "video_id": "synthetic_object_026",
  "edit_id": "synthetic_object_026_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_026.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Full-scene Animation Rendering",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_freight_train_countryside_scene",
    "target_description": "the full freight-train countryside scene",
    "source_state": "The freight train and countryside use realistic photographic rendering.",
    "desired_change": "The entire scene is transformed into a warm hand-painted animation inspired by classic Miyazaki films."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      33,
      38
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 34 seconds, transform the entire freight-train countryside scene into a warm Miyazaki-inspired hand-painted animation over two seconds.",
  "expected_result": {
    "description": "The entire scene is transformed into a warm hand-painted animation inspired by classic Miyazaki films.",
    "target_phrase": "freight-train countryside in Miyazaki-inspired animation"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The train, rails, fields, trees, and sky are simultaneously visible for a coherent global rendering change."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_026_E2B

```json
{
  "video_id": "synthetic_object_026",
  "edit_id": "synthetic_object_026_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_026_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_first_brown_hopper_wagon_behind_the_locomotive",
    "target_description": "the first brown hopper wagon behind the locomotive",
    "source_state": "A brown open-top hopper wagon directly follows the locomotive.",
    "desired_change": "That first hopper wagon is replaced by a silver cylindrical tanker wagon of equal length."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      24.5,
      28.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25.5 seconds, replace the first brown hopper wagon behind the locomotive with a silver cylindrical tanker wagon of equal length.",
  "expected_result": {
    "description": "That first hopper wagon is replaced by a silver cylindrical tanker wagon of equal length.",
    "target_phrase": "silver tanker wagon behind the locomotive"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_026_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The locomotive and first several wagons are clear in the continuous curve view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_026_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the first brown hopper wagon behind the locomotive on B independently of E1's change to the freight train; both edit results must coexist in C."
  }
}
```

## synthetic_object_027

### synthetic_object_027_E1

```json
{
  "video_id": "synthetic_object_027",
  "edit_id": "synthetic_object_027_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_silver_passenger_train_along_the_bridge",
    "target_description": "the silver passenger train along the bridge",
    "source_state": "The train is approaching the camera along the elevated bridge.",
    "desired_change": "The complete train is shifted forward by two car-lengths along the same bridge track."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      11,
      15
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 12 seconds, shift the complete silver train forward by two car-lengths along the same elevated bridge track.",
  "expected_result": {
    "description": "The complete train is shifted forward by two car-lengths along the same bridge track.",
    "target_phrase": "train shifted forward along the bridge"
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
      11,
      15
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The train and a long straight run of its bridge track are both visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_027_E2A

```json
{
  "video_id": "synthetic_object_027",
  "edit_id": "synthetic_object_027_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_027.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_river_surface_beneath_the_bridge",
    "target_description": "the river surface beneath the bridge",
    "source_state": "The river surface beneath the bridge has fine, low-amplitude ripples.",
    "desired_change": "Two broad concentric ripple bands travel outward beneath the bridge over five seconds."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 39,
    "evaluation_window_sec": [
      33,
      41
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 34 seconds, make two broad concentric ripple bands travel outward across the river beneath the bridge for five seconds.",
  "expected_result": {
    "description": "Two broad concentric ripple bands travel outward beneath the bridge over five seconds.",
    "target_phrase": "two ripple bands beneath the bridge"
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
      33,
      41
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The train is distant while a wide unobstructed river area fills the lower frame."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_027_E2B

```json
{
  "video_id": "synthetic_object_027",
  "edit_id": "synthetic_object_027_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_027_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_train_s_blue_gray_side_stripe",
    "target_description": "the train's blue-gray side stripe",
    "source_state": "The passenger train carries a blue-gray stripe along its silver body.",
    "desired_change": "The side stripe becomes deep green while the silver body and windows remain unchanged."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      23.5,
      28.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 24.5 seconds, change the passenger train's blue-gray side stripe to deep green over the next two seconds.",
  "expected_result": {
    "description": "The side stripe becomes deep green while the silver body and windows remain unchanged.",
    "target_phrase": "deep-green stripe on the silver train"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_027_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Multiple side-facing carriages and the continuous colored stripe are clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_027_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the train's blue-gray side stripe on B independently of E1's change to the silver passenger train along the bridge; both edit results must coexist in C."
  }
}
```

## synthetic_object_028

### synthetic_object_028_E1

```json
{
  "video_id": "synthetic_object_028",
  "edit_id": "synthetic_object_028_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_028.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Platform-line Removal",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_yellow_platform_edge_safety_line",
    "target_description": "the yellow platform-edge safety line",
    "source_state": "A continuous yellow safety line runs along the visible platform edge.",
    "desired_change": "The yellow platform-edge safety line is removed along the visible platform section."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      13.5,
      17.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.5 seconds, remove the yellow safety line running along the visible edge of the station platform.",
  "expected_result": {
    "description": "The yellow platform-edge safety line is removed along the visible platform section.",
    "target_phrase": "yellow platform-edge safety line removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The yellow line is clearly separated from the platform tiles and train body."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_028_E2A

```json
{
  "video_id": "synthetic_object_028",
  "edit_id": "synthetic_object_028_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_028.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_visible_passenger_doors",
    "target_description": "the visible passenger doors",
    "source_state": "The visible passenger doors are closed while the train rests beside the platform.",
    "desired_change": "The visible passenger doors remain fully open as a persistent operating state."
  },
  "timing": {
    "edit_point_sec": 29.5,
    "effect_start_sec": 29.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      28.5,
      33.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 29.5 seconds, change the visible passenger doors from closed to fully open over the next two seconds.",
  "expected_result": {
    "description": "The visible passenger doors remain fully open as a persistent operating state.",
    "target_phrase": "passenger doors held fully open"
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
      28.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Several closed door pairs are visible broadside with little train displacement."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_028_E2B

```json
{
  "video_id": "synthetic_object_028",
  "edit_id": "synthetic_object_028_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_028_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Platform-light Spacing Change",
    "scope": "Environment Objects"
  },
  "target": {
    "target_id": "all_visible_ceiling_lights_along_the_left_side_of_the_platform",
    "target_description": "all visible ceiling lights along the left side of the platform",
    "source_state": "The left-side ceiling lights form an evenly spaced row along the platform.",
    "desired_change": "The spacing between all visible left-side ceiling lights is doubled while their linear order remains unchanged."
  },
  "timing": {
    "edit_point_sec": 23,
    "effect_start_sec": 23,
    "effect_end_sec": 24,
    "evaluation_window_sec": [
      22,
      26
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 23 seconds, double the spacing between all visible ceiling lights along the left side of the platform.",
  "expected_result": {
    "description": "The spacing between all visible left-side ceiling lights is doubled while their linear order remains unchanged.",
    "target_phrase": "left platform lights at double spacing"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_028_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22,
      26
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The repeated left-side ceiling lights and their platform alignment are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_028_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes all visible ceiling lights along the left side of the platform on B independently of E1's change to the yellow platform-edge safety line; both edit results must coexist in C."
  }
}
```

## synthetic_object_029

### synthetic_object_029_E1

```json
{
  "video_id": "synthetic_object_029",
  "edit_id": "synthetic_object_029_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_029.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_convertible_relative_to_the_right_curb",
    "target_description": "the convertible relative to the right curb",
    "source_state": "The convertible travels near the center of its residential lane.",
    "desired_change": "The convertible is repositioned half a lane-width closer to the right curb."
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
  "instruction": "At 14 seconds, move the cream convertible half a lane-width closer to the right curb.",
  "expected_result": {
    "description": "The convertible is repositioned half a lane-width closer to the right curb.",
    "target_phrase": "convertible closer to the right curb"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "convertible travel direction"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
    "description": "The full vehicle, lane surface, and right curb are all visible through the tree gap."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_029_E2A

```json
{
  "video_id": "synthetic_object_029",
  "edit_id": "synthetic_object_029_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_029.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_convertible_s_forward_motion",
    "target_description": "the convertible's forward motion",
    "source_state": "The convertible continues along the residential street at a steady pace.",
    "desired_change": "The convertible travels at half its original speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      30,
      38
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 31 seconds, reduce the cream convertible's forward speed to half its original rate for five seconds.",
  "expected_result": {
    "description": "The convertible travels at half its original speed for five seconds.",
    "target_phrase": "convertible moving at half speed"
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
      30,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete car remains in a continuous side view with houses as motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_029_E2B

```json
{
  "video_id": "synthetic_object_029",
  "edit_id": "synthetic_object_029_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_029_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Rainy-weather Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_weather_across_the_residential_street",
    "target_description": "the weather across the residential street",
    "source_state": "The residential street is dry under clear daylight without visible rainfall.",
    "desired_change": "Steady rain begins under an overcast sky and visibly wets the road surface."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent weather change"
  },
  "instruction": "Starting at 25.5 seconds, change the weather across the residential street to steady rain under an overcast sky over two seconds.",
  "expected_result": {
    "description": "Steady rain begins under an overcast sky and visibly wets the road surface.",
    "target_phrase": "rainy weather over the residential street"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_029_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The sky, houses, trees, and broad road surface are visible together for assessing the weather change."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_029_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the weather across the residential street on B independently of E1's change to the convertible relative to the right curb; both edit results must coexist in C."
  }
}
```

## synthetic_object_030

### synthetic_object_030_E1

```json
{
  "video_id": "synthetic_object_030",
  "edit_id": "synthetic_object_030_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_030.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_lane_behind_the_yellow_taxi",
    "target_description": "the open lane behind the yellow taxi",
    "source_state": "No red compact car occupies the lane immediately behind the taxi.",
    "desired_change": "One red compact car is added two car-lengths behind the yellow taxi in the same lane."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, add one red compact car two car-lengths behind the yellow taxi in the same traffic lane.",
  "expected_result": {
    "description": "One red compact car is added two car-lengths behind the yellow taxi in the same lane.",
    "target_phrase": "red compact car behind the taxi"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The taxi and a stable open section of its lane are visible from the rear side."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_030_E2A

```json
{
  "video_id": "synthetic_object_030",
  "edit_id": "synthetic_object_030_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_030.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_yellow_taxi_s_forward_motion",
    "target_description": "the yellow taxi's forward motion",
    "source_state": "The yellow taxi recedes along the center lane at a steady pace.",
    "desired_change": "The taxi increases its forward speed by forty percent for five seconds."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      30,
      38
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 31 seconds, increase the yellow taxi's forward speed by forty percent along the same lane for five seconds.",
  "expected_result": {
    "description": "The taxi increases its forward speed by forty percent for five seconds.",
    "target_phrase": "taxi moving forty percent faster"
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
      30,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The taxi remains visible against lane markings and roadside poles throughout the interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_030_E2B

```json
{
  "video_id": "synthetic_object_030",
  "edit_id": "synthetic_object_030_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_030_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Auxiliary Object Style Change",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_taxi_s_roof_sign",
    "target_description": "the taxi's roof sign",
    "source_state": "The taxi carries a small opaque yellow roof sign.",
    "desired_change": "Only the roof sign is rendered as frosted translucent glass while retaining its shape."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      23,
      28
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 24 seconds, render only the yellow taxi's roof sign as frosted translucent glass over two seconds.",
  "expected_result": {
    "description": "Only the roof sign is rendered as frosted translucent glass while retaining its shape.",
    "target_phrase": "frosted translucent taxi roof sign"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_030_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The roof sign is separated clearly from the roof and sky in the close side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_030_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the taxi's roof sign on B independently of E1's change to the open lane behind the yellow taxi; both edit results must coexist in C."
  }
}
```

## synthetic_object_031

### synthetic_object_031_E1

```json
{
  "video_id": "synthetic_object_031",
  "edit_id": "synthetic_object_031_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_ambulance_s_forward_orientation",
    "target_description": "the ambulance's forward orientation",
    "source_state": "The ambulance points straight along the road lane.",
    "desired_change": "The ambulance is rotated ten degrees toward the right curb while remaining on the roadway."
  },
  "timing": {
    "edit_point_sec": 15,
    "effect_start_sec": 15,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      14,
      18
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 15 seconds, rotate the ambulance ten degrees toward the right curb.",
  "expected_result": {
    "description": "The ambulance is rotated ten degrees toward the right curb while remaining on the roadway.",
    "target_phrase": "ambulance angled toward the right curb"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "all ambulance wheels remain on the roadway"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      14,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rear, road edges, and curbward red lane provide stable orientation references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_031_E2A

```json
{
  "video_id": "synthetic_object_031",
  "edit_id": "synthetic_object_031_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_031.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Roadside-branch Motion",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_branches_of_the_roadside_trees",
    "target_description": "the branches of the roadside trees",
    "source_state": "The visible roadside tree branches remain largely still as the ambulance passes.",
    "desired_change": "The roadside tree branches sway back and forth through two wind-driven arcs."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 37,
    "evaluation_window_sec": [
      31,
      39
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 32 seconds, make the visible roadside tree branches sway back and forth through two broad wind-driven arcs over five seconds.",
  "expected_result": {
    "description": "The roadside tree branches sway back and forth through two wind-driven arcs.",
    "target_phrase": "roadside tree branches swaying twice"
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
      31,
      39
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tree crowns and branches remain visible beside the roadway in a continuous shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_031_E2B

```json
{
  "video_id": "synthetic_object_031",
  "edit_id": "synthetic_object_031_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_031_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Ambulance Weathering State Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_ambulance_exterior",
    "target_description": "the ambulance exterior",
    "source_state": "The ambulance exterior appears clean, intact, and recently maintained.",
    "desired_change": "The ambulance becomes visibly old and dirty, with weathered paint and road grime across its body."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      26,
      31
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 27 seconds, make the ambulance exterior visibly old and dirty with weathered paint and road grime over two seconds.",
  "expected_result": {
    "description": "The ambulance becomes visibly old and dirty, with weathered paint and road grime across its body.",
    "target_phrase": "old dirty ambulance exterior"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_031_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The broad white body panels are continuously visible and provide a clear clean source state."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_031_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the ambulance exterior on B independently of E1's change to the ambulance's forward orientation; both edit results must coexist in C."
  }
}
```

## synthetic_object_032

### synthetic_object_032_E1

```json
{
  "video_id": "synthetic_object_032",
  "edit_id": "synthetic_object_032_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_032.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_framing_of_the_tow_truck_and_silver_car",
    "target_description": "the framing of the tow truck and silver car",
    "source_state": "The tow truck and silver car nearly fill the horizontal frame together.",
    "desired_change": "The camera widens until both vehicles and two empty lane-widths of surroundings are visible."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      10.5,
      17.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 11.5 seconds, smoothly zoom out until both vehicles and two empty lane-widths of roadway are visible.",
  "expected_result": {
    "description": "The camera widens until both vehicles and two empty lane-widths of surroundings are visible.",
    "target_phrase": "wide framing around both vehicles"
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
      10.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both vehicles are fully visible from a stable high side viewpoint."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_032_E2A

```json
{
  "video_id": "synthetic_object_032",
  "edit_id": "synthetic_object_032_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_032.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_raised_steel_tow_platform",
    "target_description": "the raised steel tow platform",
    "source_state": "The raised steel tow platform appears clean, dry, and matte.",
    "desired_change": "The platform becomes rain-wet with a continuous reflective sheen."
  },
  "timing": {
    "edit_point_sec": 28.5,
    "effect_start_sec": 28.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      27.5,
      32.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 28.5 seconds, change the raised steel tow platform from dry and matte to rain-wet and reflective.",
  "expected_result": {
    "description": "The platform becomes rain-wet with a continuous reflective sheen.",
    "target_phrase": "rain-wet reflective tow platform"
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
      27.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The empty tilted platform is broad, exposed, and separated from the silver car."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_032_E2B

```json
{
  "video_id": "synthetic_object_032",
  "edit_id": "synthetic_object_032_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_032_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_upright_red_roadside_bollard",
    "target_description": "the upright red roadside bollard",
    "source_state": "The upright red bollard beside the wall remains still while the platform tilts.",
    "desired_change": "The red bollard sways left and right twice without leaving its base."
  },
  "timing": {
    "edit_point_sec": 23.5,
    "effect_start_sec": 23.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      22.5,
      29.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 23.5 seconds, make the upright red bollard beside the wall sway left and right twice without leaving its base.",
  "expected_result": {
    "description": "The red bollard sways left and right twice without leaving its base.",
    "target_phrase": "red roadside bollard swaying twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_032_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The single upright bollard is isolated against the wall and remains separate from the wheel chocks."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_032_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the upright red roadside bollard on B independently of E1's change to the framing of the tow truck and silver car; both edit results must coexist in C."
  }
}
```

## synthetic_object_033

### synthetic_object_033_E1

```json
{
  "video_id": "synthetic_object_033",
  "edit_id": "synthetic_object_033_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_street_sweeper_s_blue_body_panels",
    "target_description": "the street sweeper's blue body panels",
    "source_state": "The street sweeper has bright blue body panels with dark brush assemblies.",
    "desired_change": "The blue body panels become vivid orange while the brush assemblies remain dark."
  },
  "timing": {
    "edit_point_sec": 9.5,
    "effect_start_sec": 9.5,
    "effect_end_sec": 11.5,
    "evaluation_window_sec": [
      8.5,
      13.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 9.5 seconds, change the street sweeper's bright blue body panels to vivid orange over the next two seconds.",
  "expected_result": {
    "description": "The blue body panels become vivid orange while the brush assemblies remain dark.",
    "target_phrase": "vivid orange street sweeper"
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
      8.5,
      13.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The body panels are fully exposed above the twin circular brushes."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_033_E2A

```json
{
  "video_id": "synthetic_object_033",
  "edit_id": "synthetic_object_033_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_033.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_loose_leaves_relative_to_the_right_circular_brush",
    "target_description": "the loose leaves relative to the right circular brush",
    "source_state": "Sparse loose leaves lie irregularly around and ahead of the circular brushes.",
    "desired_change": "The loose leaves are gathered into a narrow line directly ahead of the right circular brush."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      27,
      31
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 28 seconds, gather the visible loose leaves into a narrow line directly ahead of the right circular brush.",
  "expected_result": {
    "description": "The loose leaves are gathered into a narrow line directly ahead of the right circular brush.",
    "target_phrase": "leaf line ahead of the right brush"
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
      27,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right brush, road surface, and scattered leaves are visible in one stable view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_033_E2B

```json
{
  "video_id": "synthetic_object_033",
  "edit_id": "synthetic_object_033_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_033_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Brush-to-pavement Separation Interaction",
    "scope": "Core Object and Environment Surface"
  },
  "target": {
    "target_id": "the_right_circular_street_sweeper_brush_and_the_pavement",
    "target_description": "the right circular street-sweeper brush and the pavement",
    "source_state": "The right circular brush remains in contact with the pavement while cleaning.",
    "desired_change": "The right circular brush lifts completely clear of the pavement and remains raised for four seconds."
  },
  "timing": {
    "edit_point_sec": 21.5,
    "effect_start_sec": 21.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      20.5,
      27.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 21.5 seconds, lift the right circular street-sweeper brush completely clear of the pavement for four seconds.",
  "expected_result": {
    "description": "The right circular brush lifts completely clear of the pavement and remains raised for four seconds.",
    "target_phrase": "right circular brush raised above the pavement"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_033_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right brush head and the pavement directly beneath it remain clearly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_033_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the right circular street-sweeper brush and the pavement on B independently of E1's change to the street sweeper's blue body panels; both edit results must coexist in C."
  }
}
```

## synthetic_object_034

### synthetic_object_034_E1

```json
{
  "video_id": "synthetic_object_034",
  "edit_id": "synthetic_object_034_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_034.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_rear_discharge_chute_and_road",
    "target_description": "the rear discharge chute and road",
    "source_state": "The raised rear discharge chute remains separated from the road surface.",
    "desired_change": "The chute swings downward and pours one short stream of concrete onto the road."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 18.5,
    "evaluation_window_sec": [
      13.5,
      20.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.5 seconds, make the rear discharge chute swing downward and pour one short stream of concrete onto the road.",
  "expected_result": {
    "description": "The chute swings downward and pours one short stream of concrete onto the road.",
    "target_phrase": "chute pouring one short concrete stream"
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
      13.5,
      20.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The chute outlet and clear road directly beneath it are visible in side profile."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_034_E2A

```json
{
  "video_id": "synthetic_object_034",
  "edit_id": "synthetic_object_034_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_034.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_rear_discharge_chute",
    "target_description": "the rear discharge chute",
    "source_state": "A long pale discharge chute projects downward from the rear mixing assembly.",
    "desired_change": "The rear discharge chute is removed from the truck."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, remove the long pale discharge chute projecting downward from the concrete mixer's rear assembly.",
  "expected_result": {
    "description": "The rear discharge chute is removed from the truck.",
    "target_phrase": "rear discharge chute removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The long chute is distinct from the drum and rear wheels in the broad side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_034_E2B

```json
{
  "video_id": "synthetic_object_034",
  "edit_id": "synthetic_object_034_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_034_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_large_mixing_drum",
    "target_description": "the large mixing drum",
    "source_state": "The large mixing drum is plain white with subtle gray shading.",
    "desired_change": "The mixing drum becomes safety yellow while its bands and seams remain visible."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, change the concrete mixer's large white drum to safety yellow over the next two seconds.",
  "expected_result": {
    "description": "The mixing drum becomes safety yellow while its bands and seams remain visible.",
    "target_phrase": "safety-yellow mixing drum"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_034_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The entire rotating drum remains broadside and unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_034_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large mixing drum on B independently of E1's change to the rear discharge chute and road; both edit results must coexist in C."
  }
}
```

## synthetic_object_035

### synthetic_object_035_E1

```json
{
  "video_id": "synthetic_object_035",
  "edit_id": "synthetic_object_035_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_035.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_dump_bed_tailgate_and_rear_stop",
    "target_description": "the dump-bed tailgate and rear stop",
    "source_state": "The tailgate remains closed against the stationary dump bed.",
    "desired_change": "The tailgate swings open, contacts its lower stop once, and remains open."
  },
  "timing": {
    "edit_point_sec": 17.5,
    "effect_start_sec": 17.5,
    "effect_end_sec": 21.5,
    "evaluation_window_sec": [
      16.5,
      23.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 17.5 seconds, make the dump-bed tailgate swing open and contact its lower stop once before remaining open.",
  "expected_result": {
    "description": "The tailgate swings open, contacts its lower stop once, and remains open.",
    "target_phrase": "tailgate opening against its lower stop"
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
      16.5,
      23.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rear tailgate, hinges, bed frame, and open pavement are fully visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_035_E2A

```json
{
  "video_id": "synthetic_object_035",
  "edit_id": "synthetic_object_035_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_035.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_raised_dump_bed",
    "target_description": "the raised dump bed",
    "source_state": "The dump bed has a pale weathered beige finish.",
    "desired_change": "The dump bed becomes dark industrial green while retaining its worn surface texture."
  },
  "timing": {
    "edit_point_sec": 29.5,
    "effect_start_sec": 29.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      28.5,
      33.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 29.5 seconds, change the raised dump bed from weathered beige to dark industrial green over two seconds.",
  "expected_result": {
    "description": "The dump bed becomes dark industrial green while retaining its worn surface texture.",
    "target_phrase": "dark industrial-green dump bed"
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
      28.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bed's outer side and raised geometry are unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_035_E2B

```json
{
  "video_id": "synthetic_object_035",
  "edit_id": "synthetic_object_035_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_035_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Global Rendering Style Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_dump_truck_scene",
    "target_description": "the full dump-truck scene",
    "source_state": "The scene uses realistic photographic rendering.",
    "desired_change": "The full scene is rendered as a detailed charcoal-and-chalk drawing."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      27,
      32
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 28 seconds, transform the full dump-truck scene into a detailed charcoal-and-chalk drawing over two seconds.",
  "expected_result": {
    "description": "The full scene is rendered as a detailed charcoal-and-chalk drawing.",
    "target_phrase": "dump-truck scene as charcoal-and-chalk drawing"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_035_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete truck, lifting bed, pavement, and background trees are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_035_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full dump-truck scene on B independently of E1's change to the dump-bed tailgate and rear stop; both edit results must coexist in C."
  }
}
```

## synthetic_object_036

### synthetic_object_036_E1

```json
{
  "video_id": "synthetic_object_036",
  "edit_id": "synthetic_object_036_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_036.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_pavement_beside_the_left_brick_wall",
    "target_description": "the open pavement beside the left brick wall",
    "source_state": "The pavement beside the left brick wall contains no recycling bin.",
    "desired_change": "One blue wheeled recycling bin is added against the left brick wall."
  },
  "timing": {
    "edit_point_sec": 8.5,
    "effect_start_sec": 8.5,
    "effect_end_sec": 9.5,
    "evaluation_window_sec": [
      7.5,
      11.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 8.5 seconds, add one blue wheeled recycling bin against the left brick wall beside the van's route.",
  "expected_result": {
    "description": "One blue wheeled recycling bin is added against the left brick wall.",
    "target_phrase": "blue recycling bin beside the brick wall"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      7.5,
      11.5
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The wall base and an unoccupied stable pavement area are visible at the junction."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_036_E2A

```json
{
  "video_id": "synthetic_object_036",
  "edit_id": "synthetic_object_036_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_036.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_white_van_s_forward_motion",
    "target_description": "the white van's forward motion",
    "source_state": "The van proceeds steadily along the residential street.",
    "desired_change": "The van moves at half its original forward speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      30,
      38
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 31 seconds, reduce the white van's forward speed to half its original rate for the next five seconds.",
  "expected_result": {
    "description": "The van moves at half its original forward speed for five seconds.",
    "target_phrase": "white van moving at half speed"
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
      30,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The van remains centered with curb stones and houses providing motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_036_E2B

```json
{
  "video_id": "synthetic_object_036",
  "edit_id": "synthetic_object_036_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_036_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Weather",
    "operation": "Sunny-weather Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_weather_across_the_residential_street",
    "target_description": "the weather across the residential street",
    "source_state": "The residential street is overcast and dim beneath a gray sky.",
    "desired_change": "The weather becomes bright and sunny with a clear sky and direct sunlight across the street."
  },
  "timing": {
    "edit_point_sec": 21.5,
    "effect_start_sec": 21.5,
    "effect_end_sec": 23.5,
    "evaluation_window_sec": [
      20.5,
      25.5
    ],
    "temporal_behavior": "gradual persistent weather change"
  },
  "instruction": "Starting at 21.5 seconds, change the weather across the residential street to bright sunshine under a clear sky over two seconds.",
  "expected_result": {
    "description": "The weather becomes bright and sunny with a clear sky and direct sunlight across the street.",
    "target_phrase": "bright sunny residential street"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_036_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20.5,
      25.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The visible sky, houses, van, and roadway provide broad cues for the weather transition."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_036_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the weather across the residential street on B independently of E1's change to the open pavement beside the left brick wall; both edit results must coexist in C."
  }
}
```

## synthetic_object_037

### synthetic_object_037_E1

```json
{
  "video_id": "synthetic_object_037",
  "edit_id": "synthetic_object_037_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_037.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_lake_surface_behind_the_motorhome",
    "target_description": "the lake surface behind the motorhome",
    "source_state": "The lake surface shows only fine low-amplitude texture.",
    "desired_change": "Two diagonal ripple fronts travel across the lake toward the shore."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      11.5,
      19.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 12.5 seconds, make two broad diagonal ripple fronts travel across the lake toward the shore over five seconds.",
  "expected_result": {
    "description": "Two diagonal ripple fronts travel across the lake toward the shore.",
    "target_phrase": "two ripple fronts crossing the lake"
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
      11.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The motorhome is separated from a broad visible lake region behind it."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_037_E2A

```json
{
  "video_id": "synthetic_object_037",
  "edit_id": "synthetic_object_037_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_037.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "Global Media Style Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_lakeside_motorhome_scene",
    "target_description": "the full lakeside motorhome scene",
    "source_state": "The scene has clean contemporary digital color and contrast.",
    "desired_change": "The full scene adopts the grain, muted palette, and gentle halation of 1970s color film."
  },
  "timing": {
    "edit_point_sec": 35,
    "effect_start_sec": 35,
    "effect_end_sec": 37,
    "evaluation_window_sec": [
      34,
      39
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 35 seconds, transform the full lakeside motorhome scene into a muted 1970s color-film look over two seconds.",
  "expected_result": {
    "description": "The full scene adopts the grain, muted palette, and gentle halation of 1970s color film.",
    "target_phrase": "lakeside motorhome scene in 1970s film"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
      39
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The vehicle, parking bays, lake, foliage, and sky are jointly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_037_E2B

```json
{
  "video_id": "synthetic_object_037",
  "edit_id": "synthetic_object_037_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_037_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_motorhome_s_cream_side_panels",
    "target_description": "the motorhome's cream side panels",
    "source_state": "The motorhome has cream-white side panels with dark windows and trim.",
    "desired_change": "The cream side panels become pale sage green while the trim remains dark."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, change the motorhome's cream side panels to pale sage green over the next two seconds.",
  "expected_result": {
    "description": "The cream side panels become pale sage green while the trim remains dark.",
    "target_phrase": "pale sage-green motorhome panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_037_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The long side of the motorhome is unobstructed in the parking-area view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_037_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the motorhome's cream side panels on B independently of E1's change to the lake surface behind the motorhome; both edit results must coexist in C."
  }
}
```

## synthetic_object_038

### synthetic_object_038_E1

```json
{
  "video_id": "synthetic_object_038",
  "edit_id": "synthetic_object_038_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_038.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_van_s_reversing_motion",
    "target_description": "the red van's reversing motion",
    "source_state": "The red van reverses slowly between the white parking lines.",
    "desired_change": "The van reverses at one-and-a-half times its original speed for four seconds."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      12.5,
      19.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 13.5 seconds, increase the red van's reversing speed to one-and-a-half times its original rate for four seconds.",
  "expected_result": {
    "description": "The van reverses at one-and-a-half times its original speed for four seconds.",
    "target_phrase": "red van reversing one-and-a-half times faster"
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
      12.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rear of the van and repeated white parking lines make displacement measurable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_038_E2A

```json
{
  "video_id": "synthetic_object_038",
  "edit_id": "synthetic_object_038_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_038.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_white_parking_bay_lines",
    "target_description": "the white parking-bay lines",
    "source_state": "The parking-bay lines are painted white on gray pavement.",
    "desired_change": "The visible parking-bay lines become bright yellow while retaining their geometry."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31 seconds, change the visible white parking-bay lines to bright yellow over the next two seconds.",
  "expected_result": {
    "description": "The visible parking-bay lines become bright yellow while retaining their geometry.",
    "target_phrase": "bright-yellow parking-bay lines"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Several unoccluded line segments surround the van in the high-angle view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_038_E2B

```json
{
  "video_id": "synthetic_object_038",
  "edit_id": "synthetic_object_038_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_038_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_red_van_within_the_parking_area",
    "target_description": "the red van within the parking area",
    "source_state": "The red van is positioned near the center of one marked parking bay.",
    "desired_change": "The van is shifted forward by one full parking-bay length along its current heading."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      23.5,
      27.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.5 seconds, shift the red van forward by one full parking-bay length along its current heading.",
  "expected_result": {
    "description": "The van is shifted forward by one full parking-bay length along its current heading.",
    "target_phrase": "van shifted forward one parking-bay length"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_038_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The van, bay boundaries, and open pavement ahead are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_038_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red van within the parking area on B independently of E1's change to the red van's reversing motion; both edit results must coexist in C."
  }
}
```

## synthetic_object_039

### synthetic_object_039_E1

```json
{
  "video_id": "synthetic_object_039",
  "edit_id": "synthetic_object_039_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Wheel-to-road Impact Motion",
    "scope": "Core Object and Environment Surface"
  },
  "target": {
    "target_id": "the_tanker_truck_wheels_and_an_uneven_road_section",
    "target_description": "the tanker truck wheels and an uneven road section",
    "source_state": "The tanker truck wheels roll smoothly along the highway without a visible vertical jolt.",
    "desired_change": "The wheels strike one uneven road section, causing the truck to make a small hop before continuing forward."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 18.5,
    "evaluation_window_sec": [
      13.5,
      20.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 14.5 seconds, make the tanker truck wheels strike an uneven road section and produce one small hop before continuing forward.",
  "expected_result": {
    "description": "The wheels strike one uneven road section, causing the truck to make a small hop before continuing forward.",
    "target_phrase": "tanker truck making one small road-induced hop"
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
      13.5,
      20.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full truck, wheels, and road contact line remain visible in side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_039_E2A

```json
{
  "video_id": "synthetic_object_039",
  "edit_id": "synthetic_object_039_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_039.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_roadside_grassland",
    "target_description": "the roadside grassland",
    "source_state": "The roadside grassland is fresh green under clear daylight.",
    "desired_change": "The grassland becomes dry golden yellow while the road and sky retain their colors."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 33.5,
    "evaluation_window_sec": [
      30.5,
      35.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31.5 seconds, change the roadside grassland from fresh green to dry golden yellow over two seconds.",
  "expected_result": {
    "description": "The grassland becomes dry golden yellow while the road and sky retain their colors.",
    "target_phrase": "dry golden-yellow roadside grassland"
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
      30.5,
      35.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad continuous grass strip is visible above and below the highway."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_039_E2B

```json
{
  "video_id": "synthetic_object_039",
  "edit_id": "synthetic_object_039_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_039_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Sheep Addition",
    "scope": "Environment Objects"
  },
  "target": {
    "target_id": "the_open_grassland_away_from_the_highway",
    "target_description": "the open grassland away from the highway",
    "source_state": "The open grassland beside the highway contains no sheep.",
    "desired_change": "A flock of twelve sheep is added across the open grassland well away from the roadway."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      24.5,
      28.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25.5 seconds, add a flock of twelve sheep across the open grassland well away from the highway.",
  "expected_result": {
    "description": "A flock of twelve sheep is added across the open grassland well away from the roadway.",
    "target_phrase": "flock of twelve sheep on the grassland"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_039_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      28.5
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. A broad unoccupied grass area remains visible beyond the truck's roadway."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_039_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the open grassland away from the highway on B independently of E1's change to the tanker truck wheels and an uneven road section; both edit results must coexist in C."
  }
}
```

## synthetic_object_040

### synthetic_object_040_E1

```json
{
  "video_id": "synthetic_object_040",
  "edit_id": "synthetic_object_040_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Transit-shelter Orientation Change",
    "scope": "Environment Object"
  },
  "target": {
    "target_id": "the_glass_transit_shelter_beside_the_trolleybus",
    "target_description": "the glass transit shelter beside the trolleybus",
    "source_state": "The nearby transit shelter presents an oblique side view to the camera.",
    "desired_change": "The shelter rotates around its base until its rear face points directly toward the camera."
  },
  "timing": {
    "edit_point_sec": 16,
    "effect_start_sec": 16,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      15,
      19
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 16 seconds, rotate the glass transit shelter beside the trolleybus until its rear face points directly toward the camera.",
  "expected_result": {
    "description": "The shelter rotates around its base until its rear face points directly toward the camera.",
    "target_phrase": "transit shelter rear face toward the camera"
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
      15,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The shelter's base, side panels, and rear plane are distinguishable beside the trolleybus."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_040_E2A

```json
{
  "video_id": "synthetic_object_040",
  "edit_id": "synthetic_object_040_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_040.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_road_surface_around_the_trolleybus",
    "target_description": "the road surface around the trolleybus",
    "source_state": "The road surface is dark gray asphalt with pale painted markings.",
    "desired_change": "The unmarked asphalt becomes pale concrete while all painted markings remain distinct."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      33,
      38
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 34 seconds, change the unmarked road surface around the trolleybus from dark asphalt to pale concrete over two seconds.",
  "expected_result": {
    "description": "The unmarked asphalt becomes pale concrete while all painted markings remain distinct.",
    "target_phrase": "pale concrete road around the trolleybus"
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
      33,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad road region surrounds the bus after the bend."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_040_E2B

```json
{
  "video_id": "synthetic_object_040",
  "edit_id": "synthetic_object_040_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_040_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_behind_the_trolleybus",
    "target_description": "the camera path behind the trolleybus",
    "source_state": "The camera follows the trolleybus from a moderately elevated rear view.",
    "desired_change": "The camera rises smoothly into a high rear tracking view over five seconds."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      27,
      35
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 28 seconds, raise the camera smoothly into a high rear tracking view above the trolleybus over five seconds.",
  "expected_result": {
    "description": "The camera rises smoothly into a high rear tracking view over five seconds.",
    "target_phrase": "high rear tracking view above the trolleybus"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_040_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bus, road network, trees, and overhead wires provide strong depth references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_040_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera path behind the trolleybus on B independently of E1's change to the glass transit shelter beside the trolleybus; both edit results must coexist in C."
  }
}
```

## synthetic_object_041

### synthetic_object_041_E1

```json
{
  "video_id": "synthetic_object_041",
  "edit_id": "synthetic_object_041_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_041.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Auxiliary Object Style Change",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_sailboat_s_forward_triangular_sail",
    "target_description": "the sailboat's forward triangular sail",
    "source_state": "The forward triangular sail has realistic cream canvas shading and dark edging.",
    "desired_change": "Only the forward triangular sail is rendered with a translucent stained-glass texture in pale blue and amber."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      11.5,
      16.5
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 12.5 seconds, render only the sailboat's forward triangular sail as translucent pale-blue and amber stained glass.",
  "expected_result": {
    "description": "Only the forward triangular sail is rendered with a translucent stained-glass texture in pale blue and amber.",
    "target_phrase": "stained-glass forward sail"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The forward sail is fully deployed and cleanly separated from the sky and larger rear sail."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_041_E2A

```json
{
  "video_id": "synthetic_object_041",
  "edit_id": "synthetic_object_041_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_041.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_starboard_wake_and_the_nearby_yellow_buoy",
    "target_description": "the starboard wake and the nearby yellow buoy",
    "source_state": "The sailboat's wake passes beside the yellow buoy without visibly moving it.",
    "desired_change": "The starboard wake reaches the nearby yellow buoy and makes it bob outward once before settling."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      30,
      37
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 31 seconds, make the sailboat's starboard wake push the nearby yellow buoy outward once before it settles.",
  "expected_result": {
    "description": "The starboard wake reaches the nearby yellow buoy and makes it bob outward once before settling.",
    "target_phrase": "wake pushing the yellow buoy outward once"
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
      30,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right wake branch and adjacent yellow buoy remain visible with open water between them."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_041_E2B

```json
{
  "video_id": "synthetic_object_041",
  "edit_id": "synthetic_object_041_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_041_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_water_behind_the_sailboat_s_port_side",
    "target_description": "the open water behind the sailboat's port side",
    "source_state": "No red buoy occupies the open water behind the sailboat's port side.",
    "desired_change": "One red spherical buoy is added two boat-lengths behind the port hull."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      24,
      28
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25 seconds, add one red spherical buoy two boat-lengths behind the sailboat's port hull in the open water.",
  "expected_result": {
    "description": "One red spherical buoy is added two boat-lengths behind the port hull.",
    "target_phrase": "red spherical buoy behind the port hull"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_041_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24,
      28
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. A stable open-water placement area is visible beside the curved wake and away from the existing yellow buoys."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_041_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the open water behind the sailboat's port side on B independently of E1's change to the sailboat's forward triangular sail; both edit results must coexist in C."
  }
}
```

## synthetic_object_042

### synthetic_object_042_E1

```json
{
  "video_id": "synthetic_object_042",
  "edit_id": "synthetic_object_042_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_042.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_undisturbed_water_beyond_the_speedboat_s_wake",
    "target_description": "the undisturbed water beyond the speedboat's wake",
    "source_state": "The undisturbed water beyond the wake is muted blue-gray.",
    "desired_change": "The surrounding undisturbed water becomes clear deep turquoise while the white wake stays distinct."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      12,
      17
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 13 seconds, change the undisturbed water beyond the speedboat's wake from blue-gray to clear deep turquoise.",
  "expected_result": {
    "description": "The surrounding undisturbed water becomes clear deep turquoise while the white wake stays distinct.",
    "target_phrase": "deep-turquoise water beyond the wake"
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
      12,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad water region surrounds the boat and remains separated from the white foam trail."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_042_E2A

```json
{
  "video_id": "synthetic_object_042",
  "edit_id": "synthetic_object_042_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_042.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_nearest_orange_conical_buoy",
    "target_description": "the nearest orange conical buoy",
    "source_state": "An isolated orange conical buoy is visible ahead and to the speedboat's right.",
    "desired_change": "The nearest orange conical buoy is removed from the water."
  },
  "timing": {
    "edit_point_sec": 36,
    "effect_start_sec": 36,
    "effect_end_sec": 37,
    "evaluation_window_sec": [
      35,
      39
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 36 seconds, remove the nearest orange conical buoy visible ahead and to the speedboat's right.",
  "expected_result": {
    "description": "The nearest orange conical buoy is removed from the water.",
    "target_phrase": "nearest orange buoy removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      35,
      39
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy is isolated against open water at the command point and does not overlap the hull."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_042_E2B

```json
{
  "video_id": "synthetic_object_042",
  "edit_id": "synthetic_object_042_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_042_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_and_white_speedboat",
    "target_description": "the red-and-white speedboat",
    "source_state": "The speedboat completes one broad turn and then follows a smooth forward path.",
    "desired_change": "The speedboat performs two short alternating left-right turns before resuming its forward path."
  },
  "timing": {
    "edit_point_sec": 26.5,
    "effect_start_sec": 26.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      25.5,
      33.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 26.5 seconds, make the red-and-white speedboat perform two short alternating left-right turns before continuing forward.",
  "expected_result": {
    "description": "The speedboat performs two short alternating left-right turns before resuming its forward path.",
    "target_phrase": "two alternating turns by the speedboat"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_042_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full boat and its newly formed wake remain visible throughout the clear-water turn window."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_042_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red-and-white speedboat on B independently of E1's change to the undisturbed water beyond the speedboat's wake; both edit results must coexist in C."
  }
}
```

## synthetic_object_043

### synthetic_object_043_E1

```json
{
  "video_id": "synthetic_object_043",
  "edit_id": "synthetic_object_043_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_043.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_yellow_channel_marker_beside_the_container_ship",
    "target_description": "the yellow channel marker beside the container ship",
    "source_state": "A yellow channel marker stands in the water to the container ship's right.",
    "desired_change": "The yellow channel marker beside the approaching container ship is removed."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      11,
      15
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 12 seconds, remove the yellow channel marker standing in the water to the approaching container ship's right.",
  "expected_result": {
    "description": "The yellow channel marker beside the approaching container ship is removed.",
    "target_phrase": "yellow channel marker removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11,
      15
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The marker is isolated against the channel and remains spatially separate from the ship and quay."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_043_E2A

```json
{
  "video_id": "synthetic_object_043",
  "edit_id": "synthetic_object_043_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_043.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_dark_harbor_vessel_crossing_the_blue_and_white_vessel_s_wake",
    "target_description": "the dark harbor vessel crossing the blue-and-white vessel's wake",
    "source_state": "The dark vessel and the blue-and-white vessel pass with their hulls and wakes remaining separated.",
    "desired_change": "The dark vessel crosses the other vessel's wake and rolls gently once before leveling."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 39.5,
    "evaluation_window_sec": [
      34.5,
      41.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 35.5 seconds, make the dark harbor vessel cross the blue-and-white vessel's wake and roll gently once.",
  "expected_result": {
    "description": "The dark vessel crosses the other vessel's wake and rolls gently once before leveling.",
    "target_phrase": "dark vessel rolling once across the wake"
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
      34.5,
      41.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both vessels, their crossing paths, and the intervening water are visible in the continuous harbor view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_043_E2B

```json
{
  "video_id": "synthetic_object_043",
  "edit_id": "synthetic_object_043_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_043_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_uppermost_blue_container_row",
    "target_description": "the uppermost blue container row",
    "source_state": "The uppermost blue container row appears dry with a matte painted surface.",
    "desired_change": "The uppermost blue container row becomes coated with a thin, visibly frosted layer."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 20 seconds, coat the uppermost visible blue container row with a thin layer of frost over two seconds.",
  "expected_result": {
    "description": "The uppermost blue container row becomes coated with a thin, visibly frosted layer.",
    "target_phrase": "frost-coated blue container row"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_043_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
    "description": "The final visible container rows remain identifiable immediately before the large ship leaves the lower frame."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_043_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the uppermost blue container row on B independently of E1's change to the yellow channel marker beside the container ship; both edit results must coexist in C."
  }
}
```

## synthetic_object_044

### synthetic_object_044_E1

```json
{
  "video_id": "synthetic_object_044",
  "edit_id": "synthetic_object_044_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_044.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_small_tugboat_beside_the_cargo_ship",
    "target_description": "the small tugboat beside the cargo ship",
    "source_state": "The tugboat remains close beside the cargo ship's bow while moving laterally.",
    "desired_change": "The tugboat reverses away from the cargo ship by one tugboat-width and then holds the new separation."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      12.5,
      19.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 13.5 seconds, make the small tugboat reverse one tugboat-width away from the cargo ship and hold there.",
  "expected_result": {
    "description": "The tugboat reverses away from the cargo ship by one tugboat-width and then holds the new separation.",
    "target_phrase": "tugboat reversing away from the cargo ship"
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
      12.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tugboat, cargo-ship bow, and water gap are continuously visible in the same shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_044_E2A

```json
{
  "video_id": "synthetic_object_044",
  "edit_id": "synthetic_object_044_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_044.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_water_to_the_tugboat_s_right",
    "target_description": "the open water to the tugboat's right",
    "source_state": "No yellow spherical buoy occupies the open water to the tugboat's right.",
    "desired_change": "One yellow spherical buoy is added two tugboat-lengths to the tugboat's right."
  },
  "timing": {
    "edit_point_sec": 33,
    "effect_start_sec": 33,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      32,
      36
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 33 seconds, add one yellow spherical buoy two tugboat-lengths to the right of the small tugboat.",
  "expected_result": {
    "description": "One yellow spherical buoy is added two tugboat-lengths to the tugboat's right.",
    "target_phrase": "yellow spherical buoy beside the tugboat"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32,
      36
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The tugboat is fully visible with a clear, unoccupied water region on its right side."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_044_E2B

```json
{
  "video_id": "synthetic_object_044",
  "edit_id": "synthetic_object_044_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_044_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_tugboat_s_black_bow_fender",
    "target_description": "the tugboat's black bow fender",
    "source_state": "The thick black bow fender retains a rounded, fully expanded profile.",
    "desired_change": "The front section of the black bow fender becomes visibly compressed and flattened."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 25.5 seconds, compress and flatten the front section of the tugboat's thick black bow fender over two seconds.",
  "expected_result": {
    "description": "The front section of the black bow fender becomes visibly compressed and flattened.",
    "target_phrase": "compressed black bow fender"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_044_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tugboat bow and dark perimeter fender are distinct against the pale water and cargo hull."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_044_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tugboat's black bow fender on B independently of E1's change to the small tugboat beside the cargo ship; both edit results must coexist in C."
  }
}
```

## synthetic_object_045

### synthetic_object_045_E1

```json
{
  "video_id": "synthetic_object_045",
  "edit_id": "synthetic_object_045_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_catamaran_s_forward_sail",
    "target_description": "the catamaran's forward sail",
    "source_state": "The forward sail remains smoothly tensioned during steady travel.",
    "desired_change": "The forward sail flaps outward and returns twice while remaining attached to the mast and rigging."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      11.5,
      18.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 12.5 seconds, make the catamaran's forward sail flap outward and return twice over four seconds.",
  "expected_result": {
    "description": "The forward sail flaps outward and returns twice while remaining attached to the mast and rigging.",
    "target_phrase": "forward sail flapping twice"
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
      11.5,
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The deployed forward sail is clearly outlined against the sky throughout the continuous view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_045_E2A

```json
{
  "video_id": "synthetic_object_045",
  "edit_id": "synthetic_object_045_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_045.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_dark_aft_canopy",
    "target_description": "the dark aft canopy",
    "source_state": "The catamaran's dark aft canopy appears dry and matte.",
    "desired_change": "The aft canopy becomes rain-wet with a continuous glossy surface and small water beads."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 31 seconds, change the catamaran's dark aft canopy from dry and matte to rain-wet and glossy.",
  "expected_result": {
    "description": "The aft canopy becomes rain-wet with a continuous glossy surface and small water beads.",
    "target_phrase": "rain-wet glossy aft canopy"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The canopy remains visible between the twin hulls and below the sails in the rear-quarter view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_045_E2B

```json
{
  "video_id": "synthetic_object_045",
  "edit_id": "synthetic_object_045_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_045_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "Global Media Style Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_catamaran_sailing_scene",
    "target_description": "the full catamaran sailing scene",
    "source_state": "The scene has clean contemporary digital color and contrast.",
    "desired_change": "The full scene adopts muted colors, fine grain, and gentle halation associated with 1970s color film."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 25.5 seconds, transform the full catamaran scene into a muted 1970s color-film look over two seconds.",
  "expected_result": {
    "description": "The full scene adopts muted colors, fine grain, and gentle halation associated with 1970s color film.",
    "target_phrase": "catamaran scene in 1970s color film"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_045_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete boat, sails, twin wake, sea, and sky are visible without a shot change."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_045_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the full catamaran sailing scene on B independently of E1's change to the catamaran's forward sail; both edit results must coexist in C."
  }
}
```

## synthetic_object_046

### synthetic_object_046_E1

```json
{
  "video_id": "synthetic_object_046",
  "edit_id": "synthetic_object_046_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_yellow_motorboat_in_the_open_water",
    "target_description": "the yellow motorboat in the open water",
    "source_state": "The motorboat approaches near the horizontal center of the frame.",
    "desired_change": "The complete motorboat is shifted one boat-width toward the left side of the frame while retaining its heading."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, shift the complete yellow motorboat one boat-width toward the left side of the frame.",
  "expected_result": {
    "description": "The complete motorboat is shifted one boat-width toward the left side of the frame while retaining its heading.",
    "target_phrase": "yellow motorboat shifted one width left"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "motorboat forward heading toward the camera"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full hull, open water on both sides, and stable horizon make the displacement measurable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_046_E2A

```json
{
  "video_id": "synthetic_object_046",
  "edit_id": "synthetic_object_046_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_046.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_motorboat_bow_and_the_approaching_wave",
    "target_description": "the motorboat bow and the approaching wave",
    "source_state": "The bow crosses the approaching wave with moderate spray on both sides.",
    "desired_change": "The bow strikes the wave and throws one tall, symmetrical fan of spray before settling."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      25,
      32
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 26 seconds, make the yellow motorboat's bow strike the approaching wave and throw one tall symmetrical spray fan.",
  "expected_result": {
    "description": "The bow strikes the wave and throws one tall, symmetrical fan of spray before settling.",
    "target_phrase": "bow throwing one tall spray fan"
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
      25,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bow, wave crest, and unobstructed spray area remain centered in the continuous frontal view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_046_E2B

```json
{
  "video_id": "synthetic_object_046",
  "edit_id": "synthetic_object_046_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_046_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_framing_around_the_yellow_motorboat",
    "target_description": "the framing around the yellow motorboat",
    "source_state": "The approaching motorboat occupies about one third of the frame height.",
    "desired_change": "The camera smoothly widens until the motorboat occupies about one fifth of the frame height."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      23.5,
      30.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 24.5 seconds, smoothly zoom out until the yellow motorboat occupies about one fifth of the frame height.",
  "expected_result": {
    "description": "The camera smoothly widens until the motorboat occupies about one fifth of the frame height.",
    "target_phrase": "motorboat occupying one fifth of frame height"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_046_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The centered hull and stable sea horizon provide clear framing and scale references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_046_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the framing around the yellow motorboat on B independently of E1's change to the yellow motorboat in the open water; both edit results must coexist in C."
  }
}
```

## synthetic_object_047

### synthetic_object_047_E1

```json
{
  "video_id": "synthetic_object_047",
  "edit_id": "synthetic_object_047_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_submarine_s_forward_motion",
    "target_description": "the submarine's forward motion",
    "source_state": "The submarine travels steadily along the underwater slope while gradually receding.",
    "desired_change": "The submarine moves at twice its original forward speed for five seconds along the same path."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      11,
      19
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 12 seconds, increase the submarine's forward speed to twice its original rate along the same underwater path for five seconds.",
  "expected_result": {
    "description": "The submarine moves at twice its original forward speed for five seconds along the same path.",
    "target_phrase": "submarine moving at twice its speed"
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
      11,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full silhouette and textured seabed slope provide continuous displacement references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_047_E2A

```json
{
  "video_id": "synthetic_object_047",
  "edit_id": "synthetic_object_047_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_047.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_around_the_submarine",
    "target_description": "the camera path around the submarine",
    "source_state": "The camera observes the receding submarine from a lateral elevated angle.",
    "desired_change": "The camera arcs smoothly upward and inward to a near-overhead view of the submarine."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 35.5,
    "evaluation_window_sec": [
      29.5,
      37.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 30.5 seconds, arc the camera smoothly upward and inward to a near-overhead view of the submarine.",
  "expected_result": {
    "description": "The camera arcs smoothly upward and inward to a near-overhead view of the submarine.",
    "target_phrase": "near-overhead camera view of the submarine"
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
      29.5,
      37.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The submarine, sloping seabed, and directional light shafts provide stable depth references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_047_E2B

```json
{
  "video_id": "synthetic_object_047",
  "edit_id": "synthetic_object_047_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_047_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_large_isolated_boulder_below_the_submarine",
    "target_description": "the large isolated boulder below the submarine",
    "source_state": "A large isolated boulder lies on the seabed below and ahead of the submarine.",
    "desired_change": "The large isolated seabed boulder is removed."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      23.5,
      27.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.5 seconds, remove the large isolated boulder lying on the seabed below and ahead of the submarine.",
  "expected_result": {
    "description": "The large isolated seabed boulder is removed.",
    "target_phrase": "large seabed boulder removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_047_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The boulder is separated from the submarine silhouette and surrounding finer seabed texture."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_047_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the large isolated boulder below the submarine on B independently of E1's change to the submarine's forward motion; both edit results must coexist in C."
  }
}
```

## synthetic_object_048

### synthetic_object_048_E1

```json
{
  "video_id": "synthetic_object_048",
  "edit_id": "synthetic_object_048_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_048.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_hovercraft_s_forward_motion",
    "target_description": "the hovercraft's forward motion",
    "source_state": "The hovercraft glides away at a steady rate over the water.",
    "desired_change": "The hovercraft travels at one-and-a-half times its original forward speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      11.5,
      19.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 12.5 seconds, increase the hovercraft's forward speed to one-and-a-half times its original rate for five seconds.",
  "expected_result": {
    "description": "The hovercraft travels at one-and-a-half times its original forward speed for five seconds.",
    "target_phrase": "hovercraft moving one-and-a-half times faster"
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
      11.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The centered rear fan, water texture, and expanding wake make the displacement change measurable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_048_E2A

```json
{
  "video_id": "synthetic_object_048",
  "edit_id": "synthetic_object_048_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_048.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_hovercraft_relative_to_the_far_shoreline",
    "target_description": "the hovercraft relative to the far shoreline",
    "source_state": "The receding hovercraft remains several body-lengths in front of the far shoreline.",
    "desired_change": "The hovercraft is repositioned one body-length closer to the far shoreline along its existing heading."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, move the hovercraft one body-length closer to the far shoreline along its existing forward heading.",
  "expected_result": {
    "description": "The hovercraft is repositioned one body-length closer to the far shoreline along its existing heading.",
    "target_phrase": "hovercraft one body-length closer to shore"
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
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete hovercraft and the straight far shoreline are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_048_E2B

```json
{
  "video_id": "synthetic_object_048",
  "edit_id": "synthetic_object_048_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_048_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_hovercraft_s_black_flexible_skirt",
    "target_description": "the hovercraft's black flexible skirt",
    "source_state": "The black flexible skirt has a moderately inflated rounded profile above the water.",
    "desired_change": "The skirt becomes fully inflated, visibly lifting the rigid white body higher above the water."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      24,
      29
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 25 seconds, fully inflate the hovercraft's black skirt and lift the rigid white body visibly higher above the water.",
  "expected_result": {
    "description": "The skirt becomes fully inflated, visibly lifting the rigid white body higher above the water.",
    "target_phrase": "fully inflated hovercraft skirt"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_048_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The symmetrical rear skirt and waterline remain visible in the centered rear view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_048_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the hovercraft's black flexible skirt on B independently of E1's change to the hovercraft's forward motion; both edit results must coexist in C."
  }
}
```

## synthetic_object_049

### synthetic_object_049_E1

```json
{
  "video_id": "synthetic_object_049",
  "edit_id": "synthetic_object_049_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_lake_water_beyond_the_floatplane_s_spray",
    "target_description": "the lake water beyond the floatplane's spray",
    "source_state": "The lake water beyond the float spray is muted gray-blue.",
    "desired_change": "The undisturbed lake water becomes clear emerald green while the white spray remains distinct."
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
  "instruction": "Starting at 14 seconds, change the undisturbed lake water beyond the floatplane's spray from gray-blue to clear emerald green.",
  "expected_result": {
    "description": "The undisturbed lake water becomes clear emerald green while the white spray remains distinct.",
    "target_phrase": "emerald-green lake water"
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
    "description": "A broad water surface surrounds the two floats and remains distinct from the white spray."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_049_E2A

```json
{
  "video_id": "synthetic_object_049",
  "edit_id": "synthetic_object_049_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_049.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_lake_ahead_of_the_floatplane",
    "target_description": "the open lake ahead of the floatplane",
    "source_state": "No yellow marker buoy occupies the open water ahead of the taxiing floatplane.",
    "desired_change": "One yellow spherical marker buoy is added three wing-lengths ahead of the floatplane."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      29.5,
      33.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30.5 seconds, add one yellow spherical marker buoy three wing-lengths ahead of the taxiing floatplane.",
  "expected_result": {
    "description": "One yellow spherical marker buoy is added three wing-lengths ahead of the floatplane.",
    "target_phrase": "yellow buoy ahead of the floatplane"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.5,
      33.5
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The aircraft and a wide unobstructed area of lake ahead remain visible before takeoff."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_049_E2B

```json
{
  "video_id": "synthetic_object_049",
  "edit_id": "synthetic_object_049_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_049_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_floatplane_s_twin_floats_and_lake_surface",
    "target_description": "the floatplane's twin floats and lake surface",
    "source_state": "Both floats skim the lake continuously with low spray.",
    "desired_change": "The twin floats bounce once together on the water and settle back into a steady skim."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      25,
      32
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 26 seconds, make the floatplane's twin floats bounce once together on the lake and settle into a steady skim.",
  "expected_result": {
    "description": "The twin floats bounce once together on the water and settle back into a steady skim.",
    "target_phrase": "twin floats bouncing once on the lake"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_049_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both floats, their water contact, and the resulting spray remain visible in side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_049_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the floatplane's twin floats and lake surface on B independently of E1's change to the lake water beyond the floatplane's spray; both edit results must coexist in C."
  }
}
```

## synthetic_object_050

### synthetic_object_050_E1

```json
{
  "video_id": "synthetic_object_050",
  "edit_id": "synthetic_object_050_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_050.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_helicopter_rotor_wash_and_treetops_below",
    "target_description": "the helicopter rotor wash and treetops below",
    "source_state": "The treetops below the helicopter show no distinct response to the rotor wash.",
    "desired_change": "The rotor wash presses one circular patch of treetops downward before the foliage rebounds."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      11.5,
      18.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 12.5 seconds, make the helicopter's rotor wash press one circular patch of treetops downward before it rebounds.",
  "expected_result": {
    "description": "The rotor wash presses one circular patch of treetops downward before the foliage rebounds.",
    "target_phrase": "rotor wash pressing treetops downward"
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
      11.5,
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The helicopter, rotor disk, and forest canopy directly below are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_050_E2A

```json
{
  "video_id": "synthetic_object_050",
  "edit_id": "synthetic_object_050_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_050.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_helicopter_relative_to_the_prominent_rock_pinnacle",
    "target_description": "the helicopter relative to the prominent rock pinnacle",
    "source_state": "The helicopter flies offset from the prominent rock pinnacle below.",
    "desired_change": "The helicopter is positioned directly behind and two rotor-diameters above the prominent rock pinnacle."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      29.5,
      33.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30.5 seconds, position the helicopter directly behind and two rotor-diameters above the prominent rock pinnacle below.",
  "expected_result": {
    "description": "The helicopter is positioned directly behind and two rotor-diameters above the prominent rock pinnacle.",
    "target_phrase": "helicopter above and behind the rock pinnacle"
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
      29.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete helicopter and isolated rock pinnacle provide unambiguous relationship anchors."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_050_E2B

```json
{
  "video_id": "synthetic_object_050",
  "edit_id": "synthetic_object_050_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_050_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_helicopter_s_right_side_cabin_door",
    "target_description": "the helicopter's right-side cabin door",
    "source_state": "The right-side cabin door is closed and flush with the yellow fuselage.",
    "desired_change": "The right-side cabin door becomes fully open, revealing the dark cabin opening."
  },
  "timing": {
    "edit_point_sec": 20,
    "effect_start_sec": 20,
    "effect_end_sec": 22,
    "evaluation_window_sec": [
      19,
      24
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 20 seconds, open the helicopter's right-side cabin door fully and reveal the dark cabin opening over two seconds.",
  "expected_result": {
    "description": "The right-side cabin door becomes fully open, revealing the dark cabin opening.",
    "target_phrase": "right-side cabin door fully open"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_050_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
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
    "description": "The side of the yellow cabin is unobstructed against the forested valley."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_050_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the helicopter's right-side cabin door on B independently of E1's change to the helicopter rotor wash and treetops below; both edit results must coexist in C."
  }
}
```

## synthetic_object_051

### synthetic_object_051_E1

```json
{
  "video_id": "synthetic_object_051",
  "edit_id": "synthetic_object_051_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_051.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_first_red_and_black_upper_deck_housing",
    "target_description": "the first red-and-black upper-deck housing",
    "source_state": "A red-and-black rectangular housing stands on the ferry's upper deck.",
    "desired_change": "The first red-and-black upper-deck housing is replaced by a silver cylindrical ventilation pod of comparable size."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      13.5,
      17.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.5 seconds, replace the ferry's first red-and-black upper-deck housing with a silver cylindrical ventilation pod of comparable size.",
  "expected_result": {
    "description": "The first red-and-black upper-deck housing is replaced by a silver cylindrical ventilation pod of comparable size.",
    "target_phrase": "silver ventilation pod on the upper deck"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      13.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The housing is isolated on the upper deck and separated from the white wheelhouse."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_051_E2A

```json
{
  "video_id": "synthetic_object_051",
  "edit_id": "synthetic_object_051_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_051.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_ferry_s_broad_black_dock_ramp",
    "target_description": "the ferry's broad black dock ramp",
    "source_state": "The broad black ramp remains lowered between the ferry and the concrete dock.",
    "desired_change": "The black dock ramp rises from the roadway to a fully upright closed position."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      31,
      38
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 32 seconds, raise the ferry's broad black dock ramp from the roadway to a fully upright closed position.",
  "expected_result": {
    "description": "The black dock ramp rises from the roadway to a fully upright closed position.",
    "target_phrase": "ferry ramp raised fully upright"
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
      31,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The ramp, ferry end, and concrete dock remain visible during the high-angle orbit."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_051_E2B

```json
{
  "video_id": "synthetic_object_051",
  "edit_id": "synthetic_object_051_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_051_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_nearest_dark_car_on_the_dock",
    "target_description": "the nearest dark car on the dock",
    "source_state": "The nearest dark dockside car is parked at an oblique angle to the ferry ramp.",
    "desired_change": "The car is rotated to face directly toward the center of the ferry ramp."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      25,
      29
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 26 seconds, rotate the nearest dark car on the dock to face directly toward the center of the ferry ramp.",
  "expected_result": {
    "description": "The car is rotated to face directly toward the center of the ferry ramp.",
    "target_phrase": "dockside car facing the ferry ramp"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_051_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The car, ramp centerline, and surrounding concrete surface are visible from above."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_051_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the nearest dark car on the dock on B independently of E1's change to the first red-and-black upper-deck housing; both edit results must coexist in C."
  }
}
```

## synthetic_object_052

### synthetic_object_052_E1

```json
{
  "video_id": "synthetic_object_052",
  "edit_id": "synthetic_object_052_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_052.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_yacht_s_dark_side_window_band",
    "target_description": "the yacht's dark side-window band",
    "source_state": "The yacht has a continuous black side-window band along its white cabin.",
    "desired_change": "The dark side-window band becomes deep navy blue while retaining its shape and reflections."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      12,
      17
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 13 seconds, change the yacht's black side-window band to deep navy blue over the next two seconds.",
  "expected_result": {
    "description": "The dark side-window band becomes deep navy blue while retaining its shape and reflections.",
    "target_phrase": "deep-navy yacht window band"
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
      12,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cabin side and continuous window band are clear against the white hull and gray water."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_052_E2A

```json
{
  "video_id": "synthetic_object_052",
  "edit_id": "synthetic_object_052_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_052.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_yacht_relative_to_the_nearest_pale_water_marker",
    "target_description": "the yacht relative to the nearest pale water marker",
    "source_state": "The yacht passes with the nearest pale marker close beside its hull.",
    "desired_change": "The yacht is repositioned so the marker remains two yacht-widths off its starboard side."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, reposition the yacht so the nearest pale water marker remains two yacht-widths off its starboard side.",
  "expected_result": {
    "description": "The yacht is repositioned so the marker remains two yacht-widths off its starboard side.",
    "target_phrase": "yacht two widths from the marker"
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
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full yacht, marker, and open water gap are visible in the high rear-quarter view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_052_E2B

```json
{
  "video_id": "synthetic_object_052",
  "edit_id": "synthetic_object_052_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_052_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_yacht_s_forward_motion",
    "target_description": "the yacht's forward motion",
    "source_state": "The yacht travels at a steady speed with a narrow trailing wake.",
    "desired_change": "The yacht moves at one-and-a-half times its original forward speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      24.5,
      32.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 25.5 seconds, increase the yacht's forward speed to one-and-a-half times its original rate for five seconds.",
  "expected_result": {
    "description": "The yacht moves at one-and-a-half times its original forward speed for five seconds.",
    "target_phrase": "yacht moving one-and-a-half times faster"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_052_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete hull and lengthening wake provide continuous speed references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_052_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the yacht's forward motion on B independently of E1's change to the yacht's dark side-window band; both edit results must coexist in C."
  }
}
```

## synthetic_object_053

### synthetic_object_053_E1

```json
{
  "video_id": "synthetic_object_053",
  "edit_id": "synthetic_object_053_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_053.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_around_the_trawler_and_net",
    "target_description": "the camera path around the trawler and net",
    "source_state": "The camera observes the trawler and deployed net from a broad port-rear angle.",
    "desired_change": "The camera arcs smoothly to a centered view directly behind the deployed net."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      10.5,
      18.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 11.5 seconds, arc the camera smoothly from the trawler's port rear to a centered view behind the deployed net.",
  "expected_result": {
    "description": "The camera arcs smoothly to a centered view directly behind the deployed net.",
    "target_phrase": "centered camera view behind the net"
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
      10.5,
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The trawler, both net edges, tow lines, and horizon provide strong trajectory references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_053_E2A

```json
{
  "video_id": "synthetic_object_053",
  "edit_id": "synthetic_object_053_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_053.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_pale_deployed_fishing_net",
    "target_description": "the pale deployed fishing net",
    "source_state": "The deployed fishing net is pale gray with dark edge weights.",
    "desired_change": "The net mesh becomes bright orange while its dark edge weights remain visually distinct."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31 seconds, change the deployed fishing net's pale-gray mesh to bright orange over the next two seconds.",
  "expected_result": {
    "description": "The net mesh becomes bright orange while its dark edge weights remain visually distinct.",
    "target_phrase": "bright-orange deployed net"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The broad mesh surface and dark weighted edge are unobstructed in the close rear view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_053_E2B

```json
{
  "video_id": "synthetic_object_053",
  "edit_id": "synthetic_object_053_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_053_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_water_beside_the_net_s_left_corner",
    "target_description": "the open water beside the net's left corner",
    "source_state": "No red float is attached beside the net's left trailing corner.",
    "desired_change": "One red spherical float is added beside and connected to the net's left trailing corner."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 25,
    "evaluation_window_sec": [
      23,
      27
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24 seconds, add one red spherical float beside the deployed net's left trailing corner and connect it to the edge line.",
  "expected_result": {
    "description": "One red spherical float is added beside and connected to the net's left trailing corner.",
    "target_phrase": "red float on the net's left corner"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_053_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      27
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The corner, edge line, and adjacent open water remain stable and unobstructed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_053_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the open water beside the net's left corner on B independently of E1's change to the camera path around the trawler and net; both edit results must coexist in C."
  }
}
```

## synthetic_object_054

### synthetic_object_054_E1

```json
{
  "video_id": "synthetic_object_054",
  "edit_id": "synthetic_object_054_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_suspended_red_buoy_relative_to_the_workboat",
    "target_description": "the suspended red buoy relative to the workboat",
    "source_state": "The suspended red buoy hangs close to the workboat's starboard side on an attached crane cable.",
    "desired_change": "The buoy is shifted two buoy-widths farther outboard while the attached cable becomes diagonally extended."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      12.5,
      16.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13.5 seconds, shift the suspended red buoy two buoy-widths farther from the workboat's right side.",
  "expected_result": {
    "description": "The buoy is shifted two buoy-widths farther outboard while the attached cable becomes diagonally extended.",
    "target_phrase": "suspended red buoy shifted farther outboard"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "crane-cable attachment to the buoy",
      "diagonal cable connection from the boom tip to the shifted buoy"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy, hull edge, crane cable, boom tip, and open water are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_054_E2A

```json
{
  "video_id": "synthetic_object_054",
  "edit_id": "synthetic_object_054_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_054.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_water_around_the_suspended_buoy",
    "target_description": "the water around the suspended buoy",
    "source_state": "The water around the buoy has only fine irregular ripples.",
    "desired_change": "Three broad circular ripple rings travel outward from beneath the buoy."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      19.5,
      27.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 20.5 seconds, make three broad circular ripple rings travel outward across the water beneath the suspended buoy.",
  "expected_result": {
    "description": "Three broad circular ripple rings travel outward from beneath the buoy.",
    "target_phrase": "three ripple rings beneath the buoy"
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
      19.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy's position and surrounding open water remain identifiable as the camera moves around the vessel."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_054_E2B

```json
{
  "video_id": "synthetic_object_054",
  "edit_id": "synthetic_object_054_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_054_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_suspended_red_buoy",
    "target_description": "the suspended red buoy",
    "source_state": "The suspended buoy has a saturated red surface with a dark lower edge.",
    "desired_change": "The buoy's red surface becomes bright safety yellow while retaining the dark lower edge."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, change the suspended buoy from saturated red to bright safety yellow over two seconds.",
  "expected_result": {
    "description": "The buoy's red surface becomes bright safety yellow while retaining the dark lower edge.",
    "target_phrase": "bright safety-yellow suspended buoy"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_054_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy remains visible below the boom and separated from the dark hull."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_054_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the suspended red buoy on B independently of E1's change to the suspended red buoy relative to the workboat; both edit results must coexist in C."
  }
}
```

## synthetic_object_055

### synthetic_object_055_E1

```json
{
  "video_id": "synthetic_object_055",
  "edit_id": "synthetic_object_055_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_055.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_small_light_gray_landing_platform_on_the_far_bank",
    "target_description": "the small light-gray landing platform on the far bank",
    "source_state": "A small light-gray landing platform projects from the far bank above the cargo ship.",
    "desired_change": "The small projecting landing platform is removed from the far riverbank."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      10.5,
      14.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 11.5 seconds, remove the small light-gray landing platform projecting from the far riverbank above the cargo ship.",
  "expected_result": {
    "description": "The small projecting landing platform is removed from the far riverbank.",
    "target_phrase": "far-bank landing platform removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      10.5,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The platform is isolated against grass and shoreline and does not overlap the vessel."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_055_E2A

```json
{
  "video_id": "synthetic_object_055",
  "edit_id": "synthetic_object_055_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_055.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Cargo-ship Exterior Color Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cargo_ship_s_white_and_green_exterior",
    "target_description": "the cargo ship's white-and-green exterior",
    "source_state": "The cargo ship has a predominantly white exterior with green hull and deck sections.",
    "desired_change": "The ship's white-and-green exterior becomes a unified deep navy blue."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 34,
    "evaluation_window_sec": [
      31,
      36
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 32 seconds, change the cargo ship's white-and-green exterior to a unified deep navy blue over two seconds.",
  "expected_result": {
    "description": "The ship's white-and-green exterior becomes a unified deep navy blue.",
    "target_phrase": "deep navy-blue cargo ship"
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
      31,
      36
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The long cargo ship is fully visible after emerging beyond the bridge."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_055_E2B

```json
{
  "video_id": "synthetic_object_055",
  "edit_id": "synthetic_object_055_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_055_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_long_cargo_ship_s_path_before_the_bridge",
    "target_description": "the long cargo ship's path before the bridge",
    "source_state": "The cargo ship approaches the bridge along a straight channel path.",
    "desired_change": "The cargo ship follows one shallow S-shaped path while remaining between the bridge supports."
  },
  "timing": {
    "edit_point_sec": 23.5,
    "effect_start_sec": 23.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      22.5,
      30.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 23.5 seconds, make the long cargo ship follow one shallow S-shaped path while remaining between the bridge supports.",
  "expected_result": {
    "description": "The cargo ship follows one shallow S-shaped path while remaining between the bridge supports.",
    "target_phrase": "cargo ship following a shallow S-path"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_055_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full channel width, bridge span, and long vessel axis remain visible from above."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_055_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the long cargo ship's path before the bridge on B independently of E1's change to the small light-gray landing platform on the far bank; both edit results must coexist in C."
  }
}
```

## synthetic_object_056

### synthetic_object_056_E1

```json
{
  "video_id": "synthetic_object_056",
  "edit_id": "synthetic_object_056_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Illumination Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_black_gondola_and_standing_paddler",
    "target_description": "the black gondola and standing paddler",
    "source_state": "The gondola and standing paddler receive flat ambient daylight.",
    "desired_change": "A warm directional spotlight illuminates the full gondola and paddler from above-left."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      12.5,
      17.5
    ],
    "temporal_behavior": "gradual persistent illumination change"
  },
  "instruction": "Starting at 13.5 seconds, illuminate the full black gondola and standing paddler with a warm spotlight from above-left.",
  "expected_result": {
    "description": "A warm directional spotlight illuminates the full gondola and paddler from above-left.",
    "target_phrase": "warm spotlight on the gondola and paddler"
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
      12.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dark boat and person are separated clearly from the pale facade and green water."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_056_E2A

```json
{
  "video_id": "synthetic_object_056",
  "edit_id": "synthetic_object_056_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_056.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_gondola_s_central_red_passenger_seat",
    "target_description": "the gondola's central red passenger seat",
    "source_state": "A red passenger seat occupies the middle of the black gondola.",
    "desired_change": "The red passenger seat is replaced by a blue upholstered bench of matching width."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, replace the gondola's central red passenger seat with a blue upholstered bench of matching width.",
  "expected_result": {
    "description": "The red passenger seat is replaced by a blue upholstered bench of matching width.",
    "target_phrase": "blue upholstered bench in the gondola"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The central seat is visible between the standing paddler and the raised bow ornament."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_056_E2B

```json
{
  "video_id": "synthetic_object_056",
  "edit_id": "synthetic_object_056_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_056_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_standing_paddler_and_long_wooden_oar",
    "target_description": "the standing paddler and long wooden oar",
    "source_state": "The paddler repeats ordinary forward strokes with the long wooden oar.",
    "desired_change": "The paddler lifts the oar clear of the water, spins it once, and resumes rowing."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 29.5,
    "evaluation_window_sec": [
      24.5,
      31.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 25.5 seconds, make the standing paddler lift the wooden oar, spin it once, and resume rowing.",
  "expected_result": {
    "description": "The paddler lifts the oar clear of the water, spins it once, and resumes rowing.",
    "target_phrase": "paddler spinning the oar once"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_056_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      31.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full upper body, both hands, long oar, and open water beside the gondola are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_056_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the standing paddler and long wooden oar on B independently of E1's change to the black gondola and standing paddler; both edit results must coexist in C."
  }
}
```

## synthetic_object_057

### synthetic_object_057_E1

```json
{
  "video_id": "synthetic_object_057",
  "edit_id": "synthetic_object_057_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_057.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_orange_motorboat_crossing_the_cargo_ship_s_wake",
    "target_description": "the orange motorboat crossing the cargo ship's wake",
    "source_state": "The orange motorboat travels beside the cargo ship without a distinct wake crossing.",
    "desired_change": "The motorboat crosses the cargo ship's wake, rolls once to starboard, and levels out."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      12,
      19
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 13 seconds, make the orange motorboat cross the cargo ship's wake, roll once to starboard, and level out.",
  "expected_result": {
    "description": "The motorboat crosses the cargo ship's wake, rolls once to starboard, and levels out.",
    "target_phrase": "motorboat rolling across the cargo wake"
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
      12,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The small boat, large hull, intervening wake, and open recovery path are continuously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_057_E2A

```json
{
  "video_id": "synthetic_object_057",
  "edit_id": "synthetic_object_057_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_057.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_orange_motorboat_s_white_roof_hatch",
    "target_description": "the orange motorboat's white roof hatch",
    "source_state": "The white roof hatch above the cabin is closed and flush with the roof.",
    "desired_change": "The roof hatch becomes fully open and remains raised above the cabin."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 31 seconds, open the orange motorboat's white roof hatch fully and leave it raised above the cabin.",
  "expected_result": {
    "description": "The roof hatch becomes fully open and remains raised above the cabin.",
    "target_phrase": "white roof hatch fully open"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cabin roof is visible against the dark cargo-ship bow and open sky."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_057_E2B

```json
{
  "video_id": "synthetic_object_057",
  "edit_id": "synthetic_object_057_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_057_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_small_white_radar_dome_above_the_cabin",
    "target_description": "the small white radar dome above the cabin",
    "source_state": "A small white radar dome stands above the motorboat's cabin roof.",
    "desired_change": "The small white radar dome above the cabin is removed."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      24.5,
      28.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25.5 seconds, remove the small white radar dome mounted above the orange motorboat's cabin.",
  "expected_result": {
    "description": "The small white radar dome above the cabin is removed.",
    "target_phrase": "white cabin radar dome removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_057_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The dome is isolated above the darker windows and does not overlap the mast."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_057_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the small white radar dome above the cabin on B independently of E1's change to the orange motorboat crossing the cargo ship's wake; both edit results must coexist in C."
  }
}
```

## synthetic_object_058

### synthetic_object_058_E1

```json
{
  "video_id": "synthetic_object_058",
  "edit_id": "synthetic_object_058_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_058.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_suspended_buoy_lowering_process",
    "target_description": "the suspended buoy lowering process",
    "source_state": "The red buoy begins descending slowly and does not touch the water until around 23 seconds.",
    "desired_change": "The lowering process advances faster so the buoy first touches the water by 16 seconds."
  },
  "timing": {
    "edit_point_sec": 10.5,
    "effect_start_sec": 10.5,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      9.5,
      18
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 10.5 seconds, accelerate the buoy-lowering process so the red buoy first touches the water by 16 seconds.",
  "expected_result": {
    "description": "The lowering process advances faster so the buoy first touches the water by 16 seconds.",
    "target_phrase": "red buoy touching the water by 16 seconds"
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
      9.5,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy, vertical cable, boat rail, and waterline show a continuous measurable descent."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_058_E2A

```json
{
  "video_id": "synthetic_object_058",
  "edit_id": "synthetic_object_058_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_058.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tethered_red_buoy",
    "target_description": "the tethered red buoy",
    "source_state": "The tethered buoy remains nearly stationary at the water surface with slight incidental motion.",
    "desired_change": "The tethered buoy performs three clear vertical bobs while remaining connected to the crane cable."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      29,
      37
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 30 seconds, make the tethered red buoy perform three clear vertical bobs while remaining connected to the crane cable.",
  "expected_result": {
    "description": "The tethered buoy performs three clear vertical bobs while remaining connected to the crane cable.",
    "target_phrase": "tethered buoy bobbing three times"
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
      29,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy, cable, and waterline remain fully visible in the fixed side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_058_E2B

```json
{
  "video_id": "synthetic_object_058",
  "edit_id": "synthetic_object_058_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_058_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_red_conical_buoy",
    "target_description": "the red conical buoy",
    "source_state": "The conical buoy has a saturated red surface and dark lower rim.",
    "desired_change": "The buoy surface becomes vivid safety orange while retaining the dark lower rim."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      23,
      28
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 24 seconds, change the conical buoy from saturated red to vivid safety orange over the next two seconds.",
  "expected_result": {
    "description": "The buoy surface becomes vivid safety orange while retaining the dark lower rim.",
    "target_phrase": "vivid safety-orange conical buoy"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_058_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The buoy is clearly separated from the blue boat, crane, and pale harbor background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_058_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red conical buoy on B independently of E1's change to the suspended buoy lowering process; both edit results must coexist in C."
  }
}
```

## synthetic_object_059

### synthetic_object_059_E1

```json
{
  "video_id": "synthetic_object_059",
  "edit_id": "synthetic_object_059_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_059.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_motorboat_s_trailing_wake",
    "target_description": "the motorboat's trailing wake",
    "source_state": "The motorboat leaves one broad white wake with finer surrounding ripples.",
    "desired_change": "The trailing wake divides into three distinct parallel ripple bands for five seconds."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      11.5,
      19.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 12.5 seconds, make the motorboat's trailing wake divide into three distinct parallel ripple bands for five seconds.",
  "expected_result": {
    "description": "The trailing wake divides into three distinct parallel ripple bands for five seconds.",
    "target_phrase": "three parallel bands in the wake"
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
      11.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The boat and a long unobstructed wake region are simultaneously visible beside the breakwater."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_059_E2A

```json
{
  "video_id": "synthetic_object_059",
  "edit_id": "synthetic_object_059_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_059.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Background Style Change",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_stone_breakwater_behind_the_motorboat",
    "target_description": "the stone breakwater behind the motorboat",
    "source_state": "The background breakwater has realistic irregular gray-brown stone texture.",
    "desired_change": "Only the background breakwater is rendered as a soft hand-painted watercolor band."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      33,
      38
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 34 seconds, render only the stone breakwater behind the motorboat as a soft hand-painted watercolor band.",
  "expected_result": {
    "description": "Only the background breakwater is rendered as a soft hand-painted watercolor band.",
    "target_phrase": "watercolor stone breakwater"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The breakwater forms a continuous background band clearly separated from the boat and water."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_059_E2B

```json
{
  "video_id": "synthetic_object_059",
  "edit_id": "synthetic_object_059_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_059_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_motorboat_relative_to_the_stone_breakwater",
    "target_description": "the motorboat relative to the stone breakwater",
    "source_state": "The turning motorboat remains several boat-lengths away from the stone breakwater.",
    "desired_change": "The motorboat is repositioned one boat-length closer to the breakwater while retaining its heading."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      24.5,
      28.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25.5 seconds, move the motorboat one boat-length closer to the stone breakwater.",
  "expected_result": {
    "description": "The motorboat is repositioned one boat-length closer to the breakwater while retaining its heading.",
    "target_phrase": "motorboat one length closer to the breakwater"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "motorboat heading through the broad turn",
      "visual result of synthetic_object_059_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full boat, stone barrier, and open water gap are visible during the broad turn."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_059_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the motorboat relative to the stone breakwater on B independently of E1's change to the motorboat's trailing wake; both edit results must coexist in C."
  }
}
```

## synthetic_object_060

### synthetic_object_060_E1

```json
{
  "video_id": "synthetic_object_060",
  "edit_id": "synthetic_object_060_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_060.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_underwater_vehicle_s_near_side_wingtip",
    "target_description": "the underwater vehicle's near-side wingtip",
    "source_state": "The near-side yellow wingtip is straight and rigid.",
    "desired_change": "The near-side wingtip becomes visibly bent upward while the remaining wing stays straight."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      12.5,
      17.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 13.5 seconds, bend the underwater vehicle's near-side yellow wingtip visibly upward over the next two seconds.",
  "expected_result": {
    "description": "The near-side wingtip becomes visibly bent upward while the remaining wing stays straight.",
    "target_phrase": "upward-bent near-side wingtip"
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
      12.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The long near-side wing and its outer tip are unobstructed against the pale seabed."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_060_E2A

```json
{
  "video_id": "synthetic_object_060",
  "edit_id": "synthetic_object_060_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_060.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_underwater_vehicle_s_forward_motion",
    "target_description": "the underwater vehicle's forward motion",
    "source_state": "The yellow underwater vehicle travels steadily above the seabed.",
    "desired_change": "The vehicle moves at half its original forward speed for five seconds along the same path."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      30,
      38
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 31 seconds, reduce the underwater vehicle's forward speed to half its original rate for the next five seconds.",
  "expected_result": {
    "description": "The vehicle moves at half its original forward speed for five seconds along the same path.",
    "target_phrase": "underwater vehicle moving at half speed"
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
      30,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Seabed rocks and sand texture provide stable continuous displacement references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_060_E2B

```json
{
  "video_id": "synthetic_object_060",
  "edit_id": "synthetic_object_060_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_060_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_small_dark_dorsal_protrusion",
    "target_description": "the small dark dorsal protrusion",
    "source_state": "A small dark protrusion stands on top of the vehicle's middle fuselage.",
    "desired_change": "The small dark dorsal protrusion is removed from the fuselage."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      25,
      29
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 26 seconds, remove the small dark protrusion mounted on top of the underwater vehicle's middle fuselage.",
  "expected_result": {
    "description": "The small dark dorsal protrusion is removed from the fuselage.",
    "target_phrase": "dark dorsal protrusion removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_060_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The protrusion is silhouetted against blue water and separated from the tail fins."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_060_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the small dark dorsal protrusion on B independently of E1's change to the underwater vehicle's near-side wingtip; both edit results must coexist in C."
  }
}
```

## synthetic_object_061

### synthetic_object_061_E1

```json
{
  "video_id": "synthetic_object_061",
  "edit_id": "synthetic_object_061_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_061.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Illumination Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_metal_gear_held_by_the_robot_gripper",
    "target_description": "the metal gear held by the robot gripper",
    "source_state": "The silver gear receives diffuse factory lighting with moderate reflections.",
    "desired_change": "A cool circular inspection light illuminates the entire gear and emphasizes every outer tooth."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      11,
      16
    ],
    "temporal_behavior": "gradual persistent illumination change"
  },
  "instruction": "Starting at 12 seconds, illuminate the gripped metal gear with a cool circular inspection light over the next two seconds.",
  "expected_result": {
    "description": "A cool circular inspection light illuminates the entire gear and emphasizes every outer tooth.",
    "target_phrase": "gear illuminated by a cool inspection ring"
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
      11,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The gear is lifted into a clear frontal view with its teeth and center opening visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_061_E2A

```json
{
  "video_id": "synthetic_object_061",
  "edit_id": "synthetic_object_061_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_061.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_gear_relative_to_the_right_fixture_recess",
    "target_description": "the gear relative to the right fixture recess",
    "source_state": "The carried gear is slightly offset from the circular recess in the right fixture.",
    "desired_change": "The gear's center opening is positioned directly above and concentric with the fixture recess."
  },
  "timing": {
    "edit_point_sec": 23.5,
    "effect_start_sec": 23.5,
    "effect_end_sec": 24.5,
    "evaluation_window_sec": [
      22.5,
      26.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 23.5 seconds, center the gear's opening directly above the circular recess in the right fixture.",
  "expected_result": {
    "description": "The gear's center opening is positioned directly above and concentric with the fixture recess.",
    "target_phrase": "gear concentric with the fixture recess"
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
      22.5,
      26.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The gear opening, fixture rim, and gripper alignment are visible during the downward approach."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_061_E2B

```json
{
  "video_id": "synthetic_object_061",
  "edit_id": "synthetic_object_061_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_061_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_gripped_gear_during_its_descent",
    "target_description": "the gripped gear during its descent",
    "source_state": "The gripped gear descends without a deliberate rotation around its center axis.",
    "desired_change": "The gear completes one full axial rotation while descending toward the right fixture."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      23.5,
      30.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 24.5 seconds, make the gripped gear complete one full axial rotation while descending toward the right fixture.",
  "expected_result": {
    "description": "The gear completes one full axial rotation while descending toward the right fixture.",
    "target_phrase": "gear rotating once during descent"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_061_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The gear remains rigidly held and fully visible above the right fixture during the selected interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_061_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the gripped gear during its descent on B independently of E1's change to the metal gear held by the robot gripper; both edit results must coexist in C."
  }
}
```

## synthetic_object_062

### synthetic_object_062_E1

```json
{
  "video_id": "synthetic_object_062",
  "edit_id": "synthetic_object_062_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_loaded_warehouse_carrier_s_turning_motion",
    "target_description": "the loaded warehouse carrier's turning motion",
    "source_state": "The carrier and raised storage frame perform a steady turn in the aisle.",
    "desired_change": "The carrier completes the same turn at twice its original angular speed."
  },
  "timing": {
    "edit_point_sec": 11.5,
    "effect_start_sec": 11.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      10.5,
      16.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 11.5 seconds, make the loaded warehouse carrier complete its aisle turn at twice the original angular speed.",
  "expected_result": {
    "description": "The carrier completes the same turn at twice its original angular speed.",
    "target_phrase": "warehouse carrier turning twice as fast"
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
      10.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The orange base, elevated frame, cartons, floor lines, and side racks provide stable motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_062_E2A

```json
{
  "video_id": "synthetic_object_062",
  "edit_id": "synthetic_object_062_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_062.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Stop-before-lift Process Ordering",
    "scope": "Multiple Core-object Processes"
  },
  "target": {
    "target_id": "the_loaded_carrier_s_stopping_and_cargo_lifting_processes",
    "target_description": "the loaded carrier's stopping and cargo-lifting processes",
    "source_state": "The loaded carrier moves across the striped floor grid while holding its cargo frame at the current height.",
    "desired_change": "The carrier first stops completely inside the striped grid and only afterward raises the loaded cargo frame higher."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      25,
      35
    ],
    "temporal_behavior": "relative event reordering"
  },
  "instruction": "Starting at 26 seconds, make the loaded carrier stop completely inside the striped floor grid before raising its cargo frame higher.",
  "expected_result": {
    "description": "The carrier first stops completely inside the striped grid and only afterward raises the loaded cargo frame higher.",
    "target_phrase": "carrier stopped in the grid before raising cargo"
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
      25,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The carrier footprint, striped grid, vertical cargo frame, and lift height provide two independently visible process milestones."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_062_E2B

```json
{
  "video_id": "synthetic_object_062",
  "edit_id": "synthetic_object_062_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_062_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_front_row_of_brown_cartons_on_the_raised_pallet",
    "target_description": "the front row of brown cartons on the raised pallet",
    "source_state": "A front row of brown cardboard cartons occupies the raised pallet frame.",
    "desired_change": "The front carton row is replaced by three blue reusable plastic crates of matching total width."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      23.5,
      27.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.5 seconds, replace the front row of brown cartons on the raised pallet with three blue reusable plastic crates.",
  "expected_result": {
    "description": "The front carton row is replaced by three blue reusable plastic crates of matching total width.",
    "target_phrase": "three blue crates on the raised pallet"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_062_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The front carton faces are broad, unobstructed, and separated from the fixed warehouse racks."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_062_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the front row of brown cartons on the raised pallet on B independently of E1's change to the loaded warehouse carrier's turning motion; both edit results must coexist in C."
  }
}
```

## synthetic_object_063

### synthetic_object_063_E1

```json
{
  "video_id": "synthetic_object_063",
  "edit_id": "synthetic_object_063_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_063.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_humanoid_robot_s_standing_up_process",
    "target_description": "the humanoid robot's standing-up process",
    "source_state": "The seated robot continues extending its hips and knees and becomes upright around 10 seconds.",
    "desired_change": "The standing-up process advances faster so the robot reaches a stable upright posture by 8 seconds."
  },
  "timing": {
    "edit_point_sec": 6,
    "effect_start_sec": 6,
    "effect_end_sec": 8,
    "evaluation_window_sec": [
      5,
      10
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 6 seconds, accelerate the humanoid robot's standing-up process so it reaches a stable upright posture by 8 seconds.",
  "expected_result": {
    "description": "The standing-up process advances faster so the robot reaches a stable upright posture by 8 seconds.",
    "target_phrase": "robot standing upright by 8 seconds"
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
      5,
      10
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The chair, hips, knees, feet, and increasing seat gap show the continuous rise clearly."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_063_E2A

```json
{
  "video_id": "synthetic_object_063",
  "edit_id": "synthetic_object_063_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_063.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_black_four_legged_chair_behind_the_robot",
    "target_description": "the black four-legged chair behind the robot",
    "source_state": "A black four-legged chair remains directly behind the standing robot.",
    "desired_change": "The chair is replaced by a silver backless metal stool of comparable seat height."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      27,
      31
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 28 seconds, replace the black four-legged chair behind the humanoid robot with a silver backless metal stool.",
  "expected_result": {
    "description": "The chair is replaced by a silver backless metal stool of comparable seat height.",
    "target_phrase": "silver backless stool behind the robot"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The chair remains stationary and visibly separated from the robot's legs in the side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_063_E2B

```json
{
  "video_id": "synthetic_object_063",
  "edit_id": "synthetic_object_063_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_063_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_humanoid_robot_s_right_forearm_and_hand",
    "target_description": "the humanoid robot's right forearm and hand",
    "source_state": "The standing robot keeps its right arm close to its side with only minor posture changes.",
    "desired_change": "The robot raises its right forearm to chest height, waves twice, and lowers it."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 24.5,
    "evaluation_window_sec": [
      19.5,
      26.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 20.5 seconds, make the humanoid robot raise its right forearm, wave twice at chest height, and lower it.",
  "expected_result": {
    "description": "The robot raises its right forearm to chest height, waves twice, and lowers it.",
    "target_phrase": "robot waving its right hand twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_063_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.5,
      26.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right elbow, forearm, and hand remain visible beside the stationary torso and chair."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_063_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the humanoid robot's right forearm and hand on B independently of E1's change to the humanoid robot's standing-up process; both edit results must coexist in C."
  }
}
```

## synthetic_object_064

### synthetic_object_064_E1

```json
{
  "video_id": "synthetic_object_064",
  "edit_id": "synthetic_object_064_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_over_the_quadruped_robot",
    "target_description": "the camera path over the quadruped robot",
    "source_state": "The camera tracks the robot from a low lateral view as it crosses the wooden platform.",
    "desired_change": "The camera arcs upward to a near-overhead tracking view while the robot completes the crossing."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      11,
      19
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 12 seconds, arc the camera upward into a near-overhead tracking view as the quadruped robot crosses the wooden platform.",
  "expected_result": {
    "description": "The camera arcs upward to a near-overhead tracking view while the robot completes the crossing.",
    "target_phrase": "near-overhead tracking view of the quadruped"
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
      11,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The robot, platform slats, gravel edges, and wall provide strong depth and path references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_064_E2A

```json
{
  "video_id": "synthetic_object_064",
  "edit_id": "synthetic_object_064_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_064.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_robot_s_front_foot_and_a_loose_gravel_pebble",
    "target_description": "the robot's front foot and a loose gravel pebble",
    "source_state": "The robot's front foot steps among loose gravel without a distinct displaced pebble.",
    "desired_change": "The front foot kicks one visible pebble forward and the pebble rolls to a stop."
  },
  "timing": {
    "edit_point_sec": 29,
    "effect_start_sec": 29,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      28,
      35
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 29 seconds, make the quadruped robot's front foot kick one visible pebble forward until it rolls to a stop.",
  "expected_result": {
    "description": "The front foot kicks one visible pebble forward and the pebble rolls to a stop.",
    "target_phrase": "front foot kicking one pebble forward"
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
      28,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The front legs and granular ground remain unobstructed during continuous walking."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_064_E2B

```json
{
  "video_id": "synthetic_object_064",
  "edit_id": "synthetic_object_064_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_064_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_red_tipped_sensor_mast_on_the_robot",
    "target_description": "the red-tipped sensor mast on the robot",
    "source_state": "The short red-tipped sensor mast stands upright on top of the robot's body.",
    "desired_change": "The sensor mast folds backward until it lies flat against the upper body."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      23.5,
      28.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 24.5 seconds, fold the quadruped robot's red-tipped sensor mast backward until it lies flat against the body.",
  "expected_result": {
    "description": "The sensor mast folds backward until it lies flat against the upper body.",
    "target_phrase": "sensor mast folded flat"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_064_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The top of the dark body and red-tipped vertical element are silhouetted against the pale wall."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_064_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red-tipped sensor mast on the robot on B independently of E1's change to the camera path over the quadruped robot; both edit results must coexist in C."
  }
}
```

## synthetic_object_065

### synthetic_object_065_E1

```json
{
  "video_id": "synthetic_object_065",
  "edit_id": "synthetic_object_065_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_065.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_loose_bright_metal_chips_along_the_groove_s_front_edge",
    "target_description": "the loose bright metal chips along the groove's front edge",
    "source_state": "Several loose bright metal chips lie along the machined groove's front edge.",
    "desired_change": "The loose metal chips along the front groove edge are removed."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      12.5,
      16.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13.5 seconds, remove the loose bright metal chips scattered along the front edge of the machined groove.",
  "expected_result": {
    "description": "The loose metal chips along the front groove edge are removed.",
    "target_phrase": "loose groove-edge chips removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The chips are distinct from the fixed workpiece, vise jaws, and rotating cutting tool."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_065_E2A

```json
{
  "video_id": "synthetic_object_065",
  "edit_id": "synthetic_object_065_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_065.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_milling_table_s_feed_motion",
    "target_description": "the milling table's feed motion",
    "source_state": "The clamped workpiece advances beneath the fixed spindle at a steady feed rate.",
    "desired_change": "The milling table advances at one-and-a-half times its original feed rate for five seconds."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      29,
      37
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 30 seconds, increase the milling table's feed motion to one-and-a-half times its original rate for five seconds.",
  "expected_result": {
    "description": "The milling table advances at one-and-a-half times its original feed rate for five seconds.",
    "target_phrase": "milling table feeding one-and-a-half times faster"
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
      29,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stationary spindle housing and moving vise provide clear relative displacement references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_065_E2B

```json
{
  "video_id": "synthetic_object_065",
  "edit_id": "synthetic_object_065_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_065_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_rear_wall_of_the_machining_enclosure",
    "target_description": "the rear wall of the machining enclosure",
    "source_state": "The machining enclosure has a bare light-gray metal rear wall.",
    "desired_change": "The rear enclosure wall becomes lined with dark-blue oil-resistant panels."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, line the machining enclosure's light-gray rear wall with dark-blue oil-resistant panels over two seconds.",
  "expected_result": {
    "description": "The rear enclosure wall becomes lined with dark-blue oil-resistant panels.",
    "target_phrase": "dark-blue enclosure wall panels"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_065_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The broad rear wall remains visible around the spindle and above the clamped workpiece."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_065_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the rear wall of the machining enclosure on B independently of E1's change to the loose bright metal chips along the groove's front edge; both edit results must coexist in C."
  }
}
```

## synthetic_object_066

### synthetic_object_066_E1

```json
{
  "video_id": "synthetic_object_066",
  "edit_id": "synthetic_object_066_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_066.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_3d_printer_s_golden_build_platform",
    "target_description": "the 3D printer's golden build platform",
    "source_state": "The build platform has a plain reflective golden surface around the white print.",
    "desired_change": "The platform surface becomes matte black with a fine pale-blue alignment grid."
  },
  "timing": {
    "edit_point_sec": 12.5,
    "effect_start_sec": 12.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      11.5,
      16.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12.5 seconds, change the 3D printer's golden build platform to matte black with a pale-blue alignment grid.",
  "expected_result": {
    "description": "The platform surface becomes matte black with a fine pale-blue alignment grid.",
    "target_phrase": "black build platform with blue grid"
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
      11.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad platform area remains exposed around the low white printed structure."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_066_E2A

```json
{
  "video_id": "synthetic_object_066",
  "edit_id": "synthetic_object_066_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_066.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_printer_nozzle_and_white_rectangular_structure",
    "target_description": "the printer nozzle and white rectangular structure",
    "source_state": "The nozzle deposits material along the existing perimeter and parallel inner ribs.",
    "desired_change": "The nozzle deposits two diagonal braces that visibly bond opposite corners of the white frame."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 35,
    "evaluation_window_sec": [
      29,
      37
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 30 seconds, make the printer nozzle deposit two diagonal braces connecting opposite corners of the white rectangular frame.",
  "expected_result": {
    "description": "The nozzle deposits two diagonal braces that visibly bond opposite corners of the white frame.",
    "target_phrase": "two printed diagonal braces"
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
      29,
      37
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The nozzle, open interior, opposite frame corners, and fresh white material remain visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_066_E2B

```json
{
  "video_id": "synthetic_object_066",
  "edit_id": "synthetic_object_066_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_066_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_brass_printer_nozzle",
    "target_description": "the brass printer nozzle",
    "source_state": "A narrow brass nozzle projects below the black print-head housing.",
    "desired_change": "The brass nozzle is replaced by a wider silver-steel nozzle attached to the same housing."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      24,
      28
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25 seconds, replace the narrow brass printer nozzle with a wider silver-steel nozzle attached beneath the same print head.",
  "expected_result": {
    "description": "The brass nozzle is replaced by a wider silver-steel nozzle attached to the same housing.",
    "target_phrase": "wider silver-steel printer nozzle"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_066_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The nozzle is isolated beneath the black circular fan housing and above the white print."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_066_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the brass printer nozzle on B independently of E1's change to the 3D printer's golden build platform; both edit results must coexist in C."
  }
}
```

## synthetic_object_067

### synthetic_object_067_E1

```json
{
  "video_id": "synthetic_object_067",
  "edit_id": "synthetic_object_067_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_067.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_suspended_beam_s_horizontal_transfer",
    "target_description": "the suspended beam's horizontal transfer",
    "source_state": "The crane transfers the suspended beam horizontally at a steady rate.",
    "desired_change": "The beam and hook assembly move at one-and-a-half times their original horizontal speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 11,
    "effect_start_sec": 11,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      10,
      18
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 11 seconds, increase the suspended beam's horizontal transfer speed to one-and-a-half times its original rate for five seconds.",
  "expected_result": {
    "description": "The beam and hook assembly move at one-and-a-half times their original horizontal speed for five seconds.",
    "target_phrase": "suspended beam moving one-and-a-half times faster"
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
      10,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The crane mast, jib, hook, beam, and repeated steel columns provide stable displacement references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_067_E2A

```json
{
  "video_id": "synthetic_object_067",
  "edit_id": "synthetic_object_067_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_067.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_suspended_dark_brown_beam",
    "target_description": "the suspended dark-brown beam",
    "source_state": "The long suspended beam has a dark-brown metal surface.",
    "desired_change": "The full beam becomes bright safety yellow while both lifting slings remain distinct."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31 seconds, change the suspended dark-brown beam to bright safety yellow over the next two seconds.",
  "expected_result": {
    "description": "The full beam becomes bright safety yellow while both lifting slings remain distinct.",
    "target_phrase": "bright safety-yellow suspended beam"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The beam remains horizontal and unobstructed above the darker structural frame."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_067_E2B

```json
{
  "video_id": "synthetic_object_067",
  "edit_id": "synthetic_object_067_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_067_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_orange_crane_hook_block",
    "target_description": "the orange crane hook block",
    "source_state": "A single orange hook block supports the two angled lifting slings.",
    "desired_change": "The orange hook block is replaced by a blue double-hook block supporting the same two slings."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 25,
    "evaluation_window_sec": [
      23,
      27
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24 seconds, replace the orange crane hook block with a blue double-hook block supporting the same two lifting slings.",
  "expected_result": {
    "description": "The orange hook block is replaced by a blue double-hook block supporting the same two slings.",
    "target_phrase": "blue double-hook crane block"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_067_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      27
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The block is centered below the jib and clearly separated from the beam and red lattice."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_067_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the orange crane hook block on B independently of E1's change to the suspended beam's horizontal transfer; both edit results must coexist in C."
  }
}
```

## synthetic_object_068

### synthetic_object_068_E1

```json
{
  "video_id": "synthetic_object_068",
  "edit_id": "synthetic_object_068_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_combine_header_relative_to_the_standing_crop",
    "target_description": "the combine header relative to the standing crop",
    "source_state": "The combine header runs along the boundary between standing crop and cut stubble.",
    "desired_change": "The combine is positioned half a header-depth farther into the standing crop while preserving its direction."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, move the combine header half a header-depth farther into the standing crop.",
  "expected_result": {
    "description": "The combine is positioned half a header-depth farther into the standing crop while preserving its direction.",
    "target_phrase": "combine header deeper into standing crop"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "combine forward travel direction"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The wide header and sharp crop-height boundary are continuously visible from above."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_068_E2A

```json
{
  "video_id": "synthetic_object_068",
  "edit_id": "synthetic_object_068_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_068.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_combine_s_harvesting_progress",
    "target_description": "the combine's harvesting progress",
    "source_state": "The combine extends the cut strip gradually along the crop boundary.",
    "desired_change": "The harvesting advances faster until three additional header-widths of crop are reduced to short stubble by 29 seconds."
  },
  "timing": {
    "edit_point_sec": 23,
    "effect_start_sec": 23,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      22,
      31
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 23 seconds, accelerate the combine's harvesting until three additional header-widths become short stubble by 29 seconds.",
  "expected_result": {
    "description": "The harvesting advances faster until three additional header-widths of crop are reduced to short stubble by 29 seconds.",
    "target_phrase": "three additional header-widths harvested"
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
      22,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The rotating header, standing crop edge, and newly exposed stubble form a directional progress measure."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_068_E2B

```json
{
  "video_id": "synthetic_object_068",
  "edit_id": "synthetic_object_068_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_068_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_combine_s_pale_upper_grain_tank",
    "target_description": "the combine's pale upper grain tank",
    "source_state": "The combine's upper grain tank and cover panels are pale beige-gray.",
    "desired_change": "The upper grain tank becomes bright red while the rest of the machine retains its colors."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, change the combine's pale upper grain tank to bright red over the next two seconds.",
  "expected_result": {
    "description": "The upper grain tank becomes bright red while the rest of the machine retains its colors.",
    "target_phrase": "bright-red upper grain tank"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_068_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The raised upper panels are broad and separated from the green header and golden crop."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_068_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the combine's pale upper grain tank on B independently of E1's change to the combine header relative to the standing crop; both edit results must coexist in C."
  }
}
```

## synthetic_object_069

### synthetic_object_069_E1

```json
{
  "video_id": "synthetic_object_069",
  "edit_id": "synthetic_object_069_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_069.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_blue_bottle_s_white_cap",
    "target_description": "the blue bottle's white cap",
    "source_state": "The upright blue bottle has a small white cap beneath the upper mechanism.",
    "desired_change": "The white bottle cap is replaced by a matte black cap of matching shape."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, replace the upright blue bottle's white cap with a matte black cap of matching shape.",
  "expected_result": {
    "description": "The white bottle cap is replaced by a matte black cap of matching shape.",
    "target_phrase": "matte-black bottle cap"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cap is visible above the narrow bottle neck within the transparent enclosure."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_069_E2A

```json
{
  "video_id": "synthetic_object_069",
  "edit_id": "synthetic_object_069_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_069.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_bottle_release_and_falling_process",
    "target_description": "the bottle-release and falling process",
    "source_state": "The bottle remains upright until about 25.5 seconds and then falls horizontally to the bottom.",
    "desired_change": "The release progresses faster so the bottle lies fully horizontal at the enclosure bottom by 23.5 seconds."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 23.5,
    "evaluation_window_sec": [
      19.5,
      25.5
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 20.5 seconds, accelerate the bottle-release process so it lies fully horizontal at the enclosure bottom by 23.5 seconds.",
  "expected_result": {
    "description": "The release progresses faster so the bottle lies fully horizontal at the enclosure bottom by 23.5 seconds.",
    "target_phrase": "bottle horizontal at the bottom by 23.5 seconds"
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
      19.5,
      25.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bottle's vertical axis, lowest spiral ring, and enclosure base provide clear stage landmarks."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_069_E2B

```json
{
  "video_id": "synthetic_object_069",
  "edit_id": "synthetic_object_069_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_069_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_fallen_bottle_relative_to_the_lowest_spiral_ring",
    "target_description": "the fallen bottle relative to the lowest spiral ring",
    "source_state": "The falling bottle reaches the lower enclosure at an off-center angle.",
    "desired_change": "The horizontal bottle is centered inside the lowest spiral ring with its cap facing right."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      24.5,
      28.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25.5 seconds, center the horizontal blue bottle inside the lowest spiral ring with its cap facing right.",
  "expected_result": {
    "description": "The horizontal bottle is centered inside the lowest spiral ring with its cap facing right.",
    "target_phrase": "horizontal bottle centered in the lowest ring"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_069_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bottle, lowest transparent ring, and right enclosure wall are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_069_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the fallen bottle relative to the lowest spiral ring on B independently of E1's change to the blue bottle's white cap; both edit results must coexist in C."
  }
}
```

## synthetic_object_070

### synthetic_object_070_E1

```json
{
  "video_id": "synthetic_object_070",
  "edit_id": "synthetic_object_070_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_070.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Semantic Process Pause and Resume",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_carton_conveyor_process",
    "target_description": "the carton conveyor process",
    "source_state": "The carton continues forward through the sealing head and stops near 10 seconds.",
    "desired_change": "The carton pauses for three seconds at 6 seconds and then resumes its forward travel."
  },
  "timing": {
    "edit_point_sec": 6,
    "effect_start_sec": 6,
    "effect_end_sec": 12,
    "evaluation_window_sec": [
      5,
      14
    ],
    "temporal_behavior": "temporary process pause"
  },
  "instruction": "Starting at 6 seconds, pause the carton's forward conveyor motion for three seconds, then resume it toward the sealing head.",
  "expected_result": {
    "description": "The carton pauses for three seconds at 6 seconds and then resumes its forward travel.",
    "target_phrase": "carton pausing for three seconds then resuming"
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
      5,
      14
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The carton edges, roller bed, and sealing head provide continuous position references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_070_E2A

```json
{
  "video_id": "synthetic_object_070",
  "edit_id": "synthetic_object_070_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_070.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_sealing_head_tape_and_carton_top_seam",
    "target_description": "the sealing head, tape, and carton top seam",
    "source_state": "The tape remains stretched diagonally between the sealing head and carton top.",
    "desired_change": "The sealing head presses the stretched tape flat along the carton seam in one downward stroke."
  },
  "timing": {
    "edit_point_sec": 36,
    "effect_start_sec": 36,
    "effect_end_sec": 40,
    "evaluation_window_sec": [
      35,
      42
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 36 seconds, make the sealing head press the stretched tape flat along the carton's top seam in one downward stroke.",
  "expected_result": {
    "description": "The sealing head presses the stretched tape flat along the carton seam in one downward stroke.",
    "target_phrase": "sealing head pressing tape onto the carton"
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
      35,
      42
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tape span, red head, top seam, and stationary carton are visible in the close view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_070_E2B

```json
{
  "video_id": "synthetic_object_070",
  "edit_id": "synthetic_object_070_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_070_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Auxiliary Object Style Change",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_red_horizontal_sealing_head",
    "target_description": "the red horizontal sealing head",
    "source_state": "The horizontal sealing head has a smooth red industrial finish.",
    "desired_change": "Only the red sealing head is rendered with a hammered copper texture."
  },
  "timing": {
    "edit_point_sec": 20.5,
    "effect_start_sec": 20.5,
    "effect_end_sec": 22.5,
    "evaluation_window_sec": [
      19.5,
      24.5
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 20.5 seconds, render only the red horizontal sealing head with a hammered copper texture over two seconds.",
  "expected_result": {
    "description": "Only the red sealing head is rendered with a hammered copper texture.",
    "target_phrase": "hammered-copper sealing head"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_070_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      19.5,
      24.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The red head is isolated between pale uprights and above the brown carton."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_070_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the red horizontal sealing head on B independently of E1's change to the carton conveyor process; both edit results must coexist in C."
  }
}
```

## synthetic_object_071

### synthetic_object_071_E1

```json
{
  "video_id": "synthetic_object_071",
  "edit_id": "synthetic_object_071_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Global Tone and Texture Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_bottle_filling_scene",
    "target_description": "the full bottle-filling scene",
    "source_state": "The factory scene has neutral silver, pale-yellow, and green colors.",
    "desired_change": "The full scene adopts a cool cyan monochrome grade with crisp metallic contrast."
  },
  "timing": {
    "edit_point_sec": 19.5,
    "effect_start_sec": 19.5,
    "effect_end_sec": 21.5,
    "evaluation_window_sec": [
      18.5,
      23.5
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 19.5 seconds, transform the full bottle-filling scene into a cool cyan monochrome grade over two seconds.",
  "expected_result": {
    "description": "The full scene adopts a cool cyan monochrome grade with crisp metallic contrast.",
    "target_phrase": "cool cyan monochrome filling scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      18.5,
      23.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bottle, nozzle, control box, platform, and background tanks are visible together."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_071_E2A

```json
{
  "video_id": "synthetic_object_071",
  "edit_id": "synthetic_object_071_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_071.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_liquid_visible_inside_the_clear_bottle",
    "target_description": "the liquid visible inside the clear bottle",
    "source_state": "The partially filled liquid appears pale yellow beneath a white foam layer.",
    "desired_change": "The visible liquid becomes translucent violet while the foam remains white."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      29.5,
      34.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 30.5 seconds, change the liquid inside the clear bottle from pale yellow to translucent violet over two seconds.",
  "expected_result": {
    "description": "The visible liquid becomes translucent violet while the foam remains white.",
    "target_phrase": "translucent violet liquid in the bottle"
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
      29.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The bottle wall, liquid boundary, and foam layer remain visible against the stainless background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_071_E2B

```json
{
  "video_id": "synthetic_object_071",
  "edit_id": "synthetic_object_071_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_071_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_filling_nozzle_s_upward_retraction",
    "target_description": "the filling nozzle's upward retraction",
    "source_state": "The filling nozzle begins a gradual upward withdrawal near the end of the filling stage.",
    "desired_change": "The nozzle retracts upward at twice its original vertical speed until clear of the bottle neck."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      33.5,
      39.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 34.5 seconds, retract the filling nozzle upward at twice its original speed until it clears the bottle neck.",
  "expected_result": {
    "description": "The nozzle retracts upward at twice its original vertical speed until clear of the bottle neck.",
    "target_phrase": "nozzle retracting upward twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_071_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The nozzle tip, bottle mouth, neck, and vertical support provide clear motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_071_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the filling nozzle's upward retraction on B independently of E1's change to the full bottle-filling scene; both edit results must coexist in C."
  }
}
```

## synthetic_object_072

### synthetic_object_072_E1

```json
{
  "video_id": "synthetic_object_072",
  "edit_id": "synthetic_object_072_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_072.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_overhead_spray_jets",
    "target_description": "the overhead spray jets",
    "source_state": "The overhead spray jets fall in largely fixed directions onto the stationary dish rack.",
    "desired_change": "The spray jets sweep left and right across the plates twice over five seconds."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 18.5,
    "evaluation_window_sec": [
      12.5,
      20.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 13.5 seconds, make the overhead spray jets sweep left and right across the plates twice over five seconds.",
  "expected_result": {
    "description": "The spray jets sweep left and right across the plates twice over five seconds.",
    "target_phrase": "spray jets sweeping across the plates twice"
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
      12.5,
      20.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The jet origins, plate row, transparent guard, and wet reflections remain visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_072_E2A

```json
{
  "video_id": "synthetic_object_072",
  "edit_id": "synthetic_object_072_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_072.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Process Ordering Change",
    "scope": "Multiple Processes"
  },
  "target": {
    "target_id": "the_first_rack_exit_and_second_rack_entry",
    "target_description": "the first rack exit and second rack entry",
    "source_state": "The first rack begins leaving while the second rack is already entering from the right.",
    "desired_change": "The first rack exits the spray chamber completely before the second rack begins entering."
  },
  "timing": {
    "edit_point_sec": 34,
    "effect_start_sec": 34,
    "effect_end_sec": 41,
    "evaluation_window_sec": [
      33,
      43
    ],
    "temporal_behavior": "relative event reordering"
  },
  "instruction": "Starting at 34 seconds, let the first dish rack exit completely before the second rack begins entering the spray chamber.",
  "expected_result": {
    "description": "The first rack exits the spray chamber completely before the second rack begins entering.",
    "target_phrase": "first rack exiting before the second enters"
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
      33,
      43
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both rack edges and the fixed chamber entrance make the two transport processes independently trackable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_072_E2B

```json
{
  "video_id": "synthetic_object_072",
  "edit_id": "synthetic_object_072_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_072_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_along_the_stationary_plate_row",
    "target_description": "the camera path along the stationary plate row",
    "source_state": "The camera holds a fixed oblique view of the plates inside the spray chamber.",
    "desired_change": "The camera dollies smoothly from the rightmost plate to the leftmost plate."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      24.5,
      32.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 25.5 seconds, move the camera smoothly from the rightmost plate to the leftmost plate over five seconds.",
  "expected_result": {
    "description": "The camera dollies smoothly from the rightmost plate to the leftmost plate.",
    "target_phrase": "right-to-left camera dolly along the plates"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_072_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Repeated plate edges, guide rail, control panel, and chamber frame provide stable trajectory references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_072_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera path along the stationary plate row on B independently of E1's change to the overhead spray jets; both edit results must coexist in C."
  }
}
```

## synthetic_object_073

### synthetic_object_073_E1

```json
{
  "video_id": "synthetic_object_073",
  "edit_id": "synthetic_object_073_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_073.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Specified Auxiliary Object-local Style",
    "operation": "Auxiliary Object Style Change",
    "scope": "Supporting Object"
  },
  "target": {
    "target_id": "the_bread_machine_s_silver_upper_housing",
    "target_description": "the bread machine's silver upper housing",
    "source_state": "The upper machine housing has a smooth brushed-silver surface.",
    "desired_change": "Only the upper housing is rendered with a warm hammered-copper texture."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 15,
    "evaluation_window_sec": [
      12,
      17
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 13 seconds, render only the bread machine's silver upper housing with a warm hammered-copper texture over two seconds.",
  "expected_result": {
    "description": "Only the upper housing is rendered with a warm hammered-copper texture.",
    "target_phrase": "hammered-copper upper machine housing"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12,
      17
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The housing is separated from the bread, tray, outdoor pavement, and black side knob."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_073_E2A

```json
{
  "video_id": "synthetic_object_073",
  "edit_id": "synthetic_object_073_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_073.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_machine_s_right_side_black_adjustment_knob",
    "target_description": "the machine's right-side black adjustment knob",
    "source_state": "A physical black adjustment knob protrudes from the machine's right-side frame.",
    "desired_change": "The right-side physical black adjustment knob is removed from the machine."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, remove the physical black adjustment knob protruding from the bread machine's right-side frame.",
  "expected_result": {
    "description": "The right-side physical black adjustment knob is removed from the machine.",
    "target_phrase": "right-side adjustment knob removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "target boundary: Only the physical black adjustment knob is editable; adjacent markings, labels, symbols, and printed text remain protected."
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The knob is isolated against the outdoor background and does not overlap the bread."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_073_E2B

```json
{
  "video_id": "synthetic_object_073",
  "edit_id": "synthetic_object_073_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_073_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_outdoor_paving_stones_behind_the_bread_machine",
    "target_description": "the outdoor paving stones behind the bread machine",
    "source_state": "The paving stones behind the machine are dry and light gray.",
    "desired_change": "The background paving stones become rain-wet and dark with soft reflections."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      23.5,
      28.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 24.5 seconds, change the outdoor paving stones behind the bread machine from dry to rain-wet and reflective.",
  "expected_result": {
    "description": "The background paving stones become rain-wet and dark with soft reflections.",
    "target_phrase": "rain-wet paving behind the machine"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_073_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad pavement area is visible around the machine base and tray."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_073_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the outdoor paving stones behind the bread machine on B independently of E1's change to the bread machine's silver upper housing; both edit results must coexist in C."
  }
}
```

## synthetic_object_074

### synthetic_object_074_E1

```json
{
  "video_id": "synthetic_object_074",
  "edit_id": "synthetic_object_074_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_active_straight_groove_cutting_progress",
    "target_description": "the active straight-groove cutting progress",
    "source_state": "The glowing processing point extends the current straight groove gradually across the plate.",
    "desired_change": "The cutting progresses faster so the current groove reaches the far edge by 14 seconds."
  },
  "timing": {
    "edit_point_sec": 10,
    "effect_start_sec": 10,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      9,
      16
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 10 seconds, accelerate the active groove-cutting process so the current straight groove reaches the far plate edge by 14 seconds.",
  "expected_result": {
    "description": "The cutting progresses faster so the current groove reaches the far edge by 14 seconds.",
    "target_phrase": "current groove reaching the far edge by 14 seconds"
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
      9,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The glowing point, completed dark line, remaining clean plate, and far edge form clear progress landmarks."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_074_E2A

```json
{
  "video_id": "synthetic_object_074",
  "edit_id": "synthetic_object_074_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_074.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_blue_coolant_hose_beside_the_cutting_head",
    "target_description": "the blue coolant hose beside the cutting head",
    "source_state": "A blue coolant hose runs beside the metal processing head.",
    "desired_change": "The visible blue coolant hose is removed from beside the cutting head."
  },
  "timing": {
    "edit_point_sec": 32,
    "effect_start_sec": 32,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      31,
      35
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32 seconds, remove the visible blue coolant hose running beside the metal cutting head.",
  "expected_result": {
    "description": "The visible blue coolant hose is removed from beside the cutting head.",
    "target_phrase": "blue coolant hose removed"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The blue hose is distinct from the copper nozzle and reflective metal plate."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_074_E2B

```json
{
  "video_id": "synthetic_object_074",
  "edit_id": "synthetic_object_074_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_074_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_metal_cutting_head",
    "target_description": "the metal cutting head",
    "source_state": "The cutting head follows another straight path over the metal plate.",
    "desired_change": "The cutting head traces one complete circle and then resumes its straight path."
  },
  "timing": {
    "edit_point_sec": 23,
    "effect_start_sec": 23,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      22,
      29
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 23 seconds, make the metal cutting head trace one complete circle before resuming its straight path.",
  "expected_result": {
    "description": "The cutting head traces one complete circle and then resumes its straight path.",
    "target_phrase": "cutting head tracing one complete circle"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_074_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The glowing contact point and broad plate surface make the altered trajectory directly visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_074_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the metal cutting head on B independently of E1's change to the active straight-groove cutting progress; both edit results must coexist in C."
  }
}
```

## synthetic_object_075

### synthetic_object_075_E1

```json
{
  "video_id": "synthetic_object_075",
  "edit_id": "synthetic_object_075_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_075.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Supporting/Environment Motion",
    "operation": "Supporting Motion Control",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_conveyor_rollers_beneath_the_apple_path",
    "target_description": "the conveyor rollers beneath the apple path",
    "source_state": "The conveyor rollers continue turning at their regular transport rate.",
    "desired_change": "The exposed rollers rotate at twice their original rate for five seconds."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      12,
      20
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 13 seconds, make the exposed conveyor rollers beneath the apple path rotate at twice their original rate for five seconds.",
  "expected_result": {
    "description": "The exposed rollers rotate at twice their original rate for five seconds.",
    "target_phrase": "conveyor rollers rotating twice as fast"
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
      12,
      20
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The emptying transfer point and repeated metal roller edges remain visible after the first apple passes."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_075_E2A

```json
{
  "video_id": "synthetic_object_075",
  "edit_id": "synthetic_object_075_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_075.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_conveyor_behind_the_red_and_yellow_apple",
    "target_description": "the conveyor behind the red-and-yellow apple",
    "source_state": "No second apple follows the red-and-yellow apple entering the conveyor transfer.",
    "desired_change": "One green apple is added one belt-length behind the red-and-yellow apple."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      30,
      34
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31 seconds, add one green apple one belt-length behind the red-and-yellow apple on the incoming conveyor.",
  "expected_result": {
    "description": "One green apple is added one belt-length behind the red-and-yellow apple.",
    "target_phrase": "green apple behind the red-and-yellow apple"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30,
      34
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The incoming apple and an unoccupied upstream belt segment are visible before the sloped chute."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_075_E2B

```json
{
  "video_id": "synthetic_object_075",
  "edit_id": "synthetic_object_075_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_075_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_silver_sloped_transfer_chute",
    "target_description": "the silver sloped transfer chute",
    "source_state": "The empty transfer chute has a plain reflective silver surface.",
    "desired_change": "The chute's inner surface becomes glossy cobalt blue while its metal side walls remain silver."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 25.5 seconds, change the sloped transfer chute's inner surface from silver to glossy cobalt blue over two seconds.",
  "expected_result": {
    "description": "The chute's inner surface becomes glossy cobalt blue while its metal side walls remain silver.",
    "target_phrase": "glossy cobalt-blue transfer chute"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_075_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The empty chute interior is broad, unobstructed, and separated from the conveyor frame."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_075_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the silver sloped transfer chute on B independently of E1's change to the conveyor rollers beneath the apple path; both edit results must coexist in C."
  }
}
```

## synthetic_object_076

### synthetic_object_076_E1

```json
{
  "video_id": "synthetic_object_076",
  "edit_id": "synthetic_object_076_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_076.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_smaller_upper_cardboard_carton",
    "target_description": "the smaller upper cardboard carton",
    "source_state": "The smaller upper carton has the same brown cardboard appearance as the lower carton.",
    "desired_change": "The smaller upper carton becomes bright blue while retaining its seams and rectangular shape."
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
  "instruction": "Starting at 14 seconds, change the smaller upper carton from brown cardboard to bright blue over the next two seconds.",
  "expected_result": {
    "description": "The smaller upper carton becomes bright blue while retaining its seams and rectangular shape.",
    "target_phrase": "bright-blue upper carton"
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
    "description": "Both stacked cartons are fully visible before the cart begins moving toward the door."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_076_E2A

```json
{
  "video_id": "synthetic_object_076",
  "edit_id": "synthetic_object_076_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_076.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_cart_s_front_wheels_and_the_doorway_threshold",
    "target_description": "the cart's front wheels and the doorway threshold",
    "source_state": "The cart's wheels cross the doorway threshold with little visible body response.",
    "desired_change": "Both front wheels bump across the threshold together and make the loaded cart bounce once."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      24,
      31
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 25 seconds, make both front cart wheels bump across the doorway threshold and bounce the loaded cart once.",
  "expected_result": {
    "description": "Both front wheels bump across the threshold together and make the loaded cart bounce once.",
    "target_phrase": "loaded cart bouncing once at the threshold"
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
      24,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The front wheels, threshold line, cart frame, and stacked cartons remain visible during the crossing."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_076_E2B

```json
{
  "video_id": "synthetic_object_076",
  "edit_id": "synthetic_object_076_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_076_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_loaded_cart_s_doorway_crossing_progress",
    "target_description": "the loaded cart's doorway-crossing progress",
    "source_state": "The loaded cart takes until about 30 seconds to move fully outside the sliding doors.",
    "desired_change": "The crossing progresses faster so the entire cart is outside the doorway by 28 seconds."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      23.5,
      30
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 24.5 seconds, accelerate the loaded cart's doorway crossing so the entire cart is outside by 28 seconds.",
  "expected_result": {
    "description": "The crossing progresses faster so the entire cart is outside the doorway by 28 seconds.",
    "target_phrase": "loaded cart fully outside by 28 seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of synthetic_object_076_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      30
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cart footprint, door threshold, open panels, and exterior pavement form clear stage boundaries."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_076_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the loaded cart's doorway-crossing progress on B independently of E1's change to the smaller upper cardboard carton; both edit results must coexist in C."
  }
}
```

## synthetic_object_077

### synthetic_object_077_E1

```json
{
  "video_id": "synthetic_object_077",
  "edit_id": "synthetic_object_077_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_077.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_framing_of_the_two_parallel_escalators",
    "target_description": "the framing of the two parallel escalators",
    "source_state": "The central escalator dominates the frame while the parallel right escalator is only partly visible.",
    "desired_change": "The camera widens until both escalators and their complete glass side panels are visible."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      11,
      18
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 12 seconds, smoothly zoom out until both parallel escalators and their complete glass side panels are visible.",
  "expected_result": {
    "description": "The camera widens until both escalators and their complete glass side panels are visible.",
    "target_phrase": "both escalators fully framed"
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
      11,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The converging handrails, stair runs, and surrounding walls provide stable framing references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_077_E2A

```json
{
  "video_id": "synthetic_object_077",
  "edit_id": "synthetic_object_077_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_077.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_central_escalator_s_step_motion",
    "target_description": "the central escalator's step motion",
    "source_state": "The grooved steps travel toward the upper landing at a steady rate.",
    "desired_change": "The escalator steps move at one-and-a-half times their original speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 36,
    "evaluation_window_sec": [
      30,
      38
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 31 seconds, increase the central escalator steps to one-and-a-half times their original speed for five seconds.",
  "expected_result": {
    "description": "The escalator steps move at one-and-a-half times their original speed for five seconds.",
    "target_phrase": "escalator steps moving one-and-a-half times faster"
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
      30,
      38
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Repeated step edges and the fixed side panels make the transport speed assessable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_077_E2B

```json
{
  "video_id": "synthetic_object_077",
  "edit_id": "synthetic_object_077_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_077_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_right_parallel_escalator",
    "target_description": "the right parallel escalator",
    "source_state": "The right escalator runs parallel to the central escalator at a fixed lateral separation.",
    "desired_change": "The right escalator is rotated five degrees inward toward the central escalator while its lower landing stays fixed."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      24,
      28
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 25 seconds, rotate the right parallel escalator five degrees inward toward the central escalator while fixing its lower landing.",
  "expected_result": {
    "description": "The right escalator is rotated five degrees inward toward the central escalator while its lower landing stays fixed.",
    "target_phrase": "right escalator angled inward five degrees"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_077_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both escalator axes, lower side-panel edges, and upper landing area are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_077_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the right parallel escalator on B independently of E1's change to the framing of the two parallel escalators; both edit results must coexist in C."
  }
}
```

## synthetic_object_078

### synthetic_object_078_E1

```json
{
  "video_id": "synthetic_object_078",
  "edit_id": "synthetic_object_078_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_078.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_right_bridge_leaf_s_dark_side_rail",
    "target_description": "the right bridge leaf's dark side rail",
    "source_state": "A narrow dark metal rail follows the raised edge of the right bridge leaf.",
    "desired_change": "The dark side rail is replaced by a solid silver safety barrier of the same length."
  },
  "timing": {
    "edit_point_sec": 13.5,
    "effect_start_sec": 13.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      12.5,
      16.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13.5 seconds, replace the right bridge leaf's dark side rail with a solid silver safety barrier of equal length.",
  "expected_result": {
    "description": "The dark side rail is replaced by a solid silver safety barrier of the same length.",
    "target_phrase": "solid silver barrier on the right bridge leaf"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      12.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right leaf edge is cleanly outlined against trees and sky throughout the opening."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_078_E2A

```json
{
  "video_id": "synthetic_object_078",
  "edit_id": "synthetic_object_078_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_078.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_gap_between_the_two_raised_bridge_tips",
    "target_description": "the gap between the two raised bridge tips",
    "source_state": "The two inner bridge tips are separated by a moderate central gap above the waterway.",
    "desired_change": "The central gap is increased until it equals one full bridge-leaf width."
  },
  "timing": {
    "edit_point_sec": 30,
    "effect_start_sec": 30,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      29,
      33
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 30 seconds, increase the gap between the two raised bridge tips to one full bridge-leaf width.",
  "expected_result": {
    "description": "The central gap is increased until it equals one full bridge-leaf width.",
    "target_phrase": "one-leaf-width gap between bridge tips"
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
      29,
      33
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The symmetrical leaf tips, fixed shore hinges, and central water channel provide exact relationship anchors."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_078_E2B

```json
{
  "video_id": "synthetic_object_078",
  "edit_id": "synthetic_object_078_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_078_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_right_bridge_leaf_and_overhanging_branches",
    "target_description": "the right bridge leaf and overhanging branches",
    "source_state": "The rising right bridge leaf remains separated from the nearby overhanging branches.",
    "desired_change": "The leaf edge presses the branches upward once, and the branches bend back after contact."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 29.5,
    "evaluation_window_sec": [
      24.5,
      31.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 25.5 seconds, make the rising right bridge leaf press the overhanging branches upward once before they bend back.",
  "expected_result": {
    "description": "The leaf edge presses the branches upward once, and the branches bend back after contact.",
    "target_phrase": "bridge leaf bending the branches upward once"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_078_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      31.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The right leaf edge and adjacent foliage remain visible against the stable bank."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_078_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the right bridge leaf and overhanging branches on B independently of E1's change to the right bridge leaf's dark side rail; both edit results must coexist in C."
  }
}
```

## synthetic_object_079

### synthetic_object_079_E1

```json
{
  "video_id": "synthetic_object_079",
  "edit_id": "synthetic_object_079_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_079.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_blue_suitcase_and_the_scanner_curtain_strips",
    "target_description": "the blue suitcase and the scanner curtain strips",
    "source_state": "The blue suitcase approaches the dark flexible entrance curtain before entering.",
    "desired_change": "The suitcase pushes the curtain strips into a wide fan and the strips rebound behind it."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 16,
    "evaluation_window_sec": [
      11,
      18
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 12 seconds, make the blue suitcase push the scanner curtain strips into a wide fan before they rebound.",
  "expected_result": {
    "description": "The suitcase pushes the curtain strips into a wide fan and the strips rebound behind it.",
    "target_phrase": "suitcase spreading and releasing the curtain strips"
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
      11,
      18
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The suitcase shell, tunnel entrance, flexible strips, and conveyor are visible during entry."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_079_E2A

```json
{
  "video_id": "synthetic_object_079",
  "edit_id": "synthetic_object_079_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_079.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_blue_suitcase_entering_near_31_seconds",
    "target_description": "the blue suitcase entering near 31 seconds",
    "source_state": "The incoming suitcase has a dark-blue ribbed hard shell.",
    "desired_change": "The suitcase shell becomes bright yellow while its dark zipper, handle, and wheels remain distinct."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31 seconds, change the incoming dark-blue suitcase to bright yellow over the next two seconds.",
  "expected_result": {
    "description": "The suitcase shell becomes bright yellow while its dark zipper, handle, and wheels remain distinct.",
    "target_phrase": "bright-yellow incoming suitcase"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The suitcase is isolated on the pale conveyor outside the dark tunnel opening."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_079_E2B

```json
{
  "video_id": "synthetic_object_079",
  "edit_id": "synthetic_object_079_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_079_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_dark_gray_suitcase_at_the_tunnel_entrance",
    "target_description": "the dark-gray suitcase at the tunnel entrance",
    "source_state": "The dark-gray suitcase lies crosswise with its long axis roughly parallel to the conveyor edge.",
    "desired_change": "The suitcase is rotated ninety degrees so its side handle faces directly toward the camera."
  },
  "timing": {
    "edit_point_sec": 24.5,
    "effect_start_sec": 24.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      23.5,
      27.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24.5 seconds, rotate the dark-gray suitcase ninety degrees so its side handle faces directly toward the camera.",
  "expected_result": {
    "description": "The suitcase is rotated ninety degrees so its side handle faces directly toward the camera.",
    "target_phrase": "dark-gray suitcase rotated toward the camera"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_079_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete suitcase outline, side handle, belt edges, and tunnel opening are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_079_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the dark-gray suitcase at the tunnel entrance on B independently of E1's change to the blue suitcase and the scanner curtain strips; both edit results must coexist in C."
  }
}
```

## synthetic_object_080

### synthetic_object_080_E1

```json
{
  "video_id": "synthetic_object_080",
  "edit_id": "synthetic_object_080_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_080.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_milking_cup_cluster_relative_to_the_cow_s_rear_hooves",
    "target_description": "the milking cup cluster relative to the cow's rear hooves",
    "source_state": "The connected cup cluster hangs slightly offset between the cow's two rear hooves.",
    "desired_change": "The cup cluster is shifted to hang exactly midway between the two rear hooves."
  },
  "timing": {
    "edit_point_sec": 13,
    "effect_start_sec": 13,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      12,
      16
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 13 seconds, shift the connected milking cup cluster to hang exactly midway between the cow's two rear hooves.",
  "expected_result": {
    "description": "The cup cluster is shifted to hang exactly midway between the two rear hooves.",
    "target_phrase": "cup cluster centered between the rear hooves"
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
      12,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Both hooves, the attached cup group, and the wet floor are visible in the low rear view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_080_E2A

```json
{
  "video_id": "synthetic_object_080",
  "edit_id": "synthetic_object_080_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_080.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_long_yellow_hose_connected_to_the_cup_cluster",
    "target_description": "the long yellow hose connected to the cup cluster",
    "source_state": "A long yellow hose extends from the metal collection unit toward the floor.",
    "desired_change": "The yellow hose becomes bright blue while its black couplings remain distinct."
  },
  "timing": {
    "edit_point_sec": 31,
    "effect_start_sec": 31,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      30,
      35
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 31 seconds, change the long yellow milking hose to bright blue over the next two seconds.",
  "expected_result": {
    "description": "The yellow hose becomes bright blue while its black couplings remain distinct.",
    "target_phrase": "bright-blue milking hose"
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
      30,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The hose is exposed below the cow and separated from the darker tubing and metal cups."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_080_E2B

```json
{
  "video_id": "synthetic_object_080",
  "edit_id": "synthetic_object_080_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_080_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_cow_s_tail_swinging_motion",
    "target_description": "the cow's tail-swinging motion",
    "source_state": "The cow's tail makes occasional slow lateral swings behind the connected equipment.",
    "desired_change": "The tail swings left and right at twice its original rate for five seconds."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      24.5,
      32.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 25.5 seconds, make the cow's tail swing left and right at twice its original rate for five seconds.",
  "expected_result": {
    "description": "The tail swings left and right at twice its original rate for five seconds.",
    "target_phrase": "cow tail swinging twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_080_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tail, rear legs, cup cluster, and open lateral space remain visible during the continuous shot."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_080_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the cow's tail-swinging motion on B independently of E1's change to the milking cup cluster relative to the cow's rear hooves; both edit results must coexist in C."
  }
}
```

## synthetic_object_081

### synthetic_object_081_E1

```json
{
  "video_id": "synthetic_object_081",
  "edit_id": "synthetic_object_081_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_081.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_teapot_lid",
    "target_description": "the teapot lid",
    "source_state": "The round lid remains fitted on top of the teapot throughout the product display.",
    "desired_change": "The lid rises one lid-height, completes one full rotation, and settles back onto the teapot."
  },
  "timing": {
    "edit_point_sec": 10.5,
    "effect_start_sec": 10.5,
    "effect_end_sec": 14.5,
    "evaluation_window_sec": [
      9.5,
      16.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 10.5 seconds, make the teapot lid rise, rotate once, and settle back onto the opening over four seconds.",
  "expected_result": {
    "description": "The lid rises one lid-height, completes one full rotation, and settles back onto the teapot.",
    "target_phrase": "teapot lid rising, rotating, and settling"
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
      9.5,
      16.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The lid, top knob, opening rim, and full upper body are unobstructed in the stable close view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_081_E2A

```json
{
  "video_id": "synthetic_object_081",
  "edit_id": "synthetic_object_081_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_081.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_teapot_s_glazed_body",
    "target_description": "the teapot's glazed body",
    "source_state": "The teapot has a glossy deep-blue to teal glaze with fine horizontal texture.",
    "desired_change": "The glazed body becomes warm ivory with fine cobalt-blue horizontal bands."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      29.5,
      34.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 30.5 seconds, change the teapot's deep teal glaze to warm ivory with fine cobalt-blue horizontal bands.",
  "expected_result": {
    "description": "The glazed body becomes warm ivory with fine cobalt-blue horizontal bands.",
    "target_phrase": "ivory teapot with cobalt-blue bands"
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
      29.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete belly, spout, lid, and most of the handle are visible against the softly blurred room."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_081_E2B

```json
{
  "video_id": "synthetic_object_081",
  "edit_id": "synthetic_object_081_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_081_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_tabletop_beside_the_teapot_spout",
    "target_description": "the open tabletop beside the teapot spout",
    "source_state": "No cup occupies the clear wooden tabletop beside the teapot spout.",
    "desired_change": "One small white porcelain teacup is added directly below and to the right of the spout."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 25,
    "evaluation_window_sec": [
      23,
      27
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 24 seconds, add one small white porcelain teacup on the wooden table directly below and right of the teapot spout.",
  "expected_result": {
    "description": "One small white porcelain teacup is added directly below and to the right of the spout.",
    "target_phrase": "white teacup beside the teapot spout"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "visual result of synthetic_object_081_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      27
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The spout and an empty, stable tabletop area below it remain visible after the mid-video dissolve."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_081_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the open tabletop beside the teapot spout on B independently of E1's change to the teapot lid; both edit results must coexist in C."
  }
}
```

## synthetic_object_082

### synthetic_object_082_E1

```json
{
  "video_id": "synthetic_object_082",
  "edit_id": "synthetic_object_082_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_082.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_open_watch_lid_relative_to_the_dial",
    "target_description": "the open watch lid relative to the dial",
    "source_state": "The raised circular lid forms a broad obtuse angle above the exposed watch dial.",
    "desired_change": "The lid is positioned at a right angle to the dial around its existing hinge."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 15.5,
    "evaluation_window_sec": [
      13.5,
      17.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 14.5 seconds, position the open pocket-watch lid at a right angle to the exposed dial around its existing hinge.",
  "expected_result": {
    "description": "The lid is positioned at a right angle to the dial around its existing hinge.",
    "target_phrase": "watch lid perpendicular to the dial"
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
      13.5,
      17.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The circular dial, raised lid, hinge region, and supporting glove are visible in the same close view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_082_E2A

```json
{
  "video_id": "synthetic_object_082",
  "edit_id": "synthetic_object_082_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_082.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_pocket_watch_s_physical_thin_red_seconds_hand",
    "target_description": "the pocket watch's physical thin red seconds hand",
    "source_state": "The physical thin red seconds hand advances gradually around the exposed dial.",
    "desired_change": "The red seconds hand rotates at twice its original angular speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 33.5,
    "effect_start_sec": 33.5,
    "effect_end_sec": 38.5,
    "evaluation_window_sec": [
      32.5,
      40.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 33.5 seconds, make the pocket watch's physical thin red seconds hand rotate at twice its original speed for five seconds.",
  "expected_result": {
    "description": "The red seconds hand rotates at twice its original angular speed for five seconds.",
    "target_phrase": "red seconds hand rotating twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "target boundary: Only the physical red seconds hand and its rotation are editable; dial numerals, tick marks, logos, and inscriptions remain protected."
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      32.5,
      40.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The open watch is stationary and the enlarging close view makes the dial and thin hand continuously observable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_082_E2B

```json
{
  "video_id": "synthetic_object_082",
  "edit_id": "synthetic_object_082_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_082_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Pause/Resume/Reverse",
    "operation": "Semantic Process Pause and Resume",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_pocket_watch_s_physical_thin_red_seconds_hand",
    "target_description": "the pocket watch's physical thin red seconds hand",
    "source_state": "The physical thin red seconds hand continues moving after the gloved hand leaves the open watch.",
    "desired_change": "The red seconds hand pauses for four seconds and then resumes its original motion."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 33,
    "evaluation_window_sec": [
      25,
      35
    ],
    "temporal_behavior": "temporary process pause"
  },
  "instruction": "Starting at 26 seconds, pause the pocket watch's physical thin red seconds hand for four seconds, then resume its original motion.",
  "expected_result": {
    "description": "The red seconds hand pauses for four seconds and then resumes its original motion.",
    "target_phrase": "red seconds hand pausing and resuming"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "target boundary: Only the physical red seconds hand and its rotation are editable; dial numerals, tick marks, logos, and inscriptions remain protected.",
      "visual result of synthetic_object_082_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      35
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The hand has withdrawn, leaving the open dial stable and unobstructed through the selected interval."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_082_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the pocket watch's physical thin red seconds hand on B independently of E1's change to the open watch lid relative to the dial; both edit results must coexist in C."
  }
}
```

## synthetic_object_083

### synthetic_object_083_E1

```json
{
  "video_id": "synthetic_object_083",
  "edit_id": "synthetic_object_083_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_framing_around_the_compass",
    "target_description": "the camera framing around the compass",
    "source_state": "The left side of the brass compass is cropped while the map fills the surrounding frame.",
    "desired_change": "The camera widens until the complete compass case and a broad border of the map are visible."
  },
  "timing": {
    "edit_point_sec": 9.5,
    "effect_start_sec": 9.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      8.5,
      14.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 9.5 seconds, smoothly zoom out until the complete brass compass and a broad surrounding section of the map are visible.",
  "expected_result": {
    "description": "The camera widens until the complete compass case and a broad border of the map are visible.",
    "target_phrase": "complete compass framed with surrounding map"
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
      8.5,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The fixed compass rim and map provide stable boundaries for judging the wider framing."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_083_E2A

```json
{
  "video_id": "synthetic_object_083",
  "edit_id": "synthetic_object_083_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_083.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Illumination Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_compass_and_its_dial",
    "target_description": "the compass and its dial",
    "source_state": "The compass is illuminated by diffuse neutral light with modest metal reflections.",
    "desired_change": "A narrow warm spotlight from the upper right illuminates the needle and right half of the dial."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      34.5,
      39.5
    ],
    "temporal_behavior": "gradual persistent illumination change"
  },
  "instruction": "Starting at 35.5 seconds, illuminate the compass needle and right half of the dial with a narrow warm spotlight from above right.",
  "expected_result": {
    "description": "A narrow warm spotlight from the upper right illuminates the needle and right half of the dial.",
    "target_phrase": "warm upper-right spotlight on the compass"
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
      34.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stationary case, pale dial, dark needle, and surrounding map make the directed lighting effect visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_083_E2B

```json
{
  "video_id": "synthetic_object_083",
  "edit_id": "synthetic_object_083_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_083_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_physical_compass_needle_and_inner_brass_rim",
    "target_description": "the physical compass needle and inner brass rim",
    "source_state": "The physical dark needle rotates around its center without contacting the surrounding brass rim.",
    "desired_change": "The pointed needle end swings outward, taps the inner brass rim twice, and rebounds each time."
  },
  "timing": {
    "edit_point_sec": 22.5,
    "effect_start_sec": 22.5,
    "effect_end_sec": 25.5,
    "evaluation_window_sec": [
      21.5,
      27.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 22.5 seconds, make the physical compass needle tap the inner brass rim twice and rebound after each contact.",
  "expected_result": {
    "description": "The pointed needle end swings outward, taps the inner brass rim twice, and rebounds each time.",
    "target_phrase": "compass needle tapping the inner rim twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "target boundary: Only the physical compass needle and its contact with the brass rim are editable; dial markings, letters, map text, and printed symbols remain protected.",
      "visual result of synthetic_object_083_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21.5,
      27.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The pointed needle end and adjacent inner rim are visible together against the stationary dial."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_083_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the physical compass needle and inner brass rim on B independently of E1's change to the camera framing around the compass; both edit results must coexist in C."
  }
}
```

## synthetic_object_084

### synthetic_object_084_E1

```json
{
  "video_id": "synthetic_object_084",
  "edit_id": "synthetic_object_084_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_folding_fan_s_plain_cream_leaf",
    "target_description": "the folding fan's plain cream leaf",
    "source_state": "The broadly opened fan has a plain cream pleated leaf above the pale wooden ribs.",
    "desired_change": "The plain cream leaf becomes pale sky blue with darker blue pleat edges."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 14,
    "evaluation_window_sec": [
      11,
      16
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 12 seconds, change the folding fan's plain cream leaf to pale sky blue with darker blue pleat edges.",
  "expected_result": {
    "description": "The plain cream leaf becomes pale sky blue with darker blue pleat edges.",
    "target_phrase": "pale-blue fan leaf with darker pleats"
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
      11,
      16
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The plain leaf, radiating ribs, lower pivot, and wooden stand are visible before the close push-in."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_084_E2A

```json
{
  "video_id": "synthetic_object_084",
  "edit_id": "synthetic_object_084_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_084.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_folding_fan_around_its_lower_pivot",
    "target_description": "the folding fan around its lower pivot",
    "source_state": "The decorated fan remains broadly opened on its wooden stand during the widening view.",
    "desired_change": "The ribs fold together to half width and then reopen around the lower pivot."
  },
  "timing": {
    "edit_point_sec": 32.5,
    "effect_start_sec": 32.5,
    "effect_end_sec": 36.5,
    "evaluation_window_sec": [
      31.5,
      38.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 32.5 seconds, make the folding fan close to half its width and reopen around the lower pivot over four seconds.",
  "expected_result": {
    "description": "The ribs fold together to half width and then reopen around the lower pivot.",
    "target_phrase": "fan closing halfway and reopening"
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
      31.5,
      38.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The decorated leaf, radiating ribs, pivot pin, and supporting stand are visible as the framing widens."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_084_E2B

```json
{
  "video_id": "synthetic_object_084",
  "edit_id": "synthetic_object_084_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_084_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_along_the_fan_ribs",
    "target_description": "the camera path along the fan ribs",
    "source_state": "The camera holds a close frontal view around the fan's lower ribs and pivot.",
    "desired_change": "The camera dollies upward along the central ribs until the upper curved leaf edge enters the frame."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 31,
    "evaluation_window_sec": [
      25,
      33
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 26 seconds, move the camera upward along the fan's central ribs until the upper curved leaf edge enters the frame.",
  "expected_result": {
    "description": "The camera dollies upward along the central ribs until the upper curved leaf edge enters the frame.",
    "target_phrase": "upward camera move along the fan ribs"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "actions",
      "world-space relationships",
      "visual style",
      "visual result of synthetic_object_084_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      33
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The central ribs form clear converging guides from the visible pivot toward the temporarily cropped upper leaf."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_084_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the camera path along the fan ribs on B independently of E1's change to the folding fan's plain cream leaf; both edit results must coexist in C."
  }
}
```

## synthetic_object_085

### synthetic_object_085_E1

```json
{
  "video_id": "synthetic_object_085",
  "edit_id": "synthetic_object_085_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_toy_car_s_green_body_shell",
    "target_description": "the toy car's green body shell",
    "source_state": "The wind-up toy car has a glossy dark-green body shell with silver and black components.",
    "desired_change": "The dark-green body shell becomes glossy cherry red."
  },
  "timing": {
    "edit_point_sec": 15.5,
    "effect_start_sec": 15.5,
    "effect_end_sec": 17.5,
    "evaluation_window_sec": [
      14.5,
      19.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 15.5 seconds, change the wind-up toy car's dark-green body shell to glossy cherry red over two seconds.",
  "expected_result": {
    "description": "The dark-green body shell becomes glossy cherry red.",
    "target_phrase": "glossy cherry-red toy car"
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
      14.5,
      19.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The body shell, front grille, wheels, and raised wind-up key are clear in the low tracking view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_085_E2A

```json
{
  "video_id": "synthetic_object_085",
  "edit_id": "synthetic_object_085_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_085.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_above_the_moving_toy_car",
    "target_description": "the camera path above the moving toy car",
    "source_state": "The camera follows the car from a low front-side angle along the marked wooden route.",
    "desired_change": "The camera rises into a near-overhead tracking view while following the car for five seconds."
  },
  "timing": {
    "edit_point_sec": 36,
    "effect_start_sec": 36,
    "effect_end_sec": 41,
    "evaluation_window_sec": [
      35,
      43
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 36 seconds, raise the camera into a near-overhead tracking view while following the moving toy car for five seconds.",
  "expected_result": {
    "description": "The camera rises into a near-overhead tracking view while following the car for five seconds.",
    "target_phrase": "near-overhead tracking view of the toy car"
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
      35,
      43
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full car, black route lines, board edges, and surrounding tabletop provide stable depth references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_085_E2B

```json
{
  "video_id": "synthetic_object_085",
  "edit_id": "synthetic_object_085_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_085_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_toy_car_s_circular_wind_up_key",
    "target_description": "the toy car's circular wind-up key",
    "source_state": "The raised circular key turns gradually as the toy car follows the curved route.",
    "desired_change": "The circular key completes three rapid clockwise rotations while the car continues around the bend."
  },
  "timing": {
    "edit_point_sec": 26.5,
    "effect_start_sec": 26.5,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      25.5,
      32.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 26.5 seconds, make the toy car's raised circular key complete three rapid clockwise rotations while rounding the bend.",
  "expected_result": {
    "description": "The circular key completes three rapid clockwise rotations while the car continues around the bend.",
    "target_phrase": "wind-up key rotating clockwise three times"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_085_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25.5,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The key remains silhouetted above the complete car during the clear side-front view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_085_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the toy car's circular wind-up key on B independently of E1's change to the toy car's green body shell; both edit results must coexist in C."
  }
}
```

## synthetic_object_086

### synthetic_object_086_E1

```json
{
  "video_id": "synthetic_object_086",
  "edit_id": "synthetic_object_086_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_086.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_camera_s_black_body_covering",
    "target_description": "the camera's black body covering",
    "source_state": "The displayed camera body has a black pebbled covering around its silver details.",
    "desired_change": "The black body covering becomes smooth warm ivory."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      13.5,
      18.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 14.5 seconds, change the displayed camera's black pebbled body covering to smooth warm ivory over two seconds.",
  "expected_result": {
    "description": "The black body covering becomes smooth warm ivory.",
    "target_phrase": "warm-ivory camera body covering"
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
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The front body panels, lens barrel, viewfinder windows, and top controls fill the unobstructed close view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_086_E2A

```json
{
  "video_id": "synthetic_object_086",
  "edit_id": "synthetic_object_086_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_086.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Multi-object Relationship",
    "operation": "Relationship Repositioning",
    "scope": "Multiple Objects"
  },
  "target": {
    "target_id": "the_camera_body_relative_to_the_black_display_disk",
    "target_description": "the camera body relative to the black display disk",
    "source_state": "The camera body stands near the center of the black circular display disk.",
    "desired_change": "The camera is positioned half a body-depth toward the disk's front edge without crossing the rim."
  },
  "timing": {
    "edit_point_sec": 33.5,
    "effect_start_sec": 33.5,
    "effect_end_sec": 34.5,
    "evaluation_window_sec": [
      32.5,
      36.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 33.5 seconds, move the displayed camera half a body-depth toward the front edge of the black circular disk.",
  "expected_result": {
    "description": "The camera is positioned half a body-depth toward the disk's front edge without crossing the rim.",
    "target_phrase": "camera closer to the display disk's front edge"
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
      32.5,
      36.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The camera base, circular disk, silver perimeter ring, and free front area are visible in the side-rear view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_086_E2B

```json
{
  "video_id": "synthetic_object_086",
  "edit_id": "synthetic_object_086_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_086_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_displayed_camera_s_rotation",
    "target_description": "the displayed camera's rotation",
    "source_state": "The camera turns gradually around a vertical axis during the product display.",
    "desired_change": "The camera rotates at twice its original angular speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 32,
    "evaluation_window_sec": [
      26,
      34
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 27 seconds, make the displayed camera rotate around its vertical axis at twice the original speed for five seconds.",
  "expected_result": {
    "description": "The camera rotates at twice its original angular speed for five seconds.",
    "target_phrase": "displayed camera rotating twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_086_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26,
      34
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete camera, fixed disk outline, tabletop, and blurred cabinet provide reliable angular-motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_086_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the displayed camera's rotation on B independently of E1's change to the camera's black body covering; both edit results must coexist in C."
  }
}
```

## synthetic_object_087

### synthetic_object_087_E1

```json
{
  "video_id": "synthetic_object_087",
  "edit_id": "synthetic_object_087_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_087.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Background Style Change",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_tabletop_background_outside_the_bowl",
    "target_description": "the tabletop background outside the bowl",
    "source_state": "A neutral gray finely textured tabletop surrounds the white bowl.",
    "desired_change": "Only the surrounding tabletop is rendered as a dark indigo watercolor wash."
  },
  "timing": {
    "edit_point_sec": 11,
    "effect_start_sec": 11,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      10,
      15
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 11 seconds, render only the tabletop surrounding the white bowl as a dark indigo watercolor wash over two seconds.",
  "expected_result": {
    "description": "Only the surrounding tabletop is rendered as a dark indigo watercolor wash.",
    "target_phrase": "indigo watercolor tabletop around the bowl"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      10,
      15
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "A broad ring of tabletop remains visible around the stationary bowl and moving green marble."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_087_E2A

```json
{
  "video_id": "synthetic_object_087",
  "edit_id": "synthetic_object_087_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_087.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_around_the_bowl",
    "target_description": "the camera path around the bowl",
    "source_state": "The camera holds a fixed oblique overhead view of the bowl and rolling marble.",
    "desired_change": "The camera makes a smooth half-circle arc from the near side to the far side of the bowl."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 35.5,
    "evaluation_window_sec": [
      29.5,
      37.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 30.5 seconds, move the camera in a smooth half-circle arc from the near side to the far side of the bowl.",
  "expected_result": {
    "description": "The camera makes a smooth half-circle arc from the near side to the far side of the bowl.",
    "target_phrase": "half-circle camera arc around the bowl"
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
      29.5,
      37.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The circular rim, bowl center, marble, and tabletop texture provide stable parallax references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_087_E2B

```json
{
  "video_id": "synthetic_object_087",
  "edit_id": "synthetic_object_087_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_087_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_green_marble_s_rolling_motion",
    "target_description": "the green marble's rolling motion",
    "source_state": "The green marble continues rolling around the inner slope of the stationary white bowl.",
    "desired_change": "The marble rolls at twice its original speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 24,
    "effect_start_sec": 24,
    "effect_end_sec": 29,
    "evaluation_window_sec": [
      23,
      31
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 24 seconds, make the green marble roll around the bowl at twice its original speed for five seconds.",
  "expected_result": {
    "description": "The marble rolls at twice its original speed for five seconds.",
    "target_phrase": "green marble rolling twice as fast"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_087_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      23,
      31
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The marble remains visible against the white interior while the fixed rim provides a speed reference."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_087_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the green marble's rolling motion on B independently of E1's change to the tabletop background outside the bowl; both edit results must coexist in C."
  }
}
```

## synthetic_object_088

### synthetic_object_088_E1

```json
{
  "video_id": "synthetic_object_088",
  "edit_id": "synthetic_object_088_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_088.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_pale_display_surface_beneath_the_shoe",
    "target_description": "the pale display surface beneath the shoe",
    "source_state": "The white athletic shoe rests on a smooth pale display surface.",
    "desired_change": "The display surface becomes dark navy felt with a fine woven texture."
  },
  "timing": {
    "edit_point_sec": 17,
    "effect_start_sec": 17,
    "effect_end_sec": 19,
    "evaluation_window_sec": [
      16,
      21
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 17 seconds, change the pale display surface beneath the athletic shoe to dark navy felt over two seconds.",
  "expected_result": {
    "description": "The display surface becomes dark navy felt with a fine woven texture.",
    "target_phrase": "dark navy felt display surface"
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
      16,
      21
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The support surface is exposed around the shoe sole and clearly separated from the blurred room background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_088_E2A

```json
{
  "video_id": "synthetic_object_088",
  "edit_id": "synthetic_object_088_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_088.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Color/Tone/Graphic Texture",
    "operation": "Global Tone and Texture Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_athletic_shoe_display_scene",
    "target_description": "the full athletic-shoe display scene",
    "source_state": "The shoe display has neutral white, gray, and softly colored indoor tones.",
    "desired_change": "The full scene adopts a cool black-and-white grade with crisp tonal contrast."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 36.5,
    "evaluation_window_sec": [
      33.5,
      38.5
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 34.5 seconds, convert the full athletic-shoe display into cool black and white with crisp tonal contrast over two seconds.",
  "expected_result": {
    "description": "The full scene adopts a cool black-and-white grade with crisp tonal contrast.",
    "target_phrase": "cool black-and-white athletic-shoe display"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.5,
      38.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The shoe, support surface, ceiling lights, and distant interior are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_088_E2B

```json
{
  "video_id": "synthetic_object_088",
  "edit_id": "synthetic_object_088_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_088_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_athletic_shoe_on_its_display_surface",
    "target_description": "the athletic shoe on its display surface",
    "source_state": "The complete shoe rests near the central portion of the pale display surface.",
    "desired_change": "The shoe is shifted one shoe-width toward the right side of the display surface."
  },
  "timing": {
    "edit_point_sec": 27.5,
    "effect_start_sec": 27.5,
    "effect_end_sec": 28.5,
    "evaluation_window_sec": [
      26.5,
      30.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 27.5 seconds, shift the complete athletic shoe one shoe-width toward the right side of the display surface.",
  "expected_result": {
    "description": "The shoe is shifted one shoe-width toward the right side of the display surface.",
    "target_phrase": "athletic shoe shifted right on the display"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_088_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.5,
      30.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full sole outline and unoccupied surface to the right are visible before the shoe rotates toward the front."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_088_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the athletic shoe on its display surface on B independently of E1's change to the pale display surface beneath the shoe; both edit results must coexist in C."
  }
}
```

## synthetic_object_089

### synthetic_object_089_E1

```json
{
  "video_id": "synthetic_object_089",
  "edit_id": "synthetic_object_089_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_089.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_moving_spotlight_across_the_crystal_cluster",
    "target_description": "the moving spotlight across the crystal cluster",
    "source_state": "A bright spotlight sweeps gradually from the central crystal toward the right-side crystal points.",
    "desired_change": "The spotlight crosses the same visible path at twice its original sweep speed."
  },
  "timing": {
    "edit_point_sec": 16.5,
    "effect_start_sec": 16.5,
    "effect_end_sec": 21.5,
    "evaluation_window_sec": [
      15.5,
      23.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 16.5 seconds, make the spotlight sweep across the crystal cluster at twice its original speed for five seconds.",
  "expected_result": {
    "description": "The spotlight crosses the same visible path at twice its original sweep speed.",
    "target_phrase": "spotlight sweeping across the crystals twice as fast"
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
      15.5,
      23.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The moving highlight, fixed crystal facets, tabletop glow, and dark background make the sweep directly observable."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_089_E2A

```json
{
  "video_id": "synthetic_object_089",
  "edit_id": "synthetic_object_089_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_089.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_crystal_cluster_on_the_illuminated_tabletop",
    "target_description": "the crystal cluster on the illuminated tabletop",
    "source_state": "The crystal cluster stands near the center of its illuminated tabletop region.",
    "desired_change": "The full cluster is shifted one cluster-width toward the right side of the illuminated region."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      30.5,
      34.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.5 seconds, shift the entire crystal cluster one cluster-width toward the right side of the illuminated tabletop region.",
  "expected_result": {
    "description": "The full cluster is shifted one cluster-width toward the right side of the illuminated region.",
    "target_phrase": "crystal cluster shifted to the right"
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
      30.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full dark base and open lit tabletop to its right are visible during the wide-facing orientation."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_089_E2B

```json
{
  "video_id": "synthetic_object_089",
  "edit_id": "synthetic_object_089_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_089_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_tallest_central_purple_crystal_tip",
    "target_description": "the tallest central purple crystal tip",
    "source_state": "The tallest central purple crystal ends in a complete sharp faceted point.",
    "desired_change": "The point becomes visibly chipped with one small triangular section missing."
  },
  "timing": {
    "edit_point_sec": 28.5,
    "effect_start_sec": 28.5,
    "effect_end_sec": 29.5,
    "evaluation_window_sec": [
      27.5,
      31.5
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "At 28.5 seconds, chip one small triangular section from the tip of the tallest central purple crystal.",
  "expected_result": {
    "description": "The point becomes visibly chipped with one small triangular section missing.",
    "target_phrase": "chipped tip on the tallest purple crystal"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_089_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.5,
      31.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tall central point is distinct from the shorter surrounding crystals in the rotating display."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_089_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the tallest central purple crystal tip on B independently of E1's change to the moving spotlight across the crystal cluster; both edit results must coexist in C."
  }
}
```

## synthetic_object_090

### synthetic_object_090_E1

```json
{
  "video_id": "synthetic_object_090",
  "edit_id": "synthetic_object_090_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_globe_s_dark_circular_support_frame",
    "target_description": "the globe's dark circular support frame",
    "source_state": "The globe sphere is held inside a dark brown circular support frame.",
    "desired_change": "The circular support frame becomes brushed silver."
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
  "instruction": "Starting at 14 seconds, change the globe's dark brown circular support frame to brushed silver over two seconds.",
  "expected_result": {
    "description": "The circular support frame becomes brushed silver.",
    "target_phrase": "brushed-silver globe support frame"
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
    "description": "The complete circular frame is visible around the rotating sphere against the plain gray background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_090_E2A

```json
{
  "video_id": "synthetic_object_090",
  "edit_id": "synthetic_object_090_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_090.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Core Object Style Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_globe_sphere",
    "target_description": "the globe sphere",
    "source_state": "The sphere has a conventional colored printed world-map appearance.",
    "desired_change": "Only the sphere is rendered as an embossed antique-bronze relief globe."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 36.5,
    "evaluation_window_sec": [
      33.5,
      38.5
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 34.5 seconds, render only the globe sphere as an embossed antique-bronze relief object over the next two seconds.",
  "expected_result": {
    "description": "Only the sphere is rendered as an embossed antique-bronze relief globe.",
    "target_phrase": "antique-bronze relief globe sphere"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      33.5,
      38.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The sphere is centered inside the stable support ring and its full circular boundary remains visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_090_E2B

```json
{
  "video_id": "synthetic_object_090",
  "edit_id": "synthetic_object_090_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_090_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_globe_sphere_s_rotation",
    "target_description": "the globe sphere's rotation",
    "source_state": "The globe sphere rotates steadily within its stationary circular frame.",
    "desired_change": "The sphere rotates at half its original angular speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 26.5,
    "effect_start_sec": 26.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      25.5,
      33.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 26.5 seconds, reduce the globe sphere's rotation to half its original angular speed for five seconds.",
  "expected_result": {
    "description": "The sphere rotates at half its original angular speed for five seconds.",
    "target_phrase": "globe sphere rotating at half speed"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_090_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The stationary frame and changing continental silhouettes provide a clear angular-speed reference."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_090_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the globe sphere's rotation on B independently of E1's change to the globe's dark circular support frame; both edit results must coexist in C."
  }
}
```

## synthetic_object_091

### synthetic_object_091_E1

```json
{
  "video_id": "synthetic_object_091",
  "edit_id": "synthetic_object_091_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_091.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_pale_support_surface_beneath_the_pen",
    "target_description": "the pale support surface beneath the pen",
    "source_state": "The fountain pen and separated cap rest on a smooth pale support surface.",
    "desired_change": "The support surface becomes dark forest-green felt with a fine woven texture."
  },
  "timing": {
    "edit_point_sec": 10.5,
    "effect_start_sec": 10.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      9.5,
      14.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 10.5 seconds, change the pale support surface beneath the fountain pen to dark forest-green felt over two seconds.",
  "expected_result": {
    "description": "The support surface becomes dark forest-green felt with a fine woven texture.",
    "target_phrase": "forest-green felt beneath the pen"
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
      9.5,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Exposed support surface surrounds the pen tip, cap, and silver fittings in the close view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_091_E2A

```json
{
  "video_id": "synthetic_object_091",
  "edit_id": "synthetic_object_091_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_091.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_surface_above_the_fountain_pen_barrel",
    "target_description": "the open surface above the fountain pen barrel",
    "source_state": "No ink container occupies the clear support surface above the fountain pen barrel.",
    "desired_change": "One square cobalt-blue glass ink bottle is added one pen-width above the barrel."
  },
  "timing": {
    "edit_point_sec": 32.5,
    "effect_start_sec": 32.5,
    "effect_end_sec": 33.5,
    "evaluation_window_sec": [
      31.5,
      35.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 32.5 seconds, add one square cobalt-blue glass ink bottle on the surface one pen-width above the fountain pen barrel.",
  "expected_result": {
    "description": "One square cobalt-blue glass ink bottle is added one pen-width above the barrel.",
    "target_phrase": "cobalt-blue ink bottle above the pen"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      31.5,
      35.5
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The complete barrel and an open, stable surface region above it are visible in the wider view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_091_E2B

```json
{
  "video_id": "synthetic_object_091",
  "edit_id": "synthetic_object_091_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_091_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_separated_pen_cap",
    "target_description": "the separated pen cap",
    "source_state": "The black pen cap remains stationary below and to the right of the exposed nib.",
    "desired_change": "The cap rolls one complete turn toward the nib and stops one cap-width away."
  },
  "timing": {
    "edit_point_sec": 22,
    "effect_start_sec": 22,
    "effect_end_sec": 26,
    "evaluation_window_sec": [
      21,
      28
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 22 seconds, make the separated pen cap roll one complete turn toward the nib and stop one cap-width away.",
  "expected_result": {
    "description": "The cap rolls one complete turn toward the nib and stops one cap-width away.",
    "target_phrase": "pen cap rolling once toward the nib"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_091_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      21,
      28
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The cap, exposed nib, intervening gap, and flat support surface are simultaneously visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_091_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the separated pen cap on B independently of E1's change to the pale support surface beneath the pen; both edit results must coexist in C."
  }
}
```

## synthetic_object_092

### synthetic_object_092_E1

```json
{
  "video_id": "synthetic_object_092",
  "edit_id": "synthetic_object_092_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_092.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Art/Rendering Style",
    "operation": "Global Rendering Style Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_open_padlock_scene",
    "target_description": "the full open-padlock scene",
    "source_state": "The open brass padlock and wooden tabletop have realistic photographic textures.",
    "desired_change": "The full scene is transformed into a detailed ink-and-watercolor illustration."
  },
  "timing": {
    "edit_point_sec": 15,
    "effect_start_sec": 15,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      14,
      19
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 15 seconds, transform the full open-padlock scene into a detailed ink-and-watercolor illustration over two seconds.",
  "expected_result": {
    "description": "The full scene is transformed into a detailed ink-and-watercolor illustration.",
    "target_phrase": "ink-and-watercolor open-padlock scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      14,
      19
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The lock body, open shackle, tabletop grain, reflections, and plain backdrop are visible together."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_092_E2A

```json
{
  "video_id": "synthetic_object_092",
  "edit_id": "synthetic_object_092_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_092.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Environment Object",
    "operation": "Environment Appearance Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_wooden_tabletop_beneath_the_padlock",
    "target_description": "the wooden tabletop beneath the padlock",
    "source_state": "The open padlock rests on a warm brown wood-grain tabletop.",
    "desired_change": "The tabletop becomes polished white marble with soft gray veins."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      34.5,
      39.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 35.5 seconds, change the wooden tabletop beneath the open padlock to polished white marble with soft gray veins.",
  "expected_result": {
    "description": "The tabletop becomes polished white marble with soft gray veins.",
    "target_phrase": "white marble tabletop beneath the padlock"
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
      34.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The support surface remains exposed around the full lock and beneath its reflected outline."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_092_E2B

```json
{
  "video_id": "synthetic_object_092",
  "edit_id": "synthetic_object_092_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_092_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_padlock_s_free_shackle_end",
    "target_description": "the padlock's free shackle end",
    "source_state": "The silver shackle remains open with its left end held above the top socket.",
    "desired_change": "The free shackle end swings outward by ninety degrees and returns once around the fixed right connection."
  },
  "timing": {
    "edit_point_sec": 27.5,
    "effect_start_sec": 27.5,
    "effect_end_sec": 31.5,
    "evaluation_window_sec": [
      26.5,
      33.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 27.5 seconds, make the padlock's free shackle end swing outward ninety degrees and return once around the right connection.",
  "expected_result": {
    "description": "The free shackle end swings outward by ninety degrees and returns once around the fixed right connection.",
    "target_phrase": "open shackle swinging outward and returning"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_092_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26.5,
      33.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The free left end, top socket, fixed right connection, and complete lock body remain visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_092_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the padlock's free shackle end on B independently of E1's change to the full open-padlock scene; both edit results must coexist in C."
  }
}
```

## synthetic_object_093

### synthetic_object_093_E1

```json
{
  "video_id": "synthetic_object_093",
  "edit_id": "synthetic_object_093_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_093.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_left_edge_of_the_paper_stack",
    "target_description": "the left edge of the paper stack",
    "source_state": "No alignment marker is attached to the exposed left edge of the white paper stack.",
    "desired_change": "One small blue rectangular alignment tab is added to the middle of the stack's left edge."
  },
  "timing": {
    "edit_point_sec": 12,
    "effect_start_sec": 12,
    "effect_end_sec": 13,
    "evaluation_window_sec": [
      11,
      15
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 12 seconds, add one small blue rectangular alignment tab to the middle of the white paper stack's exposed left edge.",
  "expected_result": {
    "description": "One small blue rectangular alignment tab is added to the middle of the stack's left edge.",
    "target_phrase": "blue alignment tab on the paper stack"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      11,
      15
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The left paper edge is unobstructed beside the raised stapler handle and offers a stable attachment point."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_093_E2A

```json
{
  "video_id": "synthetic_object_093",
  "edit_id": "synthetic_object_093_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_093.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_stapler_s_silver_upper_handle",
    "target_description": "the stapler's silver upper handle",
    "source_state": "The long upper handle has a smooth silver metal appearance.",
    "desired_change": "The upper handle becomes glossy signal red."
  },
  "timing": {
    "edit_point_sec": 32.5,
    "effect_start_sec": 32.5,
    "effect_end_sec": 34.5,
    "evaluation_window_sec": [
      31.5,
      36.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 32.5 seconds, change the stapler's long silver upper handle to glossy signal red over the next two seconds.",
  "expected_result": {
    "description": "The upper handle becomes glossy signal red.",
    "target_phrase": "glossy red stapler handle"
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
      31.5,
      36.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The full upper handle is lowered but visible above the white paper stack and silver base."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_093_E2B

```json
{
  "video_id": "synthetic_object_093",
  "edit_id": "synthetic_object_093_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_093_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_stapler_handle_and_paper_stack",
    "target_description": "the stapler handle and paper stack",
    "source_state": "The raised handle is ready above the stack positioned between the stapler head and base.",
    "desired_change": "The upper handle presses the paper stack twice and rebounds fully after each contact."
  },
  "timing": {
    "edit_point_sec": 21.5,
    "effect_start_sec": 21.5,
    "effect_end_sec": 26.5,
    "evaluation_window_sec": [
      20.5,
      28.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 21.5 seconds, make the stapler handle press the paper stack twice and rebound fully after each contact.",
  "expected_result": {
    "description": "The upper handle presses the paper stack twice and rebounds fully after each contact.",
    "target_phrase": "stapler pressing the paper stack twice"
  },
  "constraints": {
    "preserve": [
      "target identity and appearance",
      "non-target entities",
      "scene layout",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_093_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      20.5,
      28.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The raised handle, paper layers, base, pivot, and supporting gloved hands remain visible through the repeated contact."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_093_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the stapler handle and paper stack on B independently of E1's change to the left edge of the paper stack; both edit results must coexist in C."
  }
}
```

## synthetic_object_094

### synthetic_object_094_E1

```json
{
  "video_id": "synthetic_object_094",
  "edit_id": "synthetic_object_094_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_094.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_extended_yellow_measuring_tape",
    "target_description": "the extended yellow measuring tape",
    "source_state": "The yellow metal tape is held taut and nearly straight between the two gloved hands.",
    "desired_change": "The extended tape becomes visibly slack with two broad downward bends between the hands."
  },
  "timing": {
    "edit_point_sec": 16,
    "effect_start_sec": 16,
    "effect_end_sec": 18,
    "evaluation_window_sec": [
      15,
      20
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "Starting at 16 seconds, make the extended yellow measuring tape slack with two broad downward bends over the next two seconds.",
  "expected_result": {
    "description": "The extended tape becomes visibly slack with two broad downward bends between the hands.",
    "target_phrase": "slack measuring tape with two bends"
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
      20
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The tape spans the full gap between both hands and remains clearly separated from the person's dark clothing."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_094_E2A

```json
{
  "video_id": "synthetic_object_094",
  "edit_id": "synthetic_object_094_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_094.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Core Object-local Style",
    "operation": "Core Object Style Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_tape_measure_housing_and_extended_yellow_tape",
    "target_description": "the tape-measure housing and extended yellow tape",
    "source_state": "The tape-measure housing and extended yellow tape use realistic photographic materials and lighting.",
    "desired_change": "Only the tape-measure housing and extended yellow tape are rendered as clean colored-pencil artwork."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      29.5,
      34.5
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 30.5 seconds, render the tape-measure housing and extended yellow tape as clean colored-pencil artwork over the next two seconds.",
  "expected_result": {
    "description": "Only the tape-measure housing and extended yellow tape are rendered as clean colored-pencil artwork.",
    "target_phrase": "colored-pencil tape measure and extended tape"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "target boundary: Only the tape-measure housing and yellow tape material rendering are editable; tape graduations, numbers, logos, hands, face, and background remain protected."
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      29.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The housing and extended tape are fully visible and separable from the hands and background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_094_E2B

```json
{
  "video_id": "synthetic_object_094",
  "edit_id": "synthetic_object_094_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_094_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Removal",
    "operation": "Removal",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_physical_red_locking_button_on_top_of_the_tape_housing",
    "target_description": "the physical red locking button on top of the tape housing",
    "source_state": "A small physical red locking button protrudes from the top of the silver tape-measure housing.",
    "desired_change": "The physical red locking button is removed from the housing."
  },
  "timing": {
    "edit_point_sec": 27,
    "effect_start_sec": 27,
    "effect_end_sec": 28,
    "evaluation_window_sec": [
      26,
      30
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 27 seconds, remove the physical red locking button protruding from the top of the silver tape-measure housing.",
  "expected_result": {
    "description": "The physical red locking button is removed from the housing.",
    "target_phrase": "top red locking button removed"
  },
  "constraints": {
    "preserve": [
      "non-target entities",
      "existing actions",
      "non-target spatial relationships",
      "background appearance",
      "camera behavior",
      "target boundary: Only the physical red locking button is editable; tape graduations, numbers, labels, and printed markings remain protected.",
      "visual result of synthetic_object_094_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      26,
      30
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The red button is isolated above the silver housing while the left hand holds the case steady."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_094_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the physical red locking button on top of the tape housing on B independently of E1's change to the extended yellow measuring tape; both edit results must coexist in C."
  }
}
```

## synthetic_object_095

### synthetic_object_095_E1

```json
{
  "video_id": "synthetic_object_095",
  "edit_id": "synthetic_object_095_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Camera Movement",
    "operation": "Camera Trajectory Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_camera_path_above_the_cutting_action",
    "target_description": "the camera path above the cutting action",
    "source_state": "The camera observes the scissors and sheet from a low oblique overhead angle.",
    "desired_change": "The camera rises to a near-overhead view and tracks the blades along the visible red cutting line."
  },
  "timing": {
    "edit_point_sec": 14.5,
    "effect_start_sec": 14.5,
    "effect_end_sec": 19.5,
    "evaluation_window_sec": [
      13.5,
      21.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 14.5 seconds, raise the camera to a near-overhead view and track the scissors along the red cutting line for five seconds.",
  "expected_result": {
    "description": "The camera rises to a near-overhead view and tracks the blades along the visible red cutting line.",
    "target_phrase": "overhead tracking view of the cutting action"
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
      13.5,
      21.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The moving blades, red guide line, sheet edge, and supporting hands provide stable path and depth references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_095_E2A

```json
{
  "video_id": "synthetic_object_095",
  "edit_id": "synthetic_object_095_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_095.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_scissors_visible_outer_silver_ring_handle",
    "target_description": "the scissors' visible outer silver ring handle",
    "source_state": "The visible outer ring handle has the same plain silver finish as the blades.",
    "desired_change": "The visible outer ring handle becomes glossy bright red."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 37.5,
    "evaluation_window_sec": [
      34.5,
      39.5
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 35.5 seconds, coat the scissors' visible outer silver ring handle in glossy bright red enamel over two seconds.",
  "expected_result": {
    "description": "The visible outer ring handle becomes glossy bright red.",
    "target_phrase": "bright-red outer scissor ring handle"
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
      34.5,
      39.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The outer handle loop is unobstructed beside the operator's black glove and remains distinct from the silver blades."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_095_E2B

```json
{
  "video_id": "synthetic_object_095",
  "edit_id": "synthetic_object_095_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_095_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Background-local Style",
    "operation": "Background Style Change",
    "scope": "Background"
  },
  "target": {
    "target_id": "the_exposed_tabletop_around_the_cut_sheet",
    "target_description": "the exposed tabletop around the cut sheet",
    "source_state": "A plain smooth gray tabletop surrounds the pale sheet and scissors.",
    "desired_change": "Only the exposed tabletop is rendered as textured blue watercolor paper."
  },
  "timing": {
    "edit_point_sec": 25.5,
    "effect_start_sec": 25.5,
    "effect_end_sec": 27.5,
    "evaluation_window_sec": [
      24.5,
      29.5
    ],
    "temporal_behavior": "gradual persistent local style change"
  },
  "instruction": "Starting at 25.5 seconds, render only the exposed gray tabletop around the cut sheet as textured blue watercolor paper.",
  "expected_result": {
    "description": "Only the exposed tabletop is rendered as textured blue watercolor paper.",
    "target_phrase": "blue watercolor-paper tabletop"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions",
      "visual result of synthetic_object_095_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24.5,
      29.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "Exposed tabletop remains visible below the sheet edge and around the moving scissors."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_095_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the exposed tabletop around the cut sheet on B independently of E1's change to the camera path above the cutting action; both edit results must coexist in C."
  }
}
```

## synthetic_object_096

### synthetic_object_096_E1

```json
{
  "video_id": "synthetic_object_096",
  "edit_id": "synthetic_object_096_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_vase_s_blue_glazed_body",
    "target_description": "the vase's blue glazed body",
    "source_state": "The vase has a blue glaze with pale violet highlights and tan raised ornaments.",
    "desired_change": "The blue glazed body becomes deep emerald green."
  },
  "timing": {
    "edit_point_sec": 10,
    "effect_start_sec": 10,
    "effect_end_sec": 12,
    "evaluation_window_sec": [
      9,
      14
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 10 seconds, change the vase's blue glazed body to deep emerald green over the next two seconds.",
  "expected_result": {
    "description": "The blue glazed body becomes deep emerald green.",
    "target_phrase": "deep emerald-green glazed vase"
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
      9,
      14
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete vase profile and broad glazed belly are visible against the softly blurred trees."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_096_E2A

```json
{
  "video_id": "synthetic_object_096",
  "edit_id": "synthetic_object_096_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_096.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Kinematic Adjustment",
    "operation": "Kinematic Adjustment",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_vase_s_vertical_axis_rotation",
    "target_description": "the vase's vertical-axis rotation",
    "source_state": "The upright vase turns gradually while its raised ornament moves across the visible side.",
    "desired_change": "The vase rotates around its vertical axis at twice its original angular speed for five seconds."
  },
  "timing": {
    "edit_point_sec": 30.5,
    "effect_start_sec": 30.5,
    "effect_end_sec": 35.5,
    "evaluation_window_sec": [
      29.5,
      37.5
    ],
    "temporal_behavior": "bounded motion modification"
  },
  "instruction": "Starting at 30.5 seconds, make the upright vase rotate around its vertical axis at twice the original speed for five seconds.",
  "expected_result": {
    "description": "The vase rotates around its vertical axis at twice its original angular speed for five seconds.",
    "target_phrase": "vase rotating twice as fast"
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
      29.5,
      37.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The raised ornament, neck profile, fixed circular tabletop, and distant trees provide angular-motion references."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_096_E2B

```json
{
  "video_id": "synthetic_object_096",
  "edit_id": "synthetic_object_096_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_096_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Absolute Position",
    "operation": "Absolute Repositioning",
    "scope": "Specified Object"
  },
  "target": {
    "target_id": "the_vase_on_the_white_circular_tabletop",
    "target_description": "the vase on the white circular tabletop",
    "source_state": "The upright vase stands near the center of the white circular tabletop.",
    "desired_change": "The vase is shifted onto the right half of the tabletop while remaining fully supported."
  },
  "timing": {
    "edit_point_sec": 23,
    "effect_start_sec": 23,
    "effect_end_sec": 24,
    "evaluation_window_sec": [
      22,
      26
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 23 seconds, shift the upright vase onto the right half of the white circular tabletop.",
  "expected_result": {
    "description": "The vase is shifted onto the right half of the tabletop while remaining fully supported.",
    "target_phrase": "vase positioned on the tabletop's right half"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity appearances",
      "entity count",
      "ongoing actions",
      "background environment",
      "camera behavior",
      "visual result of synthetic_object_096_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      22,
      26
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The complete vase base and open right half of the circular support surface are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_096_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the vase on the white circular tabletop on B independently of E1's change to the vase's blue glazed body; both edit results must coexist in C."
  }
}
```

## synthetic_object_097

### synthetic_object_097_E1

```json
{
  "video_id": "synthetic_object_097",
  "edit_id": "synthetic_object_097_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_097.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Spatial",
    "secondary_type": "Orientation",
    "operation": "Orientation Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_spiral_shell_s_aperture_orientation",
    "target_description": "the spiral shell's aperture orientation",
    "source_state": "The shell aperture points diagonally toward the upper-right side of the frame.",
    "desired_change": "The shell is rotated until the aperture faces directly toward the camera."
  },
  "timing": {
    "edit_point_sec": 15.5,
    "effect_start_sec": 15.5,
    "effect_end_sec": 16.5,
    "evaluation_window_sec": [
      14.5,
      18.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 15.5 seconds, rotate the spiral shell until its large aperture faces directly toward the camera.",
  "expected_result": {
    "description": "The shell is rotated until the aperture faces directly toward the camera.",
    "target_phrase": "shell aperture facing the camera"
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
      14.5,
      18.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The aperture rim, central spiral, and complete shell outline are visible against the uniform black background."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_097_E2A

```json
{
  "video_id": "synthetic_object_097",
  "edit_id": "synthetic_object_097_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_097.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Replacement",
    "operation": "Replacement",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_brown_spiral_shell",
    "target_description": "the brown spiral shell",
    "source_state": "A single brown spiral shell with pale radial bands occupies the black background.",
    "desired_change": "The brown spiral shell is replaced by one white ridged conch shell of comparable size."
  },
  "timing": {
    "edit_point_sec": 31.5,
    "effect_start_sec": 31.5,
    "effect_end_sec": 32.5,
    "evaluation_window_sec": [
      30.5,
      34.5
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 31.5 seconds, replace the brown spiral shell with one white ridged conch shell of comparable size.",
  "expected_result": {
    "description": "The brown spiral shell is replaced by one white ridged conch shell of comparable size.",
    "target_phrase": "white ridged conch shell"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      30.5,
      34.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The isolated shell has a complete silhouette and no contact with another visible object."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_097_E2B

```json
{
  "video_id": "synthetic_object_097",
  "edit_id": "synthetic_object_097_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_097_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Physical State",
    "operation": "Physical State Change",
    "scope": "Core Object or Environment Object"
  },
  "target": {
    "target_id": "the_lowest_visible_edge_of_the_shell_s_outer_lip",
    "target_description": "the lowest visible edge of the shell's outer lip",
    "source_state": "The shell's pale outer lip has a continuous smooth lower edge.",
    "desired_change": "One small triangular chip appears in the lowest visible lip edge."
  },
  "timing": {
    "edit_point_sec": 26,
    "effect_start_sec": 26,
    "effect_end_sec": 27,
    "evaluation_window_sec": [
      25,
      29
    ],
    "temporal_behavior": "gradual persistent state change"
  },
  "instruction": "At 26 seconds, create one small triangular chip in the lowest visible edge of the shell's pale outer lip.",
  "expected_result": {
    "description": "One small triangular chip appears in the lowest visible lip edge.",
    "target_phrase": "triangular chip in the shell lip"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_097_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      25,
      29
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The pale lip edge is sharply silhouetted against black in the stable oblique view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_097_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the lowest visible edge of the shell's outer lip on B independently of E1's change to the spiral shell's aperture orientation; both edit results must coexist in C."
  }
}
```

## synthetic_object_098

### synthetic_object_098_E1

```json
{
  "video_id": "synthetic_object_098",
  "edit_id": "synthetic_object_098_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_098.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Composition",
    "secondary_type": "Entity Addition",
    "operation": "Addition",
    "scope": "Related Object"
  },
  "target": {
    "target_id": "the_open_stump_surface_left_of_the_pine_cone",
    "target_description": "the open stump surface left of the pine cone",
    "source_state": "No second object occupies the exposed stump surface immediately left of the pine cone.",
    "desired_change": "One small brown acorn is added one pine-cone width to the left of the pine cone."
  },
  "timing": {
    "edit_point_sec": 16,
    "effect_start_sec": 16,
    "effect_end_sec": 17,
    "evaluation_window_sec": [
      15,
      19
    ],
    "temporal_behavior": "instant persistent change"
  },
  "instruction": "At 16 seconds, add one small brown acorn on the stump one pine-cone width to the left of the pine cone.",
  "expected_result": {
    "description": "One small brown acorn is added one pine-cone width to the left of the pine cone.",
    "target_phrase": "brown acorn left of the pine cone"
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
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      15,
      19
    ],
    "target_visible": false,
    "target_stability": "not applicable; target is newly added",
    "occlusion_level": "placement anchor has none or low occlusion",
    "shot_continuity": "continuous within the selected window",
    "description": "The new target is absent in the source, while its placement anchor remains identifiable around the edit point. The complete pine cone and a clear, stable patch of stump surface to its left are visible."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_098_E2A

```json
{
  "video_id": "synthetic_object_098",
  "edit_id": "synthetic_object_098_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_098.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Camera",
    "secondary_type": "Framing/Zoom",
    "operation": "Framing Change",
    "scope": "Camera"
  },
  "target": {
    "target_id": "the_framing_around_the_pine_cone_and_stump",
    "target_description": "the framing around the pine cone and stump",
    "source_state": "The frame includes the pine cone and part of the circular stump top.",
    "desired_change": "The camera widens until the complete stump top, bark edge, and a surrounding band of grass are visible."
  },
  "timing": {
    "edit_point_sec": 35.5,
    "effect_start_sec": 35.5,
    "effect_end_sec": 40.5,
    "evaluation_window_sec": [
      34.5,
      42.5
    ],
    "temporal_behavior": "camera trajectory change"
  },
  "instruction": "Starting at 35.5 seconds, smoothly zoom out until the complete stump top, bark edge, and a surrounding band of grass are visible.",
  "expected_result": {
    "description": "The camera widens until the complete stump top, bark edge, and a surrounding band of grass are visible.",
    "target_phrase": "complete stump and surrounding grass framed"
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
      34.5,
      42.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The pine cone remains centered while the stump rim and grass provide unambiguous framing boundaries."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_098_E2B

```json
{
  "video_id": "synthetic_object_098",
  "edit_id": "synthetic_object_098_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_098_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Appearance",
    "operation": "Visual Appearance Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_pine_cone_s_brown_scale_tips",
    "target_description": "the pine cone's brown scale tips",
    "source_state": "The layered pine-cone scales have uniformly brown outer tips.",
    "desired_change": "Every exposed scale tip becomes frosted white."
  },
  "timing": {
    "edit_point_sec": 28,
    "effect_start_sec": 28,
    "effect_end_sec": 30,
    "evaluation_window_sec": [
      27,
      32
    ],
    "temporal_behavior": "gradual persistent change"
  },
  "instruction": "Starting at 28 seconds, change every exposed brown scale tip on the pine cone to frosted white over two seconds.",
  "expected_result": {
    "description": "Every exposed scale tip becomes frosted white.",
    "target_phrase": "frosted-white pine-cone scale tips"
  },
  "constraints": {
    "preserve": [
      "target identity",
      "target motion",
      "non-target attributes",
      "other entities",
      "scene layout",
      "camera behavior",
      "visual result of synthetic_object_098_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27,
      32
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The close view exposes many separate scale tips against the darker gaps and blurred grass."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_098_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the pine cone's brown scale tips on B independently of E1's change to the open stump surface left of the pine cone; both edit results must coexist in C."
  }
}
```

## synthetic_object_099

### synthetic_object_099_E1

```json
{
  "video_id": "synthetic_object_099",
  "edit_id": "synthetic_object_099_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Style",
    "secondary_type": "Global Media/Era Style",
    "operation": "Global Media Style Change",
    "scope": "Full Frame"
  },
  "target": {
    "target_id": "the_full_feather_display_scene",
    "target_description": "the full feather display scene",
    "source_state": "The blue-gray feather and black reflective surface have clean modern photographic rendering.",
    "desired_change": "The full scene adopts a blue-tinted silent-film look with fine grain and a soft vignette."
  },
  "timing": {
    "edit_point_sec": 10.5,
    "effect_start_sec": 10.5,
    "effect_end_sec": 12.5,
    "evaluation_window_sec": [
      9.5,
      14.5
    ],
    "temporal_behavior": "gradual persistent style change"
  },
  "instruction": "Starting at 10.5 seconds, transform the full feather display into a blue-tinted silent-film look with fine grain and a soft vignette.",
  "expected_result": {
    "description": "The full scene adopts a blue-tinted silent-film look with fine grain and a soft vignette.",
    "target_phrase": "blue-tinted silent-film feather scene"
  },
  "constraints": {
    "preserve": [
      "entity identities",
      "entity count",
      "actions",
      "spatial relationships",
      "camera trajectory",
      "non-target style regions"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      9.5,
      14.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The feather, reflection, and uninterrupted black background occupy the full frame without text or other objects."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_099_E2A

```json
{
  "video_id": "synthetic_object_099",
  "edit_id": "synthetic_object_099_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_099.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "Object Interaction",
    "operation": "Interactive Motion",
    "scope": "Core Object and Related Objects"
  },
  "target": {
    "target_id": "the_feather_s_loose_vane_edge_and_reflective_surface",
    "target_description": "the feather's loose vane edge and reflective surface",
    "source_state": "The loose vane edge stays raised slightly above the black reflective surface.",
    "desired_change": "The vane edge brushes the reflective surface twice and rebounds after each contact."
  },
  "timing": {
    "edit_point_sec": 34.5,
    "effect_start_sec": 34.5,
    "effect_end_sec": 38.5,
    "evaluation_window_sec": [
      33.5,
      40.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 34.5 seconds, make the feather's loose vane edge brush the reflective surface twice and rebound after each contact.",
  "expected_result": {
    "description": "The vane edge brushes the reflective surface twice and rebounds after each contact.",
    "target_phrase": "feather edge brushing the surface twice"
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
      33.5,
      40.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The raised vane edge, nearby reflection, pale shaft, and black surface remain visible in the close side view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_099_E2B

```json
{
  "video_id": "synthetic_object_099",
  "edit_id": "synthetic_object_099_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_099_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Progress Speed",
    "operation": "Semantic Progress Speed Change",
    "scope": "Semantic Process"
  },
  "target": {
    "target_id": "the_feather_s_post_cut_lowering_process",
    "target_description": "the feather's post-cut lowering process",
    "source_state": "After the shot change, the broad feather vane remains raised above its reflection and lowers only slightly.",
    "desired_change": "The lowering progresses faster until the broad vane lies flat beside its reflection by 30.5 seconds."
  },
  "timing": {
    "edit_point_sec": 25,
    "effect_start_sec": 25,
    "effect_end_sec": 30.5,
    "evaluation_window_sec": [
      24,
      32.5
    ],
    "temporal_behavior": "process speed change"
  },
  "instruction": "Starting at 25 seconds, accelerate the feather's lowering until its broad vane lies flat beside the reflection by 30.5 seconds.",
  "expected_result": {
    "description": "The lowering progresses faster until the broad vane lies flat beside its reflection by 30.5 seconds.",
    "target_phrase": "feather vane lying flat by 30.5 seconds"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of synthetic_object_099_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      24,
      32.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The new close shot begins at 25 seconds with a clear gap between the raised vane and its reflected outline."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "independent_but_compatible",
    "parent_edit_id": "synthetic_object_099_E1",
    "must_preserve_e1_result": true,
    "description": "This edit changes the feather's post-cut lowering process on B independently of E1's change to the full feather display scene; both edit results must coexist in C."
  }
}
```

## synthetic_object_100

### synthetic_object_100_E1

```json
{
  "video_id": "synthetic_object_100",
  "edit_id": "synthetic_object_100_E1",
  "edge": "A_to_B",
  "source_video_path": "object/object_100.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Motion",
    "secondary_type": "New/Changed Motion",
    "operation": "Motion Change",
    "scope": "Core Object"
  },
  "target": {
    "target_id": "the_white_particles_inside_the_snow_globe",
    "target_description": "the white particles inside the snow globe",
    "source_state": "Most white particles have settled around the miniature house and tree by this stage.",
    "desired_change": "The settled particles rise and begin circling clockwise around the miniature tree continuously."
  },
  "timing": {
    "edit_point_sec": 15.5,
    "effect_start_sec": 15.5,
    "effect_end_sec": 21.5,
    "evaluation_window_sec": [
      14.5,
      23.5
    ],
    "temporal_behavior": "bounded action"
  },
  "instruction": "Starting at 15.5 seconds, make the settled white particles rise and circle clockwise around the miniature tree continuously.",
  "expected_result": {
    "description": "The settled particles rise and begin circling clockwise around the miniature tree continuously.",
    "target_phrase": "white particles circling clockwise around the tree"
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
      14.5,
      23.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The clear globe, miniature tree, house, and largely settled white particles are visible in the stable full view."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "first_branch_edit",
    "must_preserve_e1_result": false,
    "description": "This is the first edit applied to A to produce B."
  }
}
```

### synthetic_object_100_E2A

```json
{
  "video_id": "synthetic_object_100",
  "edit_id": "synthetic_object_100_E2A",
  "edge": "A_to_D",
  "source_video_path": "object/object_100.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Attribute",
    "secondary_type": "Illumination",
    "operation": "Illumination Change",
    "scope": "Environment"
  },
  "target": {
    "target_id": "the_miniature_house_and_tree_inside_the_globe",
    "target_description": "the miniature house and tree inside the globe",
    "source_state": "The miniature house and tree receive only soft ambient room light.",
    "desired_change": "A warm amber light glows from the house and illuminates the lower half of the tree."
  },
  "timing": {
    "edit_point_sec": 33.5,
    "effect_start_sec": 33.5,
    "effect_end_sec": 35.5,
    "evaluation_window_sec": [
      32.5,
      37.5
    ],
    "temporal_behavior": "gradual persistent illumination change"
  },
  "instruction": "Starting at 33.5 seconds, illuminate the miniature house from within with warm amber light that reaches the tree's lower half.",
  "expected_result": {
    "description": "A warm amber light glows from the house and illuminates the lower half of the tree.",
    "target_phrase": "warm house light illuminating the tree"
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
      32.5,
      37.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The house facade, tree base, transparent sphere, and surrounding dim room are visible together."
  },
  "dependency": {
    "semantic_dependency_on_e1": false,
    "relationship_to_e1": "parallel_edit_from_a",
    "must_preserve_e1_result": false,
    "description": "This edit is applied directly to A to produce D and is independent of E1."
  }
}
```

### synthetic_object_100_E2B

```json
{
  "video_id": "synthetic_object_100",
  "edit_id": "synthetic_object_100_E2B",
  "edge": "B_to_C",
  "source_video_path": "edited/synthetic_object_100_B.mp4",
  "output_video_path": null,
  "taxonomy": {
    "primary_type": "Temporal",
    "secondary_type": "Multi-process Ordering",
    "operation": "Rotation-and-settling Process Ordering",
    "scope": "Multiple Particle Processes"
  },
  "target": {
    "target_id": "the_clockwise_particle_motion_and_settling_process_inside_the_snow_globe",
    "target_description": "the clockwise particle motion and settling process inside the snow globe",
    "source_state": "The white particles introduced by E1 circle clockwise around the miniature tree without steadily settling.",
    "desired_change": "The particles continue rotating clockwise while steadily descending until they settle at the bottom of the globe."
  },
  "timing": {
    "edit_point_sec": 28.5,
    "effect_start_sec": 28.5,
    "effect_end_sec": 35.5,
    "evaluation_window_sec": [
      27.5,
      37.5
    ],
    "temporal_behavior": "relative event reordering"
  },
  "instruction": "Starting at 28.5 seconds, make the white particles continue rotating clockwise as they steadily settle to the bottom of the snow globe.",
  "expected_result": {
    "description": "The particles continue rotating clockwise while steadily descending until they settle at the bottom of the globe.",
    "target_phrase": "clockwise particles steadily settling to the bottom"
  },
  "constraints": {
    "preserve": [
      "process semantics",
      "entity identities",
      "entity appearances",
      "spatial layout",
      "camera behavior",
      "unrelated actions",
      "visual result of synthetic_object_100_E1"
    ],
    "protected_elements": [
      "existing subtitles and captions",
      "news tickers and lower-thirds",
      "channel bugs, logos, and watermarks",
      "title cards, end cards, and subscription prompts",
      "interface overlays and animated graphics",
      "screen, packaging, printed-paper, object-label, and handheld-card text",
      "flags, emblems, and cultural or religious symbols unless explicitly targeted"
    ]
  },
  "evidence": {
    "observation_window_sec": [
      27.5,
      37.5
    ],
    "target_visible": true,
    "target_stability": "stable within the selected source window",
    "occlusion_level": "none or manageable within the selected window",
    "shot_continuity": "continuous within the selected window",
    "description": "The miniature tree, house, and globe base provide fixed references for observing simultaneous rotation and settling."
  },
  "dependency": {
    "semantic_dependency_on_e1": true,
    "relationship_to_e1": "dependent_extension",
    "parent_edit_id": "synthetic_object_100_E1",
    "must_preserve_e1_result": true,
    "description": "This edit extends the clockwise particle motion created by E1 by adding simultaneous downward settling until the particles reach the globe bottom."
  }
}
```
