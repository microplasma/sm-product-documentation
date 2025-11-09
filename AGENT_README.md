# AGENT_README
version: 0.1.0  
last_updated: 2025-11-09  

## Purpose
This file describes the structure and metadata conventions of the **SM Product Documentation** repository so both humans and automated agents (LLMs, indexing tools, chatbots) can understand and navigate it consistently.

## Repository Structure
- **00_Product_Foundation/** — Product vision, strategy, architecture, and pillars.  
- **01_UX_Research/** — Research findings, user roles, workflows, and insights.  
- **02_Product_Design/** — Information architecture, UX framework, product features, and future roadmap.  
- `README.md` — Human overview and navigation guide.  
> The folder `bits/` is intentionally excluded from indexing.

## File Naming Convention
Each file includes a **doc_id prefix**:
- `PFD.*` → Product Foundation  
- `UXR.*` → UX Research  
- `PDD.*` → Product Design  

Example:  
`PFD.03_Product_Architecture_Overview.md`  
→ `doc_id: PFD.03`, section `00_Product_Foundation`.

## Retrieval & Indexing Hints
- Agents should use the YAML manifest (`DOC_MANIFEST.yml`) to map doc_ids to file paths.  
- If front-matter exists inside a file, prefer that metadata over filename inference.  
- Chunk text by Markdown headings (`#`, `##`, `###`) with a target size of ~1,000 tokens.  
- Preserve complete tables, lists, and code blocks in single chunks.  
- Each chunk should carry metadata:
  ```json
  {
    "doc_id": "PDD.04.03",
    "path": "02_Product_Design/PDD.04.03_Stream_Viewer.md",
    "heading": "### Stream Layout",
    "last_updated": "2025-11-09"
  }
  ```

## Cross-Section Navigation
- From **Product Foundation → UX Research → Product Design**, the documentation flows from high-level vision to design implementation.  
- When unsure which file to query, start from the section README and follow linked summaries.

## Maintenance
- Keep filenames stable; they are tied to doc_ids.
- When adding new files, register them in `DOC_MANIFEST.yml`.
- If major structure changes occur, bump this file’s version.
