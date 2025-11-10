---
doc_id: PDD.06
version: 0.1.1
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [roles, operational-modes, permissions, workflows, remote-operations]
---

# 06_User_Roles_and_Operational_Modes

## Purpose
This document defines the **user roles** and **operational modes** within the Survey Management Platform (SMP).  
It describes how each role interacts with the platform, their core responsibilities, and how operational modes (Preparation, Active Logging, and Review) influence feature accessibility and decision-making authority.

These definitions ensure operational safety, clear accountability, and efficient collaboration across distributed survey operations.

---

## Scope & Context
The SMP supports **multi-mission, multi-role collaboration** between onshore and offshore personnel.  
Access is governed by **global role-based permissions**, where users are assigned to missions with specific roles through a global user management layer.  

Operational modes define system state and determine which functions are active or locked, ensuring safe transitions throughout the mission lifecycle.

---

## Key Concepts / Framework

| Concept | Description | Purpose |
|----------|--------------|----------|
| **Global RBAC (Role-Based Access Control)** | User permissions are managed globally. Each user may hold different roles in different missions. | Enables flexible, mission-specific role assignments while maintaining centralized control. |
| **Operational Mode** | Defines the mission’s current lifecycle phase. | Controls system behavior, tool availability, and safety locks. |
| **Mission Context** | Determines which mission’s data, controls, and metrics are active. | Ensures coherent data display across screens. |
| **Cross-Mission Awareness** | Enables users to monitor multiple missions concurrently. | Supports efficient remote oversight and task switching. |

---

## User Roles

| Role | Primary Focus | Core Responsibilities | Typical Screens / Tools |
|------|----------------|------------------------|--------------------------|
| **Survey Operator** | Execute and monitor live survey operations across one or more missions. | - Control sensors and manage logging.<br>- Monitor system and data health across multiple missions.<br>- Ensure the quality of acquired data.<br>- Add notes to Online Log.<br>- Apply configuration templates during preparation. | Triage Hub, Mission Deck, Stream Viewer, Navigation, Online Log. |
| **Senior Surveyor** | Technical oversight and calibration. | - Lead mobilisation and sensor calibration.<br>- Support troubleshooting during operations.<br>- Validate configuration and QC thresholds. | Mission Deck, Configuration Manager, Diagnostics. |
| **Project Execution Coordinator (PEC)** | Oversee operational coordination and mission performance. | - Track mission health and progress.<br>- Coordinate onshore/offshore communications.<br>- Oversee compliance and delivery progress. | Does not directly utilize the SMP |
| **Data Processor** | Post-processing and validation. | - Verify data integrity and completeness.<br>- Review logs and file transfers.<br>- Validate QC outcomes and file naming compliance.<br>- Generate post-mission summaries. | Online Log, File Transfer Monitor, Data Archives. |

> **Note:** Role permissions are managed through a **global RBAC system**, not mission-specific configuration.  
> The mechanism for user–mission assignment will be defined in a future phase.

---

## Operational Modes

| Mode | Description | Feature Availability | Notes |
|------|--------------|----------------------|-------|
| **Preparation** | Pre-mission configuration and calibration phase. | - Sensors can be added/removed.<br>- Templates can be applied.<br>- Thresholds adjustable.<br>- Diagnostics fully enabled. | Primarily used by Senior Surveyor and Survey Operator during setup (mobilization and calibration phases). |
| **Active Logging** | Live data acquisition phase. | - Sensor ON/OFF/Restart.<br>- QC overlays active in Stream Viewer.<br>- Alerts and health indicators live.<br>- Manual log entries available. | Survey Operator monitors multiple missions simultaneously. |
| **Review** | Post-mission assessment phase. | - Logging disabled.<br>- Configuration editable for next mission.<br>- Log and alert archives accessible.<br>- File transfer and completeness checks active.<br>- Export summaries enabled. | Used by Data Processor and Senior Surveyor for validation. |

---

## Role–Mode Interaction Matrix

| Role ↓ / Mode → | Preparation | Active Logging | Review |
|------------------|--------------|----------------|---------|
| **Survey Operator** | Configure and prepare mission; test sensors. | Control and monitor multiple missions; manage quality and live performance. | Review logs and data quality reports. |
| **Senior Surveyor** | Lead calibration and configuration; lock setup. | Support operations and monitor QC thresholds. | Validate data, update templates, prepare next setup. |
| **PEC** | Observe setup progress across missions. | Monitor health and mission timelines. | Review mission completion summaries. |
| **Data Processor** | Not involved in setup. | Read-only view of mission status. | Validate data and compile final reports. |

---

## Cross-Mission Visibility

| Component | Visibility | Description |
|------------|-------------|-------------|
| **Triage Hub** | Global | Displays all active missions with status and health. |
| **Online Log** | Global + Contextual | Allows filtering between all missions or the active mission. |
| **Mission Deck / Stream Viewer** | Contextual | Displays data for the selected active mission. |
| **Configuration Manager** | Contextual | Loads configuration for the selected mission only. |
| **File Transfer Monitor** | Global summary + per-mission detail | Tracks file status and delivery progress. |

---

## User Safety & Access Design Principles

1. **Safety by Design:**  
   - Only authorized roles can lock or unlock configurations.  

2. **Global RBAC Integration (Future):**  
   - User roles and permissions will be defined globally, with mission-level assignments made via user management.  
   - A single user can have different roles across missions (e.g., Operator in one, Observer in another).  

3. **Read-Only Assurance:**  
   - For some parameters, configuration is locked to prevent accidental disruptions.  

4. **Cross-Mission Isolation:**  
   - Missions maintain independent operational states to prevent data cross-contamination.  

---

## Acceptance Criteria

- Survey Operators can monitor and manage multiple missions concurrently.  
- Each role’s visibility and tool access align with responsibilities.  
- Operational modes enforce correct locking behavior automatically.  
- Global RBAC architecture supports user-to-mission role assignment.  
- Cross-mission and contextual views operate independently and safely.  
- All user actions are logged for traceability.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Global RBAC Definition** | Confirm structure and management interface for user-role assignments. |
| **Mission Ownership** | Determine how missions are transferred between users. |
| **Concurrent Mission Load** | Establish upper limit of missions per operator for safe monitoring. |
| **UI Role Personalization** | Explore role-specific UI presets or shortcuts. |

---

### Summary Statement

> The **User Roles and Operational Modes** framework defines how SMP users operate safely and efficiently across multi-mission environments.  
> By introducing global role-based management and flexible mission assignments, the platform enables scalable operations, continuous oversight, and clear role accountability while maintaining mission-level isolation and safety.

---

**End of Document**
