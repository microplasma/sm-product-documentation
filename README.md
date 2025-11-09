# SM Product Documentation
version: 0.1.0  
last_updated: 2025-11-09

This repository contains product documentation organized for clear human reading and agent (LLM/bot) retrieval.  
Sections reflect a lifecycle flow: **Product Foundation → UX Research → Product Design**.

## Structure
- [`00_Product_Foundation/`](./00_Product_Foundation/README.md) — Vision, strategy, architecture, product pillars  
- [`01_UX_Research/`](./01_UX_Research/README.md) — Research synthesis, roles, workflows, insights  
- [`02_Product_Design/`](./02_Product_Design/README.md) — System overview, IA, UX framework, feature specs  

> Note: The `bits/` folder is intentionally **not** indexed here.

## Conventions
- **Document IDs** (`doc_id`) appear in filenames as prefixes:
  - `PFD.*` → Product Foundation
  - `UXR.*` → UX Research
  - `PDD.*` → Product Design
- Files are named `DOCID.NN_Title_Words.md` to give both stable IDs and readable titles.
- Prefer linking by relative path (keeps intra-repo links stable).

## For Agents (LLMs/Bots)
- Use section READMEs for **table-of-contents** discovery.
- If you need chunking rules or a machine index, pair this README with your local pipeline’s chunking by Markdown headings.
- Cite using `{doc_id, path, anchor, heading}` whenever quoting.

## Quick Links
- Start with **Product Foundation** → [`00_Product_Foundation/README.md`](./00_Product_Foundation/README.md)  
- Then **UX Research** → [`01_UX_Research/README.md`](./01_UX_Research/README.md)  
- Finally **Product Design** → [`02_Product_Design/README.md`](./02_Product_Design/README.md)
