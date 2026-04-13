---
doc_id: PFD.02
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [product-strategy, ois, design, operations, transformation]
---

# PFD.02 - Product Strategy Overview

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft

---

## 1. Purpose

This document defines the **strategic intent** of OI Survey (OIS), describing how it delivers operational, technological, and experiential transformation across Ocean Infinity's survey operations.

It translates OIS's **vision** ("to unify control, monitoring, and collaboration across survey operations") into **actionable strategic objectives** and **guiding principles**.

---

## 2. Strategic Context

### 2.1 Industry Transformation

The marine survey industry is shifting from on-vessel operations to distributed, remote, and increasingly autonomous workflows. Ocean Infinity's operational model requires scalability, efficiency, and resilience to maintain mission throughput with fewer personnel.

OIS is intended to enable this model - consolidating fragmented tools into a coherent environment that supports multi-user work and future **multi-mission operations at the operator level** where safely validated.

### 2.2 The Strategic Opportunity

Surveyors currently manage complex toolchains across multiple systems and displays, leading to inefficiency and fatigue. OIS's strategic opportunity is to:

* **Reduce operational complexity.**
* **Enable surveyors to manage multiple concurrent missions safely and effectively where validated.**
* **Preserve situational awareness** through unified control and monitoring.
* **Allow seamless peer assistance and supervisory support** without interrupting active missions.

---

## 3. Strategic Objectives

| **Objective** | **Goal** | **Outcome** |
| ------------- | -------- | ----------- |
| **1. Operational Efficiency** | Simplify workflows and reduce manual intervention. | Faster mobilization and reduced crew size. |
| **2. Multi-Mission Readiness** | Allow individual operators to manage multiple concurrent missions where it is safe and operationally credible. | Maintain operational throughput with fewer personnel. |
| **3. Situational Awareness** | Unify visibility across systems, missions, and roles. | Early anomaly detection and faster recovery. |
| **4. Traceable Collaboration** | Enable safe, auditable, and distributed teamwork. | Seamless assistance and handovers. |
| **5. Scalable Architecture** | Ensure the system can expand across fleet and shore nodes. | Sustained efficiency at scale. |

---

## 4. Strategic Pillars

| **Pillar** | **Focus** | **Strategic Intent** |
| ---------- | --------- | -------------------- |
| **Command & Control** | Safe execution of commands and configurations. | Standardize and automate operational workflows where direct control is appropriate. |
| **Active Monitoring** | Real-time data, system, and QC visibility. | Deliver unified awareness across missions with intelligent triage. |
| **Collaboration & Traceability** | Shared operations and historical transparency. | Introduce multi-user assistance, shared logs, and change tracking. |
| **Scalability & Resilience** | Multi-mission and multi-user scalability. | Support operator-level concurrency and distributed fleet control as a future-state capability. |

---

## 5. Strategic Approach

### 5.1 Design Strategy

* **Reduced Operational Complexity:** Consolidate essential functions to reduce switching between tools.
* **Role-Based Workspaces:** Interfaces adapt to each user's function (Operator, Senior, PEC).
* **Multi-Mission Readiness:** Design for safe concurrent mission handling by individual surveyors where validated.
* **Collaborative Assistance:** Enable shared control and supervision without disruption.
* **Cognitive Efficiency:** Focus user attention through triage, priority alerts, and contextual visibility.

### 5.2 Technology Strategy

* **Mission Containerization:** Each mission runs in an isolated workspace with synchronized state.
* **Pub/Sub Data Model:** Live updates and non-blocking synchronization between modules.
* **RBAC Enforcement:** Command and view permissions controlled by roles and session context.
* **Diagnostic Automation:** Health checks and safe rollback capabilities.
* **Interoperability:** Abstract heterogeneous acquisition, navigation, and telemetry systems into a coherent operational layer.

### 5.3 Operational Strategy

* **Remote-First Model:** Designed for onshore and offshore collaboration.
* **Incremental Adoption:** OIS integrates progressively with existing workflows.
* **Standardization:** Configuration templates and predefined mission profiles reduce variance.
* **Data Integrity:** Automated event logging ensures traceability across missions.

---

## 6. Roadmap Framework

The following roadmap is **indicative only** and will be validated against **feature prioritization workshops** (Command & Control and Active Monitoring short-/long-term scopes).

| **Phase** | **Focus** | **Indicative Milestones** |
| --------- | --------- | ------------------------- |
| **Phase 1 - Core Operations** | Establish unified mission control and monitoring. | Mission Deck v1, Online Log integration, Sensor Control, QC Dashboard. |
| **Phase 2 - Collaboration & Concurrency** | Enable multi-user and multi-mission operation. | Multi-Mission Context, Ack Loop, Config Templates, operator-level multi-mission sessions where validated. |
| **Phase 3 - Intelligent Operations** | Introduce automation and predictive diagnostics. | AI Diagnostics, auto-triage, fleet orchestration. |

**Note:** Final roadmap structure will be derived from workshop validation sessions.

---

## 7. Success Criteria

| **Category** | **Metric** | **Target** |
| ------------ | ---------- | ---------- |
| **Efficiency** | Mobilization time reduction | >= 30% |
| **Operational Efficiency** | **Average concurrent missions per operator** | Target future state: >= 2 sustained safely |
| **Reliability** | Mean fault recovery time | <= 10 min |
| **Situational Awareness** | Time to detect anomaly | <= 2 min |
| **User Experience** | Operator satisfaction | >= 90% positive |
| **Traceability** | Logged actions automatically captured | 100% |

---

## 8. Strategic Outcomes

1. **Unified Operational Command:** Operators manage core mission actions and awareness through one platform layer.
2. **Operational Efficiency:** Multi-mission concurrency reduces crew needs while maintaining throughput where it can be introduced safely.
3. **Fleet-Level Awareness:** Supervisors triage and assist across distributed missions.
4. **Predictive Resilience:** Faults detected, logged, and triaged before impact.
5. **Cultural Transformation:** A shift toward distributed, data-driven, remote operations.

---

**End of Document**
*"From complexity to clarity - enabling every surveyor to manage more, safely and efficiently."*

