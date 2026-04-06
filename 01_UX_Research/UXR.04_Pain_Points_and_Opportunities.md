---
doc_id: UXR.04
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, pain-points, opportunities, ois]
---

# UXR.04 - Pain Points and Opportunities

<!--
Changes made:
1. Added standardized front-matter for repository uniformity.
2. Updated heading to clean ASCII formatting.
3. Added mission-state reconciliation and mixed sensor-control-model implications.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Consolidated Summary (Strategic Layer)

---

## 1. Purpose & Scope

This document consolidates pain points identified across research, workflow analyses, and workshops, translating them into **strategic opportunity areas** for the OI Survey (OIS).

It complements `01.03_Tasks_and_Tools_Matrix.md` by organizing findings into clusters that reflect operational stages and align with OIS's **core product pillars** - **Command & Control (C&C)**, **Active Monitoring (AM)**, **Online Log & Traceability**, and **Collaboration & Multi-Mission Enablement**.

---

## 2. Methodology & Sources

Derived from cross-analysis of:

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* Sensor catalog and usage summary

Pain points were categorized according to operational phase, user role, and system dependency. Opportunities were mapped based on feature alignment and design feasibility.

---

## 3. Pain Point Clusters by Operational Phase

| **Phase** | **Pain Points (Summary)** | **Root Causes** | **Opportunity Theme** |
| --- | --- | --- | --- |
| **Startup & Planning** | Network whitelisting delays; redundant configuration effort across sensors; manual setup of folder structures; unclear distinction between direct-control and dependency systems. | IT dependency; lack of automation; no standardized templates; uneven integration models. | **Configuration Automation & Access Readiness** - Predefined configuration templates, network pre-check routines, and clearer sensor/system classification. |
| **Mobilisation** | Manual calibration and validation (USBL, INS, MBES); missing integration visibility; poor handover between setup and operation. | Tool isolation; lack of diagnostic automation; weak dependency confidence signals. | **Automated Calibration & Health Checks** - Embedded diagnostic and status verification tools. |
| **Operation (Live)** | Fragmented tool landscape (8-12 active tools); repeated parameter checks across UIs; logging inconsistencies; no centralized alert system; mixed control models across sensors. | Legacy architecture; manual quality assurance; limited interoperability; inconsistent integration depth. | **Unified Operational Interface** - Single OIS workspace integrating control, monitoring, and logging with alert hierarchy and explicit system-state semantics. |
| **Recovery / Retrieval** | Deployed or autonomous assets require manual reconciliation of state, completeness, and exceptions. | Delayed-validation workflows; inventory tracking outside core operational tools. | **Mission-State Reconciliation** - Unified asset lifecycle tracking across deployment, recovery, ingest, and exception handling. |
| **Shift Handover** | Disconnected systems (OneNote, Online Log); inconsistent event documentation; reliance on memory and verbal briefings. | Lack of structured handover interface; no continuity of context. | **Integrated Handover & Traceability** - Shared session state, auto-log summaries, role-based access continuity. |
| **Reporting & Post-Processing** | Manual compilation of daily reports; folder validation; inconsistent metadata standards; late reconciliation for downloaded or self-logging devices. | Disparate data sources; lack of automation; delayed validation outside the main operational flow. | **Automated Reporting & Data Integrity Validation** - Auto-generated QC summaries, file traceability verification, and reconciliation outputs. |

---

## 4. Cross-Role Pain & Opportunity Mapping

| **Role** | **Primary Pain Points** | **Opportunity Direction (OIS Intervention)** |
| --- | --- | --- |
| **Surveyor (Operator)** | Manual data validation, repetitive UI switching, fragmented alarms, mixed control models. | Unified mission console combining control, QC, alerts, and explicit dependency visibility. |
| **Senior Surveyor** | No cross-mission visibility, repeated oversight of surveyor actions, weak clarity on integration depth by system. | Multi-mission supervisory view, configuration templates, and distinction between command, monitor, and review-only systems. |
| **PEC / Supervisor** | Manual mission progress tracking, downtime awareness, and weak confidence in deployed-asset completeness. | Mission Deck with live progress, completion %, downtime alerts, and recovery-state visibility. |
| **Data Manager** | Manual file structure and metadata validation; delayed reconciliation for downloaded assets. | Auto-log to file mapping, metadata compliance tools, and asset-ingest reconciliation. |
| **IT Support** | Ticket bottlenecks during mobilisation; inconsistent integration methods across devices. | Integrated diagnostic routines, network self-check tools, and clearer adapter/integration-state visibility. |

---

## 5. Opportunity Themes (Strategic Grouping)

| **Theme** | **Problem Addressed** | **Example OIS Features / Modules** |
| --- | --- | --- |
| **1. Configuration Automation & Control Safety** | Manual setup, inconsistent configuration, error-prone calibration | Configuration Templates, Configuration Lock, Rollback, Auto-Diagnostics |
| **2. Unified Operational Environment** | Multi-tool fragmentation, manual validation | Mission Deck, Command & Control Core, Multi-Sensor Dashboard |
| **3. Active Monitoring & Health Awareness** | Lack of real-time QC, no consistent alert hierarchy | Threshold Configuration, Health Indicators, Severity Alerts, Signal Flow Diagram |
| **4. Logging & Traceability Automation** | Manual log entry, duplication, poor continuity | Online Log Integration, Auto-Log Events, Log Consistency Checker |
| **5. Collaboration & Multi-User Accessibility** | Limited concurrent access, interference risk | Session Sharing, Assist Mode, Role-Based Permissions |
| **6. Reporting & Data Integrity Automation** | Manual reporting, metadata mismatches | File Monitor, Auto-QC Report, Changelog Journal |
| **7. Mission-State Reconciliation** | Deployed assets, downloaded sensors, and delayed validation create gaps across phases | Asset lifecycle tracker, ingest-state verification, node or sortie reconciliation views |
| **8. Sensor-Aware System Modeling** | Not all sensors are equivalent in control depth, coupling, or validation timing | Sensor taxonomy, dependency-aware readiness, coupled-system representation |

---

## 6. Pain Point Intensity Matrix (Prioritized by Impact)

| **Pain Area** | **Impact (Operational Downtime)** | **Frequency** | **Priority Level** |
| --- | --- | --- | --- |
| Tool Fragmentation | High | Constant | Critical |
| Manual Logging | High | Constant | Critical |
| Mission-State Reconciliation | High | Recurring in relevant operations | High |
| IT Access Delays | Medium | Frequent | High |
| Lack of QC Automation | Medium | Frequent | High |
| Poor Handover Traceability | Medium | Frequent | Moderate |
| Manual Reporting | Low | Common | Moderate |

---

## 7. Strategic Design Implications

1. **OIS as the single operational environment:** unify fragmented tool landscape into a cohesive workspace.
2. **Shift from reactive QC to proactive health monitoring:** embed diagnostics, auto-thresholds, and alerts.
3. **Enable operator efficiency scaling:** through automation, template-driven configuration, and multi-mission support.
4. **Institutionalize traceability:** every event, action, and change is auto-logged with role attribution.
5. **Reduce cognitive load:** use role-based visibility layers and simplified alert hierarchies.
6. **Model systems honestly:** distinguish between first-class controls, monitored dependencies, coupled subsystems, and delayed-validation assets.

---

## 8. Canonical Sources

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary

---

**End of Document**
*"Every friction mapped is an opportunity for precision and simplification."*
