---
doc_id: PDD.04.01
title: Multi-Mission Context
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
tags: ["design", "multi-mission", "awareness", "prioritization"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
---

# PDD.04.01 - Multi-Mission Context

## Maturity
**Core**

## Purpose
Multi-Mission Context is the cross-mission awareness surface for OI Survey. It gives surveyors a real-time view of the missions assigned to them and helps them decide where to focus attention.

## Surveyor Need
A surveyor may be responsible for more than one mission or operational thread. They need a way to:
- understand overall mission posture quickly
- spot which mission is degrading
- shift focus without losing orientation
- maintain safe workload awareness across assigned work

## Operational Role
This surface is not for detailed system control. Its role is to support:
- prioritization
- focus switching
- mission posture recognition
- escalation awareness
- safe multi-mission operations where validated

## Information To Show

| Information | Why It Matters |
| --- | --- |
| **Mission identity and assignment** | Confirms what is under the surveyor's responsibility. |
| **Mission posture** | Shows whether the mission is nominal, degraded, waiting, or at risk. |
| **Recent critical changes** | Helps the surveyor understand why attention is needed now. |
| **Unread or unresolved operational issues** | Prevents hidden problems from being lost in mission switching. |
| **Readiness and confidence summaries** | Supports fast judgment without opening every mission. |
| **Time relevance** | Indicates how fresh the displayed understanding is. |

## Interaction Expectations
- Selecting a mission should shift active operational focus coherently.
- Mission switching should be fast and deliberate, not friction-heavy.
- The active mission should remain clearly indicated.
- The surface should help a surveyor understand relative urgency across missions.
- The surface should not try to replace the detailed evidence and action model of Mission Deck.

## Relationship To Other Surfaces
- **Mission Deck**: active mission-time workspace once focus is selected.
- **Online Log**: supports cross-mission awareness of what changed.
- **Detached Evidence Surfaces**: may remain open for a mission even when the surveyor is reviewing another mission at summary level.

## Current Direction
The former `Triage Hub` concept is now more accurately expressed as Multi-Mission Context. The concept remains core, but the exact UI treatment can evolve.

## Summary Statement
> Multi-Mission Context should help surveyors manage attention safely across missions by showing which mission matters now, why it matters, and how focus can shift without losing situational understanding.
