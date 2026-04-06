---
doc_id: UXR.00
version: 0.3.0
last_updated: 2026-04-06
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, user-insights, ois, operator-workflows]
---

# UXR.00 - User Research Summary

<!--
Changes made:
1. Added standardized front-matter for consistency.
2. Updated heading formatting to clean ASCII.
3. Added sensor availability and operational prevalence synthesis based on catalog and usage summary.
-->

**Version:** 1.3  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Updated - Includes Task-Tool Mapping and Sensor Grounding

---

## 1. Purpose & Scope

This document consolidates user research for OIS. It summarizes **who our users are**, **how they work** (operations, tasks, and tools), **their pain points**, and **opportunity areas** that inform product pillars and feature design.

Derived from validated internal studies, operational data, and workshop results.

---

## 2. Methods & Sources (Evidence Base)

- Multi-role interviews and observational sessions (Surveyor, Senior Surveyor, PEC, IT).
- Operational-workflow transcription and cross-system tool audits.
- Workshop on pain points and feature priorities.
- Quantitative task-tool datasets (new integration 2025-10-25).
- Sensor catalog and Planner-derived usage summary used as an additional grounding layer for sensor availability and prevalence.

Primary sources: `OI_SMP_Full_UX_Research.md`, `Operational_Workflows.md`, `OperationTypesWorkflows.md`, `Surveyor_Tasks.csv`, `Workshop_workflow_map-features-pain.xlsx`, `Underwater Survey Operations - Task Structure`, `DLog 241025 SMP Direction Update.md`, sensor catalog, and Planner-derived sensor usage summaries.

---

## 3. Participants & Roles (Operational Ecosystem)

| Role | Core Responsibilities | Typical Decisions / Authority | Top Pain Points |
| --- | --- | --- | --- |
| **Surveyor (Operator)** | Operate and monitor sensors; real-time QC and logging. | Start/stop logging; minor config; line selection. | Fragmented tool use, manual logging checks, limited remote control. |
| **Senior Surveyor** | Supervise execution, perform calibrations, ensure spec compliance. | Approve critical settings; handle mobilisation and troubleshooting. | Manual MAC and daily reports; no central diagnostics. |
| **PEC / Supervisor** | Coordinate missions, reallocate vessels or teams, client communication. | Prioritise operations, review data delivery timelines. | Limited multi-mission visibility and handover traceability. |
| **IT Support** | Network access, whitelisting, security approval. | Port rules and MAC/IP management. | Ticketing delays impact mobilisation readiness. |

---

## 4. Operation Types & Contexts

| Operation Type | Purpose / Characteristics | Equipment & Tools |
| --- | --- | --- |
| **Pipeline / Cable Inspection (IMR)** | Highly visual and decision-heavy; requires precise orientation and rapid QC. | ROV + HD video, MBES/SSS, QINSy NAV Display, Online Log, OneNote for handover. |
| **Geophysical** | Fast coverage of large areas with remote instruments. | Discover SSS, Inomar SBP, SIS MBES, Rovins INS, QINSy / EIVA / APOS. |
| **Geotechnical** | Slow, sampling-intensive operations with frequent waiting and manual annotation. | CPT / Vibrocorer, QINSy, EIVA, APOS, manual Redgate logging. |
| **OBN (Ocean Bottom Nodes)** | Seabed seismic workflow built around node deployment, source acquisition, and recovery/reconciliation. | Node programming and inventory tools, deployment/recovery systems, source coordination tools, positioning/QC systems. |
| **Geophysical with ROV** | Close-in, maneuver-driven survey around assets or complex seabed using powered vehicles and mixed payloads. | ROV control system, sonar/camera payloads, USBL/INS, navigation display, Online Log. |
| **Geophysical with ROTV** | Controlled towed-vehicle corridor survey balancing speed and stable sensor altitude. | ROTV control/telemetry, SSS/MBES/magnetometer payloads, navigation/tow management tools, QC viewers. |
| **Geophysical with AUV** | Autonomous or supervised-autonomous geophysical survey driven by mission plans and post-mission ingest/QC. | AUV mission planning tools, onboard acoustic/imaging payloads, acoustic tracking/comms, recovery and data offload tools. |

---

## 5. Operational Phases & High-Level Workflows

**Typical phases:** Project Startup -> Planning -> Mobilisation -> Calibration -> Operation -> Recovery / Retrieval -> Shift Handover -> Reporting.

Key friction themes: network whitelisting, multi-tool integration, manual reporting, bandwidth limits for remote ops, and mission-state reconciliation for deployed or autonomous assets.

