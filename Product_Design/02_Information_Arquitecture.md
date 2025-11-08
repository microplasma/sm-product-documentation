---
doc_id: PDD.02.00
version: 0.1.0
last_updated: 2025-11-08
status: draft
owners: [design@survey-platform.io]
tags: [information, architecture, system-model, mission-structure, data-flow]
---

# 02_Information_Architecture

## Purpose
This document defines the **information structure and logical relationships** that underpin the Survey Management Platform (SMP).  
It describes how missions, sensors, configurations, metrics, and logs relate to one another—establishing the conceptual data architecture that supports consistent situational awareness, traceability, and collaboration.

The goal is to ensure that all design and functional specifications share a **common mental model** of the system’s information flow and dependencies.

---

## Scope & Context
The SMP operates as a distributed, mission-centered ecosystem.  
Each active mission aggregates and manages data from sensors, configurations, commands, and health metrics, while maintaining strict separation from other missions.

The Information Architecture defines:
- **Entities** (core information objects).  
- **Relationships** (how entities interact).  
- **Flows** (how data moves between modules).  
- **Contextual behavior** (what happens when missions or roles change).  

---

## Key Concepts / Framework

### Core Entities
| Entity | Description | Ownership | Notes |
|---------|--------------|------------|-------|
| **Mission** | The fundamental operational unit within SMP. Encapsulates objectives, configurations, and associated data. | Survey Operator / PEC | Always unique and traceable via Mission ID. |
| **Sensor** | Physical or virtual device contributing data to a mission (e.g., MBES, SSS, INS). | Senior Surveyor / IT | Configured via templates, monitored continuously. |
| **Subsystem** | Logical grouping of related sensors or systems (e.g., Navigation, Imaging, Motion). | Survey Operator | Simplifies monitoring at system level. |
| **Metric** | A quantifiable value representing system or sensor performance. | Survey Operator | Derived from telemetry and threshold logic. |
| **Alert** | An actionable system event triggered when conditions breach limits or expectations. | System / Operator | Categorized by severity and linked to log entries. |
| **Configuration** | The operational parameters defining how systems and sensors behave. | Senior Surveyor / IT | Stored as templates; versioned for rollback and validation. |
| **Log Entry** | Time-stamped record of mission actions, alerts, and operator notes. | System / All Users | Immutable chronological trace; cross-linked to events. |
| **File Transfer Object (FTO)** | Represents recorded or generated files with associated metadata (status, checksum, destination). | Data Processor | Supports live monitoring and validation by the offline team. |

---

## Functional or UX Details

### 1. Hierarchical Model

The SMP organizes its information in a hierarchical and contextual manner:

├── Global Layer 
│ ├── Triage Hub (cross-mission awareness) 
│ └── Online Log (cross-mission traceability) 
└── Mission Layer 
    ├── Mission Deck (command and health) 
    ├── Stream Viewer (sensor visualization) 
    ├── Diagnostics & Tools (validation) 
    ├── Configuration Manager 
    └── File Transfer Monitor 
        └── File Transfer Objects (FTOs)


Each mission instance carries its own complete ecosystem of data and relationships.  
Global layers are mission-independent but remain aware of mission summaries and identifiers.

---

### 2. Relationships Between Entities

| Source | Target | Relationship | Description |
|---------|---------|---------------|-------------|
| **Mission → Sensor** | One-to-Many | Each mission controls and monitors several sensors. |
| **Sensor → Metric** | One-to-Many | Sensors generate multiple metrics (e.g., SNR, Ping Density). |
| **Metric → Alert** | One-to-Many (conditional) | Threshold breaches produce alerts tied back to metrics. |
| **Command → Log Entry** | One-to-One | Each executed command results in a logged action. |
| **Alert → Log Entry** | One-to-One | Each alert generates a corresponding log reference. |
| **Configuration → Sensor** | One-to-Many | A configuration defines operational parameters for sensors. |
| **File Transfer Object → Mission** | Many-to-One | All mission files are scoped to a single mission ID. |
| **Mission → Online Log** | Many-to-One (aggregated) | Mission logs roll up into the global Online Log for review. |

