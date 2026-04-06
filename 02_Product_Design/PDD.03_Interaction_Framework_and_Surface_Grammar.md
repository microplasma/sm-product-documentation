---
doc_id: PDD.03
title: Interaction Framework and Surface Grammar
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
tags: ["design", "interaction", "ux", "surfaces"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.03_Interaction_Framework_and_Surface_Grammar.md
  - rel: related
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
---

# PDD.03 - Interaction Framework and Surface Grammar

## Purpose
This document defines the shared interaction rules that should make OI Survey feel coherent across cross-mission surfaces, mission-context surfaces, detached evidence surfaces, specialized subsystems, and shared services.

## Surface Families

| Surface Family | Role | Typical User Question |
| --- | --- | --- |
| **Cross-Mission Surfaces** | Help the surveyor prioritize attention across assigned work. | Which mission needs me now? |
| **Mission-Context Surfaces** | Support active mission supervision and intervention. | What is happening in this mission, and what is safe to do? |
| **Detached Evidence Surfaces** | Support deeper inspection, comparison, or extended watching. | What does the evidence actually show? |
| **Specialized Operational Subsystems** | Handle deep domain workflows that require their own focused model. | Is this environmental or specialist workflow valid and ready? |
| **Shared Services** | Capture or distribute cross-cutting operational truth. | What happened, who acted, and what record remains? |

## Shared Interaction Rules
- Cross-mission surfaces should summarize and prioritize, not overwhelm with raw telemetry.
- Mission-context surfaces should help operators connect state, evidence, and intervention.
- Detached evidence surfaces should privilege interpretation over broad command density.
- Shared services should remain linked to mission and system context without requiring users to reconstruct the narrative manually.
- Specialized subsystems should feel connected to OI Survey even when they maintain distinct workflows.

## Context Propagation
OI Survey should treat mission context as a first-class interaction contract.

### Rules
- The surveyor should always know which mission is currently active.
- Cross-mission surfaces should remain global.
- Mission-context surfaces should update coherently when active mission focus changes.
- Detached evidence should be able to remain mission-bound even when it is moved or opened elsewhere.
- Traceability should preserve mission linkage even when actions originate in specialized subsystems.

## Control And Evidence Relationship
The product should not force all evidence into the same surface that owns control.

### Design intent
- Keep mission-time intervention close to the evidence needed for confidence.
- Allow evidence to detach when deep inspection or monitoring would otherwise overload the main control surface.
- Make downstream impact legible before and after action.
- Preserve a stable surveyor mental model even when specialized subsystems are involved.

## Multi-Screen Guidance
Multi-screen operations remain an expected context for survey desks. However, the product should not depend on a single fixed screen map.

### Implications
- Surfaces should support multiple-screen arrangements.
- The same product model should also tolerate reduced-screen or iterative deployment contexts.
- Qinsy navigation visibility remains operationally important and should be treated as part of the working environment.

## Summary Statement
> OI Survey should behave as one coherent operating ecosystem, even when awareness, intervention, evidence, environmental workflows, and traceability are distributed across different surfaces and tools.
