---
doc_id: PDD.02
title: Operational Information Model
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "information-model", "operations", "traceability"]
created: 2025-11-08
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.02_Operational_Information_Model.md
  - rel: related
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
  - rel: related
    href: 01_UX_Research/UXR.07_Sensor_Taxonomy.md
---

# PDD.02 - Operational Information Model

## Purpose
This document defines the product-level information model that should underpin OI Survey. It focuses on operational truth rather than software schema.

## Core Operational Objects

| Object | Meaning | Why It Matters |
| --- | --- | --- |
| **Mission** | The unit of operational intent and execution. | Organizes work, attention, traceability, and authority. |
| **Operational System** | A survey-relevant system inside a mission, including sensors, infrastructure, and supporting systems. | Lets the surveyor reason about availability, readiness, impact, and evidence. |
| **Subsystem** | A specialized capability or workflow that supports mission success but may not live inside the central workspace at all times. | Supports deep workflows such as environmental profile management. |
| **Evidence Stream** | Any live or near-live evidence source used for interpretation. | Supports QC, trust, anomaly detection, and intervention confidence. |
| **Configuration State** | The currently applied and/or staged operational setup for a mission or system. | Determines whether the observed behavior can be trusted as survey-ready. |
| **Environmental Profile** | A validated SVP or related environmental profile used to support survey accuracy. | Critical to survey quality, environmental readiness, and downstream system confidence. |
| **Alert** | A surfaced operational condition that requires awareness, validation, or action. | Helps the surveyor prioritize attention. |
| **Trace Event** | A timestamped record of a system event, user action, or manual note. | Enables handover, accountability, and reporting. |
| **Downstream Consumer** | Any system, workflow, or deliverable that depends on a system or profile remaining valid. | Makes operational consequences explicit. |

## Relationship Model
- A mission contains many operational systems and many trace events.
- A system may publish one or more evidence streams.
- A system may depend on one or more upstream inputs and may have downstream consumers.
- Configuration state may exist at mission level, system level, or subsystem level.
- Environmental profiles may influence the confidence or readiness of multiple systems.
- Alerts are tied to missions, systems, profiles, or evidence conditions.
- Trace events can be generated automatically or manually and should remain linkable to their origin.

## Information Questions The Product Must Answer

| Surveyor Question | Required Information |
| --- | --- |
| **What needs attention now?** | Mission posture, alerts, degraded systems, recent operational changes. |
| **Can I trust this system?** | Availability, readiness, dependencies, last known evidence, and recent interventions. |
| **What changed?** | Trace events, state changes, applied configuration, profile updates, and manual notes. |
| **What happens if I act?** | Downstream consumers, impact, lock state, and system relationships. |
| **Is the environment still survey-ready?** | Profile age, validation status, source provenance, export/distribution status. |

## Operational Modeling Rules
- Do not flatten all systems into one generic sensor concept.
- Represent control-oriented systems differently from measurement-oriented systems when their operator meaning differs.
- Treat environmental profile truth as a first-class operational object.
- Keep traceability connected to operational meaning, not only to technical events.
- Model external dependencies such as Qinsy explicitly when the surveyor relies on them to understand mission state.

## Summary Statement
> OI Survey should organize information around the operational truths a surveyor must trust: mission state, system state, evidence, configuration, environmental validity, downstream impact, and traceable events.
