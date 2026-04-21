---
doc_id: PDD.05
title: Operational State and Configuration Model
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "state", "configuration", "operations"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
  - rel: related
    href: 02_Product_Design/PDD.04.04_Operational_Configuration_Management.md
---

# PDD.05 - Operational State and Configuration Model

## Maturity
**Core / Evolving**

## Purpose
This document defines the key states that matter across mission execution, configuration management, evidence interpretation, and environmental profile distribution.

## Mission Lifecycle States
- **Preparation**: setup, validation, calibration, and readiness work before live acquisition.
- **Active Acquisition**: mission-time operation, evidence interpretation, and live intervention.
- **Degraded Operation**: survey continues or pauses under degraded confidence, dependencies, or evidence quality.
- **Review / Handover**: mission narrative, state understanding, and follow-on work are consolidated.

## Configuration States
- **Baseline**: known configuration starting point.
- **Staged**: proposed but not yet applied.
- **Applied**: accepted as the active operational setup.
- **Locked**: prevented from change due to authority or operational safety.
- **Divergent**: observed runtime behavior no longer matches expected configuration truth.

## Evidence States
- **Nominal**: evidence supports current understanding.
- **Watch**: evidence suggests closer attention is needed.
- **Invalidating**: evidence undermines confidence in readiness or quality.
- **Detached Review**: evidence requires deeper inspection outside the main control surface.

## Environmental Profile States
- **Acquired**: profile captured from source systems.
- **Prepared**: reviewed and processed but not yet approved.
- **Survey-Ready**: accepted for operational use.
- **Distributed**: exported or delivered to downstream systems.
- **Stale / Questioned**: no longer trusted without revalidation.

Environmental profile state should be treated as a **first-class operational state**, not merely as a background dependency. It should affect:
- mission-level environmental readiness
- affected-system readiness and dependency state
- traceability and handover confidence

## Environmental Readiness Expectations
The product should make environmental readiness legible at mission level by answering:
- how fresh the currently relevant profile is
- whether the active profile is trusted
- whether a newer cast is pending review
- whether an approved profile has been distributed or applied to affected systems
- what operational consequence follows if profile truth is stale, missing, or questioned

## Traceability Expectations
Every significant shift between these states should be traceable through Online Log or equivalent trace events, with enough context to support handover, reporting, and audit.

## Summary Statement
> OI Survey should make operational state visible across missions, systems, evidence, configuration, and environmental profiles so that survey teams can tell not only what is happening, but what is trustworthy right now.
