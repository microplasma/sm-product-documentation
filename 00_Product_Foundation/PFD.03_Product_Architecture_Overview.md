---
doc_id: PFD.03
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [architecture, smp, system-design, remote-operations, multi-mission]
---

# PFD.03 – Product Architecture Overview

<!--
Changes made:
1. Added standardized front-matter for alignment with documentation format.
2. Updated H1 heading for ID consistency.
3. Fixed a minor table formatting issue before the roadmap phases.
4. All body text remains verbatim.
-->

*(Originally titled “Ocean Infinity – Survey Management Platform (SMP)”)*

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** SMP Product Design & Strategy  
**Status:** Updated Draft – Reflecting Operator-Level Multi-Mission Capability

---

## 1. Purpose

This document defines the **conceptual architecture** of the Ocean Infinity Survey Management Platform (SMP).  
It describes how the platform is structured to deliver safe, efficient, and scalable multi-mission marine survey operations, emphasizing the ability for **surveyors to manage multiple missions simultaneously** without losing situational awareness or operational safety.

SMP aims to:

* Simplify operational workflows and reduce tool fragmentation.  
* Support remote, multi-user, and **multi-mission operations at the operator level**.  
* Maintain integrity, traceability, and safety of all survey control actions.  
* Enable collaborative assistance and support across distributed teams.

---

## 2. Architectural Principles

| **Principle**                     | **Description**                                                                                                                                                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modularity**                    | Each SMP capability exists as an independent module. Modules can evolve or be replaced without redesigning the entire system.                                                                                        |
| **Mission-Centric Design**        | Operations revolve around "missions" — virtualized representations of ongoing surveys. Every action, log, and configuration is contextualized within a mission workspace.                                            |
| **Reduced Complexity**            | SMP simplifies operators’ interaction with complex systems by integrating key workflows, minimizing tool-switching, and ensuring consistency across functions.                                                       |
| **Concurrent Mission Operations** | Individual surveyors can safely manage, monitor, and control multiple active missions at once. The system dynamically manages focus, alerts, and data synchronization to preserve operational safety and efficiency. |
| **Distributed Collaboration**     | Multiple users (onboard, onshore, remote) can safely observe, assist, or command without conflict. Access and actions are governed by role-based permissions.                                                        |
| **Traceable State Management**    | All actions, configurations, and events are automatically recorded — forming a continuous operational record.                                                                                                        |
| **Scalable Architecture**         | The system expands from single-vessel control to multi-mission fleet operations through modular orchestration and scalable data management.                                                                          |
| **Interoperability**              | SMP connects seamlessly with acquisition, navigation, and IT systems through defined data and API interfaces.                                                                                                        |

---

## 3. Conceptual Overview

SMP functions as an **orchestration layer** connecting people, systems, and data across multiple concurrent survey missions. It reduces operational complexity while ensuring every mission remains contextually distinct, safe, and traceable.

The architecture enables:

* Simultaneous mission sessions per operator.  
* Synchronized data and alerts across missions.  
* Context preservation when switching between missions.  
* Peer or supervisor assistance without workflow disruption.

---

## 4. Core System Concepts

### 4.1 Mission Deck

The **Mission Deck** is the operator’s live workspace environment. Each operator can run multiple mission decks in parallel, switching between them seamlessly.

* Each deck represents a single mission context: controls, logs, and monitoring views.  
* Operators can manage several missions concurrently within the same interface session.  
* Alerts and task queues dynamically triage focus between missions.  
* Assistance from peers or seniors can be initiated contextually (view-only or shared control modes).  
* Each mission deck maintains independent command safety and data isolation.

**Outcome:** One operator can maintain operational volume previously requiring multiple personnel.

---

### 4.2 Triage Hub

The **Triage Hub** enables situational overview and support across active missions:

* Aggregates mission states, alerts, and health scores.  
* Provides real-time prioritization of missions needing attention.  
* Allows supervisors or peers to assist in a mission temporarily without interrupting others.  
* Forms the backbone for distributed operations and workload balancing.

---

### 4.3 Online Log

The **Online Log** captures every system and user event across all active missions:

* Consolidates mission event data in real time.  
* Maintains a single source of truth for operational review, audit, and handover.  
* Supports mission switching without losing event continuity.  
* Enables traceability across parallel operations.

---

## 5. Module Architecture

Each SMP **module** is independent but interoperable across missions.  
Modules subscribe to mission contexts and can operate concurrently for multiple missions within the same user session.

| **Module**                      | **Primary Purpose**                                                      | **Multi-Mission Role**                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Sensor Control**              | Execute ON/OFF, restart, and configuration commands for onboard sensors. | Manages multiple sensor sets per mission context.                                                                      |
| **Output Monitoring**           | Visualize live sensor streams and QC metrics.                            | Displays parallel data streams across active missions.                                                                 |
| **Navigation Display**          | Track vessel position, planned lines, and coverage completion.           | Multi-context navigation visualization with safe focus transitions.                                                    |
| **Online Log**                  | Capture, annotate, and search all operational events (system + human).   | Maintains continuous, per-mission audit trails across concurrent missions; supports auto-logging from commands/alerts. |
| **File Monitoring**             | Verify data creation, integrity, and sync status.                        | Cross-mission file state monitoring and transfer validation.                                                           |
| **Diagnostics & Health**        | Run automated system checks and highlight degraded connections.          | Supports aggregated fleet or mission-level health overview.                                                            |
| **Configuration Manager**       | Manage mission templates, locks, and rollback functions.                 | Enables shared template application across missions.                                                                   |
| **Alerts & QC**                 | Surface deviations, thresholds, and critical events.                     | Aggregates alert streams and highlights priority missions.                                                             |
| **RBAC & Collaboration Engine** | Enforce permissions and multi-user session control.                      | Supports peer assistance, view-only joins, and escalation workflows.                                                   |

