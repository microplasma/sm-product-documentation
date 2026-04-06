---
doc_id: PDD.04.02
title: Mission Deck
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
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
---

# PDD.04.02 - Mission Deck

## Maturity
**Core**

## Purpose
Mission Deck is the primary mission-time workspace in OI Survey. It is where the surveyor supervises the active mission, understands selected system state, interprets key evidence, and performs safe interventions.

## Surveyor Need
During live operations the surveyor needs one dependable workspace to answer:
- What is happening in this mission right now?
- Which system or dependency is causing concern?
- What action is safe to take now?
- What evidence supports or challenges my understanding?
- What should be recorded for the next person or downstream process?

## Operational Role
Mission Deck should coordinate:
- mission posture and status
- selected-system understanding
- intervention and recovery actions
- readiness and dependency awareness
- quick launch to deeper evidence or specialized workflows
- traceable mission-time action

## Core Experience Model

| Area | Purpose |
| --- | --- |
| **Mission identity and posture** | Establishes active mission context, phase, and confidence. |
| **Selected-system context** | Focuses the surveyor on the currently relevant operational system. |
| **Intervention surfaces** | Supports actions that must be taken during mission time. |
| **Evidence and health summaries** | Provide enough understanding to act or escalate without overloading the surveyor. |
| **Links to deeper tools** | Launches detached evidence, Online Log, Hydrosens, or external navigation context when needed. |

## Relationship To Other Product Elements
- **Multi-Mission Context** chooses or shifts mission focus.
- **Detached Evidence Surfaces** support deep inspection when evidence should detach from control.
- **Online Log** captures the narrative of mission-time actions, alerts, and notes.
- **Hydrosens** informs environmental readiness where sound velocity and related profiles matter.
- **Qinsy** remains an external but essential navigation context for current operations.

## Design Requirements
- The surveyor should be able to move from awareness to intervention without reconstructing context.
- Actions should expose consequence and downstream impact clearly.
- Mission Deck should not try to fully absorb every specialized workflow.
- It should support selected-system experiences that vary by system type while still feeling like one product.
- The deck should remain effective in dense operational environments and support multiple-screen setups without depending on a rigid layout definition.

## Current Direction
Mission Deck remains one of the most important and stable concepts in OI Survey. While the exact internal structure has evolved through prototyping, the product role remains clear: it is the surveyor's central mission-time workspace.

## Summary Statement
> Mission Deck should be the surveyor's dependable mission-time cockpit: a place where state, evidence, intervention, and operational confidence come together without forcing deep specialist workflows into one flat surface.
