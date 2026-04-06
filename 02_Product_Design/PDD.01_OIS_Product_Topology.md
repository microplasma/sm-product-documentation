---
doc_id: PDD.01
title: OIS Product Topology
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
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

# PDD.01 - OIS Product Topology

## Purpose
This document describes the OI Survey product ecosystem and the relationship between its core surfaces, specialized subsystems, and shared services.

## Topology Overview
OI Survey is not a single screen or a single application panel. It is an operational ecosystem that helps survey teams supervise missions, interpret evidence, intervene safely, manage critical environmental data, and preserve traceability.

| Product Element | Type | Primary Role |
| --- | --- | --- |
| **OI Survey Core / Foundational App** | Core workspace | The central mission-time operating environment for survey supervision and intervention. |
| **Multi-Mission Context** | Core surface | Cross-mission awareness, prioritization, and safe attention management. |
| **Mission Deck** | Core surface | Active mission workspace for supervision, intervention, and selected-system context. |
| **Detached Evidence Surfaces** | Core / Evolving surface family | Views where evidence must detach from control to support interpretation, comparison, or extended monitoring. |
| **Online Log** | Shared service | Structured operational traceability, event capture, annotation, and reporting backbone. |
| **Hydrosens** | Specialized / Active subsystem | SVP and environmental profile acquisition, QC, preparation, and downstream distribution. |
| **Qinsy Navigation Context** | External operational dependency | Navigation view and infrastructure dependency used during survey execution. |

## Product Layers

### OI Survey Core
The core product is the surveyor's primary workspace. It should help a surveyor answer:
- Which mission needs my attention?
- What is happening in the active mission right now?
- What system is degraded, and why?
- What action is safe to take now?

### Specialized Operational Subsystems
Some workflows remain deep, domain-specific, and operationally central. Hydrosens is the clearest current example. These workflows should remain connected to the OI Survey experience without being flattened into generic controls.

### Shared Services
Online Log is not merely a UI panel. It is the traceability service that binds together automated events, user actions, manual annotations, and downstream reporting. Similar shared services may grow around state synchronization, configuration governance, and analytics.

### External Dependencies
Not every operationally essential function needs to be absorbed into OI Survey UI scope immediately. Qinsy remains a major navigation and infrastructure dependency and should be documented as such.

## Operational Relationships

| From | To | Relationship |
| --- | --- | --- |
| **Multi-Mission Context** | **Mission Deck** | Selects or shifts operational focus to a mission. |
| **Mission Deck** | **Detached Evidence Surfaces** | Launches or coordinates deeper evidence review when dense interpretation should detach from control. |
| **Mission Deck** | **Online Log** | Produces operational actions, system events, and operator notes that become part of the mission narrative. |
| **Mission Deck** | **Hydrosens** | Consumes environmental profile readiness and distribution truth where sound velocity affects survey confidence. |
| **Hydrosens** | **Online Log** | Produces traceable events for acquisition, QC, approval, export, and distribution. |
| **Qinsy** | **Mission Deck / survey operation** | Provides navigation context and infrastructure integration that remain operationally essential even when external. |

## Current Product Direction
- The current prototype is strongest in the acquisition-layer workspace and system-specific experiences.
- Multi-mission context remains a core concept, even where prototype coverage is incomplete.
- Online Log is an active product/service, not only a future concept.
- Hydrosens should now be treated as part of the broader OI Survey ecosystem.
- Detached evidence viewing remains strategically important even if its final product shape is still evolving.

## Summary Statement
> OI Survey should be understood as a layered operational ecosystem: a core mission-time workspace supported by specialized subsystems, shared traceability services, and explicit external dependencies that remain part of the surveyor's working reality.
