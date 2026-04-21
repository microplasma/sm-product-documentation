---
doc_id: PFD.04
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [product-pillars, command-and-control, active-monitoring, strategy]
---

# PFD.04 - Product Pillars

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft - Workshop-Aligned

---

## 1. Purpose

This document defines the **core product pillars** that guide OI Survey (OIS), specifically the two operational priorities identified in the workshop:

1. **Command & Control (C&C)**
2. **Active Monitoring (AM)**

These pillars should now be understood within the updated product model: OI Survey as a **unified operational ecosystem** expressed through operational surfaces, with mission-level clarity and multi-mission support developing together.

---

## 2. Overview of Pillars

| **Pillar** | **Goal** | **Strategic Outcome** |
| --- | --- | --- |
| **Command & Control** | Support safe, legible operational action through the right mission-time surfaces. | Faster intervention, clearer consequence understanding, and stronger recovery behavior. |
| **Active Monitoring** | Provide real-time awareness of data quality, system health, and evidence. | Better mission-time judgment, earlier anomaly detection, and stronger survey confidence. |

---

## 3. Pillar 1 - Command & Control (C&C)

### 3.1 Vision

Enable safe, centralized, and efficient mission-time action across operational systems through surfaces that match the work being done, especially the **Systems** surface inside **Mission Deck**.

### 3.2 Design Intent

* **Simplify operational complexity** by reducing fragmentation between issue recognition, system context, and action.
* **Place action in the right surface** so overview and deep control do not compete for the same interaction role.
* **Ensure safety** through clear consequence language, validation, and acknowledgement patterns where needed.
* **Support collaboration** by making authority and traceability legible during mission-time work.

### 3.3 Short-Term Priorities (Workshop-Aligned)

| **Capability** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Mission Overview -> Systems handoff** | Move from decision surface to deep operational action without reconstructing context. | Faster, safer intervention. |
| **ON/OFF/Restart Commands** | Execute safe control of operational systems where direct command is appropriate. | Streamlined recovery and reduced manual intervention. |
| **Start/Stop Logging Commands** | Manage mission logging coherently with mission-time work. | Better continuity between operation and traceability. |
| **Configuration Templates / Profiles** | Save and apply predefined setups for mission types. | Consistent configurations and faster mobilization. |
| **Online Log Integration** | Automatically record key operational events and user actions. | Seamless traceability and audit history. |
| **Authority and Lock Visibility** | Make role boundaries visible where live changes carry consequence. | Safer collaboration and fewer accidental edits. |

### 3.4 Long-Term Priorities (Workshop-Aligned)

| **Capability** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Requesting Setting Changes (Ack Loop)** | Send -> Ack -> Working -> Finished confirmation flow. | Increased safety and transparency of remote operations. |
| **Auto-Diagnostics / Health Check** | Routine connection and driver checks. | Earlier fault detection and proactive maintenance. |
| **Configurable Thresholds** | Define acceptable operational ranges. | Stronger readiness and QC interpretation. |
| **Configuration Lock / Permission System** | Prevent unauthorized edits during live acquisition. | Operational safety and control integrity. |
| **Changelog Journal** | Record all configuration changes over time. | Full operational traceability. |
| **Rollback to Previous Config** | Restore last working configuration after issue. | Rapid recovery and minimal downtime. |
| **Broader validated multi-mission control patterns** | Extend command models beyond the active mission package where credible. | Future-state scale without weakening near-term mission clarity. |

### 3.5 Success Metrics

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Setup Efficiency** | Average setup time per mission | -30% |
| **Safety & Reliability** | Command execution success rate | >= 99.5% |
| **Traceability** | Logged control actions per mission | 100% |
| **Operational Clarity** | Reduced context reconstruction during intervention | Qualitative validation through operator review |

---

## 4. Pillar 2 - Active Monitoring (AM)

### 4.1 Vision

Deliver unified, real-time situational awareness across the mission package through the right combination of **Mission Overview**, **Data Monitor**, **Systems**, and related evidence/QC capabilities.

### 4.2 Design Intent

* **Enable clarity at mission time** by showing what matters now before overwhelming users with raw telemetry.
* **Focus attention dynamically** through issue, readiness, and QC signals that support judgment.
* **Provide stronger evidence interpretation** through Data Monitor capabilities and detached evidence workflows where needed.
* **Integrate traceability** so alerts, anomalies, and manual observations contribute to the operational record.

### 4.3 Short-Term Priorities (Workshop-Aligned)

| **Capability** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Mission Overview issue posture** | Summarize state, attention, issues, and next action for the active mission. | Faster mission-time orientation. |
| **Live Sensor Stream Viewer** | Display live operational evidence where it is meaningful to the mission context. | Immediate fault and data awareness. |
| **Stream QC / Detached Evidence Views** | Support deeper evidence interpretation without overloading Mission Overview or Systems. | Stronger confidence in QC decisions. |
| **Connection & Sync State** | Show timing, sync, and heartbeat confidence. | Early detection of infrastructure and data issues. |
| **Alert Severity Levels** | Distinguish minor vs critical issues. | Prioritized operator focus. |
| **Status and Quality Indicators** | Make readiness and confidence easier to interpret. | Faster situational judgment. |

### 4.4 Long-Term Priorities (Workshop-Aligned)

| **Capability** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Cross-Sensor Correlation** | Relate evidence across systems and modalities. | Better cause-and-effect understanding. |
| **Multi-Sensor Split View** | Display multiple data sources side-by-side. | Stronger comparative monitoring. |
| **Color-Coded Quality Layer** | Overlay quality metrics over evidence and monitoring views. | Unified QC interpretation. |
| **Survey Area Completion View** | Show progress and remaining work. | Stronger mission posture awareness. |
| **Broader cross-mission monitoring patterns** | Extend awareness beyond one mission where validated. | Future-state supervisory scale. |

### 4.5 Success Metrics

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Situational Awareness** | Time to detect anomaly | <= 2 minutes |
| **Data Quality** | QC alert accuracy | >= 95% |
| **Resilience** | Downtime before alert escalation | <= 1 minute |
| **Evidence Trust** | Reduced need for manual re-checking of "green" states | Qualitative validation through research follow-up |

---

## 5. Inter-Pillar Dependencies

| **Dependency Area** | **Relationship** | **Impact** |
| --- | --- | --- |
| **Mission Overview <-> Systems** | Monitoring informs action; action should remain connected to issue context. | Closed mission-time feedback loop. |
| **Data Monitor <-> Systems** | Evidence supports intervention and validation. | Better judgment at the point of action. |
| **Online Log & Traceability** | Common backbone supporting both pillars. | Visibility and auditability across mission work. |
| **Configuration Templates & Permissions** | Shared foundation for safety and efficiency. | Consistent setup and safe collaboration. |
| **Multi-Mission Context** | Extends awareness patterns beyond the active mission package. | Future supervisory scale without replacing single-mission focus. |

---

## 6. Strategic Outcomes

1. **Operational Efficiency:** Faster mission-time understanding and recovery through clearer surface roles.
2. **Situational Awareness:** Better issue recognition and QC interpretation across overview, systems, and evidence surfaces.
3. **Traceability:** Complete narrative of control, alert, and QC events.
4. **Collaboration:** Safer cross-role support with clearer authority and accountability.
5. **Scalable Product Structure:** A strong active-mission package that can later support broader cross-mission patterns.

---

**End of Document**
*"Act where action belongs; monitor where evidence is clearest."*
