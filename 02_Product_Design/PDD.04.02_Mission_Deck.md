---
doc_id: PDD.04.02
version: 0.1.3
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [functional-specification, mission-deck, command-control, health-monitoring, configuration-manager, remote-operations]
---

# 04.02_Mission_Deck

## Purpose
The **Mission Deck** is the central operational workspace of the Survey Management Platform (SMP).  
It enables surveyors to control sensors, execute mission-level actions, monitor system and data health, manage alerts, and supervise live data recording and transfer—all within the active mission context.

The Mission Deck integrates **Command & Control**, **Health and Quality Monitoring**, **Alert Management**, and **Traceability** into one synchronized view, ensuring safe, transparent, and efficient mission operations.

---

## Scope & Context
The Mission Deck belongs to the **Mission Layer** of the SMP and operates strictly within the currently active mission.  
It is primarily used by **Survey Operators** and **Senior Surveyors** during mission preparation, execution, and live data acquisition.

Functions include:
- Starting and stopping logging.  
- Adding, configuring, or removing sensors during preparation.  
- Monitoring health, performance, and data quality.  
- Reviewing and acknowledging alerts.  
- Observing file transfer and logging states.  
- Accessing Diagnostics, Calibration, and Configuration tools via modals.

---

## Key Concepts / Framework

| Dimension | Description | Role |
|------------|--------------|------|
| **Command & Execution** | Direct control of sensors and logging within mission scope. | Mission and sensor management. |
| **Health & Quality Monitoring** | Aggregated visibility of system and sensor performance. | Detect early degradation. |
| **Alert Awareness** | Highlights advisory and critical alerts for operator action. | Informs decision-making, non-automated. |
| **Traceability** | Automatically logs operational actions. | Supports audit and accountability. |
| **File Transfer Status** | Displays real-time recording and transfer state. | Confirms mission continuity and data integrity. |

---

## Functional or UX Details

### 1. Layout Overview

| Zone | Purpose | Components |
|------|----------|-------------|
| **Header** | Mission identity and global tools access. | Mission ID, vessel, operator, UTC, health summary, Tools (SVP/CDT, Calibration, Diagnostics, Config Manager). |
| **Left Panel – Command & Sensors** | Sensor and logging control. | Logging controls, sensor list with power controls and add/remove functions. |
| **Center Panel – Health & Quality** | Real-time system and sensor metrics. | Grouped metric tiles with thresholds. |
| **Right Panel – Alerts** | Displays all current mission alerts. | Alert stack by severity. |
| **Bottom Dock – Online Log** | Chronological mission events. | Real-time event and comment log. |
| **Bottom-Right – File Transfer** | Displays recording and file throughput. | File name, rate, and state indicators. |

---

### 2. Command & Sensor Controls

| Function | Description | Behavior |
|-----------|-------------|-----------|
| **Start Logging** | Begins recording of all live mission data. | Immediate start with visual confirmation. |
| **Stop Logging** | Safely halts data recording. | Requires confirmation to prevent interruption. |
| **Sensor ON/OFF** | Toggles sensor power state. | Updates status instantly in Health panel. |
| **Restart Sensor** | Restarts connection or device process. | Shows temporary progress indicator on tile border. |
| **Add Sensor** | Opens modal listing available sensors. | Selecting a sensor adds it to mission list; entry logged. |
| **Remove Sensor** | Removes selected sensor from mission. | Requires confirmation; removal logged. |
| **Signal Flow** | Opens sensor diagnostic modal. | Contextual per sensor. |

> All add/remove or state-change actions are recorded automatically in the mission log.  
> Configuration parameters for new sensors are set within the Configuration Manager.

---

### 3. Header & Tool Access

| Tool | Purpose | Behavior |
|------|----------|-----------|
| **SVP/CDT (Hydrosens)** | Opens oceanographic profile tools. | Modal overlay. |
| **Calibration** | Accesses calibration status and routines. | Modal overlay. |
| **Diagnostics** | Opens diagnostic tools for network and signal flow. | Fully accessible; independent per mission. |
| **Configuration Manager** | Provides configuration access for System, Sensors, Thresholds & Health, and Templates. | Allows per-sensor diagnostics access. |

