---
doc_id: UXR.07
version: 0.1.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, sensors, taxonomy, ois]
---

# UXR.07 - Sensor Taxonomy

<!--
Changes made:
1. Created a sensor taxonomy reference to support OIS design and future SME-review skill work.
2. Classified sensors by operational behavior, not only vendor/model.
3. Grounded the taxonomy in the sensor catalog, usage summary, and UX research set.
-->

**Version:** 1.0  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Draft Reference

---

## 1. Purpose

This document defines a practical **sensor taxonomy** for OI Survey (OIS).

Its purpose is to help design and review work answer a more useful question than "what hardware exists?":

> **How should this system behave in the product model?**

This taxonomy groups sensors and related systems by **operational behavior**, **control depth**, **dependency role**, **deployment context**, and **validation timing**.

It is intended to support:

- product and UX design decisions
- prototype prioritization
- workflow analysis
- future Codex skill references for SME-style review

---

## 2. How To Use This Reference

Use this file when deciding:

- whether a system should be a first-class control surface
- whether it should be represented mainly as a dependency or confidence signal
- whether it is better modeled as part of a parent system
- whether its truth is established live, after recovery, or after ingest/post-processing

Working rule:

- do not assume every catalog item should become its own standalone pane
- do not assume every sensor supports the same command model
- do not assume live visibility means live control

---

## 3. Primary Acquisition Sensors

These are the systems most likely to anchor the operator's live work surface because they directly define survey output quality during acquisition.

### 3.1 MBES

- **Examples:** `Kongsberg EM2040`, `R2Sonic 2026 Dual-head`
- **Typical role:** first-class acquisition sensor
- **Operational focus:** coverage, swath quality, readiness, line-time QC
- **Design implication:** should remain a top-tier reference workflow for control, monitoring, and config-to-runtime integrity

### 3.2 SSS

- **Examples:** `Edgetech 4205`
- **Typical role:** first-class acquisition sensor
- **Operational focus:** corridor imaging, anomaly detection, revisit decisions, waterfall interpretation
- **Design implication:** deserves dedicated live-view and anomaly-logging workflows

### 3.3 SBP

- **Examples:** `Innomar Medium-100`
- **Typical role:** first-class acquisition sensor
- **Operational focus:** sub-bottom quality, channel configuration, line-time monitoring, readiness
- **Design implication:** should be treated as a serious live-operational sensor, not a generic chart surface

### 3.4 Magnetometer / Pipe Tracker / Related Survey Sensors

- **Examples:** `Geometrics G-882`, `Teledyne TSS440 / 660`
- **Typical role:** primary or supporting acquisition sensor depending on operation type
- **Operational focus:** event/target detection, overlay confidence, anomaly workflow
- **Design implication:** often needs simpler live display than MBES/SSS, but still strong linkage to position, events, and later interpretation

---

## 4. Supporting Navigation And Reference Systems

These systems often determine whether the primary acquisition picture can be trusted.

They may not always be the user's main screen focus, but they should heavily influence readiness and confidence.

### 4.1 INS / AHRS / Motion / Heading

- **Examples:** `SeaPath 385`, `POSMV Elite`, `Sprint500`, `SprintNav500`
- **Typical role:** operational dependency with high confidence impact
- **Design implication:** must be visible in readiness, dependency, and degraded-state logic

### 4.2 GNSS / Positioning

- **Examples:** `Veripos LD900`
- **Typical role:** dependency and trust signal
- **Design implication:** integration maturity may vary, but status and confidence remain critical

### 4.3 USBL / Acoustic Positioning

- **Examples:** `HiPAP`, `Ranger2 Pro`
- **Typical role:** primary dependency for subsea positioning workflows
- **Design implication:** should be modeled as operationally important even when command access is limited or indirect

### 4.4 Time Sync

- **Examples:** `Meinberg microSync rx100`
- **Typical role:** cross-cutting dependency system
- **Design implication:** timing integrity should be treated as a first-class readiness and audit concern

### 4.5 Sound Velocity Inputs

- **Examples:** `Valeport MiniSVS+P`, `Valeport Midas SVX2`
- **Typical role:** supporting environmental dependency
- **Design implication:** OIS should distinguish between "sensor connected" and "input trusted / QA-verified"

---

## 5. Infrastructure And Control Systems

These systems do not usually represent survey data products themselves, but they directly affect operational availability and command execution.

### 5.1 Power And Distribution

- **Examples:** `CyberPower 41004 PDU`, `MacArtney MUX`
- **Typical role:** infrastructure control system
- **Design implication:** should use command-and-impact semantics rather than sensor semantics

