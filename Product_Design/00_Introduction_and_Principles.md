# 00_Introduction_and_Principles.md
**Version:** 0.1  
**Date:** 2025-11-08  
**Owner:** Product Design  
**Status:** Draft  

---

## 1. Purpose of the Survey Management Platform (SMP)

The **Survey Management Platform (SMP)** is a unified operational environment that enables marine survey teams to plan, execute, monitor, and manage multiple concurrent missions with full situational awareness and data traceability.

It provides a **single command surface** across vessel systems, sensors, and mission states—designed to reduce operational complexity, enhance decision-making, and ensure the integrity of acquired survey data.

SMP bridges the gap between **control systems** and **data assurance workflows**, creating a continuous loop of command, observation, and verification.

---

## 2. Core Design Principles

| Principle | Description |
|------------|--------------|
| **Command & Control** | Centralized yet modular mission execution. Operators issue commands and view system state in real time. |
| **Active Monitoring** | Continuous, contextual awareness of system and sensor health to anticipate issues before failure. |
| **Traceability by Design** | Every command, event, and configuration change is logged for accountability and audit. |
| **Multi-Mission Safety** | Operators can safely manage multiple missions concurrently without cross-contamination of data or commands. |
| **Operator-Centric Workflow** | Interfaces designed for the pace, focus, and stress level of real survey operations—prioritizing situational clarity and minimal friction. |
| **Consistency Across Screens** | Uniform interaction patterns and visual hierarchy enable fluid multi-screen operation. |
| **Transparency of State** | At any time, users can see what the system is doing, what has been done, and what is about to happen. |

---

## 3. Product Vision

> “A single operational platform that empowers surveyors to command, monitor, and validate multiple missions in real time—safely, transparently, and with total confidence in data quality.”

SMP is both **mission control** and **assurance layer**, supporting:
- **Live execution:** sending commands, managing sensors, and monitoring outputs.
- **Quality assurance:** surfacing sensor health and performance indicators continuously.
- **Accountability:** creating a persistent mission log that connects all actions and outcomes.

---

## 4. Target Users

| Role | Responsibilities | SMP Perspective |
|------|------------------|-----------------|
| **Surveyor** | Operates missions, monitors data collection, manages real-time QC. | Primary user of Mission Deck and Stream Viewer. |
| **Senior Surveyor** | Oversees multiple missions, supports troubleshooting and configuration. | Supervisory access to all mission contexts. |
| **Party Chief (PEC)** | Ensures safe operations, validates mission readiness and compliance. | Oversees Triage Hub and mission summaries. |
| **Data Manager** | Manages data flow, file integrity, and client deliverables. | Uses Online Log and File Transfer views. |
| **IT / Systems Engineer** | Maintains platform reliability, network, and system configurations. | Accesses Diagnostics and Configuration tools. |

---

## 5. Operational Context

### 5.1 Marine Survey Environment
- High-complexity, multi-sensor operations (MBES, SSS, SBP, INS, GNSS, Cameras, CTD, USBL).
- Workstations are typically **multi-screen** (8 screens in a 4×2 grid).
- Operations are **mission-driven**: each mission represents a defined survey activity.
- Network reliability, synchronization, and recording status are mission-critical.

### 5.2 Operator Workspace Layout (Baseline)
| Screen | Function | Scope |
|---------|-----------|-------|
| **1. Triage Hub** | Global mission overview and activation | Cross-mission |
| **2. Mission Deck** | Command and control surface | Active mission |
| **3. Navigation / Reference** | Vessel navigation and situational map | Mission |
| **4–5. Stream Viewer(s)** | Live sensor outputs | Mission |
| **6–7. Diagnostics / Config Tools** | Troubleshooting and configuration | Mission |
| **8. Online Log** | Mission and system log | Cross-mission |

Each screen contributes to a **cohesive operational picture**, with the active mission context propagated across mission-scoped windows.

---

## 6. Design Objectives

1. **Unify disparate tools** into a cohesive operational ecosystem.  
2. **Minimize operator workload** through clear visual hierarchy and consistent controls.  
3. **Enable safe multitasking**—operators can manage several missions concurrently without risk of cross-command.  
4. **Provide transparency** of data health, system state, and event history.  
5. **Support structured collaboration** between roles (Surveyor ↔ Data Manager ↔ PEC).  
6. **Deliver visual calmness**—no flashing or intrusive behavior; clarity through information design.

---

## 7. Key Experience Principles

| Principle | Intent | Example |
|------------|--------|----------|
| **At-a-Glance Awareness** | Operators must interpret mission state within 3 seconds. | Compact health bars, color-coded status, trend micro-charts. |
| **No Dead Ends** | Every alert or metric leads to a diagnostic or log entry. | Clicking a metric opens Diagnostics. |
| **Mission Context Continuity** | Changing mission updates all relevant screens simultaneously. | Mission broadcast behavior. |
| **Progressive Disclosure** | Detail appears on demand, reducing cognitive noise. | Health overview → click for detailed metrics. |
| **Data Integrity by Default** | The system should prevent data loss or silent failure. | File Transfer verification states visible at all times. |
| **Human Confirmation** | Key actions require acknowledgment to prevent accidental disruption. | Stop Logging → confirmation prompt. |

---

## 8. SMP in One Sentence

> The Survey Management Platform is the surveyor’s operational command environment — a distributed, synchronized workspace designed to control, monitor, and validate marine survey missions with precision and traceable accountability.

---

### End of Document
