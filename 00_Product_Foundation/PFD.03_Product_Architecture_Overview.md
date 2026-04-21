---
doc_id: PFD.03
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [architecture, ois, system-design, remote-operations, multi-mission]
---

# PFD.03 - Product Architecture Overview

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft - Surface Model Alignment

---

## 1. Purpose

This document defines the **conceptual product architecture** of OI Survey (OIS).  
It describes how the product should be structured as a unified operational ecosystem expressed through connected operational surfaces that support mission-time survey work, traceability, evidence interpretation, and broader cross-mission awareness.

The architecture is intended to:

* simplify operational workflows and reduce tool fragmentation
* give the active mission a stronger, clearer operating model
* separate decision, control, evidence, and traceability responsibilities more cleanly
* support cross-mission and multi-mission workflows as part of the same evolving ecosystem

---

## 2. Architectural Principles

| **Principle** | **Description** |
| --- | --- |
| **Modularity** | OI Survey should behave as a unified ecosystem of connected surfaces and services rather than one flat application shell. |
| **Mission-Centric Design** | The active mission remains the primary operational context for decision, control, evidence, and traceability. |
| **Surface-Specific Purpose** | Different operational questions should be answered by the right surface: overview, control, evidence, or cross-mission awareness. |
| **Reduced Complexity** | The architecture should reduce tool-switching and context reconstruction, especially inside single-mission workflows. |
| **Traceable State Management** | Actions, events, configuration changes, and observations should remain linked to mission context and reviewable later. |
| **Distributed Collaboration** | Multiple users and services should be able to contribute safely without collapsing authority boundaries. |
| **Scalable Architecture** | The product should expand across mission-level and cross-mission capability together, with future validated concurrency patterns building on both. |
| **Interoperability** | OIS should connect heterogeneous acquisition, navigation, telemetry, and specialist systems through coherent product abstractions. |

---

## 3. Conceptual Overview

OI Survey functions as a **unified operational ecosystem composed of connected surfaces and shared services**. The architecture should preserve a clear distinction between:

* the **active mission operating package**
* **evidence and QC capabilities**
* **traceability and service backbones**
* **cross-mission awareness**

This means the architecture should not treat every operational need as a feature inside one workspace. Instead, it should organize work across purpose-built surfaces that remain mission-aware and operationally coherent.

---

## 4. Core System Concepts

### 4.1 Mission Deck

**Mission Deck** is the mission-time container for the active mission. It is not one flat cockpit. It should coordinate the surfaces that matter most while a surveyor is working inside a single mission context.

Mission Deck contains, at minimum:

* **Mission Overview** as the default decision surface
* **Systems** as the deep operational and control surface

Mission Deck should help the surveyor understand the mission, move toward intervention safely, and stay oriented while related surfaces such as Online Log or Data Monitor are in use.

### 4.2 Mission Overview

**Mission Overview** is the primary decision surface for the active mission.

Its role is to answer:

* what is happening in this mission right now
* what needs attention now
* what issue or readiness concern is emerging
* what the next sensible action likely is

It should summarize mission posture, attention, and issue context without becoming the deep control surface itself.

### 4.3 Systems

**Systems** is the deep operational and control surface inside Mission Deck.

Its role is to support:

* selected-system understanding
* direct operational action and recovery
* system-specific configuration and dependency review
* mission-time investigation when action needs deeper operational context

### 4.4 Online Log

**Online Log** is the traceability service and operational record for the mission package.

It should:

* capture automated and user-generated events
* preserve the mission narrative across actions, anomalies, and handovers
* support downstream reporting and accountability

### 4.5 Data Monitor

**Data Monitor** is the package-level evidence and QC capability family.

It should cover:

* evidence viewing and monitoring
* stream-oriented interpretation
* QC review and comparison
* evolving forms such as stream viewers, QC surfaces, and detached evidence views

The current product direction should treat Data Monitor as the package-level capability name, even where implementation still appears through multiple specialized evidence surfaces rather than one consolidated module.

### 4.6 Multi-Mission Context

**Multi-Mission Context** is the cross-mission awareness surface.

Its role is to:

* show relative mission posture
* help prioritize where attention should shift
* support broader supervision patterns

It should remain parallel to the active mission package rather than becoming a detached future layer. As Mission Overview matures, Multi-Mission Context should progressively recombine the most important mission-level signals across several missions.

---

## 5. Module Architecture

| **Product Element** | **Primary Purpose** | **Architectural Role** |
| --- | --- | --- |
| **Mission Deck** | Active mission-time container | Coordinates the mission package and keeps active context coherent within the broader ecosystem. |
| **Mission Overview** | Primary decision surface | Summarizes posture, issue state, and next attention target for the active mission. |
| **Systems** | Deep operational/control surface | Hosts selected-system intervention, recovery, configuration, and dependency understanding. |
| **Online Log** | Traceability service | Preserves operational narrative, handover continuity, and downstream reporting support. |
| **Data Monitor** | Evidence and QC capability family | Supports evidence interpretation, monitoring, comparison, and QC-focused review. |
| **Multi-Mission Context** | Cross-mission awareness surface | Supports prioritization and safe attention shifting across missions by aggregating the most important mission-level signals. |
| **Specialized Subsystems** | Domain-specific workflows such as Hydrosens | Maintain deep workflow integrity while remaining connected to the broader package. |

