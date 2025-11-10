---
doc_id: PDD.04.03
version: 0.1.1
last_updated: 2025-11-09
status: draft
owners: [design@survey-platform.io]
tags: [functional-specification, stream-viewer, monitoring, qc, sensor-visualization, remote-operations]
---

# PDD.04.03_Stream_Viewer

## Purpose
The **Stream Viewer** provides real-time visualization of sensor data streams within the active mission.  
It enables **Survey Operators** and **Senior Surveyors** to assess sensor performance, signal quality, and environmental consistency in live conditions—without interrupting ongoing data collection.

The Stream Viewer is a mission-contextual, visual component of the SMP that converts live sensor telemetry into actionable situational awareness.

---

## Scope & Context
The Stream Viewer belongs to the **Mission Layer** of the Survey Management Platform (SMP).  
It is contextual to the **currently active mission** and automatically updates when a new mission is selected via the Triage Hub.  
Each mission maintains its own layout and active feeds, which are restored when the mission is reactivated.

Core functions:
- Display real-time sensor feeds (acoustic, navigation, and video).  
- Enable per-feed QC overlay toggling for quality control.  
- Provide feed-level configuration (view type, scale, overlay visibility).  
- Maintain synchronization with other mission-context windows (Mission Deck, Online Log).  

No configuration or parameter changes can be made from this screen—Stream Viewer is strictly observational.

---

## Key Concepts / Framework

| Concept | Description | Role |
|----------|--------------|------|
| **Sensor Feed** | Each viewer panel displays one live data stream from a selected sensor. | Visualizes data and signal quality. |
| **QC Overlay** | Optional visual layer showing live quality metrics derived from telemetry. | Supports data integrity assessment. |
| **Feed Layout** | The operator’s grid arrangement for viewing multiple feeds simultaneously. | Provides multi-sensor situational awareness. |
| **Mission Synchronization** | The viewer’s content changes automatically when mission context changes. | Ensures consistent operational view. |

---

## Functional or UX Details

### 1. Layout Overview

| Zone | Purpose | Components |
|------|----------|-------------|
| **Header Bar** | Mission context and layout tools. | Mission ID, layout selector (1×1 / 1×2 / 2×2), Add Feed button. |
| **Viewer Grid** | Main visualization area showing one or more active feeds. | Dynamic tiles with per-feed controls. |
| **Feed Header (per tile)** | Identifies feed and offers local control. | Sensor name, QC overlay menu, settings (⚙️). |

---

### 2. Header Bar Functions

| Function | Description | Behavior |
|-----------|-------------|-----------|
| **Mission ID** | Displays the active mission name or ID. | Automatically updates with mission context. |
| **Layout Selector** | Allows the operator to choose between common grid layouts. | Updates grid dynamically; non-destructive. |
| **Add Feed** | Opens modal listing available mission sensors. | Selected sensor feed appears in next available tile. |
| **Remove Feed** | Closes a feed and frees up the tile. | Action is logged (“Feed removed”). |

> Layout and feed configuration are mission-specific and restored upon reactivation.

---

### 3. Sensor Feed Tiles

Each feed tile displays one live sensor data stream and includes basic contextual controls.

| Control | Description | Behavior |
|----------|--------------|-----------|
| **Sensor Dropdown** | Selects the sensor for the feed. | Updates data stream immediately. |
| **QC Overlay Menu** | Enables or disables specific QC overlays. | Overlay applies locally to the feed only. |
| **Settings (⚙️)** | Opens modal for view adjustments (e.g., color scale, refresh rate). | Visual-only changes; no system commands. |
| **Visualization Area** | Displays live sensor data in the chosen mode. | Auto-adjusts to screen layout and overlay state. |

---

### 4. QC Overlays

QC Overlays provide **live, feed-level visual layers** to help surveyors assess signal performance and environmental or mechanical stability.  
All thresholds and tolerance limits originate from the **Configuration Manager → Thresholds & Health** tab.

