---
doc_id: PDD.06
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [roles, operational-modes, permissions, workflows, remote-operations]
---

# 06_User_Roles_and_Operational_Modes

## Purpose
This document defines the **user roles** and **operational modes** within the Survey Management Platform (SMP).  
It describes how each role interacts with the platform, the scope of their permissions, and how operational modes (Preparation, Active Logging, and Review) influence feature accessibility and responsibilities.

Understanding these relationships ensures safe operation, clear accountability, and efficient collaboration between onshore and offshore teams.

---

## Scope & Context
The SMP supports **multi-mission, multi-role collaboration** between onshore and offshore participants.  
The user model is role-based rather than user-specific, meaning that capabilities are tied to role responsibilities, not individuals.  

The operational modes reflect mission lifecycle phases, ensuring that features are only available when appropriate to operational safety and data integrity.

---

## Key Concepts / Framework

| Concept | Description | Purpose |
|----------|--------------|----------|
| **Role-Based Access Control (RBAC)** | User permissions are tied to roles, not individual accounts. | Provides consistent operational safety and traceability. |
| **Operational Mode** | Defines the active phase of a mission (Preparation, Active Logging, Review). | Controls system behavior and access scope. |
| **Mission Context** | Active mission determines available data, visualizations, and controls. | Ensures contextual coherence across all screens. |
| **Cross-Mission Visibility** | Global views available to some roles (e.g., PEC) for overview and coordination. | Enables efficient multi-mission management. |

---

## User Roles

| Role | Primary Focus | Core Responsibilities | Typical Screens / Tools |
|------|----------------|------------------------|--------------------------|
| **Survey Operator** | Execute live survey operations. | - Control sensors and data logging.<br>- Monitor system health and alerts.<br>- Add notes to Online Log.<br>- Apply templates during setup. | Mission Deck, Stream Viewer, Online Log. |
| **Senior Surveyor** | Technical oversight and calibration. | - Mobilisation and calibration of sensors.<br>- Assist operators with troubleshooting.<br>- Validate mission setup and QC thresholds.<br>- Authorize configuration locks. | Mission Deck, Configuration Manager, Diagnostics. |
| **Project Execution Coordinator (PEC)** | Project-level oversight and coordination. | - Monitor multiple missions.<br>- Review health, progress, and alerts.<br>- Facilitate communication between offshore and onshore teams.<br>- Oversee project compliance. | Triage Hub, Mission Health Summary, File Transfer Monitor. |
| **Data Processor** | Data validation and post-processing. | - Verify data completeness and transfer integrity.<br>- Perform post-acquisition QC.<br>- Access mission metadata and transfer logs.<br>- Review Online Log archives. | Online Log, File Transfer Monitor (read-only), Data Archives. |

> Each role’s access scope is determined by mission state and RBAC configuration defined in the Configuration Manager.

---

## Operational Modes

| Mode | Description | Feature Availability | Notes |
|------|--------------|----------------------|-------|
| **Preparation** | Pre-mission setup and calibration phase. | - All configuration tabs editable.<br>- Sensors can be added or removed.<br>- Templates can be applied.<br>- Thresholds adjustable.<br>- Diagnostics and calibration fully enabled. | Used primarily by Senior Surveyor and Survey Operator before data logging starts. |
| **Active Logging** | Live data acquisition phase. | - Configuration locked (read-only).<br>- Sensors controllable (ON/OFF/Restart).<br>- QC overlays active in Stream Viewer.<br>- Alerts and health indicators updated live.<br>- Manual Online Log entries permitted. | Primary operational phase; managed by Survey Operator. |
| **Review** | Post-mission assessment and data validation. | - Logging disabled.<br>- Configuration editable for next mission planning.<br>- Log and alert archives accessible.<br>- File transfer and completeness checks active.<br>- Export of summaries enabled. | Used by Data Processor and Senior Surveyor for validation and reporting. |

---

## Role–Mode Interaction Matrix

| Role ↓ / Mode → | Preparation | Active Logging | Review |
|------------------|--------------|----------------|---------|
| **Survey Operator** | Configure and prepare mission; test sensors. | Full control of sensors and data logging; restricted configuration edits. | View-only; can review logs. |
| **Senior Surveyor** | Lead configuration and calibration; lock configurations. | Monitor operations and provide technical support. | Validate data and update templates. |
| **PEC** | Observe mission setup progress. | Monitor health and alerts across missions. | Review mission outcomes and health summaries. |
| **Data Processor** | No role in preparation. | Read-only monitoring (if applicable). | Review data completeness and quality; generate reports. |

---

## Cross-Mission Visibility

| Component | Visibility | Description |
|------------|-------------|-------------|
| **Triage Hub** | Global | Displays all active missions with health summaries and alert status. |
| **Online Log** | Global | Allows review of multi-mission activity; filter to active mission. |
| **Mission Deck / Stream Viewer** | Contextual | Displays only data from the active mission. |
| **Configuration Manager** | Contextual | Loads configuration data for the selected mission only. |
| **File Transfer Monitor** | Global summary + mission detail | Monitors progress and status across multiple missions. |

---

## User Safety & Access Design Principles

1. **Safety by Role:**  
   - Operators cannot modify configurations during live logging.  
   - Senior Surveyors or PECs may authorize changes only when mission is in preparation or paused.

2. **Least Privilege:**  
   - Each role sees only what is needed for their task to prevent accidental disruption.

3. **Read-Only Assurance:**  
   - During critical operations, configuration and diagnostic tools default to read-only states.

4. **Cross-Mission Isolation:**  
   - Each mission retains independent operational and data states to prevent unintended interference.

---

## Acceptance Criteria

- Each role’s permissions and visible tools align with defined responsibilities.  
- Operational modes dynamically enforce configuration locks and tool accessibility.  
- Roles share synchronized mission data but maintain clear separation of control.  
- Cross-mission visibility functions correctly in global tools (Triage Hub, Online Log).  
- All mission and user actions are logged for traceability.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **RBAC Granularity** | Define whether role privileges are vessel-specific or global. |
| **Mission Transfer of Ownership** | Determine how missions are reassigned between surveyors. |
| **PEC Alert Customization** | Confirm whether PEC can set cross-mission alert filters. |
| **Offline Mode Behavior** | Define how roles interact when disconnected from live telemetry. |
| **User Interface Personalization** | Evaluate optional UI presets per role (Operator, PEC, etc.). |

---

### Summary Statement

> The **User Roles and Operational Modes** framework ensures safe, predictable, and collaborative survey execution.  
> By clearly defining role capabilities and restricting actions based on mission mode, the SMP maintains operational integrity while supporting efficient coordination across multi-mission, remote survey environments.

---

**End of Document**
