---
doc_id: PDD.04.05
title: Online Log and Traceability Service
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
tags: ["design", "traceability", "logging", "service"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
---

# PDD.04.05 - Online Log and Traceability Service

## Maturity
**Specialized / Active**

## Purpose
Online Log is the traceability layer of OI Survey. It replaces legacy spreadsheet-based logging with a structured, semi-automated event database that captures the operational narrative of survey and vessel activity.

## Product Role In OI Survey
Within the OI Survey ecosystem, Online Log:
- captures automated events from operational systems
- captures user actions from the Foundational App and related OI Survey workflows
- supports low-friction manual annotation by surveyors and supervisors
- provides a synchronized source of operational truth across vessels, payloads, and missions
- supports DPR generation, reporting workflows, compliance, billing support, and auditability

## Surveyor Need
Survey teams need a record they can trust for:
- handovers
- incident understanding
- defensible reporting
- client transparency
- reconstructing what happened and why

## Service Boundaries
Online Log should be understood as a shared service, not only a panel or window.

| Capability | Operational Value |
| --- | --- |
| **Automated event capture** | Reduces manual burden and improves completeness. |
| **User action traceability** | Preserves accountability for mission-time intervention. |
| **Manual annotations** | Allows contextual human judgment to remain part of the record. |
| **Cross-mission consistency** | Supports fleet-level, vessel-level, and mission-level reporting continuity. |
| **Export and reporting support** | Enables downstream DPR and related workflows. |

## Relationship To OI Survey Core
- Mission Deck and related surfaces should feed Online Log through both system-generated and user-generated events.
- Specialized subsystems such as Hydrosens should also contribute traceable workflow events.
- Online Log should remain the backbone for later automation, analytics, and multi-mission operational understanding.

## Summary Statement
> Online Log should be treated as the traceability backbone of OI Survey: a structured operational record that binds together automation, intervention, annotation, reporting, and confidence in what happened across survey work.
