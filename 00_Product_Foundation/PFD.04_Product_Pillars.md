---
doc_id: PFD.04
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [product-pillars, command-and-control, active-monitoring, strategy]
---

# PFD.04 – Product Pillars

<!--
Changes made:
1) Added standardized front-matter for consistency across the repository.
2) Updated H1 heading to the standardized format (“# PFD.04 – Product Pillars”).
3) No internal links in source; none updated.
4) All body text below remains verbatim.
-->

*(Originally titled “Ocean Infinity – Survey Management Platform (SMP)”)*
  
**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** SMP Product Design & Strategy  
**Status:** Updated Draft – Workshop-Aligned

---

## 1. Purpose

This document defines the **core product pillars** that guide the Survey Management Platform (SMP) — specifically the two operational priorities identified in the workshop:

1. **Command & Control (C&C)**
2. **Active Monitoring (AM)**

Each pillar integrates validated workshop priorities (short-term and long-term) and reflects the strategic goal of **reducing operational complexity** while enabling **operator-level multi-mission efficiency**.

---

## 2. Overview of Pillars

| **Pillar**            | **Goal**                                                                            | **Strategic Outcome**                                                                                |
| --------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Command & Control** | Simplify and centralize the safe execution of operational commands across missions. | Empower surveyors to manage multiple missions efficiently through automation and role-based control. |
| **Active Monitoring** | Provide real-time, unified awareness of data, sensor health, and mission progress.  | Enhance data integrity, QC consistency, and early anomaly detection across concurrent operations.    |

---

## 3. Pillar 1 – Command & Control (C&C)

### 3.1 Vision

To enable safe, centralized, and efficient execution of mission control actions across all connected systems and sensors — allowing a single operator to perform coordinated, traceable operations over multiple concurrent missions.

### 3.2 Design Intent

* **Simplify operational complexity** by integrating control functions into a single environment.
* **Standardize control behavior** through role-based permissions and feedback loops.
* **Ensure safety** through validation and acknowledgement loops.
* **Support collaboration** by allowing assistance and shared diagnostics without disrupting mission workflows.

### 3.3 Short-Term Priorities (Workshop-Aligned)

| **Capability**                         | **Purpose**                                                                           | **Outcome**                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **ON/OFF/Restart Commands**            | Execute safe control of sensor data streams.                                          | Streamlined sensor recovery and reduced manual intervention. |
| **Start/Stop Logging Commands**        | Manage mission logging manually or automatically.                                     | Prevents data loss and standardizes workflow.                |
| **Multi-User Accessibility**           | Allow supervisors or seniors to access and troubleshoot sensors without interference. | Faster resolution and reduced downtime.                      |
| **Configuration Templates / Profiles** | Save and apply predefined setups for mission types (e.g., Pipeline Inspection).       | Consistent configurations and faster mobilization.           |
| **Online Log Integration**             | Automatically record “Line start / Line end / Deviation” events.                      | Seamless traceability and audit history.                     |
| **I/O Tool from Sensor to Sensor**     | Route or output data streams between sensors.                                         | Improved integration and flexibility across systems.         |

### 3.4 Long-Term Priorities (Workshop-Aligned)

| **Capability**                             | **Purpose**                                          | **Outcome**                                               |
| ------------------------------------------ | ---------------------------------------------------- | --------------------------------------------------------- |
| **Requesting Setting Changes (Ack Loop)**  | Send–Ack–Working–Finished confirmation flow.         | Increased safety and transparency of remote operations.   |
| **Auto-Diagnostics / Health Check**        | Routine connection and driver checks.                | Early fault detection and proactive maintenance.          |
| **User-Defined Metrics (Advanced)**        | Define custom derived values (e.g., INS drift rate). | Power-user customization and advanced QC.                 |
| **Configurable Thresholds**                | Define acceptable operational ranges.                | Early identification of off-nominal conditions.           |
| **Configuration Lock / Permission System** | Prevent unauthorized edits during live acquisition.  | Operational safety and control integrity.                 |
| **File Configuration (Split/Size/Time)**   | Define file storage and splitting logic.             | Streamlined data management and backup.                   |
| **Auto-Pilot / DP System Integration**     | Interface with DP systems for line/position holding. | Enhanced vessel stability during autonomous survey lines. |
| **Read/Write Permissions**                 | Restrict edit/delete rights by role.                 | Role-based safety enforcement.                            |
| **Changelog Journal**                      | Record all configuration changes over time.          | Full operational traceability.                            |
| **Rollback to Previous Config**            | Restore last working configuration after issue.      | Rapid recovery and minimal downtime.                      |

### 3.5 Success Metrics

| **Category**               | **Metric**                         | **Target**           |
| -------------------------- | ---------------------------------- | -------------------- |
| **Setup Efficiency**       | Average setup time per mission     | -30%                 |
| **Safety & Reliability**   | Command execution success rate     | ≥ 99.5%              |
| **Traceability**           | Logged control actions per mission | 100%                 |
| **Operational Efficiency** | Missions controlled per operator   | ≥ 2 sustained safely |

---

## 4. Pillar 2 – Active Monitoring (AM)

### 4.1 Vision

Deliver unified, real-time situational awareness across all mission contexts — allowing operators to detect, prioritize, and respond to issues faster while maintaining multi-mission oversight.

