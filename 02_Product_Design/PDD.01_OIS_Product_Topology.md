---
doc_id: PDD.01
title: OI Survey Product Topology
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "topology", "product-model", "survey-operations"]
created: 2025-11-08
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
---

# PDD.01 - OI Survey Product Topology

## Purpose
This document describes the OI Survey product ecosystem and the relationship between its core surfaces, specialized subsystems, and shared services.

## Topology Overview
OI Survey is not one screen or one flat application shell. It is a **unified operational ecosystem** composed of mission-time surfaces, evidence and QC capabilities, shared services, and specialist subsystems that together support remote survey work.

| Product Element | Type | Primary Role |
| --- | --- | --- |
| **Mission Deck** | Core mission-time container | The active mission package that coordinates the primary mission-time surfaces. |
| **Mission Overview** | Core surface | Default decision surface for active mission posture, issue state, and next attention target. |
| **Systems** | Core surface | Deep operational and control surface for selected-system understanding, intervention, and recovery. |
| **Data Monitor** | Core / Evolving surface family | Package-level evidence and QC capability family, including stream-oriented and detached evidence views. |
| **Multi-Mission Context** | Core / Evolving surface | Cross-mission awareness, prioritization, and safe attention management. |
| **Online Log** | Shared service | Structured operational traceability, event capture, annotation, and reporting backbone. |
| **Hydrosens** | Specialized / Active subsystem | Specialized environmental readiness subsystem for SVP acquisition, QC, preparation, approval, and downstream distribution. |
| **Qinsy Navigation Context** | External operational dependency | Navigation view and infrastructure dependency used during survey execution. |

## Product Layers

### Mission-Time Package
The core mission-time package should help a surveyor answer:
- What is happening in the active mission right now?
- What needs attention now?
- Which system or dependency is causing concern?
- What action is safe to take now?

Mission Deck is the container for that mission-time package. Within it:
- **Mission Overview** is the primary decision surface.
- **Systems** is the deep operational and control surface.

### Evidence and QC Capability
Evidence interpretation should not be flattened into the same surface that owns all control.  
**Data Monitor** is the package-level name for the evidence and QC capability family. It can include stream viewers, QC-focused surfaces, and detached evidence views that remain mission-aware without overloading Mission Deck.

### Cross-Mission Awareness
**Multi-Mission Context** remains a core concept for broader awareness and prioritization across assigned missions. It should develop in parallel to the active mission package, using a subset of the most important mission-level signals rather than replacing the active mission model.

### Specialized Operational Subsystems
Some workflows remain deep, domain-specific, and operationally central. Hydrosens is the clearest current example. These workflows should remain connected to the OI Survey experience without being flattened into generic controls.

Hydrosens should be treated specifically as:
- a specialized environmental readiness subsystem
- not a generic `Systems` pane
- not merely an evidence-monitoring surface under `Data Monitor`
- a workflow that supports acquisition, review, preparation, approval, export, and distribution of environmental profile truth

### Shared Services
Online Log is not merely a panel. It is the traceability service that binds together automated events, user actions, manual annotations, and downstream reporting. Similar shared services may grow around state synchronization, configuration governance, and analytics.

### External Dependencies
Not every operationally essential function needs to be absorbed into OI Survey UI scope immediately. Qinsy remains a major navigation and infrastructure dependency and should be documented as such.

## Operational Relationships

| From | To | Relationship |
| --- | --- | --- |
| **Mission Overview** | **Systems** | Escalates from summary posture and issue recognition to deeper operational action. |
| **Mission Deck** | **Mission Overview / Systems** | Coordinates the active mission package without collapsing both surfaces into one flat workspace. |
| **Mission Deck** | **Data Monitor** | Launches or coordinates deeper evidence and QC review when interpretation should detach from control. |
| **Mission Deck** | **Online Log** | Produces mission-time actions, system events, and operator notes that become part of the mission narrative. |
| **Multi-Mission Context** | **Mission Deck** | Selects or shifts mission focus to an active mission package. |
| **Hydrosens** | **Mission Deck** | Supplies environmental readiness truth that affects mission confidence without collapsing the full SVP workflow into Mission Deck. |
| **Hydrosens** | **Online Log** | Produces traceable events for acquisition, QC, approval, export, and distribution. |
| **Qinsy** | **Mission Deck / survey operation** | Provides navigation context and infrastructure integration that remain operationally essential even when external. |

## Current Product Direction
- The current prototype already shows `Mission Overview` as the default overview surface inside Mission Deck.
- The current prototype already expresses `Systems` as the explicit deep operational workspace.
- Online Log is an active product/service, not only a future concept.
- Data Monitor should be treated as the package-level evidence/QC direction, even where implementation still appears through stream windows and detached evidence patterns rather than one consolidated module.
- Multi-Mission Context remains strategically important and should continue evolving in parallel with mission-level surfaces rather than being treated as a distant later-stage capability.
- Hydrosens should remain a specialized subsystem whose workflow is surfaced into mission-time experience through environmental readiness and system dependency meaning rather than through generic system ownership.

## Summary Statement
> OI Survey should be understood as a layered operational ecosystem: a mission-time container built around Mission Overview and Systems, supported by Data Monitor capabilities, shared traceability services, specialist subsystems, and explicit external dependencies that remain part of the surveyor's working reality.