---

## 6. Tasks & Tool Usage (Expanded Dataset 2025-10-25)

| Operation Type | Role | Task Type | Task | Tool / Software Used | Notes |
| --- | --- | --- | --- | --- | --- |
| Geo / Pipeline | Surveyor | Navigation | Check which survey line is running | QINSy Quantum (GPS navigation) | Routine start-of-shift check for context. |
| Geotechnical | Surveyor | Navigation | Position vessel for CPT or Vibrocore deployment | QINSy Quantum | Precise position required per client spec. |
| Geotechnical | Surveyor | Navigation | Move to next planned sampling point | QINSy Quantum | Task sequencing after core recovery. |
| Pipeline Inspection | Surveyor | Navigation | Check infrastructure and exclusion zones | Background data in QINSy Display | Avoid collision with ROV equipment. |
| Pipeline Inspection | Surveyor | Navigation | Check current KP (Kilometer Point) reference | QINSy | Maintains alignment and traceability. |
| Pipeline Inspection | Surveyor | Navigation | Orient vessel within 500 m exclusion zone | QINSy (positional guidance) | Part of permit-time management. |
| Pipeline Inspection | Senior Surveyor | Navigation | Validate each pipeline KP reference is correct | QINSy (Line-plan view) | Ensures data coherence and offset accuracy. |
| Pipeline Inspection | PEC / Senior Surveyor | Navigation | Reposition vessel when time limit reached | QINSy planning + situational view | Prevent idle vessel time. |
| Geo / Pipeline | Surveyor | Data Logging & Validation | Verify parameters logged per project manual | Redgate (local file structure) | Manual folder inspection even if status green. |
| Geotechnical | Surveyor | Data Logging & Validation | Set up extra log files as requested | Redgate folders | Client/offline team customization. |
| Pipeline Inspection | Surveyor | Data Logging & Validation | Confirm video overlay accuracy (KP, pipe name, node) | VOYIS / RVHD cams / QINSy / Windy | Ensures synchronized metadata. |
| Pipeline Inspection (IMR) | 3.4U Inspector | Data Logging & Validation | Perform visual inspection and video logging | VOYIS / RVHD cams | Visual confirmation of asset condition. |
| Geo / Pipeline | Surveyor | Data Logging & Validation | Maintain online log of vessel and survey activities | Online Log | Primary timeline of events. |
| Pipeline Inspection | Surveyor | Data Logging & Validation | Comment on pipe abnormalities linked to position | Online Log | Geospatially referenced annotations. |

*Sources: Task Structure transcription + Surveyor_Tasks.csv (verified Oct 2025).*

---

## 7. Sensor Availability and Operational Prevalence

The sensor catalog and Planner-derived usage summary are useful because they sharpen which sensor families appear to matter most operationally and where OIS should avoid treating every sensor as the same kind of product object.

### 7.1 High-prevalence primary acquisition families

| Sensor Family | Usage Signal | Design Relevance |
| --- | --- | --- |
| **MBES** | Strongest prevalence signal in the material provided, with broad vessel usage and high total days. | Should remain a first-class reference workflow for control, QC, and logging confidence. |
| **SSS** | High prevalence across geophysical operations and many vessels. | Supports corridor survey, anomaly marking, revisit logic, and high-throughput QC workflows. |
| **SBP** | High prevalence alongside MBES and SSS in geophysical campaigns. | Reinforces the value of line-time monitoring plus post-line validation. |
| **Magnetometer** | Strong prevalence in geophysical work across multiple vessels. | Important for overlay/QC workflows and for distinguishing real-time display from richer post-processing outputs. |

### 7.2 Critical supporting and dependency systems

| Sensor / System Type | Evidence from Catalog | Design Implication |
| --- | --- | --- |
| **INS / GNSS / USBL / Time Sync** | Multiple variants appear in the catalog, including vessel-, ROV-, and network-specific notes. | Readiness, positioning confidence, and timing integrity should be highly visible in OIS. |
| **PDU / MUX** | Present as available operational systems, not just abstract infrastructure concepts. | Supports dedicated command-and-impact workflows already reflected in the prototype direction. |
| **SVS / SVP** | Notes indicate quality-control needs and direct coupling to MBES workflows. | OIS should distinguish between raw availability and QA-verified environmental input quality. |

### 7.3 Sensors that should not be modeled as generic controllable devices

