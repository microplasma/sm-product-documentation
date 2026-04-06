# 00 - Product Foundation
version: 0.2.0  
last_updated: 2026-04-06

This section defines the **why** and **what** of OIS: product vision, strategy, conceptual architecture, and guiding pillars.

These documents are intended to describe the target future-state product direction. They should stay strategic and conceptually clear, while avoiding unnecessary implementation detail or overclaiming where validation is still in progress.

## Files (PFD.*)
- **PFD.01 - Product Vision**  
  [`PFD.01_Product_Vision.md`](./PFD.01_Product_Vision.md)  
  *North star and outcomes the product seeks to enable.*

- **PFD.02 - Product Strategy Overview**  
  [`PFD.02_Product_Strategy_Overview.md`](./PFD.02_Product_Strategy_Overview.md)  
  *Strategic approach, objectives, success metrics, and horizons.*

- **PFD.03 - Product Architecture Overview**  
  [`PFD.03_Product_Architecture_Overview.md`](./PFD.03_Product_Architecture_Overview.md)  
  *Conceptual system structure, interactions, and design-level constraints.*

- **PFD.04 - Product Pillars**  
  [`PFD.04_Product_Pillars.md`](./PFD.04_Product_Pillars.md)  
  *Principles that anchor decisions and trade-offs.*

## Navigation
- Next: **UX Research** -> [`../01_UX_Research/README.md`](../01_UX_Research/README.md)  
- Downstream: **Product Design** -> [`../02_Product_Design/README.md`](../02_Product_Design/README.md)

## Agent Hints
- `doc_id` pattern: `PFD.<NN>`  
- Chunk by `#`, `##`, `###`. Keep lists intact; prefer ~1k tokens per chunk.  
- When answering product-intent or "why" questions, prioritize `PFD.01` and `PFD.02`.  
- When answering conceptual system or boundary questions, prioritize `PFD.03`.  
- Treat these files as future-state product framing, not as implementation or integration source-of-truth.
