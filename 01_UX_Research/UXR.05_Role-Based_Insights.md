---
doc_id: UXR.05
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, behavioral-insights, roles, smp]
---

# UXR.05 – Role-Based Insights

<!--
Changes made:
1. Added standardized metadata block.
2. Updated top-level heading to follow SMP documentation convention.
3. All body content preserved verbatim.
-->

**Version:** 1.0  
**Date:** 2025-10-25  
**Owner:** SMP Research & Design  
**Status:** Draft (Synthesis Layer)

---

## 1. Purpose & Scope

This document summarizes key behavioral insights and operational tendencies per role within offshore and remote survey operations.
It translates observational data and workflow evidence into **design-relevant insights** for SMP, clarifying how each role interacts with systems, what they prioritize, and where their workflows break down.

Each role insight includes:

* **Core behavioral drivers**
* **Operational context and mental model**
* **Pain patterns**
* **System dependencies and limitations**
* **Design principles to support this role in SMP**

---

## 2. Methodology & Sources

Synthesized from:

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* Workshop feature prioritization lists
* Field interviews and onboard observations from `OI_SMP_Full_UX_Research.md`
* Task-level data from `Underwater Survey Operations – Task Structure`

---

## 3. Surveyor (Operator)

### Behavioral Summary

The Surveyor is the **frontline operator** responsible for controlling sensors, maintaining data integrity, and logging operational events. Their focus is divided between monitoring live feeds, verifying recording states, and ensuring compliance with project parameters.

### Mental Model

> “Keep the line running and data clean.”

Surveyors think in **timelines and thresholds**: time on line, line completion, green indicators, and immediate QC feedback. They prefer stable, visible systems over automation they can’t confirm.

### Pain Patterns

* Frequent context switching between 8–12 tools.
* “Green light fallacy”: systems indicate logging success, but files are missing.
* Manual Online Log entries prone to gaps and inconsistency.
* Disjointed alarms and lack of unified health awareness.

### SMP Design Implications

| Design Principle                  | Implementation Example                                                  |
| --------------------------------- | ----------------------------------------------------------------------- |
| **Clarity first, not complexity** | Unified dashboard with one status layer per sensor.                     |
| **Confidence through feedback**   | Real-time “recording verified” indicators linked to file system checks. |
| **Frictionless action**           | One-click controls for start/stop, restart, or switch mission.          |
| **Low cognitive load**            | Role-optimized layout (data flow left→right, alerts top→bottom).        |

---

## 4. Senior Surveyor

### Behavioral Summary

The Senior Surveyor ensures quality, oversees configuration, and supervises operators. Their attention spans across **multiple missions or sensors**, jumping between supervisory review, calibration, and problem-solving.

### Mental Model

> “Trust but verify.”

They see themselves as system guardians — maintaining correctness and ensuring junior operators don’t misconfigure or miss data.

### Pain Patterns

* No aggregated view of multiple missions.
* Manual MAC and QC reports.
* Time lost verifying settings across UIs.
* No ability to isolate and assist remotely without interrupting the operator.

### SMP Design Implications

| Design Principle                     | Implementation Example                                           |
| ------------------------------------ | ---------------------------------------------------------------- |
| **Supervisor situational awareness** | Multi-mission view with color-coded health states.               |
| **Guided oversight**                 | Auto-flag deviations for rapid triage.                           |
| **Role-protected control**           | Read/write access by mission and sensor scope.                   |
| **Assistance without interference**  | Remote assist mode with observation-only or controlled handover. |

---

## 5. Project Execution Coordinator (PEC / Supervisor)

### Behavioral Summary

The PEC is responsible for operational efficiency, coordination, and compliance with permit timelines. They think in terms of mission throughput, resource allocation, and downtime avoidance.

### Mental Model

> “Stay on schedule, keep everyone busy.”

They operate at a **macro level**, assessing mission readiness and completion metrics rather than individual sensor details.

### Pain Patterns

