# AGENT_README
version: 0.2.0  
last_updated: 2026-04-06  

## Purpose
This file describes the structure and metadata conventions of the **SM Product Documentation** repository so both humans and automated agents (LLMs, indexing tools, chatbots) can understand and navigate it consistently.

## Repository Structure
- **00_Product_Foundation/** - Product vision, strategy, architecture, and pillars.  
- **01_UX_Research/** - Research findings, user roles, workflows, and insights.  
- **02_Product_Design/** - Layered product-design documentation covering principles, topology, operational surfaces, subsystems, shared services, and future directions.  
- `README.md` - Human overview and navigation guide.  
> The folder `bits/` is intentionally excluded from indexing.

## File Naming Convention
Each file includes a **doc_id prefix**:
- `PFD.*` -> Product Foundation  
- `UXR.*` -> UX Research  
- `PDD.*` -> Product Design  

Example:  
`PDD.04.05_Online_Log_and_Traceability_Service.md`  
-> `doc_id: PDD.04.05`, section `02_Product_Design`.

## Retrieval and Indexing Hints
- Agents should use the YAML manifest (`DOC_MANIFEST.yml`) to map doc_ids to file paths.  
- If front-matter exists inside a file, prefer that metadata over filename inference.  
- Chunk text by Markdown headings (`#`, `##`, `###`) with a target size of ~1,000 tokens.  
- Preserve complete tables, lists, and code blocks in single chunks.  
- Each chunk should carry metadata:
  ```json
  {
    "doc_id": "PDD.04.05",
    "path": "02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md",
    "heading": "## Product Role In OI Survey",
    "last_updated": "2026-04-06"
  }
  ```

## Cross-Section Navigation
- From **Product Foundation -> UX Research -> Product Design**, the documentation flows from high-level vision to research grounding to product-shape definition.  
- When unsure which file to query, start from the section README and follow linked summaries.
- In `02_Product_Design`, read `PDD.00` and `PDD.01` first for product shape, then `PDD.03` for interaction rules, then `PDD.04.*` for surface or subsystem specifics.

## Maintenance
- Keep filenames stable once published; if renamed, update relative links and `DOC_MANIFEST.yml` together.
- When adding new files, register them in `DOC_MANIFEST.yml`.
- If major structure changes occur, bump this file's version.
