# 03 Decisions
version: 0.1.0  
last_updated: 2026-04-06

This section stores canonical product and design decisions after they have been promoted from research, workshops, design work, or other evidence sources.

## Purpose
Decision records exist to make important choices explicit, traceable, and reviewable.

They should capture:
- what question was being answered
- what was decided
- why that decision was made
- which evidence informed it
- which canonical docs are affected

## Status Model
- `draft` - captured but not ready for wider review
- `proposed` - formed enough for decision review
- `accepted` - canonical decision for the repo
- `superseded` - replaced by a later decision
- `rejected` - explicitly considered but not adopted

## Rules
- Decisions should link to evidence in `sources/` and/or promoted research docs.
- Decisions should link to affected canonical docs in `00_Product_Foundation`, `01_UX_Research`, and `02_Product_Design`.
- Decisions should be concise and product-oriented, not technical ADRs unless the decision is genuinely technical in nature.
- A decision record is not a meeting note; it is the promoted statement of an actual choice.

## Files
- **DECISION_TEMPLATE.md**  
  *Template for new decision records.*

- **DCR.0001 - Multi-Mission Context Naming**  
  *Example record showing how to capture a naming and product-model decision.*

- **DCR.0002 - Product Surface Model**  
  *Locks the current package/surface framing for Mission Deck, Mission Overview, Systems, Data Monitor, and Multi-Mission Context.*

- **DCR.0003 - Hydrosens Placement Model**  
  *Locks Hydrosens as a specialized environmental readiness subsystem rather than a normal system pane or a Data Monitor sub-surface.*