* Limited visibility into progress and downtime per mission.
* Manual vessel reallocation based on verbal updates.
* Fragmented communication with data teams.

### SMP Design Implications

| Design Principle                     | Implementation Example                                          |
| ------------------------------------ | --------------------------------------------------------------- |
| **Operational overview at a glance** | Mission Deck showing mission %, vessel status, and downtime.    |
| **Predictive awareness**             | Alerts for time limits, weather, or permit expirations.         |
| **Cross-team synchronization**       | Integration between operations and data QC logs.                |
| **Minimal distraction**              | Abstracted data view, focused on milestones, not raw telemetry. |

---

## 6. Data Manager / Survey Advisor

### Behavioral Summary

The Data Manager ensures post-operation quality, traceability, and compliance. They are focused on **data lineage** — verifying that every recorded event matches specifications and naming conventions.

### Mental Model

> “If it’s not traceable, it’s not valid.”

They rely heavily on logs, folder structures, and reports, often performing redundant cross-checks due to poor automation.

### Pain Patterns

* Manual verification of Online Log vs actual files.
* Non-standardized metadata and file naming.
* Time-intensive QC report generation.

### SMP Design Implications

| Design Principle               | Implementation Example                                      |
| ------------------------------ | ----------------------------------------------------------- |
| **End-to-end traceability**    | Auto-linked Online Log → File Mapping.                      |
| **Data integrity visibility**  | File Monitor with QC completeness scoring.                  |
| **Automation over inspection** | Auto-generated daily/QC reports.                            |
| **Historical context**         | Version history and changelog for configuration and events. |

---

## 7. IT / Network Support

### Behavioral Summary

IT supports secure access and network connectivity. Their operational pain comes from firefighting — often handling reactive tickets due to poor pre-check capabilities in the field.

### Mental Model

> “Keep data flowing and ports open.”

### Pain Patterns

* Mobilisation delays due to access tickets.
* No visibility into sensor network status.
* Limited diagnostic tools for remote users.

### SMP Design Implications

| Design Principle            | Implementation Example                                        |
| --------------------------- | ------------------------------------------------------------- |
| **Preventive transparency** | Built-in network self-test and status dashboard.              |
| **Empower operators**       | Diagnostic shortcuts to reduce ticket load.                   |
| **Traceable changes**       | Configuration change log visible to IT.                       |
| **Fail-safe defaults**      | Auto-alert if whitelisting or ports fail before mobilisation. |

---

## 8. Behavioral Patterns Across Roles

| **Dimension**                            | **Shared Behavior**                                      | **Design Consideration**                                 |
| ---------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| **Reliance on manual verification**      | All roles distrust automation without transparency.      | Provide verifiable system feedback (“verified logging”). |
| **Need for situational awareness**       | Surveyor ↔ Senior ↔ PEC require tiered awareness levels. | Design modular visibility layers by role.                |
| **Parallel workflows**                   | Multiple missions and systems managed concurrently.      | Multi-mission workspaces and alert prioritization.       |
| **Dependence on shared logs**            | Collaboration hinges on event traceability.              | Centralized Online Log with structured event types.      |
| **Cognitive fatigue from tool overload** | Especially for operators and seniors.                    | Streamline interfaces, use persistent layouts.           |

---

## 9. Summary of Role-Driven Design Principles

1. **Build confidence through feedback** – Show what’s happening and why.
2. **Design for mental models** – Reflect how users think: by line, mission, and state.
3. **Support supervision without interruption** – Allow assistance without loss of control.
4. **Encourage consistency through structure** – Use templates and auto-checks to enforce standardization.
5. **Scale through modularity** – Support multiple missions, roles, and devices seamlessly.

---

## 10. Canonical Sources

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* `2.1.OI_SMP_Full_UX_Research.md`
* `Underwater Survey Operations – Task Structure`

---

**End of Document**
*“Every role sees the system differently — SMP must make those views align without friction.”*
