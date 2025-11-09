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
