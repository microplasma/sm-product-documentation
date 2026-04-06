---
doc_id: UXR.04
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, pain-points, opportunities, ois]
---

# UXR.04 – Pain Points and Opportunities

<!--
Changes made:
1. Added standardized front-matter for repository uniformity.
2. Updated H1 heading to align with OIS documentation naming convention.
3. No textual, tabular, or semantic changes.
-->

**Version:** 1.0  
**Date:** 2025-10-25  
**Owner:** OIS Research & Design  
**Status:** Consolidated Summary (Strategic Layer)

---

## 1. Purpose & Scope

This document consolidates pain points identified across research, workflow analyses, and workshops, translating them into **strategic opportunity areas** for the OI Survey (OIS).

It complements `01.03_Tasks_and_Tools_Matrix.md` by organizing findings into clusters that reflect operational stages and align with OIS's **core product pillars** — **Command & Control (C&C)**, **Active Monitoring (AM)**, **Online Log & Traceability**, and **Collaboration & Multi-Mission Enablement**.

---

## 2. Methodology & Sources

Derived from cross-analysis of:

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations – Task Structure`
* `Surveyor_Tasks.csv`

Pain points were categorized according to operational phase, user role, and system dependency. Opportunities were mapped based on feature alignment and design feasibility.

---

## 3. Pain Point Clusters by Operational Phase

| **Phase**                       | **Pain Points (Summary)**                                                                                                                      | **Root Causes**                                                             | **Opportunity Theme**                                                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Startup & Planning**          | - Network whitelisting delays  - Redundant configuration effort across sensors - Manual setup of folder structures                             | - IT dependency and lack of automation - No standardized templates          | **Configuration Automation & Access Readiness** – Predefined configuration templates, network pre-check routines.           |
| **Mobilisation**                | - Manual calibration and validation (USBL, INS, MBES) - Missing integration visibility - Poor handover between setup and operation             | - Tool isolation - Lack of diagnostic automation                            | **Automated Calibration & Health Checks** – Embedded diagnostic and status verification tools.                              |
| **Operation (Live)**            | - Fragmented tool landscape (8–12 active tools) - Repeated parameter checks across UIs - Logging inconsistencies - No centralized alert system | - Legacy architecture - Manual quality assurance - Limited interoperability | **Unified Operational Interface** – Single OIS workspace integrating control, monitoring, and logging with alert hierarchy. |
| **Shift Handover**              | - Disconnected systems (OneNote, Online Log) - Inconsistent event documentation - Reliance on memory and verbal briefings                      | - Lack of structured handover interface - No continuity of context          | **Integrated Handover & Traceability** – Shared session state, auto-log summaries, role-based access continuity.            |
| **Reporting & Post-Processing** | - Manual compilation of daily reports - Folder validation - Inconsistent metadata standards                                                    | - Disparate data sources - Lack of automation                               | **Automated Reporting & Data Integrity Validation** – Auto-generated QC summaries, file traceability verification.          |

---

## 4. Cross-Role Pain & Opportunity Mapping

| **Role**                | **Primary Pain Points**                                               | **Opportunity Direction (OIS Intervention)**                        |
| ----------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Surveyor (Operator)** | - Manual data validation, repetitive UI switching, fragmented alarms  | Unified mission console combining control, QC, and alerts.          |
| **Senior Surveyor**     | - No cross-mission visibility, repeated oversight of surveyor actions | Multi-mission supervisory view and configuration templates.         |
| **PEC / Supervisor**    | - Manual mission progress tracking and downtime awareness             | Mission Deck with live progress, completion %, and downtime alerts. |
| **Data Manager**        | - Manual file structure and metadata validation                       | Auto-log to file mapping and metadata compliance tools.             |
| **IT Support**          | - Ticket bottlenecks during mobilisation                              | Integrated diagnostic routines and network self-check tools.        |

---

## 5. Opportunity Themes (Strategic Grouping)

| **Theme**                                        | **Problem Addressed**                                             | **Example OIS Features / Modules**                                               |
| ------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **1. Configuration Automation & Control Safety** | Manual setup, inconsistent configuration, error-prone calibration | Configuration Templates, Configuration Lock, Rollback, Auto-Diagnostics          |
| **2. Unified Operational Environment**           | Multi-tool fragmentation, manual validation                       | Mission Deck, Command & Control Core, Multi-Sensor Dashboard                     |
| **3. Active Monitoring & Health Awareness**      | Lack of real-time QC, no consistent alert hierarchy               | Threshold Configuration, Health Indicators, Severity Alerts, Signal Flow Diagram |
| **4. Logging & Traceability Automation**         | Manual log entry, duplication, poor continuity                    | Online Log Integration, Auto-Log Events, Log Consistency Checker                 |
| **5. Collaboration & Multi-User Accessibility**  | Limited concurrent access, interference risk                      | Session Sharing, Assist Mode, Role-Based Permissions                             |
| **6. Reporting & Data Integrity Automation**     | Manual reporting, metadata mismatches                             | File Monitor, Auto-QC Report, Changelog Journal                                  |

---

## 6. Pain Point Intensity Matrix (Prioritized by Impact)

| **Pain Area**              | **Impact (Operational Downtime)** | **Frequency** | **Priority Level** |
| -------------------------- | --------------------------------- | ------------- | ------------------ |
| Tool Fragmentation         | High                              | Constant      | 🔴 Critical        |
| Manual Logging             | High                              | Constant      | 🔴 Critical        |
| IT Access Delays           | Medium                            | Frequent      | 🟠 High            |
| Lack of QC Automation      | Medium                            | Frequent      | 🟠 High            |
| Poor Handover Traceability | Medium                            | Frequent      | 🟡 Moderate        |
| Manual Reporting           | Low                               | Common        | 🟡 Moderate        |

---

## 7. Strategic Design Implications

1. **OIS as the single operational environment:** unify fragmented tool landscape into a cohesive workspace.
2. **Shift from reactive QC to proactive health monitoring:** embed diagnostics, auto-thresholds, and alerts.
3. **Enable operator efficiency scaling:** through automation, template-driven configuration, and multi-mission support.
4. **Institutionalize traceability:** every event, action, and change is auto-logged with role attribution.
5. **Reduce cognitive load:** use role-based visibility layers and simplified alert hierarchies.

---

## 8. Canonical Sources

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations – Task Structure`

---

**End of Document**
*“Every friction mapped is an opportunity for precision and simplification.”*
