---
doc_id: PDD.07
title: Design Bets, Gaps and Future Directions
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
tags: ["design", "future", "gaps", "bets"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.07_Design_Bets_Gaps_and_Future_Directions.md
---

# PDD.07 - Design Bets, Gaps and Future Directions

## Maturity
**Draft / Emerging**

## Purpose
This document preserves unresolved product questions, active design bets, prototype gaps, and future-facing concepts without confusing them with core product truth.

## Active Design Bets
- Safe multi-mission operations remain strategically important and should continue to be refined rather than discarded.
- Detached evidence surfaces remain important even if their final product shape is not yet fixed.
- Operational configuration management is a necessary capability, even if its final UI boundary is still evolving.

## Current Gaps
- Prototype coverage is strongest in acquisition-layer system experiences and does not yet represent the full OI Survey product.
- Collaboration, some role-specific workflows, and some cross-mission behaviors remain underdefined.
- Exact product boundaries between core surfaces, specialized subsystems, and shared services still need refinement.

## Future Directions Worth Preserving
- richer cross-mission supervision patterns
- broader evidence detachment and comparison workflows
- deeper integration between Online Log and operational automation
- expanded environmental workflow automation through Hydrosens
- clearer product treatment of external dependencies such as Qinsy over time

## Rule For Use
Items in this document should inform research and design iteration, but should not override the more mature design truth captured in `PDD.00` through `PDD.06`.

## Summary Statement
> PDD.07 exists to preserve promising directions and acknowledged gaps without allowing unresolved ideas to silently become the default product model.
