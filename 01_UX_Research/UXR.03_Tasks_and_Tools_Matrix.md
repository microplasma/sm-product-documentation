---
doc_id: UXR.03
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, tasks, tools, matrix, smp]
---

# UXR.03 – Tasks and Tools Matrix

<!--
Changes made:
1. Added standardized front-matter block.
2. Updated H1 heading to match naming convention.
3. All subsequent content remains verbatim.
-->

**Version:** 1.0  
**Date:** 2025-10-25  
**Owner:** SMP Research & Design  
**Status:** Complete Baseline (with Pain & Opportunity Overlay)

---

## 1. Purpose & Scope

This document provides a **comprehensive matrix** connecting operational tasks, tools, and user roles across the three primary survey operation types — **Geophysical**, **Geotechnical**, and **Pipeline / IMR**.

It identifies how current workflows function, where pain points occur, and highlights the **strategic opportunities for the Survey Management Platform (SMP)** to improve efficiency, safety, and collaboration.

This file serves as the factual and analytical backbone linking **User Research**, **Operational Workflows**, and **Feature Framework** design.

---

## 2. Methodology & Evidence Base

This matrix is derived from:

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations – Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`

All findings are evidence-based and consolidated from verified operational research, workshop discussions, and field observations (2023–2025).

---

## 3. Operational Task Matrix

| Operation Type                        | Role              | Task Type                 | Task Description                                   | Tool(s)                                | Pain Point                                                                        | SMP Opportunity                                                       |
| ------------------------------------- | ----------------- | ------------------------- | -------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Geophysical / Geotechnical / Pipeline | Surveyor          | Navigation                | Check current survey line                          | QINSy / Quantum                        | Switching between software for progress checks; poor line tracking visualization. | Unified line tracker with live completion % and deviation alerts.     |
| Geotechnical                          | Surveyor          | Navigation                | Position vessel for sampling (CPT / Vibrocore)     | QINSy / Quantum                        | Manual positioning requires constant verbal communication with bridge.            | Integrated deck and survey alignment view with position confirmation. |
| Geotechnical                          | Surveyor          | Navigation                | Move to next station                               | QINSy                                  | No automation of next-point navigation.                                           | Auto-next-line / waypoint trigger integrated with mission plan.       |
| Pipeline / IMR                        | Surveyor          | Navigation                | Check infrastructure & exclusion zones             | QINSy Display                          | Risk of ROV collision; manual reference check.                                    | Overlay infrastructure zones and ROV footprint in navigation map.     |
| Pipeline / IMR                        | Senior Surveyor   | Navigation                | Validate KP reference and offsets                  | QINSy / Line-plan view                 | Requires manual spreadsheet cross-check.                                          | Automated KP validation tool with offset tolerance alerts.            |
| Pipeline / IMR                        | PEC               | Navigation                | Reposition vessel when time limit reached          | QINSy / Planner                        | Requires manual tracking of permit duration.                                      | Mission time management with alert for permit expiry.                 |
| All                                   | Surveyor          | Data Logging & Validation | Verify if parameters are correctly logged          | Redgate / Folder Structure             | Manual folder check even when tool shows “green”.                                 | Auto-logging validation integrated with data status indicator.        |
| Geotechnical                          | Surveyor          | Data Logging & Validation | Set up extra log files based on client needs       | Redgate                                | Time-consuming manual folder setup.                                               | Configuration templates for client log structures.                    |
| Pipeline / IMR                        | Surveyor          | Data Logging & Validation | Check video overlays and camera node settings      | VOYIS / RVHD / QINSy                   | Manual verification; frequent mismatch between video and telemetry.               | Unified camera config and overlay verification tool.                  |
| Pipeline / IMR                        | 3.4U Inspector    | Data Logging & Validation | Inspect pipeline visually and record abnormalities | VOYIS / HD Cams                        | Requires manual logging of anomalies.                                             | Auto-log abnormality snapshots linked to position.                    |
| All                                   | Surveyor          | Data Logging & Validation | Record survey events in Online Log                 | Online Log                             | Manual event entry, risk of missing key events.                                   | Auto-event capture for line start/stop, calibration, deviation.       |
| Pipeline / IMR                        | Surveyor          | Data Logging & Validation | Add comments linked to KP reference                | Online Log                             | Requires manual cross-referencing with map.                                       | Auto-tag comments with geolocation from nav feed.                     |
| All                                   | Surveyor / Senior | Monitoring & QC           | Monitor sensor feeds (MBES, SSS, INS, CTD, video)  | SIS / Discover / Inomar / EIVA / VOYIS | Multiple UIs; high cognitive load.                                                | Multi-sensor dashboard with unified visual and QC layers.             |
| All                                   | Surveyor          | Monitoring & QC           | Check alarms and thresholds                        | Native Sensor Software                 | Inconsistent alarm hierarchies across tools.                                      | Centralized alert panel with configurable severity levels.            |
| Pipeline / IMR                        | Senior Surveyor   | Monitoring & QC           | Conduct sensor health check                        | QINSy / Diagnostics                    | Manual verification only during setup.                                            | Auto-diagnostics with periodic health reports.                        |
| All                                   | Surveyor / Senior | Communication & Handover  | Conduct shift handover (notes, discussion)         | OneNote / Verbal                       | Inconsistent documentation, data loss across shifts.                              | Integrated Handover Log linked to Online Log.                         |
| All                                   | Senior / PEC      | Reporting                 | Prepare daily report and QC summary                | Planner / Excel                        | Manual compilation from multiple data sources.                                    | Auto-generated daily report with key mission metrics.                 |
| Geotechnical                          | Surveyor          | Reporting                 | Verify log file structure before delivery          | Redgate                                | File name inconsistencies and missing logs.                                       | Automated file integrity and naming check.                            |
| Pipeline / IMR                        | Senior Surveyor   | Reporting                 | Produce MAC / calibration reports                  | Excel / Word                           | Manual image capture and parameter copy.                                          | Auto-MAC template generator with embedded images.                     |

---

## 4. Shared vs. Unique Tasks

| Category                      | Shared Across All Ops              | Unique to Specific Ops                                                  |
| ----------------------------- | ---------------------------------- | ----------------------------------------------------------------------- |
| **Navigation**                | Line selection, line tracking      | IMR: orientation & exclusion zone control; Geotech: station positioning |
| **Data Logging & Validation** | Parameter validation, folder check | IMR: video overlay validation; Geotech: event-based log setup           |
| **Monitoring & QC**           | Sensor data review, alarms         | IMR: visual QC, multi-sensor overlay; Geo: coverage completion          |
| **Communication & Handover**  | Shift exchange, log update         | —                                                                       |
| **Reporting**                 | Daily summaries, QC checks         | IMR: MAC report preparation; Geotech: client event file review          |

---

## 5. Insights Summary

**Top Pain Point Categories:**

1. **Tool Fragmentation:** Operators use 8–12 separate applications per mission.
2. **Manual Verification:** Data integrity checks require folder-level inspection.
3. **Redundant Logging:** Online Log, OneNote, and manual reports duplicate information.
4. **Lack of Standardization:** No consistent thresholds or templates across operation types.
5. **Limited Visibility:** Supervisors lack a live mission overview.

**Key SMP Opportunities:**

* Consolidate navigation, QC, and logging interfaces.
* Automate event recording and file verification.
* Standardize configuration templates across operations.
* Provide multi-role access with assist modes.
* Enable live mission progress and QC dashboards.

---

## 6. Canonical Sources

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations – Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`

---

**End of Document**
*“From task reality to design clarity – SMP’s backbone begins with operator truth.”*