Working rule:

- infrastructure systems often deserve their own dedicated product model
- their main job is not measurement, but availability, routing, and downstream operational consequence

---

## 6. Coupled Or Parent-Child Systems

Some catalog items should not always be modeled as independent top-level objects.

### 6.1 Coupled Navigation Components

- **Examples:** `Sonardyne Syrinx DVL` tightly coupled to `SprintNav500`
- **Design implication:** may be better represented within a parent navigation or vehicle state model rather than as a separate control pane

### 6.2 Software-Mediated Components

- **Examples:** `MGC R3` through `SeaPath 385`
- **Design implication:** some state and functionality will be visible only through the parent system's interface or abstraction

Working rule:

- if the system is operationally meaningful but not independently managed, model it as a dependency, subcomponent, or contributing signal rather than as a fake standalone system

---

## 7. Delayed-Validation Or Self-Logging Devices

These systems break the assumption that the truth of acquisition is always known live.

### 7.1 Self-Logging Devices

- **Examples:** `Nortek Signature 500 ADCP`
- **Typical role:** deployed asset with delayed data validation
- **Design implication:** workflows should include deployment, recovery, ingest, and completeness/reconciliation, not just live monitoring

### 7.2 Download-After-Recovery Assets

- **Examples:** seabed-deployed or autonomous assets, including some OBN/AUV-related systems
- **Typical role:** mission object with post-recovery truth establishment
- **Design implication:** OIS should support lifecycle tracking and late validation rather than pretending these are ordinary live-controlled devices

---

## 8. Deployment Context Taxonomy

The same sensor family may behave differently depending on where and how it is deployed.

### 8.1 Vessel-Mounted

- Continuous operational context
- Strong tie to bridge/navigation/timing stack
- Usually better suited to line-time monitoring and control workflows

### 8.2 ROV-Mounted

- Coupled to vehicle health, pilot actions, and subsea positioning confidence
- Usually requires shared surveyor/pilot context

### 8.3 Towed / ROTV

- Strong dependence on tow geometry, altitude, layback, and sea-state effects
- Often favors corridor-progress and quick-look revisit workflows

### 8.4 AUV-Mounted

- Strong dependence on mission planning, autonomy, endurance, and post-recovery ingest
- Often supervised sparsely rather than controlled continuously

### 8.5 Seabed-Deployed

- Deployment and recovery become part of the operational truth model
- Completeness and traceability matter as much as live status

---

## 9. Operational Modeling Rules

Use these rules when deciding how OIS should represent a system:

1. **If the operator must actively manage it during live work, prefer first-class representation.**
2. **If it mainly affects trust in another sensor, prefer dependency-aware modeling.**
3. **If it is tightly coupled to another system, prefer parent-child representation over fake independence.**
4. **If truth is established after recovery or ingest, represent lifecycle and reconciliation explicitly.**
5. **If integration depth is limited, do not promise a richer command model than reality supports.**
6. **If a system is operationally critical but not directly controllable, make confidence and degraded-state behavior highly visible.**

---

## 10. Current Priority Families For OIS

Based on the material provided so far, the strongest priority signal appears to be:

### 11.1 First-Tier Reference Families

- `MBES`
- `SSS`
- `SBP`
- `Magnetometer`

These appear to be the strongest reference set for shaping the geophysical experience.

### 11.2 Critical Dependency Families

- `INS / AHRS`
- `GNSS`
- `USBL`
- `Time Sync`
- `SVS / SVP`

These should strongly influence readiness, trust, and degraded-state semantics.

### 11.3 Important Specialized Or Non-Uniform Families

- `PDU / MUX`
- `Pipe Tracker`
- `Camera`
- `ADCP`
- `DVL`

These are important, but they require more differentiated modeling rather than a one-size-fits-all sensor pattern.

---

## 11. Known Unknowns

This taxonomy is grounded, but still incomplete in some areas.

Open questions:

- exact mapping of sensor families to each operation type across the fleet
- which catalog items should become first-class OIS control surfaces in the near term
- where vehicle-specific or vessel-specific workflows materially differ
- which systems are operationally important but commercially or technically difficult to integrate deeply

---

## 12. Canonical Sources

- `UXR.00_User_Research_Summary.md`
- `UXR.02_Operation_Types_and_Workflows.md`
- `UXR.03_Tasks_and_Tools_Matrix.md`
- `UXR.05_Role-Based_Insights.md`
- Sensor catalog
- Planner-derived sensor usage summary

---

**End of Document**
*"A useful product model starts by telling the truth about how systems actually behave."*
