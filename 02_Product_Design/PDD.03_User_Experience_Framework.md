---
doc_id: PDD.03
version: 0.1.1
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [user-experience, ux-framework, design-system, multi-screen, remote-operations]
---

# PDD.03_User_Experience_Framework

## Purpose
This document defines the **user experience framework** for the Survey Management Platform (SMP).  
It establishes how users interact with the system across multiple screens, how mission context is propagated, and the guiding principles that ensure consistency, clarity, and operational safety—particularly within **remote onshore survey operations**.

The goal is to enable surveyors and supporting roles to operate multiple survey missions concurrently, maintaining full situational awareness and data quality oversight from an onshore facility.

---

## Scope & Context
The SMP supports **remote survey operations**, where surveyors manage live missions running offshore.  
Operators work from an **onshore control center**, coordinating with the vessel’s bridge, operational crew, and sometimes the Data Processor team.  
All interactions occur within a **multi-window environment**, where the mission context determines what data and controls are active at any given time.

Diagnostic and configuration functions are **triggered as contextual windows** (modals) from within the Mission Deck rather than having dedicated screens.  
This model simplifies the operator workspace and reduces unnecessary interface switching.

---

## Key Concepts / Framework

### 1. Multi-Screen Operational Concept

The SMP is currently designed around an **8-screen layout** (4×2 grid), though screen allocation may evolve as testing and optimization continue.

| Screen | Function | Context |
|---------|-----------|----------|
| **1. Triage Hub** | Displays all missions currently assigned to the surveyor. Each mission container shows key health and performance metrics and allows mission selection or monitoring. | Cross-mission |
| **2. Mission Deck** | Primary control and monitoring surface for the selected mission. Hosts key mission tools, health metrics, and access to Diagnostics and Configuration modals. | Active mission |
| **3. Navigation** | Displays the live operational plan and vessel tracking. For the MVP, this screen will display **QINSy** to ensure navigational accuracy and adherence to survey plan. | Active mission |
| **4. Unallocated (future)** | Reserved for future tools or expanded features. | — |
| **5–6. Stream Viewer(s)** | Visualize live data from key sensors (e.g., MBES, SSS, INS). Allow real-time quality validation and alignment with Mission Deck metrics. | Active mission |
| **7. Unallocated (future)** | Reserved for mission support or communication extensions. | — |
| **8. Online Log** | Centralized mission and system log showing chronological events, alerts, and notes. | Cross-mission |

> All screens except for **Triage Hub** and **Online Log** are contextual to the currently active mission.

---

### 2. Context Propagation Model

The SMP maintains a **single active mission context** at any time.  
When the surveyor selects a mission from the **Triage Hub**:

1. The **Mission Context** object is activated and broadcast to all mission-scoped modules.  
2. **Mission Deck**, **Stream Viewer(s)**, and **Navigation** screens update to reflect that mission’s data, health, and configurations.  
3. The **Online Log** remains global but continues to record all mission activity tagged by `MissionID`.  
4. Diagnostics or configuration modals opened from the Mission Deck automatically reference the current active mission context.

This design guarantees synchronization across all operational screens and prevents cross-mission interference.

---

### 3. Experience Pillars

| Pillar | Description | Example Application |
|--------|--------------|---------------------|
| **Situational Awareness** | Operators must maintain a clear understanding of mission status and data quality in real time. | Health summaries and status icons visible on all screens. |
| **Cognitive Clarity** | Reduce information noise and emphasize what matters most in the moment. | Context-aware display of metrics; secondary data hidden until requested. |
| **Actionable Insight** | Alerts and notifications should convey meaning and guidance, not just warning states. | “Quality threshold exceeded – pause logging and verify transducer alignment.” |
| **Consistency** | Shared patterns across modules (visual hierarchy, terminology, and layout). | All control panels follow the same command-button and status pattern. |
| **Safety by Design** | Prevent accidental actions that could compromise data integrity or mission progress. | Confirmation prompts for **Stop Logging** to avoid unintended data loss. |
| **Accessibility & Redundancy** | Critical information must be perceivable through multiple cues, not just color. | Combine color + iconography for health and alert states. |
| **Traceable Transparency** | Every action produces a visible and logged outcome. | Operator commands and system events appear in the Online Log. |

---

## Functional or UX Details

### 4. Interaction & Layout Flow

While not all screens will share identical structures, SMP interfaces will adhere to a **left-to-right, top-to-bottom interaction rhythm**, promoting intuitive scanning and control access.