> All tools open in **persistent modals** that maintain state across mission switches.  
> When switching missions, the application restores the last-known state for each mission, including open modals and unsaved progress.

---

### 4. Health & Quality Monitoring

Metrics are structured across three groups:

| Group | Example Metrics | Representation | Source |
|--------|----------------|----------------|---------|
| **System Health** | Latency, Clock Drift, Packet Loss, CPU Load | Horizontal bars + color + icon redundancy. | Mission Engine |
| **Sensor Health** | Connection %, SNR, Ping Density, INS Drift, GNSS HDOP | Numeric tiles with transient states during restart. | Sensor Telemetry |
| **Data Integrity & Environment** | Recording State, File Rate, SVP Validity | Compact tiles; visual progress and thresholds. | Logging System |

Transient states (e.g., restarting, reconnecting) use animated or border progress cues rather than static alerts.

---

### 5. Alerts & Notifications

| Element | Description | Behavior |
|----------|--------------|-----------|
| **Alert Stack** | Persistent list of mission alerts by severity. | Non-blocking; scrollable. |
| **Severity Encoding** | Red = Critical, Amber = Warning, Blue = Info. | Color + icon redundancy for accessibility. |
| **Acknowledgment** | Allows operator to acknowledge non-critical alerts. | Persistent until operator confirms. |
| **Advisory Behavior** | Alerts never take control actions (e.g., stop or pause logging). | Operator decides response. |
| **Actionable Context** | Alerts include short guidance text. | Example: “Low QC detected – review data integrity.” |
| **Traceability** | Each alert logs to the Online Log with timestamp. | Enables full audit trail. |

> Alerts are **advisory**, not autonomous; the surveyor retains complete operational control.

---

### 6. Online Log Dock

| Function | Description | Behavior |
|-----------|-------------|-----------|
| **Auto-Logging** | Displays system and operator events. | Scrollable, real-time updates. |
| **Add Comment** | Allows operator to record notes. | Inline entry; timestamped. |
| **Filter / Search** | Filters by type or keyword. | Inline quick filter. |
| **Generate Handover** | Compiles activity summary for shift transitions. | Select time window for export. |

---

### 7. File Transfer Monitor

| Element | Description | Behavior |
|----------|--------------|-----------|
| **File Path & Name** | Displays current recording file. | Updated dynamically. |
| **Status Tags** | Indicates file lifecycle (Recording, Validating, Transferring, Idle). | Color-coded with icons. |
| **Transfer Rate** | Displays throughput (MB/s). | Animated numeric label. |

> File Transfer panel remains visible and passive; used for verification only.

---

## Acceptance Criteria

- Mission Deck supports full mission and sensor control safely.  
- Adding/removing sensors is supported during mission preparation.  
- Modals preserve mission context and state when switching missions.  
- Alerts are strictly advisory; system actions are always operator-driven.  
- File Transfer panel provides accurate, continuous feedback.  
- All command actions and configuration events are logged automatically.  
- Layout is responsive and clear across resolutions and operating environments.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Sensor Library Integration** | Define how available sensors are populated in Add Sensor modal. |
| **Mission State Persistence** | Confirm behavior for restoring per-mission modal state when switching contexts. |
| **Configuration Lock Messaging** | Define UX for indicating locked state. |
| **Alert Escalation Logic** | Clarify escalation triggers for cross-mission visibility. |
| **Sensor Removal Rules** | Establish removal restrictions (e.g., cannot remove active logging sensors). |

---

### Summary Statement

> The **Mission Deck** centralizes mission execution and monitoring in a single interface.  
> It enables safe, transparent, and operator-controlled management of sensors and data collection, while maintaining mission continuity and contextual awareness across concurrent operations.

---

**End of Document**