---

## 6. Data and State Management

SMP maintains **live, synchronized mission states** across multiple concurrent sessions using a publish/subscribe (Pub/Sub) architecture.

| **Function**                   | **Description**                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Mission Context Containers** | Each mission operates in its own isolated container, with state synchronized to subscribed modules. |
| **Multi-Context State Engine** | Operators can maintain multiple mission states concurrently without conflict or data loss.          |
| **Event Logging**              | All mission actions and state transitions are captured with timestamps and user attribution.        |
| **Resilient Synchronization**  | Network or bandwidth interruptions trigger local caching and auto-reconciliation once reconnected.  |
| **Cross-Mission Event Bus**    | Centralized event routing enables prioritization, triage, and alert focus across missions.          |

---

## 7. Collaboration and Access Control

The collaboration framework supports **safe, shared operations** between surveyors and supervisors across multiple active missions.

* **Role-Based Access (RBAC):** Defines authority levels for command, view, and assistance.  
* **Session Sharing:** Another surveyor or senior can join a mission context without seizing control.  
* **Acknowledgement Loop:** All control actions follow Send → Ack → Working → Done confirmation.  
* **Focus Retention:** User interface surfaces only relevant missions or alerts requiring attention.

| **Role**                | **Capabilities**                                                                    |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Surveyor / Operator** | Manage multiple missions simultaneously, execute commands, monitor QC and alerts.   |
| **Senior Surveyor**     | Oversee and support surveyors, assist on-demand without disrupting mission control. |
| **PEC / Supervisor**    | Triage and allocate missions, monitor overall system health.                        |
| **System Admin**        | Manage configuration, RBAC permissions, and integrations.                           |

---

## 8. Integration Model

SMP integrates with existing acquisition, navigation, and IT systems.  
All integrations are abstracted through a **unified API Gateway**, supporting simultaneous mission data exchange.

* **Upstream Systems:** Sensor data acquisition, navigation, positioning, telemetry.  
* **Downstream Systems:** Log archives, QA pipelines, performance reporting.  
* **Inter-Mission Interfaces:** Data sharing, diagnostic sync, and template distribution.

---

## 9. Scalability Framework

SMP scales **horizontally across missions and operators**.

| **Level**          | **Scaling Function**                                                                |
| ------------------ | ----------------------------------------------------------------------------------- |
| **Operator-Level** | Multiple concurrent mission contexts per user session.                              |
| **Mission-Level**  | Independent mission containers executed in parallel.                                |
| **Fleet-Level**    | Aggregation of mission health, data, and alerts across all active operations.       |
| **System-Level**   | Load-balanced service architecture distributing mission orchestration across nodes. |

This architecture supports the operational goal of maintaining output volume with fewer personnel — enabling higher efficiency per operator while preserving safety and control integrity.

---

## 10. Security and Compliance Principles

* **RBAC Enforcement:** Role-based authentication for all commands and session joins.  
* **Audit Trail:** Immutable logging of all control and mission events.  
* **Fail-Safe Commands:** Validation of all actions before execution.  
* **Secure Communications:** Encrypted mission data channels.  
* **Data Integrity:** Automated verification during sync and rollback.

---

## 11. Evolution Path

> **Note:** The following is an **indicative capability progression**, not a committed roadmap. Final phasing will be validated against the **workshop feature priorities** (Command & Control and Active Monitoring short-/long-term lists) and subsequent stakeholder reviews.

| **Capability Area**              | **Initial Focus**                                                                        | **Next Maturity Step**                                              | **Future (Subject to Validation)**                               |
| -------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Command & Control**            | Core sensor ON/OFF/Restart, start/stop logging, config templates, online log integration | Ack Loop for settings, configuration lock/permissions, rollback     | Auto-diagnostics routines, safe auto-actions based on state      |
| **Active Monitoring**            | Live streams, status/health indicators, configurable thresholds, deviation indicators    | Alert hierarchy & triage across missions, parameter auto-validation | Cross-sensor correlation, quality scoring, color-coded QC layers |
| **Collaboration & Traceability** | Multi-user session join (view/assist), unified Online Log                                | Changelog journal, clearer role-based write permissions             | Distributed assistance patterns, mission handover automation     |
| **Scalability & Resilience**     | Single mission container per operator session                                            | Operator-level **multi-mission concurrency** with triage            | Fleet-wide orchestration and workload balancing                  |

**Roadmap Status:** *TBD / Not yet validated*. A formal roadmap will be created after consolidating workshop priorities into a Feature Prioritization Matrix and running validation sessions with operators and supervisors.

| **Phase** | **Description** | **Goal** |
|------------|----------------|----------|
| **Phase 1 (MVP)** | Single mission per operator, unified control and monitoring. | Establish mission container model, foundational modules. |
| **Phase 2 (Concurrent Operations)** | Multi-mission concurrency for operators, collaboration framework. | Multi-context orchestration and alert triage. |
| **Phase 3 (Intelligent Operations)** | Predictive diagnostics and automated prioritization. | Adaptive triage, AI-assisted task routing. |

---

## 12. Summary

The SMP architecture defines a **modular, mission-oriented, and scalable system** designed to:

* Simplify operations and reduce complexity.  
* Allow individual surveyors to manage multiple missions simultaneously.  
* Enable collaborative, distributed assistance without loss of control.  
* Ensure traceability, safety, and operational resilience across missions.

---

**End of Document**  
*"Designed for operational efficiency – empowering surveyors to manage more, with less complexity."*