| Zone | Function | Example Components |
|-------|-----------|--------------------|
| **Top Region** | Mission identity, system time, high-level health state. | Header, mission selector, UTC clock. |
| **Left Panel** | Command and configuration area. | Logging controls, template actions, diagnostics launcher. |
| **Main Panel** | Data visualization and health awareness zone. | Health tiles, sensor summaries, live data streams. |
| **Right Panel** | Contextual information and alerts. | Alert stack, notifications, QC summaries. |
| **Bottom Panel** | Logs and secondary context. | Online Log dock, annotations, recent actions. |

This flow reinforces **progressive disclosure**—operators start from overview (left/top) and move toward detail or response (right/bottom).

---

### 5. Information Display Principles

| Category | Principle | Design Implication |
|-----------|------------|--------------------|
| **Status & Health** | Always visible, summarized with dual-mode indicators (color + iconography). | Green + ✓, Amber + !, Red + ⚠. |
| **Alarms & Alerts** | Non-blocking by default; some critical alerts may be non-dismissible until resolved. | Critical “Low Quality” alert persists until logging conditions improve. |
| **Controls** | Grouped by functional intent (Commands, Configuration, Logging). | Consistent location across modules. |
| **Data Visualization** | Prioritize clarity and interpretability over graphical density. | Trend micro-charts and indicators instead of large dashboards. |
| **Typography & Symbolism** | Use weight, spacing, and icons to denote importance; avoid reliance on color alone. | Accessibility compliance across viewing conditions. |

---

### 6. User Interactions Overview

| Interaction | Description | Example |
|--------------|-------------|----------|
| **Mission Activation** | Selecting a mission from the Triage Hub updates all contextual windows. | Mission Deck, Stream Viewer, and Navigation update within seconds. |
| **Command Execution** | Operator initiates system action such as Start/Stop Logging. | Stop Logging → Confirmation modal → Log entry created. |
| **Alert Response** | Operator reviews actionable alert with contextual recommendations. | “Ping density low – check navigation offset or sensor alignment.” |
| **Configuration Validation** | Operator reviews or adjusts configuration using modal window. | Apply template → validate parameters → receive success confirmation. |
| **Monitoring & Observation** | Continuous health and data quality assessment during mission. | Live metric animations and alert changes in Mission Deck and Stream Viewer. |
| **Logging & Annotation** | Every command, alert, and note is automatically time-stamped and recorded. | Surveyor adds context note during QC event. |

---

### 7. Design System Guidelines

The SMP’s interface language emphasizes **calm, legible, and consistent visual hierarchy**.  
Key principles include:

- **Color + Icon Redundancy:** Color used only in combination with iconography for accessibility (e.g., ⚠ red = critical, ! amber = warning, ✓ green = normal).  
- **Consistency of Patterns:** Buttons, controls, and dialogs follow a unified interaction model across all modules.  
- **Feedback & Traceability:** Every action provides visual confirmation and creates a corresponding log event.  
- **Safe Interactions:** Critical controls (e.g., stopping logging) require deliberate user acknowledgment.  
- **Rhythmic Layouts:** Gridded alignment, generous spacing, and predictable flow minimize visual fatigue.  
- **Operational Legibility:** UI optimized for extended monitoring under varied light and environmental conditions.

---

## Acceptance Criteria

- Remote onshore operational context and screen allocation are correctly represented.  
- Experience pillars reflect the platform’s principles and real-world constraints.  
- Accessibility and redundancy (color + iconography) are included as standard practice.  
- Interaction model supports safe, contextual, and traceable workflows.  
- Layout rhythm and behavior are clearly described to guide further functional design.

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Screen Allocation Flexibility** | Validate if Navigation will remain external (QINSy) or integrated in future SMP release. |
| **Alert Dismissal Rules** | Define exact conditions where alerts must be resolved before dismissal. |
| **Diagnostics Modal Behavior** | Confirm if diagnostic views can remain persistent alongside mission controls. |
| **Layout Adaptability** | Determine how layouts adapt to reduced screen environments (e.g., laptop mode for testing). |

---

### Summary Statement

> The SMP User Experience Framework defines a mission-centric, remote-operational environment focused on safety, clarity, and accessibility.  
> It aligns all modules under shared interaction and visualization principles, ensuring that operators can manage multiple missions confidently—whether monitoring, commanding, or responding to system changes.

---

**End of Document**