| Sensor / System Type | Catalog Signal | Design Implication |
| --- | --- | --- |
| **ADCP (Signature 500)** | Self-logging and downloaded at end of project. | Treat as delayed-validation / post-recovery workflow, not as a normal live-controlled sensor. |
| **DVL (ROV Mounted) Syrinx** | Tightly coupled to SprintNav 500, not an independent OI Config item. | Treat as a dependent subsystem within vehicle/navigation context, not always as a standalone pane. |
| **MGC R3** | Connects through SeaPath 385 software. | Some systems should be represented through parent-system state rather than as direct control endpoints. |
| **Ranger2 Pro** | No API; ASCII commands used. | Control and integration depth will vary by sensor, so OIS should not assume uniform command affordances. |
| **Veripos LD900** | API uncertainty noted. | Availability in OIS may depend on integration maturity, not just operational importance. |

### 7.4 Current interpretation for OIS prioritization

1. **MBES, SSS, SBP, and Magnetometer** are the strongest geophysical reference families for shaping the baseline survey experience.
2. **INS, GNSS, USBL, and Time Sync** should be treated as operationally critical dependencies with visible confidence and failure states.
3. **Vehicle-mounted and coupled sensors** require different modeling than vessel-mounted standalone systems.
4. **Self-logging or delayed-ingest devices** create a distinct workflow that spans deployment, recovery, ingest, and later QC.

---

## 8. Pain Points (Synthesised)

- **Tool Fragmentation** - Operators use >8 applications per mission; no unified state view.
- **Manual Logging and Verification** - Redundant folder checks and manual QC of green indicators.
- **Handover Consistency** - Online Log vs OneNote dual systems create gaps.
- **Role Overlap** - Senior Surveyor re-checks tasks done by Surveyor due to trust gaps in systems.
- **Remote Ops Latency** - Bandwidth and RDP performance limit real-time collaboration.
- **Sensor Model Mismatch** - Not all sensors behave like first-class controllable endpoints, but many current toolchains force operators to treat them inconsistently.

---

## 9. Opportunity Themes (Mapped to Pillars)

| Theme | Pillar -> Module | Opportunity |
| --- | --- | --- |
| **Unified Control and Safety** | C&C -> Sensor Control, Configuration Manager | Aggregate ON/OFF/Restart and logging commands with role-based ack loops. |
| **Active Monitoring and QC** | AM -> Output Monitoring, Diagnostics & Health | Live multi-sensor views, thresholds, auto-validation of parameters. |
| **Traceability and Auditability** | Cross -> Online Log, File Monitoring | Auto-log commands + events for seamless handover. |
| **Collaborative Operations** | Cross -> RBAC & Collaboration | Supervisors join sessions without interrupting others. |
| **Operational Efficiency** | Platform -> Mission Deck / Triage Hub | Enable multi-mission operation (2-4 missions per operator). |
| **Sensor-Aware Modeling** | Cross -> Sensor Control, Active Monitoring, File Monitoring | Differentiate between controllable devices, coupled subsystems, dependency systems, and delayed-ingest assets. |

---

## 10. Implications for OIS Strategy

- **Reduce tool count** and centralize control and QC tasks within OIS.
- **Design for multi-mission workspaces** and triage management.
- **Automate log consistency checks** and system traceability.
- **Support remote assist and session sharing** natively.
- **Differentiate control models** between fully controllable sensors, coupled subsystems, dependency systems, and delayed-ingest devices.

---

## 11. Open Questions / Data Needs

1. Final role taxonomy confirmation (Survey Assistant? Client Rep?).
2. Quantitative benchmarks for missions per operator and alert tolerance.
3. Upstream integration scope (DP, weather feeds).
4. Remote ops bandwidth thresholds for multi-stream viewing.
5. Detailed workflow validation for OBN, ROV-, ROTV-, and AUV-assisted survey patterns as OIS scope matures.
6. Mapping of sensor families to operation types beyond the current high-level geophysical prevalence summary.
7. Confirmation of which cataloged sensors are expected to become first-class OIS control surfaces versus monitored dependencies.

---

## 12. Canonical Sources

- **Full UX Research** - Roles, phases, pain points, tool dataset.
- **Operational Workflows** - Mobilisation and operation steps.
- **Operation Types** - IMR / Geo / Geotech specifics.
- **Workshop Matrix** - Pain points and feature links.
- **Direction Update** - Multi-mission and collaboration focus.
- **Current State Deck** - Operational foundation and near-term improvements.
- **Sensor Catalog and usage summary** - Available sensor families, integration notes, and relative operational prevalence.

---

**End of Document**

*"Ground truth captured - OIS design anchored in operator reality."*
