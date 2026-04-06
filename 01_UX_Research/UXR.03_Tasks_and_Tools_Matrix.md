---
doc_id: UXR.03
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, tasks, tools, matrix, ois]
---

# UXR.03 - Tasks and Tools Matrix

<!--
Changes made:
1. Added standardized front-matter block.
2. Updated H1 heading to match naming convention.
3. Expanded the matrix to include OBN and vehicle-assisted geophysical workflows.
4. Preserved the original evidence-based structure while marking the expanded operation types as a working model pending direct SME confirmation.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Complete Baseline (with Pain & Opportunity Overlay)

---

## 1. Purpose & Scope

This document provides a **comprehensive matrix** connecting operational tasks, tools, and user roles across the primary survey operation types in scope - **Geophysical**, **Geotechnical**, **Pipeline / IMR**, **OBN**, and vehicle-assisted geophysical modes such as **ROV**, **ROTV**, and **AUV** survey work.

It identifies how current workflows function, where pain points occur, and highlights the **strategic opportunities for the OI Survey (OIS)** to improve efficiency, safety, and collaboration.

This file serves as the factual and analytical backbone linking **User Research**, **Operational Workflows**, and **Feature Framework** design.

This version expands the matrix to also cover **OBN** and vehicle-assisted geophysical modes such as **ROV**, **ROTV**, and **AUV** survey work.

---

## 2. Methodology & Evidence Base

