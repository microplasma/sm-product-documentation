---
doc_id: PDD.03.00
version: 0.1.0
last_updated: 2025-11-08
status: draft
owners: [design@survey-platform.io]
tags: [user-experience, ux-framework, design-system, multi-screen]
---

# 03_User_Experience_Framework

## Purpose
This document defines the **user experience framework** for the Survey Management Platform (SMP).  
It describes how users interact with the system across screens, how context flows between modules, and the principles guiding interface and interaction design.

The objective is to create a consistent, intuitive, and safe environment for operators managing complex, concurrent marine survey missions.

---

## Scope & Context
The SMP operates within a **multi-screen, multi-mission workspace**.  
It is designed for real-time survey environments where operators need to:
- Manage multiple active missions concurrently.  
- Switch context rapidly without losing situational awareness.  
- Interpret live data and respond to system health indicators quickly.  
- Collaborate with onshore teams through traceable, synchronized records.

The UX framework ensures a **common visual and behavioral language** across all screens and roles.

---

## Key Concepts / Framework

### 1. Multi-Screen Operational Concept

SMP is optimized for a **4×2 screen layout** typical of offshore survey desks.  
Each screen serves a defined operational purpose, minimizing overlap and maximizing information clarity.

| Screen | Function | Context |
|---------|-----------|----------|
| **1. Triage Hub** | Global mission overview, selection, and activation. | Cross-mission |
| **2. Mission Deck** | Primary control and monitoring surface for the selected mission. | Active mission |
| **3. Navigation / Reference** | Vessel positioning, heading, and reference systems. | Active mission |
| **4–5. Stream Viewer(s)** | Live data visualization and quality monitoring per sensor type. | Active mission |
| **6–7. Diagnostics / Configuration Tools** | Troubleshooting, validation, and configuration management. | Active mission |
| **8. Online Log** | Consolidated operational log and traceability record. | Cross-mission |

> Only the **Triage Hub** and **Online Log** are persistent across missions.  
> All other screens adapt dynamically to the currently active mission context.

---

### 2. Context Propagation Model

The SMP maintains a **single active mission context** at any time.  
When an operator selects a mission in the **Triage Hub**, the following occurs:

1. The **Mission Context** is broadcast to all mission-scoped windows.  
2. Each module (Mission Deck, Stream Viewer, Diagnostics) updates its data and state.  
3. The **Online Log** remains global but continues to tag all new entries with the current `MissionID`.  
4. Operators can confirm the active mission from any screen via a shared header component.

This ensures synchronized state across the multi-screen environment while preserving mission isolation and traceability.

---

### 3. Experience Pillars

| Pillar | Description | Example Application |
|--------|--------------|---------------------|
| **Situational Awareness** | Operators must understand the health and progress of all missions at a glance. | Global status banners, mission color coding, health badges. |
| **Cognitive Clarity** | Reduce information overload through structured layouts and minimal visual noise. | Grouping of controls by task; progressive disclosure of detail. |
| **Actionable Insight** | Information surfaces with context and recommended next steps. | Alerts include probable cause and suggested response. |
| **Consistency** | Controls, colors, and behavior remain uniform across modules. | Same command pattern for Start/Stop in Deck and Diagnostics. |
| **Safety by Design** | High-impact actions are confirmable and reversible. | Confirmation required for mission termination or config overwrite. |
| **Traceable Transparency** | Every visible change links to a logged event. | Log entries auto-generated from operator actions. |

---

## Functional or UX Details

### 4. Visual and Interaction Hierarchy

The SMP uses a **three-tier visual hierarchy**:

| Tier | Purpose | Components |
|------|----------|-------------|
| **Global Layer** | Always visible, provides orientation and mission status. | Top header (Mission ID, UTC clock, system health). |
| **Module Layer** | Screen-specific functions and views. | Command panels, sensor tables, stream canvases. |
| **Contextual Layer** | On-demand overlays for deeper insight or action. | Alerts, modals (Diagnostics, Configurations). |

Interactions follow a **predictable left-to-right, top-to-bottom flow**—overview on the left, detail on the right, logs or context at the bottom.

---

### 5. Information Display Principles

| Category | Principle | Design Implication |
|-----------|------------|--------------------|
| **Status & Health** | Always visible, summarized, color-coded. | Unified color system for normal/warning/critical. |
| **Alarms** | Contextual and non-blocking; designed to prompt action, not obstruct work. | Alerts stack at screen edge; dismissible once acknowledged. |
| **Controls** | Grouped by intent (Command, Configuration, Logging). | Consistent location across modules. |
| **Data Visualization** | Favor clarity over density. Use sparklines, gauges, and bars for trend comprehension. | Avoid 3D or unnecessary visual complexity. |
| **Typography & Color** | Use weight, not color, to emphasize hierarchy; color reserved for state. | Consistent tone across mission-scoped views. |

---

### 6. User Interactions Overview

| Interaction | Description | Example |
|--------------|-------------|----------|
| **Mission Activation** | Select mission from Triage Hub → updates all contextual windows. | Changes Mission Deck, Stream Viewer contents. |
| **Command Execution** | Operator triggers a system action (e.g., Start Logging). | Action confirmed, logged automatically. |
| **Alert Response** | Operator reviews alert with suggested remediation. | “Low SNR detected – check transducer alignment.” |
| **Configuration Update** | Apply or validate a configuration template. | Updates sensor behavior, generates log entry. |
| **Monitoring** | Continuous observation of sensor health and quality metrics. | Animated or periodic metric updates. |
| **Logging** | Manual notes or automatic event recording. | Operator annotation during data anomaly. |

---

### 7. Design System Overview

Although visual components may evolve, SMP maintains consistent **semantic and spatial rules**:
- **Color coding:**  
  - Green → Normal operation  
  - Amber → Warning or degraded performance  
  - Red → Critical or failed state  
- **Action icons:** contextual but non-intrusive (minimal animation).  
- **Layouts:** grid-aligned, fixed safe zones for core data and alerts.  
- **Feedback:** every system action triggers visible or logged feedback (no silent actions).  

> SMP’s design language prioritizes legibility, rhythm, and calm — enabling operators to sustain focus during prolonged missions.

---

## Acceptance Criteria

- The document clearly articulates SMP’s user experience principles and operational model.  
- Screen roles, context propagation, and multi-mission behavior are defined for all design and engineering stakeholders.  
- Visual hierarchy and design language guidelines are established for use in future functional specifications.  
- Interaction principles align with operational safety and traceability goals.

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Alert Escalation Path** | Define how critical alerts propagate across screens (Deck ↔ Triage). |
| **Diagnostics Access Pattern** | Confirm whether Diagnostics opens inline, as modal, or external window. |
| **Mission Summary Widgets** | Evaluate which performance indicators appear on global header vs. mission deck. |
| **Accessibility Testing** | Validate readability and color contrast under dim bridge lighting. |

---

### Summary Statement

> The SMP user experience framework defines a synchronized, mission-centric environment optimized for safety, clarity, and operational flow.  
> By maintaining consistent behavior and shared mission context across screens, the platform delivers the awareness and confidence required for complex, real-time marine survey operations.

---

**End of Document**
