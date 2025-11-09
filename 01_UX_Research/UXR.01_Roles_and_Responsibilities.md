---
doc_id: UXR.01
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, roles, workflows, responsibilities, smp]
---

# UXR.01 – Roles and Responsibilities

<!--
Changes made:
1) Added standardized front-matter for repository consistency.
2) Updated H1 heading to the standardized format (“# UXR.01 – Roles and Responsibilities”).
3) All body text below remains verbatim; sources remain as literal references (not links).
-->

**Version:** 1.0

**Date:** 2025-10-25

**Owner:** SMP Research & Design

**Status:** Draft (evidence-based)

---

## 1. Purpose & Scope

This document defines the **key roles involved in underwater survey operations**, their core responsibilities, decision-making boundaries, and tool dependencies.

It highlights how these roles interact across operation types (Geophysical, Geotechnical, Pipeline/IMR) and how SMP can support their evolving collaboration patterns — particularly in the shift toward **multi-mission, reduced-headcount operations**.

---

## 2. Methodology & Sources

Derived from:

- UX research interviews and onboard observation logs (`OI_SMP_Full_UX_Research.md`)
- Operational workflow documents (`OI_Operational_Workflows.md`, `OperationTypesWorkflows.md`)
- Role–task–tool dataset (Oct 2025 update)
- Workshop workflow & pain mapping matrix
- “Underwater Survey Operations – Task Structure” transcription

---

## 3. Role Overview (Hierarchy and Relationships)

| **Role** | **Primary Focus** | **Operational Level** | **Decision Scope** | **Typical Collaboration** |
| --- | --- | --- | --- | --- |
| **Surveyor (Operator)** | Day-to-day sensor control, data QC, logging, and real-time monitoring. | Mission / Line level | Start/stop lines, verify data integrity, minor config. | Senior Surveyor (review), PEC (coordination), 3.4U Inspector (visual). |
| **Senior Surveyor** | Oversees quality, configuration, and line validation. Troubleshoots data anomalies and coordinates multi-sensor calibration. | Vessel / Mission level | Authorizes configuration changes, supervises handovers, oversees reporting. | Surveyors (support), PEC (planning), Client Rep (validation). |
| **Project Execution Coordinator (PEC)** | Operational planning, client liaison, and vessel task allocation. | Project level | Reassigns resources, approves time-limited operations, reviews progress. | Senior Surveyor (execution), Survey Advisor (oversight). |
| **Survey Advisor / Data Manager** | Ensures data product integrity, standardization, and delivery compliance. | Cross-project | Validates final logs, QC results, and metadata consistency. | Senior Surveyor (data origin), PEC (handover). |
| **IT / Network Support** | Ensures system connectivity, security, and access. | Global support | Manages whitelisting, port setup, and user access. | Surveyor / Supervisor (field), Remote Ops (support). |

---

## 4. Role-by-Role Analysis

### 4.1 Surveyor (Operator)

**Primary Goals:**

- Maintain continuous data acquisition and QC.
- Execute lines accurately and follow configuration protocols.
- Maintain shift consistency and logging accuracy.

**Core Tasks:**

- Start/stop logging, verify folder structure.
- Check live sensor feeds (INS, MBES, SSS, cameras).
- Perform Online Log entries and event annotations.
- Communicate deviations or abnormalities.

**Tools Used:**

QINSy / Quantum, Discover, Inomar, SIS, EIVA Touchpad, APOS, VOYIS / RVHD, Online Log, OneNote.

**Pain Points:**

- Frequent manual verification across tools (“green but not recording”).
- No consolidated overview of data health.
- Bandwidth limitations in remote operation.

**Opportunities for SMP:**

- Unified status dashboard (Active Monitoring).
- Auto-verification of data stream and logging states.
- Context-aware logging shortcuts and consistency templates.

---

### 4.2 Senior Surveyor

**Primary Goals:**

- Guarantee mission compliance with project specifications.
- Supervise configurations and QC thresholds.
- Mentor surveyors and handle escalation points.

**Core Tasks:**

- Validate KP references and navigation lines.
- Execute calibrations and daily MAC reports.
- Review Online Logs for consistency.
- Support triage when sensors fail or misconfigure.

**Tools Used:**

QINSy (line plans, KP validation), Excel MAC templates, Online Log, Planner / reporting tools.

**Pain Points:**

- Manual MAC preparation with screenshots.
- No central configuration rollback.
- Limited cross-mission visibility.

**Opportunities for SMP:**

- Config template management and rollback functions.
- Role-based configuration lock.
- Cross-mission supervisory view (Mission Deck).

---

### 4.3 Project Execution Coordinator (PEC)

**Primary Goals:**

- Maintain mission progress within permit and time constraints.
- Manage vessel task allocation and downtime efficiency.

**Core Tasks:**

- Review mission coverage; reassign resources when time limits are reached.
- Communicate with Senior Surveyor for repositioning.
- Review daily operations and logs.

