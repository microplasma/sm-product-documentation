# FRONT_MATTER_TEMPLATE
version: 0.3.0  
last_updated: 2026-04-06  

Add this YAML block at the top of each Markdown file (recommended).  
It ensures consistent metadata for both humans and agents.

```yaml
---
doc_id: PDD.04.03
title: Detached Evidence Surfaces
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
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
---
```

### Field Guide
| Field | Description |
|--------|-------------|
| `doc_id` | Stable identifier (matches filename prefix). |
| `title` | Human-readable document name. |
| `version` | Increment when content meaningfully changes. |
| `status` | Workflow status (draft -> review -> approved). |
| `visibility` | Controls whether it's shared externally. |
| `owners` | Responsible maintainers. |
| `tags` | Quick topical categorization. |
| `review_after` | Optional date to trigger updates. |
| `links` | Relationships to section, source, or related docs. |

### Optional Knowledge-Base Fields
Use these when a document benefits from richer curation metadata.

| Field | Description |
|--------|-------------|
| `maturity` | Optional stability label such as Core, Core / Evolving, Specialized / Active, or Draft / Emerging. |
| `source_refs` | Optional links or IDs pointing to source artifacts or evidence packages. |
| `affected_by_decisions` | Optional list of decision records that materially shape this doc. |
| `supersedes` | Optional reference to an older doc or decision this content replaces. |
| `superseded_by` | Optional reference to the newer canonical item that replaced this one. |

### Agent Rules
- Prefer explicit front matter over inferred metadata.
- Use `doc_id` or `decision_id` as the canonical lookup key when present.
- Resolve relative paths via `DOC_MANIFEST.yml` for canonical docs and decisions.
- Treat optional knowledge-base fields as enrichment, not as mandatory schema for every file.
