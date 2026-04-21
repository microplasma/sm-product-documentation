---
doc_id: PFD.02
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [product-strategy, ois, design, operations, transformation]
---

# PFD.02 - Product Strategy Overview

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft

---

## 1. Purpose

This document defines the **strategic intent** of OI Survey (OIS), describing how it should deliver operational, technological, and experiential transformation across Ocean Infinity's survey operations.

It translates OIS's vision into a strategy grounded in a clearer product model: **OI Survey as a unified operational ecosystem** expressed through distinct but connected surfaces, not as one flat application shell.

---

## 2. Strategic Context

### 2.1 Industry Transformation

The marine survey industry is shifting from vessel-based execution to distributed, remote, and increasingly autonomous workflows. Ocean Infinity's operating model requires better mission-time clarity, stronger traceability, and a credible cross-mission operating model.

OIS should support that transition by reducing fragmentation across survey work while preserving the operational nuance of different tasks, systems, and specialist workflows.

### 2.2 The Strategic Opportunity

Surveyors currently manage complex toolchains across multiple systems and displays, leading to inefficiency, re-checking, and fatigue. OIS's strategic opportunity is to:

* **reduce operational complexity**
* **improve mission-level decision quality and intervention confidence**
* **strengthen traceability and handover continuity**
* **separate decision, control, evidence, and service concerns more clearly**
* **develop cross-mission and future multi-mission work as part of the same evolving operating model**

---

## 3. Strategic Objectives

| **Objective** | **Goal** | **Outcome** |
| --- | --- | --- |
| **1. Mission-Level Clarity** | Give surveyors a dependable operating model for the active mission. | Faster understanding of state, issue, and next safe action. |
| **2. Operational Efficiency** | Simplify workflows and reduce manual intervention across mission-time surfaces. | Faster mobilization, fewer tool switches, reduced procedural overhead. |
| **3. Situational Awareness** | Improve visibility across systems, evidence, health, and quality. | Earlier anomaly detection and better recovery decisions. |
| **4. Traceable Collaboration** | Enable auditable distributed teamwork and stronger handovers. | Better continuity across shifts, roles, and interventions. |
| **5. Scalable Product Structure** | Build a product model that can grow across mission-level and cross-mission workflows together. | Strong product coherence with broader operational range. |

---

## 4. Strategic Pillars

| **Pillar** | **Focus** | **Strategic Intent** |
| --- | --- | --- |
| **Command & Control** | Safe mission-time action and recovery. | Place operational intervention in the right surfaces, especially Systems inside Mission Deck. |
| **Active Monitoring** | Real-time data, health, and QC interpretation. | Strengthen evidence and quality understanding through Mission Overview and Data Monitor capabilities. |
| **Collaboration & Traceability** | Shared operations and historical continuity. | Make Online Log and related traceability services part of the operating model, not administrative add-ons. |
| **Scalability & Resilience** | Strong mission-level and cross-mission ecosystem growth. | Expand toward broader multi-mission support without treating cross-mission awareness as a distant layer. |

---

## 5. Strategic Approach

### 5.1 Design Strategy

* **Unified Ecosystem:** Treat OI Survey as one operational ecosystem expressed through coordinated surfaces, services, and subsystems.
* **Parallel Mission and Cross-Mission Development:** Build Mission Overview and Multi-Mission Context together as related layers of the same attention model.
* **Surface-Based Product Model:** Treat Mission Overview, Systems, Online Log, Data Monitor, and Multi-Mission Context as purpose-built parts of one ecosystem.
* **Evidence-Backed Intervention:** Keep operational action close to the evidence needed for confidence.
* **Traceable Workflows:** Ensure actions, changes, and observations contribute to a defensible narrative.
* **Validated Scale:** Preserve multi-mission as a strategic direction without forcing it to dominate near-term design decisions.

### 5.2 Technology Strategy

* **Mission-Oriented State Handling:** Maintain coherent mission context across connected surfaces and services.
* **Shared Service Backbone:** Treat logging, configuration governance, and synchronization as cross-cutting product infrastructure.
* **RBAC Enforcement:** Make role boundaries and authority visible where operationally necessary.
* **Evidence and Monitoring Extensibility:** Allow Data Monitor capabilities to mature incrementally rather than forcing one early monolith.
* **Interoperability:** Abstract heterogeneous acquisition, navigation, telemetry, and specialist tooling into product-level operational concepts.

### 5.3 Operational Strategy

* **Remote-First Collaboration:** Support distributed work between offshore, onshore, and specialist roles.
* **Incremental Adoption:** Improve mission-time work without requiring all external dependencies to be absorbed immediately.
* **Operational Trust:** Reduce manual re-checking by making readiness, impact, and traceability more credible.
* **Integrated Cross-Mission Track:** Continue developing Multi-Mission Context alongside mission-level surfaces so the two models inform each other.

---

## 6. Roadmap Framework

The following roadmap is **indicative only** and should be validated against operator research, workshop priorities, and prototype maturity.

| **Phase** | **Focus** | **Indicative Milestones** |
| --- | --- | --- |
| **Phase 1 - Core Operating Ecosystem** | Establish the primary mission-level and cross-mission foundations. | Mission Deck structure, Mission Overview, Systems, Online Log, package-level Data Monitor framing, Multi-Mission Context direction. |
| **Phase 2 - Connected Operational Surfaces** | Strengthen evidence, configuration, specialist workflow, and aggregation connections. | Expanded Data Monitor capabilities, stronger configuration governance, clearer service integration, stronger Multi-Mission Context integration. |
| **Phase 3 - Broader Operational Scale** | Mature cross-mission awareness and validated concurrency patterns. | Multi-Mission Context growth, prioritization patterns, future multi-mission operating support where validated. |

**Note:** Final roadmap structure will be derived from feature prioritization and stakeholder validation sessions.

---

## 7. Success Criteria

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Efficiency** | Mobilization time reduction | >= 30% |
| **Reliability** | Mean fault recovery time | <= 10 min |
| **Situational Awareness** | Time to detect anomaly | <= 2 min |
| **User Experience** | Operator satisfaction | >= 90% positive |
| **Traceability** | Logged actions automatically captured | 100% |
| **Scalability** | Multi-mission support | Evolving target, developed alongside mission-level clarity |

---

## 8. Strategic Outcomes

1. **Clearer Mission-Time Operations:** Surveyors can understand and act inside one coherent active-mission package.
2. **Stronger Operational Trust:** Readiness, evidence, and traceability reduce re-checking and ambiguity.
3. **Better Service Backbone:** Online Log and related shared services support live use, handover, and downstream reporting.
4. **More Credible Product Structure:** Different operational questions are served by the right surface rather than one overloaded workspace.
5. **Scalable Direction:** The product can grow toward cross-mission and multi-mission modes while keeping mission-level and cross-mission models connected.

---

**End of Document**
*"One ecosystem, clarified through connected mission-level and cross-mission surfaces."*
