---
doc_id: PDD.06
title: Roles, Authority and Operational Modes
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "roles", "authority", "operations"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.06_Roles_Authority_and_Operational_Modes.md
  - rel: related
    href: 01_UX_Research/UXR.01_Roles_and_Responsibilities.md
  - rel: related
    href: 01_UX_Research/UXR.05_Role-Based_Insights.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.06 - Roles, Authority and Operational Modes

## Purpose
This document defines who acts, supervises, validates, annotates, and configures across the OI Survey ecosystem.

## Roles

| Role | Primary Product Relationship |
| --- | --- |
| **Survey Operator** | Uses Multi-Mission Context and Mission Deck to supervise active operations and intervene during mission time. |
| **Senior Surveyor** | Validates setup, supports problem-solving, interprets quality implications, and often owns higher-consequence configuration or environmental decisions. |
| **PEC** | Needs operational awareness, coordination context, and confidence in the status narrative rather than direct low-level control. |
| **Data Processor** | Relies on traceability, completeness, and downstream clarity for validation and reporting work. |
| **IT / Support** | Supports platform reliability, infrastructure confidence, and system integrity. |

## Surface-Level Authority Model

| Product Element | Primary Actors | Typical Authority |
| --- | --- | --- |
| **Multi-Mission Context** | Operator, Senior, PEC | Awareness, prioritization, mission focus selection. |
| **Mission Deck** | Operator, Senior | Mission-time supervision and intervention. |
| **Detached Evidence Surfaces** | Operator, Senior, Data Processor | Interpretation and monitoring, usually with limited direct control. |
| **Operational Configuration Management** | Senior, Operator, IT | Staged changes, thresholds, validation, locks, and templates depending on authority. |
| **Online Log** | Operator, Senior, PEC, Data Processor | Annotation, review, filtering, and operational reconstruction. |
| **Hydrosens** | Senior, Operator, specialist users | Profile acquisition, QC, approval, and distribution depending on role and authority. |

## Operational Modes
- **Preparation**: setup and validation dominate.
- **Active Acquisition**: intervention authority and runtime clarity matter most.
- **Degraded Mode**: escalation, interpretation, and consequence management become more important.
- **Review / Handover**: narrative quality, validation, and completeness matter most.

## Design Requirements
- The product should make authority boundaries visible.
- The product should support collaboration without erasing accountability.
- The same role may need different levels of access across missions or workflows.
- Traceability should preserve both system events and human judgment.

## Research Implications
The senior surveyor workshop sharpens the importance of:
- visible lock state and permission boundaries during live work
- safe multi-user participation without overlapping interference
- clear accountability for configuration, intervention, and annotation

This supports keeping authority, permission, and collaboration concerns explicit in the product model rather than treating them as background admin behavior.

## Summary Statement
> OI Survey should make roles and authority legible at the moment of work so that survey teams can collaborate safely without losing clarity about who can act, who can validate, and who remains accountable.
