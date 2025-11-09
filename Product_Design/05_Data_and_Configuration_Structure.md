---
doc_id: PDD.05
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [data-architecture, configuration, telemetry, thresholds, traceability, design-specification]
---

# 05_Data_and_Configuration_Structure

## Purpose
This document defines the **data and configuration framework** that underpins the Survey Management Platform (SMP).  
It establishes how configurations, telemetry, and mission-related data are structured, validated, and synchronized across modules to ensure consistency, reliability, and traceability during remote survey operations.

The goal is to maintain a **single source of truth** for system and mission configuration, allowing for safe real-time monitoring, rollback, and cross-mission comparability.

---

## Scope & Context
The SMP operates across two data layers:

| Layer | Description | Example |
|-------|--------------|----------|
| **Mission Layer** | Holds live configuration, telemetry, and event data for an active survey mission. | Active sensor parameters, QC metrics, Online Log entries. |
| **Global Layer** | Stores reusable configurations, templates, and system-level profiles shared between missions. | Template libraries, threshold presets, vessel defaults. |

This document defines the structure and behavior of these layers, including how they interact through modules such as:
- **Mission Deck** (Command & Control)
- **Stream Viewer** (Sensor Visualization)
- **Configuration Manager** (Setup & Validation)
- **Online Log** (Traceability)

---

## Data Model Overview

The SMP data model follows a **mission-centric hierarchy**, where all telemetry, configuration, and log entries are tied to a specific mission context.  
Below is the conceptual entity relationship summary.

### 🔗 Primary Entities

| Entity | Description | Key Relationships |
|---------|--------------|-------------------|
| **Mission** | Core operational unit containing all mission-related configuration and data. | Links to Sensors, Events, Files, and Templates. |
| **Sensor** | Represents an individual instrument or data source within a mission. | Has parameters, thresholds, and telemetry streams. |
| **Configuration Template** | Reusable preset defining system, sensor, and threshold parameters. | Applied to Missions; versioned. |
| **Threshold Profile** | Defines operational limits and alert conditions for metrics. | Shared across Config Manager and Stream Viewer. |
| **Event / Log Entry** | Timestamped record of actions, alerts, and changes. | Tied to Mission, Sensor, and User. |
| **File Transfer Object (FTO)** | Represents live or historical data files. | Associated with Mission; used in File Transfer Monitor. |
| **User / Role** | Represents operator or system user with RBAC privileges. | Linked to actions and configuration changes. |

---

## Configuration Data Schema

The SMP uses structured, modular configuration types.  
Each type maintains parameter consistency, validation, and inheritance rules.

| Category | Example Parameters | Description |
|-----------|-------------------|--------------|
| **System** | Hostname, Port, NTP Sync, Logging Directory, Redundancy Paths | Defines operational environment and data routing. |
| **Sensors** | Sensor ID, Type, Model, Offset, IP, Latency, Calibration Constants | Defines all mission sensors and their runtime parameters. |
| **Thresholds & Health** | Latency Limit, Packet Loss %, SNR Threshold, SVP Age Limit | Governs QC overlays, alert triggers, and health scoring. |
| **Templates** | Template Name, Version, Parameter Set | Provides baseline configuration reused across missions. |

### 🧩 Configuration Hierarchy


Global Defaults → Template → Mission Configuration → Live Runtime

- **Global Defaults:** Vessel or organization-level baselines.  
- **Template:** Predefined parameter sets (e.g., “ShallowWater_Std”).  
- **Mission Configuration:** Editable during mission setup phase.  
- **Live Runtime:** Read-only operational state; locked during logging.

### 🔁 Versioning & Rollback
Each configuration is versioned. When a new configuration is applied:
- Previous version is archived automatically.
- Rollback can restore any previous version.
- Change events are logged with author, timestamp, and diff summary.

---

## Telemetry & Data Streams

All real-time sensor and system data flow through the **Mission Layer telemetry bus**, feeding visualization and alert systems.  
Each telemetry packet carries contextual metadata:

