---
doc_id: PDD.07
title: Design Bets, Gaps and Future Directions
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
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

It is also the canonical place to hold **promoted but unresolved architecture and interaction-model questions** that matter enough to preserve, but are not yet ready to become settled product truth or formal decision records.

## Active Design Bets
- Stronger mission-level surface clarity is an important organizing direction and should continue to be reinforced.
- Safe multi-mission operations remain strategically important and should continue to be refined rather than discarded.
- Detached evidence surfaces remain important even if their final product shape is not yet fixed.
- Operational configuration management is a necessary capability, even if its final UI boundary is still evolving.
- `Data Monitor` is a useful package-level framing for evidence and QC capabilities, even though its final product boundary is still evolving.

## Current Gaps
- Prototype coverage is strongest in acquisition-layer system experiences and does not yet represent the full OI Survey product.
- Cross-mission maturity is still evolving, but it should continue to be shaped in parallel with mission-level surface development.
- Collaboration, some role-specific workflows, and some cross-mission behaviors remain underdefined.
- Exact product boundaries between `Data Monitor`, detached evidence, and other evidence/QC capabilities still need refinement.
- Exact product boundaries between core surfaces, specialized subsystems, and shared services still need refinement.

## Active Architecture Questions
The following items are important enough to preserve canonically, but should not yet be treated as settled architecture. They exist to improve product memory and decision hygiene until stronger evidence or decisions are available.

### Topic: Mission-Time Decision Model
**Why it matters operationally**  
Surveyors and senior surveyors need more than status visibility. They need a trustworthy decision contract for whether work is safe to run, continue with risk, pause, or escalate.

**Current gap**  
The current architecture describes awareness, readiness, and consequence, but it does not yet define an explicit safe-to-run / continue-with-risk / pause / escalate model for mission-time use.

**Directionally true today**  
Mission Overview should likely be the primary place where this mission-time decision logic becomes legible.

**Unknowns / decisions not yet made**  
How many operational states should exist, who can move between them, and how strongly they should affect Mission Deck, Systems, and Online Log behavior.

**Evidence needed to close it**  
Senior surveyor validation of real degraded-operation decision patterns, acceptance thresholds, and escalation behavior.

**Priority / impact**  
High. This is central to product fit and operational trust.

### Topic: Spatial and Line-Context Integration
**Why it matters operationally**  
Survey work is often interpreted through line progress, KP/progress, deviation, and spatial context rather than through systems alone.

**Current gap**  
The docs acknowledge navigation and spatial truth, but the role of line, KP/progress, deviation, and survey-area context is still underdefined inside mission-time surfaces.

**Directionally true today**  
Mission Overview and Multi-Mission Context both need a stronger spatial/line-context layer, even if Qinsy remains an explicit external dependency.

**Unknowns / decisions not yet made**  
Which spatial signals should be shown directly in OI Survey, which should remain dependency acknowledgements, and how they should appear across mission-level and cross-mission surfaces.

**Evidence needed to close it**  
Examples of line-time supervisory workflows, navigation-heavy exception handling, and how surveyors actually combine spatial and system confidence signals.

**Priority / impact**  
High. This changes whether the product feels operationally credible or merely system-aware.

### Topic: Multi-Mission Context Mandatory Signal Set
**Why it matters operationally**  
Cross-mission work is only safe if each mission is compressed into a reliable set of signals that survive aggregation without hiding critical context.

**Current gap**  
Multi-Mission Context is directionally defined, but its mandatory information contract is still too generic for safe supervisory use.

**Directionally true today**  
It should likely recombine a subset of the most important mission-level signals rather than invent a separate cross-mission status model.

**Unknowns / decisions not yet made**  
Which fields are mandatory in the compressed mission view: mission phase, active risk, environmental readiness, key degraded dependency, unresolved note state, reason this mission needs attention now, or other signals.

**Evidence needed to close it**  
Cross-mission triage examples, senior-surveyor review of compressed mission states, and validation of what can be safely omitted.

**Priority / impact**  
High. This directly affects safe multi-mission fit.

### Topic: Cross-Surface Resolution Loop
**Why it matters operationally**  
Operational trust comes from the full loop: issue recognition, deeper diagnosis, specialist action, recorded outcome, and updated mission confidence.

**Current gap**  
The architecture defines the main surfaces, but not yet the explicit interaction pattern that links Mission Overview, Systems, Data Monitor, Hydrosens, and Online Log into one closed-loop operational flow.

**Directionally true today**  
Mission Overview should likely surface the issue, specialist or deeper surfaces should resolve it, and Online Log should preserve the accepted outcome while state flows back into mission-level surfaces.

**Unknowns / decisions not yet made**  
Which loops are generic across all issue types, which require subsystem-specific variants, and how much of the loop should be standardized in the product model.

**Evidence needed to close it**  
Concrete incident and recovery walkthroughs across systems, evidence, environmental workflows, and handover scenarios.

**Priority / impact**  
High. This is central to interaction-model coherence.

### Topic: Degraded-Operation Governance and Sign-Off
**Why it matters operationally**  
Real operations often continue under controlled degradation rather than under clean nominal conditions. Accountability for that choice matters.

**Current gap**  
The current docs define roles and permissions broadly, but do not yet define who can accept degraded conditions, how that choice is surfaced, or how it is logged and reviewed.

**Directionally true today**  
This likely needs explicit linkage between Mission Overview, role/authority rules, and Online Log.

**Unknowns / decisions not yet made**  
Who can accept degraded operation, when a supervisor or senior surveyor sign-off is required, how overrides expire, and how accepted risk should remain visible afterward.

**Evidence needed to close it**  
Senior surveyor and supervisory role validation on degraded-mode authority, exception handling, and audit expectations.

**Priority / impact**  
High. This is necessary for operational trust, governance, and defensible traceability.

## Future Directions Worth Preserving
- richer cross-mission supervision patterns
- broader evidence detachment and comparison workflows
- clearer consolidation of evidence and QC capabilities under the `Data Monitor` product direction
- deeper integration between Online Log and operational automation
- expanded environmental workflow automation through Hydrosens
- clearer product treatment of external dependencies such as Qinsy over time

## Rule For Use
Items in this document should inform research and design iteration, but should not override the more mature design truth captured in `PDD.00` through `PDD.06`.

Questions captured under `Active Architecture Questions` are promoted unresolved items. They should not be treated as settled truth until they are either:
- resolved into updates to more mature canonical docs
- promoted into a formal `DCR.*` decision record
- or supported by further evidence in `sources/`

## Summary Statement
> PDD.07 exists to preserve promising directions and acknowledged gaps without allowing unresolved ideas to silently become the default product model.
