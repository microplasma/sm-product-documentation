---
doc_id: PDD.04.02
title: Mission Deck
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "mission-deck", "operations", "intervention"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.02 - Mission Deck

## Maturity
**Core**

## Purpose
Mission Deck is the primary mission-time container in OI Survey. It should hold together the active mission package while keeping different operational questions in the right internal surfaces rather than collapsing everything into one flat cockpit.

## Surveyor Need
During live operations the surveyor needs one dependable mission-time package to answer:
- What is happening in this mission right now?
- What needs attention now?
- Which system or dependency is causing concern?
- What action is safe to take now?
- What evidence supports or challenges my understanding?
- What should be recorded for the next person or downstream process?

## Operational Role
Mission Deck should coordinate:
- mission posture and issue awareness
- selected-system understanding
- intervention and recovery actions
- readiness and dependency awareness
- movement to deeper evidence, traceability, or specialist workflows
- traceable mission-time action

## Core Experience Model

Mission Deck should be understood as a mission-time container composed primarily of two internal surfaces:

| Area | Purpose |
| --- | --- |
| **Mission Overview** | The default decision surface for active mission posture, issue recognition, and next attention target. |
| **Systems** | The deep operational and control surface for selected-system action, recovery, configuration, and dependency understanding. |

This means Mission Deck should support movement from overview to deeper operational action without forcing all mission-time work into one undifferentiated screen.

## Internal Surface Roles

### Mission Overview
Mission Overview should:
- establish active mission context
- summarize posture, state, and confidence
- highlight issues, attention, and next likely action
- help the surveyor decide whether deeper system action is needed

### Environmental Readiness
Mission Overview should also be the primary place where **environmental readiness** is surfaced at mission level.

This should include, where relevant:
- current active profile age / freshness
- trust state or validity of the currently relevant environmental profile
- whether a newer cast is pending review
- whether an approved profile has been distributed or applied to affected systems
- mission consequence when profile truth is stale, missing, or questioned
- a clear path to `Open Hydrosens`

### Systems
Systems should:
- focus the surveyor on the currently relevant operational system
- support intervention and recovery
- expose consequence, dependency, and readiness meaning clearly
- support system-specific variation while still feeling like one product

For affected acoustic systems, `Systems` should:
- show `SVP` as a dependency and readiness factor
- show applied profile status where operationally meaningful
- explain the consequence of stale, missing, or questioned environmental profile truth
- provide a deep link into `Hydrosens`

`Systems` should not absorb the full Hydrosens workflow. It should express dependency meaning, not subsystem ownership.

## Relationship To Other Product Elements
- **Multi-Mission Context** chooses or shifts mission focus at cross-mission level and should progressively reflect the most important mission-level signals that Mission Overview helps define.
- **Data Monitor / Detached Evidence Surfaces** support deeper evidence review when interpretation should detach from the main mission-time surfaces.
- **Online Log** captures the narrative of mission-time actions, alerts, and notes.
- **Hydrosens** informs environmental readiness where sound velocity and related profiles matter, while retaining the specialist workflow for acquisition, review, approval, and distribution.
- **Qinsy** remains an external but essential navigation context for current operations.

## Design Requirements
- The surveyor should be able to move from awareness to intervention without reconstructing context.
- Mission Deck should not be treated as one flat cockpit where every function competes for the same interaction role.
- Mission Overview should remain the default decision surface.
- Systems should remain the deeper operational and control surface.
- Environmental readiness should be visible at mission level without forcing the full Hydrosens workflow into Mission Deck.
- Systems should express `SVP` dependency meaning for affected sensors without treating Hydrosens as a normal system pane.
- Actions should expose consequence and downstream impact clearly.
- Mission Deck should not try to fully absorb every specialist workflow.
- The package should remain effective in dense operational environments and support multiple-screen setups without depending on a rigid layout definition.

## Current Direction
Mission Deck remains one of the most important and stable concepts in OI Survey, but its internal structure is now clearer than earlier versions of the documentation suggested.

The current direction is:
- **Mission Overview** as the default primary decision surface
- **Systems** as the deep operational/control surface
- **Online Log** and **Data Monitor** as connected but distinct parts of the broader mission-time package
- **Hydrosens** as a specialized environmental readiness subsystem connected through mission-level readiness and system-level dependency meaning

This does not mean Mission Deck and Multi-Mission Context are being designed on separate timelines. The mission-level model should help shape what cross-mission aggregation needs to show and support.

## Research Implications
The senior surveyor workshop strongly supports Mission Deck as the primary home for:
- mission-time understanding and intervention
- trustworthy selected-system context
- visible consequence of start/stop/restart and related actions
- fast movement between issue recognition, deep system work, evidence, and traceability

The workshop supports one central mission-time package, but it does not require every mission-time need to live in one flat surface.

## Summary Statement
> Mission Deck should be the active mission package in OI Survey: a mission-time container that brings together Mission Overview, Systems, traceability, and connected evidence workflows without forcing all work into one overloaded surface.