**Tools Used:**

Planner, QINSy (navigation planning), Online Log (summaries).

**Pain Points:**

- No real-time progress visualization across concurrent missions.
- Manual coordination with vessel operations.

**Opportunities for SMP:**

- Mission overview dashboard with completion metrics.
- Alert-based downtime indicators.

---

### 4.4 Survey Advisor / Data Manager

**Primary Goals:**

- Oversee QC delivery pipeline and metadata standards.
- Ensure traceability from acquisition to client output.

**Core Tasks:**

- Validate daily logs and handovers.
- Verify data file structure and naming compliance.
- Manage long-term data archiving.

**Tools Used:**

Network folders, Redgate, Planner, custom QC scripts.

**Pain Points:**

- Non-standardized metadata between operations.
- Manual cross-verification of event logs and folders.

**Opportunities for SMP:**

- Integrated Online Log → File structure linkage.
- QC compliance report generation.

---

### 4.5 IT / Network Support

**Primary Goals:**

- Maintain stable, secure connectivity and access control.
- Minimize mobilisation delays related to network and security.

**Core Tasks:**

- Handle IP/MAC approvals and firewall adjustments.
- Support bandwidth diagnostics.
- Troubleshoot remote session issues.

**Pain Points:**

- Delayed approval process disrupts mobilisation.
- Lack of diagnostic tools accessible to operators.

**Opportunities for SMP:**

- Embedded diagnostics / ping-test module.
- Operator-level pre-check routines before mobilisation.

---

## 5. Cross-Role Interaction Model

| **Collaboration Context** | **Participants** | **Current Mode** | **Pain Point** | **SMP Opportunity** |
| --- | --- | --- | --- | --- |
| **Shift Handover** | Surveyor ↔ Surveyor | OneNote + verbal | Inconsistent details, missing anomalies | Structured handover interface integrated with Online Log |
| **QC Review** | Surveyor ↔ Senior Surveyor | Shared folders, MAC | Redundant re-checking | Automated QC validation dashboard |
| **Troubleshooting** | Surveyor ↔ Senior Surveyor ↔ IT | RDP, Teams | Session interference | Multi-user “assist” mode with isolation |
| **Mission Oversight** | Senior Surveyor ↔ PEC | Daily reports | No live mission progress view | Mission Deck with live metrics and completion maps |
| **Data Delivery** | Senior Surveyor ↔ Data Manager | Manual file verification | Missing traceability | Log-linked file verification and QC summary generation |

---

## 6. Evolving Role Dynamics in SMP

As SMP introduces automation and multi-mission control:

| **Role Evolution** | **Change Introduced by SMP** | **Impact** |
| --- | --- | --- |
| Surveyor | Gains ability to monitor multiple missions simultaneously. | Reduces idle time; requires new alert prioritization tools. |
| Senior Surveyor | Focus shifts to supervision and triage rather than micromanagement. | Increases oversight efficiency and reduces redundant checks. |
| PEC | Moves from manual coordination to strategic triage and optimization. | Improves throughput and vessel utilization. |
| Data Manager | Benefits from automatic log–file integration and QC traceability. | Ensures auditability and consistent delivery. |
| IT | Sees reduced support tickets via embedded diagnostics. | Increases operational uptime and self-sufficiency. |

---

## 7. Role-to-Module Mapping (SMP Impact Matrix)

| **Role** | **Key SMP Modules** | **Primary Interactions** |
| --- | --- | --- |
| Surveyor | Sensor Control, Output Monitoring, Online Log | Execute commands, review data, annotate logs. |
| Senior Surveyor | Configuration Manager, Diagnostics & Health, Mission Deck | Supervise configuration, validate QC, oversee multiple missions. |
| PEC | Mission Deck, File Monitoring | Monitor completion %, manage downtime and vessel reallocation. |
| Data Manager | Online Log, File Monitoring | Audit logs and file traceability, generate QC reports. |
| IT Support | Diagnostics & Health | Conduct connectivity tests, monitor system status remotely. |

---

## 8. Summary: Design Implications

1. **Interfaces must reflect role granularity** — e.g., configuration locks by role.
2. **Multi-user concurrency is essential** — roles must work on shared missions without interference.
3. **Task and tool consolidation** should focus on reducing redundant manual checks.
4. **Supervisory roles** require multi-mission overviews, while operators need focus-preserving views.
5. **Collaboration and traceability** are foundational across all roles.

---

## 9. Canonical Sources

- `2.1.OI_SMP_Full_UX_Research.md`
- `2.3.OI_Operational_Workflows.md`
- `2.3.1.OperationTypesWorkflows.md`
- `Underwater Survey Operations – Task Structure`
- `Surveyor_Tasks.csv`
- `Workshop_workflow_map-features-pain.xlsx`

---

**End of Document**

*“Understand the people — design the system.”*