| Field | Description |
|--------|-------------|
| `mission_id` | Links telemetry to the current mission. |
| `sensor_id` | Identifies data source. |
| `timestamp_utc` | Synchronization timestamp. |
| `metric` | Type of measurement (e.g., SNR, Ping Density, HDOP). |
| `value` | Numeric or categorical value. |
| `unit` | Unit of measure (e.g., dB, m, °C). |
| `quality_flag` | Boolean or graded indicator for threshold compliance. |

### Example Data Flow
1. **Sensor Telemetry** → Stream Viewer (visual + QC overlay)  
2. **QC Overlay Threshold Breach** → Mission Deck Alert + Log Entry  
3. **Log Entry** → Online Log & Handover Summary  
4. **Config Change (post-mission)** → Configuration Manager Snapshot  

---

## Traceability & History

Traceability is ensured through **event-based versioning**:
- Each configuration change, alert, and system action is automatically recorded in the **Online Log**.  
- Each Mission retains a **configuration snapshot** for every operational state transition (Preparation, Active Logging, Completed).  
- Sensor and threshold changes maintain their own **delta history**, enabling audit and rollback.

| Type | Description | Example |
|------|--------------|----------|
| **Configuration Snapshot** | Captured each time a config is applied. | “Template: DeepWater_Std applied at 14:32 UTC.” |
| **Event Log Entry** | Real-time record of actions or alerts. | “Sensor MBES restarted.” |
| **Threshold Delta** | Tracks changes to QC limits. | “SNR threshold changed: 40 → 35 dB.” |

Snapshots and logs are linked for full operational replay and auditability.

---

## Data Validation & Safety

| Rule | Description |
|------|--------------|
| **Parameter Validation** | Each field validated against type, range, and unit definitions before save. |
| **Locked State Enforcement** | No edits allowed when mission is in active logging or locked state. |
| **Conflict Resolution** | In multi-user cases, the most recent valid save prevails; concurrent edit warnings are shown. |
| **Unit Consistency** | All numeric parameters use standardized SI units. |
| **Safe Recovery** | Incomplete or corrupted configuration loads last valid version automatically. |

---

## Dependencies & Interfaces

| Source Module | Consumes / Publishes | Description |
|----------------|----------------------|--------------|
| **Mission Deck** | Consumes configuration and thresholds; publishes operational events. | Displays real-time system and health metrics. |
| **Stream Viewer** | Consumes telemetry and threshold data. | Uses threshold definitions to render QC overlays. |
| **Configuration Manager** | Consumes templates and thresholds; publishes configuration versions. | Central configuration control. |
| **Online Log** | Consumes all event and configuration change messages. | Acts as the audit trail for SMP activity. |
| **Triage Hub** | Consumes mission summary data and health status. | Displays cross-mission awareness. |

These inter-module connections ensure that a single change in configuration or telemetry is reflected consistently across the platform.

---

## Acceptance Criteria

- All configuration data follows a unified schema with clear inheritance rules.  
- Telemetry is consistently structured, contextualized, and timestamped.  
- Each configuration change or threshold adjustment is logged and versioned.  
- Mission data can be safely restored to any prior configuration state.  
- Threshold profiles drive both alert logic and visualization across modules.  
- All modules consume synchronized configuration and telemetry data from shared structures.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Persistence Model** | Define storage format and duration for mission configurations and telemetry. |
| **Schema Standardization** | Confirm JSON vs YAML schema adoption. |
| **API / Data Bus Design** | Evaluate if a common data bus abstraction layer is needed for telemetry. |
| **Diff Visualization** | Determine how configuration changes are represented in UI. |
| **Data Export Formats** | Define standardized export structure for mission archives. |

---

### Summary Statement

> The **Data & Configuration Structure** defines the backbone of the SMP’s information integrity—ensuring all modules operate on synchronized, validated, and auditable data.  
> Through versioning, structured schemas, and consistent threshold management, it supports reliable multi-mission operations and long-term traceability of configuration and telemetry across the entire platform.

---

**End of Document**
