---
doc_id: PDD.00
version: 0.1.0
last_updated: 2025-11-08
status: draft
owners: [design@survey-platform.io]
tags: [introduction, principles, foundation, design]
---

# PDD.00_Introduction_and_Principles

## Purpose
This document introduces the **Survey Management Platform (SMP)**—a unified operational environment that enables marine survey teams to **plan, execute, monitor, and manage multiple concurrent survey missions** with full situational awareness and data traceability.  
It defines the **design philosophy**, **core principles**, and **context of use** that underpin all subsequent design and functional specifications.

---

## Scope & Context
The SMP serves as the operator’s central **command, monitoring, and assurance system**, designed for real-time management of offshore survey operations.  
It provides:
- Mission-level **Command & Control** for safe and consistent execution.  
- Continuous **Active Monitoring** of system and sensor health.  
- Built-in **Traceability**, ensuring every event, configuration, and command is recorded.  
- A flexible **multi-screen environment**, enabling concurrent mission management.

The platform is used by survey teams operating from **offshore vessels**, **remote operation centers**, or **hybrid control environments**, where network resilience, time synchronization, and data integrity are critical.

---

## Key Concepts / Framework

### Core Design Principles

| Principle | Description |
|------------|--------------|
| **Command & Control** | A central mission workspace where operators issue commands and monitor outcomes with immediate feedback. |
| **Active Monitoring** | Real-time visibility of system, sensor, and environmental conditions; rapid surfacing of degradation trends. |
| **Traceability by Design** | Every operational change—command, alert, configuration, or data event—is captured, time-stamped, and attributable. |
| **Multi-Mission Safety** | Each mission is sandboxed; concurrent operations never interfere with one another’s commands or data streams. |
| **Operator-Centric Workflow** | Interfaces structured around operational tasks, ensuring minimal friction, clarity under pressure, and consistent mental models. |
| **Consistency Across Screens** | Shared design language and behavior across all screens reduce cognitive switching costs. |
| **Transparency of State** | At any moment, users can understand what the system is doing, what has occurred, and what requires attention. |

---

## Functional or UX Details

### Product Vision
> “A single operational platform that empowers survey teams to command, monitor, and validate multiple marine survey missions safely, transparently, and with full confidence in data quality.”

SMP combines mission control with assurance capabilities—enabling surveyors to:
- **Execute** actions across missions with consistent workflows.  
- **Monitor** key metrics that indicate system health and sensor quality.  
- **Record and verify** every event for audit and collaboration.  

### Target User Roles

| Role | Responsibilities | SMP Perspective |
|------|------------------|-----------------|
| **Project Execution Coordinator (PEC)** | Coordinates project execution and communication between onshore and offshore teams. | Oversees global mission states in the **Triage Hub**; ensures operational alignment. |
| **Senior Surveyor** | Responsible for mobilisation, calibration, and problem-solving during operations. | Uses **Mission Deck** and **Diagnostics** tools to validate readiness and troubleshoot issues. |
| **Survey Operator** | Responsible for acquiring and supervising real-time data collection during survey operations. | Primary operator of **Mission Deck** and **Stream Viewer**; manages mission execution. |
| **Data Processor** | Responsible for post-processing, analysis, and validation of acquired survey data. | Interacts with **Online Log** and **mission outputs** for verification and reporting. |
| **IT / Systems Engineer** | Maintains platform reliability, network, and configuration integrity. | Uses **Configuration Manager** and **Diagnostics** modules. |

---

### Operational Context

Marine survey environments are complex, sensor-dense systems requiring synchronization and precision across multiple data acquisition subsystems (e.g., MBES, SSS, SBP, INS, GNSS, Camera, CTD, USBL).

Typical workstation layout consists of **8 screens arranged in a 4×2 grid**, allowing surveyors to distribute functions logically across physical displays.

| Screen | Function | Mission Context |
|---------|-----------|----------------|
| **1. Triage Hub** | Global mission overview and activation | **Cross-mission** |
| **2. Mission Deck** | Command and control surface | **Active mission** |
| **3. Navigation / Reference** | Vessel position and situational map | **Active mission** |
| **4–5. Stream Viewer(s)** | Live sensor data and QC monitoring | **Active mission** |
| **6–7. Diagnostics / Config Tools** | Troubleshooting and system configuration | **Active mission** |
| **8. Online Log** | Persistent operational and system log | **Cross-mission** |

> All screens except for **Triage Hub** and **Online Log** are contextual to the currently active mission.

---

### Design Objectives

1. **Unify** tools and processes into a coherent operational experience.  
2. **Simplify** the operator’s decision path through contextual information and clear prioritization.  
3. **Ensure safety** in multi-mission environments by isolating commands and data.  
4. **Provide transparency** of mission state, system health, and data integrity.  
5. **Support collaborative workflows** across onshore/offshore and between disciplines.  
6. **Design for calm clarity**, avoiding unnecessary visual noise or distractions.

---

## Acceptance Criteria

- SMP principles are clearly documented and understood by all design and engineering stakeholders.  
- Roles, responsibilities, and operational contexts are explicitly mapped.  
- The relationship between Command & Control, Active Monitoring, and Traceability is clearly expressed.  
- The multi-screen, multi-mission context is fully defined for future reference in UX and functional design files.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Alert-to-Action Patterns** | Define the standard mechanism for actionable insights (e.g., “View recommended action” within alerts). |
| **Mission Context Transition** | Confirm user flow for switching missions under high operational load. |
| **Cross-Mission Data Policies** | Validate how logs and metrics are segmented between missions. |
| **Calibration Workflow** | Awaiting definition from Survey Operations on calibration and validation data handling. |

---

### Summary Statement

> The **Survey Management Platform (SMP)** is designed to unify marine survey operations under a single, operator-centered environment—balancing command precision, monitoring clarity, and end-to-end traceability across concurrent missions.

---

**End of Document**
