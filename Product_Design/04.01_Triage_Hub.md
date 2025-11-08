---
doc_id: PDD.04.01
version: 0.1.1
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [functional-specification, triage-hub, mission-selection, cross-mission, remote-operations]
---

# 04.01_Triage_Hub

## Purpose
The **Triage Hub** is the entry point and global overview of the Survey Management Platform (SMP).  
It allows surveyors operating from onshore facilities to view all missions assigned to them, assess mission health at a glance, and select which mission to actively monitor and control.

The Triage Hub supports **multi-mission awareness**, **safe activation of mission contexts**, and **immediate visibility into system health**, forming the foundation of the platform’s command and control environment.

---

## Scope & Context
The Triage Hub exists within the **Global Layer** of the SMP, meaning it operates **outside any single mission context**.  
Its purpose is to:
- Display an overview of all missions under a surveyor’s responsibility.  
- Summarize health, performance, and alert states across missions.  
- Allow activation or switching of the current mission context seamlessly.  
- Provide immediate awareness of degraded or critical mission conditions.

When a mission is selected from the Triage Hub, all mission-scoped windows (Mission Deck, Stream Viewer, Navigation) update to that mission’s context automatically—without requiring additional confirmation.

---

## Key Concepts / Framework

### 1. Conceptual Overview

The Triage Hub acts as a **command launcher and situational dashboard**.  
It is not intended for detailed monitoring, but for quick, informed decision-making about **where to focus operational attention**.

Core design intent:
- Keep the display lightweight and scannable.  
- Emphasize **relative mission health**, not raw telemetry.  
- Allow frictionless switching between missions while ensuring contextual safety.  
- Surface alerts that may require shifting focus.

---

## Functional or UX Details

### 2. Layout Overview

| Zone | Purpose | Example Components |
|-------|----------|--------------------|
| **Global Header** | Provides global context independent of missions. | SMP logo, operator name, UTC clock, system connection status. |
| **Mission List Grid** | Displays mission cards/containers summarizing each mission’s status. | Mission title, ID, vessel name, health summary, alert badges. |
| **Filter & Search Bar** | Allows quick access when managing many missions. | Text search, status filters (Active, Idle, Critical). |
| **Action Bar / Footer** | Contains secondary utilities such as refresh, layout switch, or log shortcuts. | “Refresh Data,” “View Logs,” “Help.” |

---

### 3. Mission Card Structure

Each **Mission Card** acts as an interactive summary element that conveys the state of a mission at a glance.

| Element | Description | Representation |
|----------|--------------|----------------|
| **Mission Name / ID** | Unique mission identifier. | Text with mission icon. |
| **Vessel / Location Info** | Provides context about where the mission is running. | Vessel name + geographic tag. |
| **Health Indicator** | Aggregated mission health based on latency, drift, and packet loss. | Color + icon (✓ = normal, ! = warning, ⚠ = critical). |
| **Quality Indicator** | Represents data integrity and QC metrics from Stream Viewer. | Bar or dial visualization with numeric score (0–100). |
| **Active Status** | Highlights the currently selected mission. | Active border or accent. |
| **Alert Badge** | Displays count of unresolved alerts for that mission. | Badge with color and numeric indicator. |
| **Last Update Timestamp** | Shows last received telemetry or heartbeat. | UTC time text (“5s ago”, “Offline”). |

Mission cards are designed for **rapid scanning**, allowing operators to identify degraded missions and switch focus within seconds.

---

### 4. Key Functions & Interactions

| Function | Description | Outcome |
|-----------|--------------|----------|
| **Mission Selection** | Click to make a mission active. | Instantly updates all mission-scoped windows. |
| **Mission Health Overview** | View summarized health (system + data). | Helps prioritize which mission requires focus. |
| **Alert Awareness** | Identify active alerts per mission. | Encourages proactive response before failure. |
| **Filtering / Sorting** | Organize missions by name, status, or alert severity. | Increases clarity when handling multiple missions. |
| **Quick Log Access** | View mission-specific log summary (read-only) without changing active context. | Enables pre-activation awareness. |

> Mission switching is instantaneous and **non-destructive**—no operations are interrupted when context changes.

---

### 5. Health and Quality Metrics Displayed

The Triage Hub aggregates **mission-level summaries**, not individual sensor metrics.  
These summaries are derived from Mission Deck and Stream Viewer data.

| Metric Group | Example Metrics | Source | Representation |
|---------------|----------------|---------|----------------|
| **System Health** | Latency, Packet Loss, CPU Load | Mission Deck | Horizontal bars + color/icon indicator |
| **Sensor Performance** | SNR, Ping Density, INS Drift | Stream Viewer | Compact numeric trend indicator |
| **Data Integrity** | File Write Rate, QC Score | Mission Deck / Stream Viewer | Numeric score + progress bar |
| **Alert Count** | Active and Critical Alerts | Mission Deck / Online Log | Badge with count |
| **Last Sync** | Time since last telemetry update | System Engine | Text (“5s ago”, “Offline”) |

> Metrics provide a **relative snapshot**—the surveyor only switches missions if degradation or alert state demands attention.

---

### 6. Mission Selection Workflow

1. **Select Mission Card** – Operator clicks on a mission card.  
2. **Context Broadcast** – SMP immediately updates all mission-scoped windows (Mission Deck, Stream Viewer, Navigation).  
3. **State Feedback** – Global header updates with mission name and timestamp; log entry automatically recorded for traceability.

This workflow removes unnecessary friction and enables fast, safe transitions between missions during live operations.

---

### 7. Visual Hierarchy & Behavior

- **Color + Icon Redundancy:** All health and alert states use combined visual cues for accessibility.  
- **Adaptive Layout:** Mission cards reflow dynamically based on available screen space (typically 2–3 columns).  
- **Focus Retention:** Active mission card remains visually distinct through color, glow, or label.  
- **Alert Escalation:** Critical alerts animate subtly (pulse) until acknowledged in the Mission Deck.  
- **Non-Blocking Behavior:** The **Triage Hub remains always open** during operations—it is the global control panel that enables safe mission switching and overall situational awareness.  

---

## Acceptance Criteria

- Triage Hub enables operators to view and manage multiple missions safely from a single overview screen.  
- Health and quality indicators accurately summarize mission states without overloading the operator.  
- Mission selection is frictionless, non-destructive, and context propagation is instantaneous.  
- Alerts, health, and data quality are communicated through redundant visual cues (color + icon).  
- The platform layout is **responsive**, scaling gracefully across varying screen resolutions and maintaining legibility from a distance.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Mission Grouping** | Each mission corresponds to a single vessel. We do not anticipate a surveyor managing more than **2–3 missions concurrently** for safety and cognitive load reasons. |
| **Alert Propagation Rules** | Define how global (cross-mission) alerts are displayed versus mission-specific alerts. |
| **Offline Mission Handling** | Confirm how inactive or paused missions appear in the overview (e.g., greyed out, status label). |
| **Performance Updates** | Determine update cadence for mission health summaries (live streaming vs. periodic refresh). |

---

### Summary Statement

> The **Triage Hub** provides surveyors with a clear, always-accessible overview of their assigned missions.  
> It prioritizes awareness, responsiveness, and accessibility—enabling operators to safely switch missions without disruption, maintain control of multiple offshore operations, and quickly identify any mission requiring immediate attention.

---

**End of Document**
