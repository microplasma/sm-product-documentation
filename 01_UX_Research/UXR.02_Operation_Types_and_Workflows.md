---
doc_id: UXR.02
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, workflows, operation-types, smp]
---

# UXR.02 – Operation Types and Workflows

<!--
Changes made:
1. Added standardized front-matter for consistency across repository.
2. Updated H1 to unified format (“# UXR.02 – Operation Types and Workflows”).
3. All content below remains verbatim.
-->

**Version:** 1.0  
**Date:** 2025-10-25  
**Owner:** SMP Research & Design  
**Status:** Conceptual Overview (System Design Perspective)

---

## 1. Purpose & Scope
This document defines the major **operation types** managed within the Survey Management Platform (SMP) and describes their **core workflow structures** at a system-design level.  

The objective is to provide a **conceptual view** of how SMP supports survey operations across distinct domains (Geophysical, Geotechnical, Pipeline / IMR) while aligning workflows to SMP modules such as **Command & Control (C&C)**, **Active Monitoring (AM)**, and **Online Log Integration**.

---

## 2. Operation Type Overview

| **Operation Type** | **Purpose / Characteristics** | **Key SMP Relevance** |
|---|---|---|
| **Geophysical** | High-speed, wide-area seabed mapping using acoustic sensors (MBES, SSS, SBP). Requires multi-sensor synchronization and coverage tracking. | Emphasis on real-time monitoring, line planning, and QC validation tools. |
| **Geotechnical** | Sampling and soil investigation for construction planning. Lower tempo, more mechanical operations (CPT, coring). | Focus on event logging, equipment positioning, and coordination between survey and deck teams. |
| **Pipeline / IMR** | Visual and positional inspection of subsea infrastructure. Most complex type, requiring high operator attention and sensor diversity (video, sonar, INS). | Core user case for C&C, Active Monitoring, and configuration templates. |

---

## 3. General Workflow Phases (Shared Across Types)

| **Phase** | **Purpose** | **Representative Actions** | **SMP Interaction Layer** |
|---|---|---|---|
| **Startup & Planning** | Prepare mission parameters, equipment configs, and line plans. | Configure QINSy projects, verify IP/MAC permissions, review line files. | Configuration Manager, User Roles & Access. |
| **Mobilisation** | System calibration, equipment validation, and readiness checks. | Calibrate sensors (USBL, INS, MBES); confirm logging paths. | Diagnostics & Health, Config Templates. |
| **Operation (Live Survey)** | Execute missions, monitor data streams, QC, and anomaly detection. | Monitor live feeds, start/stop logging, annotate Online Log. | Command & Control, Active Monitoring, Online Log Integration. |
| **Shift Handover** | Transfer operational state and decisions between operators. | Handover notes, Online Log updates, supervisor validation. | Online Log, Multi-User Accessibility. |
| **Reporting & Post-Processing** | Compile logs, QC summaries, and data delivery. | Export Online Log data, verify file structure. | File Monitoring, QC Report Generation. |

---

## 4. SMP Interaction Layers by Operation Type

### 4.1 Geophysical
- **Focus:** Real-time QC and efficiency (coverage and quality).  
- **Key SMP Features:**
  - Multi-sensor sync (MBES, SSS, SBP).
  - Auto-validation of parameters (ping rate, SNR, line deviation).
  - Integrated log of calibration and event markers.
- **Workflow Simplification Goals:**
  - Reduce manual folder checks for logging verification.
  - Enable auto-QC scoring and threshold alerts.

---

### 4.2 Geotechnical
- **Focus:** Data integrity and coordination between survey and deck operations.  
- **Key SMP Features:**
  - Position and event logging for each sampling station.
  - Config templates for standard borehole operations.
  - Integration with vessel control and deck activity scheduling.
- **Workflow Simplification Goals:**
  - Automate event creation (push start, recovery complete).
  - Link deck-side equipment telemetry with survey records.

---

### 4.3 Pipeline / IMR
- **Focus:** Live visual and positional inspection.  
- **Key SMP Features:**
  - ON/OFF/Restart commands for sensors and cameras.
  - Live stream viewer with overlay controls (KP references, pipe names, depth data).
  - Alert-based QC and status indication.
  - Configurable templates for IMR project types.
- **Workflow Simplification Goals:**
  - Reduce manual camera overlay verification.
  - Enable interactive signal-flow diagram for troubleshooting.
  - Integrate Online Log events (line start/end, anomaly) automatically.

---

## 5. Comparative Characteristics Table

| **Aspect** | **Geophysical** | **Geotechnical** | **Pipeline / IMR** |
|---|---|---|---|
| **Data Type** | Acoustic | Mechanical / Environmental | Visual + Acoustic |
| **Pace** | High-speed, continuous | Slow, discrete events | Moderate, decision-heavy |
| **Risk Profile** | Low | Medium (equipment jams) | High (infrastructure proximity) |
| **Operational Dependency** | Navigation accuracy | Deck coordination | Real-time situational awareness |
| **Primary SMP Modules** | Active Monitoring | Online Log | Command & Control, Active Monitoring |

---

## 6. Multi-Mission Implications

| **Operational Challenge** | **Impact of Multi-Mission Work** | **SMP Strategy** |
|---|---|---|
| Attention management | Operators must divide focus across simultaneous missions. | Mission Deck with multi-mission views and alerts prioritization. |
| Configuration drift | Risk of inconsistent settings across missions. | Centralized Configuration Manager with templates. |
| Data integrity | Higher potential for missed logs or incorrect associations. | Auto-log validation and mission-level traceability. |
| Collaboration load | Supervisors assisting multiple surveyors concurrently. | Multi-user session management and assist mode. |

---

## 7. Strategic Implications for SMP Design
1. **Workflow harmonization**: unify core phases across operation types for consistency.  
2. **Automation of routine checks**: reduce manual QC and verification steps.  
3. **Role adaptability**: enable one operator to manage multiple missions through modular interfaces.  
4. **Template-driven configuration**: minimize setup time and reduce risk of inconsistency.  
5. **Integrated traceability**: all operational events auto-logged and cross-linked with mission context.  

---

## 8. Canonical Sources
- `2.3.OI_Operational_Workflows.md`
- `2.3.1.OperationTypesWorkflows.md`
- `Underwater Survey Operations – Task Structure`
- `Surveyor_Tasks.csv`
- `Workshop_workflow_map-features-pain.xlsx`

---

**End of Document**  
_"Clarity through structure – unified workflows as the foundation for SMP design."_