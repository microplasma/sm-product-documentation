---
decision_id: DCR.0002
title: Product Surface Model
status: accepted
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["decision", "product-model", "naming", "architecture"]
created: 2026-04-13
last_updated: 2026-04-13
links:
  - rel: evidence
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: evidence
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: evidence
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
  - rel: affected
    href: 00_Product_Foundation/PFD.01_Product_Vision.md
  - rel: affected
    href: 00_Product_Foundation/PFD.03_Product_Architecture_Overview.md
  - rel: affected
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
---

# DCR.0002 - Product Surface Model

## Question
How should OI Survey's near-term product structure be described so the documentation reflects the current direction without collapsing the product into one flat application model?

## Decision
Use a **product surface model** in which OI Survey is described first as a **unified operational ecosystem**, and structurally as a set of connected operational surfaces, shared services, and specialist subsystems.

Within that model:
- `Mission Deck` is the mission-time container/package element
- `Mission Overview` is the default primary decision surface
- `Systems` is the deep operational/control surface
- `Data Monitor` is the package-level evidence/QC capability family
- `Multi-Mission Context` remains a parallel cross-mission awareness surface
- `Online Log` remains the traceability backbone and shared service

## Why
This model reflects the current product direction more accurately than describing OI Survey as one flat application shell or reducing it to a mere software package.

It also matches observed prototype direction more closely:
- Mission Overview already exists as the default overview surface inside Mission Deck
- Systems already exists as the deeper operational workspace
- Online Log is already first-class
- Multi-Mission Context remains distinct
- Mission Overview and Multi-Mission Context are being shaped together as related layers of the same attention model
- evidence and QC capabilities exist in multiple forms that are better grouped under a package-level direction than forced into one early rigid module

## Evidence
- `02_Product_Design/PDD.01_OIS_Product_Topology.md`
- `02_Product_Design/PDD.04.02_Mission_Deck.md`
- `02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md`
- current `sm-poseidon` prototype naming and workspace structure

## Implications
- Product and design documentation should describe OI Survey as a unified operational ecosystem.
- Mission Deck should no longer be described as one flat cockpit.
- Mission Overview should be treated as the default mission-time decision surface.
- Systems should be treated as the deep operational/control surface.
- Data Monitor can be used as a package-level capability term without forcing Detached Evidence Surfaces to be renamed or discarded.
- Multi-Mission Context remains strategically important and should continue evolving in parallel with mission-level surfaces rather than being treated as a distant later-stage capability.

## Alternatives Considered
- Keep describing OI Survey as a unified application.
- Treat Multi-Mission Context as the primary default organizing model.
- Rename Detached Evidence Surfaces directly to Data Monitor.

## Follow-Up
- Align Product Foundation and Product Design language to this model.
- Preserve older terminology only where needed for traceability.
- Keep validating the product boundary of Data Monitor as evidence and QC capabilities mature.