---

## 6. Data and State Management

OIS should maintain coherent mission context across connected surfaces and services.

| **Function** | **Description** |
| --- | --- |
| **Mission Context Propagation** | The active mission should remain identifiable and stable across Mission Deck, Online Log, Data Monitor, and related workflows. |
| **State Separation** | Overview state, deep system state, evidence state, and cross-mission state should remain distinct enough to avoid confusion. |
| **Event Logging** | Actions, alerts, annotations, and service events should be captured with timestamps and attribution. |
| **Resilient Synchronization** | Surfaces and services should tolerate degraded connectivity without losing operational continuity. |
| **Cross-Surface Linking** | Users should be able to move between decision, control, evidence, and traceability without reconstructing context manually. |

---

## 7. Collaboration and Access Control

The collaboration model should support safe distributed work across surfaces and services.

* **Role-Based Access (RBAC):** Defines who can view, intervene, validate, or configure.
* **Shared Mission Context:** Users and services should operate against the same mission understanding.
* **Acknowledgement and Traceability:** Higher-consequence actions should remain legible and attributable.
* **Cross-Mission Awareness Without Overreach:** Multi-Mission Context should support supervision without replacing mission-time operating clarity.

| **Role** | **Capabilities** |
| --- | --- |
| **Surveyor / Operator** | Uses Mission Overview and Systems to supervise and intervene in the active mission. |
| **Senior Surveyor** | Validates setup, supports recovery, interprets evidence, and helps govern higher-consequence decisions. |
| **PEC / Supervisor** | Uses cross-mission and narrative surfaces for coordination and progress confidence. |
| **System Admin / Support** | Supports configuration, RBAC, and integration integrity across the package. |

---

## 8. Integration Model

OIS integrates with existing acquisition, navigation, telemetry, and specialist systems.  
These integrations should be abstracted into the product architecture without pretending every dependency is already absorbed into one native surface.

* **Upstream Systems:** Sensor data, navigation context, telemetry, environmental inputs.
* **Shared Services:** Logging, configuration governance, synchronization, and traceability.
* **Specialist Dependencies:** Hydrosens, Qinsy context, and other domain tools that remain operationally essential.

---

## 9. Scalability Framework

OIS should scale across mission-level and cross-mission operation together.

| **Level** | **Scaling Function** |
| --- | --- |
| **Mission-Level** | Strong active-mission package with clear internal surface roles. |
| **Cross-Mission Level** | Multi-Mission Context supports prioritization and attention management across assigned missions using a subset of the most important mission-level signals. |
| **Fleet-Level** | Shared services and broader operational views can support distributed oversight over time. |
| **Future Multi-Mission Level** | Operator-level multi-mission work remains a strategic future capability subject to validation. |

This framework preserves the path toward scale without turning cross-mission capability into a disconnected later-stage concern.

---

## 10. Security and Compliance Principles

* **RBAC Enforcement:** Role-based authentication and authority boundaries across surfaces and services.
* **Audit Trail:** Immutable or defensible logging of operational and mission events.
* **Fail-Safe Actions:** Validation of higher-consequence actions before execution.
* **Secure Communications:** Protected mission data and service channels.
* **Data Integrity:** Strong linkage between action, evidence, configuration, and traceability.

---

## 11. Evolution Path

> **Note:** The following is an indicative capability progression, not a committed roadmap.

| **Capability Area** | **Initial Focus** | **Next Maturity Step** | **Future (Subject to Validation)** |
| --- | --- | --- | --- |
| **Mission Package** | Clear Mission Deck structure with Mission Overview and Systems | Stronger configuration and subsystem integration | Broader adaptive mission orchestration |
| **Evidence and QC** | Data Monitor expressed through stream views, QC surfaces, and detached evidence | Clearer package-level consolidation and cross-surface workflows | Richer cross-sensor interpretation and automation |
| **Traceability** | Online Log as service backbone | Deeper automation, reporting, and service integrations | Analytics and operational intelligence on top of traceability data |
| **Cross-Mission Awareness** | Parallel Multi-Mission Context development informed by mission-level signals | Stronger prioritization and supervisory patterns | Validated operator-level multi-mission support |

| **Phase** | **Description** | **Goal** |
| --- | --- | --- |
| **Phase 1 (Core Operating Ecosystem)** | Strong active-mission structure across Mission Deck, Mission Overview, Systems, Online Log, and Multi-Mission Context direction. | Establish credible ecosystem clarity across mission-level and cross-mission work. |
| **Phase 2 (Connected Surfaces)** | Expand Data Monitor, subsystem links, configuration/service coherence, and cross-mission aggregation logic. | Strengthen evidence and operational continuity. |
| **Phase 3 (Cross-Mission Scale)** | Mature Multi-Mission Context and future concurrency patterns where validated. | Extend operational reach without losing ecosystem coherence. |

---

## 12. Summary

The OIS architecture defines a **modular operational package** designed to:

* strengthen the active mission operating model
* separate overview, control, evidence, and cross-mission responsibilities clearly
* preserve traceability and service coherence across the package
* support cross-mission and multi-mission capability as part of one evolving ecosystem

---

**End of Document**  
*"One ecosystem, clarified through connected surfaces rather than one overloaded workspace."*
