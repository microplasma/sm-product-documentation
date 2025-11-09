---
doc_id: PDD.07
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [future-directions, design-research, open-items, roadmap-alignment, smp-evolution]
---

# 07_Future_Directions_and_Open_Items

## Purpose
This document consolidates all **outstanding design questions, open topics, and future directions** identified across the Survey Management Platform (SMP) design documentation.  
It provides a single reference for tracking unresolved items, guiding validation, and prioritizing design research activities during the next stages of product definition.

---

## Scope & Context
This document covers **design-level** issues only — not implementation or engineering.  
It draws from documents `PDD.00` through `PDD.06`, capturing what remains uncertain or requires further validation.  

Each open item includes:
- The **topic** or decision area.  
- The **current assumption** (if defined).  
- The **open question** to resolve.  
- The **next step or proposed action**.

---

## Strategic Design Themes

| Theme | Objective | Direction |
|--------|------------|-----------|
| **Scalability & Concurrency** | Enable stable multi-mission operations from a single surveyor workstation. | Refine performance, mission state caching, and visual clarity when handling 2–3 missions concurrently. |
| **Safety & Control Assurance** | Ensure no accidental interruptions to data logging or mission control. | Reinforce design principles where user actions are deliberate and reversible. |
| **User Experience Maturity** | Improve usability, readability, and ergonomics across multi-screen setups. | Validate mission context switching and operator awareness through prototyping. |
| **Data Consistency & Interoperability** | Maintain synchronized configuration, telemetry, and thresholds across modules. | Continue refining the data and configuration schema (see PDD.05). |
| **Collaboration & Remote Operations Evolution** | Support distributed survey teams and onshore/offshore coordination. | Explore shared log visibility and remote session synchronization. |

---

## Open Items by Domain

### 🧭 Triage Hub
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **Mission Grouping** | One mission per vessel; 2–3 missions max per operator. | Should missions be grouped by vessel, area, or campaign? | Validate with operational teams. |
| **Mission Card Density** | Shows core metrics and status color. | Should additional live indicators (e.g., QC status) appear on mission cards? | Prototype layout variations and test with users. |
| **Health Summary Update Rate** | 1–2 Hz refresh cadence. | Confirm acceptable refresh rate for overview metrics without performance cost. | Measure during simulation. |

---

### ⚙️ Mission Deck
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **Health & Quality Visualization** | Uses color-coded tiles and progress feedback. | What visualization components best convey health without clutter? | Prototype various compact visualization types. |
| **Pre-Check Workflow** | Supports pre-mission readiness. | Should this be expanded into a dedicated pre-check screen? | Gather field user feedback. |
| **Alert Behavior** | Alerts never trigger automatic logging stops. | Should some critical alerts (e.g., sensor offline) require explicit operator acknowledgment? | Test alert UX patterns. |
| **Tool Access Persistence** | Tools open in modal, maintain mission context. | Should tool state persist across mission switches? | Validate via operational workflow study. |

---

### 🌊 Stream Viewer
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **Overlay Customization** | QC overlays toggle per feed, not global. | Should overlays be user-customizable or standardized per mission? | Define policy with data quality stakeholders. |
| **Feed Density Limit** | 4–6 feeds concurrently for performance. | Confirm maximum supported feeds per workstation. | Conduct performance testing. |
| **Camera Feeds** | Simple live tiles with QC overlays. | Should future iterations support capture or annotation? | Defer to Phase 2 research. |
| **Cross-Linking Alerts** | Alerts generated in overlays remain local. | Should critical QC breaches also appear in Mission Deck health summary? | Review integration path. |

---

### 🧰 Configuration Manager
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **RBAC Scope** | Global role-based permissions; not mission-specific. | How will RBAC integrate with Configuration Manager visibility and lock states? | Define integration with Global User Management. |
| **Template Inheritance** | Flat structure for now. | Should templates inherit from vessel or global defaults? | Evaluate with engineering. |
| **Version Control Visualization** | Versioning exists, but no UI diff view. | Should operators see change diffs between versions? | Prototype diff visual concepts. |
| **Sensor Removal Safety** | Requires confirmation. | Should dependencies (e.g., active feeds) block removal? | Validate in mock simulation. |

---

