# OI Survey Product Documentation
version: 0.3.0  
last_updated: 2026-04-06

This repository contains product documentation organized for clear human reading and agent (LLM/bot) retrieval.  
It is intended to act as the curated knowledge base for product and design work, while still allowing external tools to remain capture spaces.

## Structure
- [`00_Product_Foundation/`](./00_Product_Foundation/README.md) - Canonical product vision, strategy, architecture, and pillars  
- [`01_UX_Research/`](./01_UX_Research/README.md) - Canonical research synthesis, roles, workflows, and insights  
- [`02_Product_Design/`](./02_Product_Design/README.md) - Canonical product-design documentation covering principles, topology, surfaces, subsystems, services, and design bets  
- [`03_Decisions/`](./03_Decisions/README.md) - Canonical product and design decision records  
- [`sources/`](./sources/README.md) - Raw or lightly organized evidence from external tools and source artifacts  

> Note: The `bits/` folder is intentionally **not** indexed as a canonical documentation section.

## Knowledge Model
This repo now contains four working layers:
- **Canonical docs** - the promoted source of truth (`00`, `01`, `02`)
- **Decisions** - explicit promoted choices tied to evidence (`03`)
- **Sources / evidence** - raw artifacts and source packages (`sources/`)
- **Helper material** - prompts, working notes, and non-canonical support (`bits/`)

## Conventions
- **Document IDs** (`doc_id`) appear in filenames as prefixes:
  - `PFD.*` -> Product Foundation
  - `UXR.*` -> UX Research
  - `PDD.*` -> Product Design
  - `DCR.*` -> Decision Records
- Files are named `DOCID.NN_Title_Words.md` or equivalent stable forms to give both stable IDs and readable titles.
- Prefer linking by relative path to keep intra-repo links stable.

## Promotion Model
External tools such as Confluence, Figma, FigJam, Miro, spreadsheets, and recordings remain source systems. They do not become canonical truth automatically.

Promotion flow:
1. Capture or store the artifact in `sources/`
2. Synthesize the relevant insight into canonical docs
3. Record important accepted choices in `03_Decisions/`
4. Update canonical docs in `00`, `01`, and `02`

## For Agents (LLMs/Bots)
- Use section READMEs for table-of-contents discovery.
- Use `DOC_MANIFEST.yml` to resolve canonical file paths.
- Treat `sources/` as evidence storage unless a specific source package README is explicitly needed.
- Cite using `{doc_id or decision_id, path, anchor, heading}` whenever quoting canonical content.

## Quick Links
- **Product Foundation** -> [`00_Product_Foundation/README.md`](./00_Product_Foundation/README.md)  
- **UX Research** -> [`01_UX_Research/README.md`](./01_UX_Research/README.md)  
- **Product Design** -> [`02_Product_Design/README.md`](./02_Product_Design/README.md)  
- **Decisions** -> [`03_Decisions/README.md`](./03_Decisions/README.md)  
- **Sources** -> [`sources/README.md`](./sources/README.md)