This matrix is derived from:

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`

All findings are evidence-based and consolidated from verified operational research, workshop discussions, and field observations (2023-2025).

For OBN, ROV-, ROTV-, and AUV-assisted workflows, the added rows below are grounded in the internal workflow synthesis plus external operational references used to expand `UXR.02`. They should be treated as a validated working model for product design, pending direct SME confirmation for contractor- or vessel-specific variations.

---

## 3. Operational Task Matrix

| Operation Type | Role | Task Type | Task Description | Tool(s) | Pain Point | OIS Opportunity |
| --- | --- | --- | --- | --- | --- | --- |
| Geophysical / Geotechnical / Pipeline | Surveyor | Navigation | Check current survey line | QINSy / Quantum | Switching between software for progress checks; poor line tracking visualization. | Unified line tracker with live completion % and deviation alerts. |
| Geotechnical | Surveyor | Navigation | Position vessel for sampling (CPT / Vibrocore) | QINSy / Quantum | Manual positioning requires constant verbal communication with bridge. | Integrated deck and survey alignment view with position confirmation. |
| Geotechnical | Surveyor | Navigation | Move to next station | QINSy | No automation of next-point navigation. | Auto-next-line / waypoint trigger integrated with mission plan. |
| Pipeline / IMR | Surveyor | Navigation | Check infrastructure and exclusion zones | QINSy Display | Risk of ROV collision; manual reference check. | Overlay infrastructure zones and ROV footprint in navigation map. |
| Pipeline / IMR | Senior Surveyor | Navigation | Validate KP reference and offsets | QINSy / Line-plan view | Requires manual spreadsheet cross-check. | Automated KP validation tool with offset tolerance alerts. |
| Pipeline / IMR | PEC | Navigation | Reposition vessel when time limit reached | QINSy / Planner | Requires manual tracking of permit duration. | Mission time management with alert for permit expiry. |
| OBN | Surveyor / Senior Surveyor | Navigation | Confirm node deployment pattern, patch progress, and recovery coverage | Deployment planning tools / positioning systems | Deployment and recovery state is often tracked across fragmented tools or spreadsheets. | Mission-aware node map with deployment, recovery, and exception status. |
| Geophysical with ROV | Surveyor / ROV Pilot | Navigation | Maintain target alignment and vehicle position relative to asset or route | ROV control system / USBL-INS / navigation display | Vehicle position, target context, and survey intent are split across multiple interfaces. | Shared vehicle-and-target navigation view with georeferenced anomaly context. |
| Geophysical with ROTV | Surveyor | Navigation | Maintain tow-body altitude, line-keeping, and corridor overlap | Tow control / navigation / layback tools | Tow geometry and corridor progress are hard to interpret quickly during long runs. | Unified corridor view with tow-state, altitude, and overlap confidence. |
| Geophysical with AUV | Senior Surveyor / mission lead | Navigation | Validate mission plan, route coverage, and abort boundaries | Mission planning software / navigation planning tools | Mission logic and operational constraints are reviewed outside the live operational picture. | Mission-plan review with risk zones, abort logic, and sortie readiness checks. |
| All | Surveyor | Data Logging & Validation | Verify if parameters are correctly logged | Redgate / Folder Structure | Manual folder check even when tool shows "green". | Auto-logging validation integrated with data status indicator. |
| Geotechnical | Surveyor | Data Logging & Validation | Set up extra log files based on client needs | Redgate | Time-consuming manual folder setup. | Configuration templates for client log structures. |
| Pipeline / IMR | Surveyor | Data Logging & Validation | Check video overlays and camera node settings | VOYIS / RVHD / QINSy | Manual verification; frequent mismatch between video and telemetry. | Unified camera config and overlay verification tool. |
| Pipeline / IMR | 3.4U Inspector | Data Logging & Validation | Inspect pipeline visually and record abnormalities | VOYIS / HD Cams | Requires manual logging of anomalies. | Auto-log abnormality snapshots linked to position. |
| OBN | Surveyor / Data Manager | Data Logging & Validation | Reconcile programmed, deployed, recovered, and downloaded node states | Node inventory tools / spreadsheets / file tracking | Inventory and data-state reconciliation is manual and error-prone, especially when exceptions occur. | Unified node lifecycle tracker linking deployment, recovery, and ingest state. |
| Geophysical with ROV | Surveyor | Data Logging & Validation | Capture anomalies with synchronized position, media, and survey context | Online Log / video capture / navigation-linked annotations | Findings are recorded across separate video, note, and position systems. | One action to create event, screenshot or clip, and position-linked annotation together. |
| Geophysical with AUV | Surveyor / Data Manager | Data Logging & Validation | Verify sortie metadata, offload completeness, and mission-to-data association | Mission logs / data offload tools / file tracking | Post-mission data validation is delayed and disconnected from the operational timeline. | Sortie ingest checklist linking mission plan, recovery event, and data completeness. |
| All | Surveyor | Data Logging & Validation | Record survey events in Online Log | Online Log | Manual event entry, risk of missing key events. | Auto-event capture for line start/stop, calibration, deviation. |
| Pipeline / IMR | Surveyor | Data Logging & Validation | Add comments linked to KP reference | Online Log | Requires manual cross-referencing with map. | Auto-tag comments with geolocation from nav feed. |
| All | Surveyor / Senior | Monitoring & QC | Monitor sensor feeds (MBES, SSS, INS, CTD, video) | SIS / Discover / Inomar / EIVA / VOYIS | Multiple UIs; high cognitive load. | Multi-sensor dashboard with unified visual and QC layers. |
| All | Surveyor | Monitoring & QC | Check alarms and thresholds | Native Sensor Software | Inconsistent alarm hierarchies across tools. | Centralized alert panel with configurable severity levels. |
| Pipeline / IMR | Senior Surveyor | Monitoring & QC | Conduct sensor health check | QINSy / Diagnostics | Manual verification only during setup. | Auto-diagnostics with periodic health reports. |
| OBN | Surveyor / Senior Surveyor | Monitoring & QC | Monitor node exceptions, source-pass status, and recovery completeness | Node management / source coordination / operational status tools | Recording confidence and missing-node risk are not visible in one place during operations. | Exception-focused dashboard for node state, source progress, and recovery risk. |
| Geophysical with ROV | Surveyor / Senior Surveyor | Monitoring & QC | Monitor vehicle health, tether/comms, payload status, and live evidence quality | ROV control system / sonar-video viewers / diagnostics | Health, vehicle state, and evidence quality are split across pilot and survey displays. | Role-aware shared monitoring view with vehicle state and evidence quality in one place. |
| Geophysical with ROTV | Surveyor / Senior Surveyor | Monitoring & QC | Assess tow stability, altitude, sensor quality, and revisit triggers | Tow telemetry / sensor viewers / navigation display | Operators infer data quality degradation indirectly from several tools. | Correlate tow-body behavior with sensor-quality degradation and revisit guidance. |
| Geophysical with AUV | mission lead / Senior Surveyor | Monitoring & QC | Track vehicle status, navigation confidence, endurance, and abort conditions during sortie | AUV supervision / acoustic comms / mission status tools | Supervisory awareness is sparse and difficult to compare against mission intent. | Mission supervision panel showing sortie health, navigation confidence, and exception thresholds. |
| All | Surveyor / Senior | Communication & Handover | Conduct shift handover (notes, discussion) | OneNote / Verbal | Inconsistent documentation, data loss across shifts. | Integrated Handover Log linked to Online Log. |
| OBN / ROV / ROTV / AUV | Surveyor / Senior | Communication & Handover | Transfer deployed-asset state, unresolved exceptions, and revisit logic | Verbal / notes / Online Log | Complex mission-state context is easy to lose during handover when the asset is deployed or autonomous. | Structured handover snapshot for deployed assets, active exceptions, and next required action. |
| All | Senior / PEC | Reporting | Prepare daily report and QC summary | Planner / Excel | Manual compilation from multiple data sources. | Auto-generated daily report with key mission metrics. |
| Geotechnical | Surveyor | Reporting | Verify log file structure before delivery | Redgate | File name inconsistencies and missing logs. | Automated file integrity and naming check. |
| Pipeline / IMR | Senior Surveyor | Reporting | Produce MAC / calibration reports | Excel / Word | Manual image capture and parameter copy. | Auto-MAC template generator with embedded images. |
| OBN | Senior Surveyor / Data Manager | Reporting | Produce deployment/recovery reconciliation and exception summary | Excel / reporting packs / inventory exports | Reporting requires manual merge of node inventory, recovery status, and issue logs. | Auto-generated node reconciliation and exception report. |
| Geophysical with AUV | Senior Surveyor / Data Manager | Reporting | Review sortie outcome and decide on rerun or follow-up mission | Mission replay / QC review / reporting tools | Sortie review is separated from planning and ingest context, slowing rerun decisions. | Sortie review package linking plan, execution, QC summary, and rerun recommendation. |

---

## 4. Shared vs. Unique Tasks

| Category | Shared Across All Ops | Unique to Specific Ops |
| --- | --- | --- |
| **Navigation** | Line or task selection, progress tracking | IMR: orientation and exclusion zone control; Geotech: station positioning; OBN: deployment/recovery coverage; ROV/ROTV/AUV: vehicle or sortie path control |
| **Data Logging & Validation** | Parameter validation, event capture, data-state checks | IMR: video overlay validation; Geotech: event-based log setup; OBN: node lifecycle reconciliation; AUV: sortie ingest validation |
| **Monitoring & QC** | Sensor data review, alarms, readiness checks | IMR: visual QC and anomaly interpretation; Geo: coverage completion; OBN: exception and recovery completeness; ROV/ROTV/AUV: vehicle-state-aware QC |
| **Communication & Handover** | Shift exchange, log update | Deployed or autonomous assets require explicit transfer of active state, exceptions, and revisit logic |
| **Reporting** | Daily summaries, QC checks | IMR: MAC report preparation; Geotech: client event file review; OBN: node reconciliation; AUV: sortie outcome review |

---

## 5. Insights Summary

**Top Pain Point Categories:**

1. **Tool Fragmentation:** Operators use 8-12 separate applications per mission.
2. **Manual Verification:** Data integrity checks require folder-level inspection.
3. **Redundant Logging:** Online Log, OneNote, and manual reports duplicate information.
4. **Lack of Standardization:** No consistent thresholds or templates across operation types.
5. **Limited Visibility:** Supervisors lack a live mission overview.
6. **Mission-State Reconciliation:** Deployed or autonomous assets create delayed validation and exception-tracking work.

**Key OIS Opportunities:**

* Consolidate navigation, QC, and logging interfaces.
* Automate event recording and file verification.
* Standardize configuration templates across operations.
* Provide multi-role access with assist modes.
* Enable live mission progress and QC dashboards.
* Preserve asset, node, or sortie lifecycle state across deployment, recovery, ingest, and reporting.

---

## 6. Canonical Sources

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`
* External references used for expanded operation types:
  * Kongsberg Discovery `HUGIN` / `HUGIN Edge`
  * PXGEO and TGS OBN material
  * Horizon Geosciences and similar ROV survey references
  * EIVA `ViperFish` and related ROTV references

---

**End of Document**
*"From task reality to design clarity - OIS's backbone begins with operator truth."*