### 🧾 Online Log
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **Quick Entry** | Text + tag input. | Should we add voice or preset command shortcuts? | User research with operators. |
| **Cross-Link Behavior** | Clicking opens related module (e.g., Config, Deck). | How deep should cross-linking go (e.g., open exact sensor)? | Define interaction depth. |
| **Alert Logging** | All alerts automatically logged. | Should alert severity influence log visibility or filtering? | Prototype filtering behavior. |
| **Data Retention** | Archived after mission completion. | Define retention period and export structure. | Align with data governance requirements. |

---

### 🌐 Global & Infrastructure
| Topic | Current Assumption | Open Question | Next Step |
|--------|--------------------|----------------|------------|
| **RBAC System Location** | Global user management layer (TBD). | What interface manages user-role assignments per mission? | Define preliminary user management workflow. |
| **Multi-Screen Context Synchronization** | Handled by mission context propagation. | Should operators be able to lock screens to independent missions? | Validate with multi-mission control users. |
| **Offline Behavior** | Not yet defined. | What functions remain available without live telemetry? | Develop offline mode scenarios. |
| **Network Resilience** | Standard TCP/UDP stream ingestion. | Should critical systems have retry/buffer behavior? | Identify critical data paths with engineering. |

---

## Research & Prototyping Priorities

| Priority | Focus Area | Goal |
|-----------|-------------|------|
| **1** | Mission Deck Health Visualization | Evaluate compact, accessible visualizations for critical metrics. |
| **2** | Stream Viewer Overlay Performance | Test overlay refresh rates and feed limits under load. |
| **3** | Multi-Mission Workflow | Validate context switching efficiency and operator mental load. |
| **4** | Quick Entry Ergonomics | Design and test rapid logging and tagging shortcuts. |
| **5** | Template & Threshold Management | Validate usability of configuration editing and rollback. |
| **6** | Multi-Screen Synchronization | Confirm consistency of mission context across displays. |

---

## Cross-Functional Dependencies

| Dependency | Description | Linked Documents |
|-------------|--------------|------------------|
| **Data Schema ↔ Thresholds & Overlays** | Threshold definitions in Configuration Manager drive Stream Viewer overlays and Mission Deck alerts. | PDD.04.04, PDD.04.03 |
| **RBAC ↔ User Roles** | Global RBAC model governs access to mission features. | PDD.06 |
| **Mission Lifecycle ↔ Logging** | Transitions between modes affect configuration locks. | PDD.04.02, PDD.04.04 |
| **Telemetry ↔ Online Log** | Events from telemetry feed auto-log for traceability. | PDD.05, PDD.04.05 |
| **Network & Performance** | Affects refresh rate and mission concurrency. | Cross-cutting dependency. |

---

## Alignment & Decision Log

| Decision Area | Status | Owner | Notes |
|----------------|---------|--------|-------|
| **Logging safety model** | ✅ Confirmed | Design | Logging never stops automatically. |
| **RBAC location** | 🟡 Pending | Product | Global user management, not mission-level. |
| **Multi-Mission Scope** | ✅ Confirmed | Design | Surveyor can handle 2–3 missions concurrently. |
| **Alert severity model** | ⚙️ In Progress | UX | Define alert hierarchy and visual treatment. |
| **Offline Mode** | 🔍 Under Research | Engineering | Define telemetry caching behavior. |

---

## Next Steps & Planning

1. **Prototype Testing**  
   - Begin mission context and health visualization tests in Codex/Cursor prototype.  
   - Measure cognitive load during multi-mission monitoring sessions.

2. **Design Validation Workshops**  
   - Conduct cross-role validation with operators, seniors, and PECs.  
   - Focus on alert handling, configuration lock behavior, and multi-screen flow.

3. **RBAC Architecture Definition**  
   - Collaborate with IT/Engineering to define global user-role assignment model.  

4. **Documentation Iteration**  
   - Update all PDD files as new insights and decisions emerge from prototyping.  

---

### Summary Statement

> The **Future Directions and Open Items** document provides a structured overview of all unresolved design elements within the SMP ecosystem.  
> It connects conceptual design with future implementation, ensuring continuity, traceability, and clarity as the platform evolves toward field validation and production readiness.

---

**End of Document**
