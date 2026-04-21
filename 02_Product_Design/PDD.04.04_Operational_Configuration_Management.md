---
doc_id: PDD.04.04
title: Operational Configuration Management
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "configuration", "validation", "governance"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.04_Operational_Configuration_Management.md
  - rel: related
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
---

# PDD.04.04 - Operational Configuration Management

## Maturity
**Core / Evolving**

## Purpose
This document defines how OI Survey should handle staged setup, validation, thresholds, lock state, and confidence in configuration truth.

## Surveyor Need
Surveyors need confidence that:
- the active setup is understood
- staged changes are visible before they are applied
- thresholds and templates are not hidden or inconsistent
- they can tell what is safe to change during live operations
- configuration truth and mission-time evidence do not silently diverge

## Product Role
Operational configuration management is broader than a single tool or modal. It is the capability that governs:
- staged vs live change
- validation and review
- thresholds and health definitions
- templates and reusable setup patterns
- lock state and authority controls
- configuration traceability

## Current Direction
The older `Configuration Manager` concept remains important, but its exact product boundary is still evolving. The capability should be documented now even if the final product surface naming changes later.

## Design Rules
- Separate staged setup from live operational state.
- Make validation legible before action, not only after failure.
- Expose what a change affects, especially where survey truth or downstream consumers may be impacted.
- Keep configuration ownership compatible with specialized subsystems such as Hydrosens.

## Summary Statement
> Operational configuration management should help survey teams trust that setup, thresholds, validation, and applied runtime state remain understandable, reviewable, and safe to change within the realities of mission execution.
