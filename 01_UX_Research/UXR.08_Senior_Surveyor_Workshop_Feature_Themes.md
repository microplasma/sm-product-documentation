---
doc_id: UXR.08
title: Senior Surveyor Workshop Feature Themes
version: 0.1.0
status: draft
visibility: internal
owners: ["research@survey-platform.io"]
tags: ["ux-research", "workshop", "senior-surveyor", "feature-themes"]
created: 2026-04-06
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 01_UX_Research
  - rel: source
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
---

# UXR.08 - Senior Surveyor Workshop Feature Themes

## Purpose
This document synthesizes the feature and notes workbook produced during a senior surveyor workshop. It translates the workshop material into durable operator themes, pain points, and capability implications that can inform product design without turning the documentation into a committed feature backlog.

## Source and Interpretation Notes
- This material comes from a senior surveyor workshop captured in `OI_SMP_All_Features_Catalog-CleanBase.xlsx`.
- The workbook contains feature ideas, descriptive notes, operator needs, pain points, and opportunity signals.
- It should be interpreted as **research evidence and capability direction**, not as a finalized roadmap or committed implementation scope.
- The Excel workbook remains the raw source artifact. This markdown document is the synthesis layer intended for human and agent use.

## What The Workshop Material Represents
The workshop content is most valuable when read as a set of repeated operational concerns:
- surveyors need faster awareness of what matters now
- they need safer mission-time control and recovery
- they need stronger evidence and QC interpretation without app-hopping
- they need more trustworthy traceability, handover, and logging
- they need environmental and geodetic readiness to be visible and defensible
- they need clearer authority, lock, and permission boundaries

## Cross-Cutting Insights
- The strongest workshop signal is not a specific widget or module. It is the need to reduce fragmentation across control, diagnostics, evidence, and logging.
- The workbook repeatedly describes trust gaps: surveyors re-check "green" states manually because current tools do not make readiness or consequence sufficiently believable.
- The material reinforces that navigation context, environmental readiness, and traceability are not side concerns. They are central to operational confidence.
- Many workbook items imply the need for multiple levels of interaction density: overview, mission-time action, deep evidence review, and specialist workflow support.
- The material is rich in features, but the more durable value lies in the repeated operator jobs, bottlenecks, and coordination patterns underneath them.

## Theme 1. Mission Awareness and Prioritization
### Workshop signal
The workshop repeatedly surfaces the need for operators to understand mission posture, operational risk, and progress at a glance, especially when more than one mission or operational thread competes for attention.

### Surveyor need
Surveyors need to know which mission, asset, or operational issue deserves attention now and why.

### Pain points / opportunities
- Attention is wasted reconstructing status from many systems.
- High-level mission and survey progress is not consistently visible.
- Operators need a stronger way to decide when to shift focus before data quality or mission continuity suffers.

### Design implications
- OI Survey should maintain a distinct cross-mission awareness layer.
- Summary information should prioritize urgency, confidence, and recent change over raw telemetry density.
- Performance-style views may be useful, but should be treated as awareness support rather than core mission-time control.

### Related workbook modules
- `Navigation display`
- `Performance Dashboards & BI Analytics`

## Theme 2. Mission-Time Control and Recovery
### Workshop signal
The workbook contains many ideas around centralized sensor control, start/stop/restart actions, configuration checkpoints, and fault recovery.

### Surveyor need
Surveyors need to intervene quickly during live work without losing confidence in what they changed or what downstream effect it caused.

### Pain points / opportunities
- Operators lose time jumping into vendor tools or remote sessions for simple recovery steps.
- Recovery actions and configuration changes are not consistently traceable.
- Manual verification loops exist because the control surface does not fully explain operational consequence.

### Design implications
- The product needs a strong mission-time control model with clear guardrails.
- Recovery actions should remain close to the evidence and context needed to judge them.
- Configuration and recovery should remain related, but not collapsed into one undifferentiated feature list.

### Related workbook modules
- `SensorControl`
- `Diagnostics & Troubleshooting`

## Theme 3. Evidence and QC Interpretation
### Workshop signal
The workbook strongly emphasizes live stream viewing, split views, quality indicators, and short-history/trend visibility.

### Surveyor need
Surveyors need to interpret evidence from multiple sensors and feeds quickly enough to validate acquisition quality, detect anomalies, and decide whether to intervene.

### Pain points / opportunities
- Quality understanding is fragmented across vendor-specific views.
- Operators want multi-sensor comparison and QC overlays without excessive interface switching.
- There is a recurring need to keep evidence visible even when the main control surface is focused elsewhere.

### Design implications
- Detached evidence viewing is a valid and recurring product need.
- Evidence and QC capabilities should be modeled as a surface family, not only as a single "stream viewer" screen.
- The product should preserve the distinction between evidence interpretation and direct control.

### Related workbook modules
- `Sensor Output Monitoring`
- `Quality Control & Monitoring`

## Theme 4. Navigation and Spatial Context
### Workshop signal
The workshop repeatedly points to navigation display needs, line context, spatial validation, and awareness of where the survey is relative to plan, infrastructure, or worksite constraints.

