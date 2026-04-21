---
doc_id: UXR.05
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, behavioral-insights, roles, ois]
---

# UXR.05 - Role-Based Insights

<!--
Changes made:
1. Added standardized metadata block.
2. Updated heading to clean ASCII formatting.
3. Added sensor-model implications from catalog and usage evidence.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Draft (Synthesis Layer)

---

## 1. Purpose & Scope

This document summarizes key behavioral insights and operational tendencies per role within offshore and remote survey operations.
It translates observational data and workflow evidence into **design-relevant insights** for OIS, clarifying how each role interacts with systems, what they prioritize, and where their workflows break down.

Each role insight includes:

* **Core behavioral drivers**
* **Operational context and mental model**
* **Pain patterns**
* **System dependencies and limitations**
* **Design principles to support this role in OIS**

---

## 2. Methodology & Sources

Synthesized from:

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* Workshop feature prioritization lists
* Field interviews and onboard observations from `OI_SMP_Full_UX_Research.md`
* Task-level data from `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary as a grounding layer for sensor availability, coupling, and control-model differences

---

## 3. Surveyor (Operator)

### Behavioral Summary

The Surveyor is the **frontline operator** responsible for controlling sensors, maintaining data integrity, and logging operational events. Their focus is divided between monitoring live feeds, verifying recording states, and ensuring compliance with project parameters.

### Mental Model

> "Keep the line running and data clean."

Surveyors think in **timelines and thresholds**: time on line, line completion, green indicators, and immediate QC feedback. They prefer stable, visible systems over automation they cannot confirm.

### Pain Patterns

* Frequent context switching between 8-12 tools.
* "Green light fallacy": systems indicate logging success, but files are missing.
* Manual Online Log entries prone to gaps and inconsistency.
* Disjointed alarms and lack of unified health awareness.
* Additional cognitive load when some devices are controllable, some are read-only dependencies, and others validate only after recovery or download.

### Sensor-Model Implications

For operators, the distinction between sensor types matters behaviorally:

* **Primary acquisition sensors** such as MBES, SSS, and SBP tend to anchor the live work surface.
* **Dependency systems** such as INS, GNSS, USBL, and Time Sync drive trust in the acquisition state even when they are not the main screen focus.
* **Coupled systems** such as DVL tied to a navigation unit should often be understood through parent-system readiness rather than as isolated devices.
* **Delayed-validation devices** such as self-logging or downloaded-at-end systems create uncertainty that persists beyond the live watch.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Clarity first, not complexity** | Unified dashboard with one status layer per sensor family and explicit dependency visibility. |
| **Confidence through feedback** | Real-time "recording verified" indicators linked to file system or ingest checks. |
| **Frictionless action** | One-click controls for start/stop, restart, or switch mission where direct control is actually supported. |
| **Low cognitive load** | Role-optimized layout with consistent distinction between commandable systems, monitored dependencies, and delayed-validation assets. |

---

## 4. Senior Surveyor

### Behavioral Summary

The Senior Surveyor ensures quality, oversees configuration, and supervises operators. Their attention spans across **multiple missions or sensors**, jumping between supervisory review, calibration, and problem-solving.

### Mental Model

> "Trust but verify."

They see themselves as system guardians - maintaining correctness and ensuring junior operators do not misconfigure or miss data.

### Pain Patterns

* No aggregated view of multiple missions.
* Manual MAC and QC reports.
* Time lost verifying settings across UIs.
* No ability to isolate and assist remotely without interrupting the operator.
* Additional burden when integration depth varies by sensor and some systems expose only partial control or indirect state.

### Sensor-Model Implications

For senior surveyors, sensor diversity creates a governance problem as much as a UI problem:

* They need to know which systems are **first-class control surfaces** versus which are **monitored through other software**.
* They need confidence that **coupled systems** are not being reviewed twice through mismatched abstractions.
* They need workflows for **late validation** where data confidence is established after recovery, download, or reconciliation rather than at acquisition time.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Supervisor situational awareness** | Multi-mission view with color-coded health states and dependency confidence. |
| **Guided oversight** | Auto-flag deviations for rapid triage, especially where integration depth or delayed validation increases uncertainty. |
| **Role-protected control** | Read/write access by mission and sensor scope, with clear distinction between command, monitor, and review-only objects. |
| **Assistance without interference** | Remote assist mode with observation-only or controlled handover. |

---

## 5. Project Execution Coordinator (PEC / Supervisor)

### Behavioral Summary

The PEC is responsible for operational efficiency, coordination, and compliance with permit timelines. They think in terms of mission throughput, resource allocation, and downtime avoidance.

### Mental Model

> "Stay on schedule, keep everyone busy."

They operate at a **macro level**, assessing mission readiness and completion metrics rather than individual sensor details.

### Pain Patterns

* Limited visibility into progress and downtime per mission.
* Manual vessel reallocation based on verbal updates.
* Fragmented communication with data teams.
* Difficulty interpreting the operational impact of deployed assets or delayed-validation systems on schedule confidence.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Operational overview at a glance** | Mission Deck showing mission %, vessel status, deployed asset state, and downtime. |
| **Predictive awareness** | Alerts for time limits, weather, permit expirations, and unresolved recovery or ingest obligations. |
| **Cross-team synchronization** | Integration between operations and data QC logs. |
| **Minimal distraction** | Abstracted data view, focused on milestones, not raw telemetry. |

---

## 6. Data Manager / Survey Advisor

### Behavioral Summary

The Data Manager ensures post-operation quality, traceability, and compliance. They are focused on **data lineage** - verifying that every recorded event matches specifications and naming conventions.

### Mental Model

> "If it is not traceable, it is not valid."

They rely heavily on logs, folder structures, and reports, often performing redundant cross-checks due to poor automation.

### Pain Patterns

* Manual verification of Online Log vs actual files.
* Non-standardized metadata and file naming.
* Time-intensive QC report generation.
* Extra reconciliation effort for node inventories, downloaded sensors, sortie ingest, and systems whose final validity is only known after recovery.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **End-to-end traceability** | Auto-linked Online Log -> File Mapping and ingest status. |
| **Data integrity visibility** | File Monitor with completeness scoring and explicit delayed-validation states. |
| **Automation over inspection** | Auto-generated daily/QC reports and reconciliation outputs for nodes, sorties, and uploaded datasets. |
| **Historical context** | Version history and changelog for configuration and events. |

---

## 7. IT / Network Support

### Behavioral Summary

IT supports secure access and network connectivity. Their operational pain comes from firefighting - often handling reactive tickets due to poor pre-check capabilities in the field.

### Mental Model

> "Keep data flowing and ports open."

### Pain Patterns

* Mobilisation delays due to access tickets.
* No visibility into sensor network status.
* Limited diagnostic tools for remote users.
* Additional complexity where integration methods differ by device, including APIs, ASCII command paths, vendor software dependencies, and coupled systems hidden behind parent devices.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Preventive transparency** | Built-in network self-test and status dashboard. |
| **Empower operators** | Diagnostic shortcuts to reduce ticket load. |
| **Traceable changes** | Configuration change log visible to IT. |
| **Fail-safe defaults** | Auto-alert if whitelisting, ports, or integration adapters fail before mobilisation. |

---

## 8. Behavioral Patterns Across Roles

| **Dimension** | **Shared Behavior** | **Design Consideration** |
| --- | --- | --- |
| **Reliance on manual verification** | All roles distrust automation without transparency. | Provide verifiable system feedback such as "verified logging" or explicit ingest confirmation. |
| **Need for situational awareness** | Surveyor -> Senior -> PEC require tiered awareness levels. | Design modular visibility layers by role. |
| **Parallel workflows** | Multiple missions and systems managed concurrently. | Multi-mission workspaces and alert prioritization. |
| **Dependence on shared logs** | Collaboration hinges on event traceability. | Centralized Online Log with structured event types. |
| **Cognitive fatigue from tool overload** | Especially for operators and seniors. | Streamline interfaces and use persistent layouts. |
| **Mixed control models** | Teams work across commandable, coupled, monitored-only, and delayed-validation systems. | Make the sensor/system type explicit so users know what OIS can control, verify, or only observe. |

---

## 9. Summary of Role-Driven Design Principles

1. **Build confidence through feedback** - Show what is happening and why.
2. **Design for mental models** - Reflect how users think: by line, mission, state, and confidence level.
3. **Support supervision without interruption** - Allow assistance without loss of control.
4. **Encourage consistency through structure** - Use templates and auto-checks to enforce standardization.
5. **Scale through modularity** - Support multiple missions, roles, and devices seamlessly.
6. **Respect sensor-model differences** - Distinguish between first-class controls, dependencies, coupled subsystems, and delayed-ingest assets.

---

## 10. Canonical Sources

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* `2.1.OI_SMP_Full_UX_Research.md`
* `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary

---

**End of Document**
*"Every role sees the system differently - OIS must make those views align without friction."*
