---
doc_id: PDD.04.06
title: Hydrosens Environmental Profile Management
version: 0.1.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "hydrosens", "svp", "environmental-profiles"]
created: 2026-04-06
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.06 - Hydrosens Environmental Profile Management

## Maturity
**Specialized / Active**

## Purpose
Hydrosens is the OI Survey subsystem responsible for the lifecycle of sound velocity profiles and related environmental data. It replaces EIVA SVP Manager in Ocean Infinity operations and should be treated as a first-class part of the broader survey experience.

Hydrosens should be treated specifically as a **specialized environmental readiness subsystem**, not as a normal mission-time `Systems` pane and not merely as an evidence-monitoring surface under `Data Monitor`.

## Surveyor Need
Survey teams need a trustworthy way to:
- acquire environmental profile data
- review and clean profiles
- prepare survey-ready SVPs
- understand profile provenance and quality
- distribute approved profiles to downstream systems with confidence

## Operational Scope
Hydrosens covers:
- acquisition from connected hydrographic and environmental sensors
- logging of raw and processed profile data
- profile review, cleaning, comparison, resampling, extension, and preparation
- approval of survey-ready profiles
- export and distribution to downstream survey and navigation systems
- future automation and remote-control potential through extensible interfaces

## Why It Matters To OI Survey
Sound velocity and environmental profile truth are not peripheral concerns. They directly affect:
- survey accuracy
- system confidence
- readiness decisions
- downstream deliverable confidence
- the surveyor's trust in the mission setup

## Relationship To The Broader Experience
- **Mission Deck** should expose the operational consequence of profile readiness without trying to absorb the full Hydrosens workflow.
- **Mission Overview** should be the primary mission-level place where environmental readiness is surfaced.
- **Systems** should show `SVP` dependency meaning for affected acoustic systems without treating Hydrosens as a generic system pane.
- **Online Log** should capture profile acquisition, review, approval, export, and distribution events.
- **Operational Configuration Management** should remain compatible with Hydrosens where thresholds, profiles, or distribution choices affect mission truth.

## Placement In The Experience
The preferred product placement is:
- **primary home:** specialized subsystem
- **mission-time presence:** environmental readiness summary and consequence in Mission Overview
- **system-level presence:** `SVP` dependency and applied-profile meaning in affected acoustic systems
- **traceability presence:** lifecycle events in Online Log
- **cross-mission presence:** future aggregated environmental risk summaries in Multi-Mission Context

Hydrosens should therefore not be treated as:
- a standard `Systems` inventory item
- the default place for line-time intervention
- a capability absorbed into `Data Monitor`, except where observational or comparison views overlap

## Product Direction
Hydrosens should be documented under its current product/module identity while also representing the longer-lived capability of environmental profile management.

## Research Implications
The senior surveyor workshop adds strong support for keeping environmental and geodetic readiness visible in the broader OI Survey model. The workshop material repeatedly points to the need for:
- trustworthy SVP and reference-data preparation
- explicit visibility of profile readiness and validity
- operational continuity between specialist profile workflows and mission-time confidence

This reinforces Hydrosens as a specialized but connected subsystem rather than a hidden utility.

## Summary Statement
> Hydrosens should remain a distinct but fully connected part of OI Survey: the specialized environmental readiness subsystem that turns raw environmental acquisition into validated, survey-ready profile truth that can be distributed and trusted downstream.
