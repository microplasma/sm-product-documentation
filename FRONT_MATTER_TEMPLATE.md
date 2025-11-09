# FRONT_MATTER_TEMPLATE
version: 0.1.0  
last_updated: 2025-11-09  

Add this YAML block at the top of each Markdown file (recommended).  
It ensures consistent metadata for both humans and agents.

```yaml
---
doc_id: PDD.04.03
title: Stream Viewer
version: 0.1.0
status: draft               # draft|review|approved|deprecated
visibility: internal         # internal|public
owners: ["@microplasma"]
tags: ["design", "feature"]
created: 2025-11-09
last_updated: 2025-11-09
review_after: 2026-02-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.03_Stream_Viewer.md
---
```

### Field Guide
| Field | Description |
|--------|-------------|
| `doc_id` | Stable identifier (matches filename prefix). |
| `title` | Human-readable document name. |
| `version` | Increment when content meaningfully changes. |
| `status` | Workflow status (draft → review → approved). |
| `visibility` | Controls whether it’s shared externally. |
| `owners` | Responsible maintainers. |
| `tags` | Quick topical categorization. |
| `review_after` | Optional date to trigger updates. |
| `links` | Relationships to section, source, or related docs. |

### Agent Rules
- Prefer explicit front matter over inferred metadata.
- Use `doc_id` as the canonical lookup key.
- Resolve relative paths via `DOC_MANIFEST.yml`.