### 4.2 Design Intent

* **Enable clarity at scale**: visualize multiple missions without cognitive overload.
* **Focus attention dynamically**: surface only critical events and thresholds.
* **Provide continuous awareness**: unify QC, health, and sensor data views.
* **Integrate traceability**: every alert, anomaly, and QC deviation logged automatically.

### 4.3 Short-Term Priorities (Workshop-Aligned)

| **Capability**                      | **Purpose**                                                | **Outcome**                                 |
| ----------------------------------- | ---------------------------------------------------------- | ------------------------------------------- |
| **Live Sensor Stream Viewer**       | Display real-time graphical sensor outputs.                | Immediate fault and data awareness.         |
| **Configurable Thresholds**         | Define metric limits (e.g., SNR > 25dB).                   | Flexible QC monitoring.                     |
| **Connection & Sync State**         | Show clock drift, timing sync, and heartbeats.             | Early detection of system issues.           |
| **Auto-Validation of Parameters**   | Highlight values outside recommended ranges.               | Automatic QC and reduced manual checks.     |
| **Sensor Quickview**                | Display essential sensor details (status, downtime, etc.). | Rapid visual context for multiple missions. |
| **Deviation Indicator**             | Alert when vessel deviates from line tolerance.            | Real-time navigation accuracy.              |
| **Alert Severity Levels**           | Distinguish minor vs. critical issues.                     | Prioritized operator focus.                 |
| **Status Indicators (Health)**      | Traffic light color-coded system states.                   | Quick situational understanding.            |
| **Alert Markers**                   | Visual flags for data dropouts or anomalies.               | Easier incident traceability.               |
| **Quality Status Indicator**        | Simple color flag (Green/Amber/Red) based on thresholds.   | Standardized QC summary.                    |
| **Auto-Diagnostics / Health Check** | Routine connection integrity verification.                 | Preventive awareness before failure.        |
| **Quality Scoring (Optional)**      | Weighted index summarizing overall mission data quality.   | Quantified QC performance measure.          |

### 4.4 Long-Term Priorities (Workshop-Aligned)

| **Capability**                        | **Purpose**                                                  | **Outcome**                                |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------ |
| **Overlay Controls**                  | Toggle navigation, intensity, or grid layers.                | Enhanced spatial context.                  |
| **Snapshot Capture**                  | Take instant timestamped stills of sensor outputs.           | Quick reference for anomalies.             |
| **Weather/Tidal Overlay**             | Integrate environmental data layers.                         | Broader situational context.               |
| **Cross-Sensor Correlation**          | Overlay correlated metrics (e.g., INS drift vs. MBES noise). | Identify cause-and-effect patterns.        |
| **Track History Replay**              | Review recent vessel paths and anomalies.                    | Short-term post-mission validation.        |
| **Linked Navigation View**            | Mini-map overlay showing acquisition locations.              | Geospatial awareness.                      |
| **Multi-Sensor Split View**           | Display multiple data sources side-by-side.                  | Comparative awareness between sensors.     |
| **Waypoint Management**               | Create and manage mission reference points.                  | Simplified navigation and survey planning. |
| **Survey Area Completion View**       | Visualize heatmap of covered vs. remaining areas.            | Operational progress insight.              |
| **Line Progress Indicator**           | Show % line completed, deviation, distance remaining.        | Performance monitoring.                    |
| **Signal Flow Diagram (Interactive)** | Visualize sensor → network → acquisition → storage.          | Diagnostic insight and issue tracing.      |
| **Color-Coded Quality Layer**         | Overlay color-based QC metrics (e.g., density, SNR).         | Unified data quality visualization.        |

### 4.5 Success Metrics

| **Category**              | **Metric**                       | **Target**           |
| ------------------------- | -------------------------------- | -------------------- |
| **Situational Awareness** | Time to detect anomaly           | ≤ 2 minutes          |
| **Data Quality**          | QC alert accuracy                | ≥ 95%                |
| **Operator Efficiency**   | Missions monitored per operator  | ≥ 2 sustained safely |
| **Resilience**            | Downtime before alert escalation | ≤ 1 minute           |

---

## 5. Inter-Pillar Dependencies

| **Dependency Area**                       | **Relationship**                                                           | **Impact**                                                |
| ----------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Online Log & Traceability**             | Common infrastructure supporting both pillars.                             | Ensures visibility and auditability across missions.      |
| **Alerts & Command Feedback**             | Monitoring drives control responses; control actions feed monitoring logs. | Closed operational feedback loop.                         |
| **Configuration Templates & Permissions** | Shared foundation for safety and efficiency.                               | Consistent configurations and safe concurrent operations. |
| **RBAC & Collaboration Framework**        | Enables multi-user session support and assistance.                         | Prevents interference and ensures accountability.         |

---

## 6. Strategic Outcomes

1. **Operational Efficiency:** Fewer operators managing more missions safely.
2. **Situational Awareness:** Faster detection and triage of mission-critical issues.
3. **Traceability:** Complete log of all control, alert, and QC events.
4. **Collaboration:** Cross-role assistance and supervision with minimal disruption.
5. **Simplicity at Scale:** Operators remain focused through clear, contextual interfaces.

---

**End of Document**
*“Command and control what matters; monitor everything that does.”*