---

### 3. Mission Context Propagation

When a user activates a mission from the **Triage Hub**:
- A **Mission Context** object is broadcast to all mission-scoped modules.
- Each module updates its view (Health, Stream, Diagnostics, Configurations) with mission-specific data.
- The **Online Log** continues collecting entries but tags them with `MissionID`.
- **Cross-mission integrity** is enforced by context isolation—data or commands cannot affect non-active missions.

> This mechanism ensures that SMP behaves as a single synchronized workspace while maintaining mission-level safety and traceability.

---

### 4. Information Flow Model

| Flow Type | Description | Source | Destination | Visible In |
|------------|--------------|---------|--------------|-------------|
| **Command Flow** | Operator actions and control messages. | Mission Deck | Subsystems / Sensors | Mission Deck, Online Log |
| **Telemetry Flow** | Sensor data and performance metrics. | Sensors | Health & Quality, Stream Viewer | Mission Deck, Stream Viewer |
| **Alert Flow** | Triggered by system thresholds or conditions. | Monitoring Engine | Mission Deck, Triage Hub | Alerts Panel, Online Log |
| **Configuration Flow** | Application or modification of templates. | Config Manager | Sensors / Subsystems | Mission Deck, Log |
| **Logging Flow** | Automatic and manual entries recording events. | System / Operator | Online Log | Global Log View |
| **File Transfer Flow** | File creation, validation, and delivery. | Mission Recorders | File Transfer Monitor | Mission Deck |

Each flow is event-driven and mission-scoped, ensuring deterministic traceability from input to outcome.

---

### 5. Traceability Map

Traceability is intrinsic to SMP’s architecture.  
Each **event**, **action**, or **data object** carries metadata that allows reconstruction of full operational history.

| Metadata Field | Description | Example |
|-----------------|-------------|----------|
| **MissionID** | Unique identifier for mission context. | `MSSN_2025_0012` |
| **Timestamp (UTC)** | Standardized time reference for synchronization. | `2025-11-08T13:25:02Z` |
| **Actor / Origin** | Human or system process responsible. | `SurveyOperator`, `DiagnosticsEngine` |
| **Object Type** | Entity affected. | `Sensor`, `FileTransferObject`, `Metric` |
| **Action / Event Type** | Nature of activity. | `CommandIssued`, `ThresholdExceeded`, `FileDelivered` |
| **Outcome / Status** | Resulting condition. | `Success`, `Warning`, `Critical` |
| **Reference Link** | Cross-reference to related objects. | `Alert → LogEntry`, `Command → FileTransfer` |

All mission and system data adhere to this **traceability envelope**, forming the backbone of SMP’s auditability and quality assurance.

---

## Acceptance Criteria
- The document provides a complete and comprehensible view of SMP’s logical structure and entity relationships.  
- Information flows are clearly defined and consistent with operational behavior described in [PDD.01.00 – System Overview].  
- Traceability and mission context propagation are explicitly mapped.  
- Roles and data ownership are visible for each major entity.

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Data Persistence Model** | Define retention policies for mission data once transferred to onshore systems. |
| **File Transfer Object Scope** | Confirm how live monitoring integrates with onshore data processing validation. |
| **Cross-Mission Data References** | Determine whether certain shared resources (e.g., vessel navigation feed) are globally referenced or duplicated per mission. |
| **Event Prioritization Model** | Formalize how SMP categorizes simultaneous alerts for display priority. |

---

### Summary Statement

> The SMP Information Architecture establishes a mission-centric, traceable data model that ensures clarity, safety, and accountability across concurrent operations.  
> Every mission operates within its own information boundary, yet all are unified under a common framework that promotes consistency, interoperability, and transparent collaboration between offshore and onshore teams.

---

**End of Document**
