---
doc_id: PDD.04.03
title: Detached Evidence Surfaces
version: 0.2.0
status: draft
visibility: internal
owners: ["design@survey-platform.io"]
tags: ["design", "evidence", "qc", "monitoring"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.03 - Detached Evidence Surfaces

## Maturity
**Core / Evolving**

## Purpose
Detached Evidence Surfaces describe the family of product views used when evidence needs to be interpreted outside the immediate control surface.

## Surveyor Need
Some forms of evidence are easier to understand when they are not compressed into the same surface that owns mission-time control. Surveyors may need to:
- monitor imagery or datagrams continuously
- compare multiple evidence feeds side by side
- keep a camera or sonar view visible while working elsewhere
- apply optional QC overlays without cluttering the main control surface

## Capability Scope
This family may include:
- acoustic data views
- datagram or QC views
- vessel camera feeds
- ROV camera feeds
- evidence comparison surfaces
- optional overlay-enabled monitoring views

## Product Direction
The older `Stream Viewer` concept is still useful, but should now be treated as one possible product manifestation of the broader detached evidence capability.

## Design Rules
- Detached evidence should remain mission-context aware.
- The product should make it clear whether a surface is observational only or linked to operational consequence.
- QC overlays should support interpretation, not become decorative overlays without operational meaning.
- Detached evidence should complement Mission Deck, not compete with it as the primary operating surface.

## Research Implications
The senior surveyor workshop adds strong evidence for this surface family by repeatedly pointing to:
- live stream viewing across sensor types
- side-by-side evidence comparison
- camera and imagery visibility outside the main control workflow
- QC overlays and short-history/trend support for interpretation

This supports keeping detached evidence as a durable capability even if the exact product manifestation remains flexible.

## Summary Statement
> Detached Evidence Surfaces should help surveyors inspect, compare, and watch evidence in the way the mission demands, without forcing every evidence-heavy workflow back into the central mission-time control surface.
