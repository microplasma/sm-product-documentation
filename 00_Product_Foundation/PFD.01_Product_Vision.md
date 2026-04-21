---
doc_id: PFD.01
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [product-vision, ois, remote-operations, design-principles]
---

# PFD.01 - Product Vision

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** Product Design & Strategy - OIS Core Team  
**Status:** Updated Draft

---

## 1. Vision Statement

> **OI Survey (OIS)** enables Ocean Infinity's teams to manage, monitor, and control complex marine survey operations through a unified operational ecosystem of connected surfaces and services - with confidence, safety, and efficiency.

OIS is intended to transform how offshore, onshore, and remote surveyors collaborate. It aims to replace fragmented, tool-heavy workflows with a **unified operational ecosystem** that connects data, systems, and people through real-time awareness, safer intervention, and defensible traceability.

Current product direction develops **mission-level clarity and multi-mission awareness in parallel**. Mission Overview and Multi-Mission Context should reinforce each other: the first clarifies what matters inside one mission, while the second should progressively combine the most important mission-level signals across several missions.

---

## 2. Purpose

Modern survey operations span multiple vessels, remote hubs, and autonomous assets.  
OIS is designed to:

* reduce operational fragmentation across mission-time work
* give surveyors dependable mission-level understanding and action support
* improve confidence in data integrity, operational safety, and traceability
* connect decision, control, evidence, and logging surfaces coherently
* support cross-mission and multi-mission workflows as part of the evolving operating model

---

## 3. Strategic Context

Marine survey operations are transitioning from vessel-based execution to distributed, remote, and increasingly autonomous operating models.  
OIS sits at the center of this transition as a product direction that should reduce operational complexity without pretending every workflow belongs inside one flat application shell.

The current product direction frames OIS as a **unified operational ecosystem** structured through connected operational surfaces, with mission-level and cross-mission models evolving together rather than as strictly separate time horizons.

| Trend | OIS Response |
| --- | --- |
| Fragmented workflows and high operator load | Unified operational ecosystem with clearer boundary between decision, control, evidence, and traceability |
| Need for stronger mission-time confidence | Mission Overview as the primary decision surface for the active mission |
| Complex system recovery and control | Systems as the deep operational and control surface |
| Manual logging and weak handovers | Online Log as a traceability backbone rather than an optional side feature |
| Growing need for broader mission oversight | Multi-Mission Context as the cross-mission surface that recombines the most important mission-level signals |

---

## 4. Product Definition

### 4.1 What OIS Is

A **unified operational ecosystem** for remote and distributed survey work, structured through connected mission-time surfaces, shared services, and specialist subsystems rather than a single undifferentiated application.

### 4.2 What OIS Is Not

* Not a replacement for acquisition or navigation software.
* Not a reporting platform, though it supports reporting through traceability and exportable records.
* Not a long-term data repository - it coordinates operational truth, intervention, evidence, and traceability during survey work.

### 4.3 Core Role

> **To help survey teams understand what matters now, act safely in the active mission, interpret evidence with confidence, and preserve a trustworthy operational record.**

---

## 5. Core Vision Pillars

| **Pillar** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Command & Control** | Support safe operational action through the right mission-time surfaces. | Faster, clearer intervention with stronger consequence visibility. |
| **Active Monitoring** | Make data quality, system health, and evidence easier to interpret. | Earlier detection of degraded conditions and stronger survey confidence. |
| **Collaboration & Traceability** | Preserve a defensible operational narrative across shifts, roles, and services. | Better handovers, clearer accountability, fewer context gaps. |
| **Scalability & Resilience** | Support growth in both mission-level and cross-mission operating models. | A credible path toward multi-mission work without reducing the value of either layer. |

---

## 6. Guiding Design Principles

| **Principle** | **Description** |
| --- | --- |
| **Mission-Level Clarity With Cross-Mission Continuity** | The active mission should be easy to understand, and that clarity should inform how broader cross-mission awareness is built. |
| **Surface-Specific Purpose** | Different operational questions should be served by the right surface, not collapsed into one flat workspace. |
| **Evidence Supports Intervention** | Control actions should stay connected to the evidence needed to judge them safely. |
| **Traceability Is Product-Critical** | Logging, event capture, and narrative continuity are part of the operating model. |
| **Role-Based Trust** | Permissions and authority should protect live work while preserving collaboration. |
| **System Memory** | Every meaningful action, configuration, and event should remain reviewable and reconstructable. |

---

## 7. Success Metrics

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Operational Efficiency** | Mobilization time reduction | >= 30% |
| **Situational Awareness** | Mean time to detect anomaly | <= 2 minutes |
| **Reliability** | Fault recovery time | <= 10 minutes |
| **User Experience** | Operator satisfaction | >= 90% positive |
| **Traceability** | Automated event capture | 100% |
| **Scalability** | Safe multi-mission capability | Evolving target, developed in parallel with mission-level operating clarity |

---

## 8. Roadmap Snapshot

| **Phase** | **Focus** | **Key Deliverables** |
| --- | --- | --- |
| **Phase 1 (Core Operating Ecosystem)** | Strong mission-level and cross-mission foundations | Mission Deck, Mission Overview, Systems, Online Log, Multi-Mission Context direction, early Data Monitor direction |
| **Phase 2 (Connected Operational Surfaces)** | Stronger evidence, configuration, service, and aggregation models | Expanded Data Monitor capability, configuration governance, deeper traceability and stronger Multi-Mission Context integration |
| **Phase 3 (Broader Operational Scale)** | More mature supervisory and validated concurrency patterns | Multi-Mission Context maturity, cross-mission prioritization, future multi-mission operating support where validated |

**Note:** Roadmap phases are indicative and subject to validation through feature prioritization and operational review.

---

**End of Document**  
*"One operational ecosystem, with mission-level and cross-mission confidence evolving together."*