### Surveyor need
Surveyors need to understand where work is happening, how the vessel or asset is behaving relative to plan, and what spatial context affects acquisition confidence.

### Pain points / opportunities
- Navigation remains operationally central even when handled in external tools.
- Spatial context is needed for both overview and mission-time interpretation.
- Surveyors need the product model to acknowledge navigation truth without pretending it is already fully absorbed into OI Survey.

### Design implications
- Qinsy and navigation context should remain explicit in the product model.
- Mission-time workspace and cross-mission awareness should both acknowledge spatial context, even if OI Survey is not yet the primary navigation viewer.

### Related workbook modules
- `Navigation display`

## Theme 5. Traceability, Handover, and Collaboration
### Workshop signal
The workbook contains a strong cluster of ideas around event logging, file transfer visibility, shift handover, shared notes, and collaborative continuity.

### Surveyor need
Surveyors need an operational narrative they can trust across shifts, incidents, remote support, and reporting workflows.

### Pain points / opportunities
- Handover quality suffers when records are spread across tools and formats.
- Operators need low-friction ways to annotate what happened and why.
- Logging, file state, and operational events should support both live use and downstream reporting.

### Design implications
- Online Log should be treated as a service backbone, not only a UI feature.
- Handover and collaboration should remain tightly linked to traceability.
- File transfer and operational events should contribute to the same narrative, even if they come from different systems.

### Related workbook modules
- `Event Logging`
- `Collaboration & Shift Handover`
- `File & Data Transfer Management`

## Theme 6. Environmental and Geodetic Readiness
### Workshop signal
The workshop includes a distinct set of features around SVP and geodetic utilities, which points to the importance of environmental correction and reference truth.

### Surveyor need
Surveyors need confidence that profiles and reference data are current, validated, and correctly distributed to the systems that depend on them.

### Pain points / opportunities
- Environmental readiness is often operationally critical but weakly surfaced.
- Surveyors need better continuity between specialist profile workflows and mission-time understanding.
- There is value in making environmental preparation traceable, not just technically available.

### Design implications
- Hydrosens should be treated as a specialized but connected subsystem.
- Environmental readiness should influence core mission-time confidence without forcing the full specialist workflow into Mission Deck.

### Related workbook modules
- `SVP & Geodetic Utilities`

## Theme 7. Connectivity, Diagnostics, and Infrastructure Trust
### Workshop signal
A large portion of the workbook centers on system health, sync state, signal flow, diagnostics, network health, and failure isolation.

### Surveyor need
Surveyors need to know whether degraded behavior is caused by the sensor itself, the network path, timing drift, or a broader infrastructure problem.

### Pain points / opportunities
- Troubleshooting is slowed by poor visibility into dependency chains and signal paths.
- Time sync, connectivity, and network integrity are critical but often hidden in specialist tools.
- Operators want stronger, more actionable trust signals before the problem becomes a data loss event.

### Design implications
- Diagnostics should remain distinct from generic health summaries.
- Signal flow, connectivity, and infrastructure trust should be recognized as their own operational concern, not only as low-level engineering telemetry.
- Dependency meaning and fault isolation should be visible in both mission-time and troubleshooting contexts.

### Related workbook modules
- `Diagnostics & Troubleshooting`
- `System Connectivity & Network Diagnostics`

## Theme 8. Governance, Permissions, and Operational Safety
### Workshop signal
The workbook includes role-based access, configuration locks, immutable audit trails, multi-user protection, and security controls.

### Surveyor need
Surveyors need confidence that critical actions, edits, and approvals are governed safely without making collaboration impossible.

### Pain points / opportunities
- Operators need strong protection against accidental live edits.
- Teams still need to collaborate, observe, and support without interfering with each other.
- Permissions and lock states should be operationally legible rather than hidden admin settings.

### Design implications
- Authority and lock state belong in the product model, not only in technical security design.
- Role-based behavior should be visible in mission-time workflows and specialist subsystems alike.
- Auditability should support both governance and practical operational trust.

### Related workbook modules
- `SensorControl`
- `User Management & Security`

## Implications for Product Design
The workshop synthesis supports the current layered design direction:
- `PDD.04.01` should continue to strengthen cross-mission awareness and prioritization.
- `PDD.04.02` should remain the primary home for mission-time control and recovery logic.
- `PDD.04.03` should preserve detached evidence viewing as a durable capability.
- `PDD.04.05` should continue to treat traceability as a service backbone.
- `PDD.04.06` should position environmental profile management as specialized but connected.
- `PDD.06` should keep authority, permissions, and collaboration explicit in the operational model.

## Open Questions
- Which of the workbook's navigation and dashboard ideas should remain external-context acknowledgements versus direct OI Survey scope?
- Which diagnostic capabilities belong in mission-time use versus deeper troubleshooting contexts?
- How much of file transfer and handover should be expressed in OI Survey core surfaces versus shared services?
- Which workshop themes need stronger validation across additional roles beyond senior surveyors?

## Summary Statement
> The senior surveyor workshop material is most useful when interpreted as evidence of recurring operator needs: stronger awareness, safer control, clearer evidence, more trustworthy traceability, and better visibility into environmental, diagnostic, and governance realities that shape remote survey work.

