---
doc_id: PDD.04.04
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [functional-specification, configuration-manager, system-setup, templates, thresholds, remote-operations]
---

# 04.04_Configuration_Manager

## Purpose
The **Configuration Manager** provides a structured environment for reviewing, editing, and applying configuration parameters across system components and sensors within a mission.  
It serves as the single point of control for **mission setup**, **system calibration**, and **quality threshold definition**, ensuring operational consistency and reducing configuration errors across missions.

This tool supports both preparation and live monitoring phases—though its editing capabilities may restricted on a role basis.

---

## Scope & Context
The Configuration Manager operates within the **Mission Layer**, accessible directly from the **Mission Deck** via the Tools menu.  
It is mission-contextual, meaning it displays and edits configuration data associated only with the currently active mission.

Key capabilities include:
- Reviewing system and sensor configurations.  
- Adjusting thresholds and quality limits used by QC overlays and alerts.  
- Managing configuration templates for reuse and consistency.  
- Locking configurations under RBAC control.  

---

## Key Concepts / Framework

| Concept | Description | Role |
|----------|--------------|------|
| **Configuration Tabs** | Organized categories for all configurable elements. | Provides structure and clarity. |
| **Templates** | Predefined parameter sets for rapid deployment. | Ensures consistency across missions. |
| **Thresholds & Health** | Stores QC and alert thresholds shared with Stream Viewer and Mission Deck. | Provides centralized quality control. |
| **Locking & RBAC** | Restricts modifications to authorized users or safe mission states. | Maintains system integrity. |

---

## Functional or UX Details

### 1. Layout Overview

| Zone | Purpose | Components |
|------|----------|-------------|
| **Header Bar** | Provides mission context and configuration status. | Mission ID, last update timestamp, lock/unlock indicator, save/apply controls. |
| **Tab Navigation** | Organizes configuration categories. | Tabs: System, Sensors, Thresholds & Health, Templates. |
| **Main Panel (per tab)** | Displays editable or read-only configuration forms. | Parameter fields, dropdowns, status icons, validation results. |
| **Footer Bar** | Displays configuration state and global actions. | “Save,” “Apply Template,” “Rollback,” “Close.” |

---

### 2. Tab Structure

| Tab | Purpose | Key Elements |
|------|----------|--------------|
| **System** | Defines system-wide operational parameters (network, time sync, storage). | - Network host & port configuration. <br> - Logging directory paths. <br> - Time synchronization settings. <br> - Recording and redundancy settings. |
| **Sensors** | Lists all mission sensors with their configuration and status. | - Add / Remove Sensor actions. <br> - Sensor type, model, and connection parameters. <br> - Alignment, offset, and latency parameters. <br> - Health status indicators (green/amber/red). |
| **Thresholds & Health** | Centralized configuration of QC thresholds used across the system. | - Metric thresholds (latency, packet loss, SNR, etc.). <br> - Alert severity mapping (Warning/Critical). <br> - Default and per-sensor override options. <br> - Linked to QC overlays in Stream Viewer. |
| **Templates** | Manages reusable configuration sets. | - Template library (project / mission level). <br> - Import / Export options. <br> - Apply Template. <br> - Rollback to previous configuration. |

---

### 3. Sensor Configuration Management

#### Adding a Sensor
- Action available from **Sensors tab** or from the Mission Deck “Add Sensor” button.
- Opens modal listing available sensor types (MBES, SSS, SBP, INS, USBL, GNSS, SVP/CTD, Cameras).
- Once added:
  - Default parameters auto-populate from template or system defaults.
  - Entry appears in the sensor table with editable fields.
  - Changes are logged under mission configuration events.

#### Removing a Sensor
- Initiated via the **Sensors tab**.
- Requires confirmation.
- If the sensor is active in Mission Deck or Stream Viewer, a warning message appears.
- Action is logged for traceability.

---

### 4. Configuration State Logic

| State | Description | Editable | Behavior |
|--------|-------------|----------|-----------|
| **Preparation** | Mission not logging. | ✅ Yes | All parameters editable. |
| **Active Logging** | Mission actively recording. | ✅ Yes | All parameters editable. |
| **Locked (RBAC)** | Configuration finalized by authorized role. | 🚫 No | Locked icon shown; unlock requires proper credentials. |

---

### 5. Thresholds & Health

This tab centralizes **all health and QC parameters** used across SMP for health evaluation and visualization.

| Metric Group | Example Parameters | Description | Impact |
|---------------|--------------------|--------------|--------|
| **System Health** | CPU Load, Latency, Packet Loss | Defines thresholds that trigger system-level warnings. | Affects Mission Deck health tiles and alerts. |
| **Sensor Health** | SNR, Ping Density, Beam Validity | Defines acceptable limits for acoustic performance. | Drives Stream Viewer overlays and alerts. |
| **Data Integrity** | File Rate, Transfer Latency | Controls alert triggers related to logging or transfer performance. | Impacts File Transfer Monitor and alerts. |
| **Environmental** | SVP Age, Temperature Drift | Defines acceptable drift limits. | Used in QC overlays for SVP/CTD. |

Thresholds can be configured globally or per sensor type, allowing flexibility across mission types.

---

### 6. Templates Management

Templates provide standardized configurations that ensure consistent setup across missions and projects.

| Action | Description | Behavior |
|---------|-------------|-----------|
| **Create Template** | Saves current configuration as a reusable template. | Requires unique name and optional description. |
| **Apply Template** | Loads predefined parameters into current mission. | Confirmation message. |
| **Rollback Configuration** | Restores previously applied template or last saved state. | Confirmation required. |
| **Import / Export** | Allows sharing templates between projects or vessels. | File-based import/export (.json or .yaml). |

> Template application events are logged, and resulting configuration changes trigger validation.

---

### 7. Validation & Feedback

- Real-time validation ensures only valid parameter ranges are saved.  
- Warnings appear inline for invalid or incomplete entries.  
- Successful saves and applications display a confirmation banner with timestamp.  
- Validation results are recorded in the mission log for traceability.

---

## Acceptance Criteria

- Configuration Manager allows complete mission setup.  
- All configuration states (Preparation, Active Logging, Locked) are visually clear.  
- Thresholds & Health tab synchronizes correctly with QC overlays and alert systems.  
- Template application and rollback are logged with timestamps.  
- All configuration changes are traceable and reversible.  
- Read-only mode remains accessible for inspection.  
- Layout follows the SMP interface design standards for modularity and clarity.

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **RBAC Integration** | Define roles authorized to lock/unlock configurations. |
| **Template Inheritance** | Determine if templates can inherit settings from project or vessel defaults. |
| **Version Control** | Explore configuration version history for rollback tracking. |
| **Dynamic Thresholds** | Assess if some thresholds should adjust automatically based on conditions (e.g., water depth). |
| **Sensor Calibration Hooks** | Clarify whether calibration data can be linked or stored in configuration records. |

---

### Summary Statement

> The **Configuration Manager** establishes a unified, structured framework for managing all mission configurations across the SMP.  
> It ensures safe, auditable control of systems and sensors, supports standardized setups through templates, and centralizes quality thresholds for consistent QC and monitoring across the platform.

---

**End of Document**