| **Sensor Group** | **Sensor Type** | **QC Overlay Name** | **Purpose / Surveyor Insight** | **Display Type (Design Detail)** | **Data Source / Dependency** |
|------------------|-----------------|----------------------|--------------------------------|----------------------------------|------------------------------|
| **Positioning & Navigation** | **INS** | Motion Stability (Heave / Roll / Pitch) | Shows vessel or platform motion stability, indicating potential data degradation. | Scrolling microplot (color-coded threshold). | INS telemetry (attitude stream). |
| | **USBL** | Position Accuracy / Lock Confidence | Displays real-time acoustic positioning confidence or RMS deviation. | Gauge or confidence bar (color-coded). | USBL QC feed. |
| | **GNSS** | HDOP / RTK Quality | Shows GNSS positional quality. | Numeric badge with threshold colors. | GNSS (RTCM / NMEA) stream. |
| **Acoustic Systems** | **MBES** | Ping Density Map | Heatmap of beam coverage density; highlights gaps or dropouts. | Density heatmap overlay (green–red gradient). | MBES beam data aggregation. |
| | | SNR Bands | Displays signal-to-noise ratio across the swath. | Gradient color bands (per beam angle). | MBES amplitude and noise feed. |
| | | Beam Health / Rejected Beams | Marks invalid or rejected beams. | Red “X” overlay on affected beams. | MBES runtime QC flags. |
| | **SSS** | Coverage Uniformity | Highlights swath overlap and coverage consistency. | Horizontal heat band overlay. | SSS coverage feed. |
| | | Signal Dropout Map | Marks low-return intensity or data gaps. | Sparse orange markers overlay. | SSS intensity QC feed. |
| | **SBP** | Penetration Consistency | Indicates return penetration depth consistency. | Vertical intensity gradient overlay. | SBP amplitude feed. |
| **Environmental** | **SVP / CTD** | SVP Validity Age | Time since last profile; warns of outdated water column corrections. | Timer overlay (color-coded thresholds). | SVP metadata / logging. |
| | | Salinity / Temperature Drift | Shows live deviation from baseline. | Numeric delta overlay (Δ °C / PSU). | CTD telemetry. |
| **Visual Systems** | **ROV / Vessel Cameras** | Illumination / Focus Level | Displays image brightness and sharpness for QC. | Bar overlay or icon (low-light warning). | Camera exposure/gain telemetry. |
| | | Frame Latency | Indicates network or frame delay. | Latency badge (color-coded). | Stream FPS monitor. |

---

### 5. Overlay Design Notes

- **Overlay Activation:** Per-feed toggle via the QC Overlay menu in the feed header.  
- **Persistence:** Overlay states are saved per feed and restored per mission context.  
- **Threshold Source:** All limits and QC color rules come from the Configuration Manager.  
- **Color Standards:**  
  - Green = within tolerance  
  - Amber = approaching threshold  
  - Red = exceeds threshold  
- **Performance:**  
  - Overlay refresh cadence: **1–2 Hz** (sensor-dependent).  
  - Lightweight vector-based rendering to avoid lag.  
  - Independent overlay control ensures multi-feed efficiency.  
- **Accessibility:**  
  - Color + icon redundancy across all overlays.  
  - Optional contrast enhancement for night operations.

---

### 6. Mission Synchronization Behavior

- Each Stream Viewer instance updates automatically when mission context changes.  
- Layout, feed assignments, and overlay states are preserved per mission.  
- If a feed’s source sensor restarts or disconnects, the tile displays a **“Reconnecting”** state with animated border feedback.  
- Switching missions does not reset feed configurations; all state is cached and restored seamlessly.

---

## Acceptance Criteria

- Stream Viewer supports real-time visualization for multiple sensor feeds per mission.  
- Feed-level overlays accurately represent live QC metrics.  
- Overlay updates occur at defined cadence (1–2 Hz) without impacting performance.  
- Layout and overlay states persist across missions.  
- Overlays derive threshold values from Configuration Manager definitions.  
- Camera feeds are supported and display basic QC overlays.  
- Mission synchronization preserves viewer state and data continuity.  

---

## Open Questions & Next Steps

| Topic | Pending Decision |
|--------|------------------|
| **Overlay Customization** | Confirm whether surveyors can reorder or rename overlays per sensor type. |
| **Performance Limits** | Define maximum concurrent feed count (e.g., 4–6) for guaranteed frame rate. |
| **Camera QC Parameters** | Validate which telemetry values (exposure, brightness) are available for live QC. |
| **Sensor-Specific Enhancements** | Determine whether MBES coverage and density should integrate 2D or 3D visualization. |
| **Cross-Link to Mission Deck** | Decide if overlay alerts should raise mission-level notifications (e.g., degraded SNR). |

---

### Summary Statement

> The **Stream Viewer** transforms raw sensor telemetry into a live, visual understanding of mission performance.  
> Through sensor-specific QC overlays, surveyors can quickly identify signal issues, motion instability, or environmental drift, ensuring continuous, high-quality survey acquisition within the SMP ecosystem.

---

**End of Document**
