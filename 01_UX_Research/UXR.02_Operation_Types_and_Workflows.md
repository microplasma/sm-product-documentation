---
doc_id: UXR.02
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [research@survey-platform.io]
tags: [ux-research, workflows, operation-types, ois]
---

# UXR.02 – Operation Types and Workflows

<!--
Changes made:
1. Added standardized front-matter for consistency across repository.
2. Updated H1 to unified format (“# UXR.02 – Operation Types and Workflows”).
3. All content below remains verbatim.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Conceptual Overview (System Design Perspective)

---

## 1. Purpose & Scope
This document defines the major **operation types** managed within the OI Survey (OIS) and describes their **core workflow structures** at a system-design level.  

The objective is to provide a **conceptual view** of how OIS supports survey operations across distinct domains (Geophysical, Geotechnical, Pipeline / IMR, OBN, and vehicle-assisted geophysical modes) while aligning workflows to OIS modules such as **Command & Control (C&C)**, **Active Monitoring (AM)**, and **Online Log Integration**.

---

## 2. Operation Type Overview

| **Operation Type** | **Purpose / Characteristics** | **Key OIS Relevance** |
|---|---|---|
| **Geophysical (vessel-towed / hull-mounted)** | High-speed, wide-area seabed mapping using acoustic sensors (MBES, SSS, SBP, magnetometer). Requires multi-sensor synchronization, line discipline, and coverage tracking. | Emphasis on real-time monitoring, line planning, coverage/QC validation, and logging assurance. |
| **Geotechnical** | Sampling and soil investigation for construction planning. Lower tempo, more mechanical operations (CPT, coring). | Focus on event logging, equipment positioning, and coordination between survey and deck teams. |
| **Pipeline / IMR** | Visual and positional inspection of subsea infrastructure. Most complex type, requiring high operator attention and sensor diversity (video, sonar, INS). | Core user case for C&C, Active Monitoring, and configuration templates. |
| **OBN (Ocean Bottom Nodes)** | Seabed seismic acquisition using nodes deployed on the seafloor, then energized by source operations and later recovered. Strong dependence on deployment accuracy, node inventory, timing/QC, and recovery completeness. | Highlights mission-state traceability, deployment/recovery workflow control, inventory assurance, and time-lagged data validation. |
| **Geophysical with ROV** | High-resolution geophysical or inspection-led survey using a powered ROV carrying sonar, camera, laser, or positioning payloads close to seabed or assets. Lower speed, high maneuverability, high operator involvement. | Emphasizes vehicle state, tether/network health, pilot-surveyor collaboration, and evidence-rich anomaly logging. |
| **Geophysical with ROTV** | Controlled tow-vehicle survey used where precise altitude, stable sensor geometry, and better towing control are needed for high-resolution route, UXO, cable, or asset surveys. Faster than ROV, less autonomous than AUV. | Emphasizes tow-body stability, altitude/line-keeping, sensor synchronization, and fast-turnaround QC over long corridors. |
| **Geophysical with AUV** | Autonomous or supervised-autonomous survey where the vehicle executes preplanned lines or objectives with onboard sensors and later offloads or streams partial QC data. Strong value in close-to-seabed, high-resolution, low-noise mapping. | Emphasizes mission planning, supervised autonomy, navigation confidence, recovery/data offload workflow, and exception handling. |

---

## 3. General Workflow Phases (Shared Across Types)

| **Phase** | **Purpose** | **Representative Actions** | **OIS Interaction Layer** |
|---|---|---|---|
| **Startup & Planning** | Prepare mission parameters, equipment configs, and line plans. | Configure QINSy projects, verify IP/MAC permissions, review line files. | Configuration Manager, User Roles & Access. |
| **Mobilisation** | System calibration, equipment validation, and readiness checks. | Calibrate sensors (USBL, INS, MBES); validate launch/recovery setup; confirm logging paths. | Diagnostics & Health, Config Templates. |
| **Operation (Live Survey)** | Execute missions, monitor data streams, QC, and anomaly detection. | Monitor live feeds, start/stop logging, supervise vehicle or source states, annotate Online Log. | Command & Control, Active Monitoring, Online Log Integration. |
| **Recovery / Retrieval** | Recover deployed assets or vehicles and confirm mission completeness. | Recover nodes, AUVs, ROV/ROTV systems; reconcile inventory and mission status. | Command & Control, Diagnostics & Health, File Monitoring. |
| **Shift Handover** | Transfer operational state and decisions between operators. | Handover notes, Online Log updates, supervisor validation. | Online Log, Multi-User Accessibility. |
| **Reporting & Post-Processing** | Compile logs, QC summaries, and data delivery. | Export Online Log data, verify file structure, reconcile mission outputs against deployment records. | File Monitoring, QC Report Generation. |

---

## 4. OIS Interaction Layers by Operation Type

### 4.1 Geophysical
- **Focus:** Real-time QC and efficiency (coverage and quality).  
- **Typical workflow shape:**
  1. line planning, sensor selection, and project loading
  2. mobilisation checks for navigation, timing, logging, and sensor readiness
  3. line acquisition with continuous QC of coverage, positioning, and sensor health
  4. line turns, rerun decisions, and anomaly/event marking
  5. post-line quick-look review, logging verification, and shift/report handover
- **Key OIS Features:**
  - Multi-sensor sync (MBES, SSS, SBP).
  - Auto-validation of parameters (ping rate, SNR, line deviation).
  - Integrated log of calibration and event markers.
- **Workflow Simplification Goals:**
  - Reduce manual folder checks for logging verification.
  - Enable auto-QC scoring and threshold alerts.

---

### 4.2 Geotechnical
- **Focus:** Data integrity and coordination between survey and deck operations.  
- **Typical workflow shape:**
  1. station planning, sampling program review, and equipment configuration
  2. mobilisation and pre-task checks across survey, deck, and positioning systems
  3. approach to station, positioning confirmation, and operation start approval
  4. sampling / push / recovery events with synchronized logging and exception handling
  5. station closeout, sample/result reconciliation, and move-to-next-station readiness
- **Key OIS Features:**
  - Position and event logging for each sampling station.
  - Config templates for standard borehole operations.
  - Integration with vessel control and deck activity scheduling.
- **Workflow Simplification Goals:**
  - Automate event creation (push start, recovery complete).
  - Link deck-side equipment telemetry with survey records.

---

### 4.3 Pipeline / IMR
- **Focus:** Live visual and positional inspection.  
- **Typical workflow shape:**
  1. route or asset segment planning, overlay setup, and payload/config readiness
  2. launch / approach with vehicle, camera, sonar, and positioning checks
  3. live inspection run with continuous alignment to KP, asset geometry, and exclusion constraints
  4. anomaly investigation, annotation, and targeted reacquisition where needed
  5. recovery, handover, and reporting with linked media, events, and positional traceability
- **Key OIS Features:**
  - ON/OFF/Restart commands for sensors and cameras.
  - Live stream viewer with overlay controls (KP references, pipe names, depth data).
  - Alert-based QC and status indication.
  - Configurable templates for IMR project types.
- **Workflow Simplification Goals:**
  - Reduce manual camera overlay verification.
  - Enable interactive signal-flow diagram for troubleshooting.
  - Integrate Online Log events (line start/end, anomaly) automatically.

---

### 4.4 OBN (Ocean Bottom Nodes)
- **Focus:** Deployment precision, source-node coordination, inventory traceability, and complete recovery.  
- **Typical workflow shape:**
  1. survey design and receiver plan approval
  2. node programming, battery/time-sync verification, and deck inventory checks
  3. deployment to preplanned seabed locations by ROV, rope, wire, or autonomous deployment method
  4. source operations while node status, line progress, and exceptions are tracked
  5. node recovery, deck reconciliation, and download / ingest readiness checks
- **Key OIS Features:**
  - Mission-aware deployment and recovery tracking by line, patch, or receiver spread.
  - Node inventory dashboard with status such as programmed, deployed, interrogated, recovered, downloaded, and exception.
  - Time-sync, positioning, and source-pass traceability linked to each node group.
  - Recovery-completeness and missing-node escalation workflow.
- **Workflow Simplification Goals:**
  - Reduce spreadsheet-style inventory tracking and manual reconciliation.
  - Link deployment, source activity, and recovery into one operational timeline.
  - Make late validation visible, since recording quality is often not fully known until recovery and data handling.

---

### 4.5 Geophysical with ROV
- **Focus:** Close-in, maneuverable survey execution around assets, structures, or difficult seabed where pilot control and sensor interpretation happen together.  
- **Typical workflow shape:**
  1. dive planning, payload confirmation, and navigation/reference setup
  2. launch and descent with vehicle health and tether checks
  3. line or target-based inspection/survey run with continuous vehicle-position awareness
  4. anomaly investigation, reacquisition, and evidence capture
  5. recovery, media/data reconciliation, and event review
- **Key OIS Features:**
  - Shared pilot/surveyor view of vehicle state, altitude, heading, payload status, and positioning quality.
  - Tight integration between live evidence, annotation, and georeferenced event capture.
  - Clear distinction between vehicle control authority and survey decision support.
  - Assisted troubleshooting for tether, power, camera, sonar, and nav degradation.
- **Workflow Simplification Goals:**
  - Reduce fragmented monitoring between ROV UI, navigation tools, and logging tools.
  - Support rapid anomaly marking with linked screenshots, clips, and position context.
  - Preserve context during pauses, hold position, reacquisition, or supervisor assistance.

---

### 4.6 Geophysical with ROTV
- **Focus:** High-resolution, corridor-oriented survey with better tow control than passive towfish and higher speed than ROV-based inspection.  
- **Typical workflow shape:**
  1. route planning, layback/tow geometry setup, and sensor checks
  2. launch, depth/altitude stabilization, and line acquisition
  3. long-run data collection with tight control of altitude, speed, and cross-track performance
  4. turn management, reacquisition after disturbances, and targeted reruns if needed
  5. recovery and quick-look QC to confirm coverage and revisit needs
- **Key OIS Features:**
  - Tow-body state and altitude monitoring tied directly to data quality interpretation.
  - Route progress and corridor coverage view optimized for cable, pipeline, UXO, and site-survey patterns.
  - Fast anomaly flagging with replay of recent sensor history around an event.
  - Clear management of launch/recovery and weather/sea-state impacts on data confidence.
- **Workflow Simplification Goals:**
  - Reduce ambiguity between tow-body behavior and sensor-quality degradation.
  - Improve operator confidence in line-keeping, overlap, and rerun decisions.
  - Streamline post-line quick-look decisions before moving on.

---

### 4.7 Geophysical with AUV
- **Focus:** Mission-planned autonomous geophysical survey with strong dependence on pre-mission confidence, navigation integrity, and post-mission data recovery.  
- **Typical workflow shape:**
  1. objective-based mission planning, route/altitude/sensor plan validation, and abort criteria setup
  2. payload, battery, storage, and navigation-reference readiness checks
  3. launch and mission execution under supervised or unsupervised autonomy
  4. acoustic supervision or sparse status/QC review where available
  5. recovery, data offload, mission replay, and rerun decision-making
- **Key OIS Features:**
  - Mission-plan review surface showing planned lines, objectives, risk zones, and abort logic.
  - Distinction between preplanned autonomy, supervised autonomy, and live operator intervention.
  - Navigation-confidence, battery/endurance, storage, and comms health surfaced as mission risk indicators.
  - Post-mission ingest workflow linking sortie metadata, anomalies, and quick-look QC.
- **Workflow Simplification Goals:**
  - Reduce handoff gaps between planning, launch, mission supervision, and post-mission review.
  - Make autonomy status understandable to operators who still need trust and override confidence.
  - Support rerun decisions with one coherent record of mission plan, mission execution, and observed data quality.

---

## 5. Comparative Characteristics Table

| **Aspect** | **Geophysical** | **Geotechnical** | **Pipeline / IMR** | **OBN** | **Geo with ROV** | **Geo with ROTV** | **Geo with AUV** |
|---|---|---|---|---|---|---|---|
| **Data Type** | Acoustic | Mechanical / Environmental | Visual + Acoustic | Seismic / Node-based | Visual + Acoustic + Positioning | Acoustic / Magnetic / Corridor imaging | Acoustic / Imaging / Environmental |
| **Pace** | High-speed, continuous | Slow, discrete events | Moderate, decision-heavy | Staged deployment, then source-driven, then recovery | Slow to moderate, maneuver-driven | Moderate to high, corridor-driven | Mission-based, burst execution with delayed review |
| **Risk Profile** | Low | Medium (equipment jams) | High (infrastructure proximity) | High (asset loss, incomplete recovery, timing / positioning errors) | High (vehicle, tether, asset proximity) | Medium to High (tow stability, collision, sea-state effects) | High (autonomy failure, recovery, data-loss / rerun cost) |
| **Operational Dependency** | Navigation accuracy | Deck coordination | Real-time situational awareness | Inventory control, deployment accuracy, source coordination | Pilot-surveyor coordination and tether / nav integrity | Tow geometry, altitude control, and line-keeping | Mission planning, navigation integrity, endurance, recovery |
| **Primary OIS Modules** | Active Monitoring | Online Log | Command & Control, Active Monitoring | Command & Control, File Monitoring, Online Log | Command & Control, Active Monitoring, Online Log | Active Monitoring, Online Log | Configuration Manager, Active Monitoring, File Monitoring |

---

## 6. Multi-Mission Implications

| **Operational Challenge** | **Impact of Multi-Mission Work** | **OIS Strategy** |
|---|---|---|
| Attention management | Operators must divide focus across simultaneous missions. | Mission Deck with multi-mission views and alerts prioritization. |
| Configuration drift | Risk of inconsistent settings across missions. | Centralized Configuration Manager with templates. |
| Data integrity | Higher potential for missed logs or incorrect associations. | Auto-log validation and mission-level traceability. |
| Collaboration load | Supervisors assisting multiple surveyors concurrently. | Multi-user session management and assist mode. |

---

## 7. Role and Decision Overlay by Operation Type

This section identifies the primary decision makers and collaboration pattern across phases. It is not a rigid org chart; it is intended to show which role typically owns the decision, who supports it, and where OIS should preserve context or authority boundaries.

### 7.1 Geophysical (vessel-towed / hull-mounted)

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor | Surveyor, PEC, IT | Approve line plan, sensor set, timing/logging setup, and readiness criteria. |
| Mobilisation | Senior Surveyor | Surveyor, IT | Validate calibrations, nav/timing health, and logging readiness before going live. |
| Operation (Live Survey) | Surveyor | Senior Surveyor | Start/stop line activity, monitor QC, flag anomalies, and request reruns or support. |
| Recovery / Retrieval | Surveyor | Senior Surveyor | Confirm line closeout, secure sensor/logging state, and reconcile any open issues. |
| Shift Handover | Surveyor | Senior Surveyor, next Surveyor | Transfer current line state, anomalies, rerun candidates, and logging confidence. |
| Reporting & Post-Processing | Senior Surveyor | Data Manager, Surveyor | Validate QC summary, rerun list, and delivery readiness. |

### 7.2 Geotechnical

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | PEC / Senior Surveyor | Surveyor | Confirm station plan, equipment sequence, and operational constraints. |
| Mobilisation | Senior Surveyor | Surveyor, IT, deck team | Validate positioning, equipment readiness, and event/log templates before work starts. |
| Operation (Live Survey) | Surveyor | Senior Surveyor, deck team | Confirm station approach, start/stop events, and exception logging during push/recovery. |
| Recovery / Retrieval | Surveyor | deck team, Senior Surveyor | Reconcile sample / station state, confirm completion, and prepare next station. |
| Shift Handover | Surveyor | Senior Surveyor, next Surveyor | Transfer incomplete stations, equipment issues, and outstanding logging obligations. |
| Reporting & Post-Processing | Senior Surveyor | Data Manager, PEC | Validate station outcomes, event traceability, and reporting package completeness. |

### 7.3 Pipeline / IMR

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor / PEC | Surveyor, client-facing stakeholders | Confirm asset scope, route segment, overlays, exclusion constraints, and mission priorities. |
| Mobilisation | Senior Surveyor | Surveyor, IT, vehicle team | Validate vehicle payloads, camera/sonar overlays, positioning references, and assist permissions. |
| Operation (Live Survey) | Surveyor | Senior Surveyor, vehicle pilot, PEC | Run inspection workflow, annotate anomalies, request reacquisition, and maintain safe operational context. |
| Recovery / Retrieval | Surveyor | vehicle team, Senior Surveyor | Close out inspection segment, reconcile media/events, and capture unresolved findings. |
| Shift Handover | Surveyor | Senior Surveyor, next Surveyor | Transfer anomaly context, outstanding revisit targets, and current asset/vehicle state. |
| Reporting & Post-Processing | Senior Surveyor | Data Manager, PEC | Validate inspection findings, event/media linkage, and client-facing progress status. |

### 7.4 OBN (Ocean Bottom Nodes)

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor / PEC | Surveyor, Data Manager | Confirm receiver plan, patch logic, deployment method, and node-state traceability rules. |
| Mobilisation | Senior Surveyor | Surveyor, IT, deck/ROV team | Approve node programming, inventory readiness, timing checks, and deployment readiness. |
| Operation (Live Survey) | Surveyor | Senior Surveyor, source team, deck/ROV team | Track deployment/source/recovery state, flag exceptions, and escalate missing or suspect nodes. |
| Recovery / Retrieval | Surveyor | deck/ROV team, Senior Surveyor, Data Manager | Reconcile recovered vs planned nodes, identify losses/exceptions, and confirm ingest readiness. |
| Shift Handover | Surveyor | Senior Surveyor, next Surveyor | Transfer patch status, outstanding nodes, and unresolved inventory or timing issues. |
| Reporting & Post-Processing | Senior Surveyor / Data Manager | PEC, Surveyor | Validate completeness, node exception log, and readiness for downstream seismic handling. |

### 7.5 Geophysical with ROV

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor | Surveyor, ROV pilot, PEC | Confirm target plan, payload selection, nav references, and authority boundaries between pilot and survey roles. |
| Mobilisation | ROV pilot / Senior Surveyor | Surveyor, IT | Validate vehicle readiness, tether/comms health, and payload/sensor configuration. |
| Operation (Live Survey) | Surveyor + ROV pilot | Senior Surveyor | Pilot controls vehicle motion while surveyor owns evidence interpretation, annotation, and reacquisition requests. |
| Recovery / Retrieval | ROV pilot | Surveyor, Senior Surveyor | Recover vehicle safely and confirm media/data/event completeness. |
| Shift Handover | Surveyor | ROV pilot, Senior Surveyor, next Surveyor | Transfer target status, anomalies, revisit requirements, and vehicle/sensor issues. |
| Reporting & Post-Processing | Senior Surveyor | Data Manager, Surveyor | Validate evidence package, anomaly traceability, and follow-up actions. |

### 7.6 Geophysical with ROTV

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor | Surveyor, PEC | Approve route design, tow geometry assumptions, and QC thresholds for revisit decisions. |
| Mobilisation | Surveyor | Senior Surveyor, deck team | Confirm tow-body setup, altitude/depth references, and line-start readiness. |
| Operation (Live Survey) | Surveyor | Senior Surveyor | Monitor tow stability, coverage, and anomalies; decide whether to continue, rerun, or pause. |
| Recovery / Retrieval | Surveyor | deck team, Senior Surveyor | Recover tow vehicle, reconcile line outcomes, and capture disturbance-related notes. |
| Shift Handover | Surveyor | Senior Surveyor, next Surveyor | Transfer corridor status, suspect targets, rerun logic, and tow-body behavior concerns. |
| Reporting & Post-Processing | Senior Surveyor | Data Manager | Validate corridor completeness, anomaly shortlist, and rerun recommendations. |

### 7.7 Geophysical with AUV

| **Phase** | **Primary Role** | **Supporting Roles** | **Typical Decisions / Authority** |
|---|---|---|---|
| Startup & Planning | Senior Surveyor / AUV mission lead | Surveyor, PEC, Data Manager | Approve mission plan, abort criteria, payload/storage/battery margins, and recovery assumptions. |
| Mobilisation | AUV mission lead | Surveyor, IT, launch/recovery team | Validate autonomy configuration, nav references, and launch readiness. |
| Operation (Live Survey) | AUV mission lead / Surveyor | Senior Surveyor | Supervise mission progress, assess sparse health/QC data, and decide whether intervention or abort is needed. |
| Recovery / Retrieval | AUV mission lead | launch/recovery team, Surveyor | Recover vehicle, verify payload/data integrity, and clear mission for ingest. |
| Shift Handover | Surveyor / mission lead | Senior Surveyor, next operator | Transfer sortie status, abort events, nav confidence concerns, and ingest status. |
| Reporting & Post-Processing | Senior Surveyor / Data Manager | Surveyor, PEC | Review sortie execution against plan, validate data offload/QC, and decide on reruns or follow-up missions. |

---

## 8. Strategic Implications for OIS Design
1. **Workflow harmonization**: unify core phases across operation types for consistency.  
2. **Automation of routine checks**: reduce manual QC and verification steps.  
3. **Role adaptability**: enable one operator to manage multiple missions through modular interfaces.  
4. **Template-driven configuration**: minimize setup time and reduce risk of inconsistency.  
5. **Integrated traceability**: all operational events auto-logged and cross-linked with mission context.  

---

## 9. Canonical Sources
- `2.3.OI_Operational_Workflows.md`
- `2.3.1.OperationTypesWorkflows.md`
- `Underwater Survey Operations – Task Structure`
- `Surveyor_Tasks.csv`
- `Workshop_workflow_map-features-pain.xlsx`
- External references consulted for workflow expansion:
  - Kongsberg Discovery, `HUGIN` and `HUGIN Edge` AUV product pages
  - Kongsberg article, `How Autonomous is a HUGIN AUV?`
  - PXGEO, `Ocean Bottom Nodes`
  - TGS, `Ocean Bottom Node Technology`
  - ROVOP case study on OBN deployment
  - Horizon Geosciences and Geosonic ROV survey pages
  - EIVA `ViperFish` and Hydrospace Group `ROTV` references

---

**End of Document**  
_"Clarity through structure – unified workflows as the foundation for OIS design."_
