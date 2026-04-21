---
decision_id: DCR.0003
title: Hydrosens Placement Model
status: accepted
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["decision", "hydrosens", "svp", "product-model", "architecture"]
created: 2026-04-14
last_updated: 2026-04-14
links:
  - rel: evidence
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
  - rel: affected
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: affected
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: affected
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: affected
    href: 02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md
  - rel: affected
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
---

# DCR.0003 - Hydrosens Placement Model

## Question
Where should Hydrosens fit inside the OI Survey product architecture and experience model?

## Decision
Treat `Hydrosens` as a **specialized environmental readiness subsystem**.

Within that model:
- Hydrosens owns the full SVP workflow: acquire, inspect, clean, compare, prepare, approve, export, distribute
- Mission-time surfaces expose the **operational consequence** of environmental profile readiness
- `Mission Overview` is the primary mission-level place where environmental readiness is surfaced
- affected acoustic systems in `Systems` show `SVP` dependency state and operational consequence
- `Online Log` records Hydrosens lifecycle events
- `Multi-Mission Context` may later aggregate cross-mission environmental risk summaries, but does not own the specialist workflow

## Why
This model best matches senior surveyor operating logic.

SVP management is not a normal line-time system pane. It is a readiness-governance workflow with mission-time consequences. Surveyors need to know whether environmental profile truth is affecting the mission now, but the full Hydrosens workflow should remain a specialist subsystem rather than being flattened into `Systems` or absorbed into `Data Monitor`.

## Evidence
- `01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md`
- current Hydrosens and environmental readiness positioning in `02_Product_Design`
- prototype signals showing SVP age and dependency meaning in mission and sensor surfaces

## Implications
- Hydrosens should not be treated as a generic `Systems` pane.
- Hydrosens should not be positioned merely as an evidence-monitoring capability under `Data Monitor`.
- Mission Overview should surface environmental readiness at mission level.
- Systems should show `SVP` dependency and applied-profile meaning for affected acoustic systems.
- Online Log should capture profile acquisition, review, approval, export, and distribution events.

## Alternatives Considered
- Treat Hydrosens as a normal system pane inside `Systems`
- Treat Hydrosens as part of `Data Monitor`
- Hide Hydrosens behind mission-time dependency states without a visible subsystem identity

## Follow-Up
- Keep `Hydrosens` visible as the current product/module identity for the SVP manager.
- Refine environmental readiness as a reusable mission-level concept.
- Validate how Multi-Mission Context should summarize cross-mission environmental risk without absorbing the Hydrosens workflow.
