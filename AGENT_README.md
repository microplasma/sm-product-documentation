# AGENT_README
version: 0.3.0  
last_updated: 2026-04-06  

## Purpose
This file describes the structure and metadata conventions of the **OI Survey Product Documentation** repository so both humans and automated agents (LLMs, indexing tools, chatbots) can understand and navigate it consistently.

## Repository Structure
- **00_Product_Foundation/** - Canonical product vision, strategy, architecture, and pillars.  
- **01_UX_Research/** - Canonical research synthesis, roles, workflows, and insights.  
- **02_Product_Design/** - Canonical product-design documentation covering principles, topology, operational surfaces, subsystems, shared services, and future directions.  
- **03_Decisions/** - Canonical decision records for promoted product/design choices.  
- **sources/** - Source artifacts and evidence packages from external tools.  
- `README.md` - Human overview and navigation guide.  
> The folder `bits/` is intentionally excluded from the canonical indexed reading path.

## File Naming Convention
Each file includes a stable identifier where possible:
- `PFD.*` -> Product Foundation  
- `UXR.*` -> UX Research  
- `PDD.*` -> Product Design  
- `DCR.*` -> Decision Records  

Example:  
`PDD.04.05_Online_Log_and_Traceability_Service.md`  
-> `doc_id: PDD.04.05`, section `02_Product_Design`.

## Retrieval and Indexing Hints
- Agents should use the YAML manifest (`DOC_MANIFEST.yml`) to map canonical doc_ids and decision_ids to file paths.  
- If front matter exists inside a file, prefer that metadata over filename inference.  
- Chunk text by Markdown headings (`#`, `##`, `###`) with a target size of ~1,000 tokens.  
- Preserve complete tables, lists, and code blocks in single chunks.  
- Treat `sources/` as evidence by default, not canonical truth, unless a user explicitly asks for the source-package context.

## Cross-Section Navigation
- The canonical product flow remains **Product Foundation -> UX Research -> Product Design**.  
- `03_Decisions` records accepted choices that affect canonical docs.  
- `sources/` stores the raw or lightly organized material that may later be promoted into canonical docs or decisions.
- When unsure which canonical file to query, start from the section README and follow linked summaries.

## Maintenance
- Keep filenames stable once published; if renamed, update relative links and `DOC_MANIFEST.yml` together.
- When adding canonical docs or decision records, register them in `DOC_MANIFEST.yml`.
- When adding source artifacts, prefer adding them inside a source package folder with its own README.
- If major structure changes occur, bump this file's version.
