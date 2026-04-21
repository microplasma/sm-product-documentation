# OI Survey Product Documentation: Project Knowledge Bundle

This file is a retrieval-optimized merged export for ChatGPT Projects or GPT Knowledge.
It preserves canonical document order, stable identifiers, source paths, and section boundaries.

## Retrieval Notes

- Prefer answers from canonical docs before `sources/` evidence docs.
- Cite answers with `doc_id` or `decision_id`, document title, and repo path.
- Treat each `DOCUMENT START` / `DOCUMENT END` block as the authoritative boundary for one source file.
- The canonical reading order is Product Foundation -> UX Research -> Product Design -> Decisions.

## Bundle Index

- `00PF` | Product Foundation | base_path: `00_Product_Foundation` | tags: [vision, strategy, architecture, pillars]
  - `PFD.01` | Product Vision | `00_Product_Foundation/PFD.01_Product_Vision.md`
  - `PFD.02` | Product Strategy Overview | `00_Product_Foundation/PFD.02_Product_Strategy_Overview.md`
  - `PFD.03` | Product Architecture Overview | `00_Product_Foundation/PFD.03_Product_Architecture_Overview.md`
  - `PFD.04` | Product Pillars | `00_Product_Foundation/PFD.04_Product_Pillars.md`
- `01UX` | UX Research | base_path: `01_UX_Research` | tags: [research, roles, workflows, insights]
  - `UXR.00` | User Research Summary | `01_UX_Research/UXR.00_User_Research_Summary.md`
  - `UXR.01` | Roles and Responsibilities | `01_UX_Research/UXR.01_Roles_and_Responsibilities.md`
  - `UXR.02` | Operation Types and Workflows | `01_UX_Research/UXR.02_Operation_Types_and_Workflows.md`
  - `UXR.03` | Tasks and Tools Matrix | `01_UX_Research/UXR.03_Tasks_and_Tools_Matrix.md`
  - `UXR.04` | Pain Points and Opportunities | `01_UX_Research/UXR.04_Pain_Points_and_Opportunities.md`
  - `UXR.05` | Role-Based Insights | `01_UX_Research/UXR.05_Role-Based_Insights.md`
  - `UXR.06` | Context of Use and Environment | `01_UX_Research/UXR.06_Context_of_Use_and_Environment.md`
  - `UXR.07` | Sensor Taxonomy | `01_UX_Research/UXR.07_Sensor_Taxonomy.md`
  - `UXR.08` | Senior Surveyor Workshop Feature Themes | `01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md`
- `02PD` | Product Design | base_path: `02_Product_Design` | tags: [design, architecture, ux, operations]
  - `PDD.00` | Design Principles and Documentation Model | `02_Product_Design/PDD.00_Design_Principles_and_Documentation_Model.md`
  - `PDD.01` | OI Survey Product Topology | `02_Product_Design/PDD.01_OIS_Product_Topology.md`
  - `PDD.02` | Operational Information Model | `02_Product_Design/PDD.02_Operational_Information_Model.md`
  - `PDD.03` | Interaction Framework and Surface Grammar | `02_Product_Design/PDD.03_Interaction_Framework_and_Surface_Grammar.md`
  - `PDD.04.01` | Multi-Mission Context | `02_Product_Design/PDD.04.01_Multi-Mission_Context.md`
  - `PDD.04.02` | Mission Deck | `02_Product_Design/PDD.04.02_Mission_Deck.md`
  - `PDD.04.03` | Detached Evidence Surfaces | `02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md`
  - `PDD.04.04` | Operational Configuration Management | `02_Product_Design/PDD.04.04_Operational_Configuration_Management.md`
  - `PDD.04.05` | Online Log and Traceability Service | `02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md`
  - `PDD.04.06` | Hydrosens Environmental Profile Management | `02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md`
  - `PDD.05` | Operational State and Configuration Model | `02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md`
  - `PDD.06` | Roles, Authority and Operational Modes | `02_Product_Design/PDD.06_Roles_Authority_and_Operational_Modes.md`
  - `PDD.07` | Design Bets, Gaps and Future Directions | `02_Product_Design/PDD.07_Design_Bets_Gaps_and_Future_Directions.md`
- `03DC` | Decisions | base_path: `03_Decisions` | tags: [decisions, product, design, governance]
  - `DCR.0001` | Multi-Mission Context Naming | `03_Decisions/DCR.0001_Multi-Mission_Context_Naming.md`
  - `DCR.0002` | Product Surface Model | `03_Decisions/DCR.0002_Product_Surface_Model.md`
  - `DCR.0003` | Hydrosens Placement Model | `03_Decisions/DCR.0003_Hydrosens_Placement_Model.md`
- `ROOT` | Repository-level docs
  - `RD.ROOT` | Repository README | `README.md`
  - `SRC.ROOT` | Sources README | `sources/README.md`

## Repository-Level Documents

### DOCUMENT START | RD.ROOT | Repository README

- kind: `doc_id`
- id: `RD.ROOT`
- title: `Repository README`
- path: `README.md`
- canonical_role: `repository_context`
- estimated_tokens: `747`

# OI Survey Product Documentation
version: 0.3.0  
last_updated: 2026-04-06

This repository contains product documentation organized for clear human reading and agent (LLM/bot) retrieval.  
It is intended to act as the curated knowledge base for product and design work, while still allowing external tools to remain capture spaces.

## Structure
- [`00_Product_Foundation/`](./00_Product_Foundation/README.md) - Canonical product vision, strategy, architecture, and pillars  
- [`01_UX_Research/`](./01_UX_Research/README.md) - Canonical research synthesis, roles, workflows, and insights  
- [`02_Product_Design/`](./02_Product_Design/README.md) - Canonical product-design documentation covering principles, topology, surfaces, subsystems, services, and design bets  
- [`03_Decisions/`](./03_Decisions/README.md) - Canonical product and design decision records  
- [`sources/`](./sources/README.md) - Raw or lightly organized evidence from external tools and source artifacts  

> Note: The `bits/` folder is intentionally **not** indexed as a canonical documentation section.

## Knowledge Model
This repo now contains four working layers:
- **Canonical docs** - the promoted source of truth (`00`, `01`, `02`)
- **Decisions** - explicit promoted choices tied to evidence (`03`)
- **Sources / evidence** - raw artifacts and source packages (`sources/`)
- **Helper material** - prompts, working notes, and non-canonical support (`bits/`)

## Conventions
- **Document IDs** (`doc_id`) appear in filenames as prefixes:
  - `PFD.*` -> Product Foundation
  - `UXR.*` -> UX Research
  - `PDD.*` -> Product Design
  - `DCR.*` -> Decision Records
- Files are named `DOCID.NN_Title_Words.md` or equivalent stable forms to give both stable IDs and readable titles.
- Prefer linking by relative path to keep intra-repo links stable.

## Promotion Model
External tools such as Confluence, Figma, FigJam, Miro, spreadsheets, and recordings remain source systems. They do not become canonical truth automatically.

Promotion flow:
1. Capture or store the artifact in `sources/`
2. Synthesize the relevant insight into canonical docs
3. Record important accepted choices in `03_Decisions/`
4. Update canonical docs in `00`, `01`, and `02`

## For Agents (LLMs/Bots)
- Use section READMEs for table-of-contents discovery.
- Use `DOC_MANIFEST.yml` to resolve canonical file paths.
- Treat `sources/` as evidence storage unless a specific source package README is explicitly needed.
- Cite using `{doc_id or decision_id, path, anchor, heading}` whenever quoting canonical content.

## Quick Links
- **Product Foundation** -> [`00_Product_Foundation/README.md`](./00_Product_Foundation/README.md)  
- **UX Research** -> [`01_UX_Research/README.md`](./01_UX_Research/README.md)  
- **Product Design** -> [`02_Product_Design/README.md`](./02_Product_Design/README.md)  
- **Decisions** -> [`03_Decisions/README.md`](./03_Decisions/README.md)  
- **Sources** -> [`sources/README.md`](./sources/README.md)

### DOCUMENT END | RD.ROOT

### DOCUMENT START | SRC.ROOT | Sources README

- kind: `source_id`
- id: `SRC.ROOT`
- title: `Sources README`
- path: `sources/README.md`
- canonical_role: `repository_context`
- estimated_tokens: `318`

# Sources
version: 0.1.0  
last_updated: 2026-04-06

This section stores raw or lightly organized source artifacts that inform the canonical documentation in this repo.

## Purpose
`sources/` exists to hold evidence from external tools and working artifacts such as:
- workshops
- Confluence exports
- Figma and FigJam exports
- Miro exports
- spreadsheets
- recordings
- transcripts

## Important Rule
Content in `sources/` is **not canonical product truth by default**.

The canonical layers remain:
- `00_Product_Foundation`
- `01_UX_Research`
- `02_Product_Design`
- `03_Decisions`

## Promotion Flow
1. Capture the raw artifact in `sources/`.
2. Add or update a source package README.
3. Synthesize the important insights into `01_UX_Research` or another canonical section.
4. If a real decision was made, create or update a record in `03_Decisions`.
5. Update canonical docs in `00`, `01`, or `02` as needed.

## Subfolders
- `workshops/`
- `confluence/`
- `figma/`
- `figjam/`
- `miro/`
- `spreadsheets/`
- `recordings/`

## Usage Guidance
- Keep raw artifacts close to a README that explains what they are.
- Prefer source-package folders over dropping files loose in `sources/`.
- Link from source-package READMEs to derived outputs and related decision records.

### DOCUMENT END | SRC.ROOT

## SECTION START | 00PF | Product Foundation

- section_id: `00PF`
- title: `Product Foundation`
- base_path: `00_Product_Foundation`
- tags: [vision, strategy, architecture, pillars]
- document_count: `4`

### DOCUMENT START | PFD.01 | Product Vision

- kind: `doc_id`
- id: `PFD.01`
- title: `Product Vision`
- path: `00_Product_Foundation/PFD.01_Product_Vision.md`
- section_id: `00PF`
- section_title: `Product Foundation`
- canonical_role: `canonical_doc`
- estimated_tokens: `1776`

---
doc_id: PFD.01
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [product-vision, ois, remote-operations, design-principles]
---

# PFD.01 - Product Vision

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** Product Design & Strategy - OIS Core Team  
**Status:** Updated Draft

---

## 1. Vision Statement

> **OI Survey (OIS)** enables Ocean Infinity's teams to manage, monitor, and control complex marine survey operations through a unified operational ecosystem of connected surfaces and services - with confidence, safety, and efficiency.

OIS is intended to transform how offshore, onshore, and remote surveyors collaborate. It aims to replace fragmented, tool-heavy workflows with a **unified operational ecosystem** that connects data, systems, and people through real-time awareness, safer intervention, and defensible traceability.

Current product direction develops **mission-level clarity and multi-mission awareness in parallel**. Mission Overview and Multi-Mission Context should reinforce each other: the first clarifies what matters inside one mission, while the second should progressively combine the most important mission-level signals across several missions.

---

## 2. Purpose

Modern survey operations span multiple vessels, remote hubs, and autonomous assets.  
OIS is designed to:

* reduce operational fragmentation across mission-time work
* give surveyors dependable mission-level understanding and action support
* improve confidence in data integrity, operational safety, and traceability
* connect decision, control, evidence, and logging surfaces coherently
* support cross-mission and multi-mission workflows as part of the evolving operating model

---

## 3. Strategic Context

Marine survey operations are transitioning from vessel-based execution to distributed, remote, and increasingly autonomous operating models.  
OIS sits at the center of this transition as a product direction that should reduce operational complexity without pretending every workflow belongs inside one flat application shell.

The current product direction frames OIS as a **unified operational ecosystem** structured through connected operational surfaces, with mission-level and cross-mission models evolving together rather than as strictly separate time horizons.

| Trend | OIS Response |
| --- | --- |
| Fragmented workflows and high operator load | Unified operational ecosystem with clearer boundary between decision, control, evidence, and traceability |
| Need for stronger mission-time confidence | Mission Overview as the primary decision surface for the active mission |
| Complex system recovery and control | Systems as the deep operational and control surface |
| Manual logging and weak handovers | Online Log as a traceability backbone rather than an optional side feature |
| Growing need for broader mission oversight | Multi-Mission Context as the cross-mission surface that recombines the most important mission-level signals |

---

## 4. Product Definition

### 4.1 What OIS Is

A **unified operational ecosystem** for remote and distributed survey work, structured through connected mission-time surfaces, shared services, and specialist subsystems rather than a single undifferentiated application.

### 4.2 What OIS Is Not

* Not a replacement for acquisition or navigation software.
* Not a reporting platform, though it supports reporting through traceability and exportable records.
* Not a long-term data repository - it coordinates operational truth, intervention, evidence, and traceability during survey work.

### 4.3 Core Role

> **To help survey teams understand what matters now, act safely in the active mission, interpret evidence with confidence, and preserve a trustworthy operational record.**

---

## 5. Core Vision Pillars

| **Pillar** | **Purpose** | **Outcome** |
| --- | --- | --- |
| **Command & Control** | Support safe operational action through the right mission-time surfaces. | Faster, clearer intervention with stronger consequence visibility. |
| **Active Monitoring** | Make data quality, system health, and evidence easier to interpret. | Earlier detection of degraded conditions and stronger survey confidence. |
| **Collaboration & Traceability** | Preserve a defensible operational narrative across shifts, roles, and services. | Better handovers, clearer accountability, fewer context gaps. |
| **Scalability & Resilience** | Support growth in both mission-level and cross-mission operating models. | A credible path toward multi-mission work without reducing the value of either layer. |

---

## 6. Guiding Design Principles

| **Principle** | **Description** |
| --- | --- |
| **Mission-Level Clarity With Cross-Mission Continuity** | The active mission should be easy to understand, and that clarity should inform how broader cross-mission awareness is built. |
| **Surface-Specific Purpose** | Different operational questions should be served by the right surface, not collapsed into one flat workspace. |
| **Evidence Supports Intervention** | Control actions should stay connected to the evidence needed to judge them safely. |
| **Traceability Is Product-Critical** | Logging, event capture, and narrative continuity are part of the operating model. |
| **Role-Based Trust** | Permissions and authority should protect live work while preserving collaboration. |
| **System Memory** | Every meaningful action, configuration, and event should remain reviewable and reconstructable. |

---

## 7. Success Metrics

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Operational Efficiency** | Mobilization time reduction | >= 30% |
| **Situational Awareness** | Mean time to detect anomaly | <= 2 minutes |
| **Reliability** | Fault recovery time | <= 10 minutes |
| **User Experience** | Operator satisfaction | >= 90% positive |
| **Traceability** | Automated event capture | 100% |
| **Scalability** | Safe multi-mission capability | Evolving target, developed in parallel with mission-level operating clarity |

---

## 8. Roadmap Snapshot

| **Phase** | **Focus** | **Key Deliverables** |
| --- | --- | --- |
| **Phase 1 (Core Operating Ecosystem)** | Strong mission-level and cross-mission foundations | Mission Deck, Mission Overview, Systems, Online Log, Multi-Mission Context direction, early Data Monitor direction |
| **Phase 2 (Connected Operational Surfaces)** | Stronger evidence, configuration, service, and aggregation models | Expanded Data Monitor capability, configuration governance, deeper traceability and stronger Multi-Mission Context integration |
| **Phase 3 (Broader Operational Scale)** | More mature supervisory and validated concurrency patterns | Multi-Mission Context maturity, cross-mission prioritization, future multi-mission operating support where validated |

**Note:** Roadmap phases are indicative and subject to validation through feature prioritization and operational review.

---

**End of Document**  
*"One operational ecosystem, with mission-level and cross-mission confidence evolving together."*

### DOCUMENT END | PFD.01

### DOCUMENT START | PFD.02 | Product Strategy Overview

- kind: `doc_id`
- id: `PFD.02`
- title: `Product Strategy Overview`
- path: `00_Product_Foundation/PFD.02_Product_Strategy_Overview.md`
- section_id: `00PF`
- section_title: `Product Foundation`
- canonical_role: `canonical_doc`
- estimated_tokens: `2027`

---
doc_id: PFD.02
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [product-strategy, ois, design, operations, transformation]
---

# PFD.02 - Product Strategy Overview

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft

---

## 1. Purpose

This document defines the **strategic intent** of OI Survey (OIS), describing how it should deliver operational, technological, and experiential transformation across Ocean Infinity's survey operations.

It translates OIS's vision into a strategy grounded in a clearer product model: **OI Survey as a unified operational ecosystem** expressed through distinct but connected surfaces, not as one flat application shell.

---

## 2. Strategic Context

### 2.1 Industry Transformation

The marine survey industry is shifting from vessel-based execution to distributed, remote, and increasingly autonomous workflows. Ocean Infinity's operating model requires better mission-time clarity, stronger traceability, and a credible cross-mission operating model.

OIS should support that transition by reducing fragmentation across survey work while preserving the operational nuance of different tasks, systems, and specialist workflows.

### 2.2 The Strategic Opportunity

Surveyors currently manage complex toolchains across multiple systems and displays, leading to inefficiency, re-checking, and fatigue. OIS's strategic opportunity is to:

* **reduce operational complexity**
* **improve mission-level decision quality and intervention confidence**
* **strengthen traceability and handover continuity**
* **separate decision, control, evidence, and service concerns more clearly**
* **develop cross-mission and future multi-mission work as part of the same evolving operating model**

---

## 3. Strategic Objectives

| **Objective** | **Goal** | **Outcome** |
| --- | --- | --- |
| **1. Mission-Level Clarity** | Give surveyors a dependable operating model for the active mission. | Faster understanding of state, issue, and next safe action. |
| **2. Operational Efficiency** | Simplify workflows and reduce manual intervention across mission-time surfaces. | Faster mobilization, fewer tool switches, reduced procedural overhead. |
| **3. Situational Awareness** | Improve visibility across systems, evidence, health, and quality. | Earlier anomaly detection and better recovery decisions. |
| **4. Traceable Collaboration** | Enable auditable distributed teamwork and stronger handovers. | Better continuity across shifts, roles, and interventions. |
| **5. Scalable Product Structure** | Build a product model that can grow across mission-level and cross-mission workflows together. | Strong product coherence with broader operational range. |

---

## 4. Strategic Pillars

| **Pillar** | **Focus** | **Strategic Intent** |
| --- | --- | --- |
| **Command & Control** | Safe mission-time action and recovery. | Place operational intervention in the right surfaces, especially Systems inside Mission Deck. |
| **Active Monitoring** | Real-time data, health, and QC interpretation. | Strengthen evidence and quality understanding through Mission Overview and Data Monitor capabilities. |
| **Collaboration & Traceability** | Shared operations and historical continuity. | Make Online Log and related traceability services part of the operating model, not administrative add-ons. |
| **Scalability & Resilience** | Strong mission-level and cross-mission ecosystem growth. | Expand toward broader multi-mission support without treating cross-mission awareness as a distant layer. |

---

## 5. Strategic Approach

### 5.1 Design Strategy

* **Unified Ecosystem:** Treat OI Survey as one operational ecosystem expressed through coordinated surfaces, services, and subsystems.
* **Parallel Mission and Cross-Mission Development:** Build Mission Overview and Multi-Mission Context together as related layers of the same attention model.
* **Surface-Based Product Model:** Treat Mission Overview, Systems, Online Log, Data Monitor, and Multi-Mission Context as purpose-built parts of one ecosystem.
* **Evidence-Backed Intervention:** Keep operational action close to the evidence needed for confidence.
* **Traceable Workflows:** Ensure actions, changes, and observations contribute to a defensible narrative.
* **Validated Scale:** Preserve multi-mission as a strategic direction without forcing it to dominate near-term design decisions.

### 5.2 Technology Strategy

* **Mission-Oriented State Handling:** Maintain coherent mission context across connected surfaces and services.
* **Shared Service Backbone:** Treat logging, configuration governance, and synchronization as cross-cutting product infrastructure.
* **RBAC Enforcement:** Make role boundaries and authority visible where operationally necessary.
* **Evidence and Monitoring Extensibility:** Allow Data Monitor capabilities to mature incrementally rather than forcing one early monolith.
* **Interoperability:** Abstract heterogeneous acquisition, navigation, telemetry, and specialist tooling into product-level operational concepts.

### 5.3 Operational Strategy

* **Remote-First Collaboration:** Support distributed work between offshore, onshore, and specialist roles.
* **Incremental Adoption:** Improve mission-time work without requiring all external dependencies to be absorbed immediately.
* **Operational Trust:** Reduce manual re-checking by making readiness, impact, and traceability more credible.
* **Integrated Cross-Mission Track:** Continue developing Multi-Mission Context alongside mission-level surfaces so the two models inform each other.

---

## 6. Roadmap Framework

The following roadmap is **indicative only** and should be validated against operator research, workshop priorities, and prototype maturity.

| **Phase** | **Focus** | **Indicative Milestones** |
| --- | --- | --- |
| **Phase 1 - Core Operating Ecosystem** | Establish the primary mission-level and cross-mission foundations. | Mission Deck structure, Mission Overview, Systems, Online Log, package-level Data Monitor framing, Multi-Mission Context direction. |
| **Phase 2 - Connected Operational Surfaces** | Strengthen evidence, configuration, specialist workflow, and aggregation connections. | Expanded Data Monitor capabilities, stronger configuration governance, clearer service integration, stronger Multi-Mission Context integration. |
| **Phase 3 - Broader Operational Scale** | Mature cross-mission awareness and validated concurrency patterns. | Multi-Mission Context growth, prioritization patterns, future multi-mission operating support where validated. |

**Note:** Final roadmap structure will be derived from feature prioritization and stakeholder validation sessions.

---

## 7. Success Criteria

| **Category** | **Metric** | **Target** |
| --- | --- | --- |
| **Efficiency** | Mobilization time reduction | >= 30% |
| **Reliability** | Mean fault recovery time | <= 10 min |
| **Situational Awareness** | Time to detect anomaly | <= 2 min |
| **User Experience** | Operator satisfaction | >= 90% positive |
| **Traceability** | Logged actions automatically captured | 100% |
| **Scalability** | Multi-mission support | Evolving target, developed alongside mission-level clarity |

---

## 8. Strategic Outcomes

1. **Clearer Mission-Time Operations:** Surveyors can understand and act inside one coherent active-mission package.
2. **Stronger Operational Trust:** Readiness, evidence, and traceability reduce re-checking and ambiguity.
3. **Better Service Backbone:** Online Log and related shared services support live use, handover, and downstream reporting.
4. **More Credible Product Structure:** Different operational questions are served by the right surface rather than one overloaded workspace.
5. **Scalable Direction:** The product can grow toward cross-mission and multi-mission modes while keeping mission-level and cross-mission models connected.

---

**End of Document**
*"One ecosystem, clarified through connected mission-level and cross-mission surfaces."*

### DOCUMENT END | PFD.02

### DOCUMENT START | PFD.03 | Product Architecture Overview

- kind: `doc_id`
- id: `PFD.03`
- title: `Product Architecture Overview`
- path: `00_Product_Foundation/PFD.03_Product_Architecture_Overview.md`
- section_id: `00PF`
- section_title: `Product Foundation`
- canonical_role: `canonical_doc`
- estimated_tokens: `3226`

---
doc_id: PFD.03
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [architecture, ois, system-design, remote-operations, multi-mission]
---

# PFD.03 - Product Architecture Overview

**Version:** 2.1  
**Date:** 2025-10-25  
**Owner:** OIS Product Design & Strategy  
**Status:** Updated Draft - Surface Model Alignment

---

## 1. Purpose

This document defines the **conceptual product architecture** of OI Survey (OIS).  
It describes how the product should be structured as a unified operational ecosystem expressed through connected operational surfaces that support mission-time survey work, traceability, evidence interpretation, and broader cross-mission awareness.

The architecture is intended to:

* simplify operational workflows and reduce tool fragmentation
* give the active mission a stronger, clearer operating model
* separate decision, control, evidence, and traceability responsibilities more cleanly
* support cross-mission and multi-mission workflows as part of the same evolving ecosystem

---

## 2. Architectural Principles

| **Principle** | **Description** |
| --- | --- |
| **Modularity** | OI Survey should behave as a unified ecosystem of connected surfaces and services rather than one flat application shell. |
| **Mission-Centric Design** | The active mission remains the primary operational context for decision, control, evidence, and traceability. |
| **Surface-Specific Purpose** | Different operational questions should be answered by the right surface: overview, control, evidence, or cross-mission awareness. |
| **Reduced Complexity** | The architecture should reduce tool-switching and context reconstruction, especially inside single-mission workflows. |
| **Traceable State Management** | Actions, events, configuration changes, and observations should remain linked to mission context and reviewable later. |
| **Distributed Collaboration** | Multiple users and services should be able to contribute safely without collapsing authority boundaries. |
| **Scalable Architecture** | The product should expand across mission-level and cross-mission capability together, with future validated concurrency patterns building on both. |
| **Interoperability** | OIS should connect heterogeneous acquisition, navigation, telemetry, and specialist systems through coherent product abstractions. |

---

## 3. Conceptual Overview

OI Survey functions as a **unified operational ecosystem composed of connected surfaces and shared services**. The architecture should preserve a clear distinction between:

* the **active mission operating package**
* **evidence and QC capabilities**
* **traceability and service backbones**
* **cross-mission awareness**

This means the architecture should not treat every operational need as a feature inside one workspace. Instead, it should organize work across purpose-built surfaces that remain mission-aware and operationally coherent.

---

## 4. Core System Concepts

### 4.1 Mission Deck

**Mission Deck** is the mission-time container for the active mission. It is not one flat cockpit. It should coordinate the surfaces that matter most while a surveyor is working inside a single mission context.

Mission Deck contains, at minimum:

* **Mission Overview** as the default decision surface
* **Systems** as the deep operational and control surface

Mission Deck should help the surveyor understand the mission, move toward intervention safely, and stay oriented while related surfaces such as Online Log or Data Monitor are in use.

### 4.2 Mission Overview

**Mission Overview** is the primary decision surface for the active mission.

Its role is to answer:

* what is happening in this mission right now
* what needs attention now
* what issue or readiness concern is emerging
* what the next sensible action likely is

It should summarize mission posture, attention, and issue context without becoming the deep control surface itself.

### 4.3 Systems

**Systems** is the deep operational and control surface inside Mission Deck.

Its role is to support:

* selected-system understanding
* direct operational action and recovery
* system-specific configuration and dependency review
* mission-time investigation when action needs deeper operational context

### 4.4 Online Log

**Online Log** is the traceability service and operational record for the mission package.

It should:

* capture automated and user-generated events
* preserve the mission narrative across actions, anomalies, and handovers
* support downstream reporting and accountability

### 4.5 Data Monitor

**Data Monitor** is the package-level evidence and QC capability family.

It should cover:

* evidence viewing and monitoring
* stream-oriented interpretation
* QC review and comparison
* evolving forms such as stream viewers, QC surfaces, and detached evidence views

The current product direction should treat Data Monitor as the package-level capability name, even where implementation still appears through multiple specialized evidence surfaces rather than one consolidated module.

### 4.6 Multi-Mission Context

**Multi-Mission Context** is the cross-mission awareness surface.

Its role is to:

* show relative mission posture
* help prioritize where attention should shift
* support broader supervision patterns

It should remain parallel to the active mission package rather than becoming a detached future layer. As Mission Overview matures, Multi-Mission Context should progressively recombine the most important mission-level signals across several missions.

---

## 5. Module Architecture

| **Product Element** | **Primary Purpose** | **Architectural Role** |
| --- | --- | --- |
| **Mission Deck** | Active mission-time container | Coordinates the mission package and keeps active context coherent within the broader ecosystem. |
| **Mission Overview** | Primary decision surface | Summarizes posture, issue state, and next attention target for the active mission. |
| **Systems** | Deep operational/control surface | Hosts selected-system intervention, recovery, configuration, and dependency understanding. |
| **Online Log** | Traceability service | Preserves operational narrative, handover continuity, and downstream reporting support. |
| **Data Monitor** | Evidence and QC capability family | Supports evidence interpretation, monitoring, comparison, and QC-focused review. |
| **Multi-Mission Context** | Cross-mission awareness surface | Supports prioritization and safe attention shifting across missions by aggregating the most important mission-level signals. |
| **Specialized Subsystems** | Domain-specific workflows such as Hydrosens | Maintain deep workflow integrity while remaining connected to the broader package. |

---

## 6. Data and State Management

OIS should maintain coherent mission context across connected surfaces and services.

| **Function** | **Description** |
| --- | --- |
| **Mission Context Propagation** | The active mission should remain identifiable and stable across Mission Deck, Online Log, Data Monitor, and related workflows. |
| **State Separation** | Overview state, deep system state, evidence state, and cross-mission state should remain distinct enough to avoid confusion. |
| **Event Logging** | Actions, alerts, annotations, and service events should be captured with timestamps and attribution. |
| **Resilient Synchronization** | Surfaces and services should tolerate degraded connectivity without losing operational continuity. |
| **Cross-Surface Linking** | Users should be able to move between decision, control, evidence, and traceability without reconstructing context manually. |

---

## 7. Collaboration and Access Control

The collaboration model should support safe distributed work across surfaces and services.

* **Role-Based Access (RBAC):** Defines who can view, intervene, validate, or configure.
* **Shared Mission Context:** Users and services should operate against the same mission understanding.
* **Acknowledgement and Traceability:** Higher-consequence actions should remain legible and attributable.
* **Cross-Mission Awareness Without Overreach:** Multi-Mission Context should support supervision without replacing mission-time operating clarity.

| **Role** | **Capabilities** |
| --- | --- |
| **Surveyor / Operator** | Uses Mission Overview and Systems to supervise and intervene in the active mission. |
| **Senior Surveyor** | Validates setup, supports recovery, interprets evidence, and helps govern higher-consequence decisions. |
| **PEC / Supervisor** | Uses cross-mission and narrative surfaces for coordination and progress confidence. |
| **System Admin / Support** | Supports configuration, RBAC, and integration integrity across the package. |

---

## 8. Integration Model

OIS integrates with existing acquisition, navigation, telemetry, and specialist systems.  
These integrations should be abstracted into the product architecture without pretending every dependency is already absorbed into one native surface.

* **Upstream Systems:** Sensor data, navigation context, telemetry, environmental inputs.
* **Shared Services:** Logging, configuration governance, synchronization, and traceability.
* **Specialist Dependencies:** Hydrosens, Qinsy context, and other domain tools that remain operationally essential.

---

## 9. Scalability Framework

OIS should scale across mission-level and cross-mission operation together.

| **Level** | **Scaling Function** |
| --- | --- |
| **Mission-Level** | Strong active-mission package with clear internal surface roles. |
| **Cross-Mission Level** | Multi-Mission Context supports prioritization and attention management across assigned missions using a subset of the most important mission-level signals. |
| **Fleet-Level** | Shared services and broader operational views can support distributed oversight over time. |
| **Future Multi-Mission Level** | Operator-level multi-mission work remains a strategic future capability subject to validation. |

This framework preserves the path toward scale without turning cross-mission capability into a disconnected later-stage concern.

---

## 10. Security and Compliance Principles

* **RBAC Enforcement:** Role-based authentication and authority boundaries across surfaces and services.
* **Audit Trail:** Immutable or defensible logging of operational and mission events.
* **Fail-Safe Actions:** Validation of higher-consequence actions before execution.
* **Secure Communications:** Protected mission data and service channels.
* **Data Integrity:** Strong linkage between action, evidence, configuration, and traceability.

---

## 11. Evolution Path

> **Note:** The following is an indicative capability progression, not a committed roadmap.

| **Capability Area** | **Initial Focus** | **Next Maturity Step** | **Future (Subject to Validation)** |
| --- | --- | --- | --- |
| **Mission Package** | Clear Mission Deck structure with Mission Overview and Systems | Stronger configuration and subsystem integration | Broader adaptive mission orchestration |
| **Evidence and QC** | Data Monitor expressed through stream views, QC surfaces, and detached evidence | Clearer package-level consolidation and cross-surface workflows | Richer cross-sensor interpretation and automation |
| **Traceability** | Online Log as service backbone | Deeper automation, reporting, and service integrations | Analytics and operational intelligence on top of traceability data |
| **Cross-Mission Awareness** | Parallel Multi-Mission Context development informed by mission-level signals | Stronger prioritization and supervisory patterns | Validated operator-level multi-mission support |

| **Phase** | **Description** | **Goal** |
| --- | --- | --- |
| **Phase 1 (Core Operating Ecosystem)** | Strong active-mission structure across Mission Deck, Mission Overview, Systems, Online Log, and Multi-Mission Context direction. | Establish credible ecosystem clarity across mission-level and cross-mission work. |
| **Phase 2 (Connected Surfaces)** | Expand Data Monitor, subsystem links, configuration/service coherence, and cross-mission aggregation logic. | Strengthen evidence and operational continuity. |
| **Phase 3 (Cross-Mission Scale)** | Mature Multi-Mission Context and future concurrency patterns where validated. | Extend operational reach without losing ecosystem coherence. |

---

## 12. Summary

The OIS architecture defines a **modular operational package** designed to:

* strengthen the active mission operating model
* separate overview, control, evidence, and cross-mission responsibilities clearly
* preserve traceability and service coherence across the package
* support cross-mission and multi-mission capability as part of one evolving ecosystem

---

**End of Document**  
*"One ecosystem, clarified through connected surfaces rather than one overloaded workspace."*

### DOCUMENT END | PFD.03

### DOCUMENT START | PFD.04 | Product Pillars

- kind: `doc_id`
- id: `PFD.04`
- title: `Product Pillars`
- path: `00_Product_Foundation/PFD.04_Product_Pillars.md`
- section_id: `00PF`
- section_title: `Product Foundation`
- canonical_role: `canonical_doc`
- estimated_tokens: `2225`

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

### DOCUMENT END | PFD.04

## SECTION END | 00PF

## SECTION START | 01UX | UX Research

- section_id: `01UX`
- title: `UX Research`
- base_path: `01_UX_Research`
- tags: [research, roles, workflows, insights]
- document_count: `9`

### DOCUMENT START | UXR.00 | User Research Summary

- kind: `doc_id`
- id: `UXR.00`
- title: `User Research Summary`
- path: `01_UX_Research/UXR.00_User_Research_Summary.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `3519`

---
doc_id: UXR.00
version: 0.3.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, user-insights, ois, operator-workflows]
---

# UXR.00 - User Research Summary

<!--
Changes made:
1. Added standardized front-matter for consistency.
2. Updated heading formatting to clean ASCII.
3. Added sensor availability and operational prevalence synthesis based on catalog and usage summary.
-->

**Version:** 1.3  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Updated - Includes Task-Tool Mapping and Sensor Grounding

---

## 1. Purpose & Scope

This document consolidates user research for OIS. It summarizes **who our users are**, **how they work** (operations, tasks, and tools), **their pain points**, and **opportunity areas** that inform product pillars and feature design.

Derived from validated internal studies, operational data, and workshop results.

---

## 2. Methods & Sources (Evidence Base)

- Multi-role interviews and observational sessions (Surveyor, Senior Surveyor, PEC, IT).
- Operational-workflow transcription and cross-system tool audits.
- Workshop on pain points and feature priorities.
- Quantitative task-tool datasets (new integration 2025-10-25).
- Sensor catalog and Planner-derived usage summary used as an additional grounding layer for sensor availability and prevalence.

Primary sources: `OI_SMP_Full_UX_Research.md`, `Operational_Workflows.md`, `OperationTypesWorkflows.md`, `Surveyor_Tasks.csv`, `Workshop_workflow_map-features-pain.xlsx`, `Underwater Survey Operations - Task Structure`, `DLog 241025 SMP Direction Update.md`, sensor catalog, and Planner-derived sensor usage summaries.

---

## 3. Participants & Roles (Operational Ecosystem)

| Role | Core Responsibilities | Typical Decisions / Authority | Top Pain Points |
| --- | --- | --- | --- |
| **Surveyor (Operator)** | Operate and monitor sensors; real-time QC and logging. | Start/stop logging; minor config; line selection. | Fragmented tool use, manual logging checks, limited remote control. |
| **Senior Surveyor** | Supervise execution, perform calibrations, ensure spec compliance. | Approve critical settings; handle mobilisation and troubleshooting. | Manual MAC and daily reports; no central diagnostics. |
| **PEC / Supervisor** | Coordinate missions, reallocate vessels or teams, client communication. | Prioritise operations, review data delivery timelines. | Limited multi-mission visibility and handover traceability. |
| **IT Support** | Network access, whitelisting, security approval. | Port rules and MAC/IP management. | Ticketing delays impact mobilisation readiness. |

---

## 4. Operation Types & Contexts

| Operation Type | Purpose / Characteristics | Equipment & Tools |
| --- | --- | --- |
| **Pipeline / Cable Inspection (IMR)** | Highly visual and decision-heavy; requires precise orientation and rapid QC. | ROV + HD video, MBES/SSS, QINSy NAV Display, Online Log, OneNote for handover. |
| **Geophysical** | Fast coverage of large areas with remote instruments. | Discover SSS, Inomar SBP, SIS MBES, Rovins INS, QINSy / EIVA / APOS. |
| **Geotechnical** | Slow, sampling-intensive operations with frequent waiting and manual annotation. | CPT / Vibrocorer, QINSy, EIVA, APOS, manual Redgate logging. |
| **OBN (Ocean Bottom Nodes)** | Seabed seismic workflow built around node deployment, source acquisition, and recovery/reconciliation. | Node programming and inventory tools, deployment/recovery systems, source coordination tools, positioning/QC systems. |
| **Geophysical with ROV** | Close-in, maneuver-driven survey around assets or complex seabed using powered vehicles and mixed payloads. | ROV control system, sonar/camera payloads, USBL/INS, navigation display, Online Log. |
| **Geophysical with ROTV** | Controlled towed-vehicle corridor survey balancing speed and stable sensor altitude. | ROTV control/telemetry, SSS/MBES/magnetometer payloads, navigation/tow management tools, QC viewers. |
| **Geophysical with AUV** | Autonomous or supervised-autonomous geophysical survey driven by mission plans and post-mission ingest/QC. | AUV mission planning tools, onboard acoustic/imaging payloads, acoustic tracking/comms, recovery and data offload tools. |

---

## 5. Operational Phases & High-Level Workflows

**Typical phases:** Project Startup -> Planning -> Mobilisation -> Calibration -> Operation -> Recovery / Retrieval -> Shift Handover -> Reporting.

Key friction themes: network whitelisting, multi-tool integration, manual reporting, bandwidth limits for remote ops, and mission-state reconciliation for deployed or autonomous assets.

---

## 6. Tasks & Tool Usage (Expanded Dataset 2025-10-25)

| Operation Type | Role | Task Type | Task | Tool / Software Used | Notes |
| --- | --- | --- | --- | --- | --- |
| Geo / Pipeline | Surveyor | Navigation | Check which survey line is running | QINSy Quantum (GPS navigation) | Routine start-of-shift check for context. |
| Geotechnical | Surveyor | Navigation | Position vessel for CPT or Vibrocore deployment | QINSy Quantum | Precise position required per client spec. |
| Geotechnical | Surveyor | Navigation | Move to next planned sampling point | QINSy Quantum | Task sequencing after core recovery. |
| Pipeline Inspection | Surveyor | Navigation | Check infrastructure and exclusion zones | Background data in QINSy Display | Avoid collision with ROV equipment. |
| Pipeline Inspection | Surveyor | Navigation | Check current KP (Kilometer Point) reference | QINSy | Maintains alignment and traceability. |
| Pipeline Inspection | Surveyor | Navigation | Orient vessel within 500 m exclusion zone | QINSy (positional guidance) | Part of permit-time management. |
| Pipeline Inspection | Senior Surveyor | Navigation | Validate each pipeline KP reference is correct | QINSy (Line-plan view) | Ensures data coherence and offset accuracy. |
| Pipeline Inspection | PEC / Senior Surveyor | Navigation | Reposition vessel when time limit reached | QINSy planning + situational view | Prevent idle vessel time. |
| Geo / Pipeline | Surveyor | Data Logging & Validation | Verify parameters logged per project manual | Redgate (local file structure) | Manual folder inspection even if status green. |
| Geotechnical | Surveyor | Data Logging & Validation | Set up extra log files as requested | Redgate folders | Client/offline team customization. |
| Pipeline Inspection | Surveyor | Data Logging & Validation | Confirm video overlay accuracy (KP, pipe name, node) | VOYIS / RVHD cams / QINSy / Windy | Ensures synchronized metadata. |
| Pipeline Inspection (IMR) | 3.4U Inspector | Data Logging & Validation | Perform visual inspection and video logging | VOYIS / RVHD cams | Visual confirmation of asset condition. |
| Geo / Pipeline | Surveyor | Data Logging & Validation | Maintain online log of vessel and survey activities | Online Log | Primary timeline of events. |
| Pipeline Inspection | Surveyor | Data Logging & Validation | Comment on pipe abnormalities linked to position | Online Log | Geospatially referenced annotations. |

*Sources: Task Structure transcription + Surveyor_Tasks.csv (verified Oct 2025).*

---

## 7. Sensor Availability and Operational Prevalence

The sensor catalog and Planner-derived usage summary are useful because they sharpen which sensor families appear to matter most operationally and where OIS should avoid treating every sensor as the same kind of product object.

### 7.1 High-prevalence primary acquisition families

| Sensor Family | Usage Signal | Design Relevance |
| --- | --- | --- |
| **MBES** | Strongest prevalence signal in the material provided, with broad vessel usage and high total days. | Should remain a first-class reference workflow for control, QC, and logging confidence. |
| **SSS** | High prevalence across geophysical operations and many vessels. | Supports corridor survey, anomaly marking, revisit logic, and high-throughput QC workflows. |
| **SBP** | High prevalence alongside MBES and SSS in geophysical campaigns. | Reinforces the value of line-time monitoring plus post-line validation. |
| **Magnetometer** | Strong prevalence in geophysical work across multiple vessels. | Important for overlay/QC workflows and for distinguishing real-time display from richer post-processing outputs. |

### 7.2 Critical supporting and dependency systems

| Sensor / System Type | Evidence from Catalog | Design Implication |
| --- | --- | --- |
| **INS / GNSS / USBL / Time Sync** | Multiple variants appear in the catalog, including vessel-, ROV-, and network-specific notes. | Readiness, positioning confidence, and timing integrity should be highly visible in OIS. |
| **PDU / MUX** | Present as available operational systems, not just abstract infrastructure concepts. | Supports dedicated command-and-impact workflows already reflected in the prototype direction. |
| **SVS / SVP** | Notes indicate quality-control needs and direct coupling to MBES workflows. | OIS should distinguish between raw availability and QA-verified environmental input quality. |

### 7.3 Sensors that should not be modeled as generic controllable devices

| Sensor / System Type | Catalog Signal | Design Implication |
| --- | --- | --- |
| **ADCP (Signature 500)** | Self-logging and downloaded at end of project. | Treat as delayed-validation / post-recovery workflow, not as a normal live-controlled sensor. |
| **DVL (ROV Mounted) Syrinx** | Tightly coupled to SprintNav 500, not an independent OI Config item. | Treat as a dependent subsystem within vehicle/navigation context, not always as a standalone pane. |
| **MGC R3** | Connects through SeaPath 385 software. | Some systems should be represented through parent-system state rather than as direct control endpoints. |
| **Ranger2 Pro** | No API; ASCII commands used. | Control and integration depth will vary by sensor, so OIS should not assume uniform command affordances. |
| **Veripos LD900** | API uncertainty noted. | Availability in OIS may depend on integration maturity, not just operational importance. |

### 7.4 Current interpretation for OIS prioritization

1. **MBES, SSS, SBP, and Magnetometer** are the strongest geophysical reference families for shaping the baseline survey experience.
2. **INS, GNSS, USBL, and Time Sync** should be treated as operationally critical dependencies with visible confidence and failure states.
3. **Vehicle-mounted and coupled sensors** require different modeling than vessel-mounted standalone systems.
4. **Self-logging or delayed-ingest devices** create a distinct workflow that spans deployment, recovery, ingest, and later QC.

---

## 8. Pain Points (Synthesised)

- **Tool Fragmentation** - Operators use >8 applications per mission; no unified state view.
- **Manual Logging and Verification** - Redundant folder checks and manual QC of green indicators.
- **Handover Consistency** - Online Log vs OneNote dual systems create gaps.
- **Role Overlap** - Senior Surveyor re-checks tasks done by Surveyor due to trust gaps in systems.
- **Remote Ops Latency** - Bandwidth and RDP performance limit real-time collaboration.
- **Sensor Model Mismatch** - Not all sensors behave like first-class controllable endpoints, but many current toolchains force operators to treat them inconsistently.

---

## 9. Opportunity Themes (Mapped to Pillars)

| Theme | Pillar -> Module | Opportunity |
| --- | --- | --- |
| **Unified Control and Safety** | C&C -> Sensor Control, Configuration Manager | Aggregate ON/OFF/Restart and logging commands with role-based ack loops. |
| **Active Monitoring and QC** | AM -> Output Monitoring, Diagnostics & Health | Live multi-sensor views, thresholds, auto-validation of parameters. |
| **Traceability and Auditability** | Cross -> Online Log, File Monitoring | Auto-log commands + events for seamless handover. |
| **Collaborative Operations** | Cross -> RBAC & Collaboration | Supervisors join sessions without interrupting others. |
| **Operational Efficiency** | Platform -> Mission Deck / Multi-Mission Context | Enable multi-mission operation (2-4 missions per operator). |
| **Sensor-Aware Modeling** | Cross -> Sensor Control, Active Monitoring, File Monitoring | Differentiate between controllable devices, coupled subsystems, dependency systems, and delayed-ingest assets. |

---

## 10. Implications for OIS Strategy

- **Reduce tool count** and centralize control and QC tasks within OIS.
- **Design for multi-mission workspaces** and triage management.
- **Automate log consistency checks** and system traceability.
- **Support remote assist and session sharing** natively.
- **Differentiate control models** between fully controllable sensors, coupled subsystems, dependency systems, and delayed-ingest devices.

---

## 11. Open Questions / Data Needs

1. Final role taxonomy confirmation (Survey Assistant? Client Rep?).
2. Quantitative benchmarks for missions per operator and alert tolerance.
3. Upstream integration scope (DP, weather feeds).
4. Remote ops bandwidth thresholds for multi-stream viewing.
5. Detailed workflow validation for OBN, ROV-, ROTV-, and AUV-assisted survey patterns as OIS scope matures.
6. Mapping of sensor families to operation types beyond the current high-level geophysical prevalence summary.
7. Confirmation of which cataloged sensors are expected to become first-class OIS control surfaces versus monitored dependencies.

---

## 12. Canonical Sources

- **Full UX Research** - Roles, phases, pain points, tool dataset.
- **Operational Workflows** - Mobilisation and operation steps.
- **Operation Types** - IMR / Geo / Geotech specifics.
- **Workshop Matrix** - Pain points and feature links.
- **Direction Update** - Multi-mission and collaboration focus.
- **Current State Deck** - Operational foundation and near-term improvements.
- **Sensor Catalog and usage summary** - Available sensor families, integration notes, and relative operational prevalence.

---

**End of Document**

*"Ground truth captured - OIS design anchored in operator reality."*

### DOCUMENT END | UXR.00

### DOCUMENT START | UXR.01 | Roles and Responsibilities

- kind: `doc_id`
- id: `UXR.01`
- title: `Roles and Responsibilities`
- path: `01_UX_Research/UXR.01_Roles_and_Responsibilities.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `2466`

---
doc_id: UXR.01
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, roles, workflows, responsibilities, ois]
---

# UXR.01 – Roles and Responsibilities

<!--
Changes made:
1) Added standardized front-matter for repository consistency.
2) Updated H1 heading to the standardized format (“# UXR.01 – Roles and Responsibilities”).
3) All body text below remains verbatim; sources remain as literal references (not links).
-->

**Version:** 1.0

**Date:** 2025-10-25

**Owner:** OIS Research & Design

**Status:** Draft (evidence-based)

---

## 1. Purpose & Scope

This document defines the **key roles involved in underwater survey operations**, their core responsibilities, decision-making boundaries, and tool dependencies.

It highlights how these roles interact across operation types (Geophysical, Geotechnical, Pipeline/IMR) and how OIS can support their evolving collaboration patterns — particularly in the shift toward **multi-mission, reduced-headcount operations**.

---

## 2. Methodology & Sources

Derived from:

- UX research interviews and onboard observation logs (`OI_SMP_Full_UX_Research.md`)
- Operational workflow documents (`OI_Operational_Workflows.md`, `OperationTypesWorkflows.md`)
- Role–task–tool dataset (Oct 2025 update)
- Workshop workflow & pain mapping matrix
- “Underwater Survey Operations – Task Structure” transcription

---

## 3. Role Overview (Hierarchy and Relationships)

| **Role** | **Primary Focus** | **Operational Level** | **Decision Scope** | **Typical Collaboration** |
| --- | --- | --- | --- | --- |
| **Surveyor (Operator)** | Day-to-day sensor control, data QC, logging, and real-time monitoring. | Mission / Line level | Start/stop lines, verify data integrity, minor config. | Senior Surveyor (review), PEC (coordination), 3.4U Inspector (visual). |
| **Senior Surveyor** | Oversees quality, configuration, and line validation. Troubleshoots data anomalies and coordinates multi-sensor calibration. | Vessel / Mission level | Authorizes configuration changes, supervises handovers, oversees reporting. | Surveyors (support), PEC (planning), Client Rep (validation). |
| **Project Execution Coordinator (PEC)** | Operational planning, client liaison, and vessel task allocation. | Project level | Reassigns resources, approves time-limited operations, reviews progress. | Senior Surveyor (execution), Survey Advisor (oversight). |
| **Survey Advisor / Data Manager** | Ensures data product integrity, standardization, and delivery compliance. | Cross-project | Validates final logs, QC results, and metadata consistency. | Senior Surveyor (data origin), PEC (handover). |
| **IT / Network Support** | Ensures system connectivity, security, and access. | Global support | Manages whitelisting, port setup, and user access. | Surveyor / Supervisor (field), Remote Ops (support). |

---

## 4. Role-by-Role Analysis

### 4.1 Surveyor (Operator)

**Primary Goals:**

- Maintain continuous data acquisition and QC.
- Execute lines accurately and follow configuration protocols.
- Maintain shift consistency and logging accuracy.

**Core Tasks:**

- Start/stop logging, verify folder structure.
- Check live sensor feeds (INS, MBES, SSS, cameras).
- Perform Online Log entries and event annotations.
- Communicate deviations or abnormalities.

**Tools Used:**

QINSy / Quantum, Discover, Inomar, SIS, EIVA Touchpad, APOS, VOYIS / RVHD, Online Log, OneNote.

**Pain Points:**

- Frequent manual verification across tools (“green but not recording”).
- No consolidated overview of data health.
- Bandwidth limitations in remote operation.

**Opportunities for OIS:**

- Unified status dashboard (Active Monitoring).
- Auto-verification of data stream and logging states.
- Context-aware logging shortcuts and consistency templates.

---

### 4.2 Senior Surveyor

**Primary Goals:**

- Guarantee mission compliance with project specifications.
- Supervise configurations and QC thresholds.
- Mentor surveyors and handle escalation points.

**Core Tasks:**

- Validate KP references and navigation lines.
- Execute calibrations and daily MAC reports.
- Review Online Logs for consistency.
- Support triage when sensors fail or misconfigure.

**Tools Used:**

QINSy (line plans, KP validation), Excel MAC templates, Online Log, Planner / reporting tools.

**Pain Points:**

- Manual MAC preparation with screenshots.
- No central configuration rollback.
- Limited cross-mission visibility.

**Opportunities for OIS:**

- Config template management and rollback functions.
- Role-based configuration lock.
- Cross-mission supervisory view (Mission Deck).

---

### 4.3 Project Execution Coordinator (PEC)

**Primary Goals:**

- Maintain mission progress within permit and time constraints.
- Manage vessel task allocation and downtime efficiency.

**Core Tasks:**

- Review mission coverage; reassign resources when time limits are reached.
- Communicate with Senior Surveyor for repositioning.
- Review daily operations and logs.

**Tools Used:**

Planner, QINSy (navigation planning), Online Log (summaries).

**Pain Points:**

- No real-time progress visualization across concurrent missions.
- Manual coordination with vessel operations.

**Opportunities for OIS:**

- Mission overview dashboard with completion metrics.
- Alert-based downtime indicators.

---

### 4.4 Survey Advisor / Data Manager

**Primary Goals:**

- Oversee QC delivery pipeline and metadata standards.
- Ensure traceability from acquisition to client output.

**Core Tasks:**

- Validate daily logs and handovers.
- Verify data file structure and naming compliance.
- Manage long-term data archiving.

**Tools Used:**

Network folders, Redgate, Planner, custom QC scripts.

**Pain Points:**

- Non-standardized metadata between operations.
- Manual cross-verification of event logs and folders.

**Opportunities for OIS:**

- Integrated Online Log → File structure linkage.
- QC compliance report generation.

---

### 4.5 IT / Network Support

**Primary Goals:**

- Maintain stable, secure connectivity and access control.
- Minimize mobilisation delays related to network and security.

**Core Tasks:**

- Handle IP/MAC approvals and firewall adjustments.
- Support bandwidth diagnostics.
- Troubleshoot remote session issues.

**Pain Points:**

- Delayed approval process disrupts mobilisation.
- Lack of diagnostic tools accessible to operators.

**Opportunities for OIS:**

- Embedded diagnostics / ping-test module.
- Operator-level pre-check routines before mobilisation.

---

## 5. Cross-Role Interaction Model

| **Collaboration Context** | **Participants** | **Current Mode** | **Pain Point** | **OIS Opportunity** |
| --- | --- | --- | --- | --- |
| **Shift Handover** | Surveyor ↔ Surveyor | OneNote + verbal | Inconsistent details, missing anomalies | Structured handover interface integrated with Online Log |
| **QC Review** | Surveyor ↔ Senior Surveyor | Shared folders, MAC | Redundant re-checking | Automated QC validation dashboard |
| **Troubleshooting** | Surveyor ↔ Senior Surveyor ↔ IT | RDP, Teams | Session interference | Multi-user “assist” mode with isolation |
| **Mission Oversight** | Senior Surveyor ↔ PEC | Daily reports | No live mission progress view | Mission Deck with live metrics and completion maps |
| **Data Delivery** | Senior Surveyor ↔ Data Manager | Manual file verification | Missing traceability | Log-linked file verification and QC summary generation |

---

## 6. Evolving Role Dynamics in OIS

As OIS introduces automation and multi-mission control:

| **Role Evolution** | **Change Introduced by OIS** | **Impact** |
| --- | --- | --- |
| Surveyor | Gains ability to monitor multiple missions simultaneously. | Reduces idle time; requires new alert prioritization tools. |
| Senior Surveyor | Focus shifts to supervision and triage rather than micromanagement. | Increases oversight efficiency and reduces redundant checks. |
| PEC | Moves from manual coordination to strategic triage and optimization. | Improves throughput and vessel utilization. |
| Data Manager | Benefits from automatic log–file integration and QC traceability. | Ensures auditability and consistent delivery. |
| IT | Sees reduced support tickets via embedded diagnostics. | Increases operational uptime and self-sufficiency. |

---

## 7. Role-to-Module Mapping (OIS Impact Matrix)

| **Role** | **Key OIS Modules** | **Primary Interactions** |
| --- | --- | --- |
| Surveyor | Sensor Control, Output Monitoring, Online Log | Execute commands, review data, annotate logs. |
| Senior Surveyor | Configuration Manager, Diagnostics & Health, Mission Deck | Supervise configuration, validate QC, oversee multiple missions. |
| PEC | Mission Deck, File Monitoring | Monitor completion %, manage downtime and vessel reallocation. |
| Data Manager | Online Log, File Monitoring | Audit logs and file traceability, generate QC reports. |
| IT Support | Diagnostics & Health | Conduct connectivity tests, monitor system status remotely. |

---

## 8. Summary: Design Implications

1. **Interfaces must reflect role granularity** — e.g., configuration locks by role.
2. **Multi-user concurrency is essential** — roles must work on shared missions without interference.
3. **Task and tool consolidation** should focus on reducing redundant manual checks.
4. **Supervisory roles** require multi-mission overviews, while operators need focus-preserving views.
5. **Collaboration and traceability** are foundational across all roles.

---

## 9. Canonical Sources

- `2.1.OI_SMP_Full_UX_Research.md`
- `2.3.OI_Operational_Workflows.md`
- `2.3.1.OperationTypesWorkflows.md`
- `Underwater Survey Operations – Task Structure`
- `Surveyor_Tasks.csv`
- `Workshop_workflow_map-features-pain.xlsx`

---

**End of Document**

*“Understand the people — design the system.”*

### DOCUMENT END | UXR.01

### DOCUMENT START | UXR.02 | Operation Types and Workflows

- kind: `doc_id`
- id: `UXR.02`
- title: `Operation Types and Workflows`
- path: `01_UX_Research/UXR.02_Operation_Types_and_Workflows.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `6145`

---
doc_id: UXR.02
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
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

### DOCUMENT END | UXR.02

### DOCUMENT START | UXR.03 | Tasks and Tools Matrix

- kind: `doc_id`
- id: `UXR.03`
- title: `Tasks and Tools Matrix`
- path: `01_UX_Research/UXR.03_Tasks_and_Tools_Matrix.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `3592`

---
doc_id: UXR.03
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, tasks, tools, matrix, ois]
---

# UXR.03 - Tasks and Tools Matrix

<!--
Changes made:
1. Added standardized front-matter block.
2. Updated H1 heading to match naming convention.
3. Expanded the matrix to include OBN and vehicle-assisted geophysical workflows.
4. Preserved the original evidence-based structure while marking the expanded operation types as a working model pending direct SME confirmation.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Complete Baseline (with Pain & Opportunity Overlay)

---

## 1. Purpose & Scope

This document provides a **comprehensive matrix** connecting operational tasks, tools, and user roles across the primary survey operation types in scope - **Geophysical**, **Geotechnical**, **Pipeline / IMR**, **OBN**, and vehicle-assisted geophysical modes such as **ROV**, **ROTV**, and **AUV** survey work.

It identifies how current workflows function, where pain points occur, and highlights the **strategic opportunities for the OI Survey (OIS)** to improve efficiency, safety, and collaboration.

This file serves as the factual and analytical backbone linking **User Research**, **Operational Workflows**, and **Feature Framework** design.

This version expands the matrix to also cover **OBN** and vehicle-assisted geophysical modes such as **ROV**, **ROTV**, and **AUV** survey work.

---

## 2. Methodology & Evidence Base

This matrix is derived from:

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`

All findings are evidence-based and consolidated from verified operational research, workshop discussions, and field observations (2023-2025).

For OBN, ROV-, ROTV-, and AUV-assisted workflows, the added rows below are grounded in the internal workflow synthesis plus external operational references used to expand `UXR.02`. They should be treated as a validated working model for product design, pending direct SME confirmation for contractor- or vessel-specific variations.

---

## 3. Operational Task Matrix

| Operation Type | Role | Task Type | Task Description | Tool(s) | Pain Point | OIS Opportunity |
| --- | --- | --- | --- | --- | --- | --- |
| Geophysical / Geotechnical / Pipeline | Surveyor | Navigation | Check current survey line | QINSy / Quantum | Switching between software for progress checks; poor line tracking visualization. | Unified line tracker with live completion % and deviation alerts. |
| Geotechnical | Surveyor | Navigation | Position vessel for sampling (CPT / Vibrocore) | QINSy / Quantum | Manual positioning requires constant verbal communication with bridge. | Integrated deck and survey alignment view with position confirmation. |
| Geotechnical | Surveyor | Navigation | Move to next station | QINSy | No automation of next-point navigation. | Auto-next-line / waypoint trigger integrated with mission plan. |
| Pipeline / IMR | Surveyor | Navigation | Check infrastructure and exclusion zones | QINSy Display | Risk of ROV collision; manual reference check. | Overlay infrastructure zones and ROV footprint in navigation map. |
| Pipeline / IMR | Senior Surveyor | Navigation | Validate KP reference and offsets | QINSy / Line-plan view | Requires manual spreadsheet cross-check. | Automated KP validation tool with offset tolerance alerts. |
| Pipeline / IMR | PEC | Navigation | Reposition vessel when time limit reached | QINSy / Planner | Requires manual tracking of permit duration. | Mission time management with alert for permit expiry. |
| OBN | Surveyor / Senior Surveyor | Navigation | Confirm node deployment pattern, patch progress, and recovery coverage | Deployment planning tools / positioning systems | Deployment and recovery state is often tracked across fragmented tools or spreadsheets. | Mission-aware node map with deployment, recovery, and exception status. |
| Geophysical with ROV | Surveyor / ROV Pilot | Navigation | Maintain target alignment and vehicle position relative to asset or route | ROV control system / USBL-INS / navigation display | Vehicle position, target context, and survey intent are split across multiple interfaces. | Shared vehicle-and-target navigation view with georeferenced anomaly context. |
| Geophysical with ROTV | Surveyor | Navigation | Maintain tow-body altitude, line-keeping, and corridor overlap | Tow control / navigation / layback tools | Tow geometry and corridor progress are hard to interpret quickly during long runs. | Unified corridor view with tow-state, altitude, and overlap confidence. |
| Geophysical with AUV | Senior Surveyor / mission lead | Navigation | Validate mission plan, route coverage, and abort boundaries | Mission planning software / navigation planning tools | Mission logic and operational constraints are reviewed outside the live operational picture. | Mission-plan review with risk zones, abort logic, and sortie readiness checks. |
| All | Surveyor | Data Logging & Validation | Verify if parameters are correctly logged | Redgate / Folder Structure | Manual folder check even when tool shows "green". | Auto-logging validation integrated with data status indicator. |
| Geotechnical | Surveyor | Data Logging & Validation | Set up extra log files based on client needs | Redgate | Time-consuming manual folder setup. | Configuration templates for client log structures. |
| Pipeline / IMR | Surveyor | Data Logging & Validation | Check video overlays and camera node settings | VOYIS / RVHD / QINSy | Manual verification; frequent mismatch between video and telemetry. | Unified camera config and overlay verification tool. |
| Pipeline / IMR | 3.4U Inspector | Data Logging & Validation | Inspect pipeline visually and record abnormalities | VOYIS / HD Cams | Requires manual logging of anomalies. | Auto-log abnormality snapshots linked to position. |
| OBN | Surveyor / Data Manager | Data Logging & Validation | Reconcile programmed, deployed, recovered, and downloaded node states | Node inventory tools / spreadsheets / file tracking | Inventory and data-state reconciliation is manual and error-prone, especially when exceptions occur. | Unified node lifecycle tracker linking deployment, recovery, and ingest state. |
| Geophysical with ROV | Surveyor | Data Logging & Validation | Capture anomalies with synchronized position, media, and survey context | Online Log / video capture / navigation-linked annotations | Findings are recorded across separate video, note, and position systems. | One action to create event, screenshot or clip, and position-linked annotation together. |
| Geophysical with AUV | Surveyor / Data Manager | Data Logging & Validation | Verify sortie metadata, offload completeness, and mission-to-data association | Mission logs / data offload tools / file tracking | Post-mission data validation is delayed and disconnected from the operational timeline. | Sortie ingest checklist linking mission plan, recovery event, and data completeness. |
| All | Surveyor | Data Logging & Validation | Record survey events in Online Log | Online Log | Manual event entry, risk of missing key events. | Auto-event capture for line start/stop, calibration, deviation. |
| Pipeline / IMR | Surveyor | Data Logging & Validation | Add comments linked to KP reference | Online Log | Requires manual cross-referencing with map. | Auto-tag comments with geolocation from nav feed. |
| All | Surveyor / Senior | Monitoring & QC | Monitor sensor feeds (MBES, SSS, INS, CTD, video) | SIS / Discover / Inomar / EIVA / VOYIS | Multiple UIs; high cognitive load. | Multi-sensor dashboard with unified visual and QC layers. |
| All | Surveyor | Monitoring & QC | Check alarms and thresholds | Native Sensor Software | Inconsistent alarm hierarchies across tools. | Centralized alert panel with configurable severity levels. |
| Pipeline / IMR | Senior Surveyor | Monitoring & QC | Conduct sensor health check | QINSy / Diagnostics | Manual verification only during setup. | Auto-diagnostics with periodic health reports. |
| OBN | Surveyor / Senior Surveyor | Monitoring & QC | Monitor node exceptions, source-pass status, and recovery completeness | Node management / source coordination / operational status tools | Recording confidence and missing-node risk are not visible in one place during operations. | Exception-focused dashboard for node state, source progress, and recovery risk. |
| Geophysical with ROV | Surveyor / Senior Surveyor | Monitoring & QC | Monitor vehicle health, tether/comms, payload status, and live evidence quality | ROV control system / sonar-video viewers / diagnostics | Health, vehicle state, and evidence quality are split across pilot and survey displays. | Role-aware shared monitoring view with vehicle state and evidence quality in one place. |
| Geophysical with ROTV | Surveyor / Senior Surveyor | Monitoring & QC | Assess tow stability, altitude, sensor quality, and revisit triggers | Tow telemetry / sensor viewers / navigation display | Operators infer data quality degradation indirectly from several tools. | Correlate tow-body behavior with sensor-quality degradation and revisit guidance. |
| Geophysical with AUV | mission lead / Senior Surveyor | Monitoring & QC | Track vehicle status, navigation confidence, endurance, and abort conditions during sortie | AUV supervision / acoustic comms / mission status tools | Supervisory awareness is sparse and difficult to compare against mission intent. | Mission supervision panel showing sortie health, navigation confidence, and exception thresholds. |
| All | Surveyor / Senior | Communication & Handover | Conduct shift handover (notes, discussion) | OneNote / Verbal | Inconsistent documentation, data loss across shifts. | Integrated Handover Log linked to Online Log. |
| OBN / ROV / ROTV / AUV | Surveyor / Senior | Communication & Handover | Transfer deployed-asset state, unresolved exceptions, and revisit logic | Verbal / notes / Online Log | Complex mission-state context is easy to lose during handover when the asset is deployed or autonomous. | Structured handover snapshot for deployed assets, active exceptions, and next required action. |
| All | Senior / PEC | Reporting | Prepare daily report and QC summary | Planner / Excel | Manual compilation from multiple data sources. | Auto-generated daily report with key mission metrics. |
| Geotechnical | Surveyor | Reporting | Verify log file structure before delivery | Redgate | File name inconsistencies and missing logs. | Automated file integrity and naming check. |
| Pipeline / IMR | Senior Surveyor | Reporting | Produce MAC / calibration reports | Excel / Word | Manual image capture and parameter copy. | Auto-MAC template generator with embedded images. |
| OBN | Senior Surveyor / Data Manager | Reporting | Produce deployment/recovery reconciliation and exception summary | Excel / reporting packs / inventory exports | Reporting requires manual merge of node inventory, recovery status, and issue logs. | Auto-generated node reconciliation and exception report. |
| Geophysical with AUV | Senior Surveyor / Data Manager | Reporting | Review sortie outcome and decide on rerun or follow-up mission | Mission replay / QC review / reporting tools | Sortie review is separated from planning and ingest context, slowing rerun decisions. | Sortie review package linking plan, execution, QC summary, and rerun recommendation. |

---

## 4. Shared vs. Unique Tasks

| Category | Shared Across All Ops | Unique to Specific Ops |
| --- | --- | --- |
| **Navigation** | Line or task selection, progress tracking | IMR: orientation and exclusion zone control; Geotech: station positioning; OBN: deployment/recovery coverage; ROV/ROTV/AUV: vehicle or sortie path control |
| **Data Logging & Validation** | Parameter validation, event capture, data-state checks | IMR: video overlay validation; Geotech: event-based log setup; OBN: node lifecycle reconciliation; AUV: sortie ingest validation |
| **Monitoring & QC** | Sensor data review, alarms, readiness checks | IMR: visual QC and anomaly interpretation; Geo: coverage completion; OBN: exception and recovery completeness; ROV/ROTV/AUV: vehicle-state-aware QC |
| **Communication & Handover** | Shift exchange, log update | Deployed or autonomous assets require explicit transfer of active state, exceptions, and revisit logic |
| **Reporting** | Daily summaries, QC checks | IMR: MAC report preparation; Geotech: client event file review; OBN: node reconciliation; AUV: sortie outcome review |

---

## 5. Insights Summary

**Top Pain Point Categories:**

1. **Tool Fragmentation:** Operators use 8-12 separate applications per mission.
2. **Manual Verification:** Data integrity checks require folder-level inspection.
3. **Redundant Logging:** Online Log, OneNote, and manual reports duplicate information.
4. **Lack of Standardization:** No consistent thresholds or templates across operation types.
5. **Limited Visibility:** Supervisors lack a live mission overview.
6. **Mission-State Reconciliation:** Deployed or autonomous assets create delayed validation and exception-tracking work.

**Key OIS Opportunities:**

* Consolidate navigation, QC, and logging interfaces.
* Automate event recording and file verification.
* Standardize configuration templates across operations.
* Provide multi-role access with assist modes.
* Enable live mission progress and QC dashboards.
* Preserve asset, node, or sortie lifecycle state across deployment, recovery, ingest, and reporting.

---

## 6. Canonical Sources

* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* `Workshop_workflow_map-features-pain.xlsx`
* External references used for expanded operation types:
  * Kongsberg Discovery `HUGIN` / `HUGIN Edge`
  * PXGEO and TGS OBN material
  * Horizon Geosciences and similar ROV survey references
  * EIVA `ViperFish` and related ROTV references

---

**End of Document**
*"From task reality to design clarity - OIS's backbone begins with operator truth."*

### DOCUMENT END | UXR.03

### DOCUMENT START | UXR.04 | Pain Points and Opportunities

- kind: `doc_id`
- id: `UXR.04`
- title: `Pain Points and Opportunities`
- path: `01_UX_Research/UXR.04_Pain_Points_and_Opportunities.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `2156`

---
doc_id: UXR.04
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, pain-points, opportunities, ois]
---

# UXR.04 - Pain Points and Opportunities

<!--
Changes made:
1. Added standardized front-matter for repository uniformity.
2. Updated heading to clean ASCII formatting.
3. Added mission-state reconciliation and mixed sensor-control-model implications.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Consolidated Summary (Strategic Layer)

---

## 1. Purpose & Scope

This document consolidates pain points identified across research, workflow analyses, and workshops, translating them into **strategic opportunity areas** for the OI Survey (OIS).

It complements `01.03_Tasks_and_Tools_Matrix.md` by organizing findings into clusters that reflect operational stages and align with OIS's **core product pillars** - **Command & Control (C&C)**, **Active Monitoring (AM)**, **Online Log & Traceability**, and **Collaboration & Multi-Mission Enablement**.

---

## 2. Methodology & Sources

Derived from cross-analysis of:

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations - Task Structure`
* `Surveyor_Tasks.csv`
* Sensor catalog and usage summary

Pain points were categorized according to operational phase, user role, and system dependency. Opportunities were mapped based on feature alignment and design feasibility.

---

## 3. Pain Point Clusters by Operational Phase

| **Phase** | **Pain Points (Summary)** | **Root Causes** | **Opportunity Theme** |
| --- | --- | --- | --- |
| **Startup & Planning** | Network whitelisting delays; redundant configuration effort across sensors; manual setup of folder structures; unclear distinction between direct-control and dependency systems. | IT dependency; lack of automation; no standardized templates; uneven integration models. | **Configuration Automation & Access Readiness** - Predefined configuration templates, network pre-check routines, and clearer sensor/system classification. |
| **Mobilisation** | Manual calibration and validation (USBL, INS, MBES); missing integration visibility; poor handover between setup and operation. | Tool isolation; lack of diagnostic automation; weak dependency confidence signals. | **Automated Calibration & Health Checks** - Embedded diagnostic and status verification tools. |
| **Operation (Live)** | Fragmented tool landscape (8-12 active tools); repeated parameter checks across UIs; logging inconsistencies; no centralized alert system; mixed control models across sensors. | Legacy architecture; manual quality assurance; limited interoperability; inconsistent integration depth. | **Unified Operational Interface** - Single OIS workspace integrating control, monitoring, and logging with alert hierarchy and explicit system-state semantics. |
| **Recovery / Retrieval** | Deployed or autonomous assets require manual reconciliation of state, completeness, and exceptions. | Delayed-validation workflows; inventory tracking outside core operational tools. | **Mission-State Reconciliation** - Unified asset lifecycle tracking across deployment, recovery, ingest, and exception handling. |
| **Shift Handover** | Disconnected systems (OneNote, Online Log); inconsistent event documentation; reliance on memory and verbal briefings. | Lack of structured handover interface; no continuity of context. | **Integrated Handover & Traceability** - Shared session state, auto-log summaries, role-based access continuity. |
| **Reporting & Post-Processing** | Manual compilation of daily reports; folder validation; inconsistent metadata standards; late reconciliation for downloaded or self-logging devices. | Disparate data sources; lack of automation; delayed validation outside the main operational flow. | **Automated Reporting & Data Integrity Validation** - Auto-generated QC summaries, file traceability verification, and reconciliation outputs. |

---

## 4. Cross-Role Pain & Opportunity Mapping

| **Role** | **Primary Pain Points** | **Opportunity Direction (OIS Intervention)** |
| --- | --- | --- |
| **Surveyor (Operator)** | Manual data validation, repetitive UI switching, fragmented alarms, mixed control models. | Unified mission console combining control, QC, alerts, and explicit dependency visibility. |
| **Senior Surveyor** | No cross-mission visibility, repeated oversight of surveyor actions, weak clarity on integration depth by system. | Multi-mission supervisory view, configuration templates, and distinction between command, monitor, and review-only systems. |
| **PEC / Supervisor** | Manual mission progress tracking, downtime awareness, and weak confidence in deployed-asset completeness. | Mission Deck with live progress, completion %, downtime alerts, and recovery-state visibility. |
| **Data Manager** | Manual file structure and metadata validation; delayed reconciliation for downloaded assets. | Auto-log to file mapping, metadata compliance tools, and asset-ingest reconciliation. |
| **IT Support** | Ticket bottlenecks during mobilisation; inconsistent integration methods across devices. | Integrated diagnostic routines, network self-check tools, and clearer adapter/integration-state visibility. |

---

## 5. Opportunity Themes (Strategic Grouping)

| **Theme** | **Problem Addressed** | **Example OIS Features / Modules** |
| --- | --- | --- |
| **1. Configuration Automation & Control Safety** | Manual setup, inconsistent configuration, error-prone calibration | Configuration Templates, Configuration Lock, Rollback, Auto-Diagnostics |
| **2. Unified Operational Environment** | Multi-tool fragmentation, manual validation | Mission Deck, Command & Control Core, Multi-Sensor Dashboard |
| **3. Active Monitoring & Health Awareness** | Lack of real-time QC, no consistent alert hierarchy | Threshold Configuration, Health Indicators, Severity Alerts, Signal Flow Diagram |
| **4. Logging & Traceability Automation** | Manual log entry, duplication, poor continuity | Online Log Integration, Auto-Log Events, Log Consistency Checker |
| **5. Collaboration & Multi-User Accessibility** | Limited concurrent access, interference risk | Session Sharing, Assist Mode, Role-Based Permissions |
| **6. Reporting & Data Integrity Automation** | Manual reporting, metadata mismatches | File Monitor, Auto-QC Report, Changelog Journal |
| **7. Mission-State Reconciliation** | Deployed assets, downloaded sensors, and delayed validation create gaps across phases | Asset lifecycle tracker, ingest-state verification, node or sortie reconciliation views |
| **8. Sensor-Aware System Modeling** | Not all sensors are equivalent in control depth, coupling, or validation timing | Sensor taxonomy, dependency-aware readiness, coupled-system representation |

---

## 6. Pain Point Intensity Matrix (Prioritized by Impact)

| **Pain Area** | **Impact (Operational Downtime)** | **Frequency** | **Priority Level** |
| --- | --- | --- | --- |
| Tool Fragmentation | High | Constant | Critical |
| Manual Logging | High | Constant | Critical |
| Mission-State Reconciliation | High | Recurring in relevant operations | High |
| IT Access Delays | Medium | Frequent | High |
| Lack of QC Automation | Medium | Frequent | High |
| Poor Handover Traceability | Medium | Frequent | Moderate |
| Manual Reporting | Low | Common | Moderate |

---

## 7. Strategic Design Implications

1. **OIS as the single operational environment:** unify fragmented tool landscape into a cohesive workspace.
2. **Shift from reactive QC to proactive health monitoring:** embed diagnostics, auto-thresholds, and alerts.
3. **Enable operator efficiency scaling:** through automation, template-driven configuration, and multi-mission support.
4. **Institutionalize traceability:** every event, action, and change is auto-logged with role attribution.
5. **Reduce cognitive load:** use role-based visibility layers and simplified alert hierarchies.
6. **Model systems honestly:** distinguish between first-class controls, monitored dependencies, coupled subsystems, and delayed-validation assets.

---

## 8. Canonical Sources

* `01.03_Tasks_and_Tools_Matrix.md`
* `Workshop_workflow_map-features-pain.xlsx`
* `2.1.OI_SMP_Full_UX_Research.md`
* `2.3.OI_Operational_Workflows.md`
* `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary

---

**End of Document**
*"Every friction mapped is an opportunity for precision and simplification."*

### DOCUMENT END | UXR.04

### DOCUMENT START | UXR.05 | Role-Based Insights

- kind: `doc_id`
- id: `UXR.05`
- title: `Role-Based Insights`
- path: `01_UX_Research/UXR.05_Role-Based_Insights.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `2894`

---
doc_id: UXR.05
version: 0.2.0
last_updated: 2026-04-06
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, behavioral-insights, roles, ois]
---

# UXR.05 - Role-Based Insights

<!--
Changes made:
1. Added standardized metadata block.
2. Updated heading to clean ASCII formatting.
3. Added sensor-model implications from catalog and usage evidence.
-->

**Version:** 1.1  
**Date:** 2026-04-06  
**Owner:** OIS Research & Design  
**Status:** Draft (Synthesis Layer)

---

## 1. Purpose & Scope

This document summarizes key behavioral insights and operational tendencies per role within offshore and remote survey operations.
It translates observational data and workflow evidence into **design-relevant insights** for OIS, clarifying how each role interacts with systems, what they prioritize, and where their workflows break down.

Each role insight includes:

* **Core behavioral drivers**
* **Operational context and mental model**
* **Pain patterns**
* **System dependencies and limitations**
* **Design principles to support this role in OIS**

---

## 2. Methodology & Sources

Synthesized from:

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* Workshop feature prioritization lists
* Field interviews and onboard observations from `OI_SMP_Full_UX_Research.md`
* Task-level data from `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary as a grounding layer for sensor availability, coupling, and control-model differences

---

## 3. Surveyor (Operator)

### Behavioral Summary

The Surveyor is the **frontline operator** responsible for controlling sensors, maintaining data integrity, and logging operational events. Their focus is divided between monitoring live feeds, verifying recording states, and ensuring compliance with project parameters.

### Mental Model

> "Keep the line running and data clean."

Surveyors think in **timelines and thresholds**: time on line, line completion, green indicators, and immediate QC feedback. They prefer stable, visible systems over automation they cannot confirm.

### Pain Patterns

* Frequent context switching between 8-12 tools.
* "Green light fallacy": systems indicate logging success, but files are missing.
* Manual Online Log entries prone to gaps and inconsistency.
* Disjointed alarms and lack of unified health awareness.
* Additional cognitive load when some devices are controllable, some are read-only dependencies, and others validate only after recovery or download.

### Sensor-Model Implications

For operators, the distinction between sensor types matters behaviorally:

* **Primary acquisition sensors** such as MBES, SSS, and SBP tend to anchor the live work surface.
* **Dependency systems** such as INS, GNSS, USBL, and Time Sync drive trust in the acquisition state even when they are not the main screen focus.
* **Coupled systems** such as DVL tied to a navigation unit should often be understood through parent-system readiness rather than as isolated devices.
* **Delayed-validation devices** such as self-logging or downloaded-at-end systems create uncertainty that persists beyond the live watch.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Clarity first, not complexity** | Unified dashboard with one status layer per sensor family and explicit dependency visibility. |
| **Confidence through feedback** | Real-time "recording verified" indicators linked to file system or ingest checks. |
| **Frictionless action** | One-click controls for start/stop, restart, or switch mission where direct control is actually supported. |
| **Low cognitive load** | Role-optimized layout with consistent distinction between commandable systems, monitored dependencies, and delayed-validation assets. |

---

## 4. Senior Surveyor

### Behavioral Summary

The Senior Surveyor ensures quality, oversees configuration, and supervises operators. Their attention spans across **multiple missions or sensors**, jumping between supervisory review, calibration, and problem-solving.

### Mental Model

> "Trust but verify."

They see themselves as system guardians - maintaining correctness and ensuring junior operators do not misconfigure or miss data.

### Pain Patterns

* No aggregated view of multiple missions.
* Manual MAC and QC reports.
* Time lost verifying settings across UIs.
* No ability to isolate and assist remotely without interrupting the operator.
* Additional burden when integration depth varies by sensor and some systems expose only partial control or indirect state.

### Sensor-Model Implications

For senior surveyors, sensor diversity creates a governance problem as much as a UI problem:

* They need to know which systems are **first-class control surfaces** versus which are **monitored through other software**.
* They need confidence that **coupled systems** are not being reviewed twice through mismatched abstractions.
* They need workflows for **late validation** where data confidence is established after recovery, download, or reconciliation rather than at acquisition time.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Supervisor situational awareness** | Multi-mission view with color-coded health states and dependency confidence. |
| **Guided oversight** | Auto-flag deviations for rapid triage, especially where integration depth or delayed validation increases uncertainty. |
| **Role-protected control** | Read/write access by mission and sensor scope, with clear distinction between command, monitor, and review-only objects. |
| **Assistance without interference** | Remote assist mode with observation-only or controlled handover. |

---

## 5. Project Execution Coordinator (PEC / Supervisor)

### Behavioral Summary

The PEC is responsible for operational efficiency, coordination, and compliance with permit timelines. They think in terms of mission throughput, resource allocation, and downtime avoidance.

### Mental Model

> "Stay on schedule, keep everyone busy."

They operate at a **macro level**, assessing mission readiness and completion metrics rather than individual sensor details.

### Pain Patterns

* Limited visibility into progress and downtime per mission.
* Manual vessel reallocation based on verbal updates.
* Fragmented communication with data teams.
* Difficulty interpreting the operational impact of deployed assets or delayed-validation systems on schedule confidence.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Operational overview at a glance** | Mission Deck showing mission %, vessel status, deployed asset state, and downtime. |
| **Predictive awareness** | Alerts for time limits, weather, permit expirations, and unresolved recovery or ingest obligations. |
| **Cross-team synchronization** | Integration between operations and data QC logs. |
| **Minimal distraction** | Abstracted data view, focused on milestones, not raw telemetry. |

---

## 6. Data Manager / Survey Advisor

### Behavioral Summary

The Data Manager ensures post-operation quality, traceability, and compliance. They are focused on **data lineage** - verifying that every recorded event matches specifications and naming conventions.

### Mental Model

> "If it is not traceable, it is not valid."

They rely heavily on logs, folder structures, and reports, often performing redundant cross-checks due to poor automation.

### Pain Patterns

* Manual verification of Online Log vs actual files.
* Non-standardized metadata and file naming.
* Time-intensive QC report generation.
* Extra reconciliation effort for node inventories, downloaded sensors, sortie ingest, and systems whose final validity is only known after recovery.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **End-to-end traceability** | Auto-linked Online Log -> File Mapping and ingest status. |
| **Data integrity visibility** | File Monitor with completeness scoring and explicit delayed-validation states. |
| **Automation over inspection** | Auto-generated daily/QC reports and reconciliation outputs for nodes, sorties, and uploaded datasets. |
| **Historical context** | Version history and changelog for configuration and events. |

---

## 7. IT / Network Support

### Behavioral Summary

IT supports secure access and network connectivity. Their operational pain comes from firefighting - often handling reactive tickets due to poor pre-check capabilities in the field.

### Mental Model

> "Keep data flowing and ports open."

### Pain Patterns

* Mobilisation delays due to access tickets.
* No visibility into sensor network status.
* Limited diagnostic tools for remote users.
* Additional complexity where integration methods differ by device, including APIs, ASCII command paths, vendor software dependencies, and coupled systems hidden behind parent devices.

### OIS Design Implications

| Design Principle | Implementation Example |
| --- | --- |
| **Preventive transparency** | Built-in network self-test and status dashboard. |
| **Empower operators** | Diagnostic shortcuts to reduce ticket load. |
| **Traceable changes** | Configuration change log visible to IT. |
| **Fail-safe defaults** | Auto-alert if whitelisting, ports, or integration adapters fail before mobilisation. |

---

## 8. Behavioral Patterns Across Roles

| **Dimension** | **Shared Behavior** | **Design Consideration** |
| --- | --- | --- |
| **Reliance on manual verification** | All roles distrust automation without transparency. | Provide verifiable system feedback such as "verified logging" or explicit ingest confirmation. |
| **Need for situational awareness** | Surveyor -> Senior -> PEC require tiered awareness levels. | Design modular visibility layers by role. |
| **Parallel workflows** | Multiple missions and systems managed concurrently. | Multi-mission workspaces and alert prioritization. |
| **Dependence on shared logs** | Collaboration hinges on event traceability. | Centralized Online Log with structured event types. |
| **Cognitive fatigue from tool overload** | Especially for operators and seniors. | Streamline interfaces and use persistent layouts. |
| **Mixed control models** | Teams work across commandable, coupled, monitored-only, and delayed-validation systems. | Make the sensor/system type explicit so users know what OIS can control, verify, or only observe. |

---

## 9. Summary of Role-Driven Design Principles

1. **Build confidence through feedback** - Show what is happening and why.
2. **Design for mental models** - Reflect how users think: by line, mission, state, and confidence level.
3. **Support supervision without interruption** - Allow assistance without loss of control.
4. **Encourage consistency through structure** - Use templates and auto-checks to enforce standardization.
5. **Scale through modularity** - Support multiple missions, roles, and devices seamlessly.
6. **Respect sensor-model differences** - Distinguish between first-class controls, dependencies, coupled subsystems, and delayed-ingest assets.

---

## 10. Canonical Sources

* `01.01_Roles_and_Responsibilities.md`
* `01.03_Tasks_and_Tools_Matrix.md`
* `01.04_Pain_Points_and_Opportunities.md`
* `2.1.OI_SMP_Full_UX_Research.md`
* `Underwater Survey Operations - Task Structure`
* Sensor catalog and usage summary

---

**End of Document**
*"Every role sees the system differently - OIS must make those views align without friction."*

### DOCUMENT END | UXR.05

### DOCUMENT START | UXR.06 | Context of Use and Environment

- kind: `doc_id`
- id: `UXR.06`
- title: `Context of Use and Environment`
- path: `01_UX_Research/UXR.06_Context_of_Use_and_Environment.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `2106`

---
doc_id: UXR.06
version: 0.1.0
last_updated: 2025-11-09
status: draft
owners: [pedro.baptista@oceaninfinity.com]
tags: [ux-research, context-of-use, environment, ois]
---

# UXR.06 – Context of Use and Environment

<!--
Changes made:
1. Added standardized front-matter for repository alignment.
2. Corrected minor typo (“---singe”).
3. Updated H1 to standard format.
4. Content unchanged.
-->

**Version:** 1.0  
**Date:** 2025-10-25  
**Owner:** OIS Research & Design  
**Status:** Complete (Operational Environment Overview)

---

## 1. Purpose & Scope

This document defines the **context of use** for the OI Survey (OIS) — the physical, technical, and cognitive environment in which offshore and remote survey operations occur.

It describes constraints, environmental conditions, and collaboration patterns that directly influence the platform’s design decisions.

The goal is to ensure OIS is built with an **accurate understanding of user conditions**, enabling effective, resilient, and safe operations both offshore and onshore.

---

## 2. Methodology & Sources

Synthesized from field observations, interviews, and documentation, including:

* `2.2.Survey current state Deck.md`
* `2.3.OI_Operational_Workflows.md`
* `2.3.1.OperationTypesWorkflows.md`
* `DLog_241025_smp_direction_update.md`
* `Underwater Survey Operations – Task Structure`

Cross-validated with operational feedback from online and offshore teams between 2023–2025.

---

## 3. Operational Environments

### 3.1 Offshore Control Room

* **Setup:** Typically 6–8 screens per operator, distributed across multiple systems (navigation, sensor monitoring, ROV video, logging, communication).  
* **Lighting & Conditions:** Dimmed environment with limited natural light, requiring strong visual contrast and low-glare interfaces.  
* **Noise & Vibration:** Constant low-frequency background noise from vessel machinery; communication via headsets and intercom.  
* **Workload Characteristics:** Long shifts (12-hour rotations), alternating focus between active control and passive monitoring.  
* **Cognitive Constraints:** High mental load due to multi-system vigilance and alarm fatigue.

### 3.2 Remote Operations Centre (ROC)

* **Setup:** 8 screens per surveyor (typically), higher bandwidth reliability, and better ergonomic setup.  
* **Role Distribution:** One senior may supervise multiple missions concurrently.  
* **Collaboration Mode:** Real-time remote assistance via chat/video overlay, shared mission dashboards.  
* **Challenge:** Latency in command feedback or data visualization may cause delayed responses during troubleshooting.

### 3.3 Vessel Deck & Equipment Zone

* **Setup:** Mobile tablets or terminals used for calibration and deck activity coordination.  
* **Environmental Factors:** Wet, cold, or variable light conditions; gloves, movement, and PPE affect usability.  
* **Design Relevance:** Mobile or touchscreen interfaces must use large targets, minimal text input, and offline cache capabilities.

---

## 4. Human and Organizational Context

| **Aspect**                  | **Description**                                                 | **OIS Design Consideration**                                  |
| --------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------- |
| **Shift Patterns**          | 12-hour rotations; frequent handovers with in-person briefings. | Persistent logs and handover snapshots.                       |
| **Roles per Mission**       | 1–2 Surveyors, 1 Senior, 1 PEC (shared across missions).        | Multi-user concurrent sessions with hierarchical permissions. |
| **Communication Channels**  | Intercom, OneNote, Online Log, chat apps.                       | Integrate key notes and events into central OIS log.          |
| **Error Tolerance**         | High operational consequence for data loss or misalignment.     | Require confirmations, rollback, and visible action trails.   |
| **Collaboration Pattern**   | Supervisor assists operators without taking control.            | Observation and assist mode design.                           |
| **Attention Distribution**  | 70% monitoring, 30% control action.                             | Prioritize visibility and early-warning systems.              |
| **Fatigue & Handover Risk** | High risk of detail loss at shift changes.                      | Standardized event templates and context snapshots.           |

---

## 5. Technical Environment

| **Domain**                | **Details / Constraints**                                                                   | **Design Implication**                                           |
| ------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Network**               | Variable reliability; offshore vessels experience intermittent latency (100–300ms typical). | Resilient UI updates; auto-reconnect for sensor feeds.           |
| **Data Volume**           | High-volume streams (video, sonar, navigation).                                             | Progressive loading and adaptive compression.                    |
| **Hardware Diversity**    | Mix of ruggedized PCs, laptops, and workstations with varying GPU/CPU capacity.             | Modular UI with dynamic scaling.                                 |
| **Integration Landscape** | Proprietary hardware (EIVA, SIS, QINSy, VOYIS, APOS).                                       | Develop middleware or API gateways for data harmonization.       |
| **Logging Systems**       | Local folder structures (“Red Network”), shared drives, Online Log.                         | Integrate logging verification and automated consistency checks. |

---

## 6. Cognitive and Interaction Context

| **Dimension**           | **Observed Behavior / Condition**                                                       | **Design Principle**                                              |
| ----------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Attention Span**      | Operators maintain multiple parallel attention threads (sensor, navigation, ROV, logs). | Reduce alarm noise; surface priority alerts only.                 |
| **Trust in Automation** | Users rely on visual confirmation, not automated validation.                            | Make automation visible and verifiable (“verified by system”).    |
| **System Navigation**   | Users prefer persistent screen layouts and minimal context switching.                   | Fixed panel layout, non-modal workflows.                          |
| **Error Recovery**      | Users fear irreversible actions.                                                        | Undo/rollback and confirmation dialogues on all critical actions. |
| **Learning Curve**      | Operators vary in experience across vessels and project types.                          | Use progressive disclosure and standardized templates.            |
| **Collaboration Style** | Real-time verbal communication remains dominant.                                        | OIS notifications should mirror verbal status cues.               |

---

## 7. Design Implications Summary

1. **Design for visibility and feedback** – users must always see what is happening and why.  
2. **Resilient interaction model** – platform must sustain partial data loss or temporary disconnections.  
3. **Standardize across contexts** – interfaces should look and behave consistently across offshore and remote settings.  
4. **Minimize manual data handling** – reduce folder management and manual log entry.  
5. **Integrate human rhythms** – support shift transitions and fatigue mitigation through structured overviews.  
6. **Accessible and ergonomic** – support both mouse/keyboard and touch under varying lighting and motion conditions.  

---

## 8. Canonical Sources

* `2.2.Survey current state Deck.md`
* `2.3.OI_Operational_Workflows.md`
* `DLog_241025_smp_direction_update.md`
* `Underwater Survey Operations – Task Structure`

---

**End of Document**  
*“Designing for the environment means designing for resilience, clarity, and control.”*

### DOCUMENT END | UXR.06

### DOCUMENT START | UXR.07 | Sensor Taxonomy

- kind: `doc_id`
- id: `UXR.07`
- title: `Sensor Taxonomy`
- path: `01_UX_Research/UXR.07_Sensor_Taxonomy.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `2545`

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

### DOCUMENT END | UXR.07

### DOCUMENT START | UXR.08 | Senior Surveyor Workshop Feature Themes

- kind: `doc_id`
- id: `UXR.08`
- title: `Senior Surveyor Workshop Feature Themes`
- path: `01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md`
- section_id: `01UX`
- section_title: `UX Research`
- canonical_role: `canonical_doc`
- estimated_tokens: `3224`

---
doc_id: UXR.08
title: Senior Surveyor Workshop Feature Themes
version: 0.1.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
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

### DOCUMENT END | UXR.08

## SECTION END | 01UX

## SECTION START | 02PD | Product Design

- section_id: `02PD`
- title: `Product Design`
- base_path: `02_Product_Design`
- tags: [design, architecture, ux, operations]
- document_count: `13`

### DOCUMENT START | PDD.00 | Design Principles and Documentation Model

- kind: `doc_id`
- id: `PDD.00`
- title: `Design Principles and Documentation Model`
- path: `02_Product_Design/PDD.00_Design_Principles_and_Documentation_Model.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1231`

---
doc_id: PDD.00
title: Design Principles and Documentation Model
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "principles", "documentation", "survey-operations"]
created: 2025-11-08
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.00_Design_Principles_and_Documentation_Model.md
  - rel: related
    href: 00_Product_Foundation/PFD.01_Product_Vision.md
  - rel: related
    href: 01_UX_Research/UXR.06_Context_of_Use_and_Environment.md
---

# PDD.00 - Design Principles and Documentation Model

## Purpose
This document defines the design principles that should shape OI Survey as a remote survey operations product. It also explains how the Product Design documentation is structured so that humans and AI agents can distinguish between stable product truth, evolving concepts, and future-facing bets.

## Surveyor-Centered Design Principles

| Principle | Meaning for OI Survey | Design Implication |
| --- | --- | --- |
| **Attention is a limited resource** | A surveyor cannot actively inspect every mission, sensor, and supporting system at the same time. | The product must help operators recognize where attention is required and what can be safely deprioritized. |
| **Evidence must support intervention** | Operators need to understand why a system appears degraded before acting. | Control surfaces and evidence surfaces must work together rather than compete for attention. |
| **Operational consequences must be legible** | A change in power, configuration, environment, or dependency can invalidate data or interrupt operations. | The UI must make downstream impact, readiness, and confidence visible before and after action. |
| **Traceability is part of the workflow** | Remote survey operations rely on defensible records for handover, reporting, billing, and compliance. | Logging and event capture are not optional support features; they are part of the operating model. |
| **Configuration truth must be trustworthy** | Surveyors need confidence that staged setup, active runtime behavior, and observed evidence remain aligned. | The product must separate staged changes from live operational state and expose validation clearly. |
| **Multiple screens are a context, not the product model** | Survey desks will likely remain multi-screen, but the exact arrangement can evolve. | The design should support multi-screen operations without hardcoding one workstation layout as the product truth. |
| **Specialized workflows belong in the ecosystem** | Functions like SVP management are operationally central even when they remain specialized. | The design model must allow dedicated subsystems such as Hydrosens to remain first-class parts of the experience. |

## Documentation Model
The Product Design documentation is intentionally layered.

### Core
Stable product concepts that should shape decision-making now.

### Core / Evolving
Important concepts whose role is clear but whose exact interaction model or product boundary is still being refined.

### Specialized / Active
Operational subsystems and services that are active parts of the survey experience, even if they are not part of the central mission-time workspace.

### Draft / Emerging
Concepts or directions that should be preserved without being treated as final product truth.

## How To Read This Section
- Use `PDD.01` for the overall OI Survey topology.
- Use `PDD.02` for the operational information model.
- Use `PDD.03` for shared interaction rules across surfaces.
- Use `PDD.04.*` for concrete surfaces, services, and subsystems.
- Use `PDD.05` and `PDD.06` when clarifying state, authority, and operational ownership.
- Use `PDD.07` for unresolved or future-facing concepts.

## Scope of Product Design Truth
This section is not intended to mirror the current prototype one-to-one. Instead, it should:
- preserve durable product concepts
- absorb lessons from prototyping
- capture known external dependencies such as Qinsy navigation context
- distinguish active product surfaces from emerging concepts
- remain grounded in remote survey operations and surveyor needs

## Writing Rules For This Section
- Start from the surveyor's task or question before describing UI structure.
- Separate current product direction from speculative future direction.
- Prefer operational language over abstract software language.
- Keep headings stable and retrieval-friendly for AI agents.
- Treat the product as an ecosystem of core workspace, specialized subsystems, and shared services.

## Summary Statement
> OI Survey should be documented as a surveyor-centered operating ecosystem: one that helps distributed teams maintain awareness, intervene safely, trust configuration and environmental truth, and preserve a defensible operational narrative across missions.

### DOCUMENT END | PDD.00

### DOCUMENT START | PDD.01 | OI Survey Product Topology

- kind: `doc_id`
- id: `PDD.01`
- title: `OI Survey Product Topology`
- path: `02_Product_Design/PDD.01_OIS_Product_Topology.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1739`

---
doc_id: PDD.01
title: OI Survey Product Topology
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "topology", "product-model", "survey-operations"]
created: 2025-11-08
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
---

# PDD.01 - OI Survey Product Topology

## Purpose
This document describes the OI Survey product ecosystem and the relationship between its core surfaces, specialized subsystems, and shared services.

## Topology Overview
OI Survey is not one screen or one flat application shell. It is a **unified operational ecosystem** composed of mission-time surfaces, evidence and QC capabilities, shared services, and specialist subsystems that together support remote survey work.

| Product Element | Type | Primary Role |
| --- | --- | --- |
| **Mission Deck** | Core mission-time container | The active mission package that coordinates the primary mission-time surfaces. |
| **Mission Overview** | Core surface | Default decision surface for active mission posture, issue state, and next attention target. |
| **Systems** | Core surface | Deep operational and control surface for selected-system understanding, intervention, and recovery. |
| **Data Monitor** | Core / Evolving surface family | Package-level evidence and QC capability family, including stream-oriented and detached evidence views. |
| **Multi-Mission Context** | Core / Evolving surface | Cross-mission awareness, prioritization, and safe attention management. |
| **Online Log** | Shared service | Structured operational traceability, event capture, annotation, and reporting backbone. |
| **Hydrosens** | Specialized / Active subsystem | Specialized environmental readiness subsystem for SVP acquisition, QC, preparation, approval, and downstream distribution. |
| **Qinsy Navigation Context** | External operational dependency | Navigation view and infrastructure dependency used during survey execution. |

## Product Layers

### Mission-Time Package
The core mission-time package should help a surveyor answer:
- What is happening in the active mission right now?
- What needs attention now?
- Which system or dependency is causing concern?
- What action is safe to take now?

Mission Deck is the container for that mission-time package. Within it:
- **Mission Overview** is the primary decision surface.
- **Systems** is the deep operational and control surface.

### Evidence and QC Capability
Evidence interpretation should not be flattened into the same surface that owns all control.  
**Data Monitor** is the package-level name for the evidence and QC capability family. It can include stream viewers, QC-focused surfaces, and detached evidence views that remain mission-aware without overloading Mission Deck.

### Cross-Mission Awareness
**Multi-Mission Context** remains a core concept for broader awareness and prioritization across assigned missions. It should develop in parallel to the active mission package, using a subset of the most important mission-level signals rather than replacing the active mission model.

### Specialized Operational Subsystems
Some workflows remain deep, domain-specific, and operationally central. Hydrosens is the clearest current example. These workflows should remain connected to the OI Survey experience without being flattened into generic controls.

Hydrosens should be treated specifically as:
- a specialized environmental readiness subsystem
- not a generic `Systems` pane
- not merely an evidence-monitoring surface under `Data Monitor`
- a workflow that supports acquisition, review, preparation, approval, export, and distribution of environmental profile truth

### Shared Services
Online Log is not merely a panel. It is the traceability service that binds together automated events, user actions, manual annotations, and downstream reporting. Similar shared services may grow around state synchronization, configuration governance, and analytics.

### External Dependencies
Not every operationally essential function needs to be absorbed into OI Survey UI scope immediately. Qinsy remains a major navigation and infrastructure dependency and should be documented as such.

## Operational Relationships

| From | To | Relationship |
| --- | --- | --- |
| **Mission Overview** | **Systems** | Escalates from summary posture and issue recognition to deeper operational action. |
| **Mission Deck** | **Mission Overview / Systems** | Coordinates the active mission package without collapsing both surfaces into one flat workspace. |
| **Mission Deck** | **Data Monitor** | Launches or coordinates deeper evidence and QC review when interpretation should detach from control. |
| **Mission Deck** | **Online Log** | Produces mission-time actions, system events, and operator notes that become part of the mission narrative. |
| **Multi-Mission Context** | **Mission Deck** | Selects or shifts mission focus to an active mission package. |
| **Hydrosens** | **Mission Deck** | Supplies environmental readiness truth that affects mission confidence without collapsing the full SVP workflow into Mission Deck. |
| **Hydrosens** | **Online Log** | Produces traceable events for acquisition, QC, approval, export, and distribution. |
| **Qinsy** | **Mission Deck / survey operation** | Provides navigation context and infrastructure integration that remain operationally essential even when external. |

## Current Product Direction
- The current prototype already shows `Mission Overview` as the default overview surface inside Mission Deck.
- The current prototype already expresses `Systems` as the explicit deep operational workspace.
- Online Log is an active product/service, not only a future concept.
- Data Monitor should be treated as the package-level evidence/QC direction, even where implementation still appears through stream windows and detached evidence patterns rather than one consolidated module.
- Multi-Mission Context remains strategically important and should continue evolving in parallel with mission-level surfaces rather than being treated as a distant later-stage capability.
- Hydrosens should remain a specialized subsystem whose workflow is surfaced into mission-time experience through environmental readiness and system dependency meaning rather than through generic system ownership.

## Summary Statement
> OI Survey should be understood as a layered operational ecosystem: a mission-time container built around Mission Overview and Systems, supported by Data Monitor capabilities, shared traceability services, specialist subsystems, and explicit external dependencies that remain part of the surveyor's working reality.

### DOCUMENT END | PDD.01

### DOCUMENT START | PDD.02 | Operational Information Model

- kind: `doc_id`
- id: `PDD.02`
- title: `Operational Information Model`
- path: `02_Product_Design/PDD.02_Operational_Information_Model.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1102`

---
doc_id: PDD.02
title: Operational Information Model
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "information-model", "operations", "traceability"]
created: 2025-11-08
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.02_Operational_Information_Model.md
  - rel: related
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
  - rel: related
    href: 01_UX_Research/UXR.07_Sensor_Taxonomy.md
---

# PDD.02 - Operational Information Model

## Purpose
This document defines the product-level information model that should underpin OI Survey. It focuses on operational truth rather than software schema.

## Core Operational Objects

| Object | Meaning | Why It Matters |
| --- | --- | --- |
| **Mission** | The unit of operational intent and execution. | Organizes work, attention, traceability, and authority. |
| **Operational System** | A survey-relevant system inside a mission, including sensors, infrastructure, and supporting systems. | Lets the surveyor reason about availability, readiness, impact, and evidence. |
| **Subsystem** | A specialized capability or workflow that supports mission success but may not live inside the central workspace at all times. | Supports deep workflows such as environmental profile management. |
| **Evidence Stream** | Any live or near-live evidence source used for interpretation. | Supports QC, trust, anomaly detection, and intervention confidence. |
| **Configuration State** | The currently applied and/or staged operational setup for a mission or system. | Determines whether the observed behavior can be trusted as survey-ready. |
| **Environmental Profile** | A validated SVP or related environmental profile used to support survey accuracy. | Critical to survey quality, environmental readiness, and downstream system confidence. |
| **Alert** | A surfaced operational condition that requires awareness, validation, or action. | Helps the surveyor prioritize attention. |
| **Trace Event** | A timestamped record of a system event, user action, or manual note. | Enables handover, accountability, and reporting. |
| **Downstream Consumer** | Any system, workflow, or deliverable that depends on a system or profile remaining valid. | Makes operational consequences explicit. |

## Relationship Model
- A mission contains many operational systems and many trace events.
- A system may publish one or more evidence streams.
- A system may depend on one or more upstream inputs and may have downstream consumers.
- Configuration state may exist at mission level, system level, or subsystem level.
- Environmental profiles may influence the confidence or readiness of multiple systems.
- Alerts are tied to missions, systems, profiles, or evidence conditions.
- Trace events can be generated automatically or manually and should remain linkable to their origin.

## Information Questions The Product Must Answer

| Surveyor Question | Required Information |
| --- | --- |
| **What needs attention now?** | Mission posture, alerts, degraded systems, recent operational changes. |
| **Can I trust this system?** | Availability, readiness, dependencies, last known evidence, and recent interventions. |
| **What changed?** | Trace events, state changes, applied configuration, profile updates, and manual notes. |
| **What happens if I act?** | Downstream consumers, impact, lock state, and system relationships. |
| **Is the environment still survey-ready?** | Profile age, validation status, source provenance, export/distribution status. |

## Operational Modeling Rules
- Do not flatten all systems into one generic sensor concept.
- Represent control-oriented systems differently from measurement-oriented systems when their operator meaning differs.
- Treat environmental profile truth as a first-class operational object.
- Keep traceability connected to operational meaning, not only to technical events.
- Model external dependencies such as Qinsy explicitly when the surveyor relies on them to understand mission state.

## Summary Statement
> OI Survey should organize information around the operational truths a surveyor must trust: mission state, system state, evidence, configuration, environmental validity, downstream impact, and traceable events.

### DOCUMENT END | PDD.02

### DOCUMENT START | PDD.03 | Interaction Framework and Surface Grammar

- kind: `doc_id`
- id: `PDD.03`
- title: `Interaction Framework and Surface Grammar`
- path: `02_Product_Design/PDD.03_Interaction_Framework_and_Surface_Grammar.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `979`

---
doc_id: PDD.03
title: Interaction Framework and Surface Grammar
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "interaction", "ux", "surfaces"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.03_Interaction_Framework_and_Surface_Grammar.md
  - rel: related
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
---

# PDD.03 - Interaction Framework and Surface Grammar

## Purpose
This document defines the shared interaction rules that should make OI Survey feel coherent across cross-mission surfaces, mission-context surfaces, detached evidence surfaces, specialized subsystems, and shared services.

## Surface Families

| Surface Family | Role | Typical User Question |
| --- | --- | --- |
| **Cross-Mission Surfaces** | Help the surveyor prioritize attention across assigned work. | Which mission needs me now? |
| **Mission-Context Surfaces** | Support active mission supervision and intervention. | What is happening in this mission, and what is safe to do? |
| **Detached Evidence Surfaces** | Support deeper inspection, comparison, or extended watching. | What does the evidence actually show? |
| **Specialized Operational Subsystems** | Handle deep domain workflows that require their own focused model. | Is this environmental or specialist workflow valid and ready? |
| **Shared Services** | Capture or distribute cross-cutting operational truth. | What happened, who acted, and what record remains? |

## Shared Interaction Rules
- Cross-mission surfaces should summarize and prioritize, not overwhelm with raw telemetry.
- Mission-context surfaces should help operators connect state, evidence, and intervention.
- Detached evidence surfaces should privilege interpretation over broad command density.
- Shared services should remain linked to mission and system context without requiring users to reconstruct the narrative manually.
- Specialized subsystems should feel connected to OI Survey even when they maintain distinct workflows.

## Context Propagation
OI Survey should treat mission context as a first-class interaction contract.

### Rules
- The surveyor should always know which mission is currently active.
- Cross-mission surfaces should remain global.
- Mission-context surfaces should update coherently when active mission focus changes.
- Detached evidence should be able to remain mission-bound even when it is moved or opened elsewhere.
- Traceability should preserve mission linkage even when actions originate in specialized subsystems.

## Control And Evidence Relationship
The product should not force all evidence into the same surface that owns control.

### Design intent
- Keep mission-time intervention close to the evidence needed for confidence.
- Allow evidence to detach when deep inspection or monitoring would otherwise overload the main control surface.
- Make downstream impact legible before and after action.
- Preserve a stable surveyor mental model even when specialized subsystems are involved.

## Multi-Screen Guidance
Multi-screen operations remain an expected context for survey desks. However, the product should not depend on a single fixed screen map.

### Implications
- Surfaces should support multiple-screen arrangements.
- The same product model should also tolerate reduced-screen or iterative deployment contexts.
- Qinsy navigation visibility remains operationally important and should be treated as part of the working environment.

## Summary Statement
> OI Survey should behave as one coherent operating ecosystem, even when awareness, intervention, evidence, environmental workflows, and traceability are distributed across different surfaces and tools.

### DOCUMENT END | PDD.03

### DOCUMENT START | PDD.04.01 | Multi-Mission Context

- kind: `doc_id`
- id: `PDD.04.01`
- title: `Multi-Mission Context`
- path: `02_Product_Design/PDD.04.01_Multi-Mission_Context.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1040`

---
doc_id: PDD.04.01
title: Multi-Mission Context
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "multi-mission", "awareness", "prioritization"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.01 - Multi-Mission Context

## Maturity
**Core**

## Purpose
Multi-Mission Context is the cross-mission awareness surface for OI Survey. It gives surveyors a real-time view of the missions assigned to them and helps them decide where to focus attention.

## Surveyor Need
A surveyor may be responsible for more than one mission or operational thread. They need a way to:
- understand overall mission posture quickly
- spot which mission is degrading
- shift focus without losing orientation
- maintain safe workload awareness across assigned work

## Operational Role
This surface is not for detailed system control. Its role is to support:
- prioritization
- focus switching
- mission posture recognition
- escalation awareness
- safe multi-mission operations where validated

It should be treated as a **parallel cross-mission surface**, not the default primary operating surface for mission-time work. The active mission package should still center on Mission Deck and its internal mission-time surfaces, while Multi-Mission Context progressively combines the most important mission-level signals across several missions.

## Information To Show

| Information | Why It Matters |
| --- | --- |
| **Mission identity and assignment** | Confirms what is under the surveyor's responsibility. |
| **Mission posture** | Shows whether the mission is nominal, degraded, waiting, or at risk. |
| **Recent critical changes** | Helps the surveyor understand why attention is needed now. |
| **Unread or unresolved operational issues** | Prevents hidden problems from being lost in mission switching. |
| **Readiness and confidence summaries** | Supports fast judgment without opening every mission. |
| **Time relevance** | Indicates how fresh the displayed understanding is. |

## Interaction Expectations
- Selecting a mission should shift active operational focus coherently.
- Mission switching should be fast and deliberate, not friction-heavy.
- The active mission should remain clearly indicated.
- The surface should help a surveyor understand relative urgency across missions.
- The surface should not try to replace the detailed evidence and action model of Mission Deck.

## Relationship To Other Surfaces
- **Mission Deck**: active mission-time workspace once focus is selected.
- **Online Log**: supports cross-mission awareness of what changed.
- **Detached Evidence Surfaces**: may remain open for a mission even when the surveyor is reviewing another mission at summary level.

## Current Direction
The former `Triage Hub` concept is now more accurately expressed as Multi-Mission Context. The concept remains core, but the exact UI treatment can evolve.

Current product direction keeps Multi-Mission Context on a parallel track: strategically important and being developed alongside mission-level surfaces, not deferred until those surfaces are "finished."

## Research Implications
The senior surveyor workshop reinforces that cross-mission context is not only a convenience layer. It is needed to:
- compare relative mission posture quickly
- recognize which mission needs attention now
- keep mission progress, spatial context, and recent critical change visible enough to support safe focus shifting

This evidence strengthens the role of Multi-Mission Context as an attention-management surface rather than a generic dashboard.

## Summary Statement
> Multi-Mission Context should help surveyors manage attention safely across missions by showing which mission matters now, why it matters, and how focus can shift without losing situational understanding.

### DOCUMENT END | PDD.04.01

### DOCUMENT START | PDD.04.02 | Mission Deck

- kind: `doc_id`
- id: `PDD.04.02`
- title: `Mission Deck`
- path: `02_Product_Design/PDD.04.02_Mission_Deck.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1737`

---
doc_id: PDD.04.02
title: Mission Deck
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "mission-deck", "operations", "intervention"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.02 - Mission Deck

## Maturity
**Core**

## Purpose
Mission Deck is the primary mission-time container in OI Survey. It should hold together the active mission package while keeping different operational questions in the right internal surfaces rather than collapsing everything into one flat cockpit.

## Surveyor Need
During live operations the surveyor needs one dependable mission-time package to answer:
- What is happening in this mission right now?
- What needs attention now?
- Which system or dependency is causing concern?
- What action is safe to take now?
- What evidence supports or challenges my understanding?
- What should be recorded for the next person or downstream process?

## Operational Role
Mission Deck should coordinate:
- mission posture and issue awareness
- selected-system understanding
- intervention and recovery actions
- readiness and dependency awareness
- movement to deeper evidence, traceability, or specialist workflows
- traceable mission-time action

## Core Experience Model

Mission Deck should be understood as a mission-time container composed primarily of two internal surfaces:

| Area | Purpose |
| --- | --- |
| **Mission Overview** | The default decision surface for active mission posture, issue recognition, and next attention target. |
| **Systems** | The deep operational and control surface for selected-system action, recovery, configuration, and dependency understanding. |

This means Mission Deck should support movement from overview to deeper operational action without forcing all mission-time work into one undifferentiated screen.

## Internal Surface Roles

### Mission Overview
Mission Overview should:
- establish active mission context
- summarize posture, state, and confidence
- highlight issues, attention, and next likely action
- help the surveyor decide whether deeper system action is needed

### Environmental Readiness
Mission Overview should also be the primary place where **environmental readiness** is surfaced at mission level.

This should include, where relevant:
- current active profile age / freshness
- trust state or validity of the currently relevant environmental profile
- whether a newer cast is pending review
- whether an approved profile has been distributed or applied to affected systems
- mission consequence when profile truth is stale, missing, or questioned
- a clear path to `Open Hydrosens`

### Systems
Systems should:
- focus the surveyor on the currently relevant operational system
- support intervention and recovery
- expose consequence, dependency, and readiness meaning clearly
- support system-specific variation while still feeling like one product

For affected acoustic systems, `Systems` should:
- show `SVP` as a dependency and readiness factor
- show applied profile status where operationally meaningful
- explain the consequence of stale, missing, or questioned environmental profile truth
- provide a deep link into `Hydrosens`

`Systems` should not absorb the full Hydrosens workflow. It should express dependency meaning, not subsystem ownership.

## Relationship To Other Product Elements
- **Multi-Mission Context** chooses or shifts mission focus at cross-mission level and should progressively reflect the most important mission-level signals that Mission Overview helps define.
- **Data Monitor / Detached Evidence Surfaces** support deeper evidence review when interpretation should detach from the main mission-time surfaces.
- **Online Log** captures the narrative of mission-time actions, alerts, and notes.
- **Hydrosens** informs environmental readiness where sound velocity and related profiles matter, while retaining the specialist workflow for acquisition, review, approval, and distribution.
- **Qinsy** remains an external but essential navigation context for current operations.

## Design Requirements
- The surveyor should be able to move from awareness to intervention without reconstructing context.
- Mission Deck should not be treated as one flat cockpit where every function competes for the same interaction role.
- Mission Overview should remain the default decision surface.
- Systems should remain the deeper operational and control surface.
- Environmental readiness should be visible at mission level without forcing the full Hydrosens workflow into Mission Deck.
- Systems should express `SVP` dependency meaning for affected sensors without treating Hydrosens as a normal system pane.
- Actions should expose consequence and downstream impact clearly.
- Mission Deck should not try to fully absorb every specialist workflow.
- The package should remain effective in dense operational environments and support multiple-screen setups without depending on a rigid layout definition.

## Current Direction
Mission Deck remains one of the most important and stable concepts in OI Survey, but its internal structure is now clearer than earlier versions of the documentation suggested.

The current direction is:
- **Mission Overview** as the default primary decision surface
- **Systems** as the deep operational/control surface
- **Online Log** and **Data Monitor** as connected but distinct parts of the broader mission-time package
- **Hydrosens** as a specialized environmental readiness subsystem connected through mission-level readiness and system-level dependency meaning

This does not mean Mission Deck and Multi-Mission Context are being designed on separate timelines. The mission-level model should help shape what cross-mission aggregation needs to show and support.

## Research Implications
The senior surveyor workshop strongly supports Mission Deck as the primary home for:
- mission-time understanding and intervention
- trustworthy selected-system context
- visible consequence of start/stop/restart and related actions
- fast movement between issue recognition, deep system work, evidence, and traceability

The workshop supports one central mission-time package, but it does not require every mission-time need to live in one flat surface.

## Summary Statement
> Mission Deck should be the active mission package in OI Survey: a mission-time container that brings together Mission Overview, Systems, traceability, and connected evidence workflows without forcing all work into one overloaded surface.

### DOCUMENT END | PDD.04.02

### DOCUMENT START | PDD.04.03 | Detached Evidence Surfaces

- kind: `doc_id`
- id: `PDD.04.03`
- title: `Detached Evidence Surfaces`
- path: `02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `853`

---
doc_id: PDD.04.03
title: Detached Evidence Surfaces
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "evidence", "qc", "monitoring"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.03 - Detached Evidence Surfaces

## Maturity
**Core / Evolving**

## Purpose
Detached Evidence Surfaces describe the family of product views used when evidence needs to be interpreted outside the immediate control surface.

## Surveyor Need
Some forms of evidence are easier to understand when they are not compressed into the same surface that owns mission-time control. Surveyors may need to:
- monitor imagery or datagrams continuously
- compare multiple evidence feeds side by side
- keep a camera or sonar view visible while working elsewhere
- apply optional QC overlays without cluttering the main control surface

## Capability Scope
This family may include:
- acoustic data views
- datagram or QC views
- vessel camera feeds
- ROV camera feeds
- evidence comparison surfaces
- optional overlay-enabled monitoring views

## Product Direction
The older `Stream Viewer` concept is still useful, but should now be treated as one possible product manifestation of the broader detached evidence capability.

## Relationship To Data Monitor
Current product direction introduces **Data Monitor** as the package-level name for the broader evidence and QC capability family.

Within that direction:
- `Detached Evidence Surfaces` remains the canonical design concept for evidence-first views that separate interpretation from direct control.
- `Data Monitor` is the broader package-level capability label that can include:
  - `Stream Viewer`
  - `Stream QC`
  - detached evidence views
  - evolving evidence comparison or QC-oriented surfaces

Working rule:
- do not collapse Detached Evidence Surfaces into a single rigid module too early
- do use `Data Monitor` when describing the broader product structure and capability family

## Design Rules
- Detached evidence should remain mission-context aware.
- The product should make it clear whether a surface is observational only or linked to operational consequence.
- QC overlays should support interpretation, not become decorative overlays without operational meaning.
- Detached evidence should complement Mission Deck, not compete with it as the primary operating surface.

## Research Implications
The senior surveyor workshop adds strong evidence for this surface family by repeatedly pointing to:
- live stream viewing across sensor types
- side-by-side evidence comparison
- camera and imagery visibility outside the main control workflow
- QC overlays and short-history/trend support for interpretation

This supports keeping detached evidence as a durable capability even if the exact product manifestation remains flexible.

## Summary Statement
> Detached Evidence Surfaces should help surveyors inspect, compare, and watch evidence in the way the mission demands, without forcing every evidence-heavy workflow back into the central mission-time control surface.

### DOCUMENT END | PDD.04.03

### DOCUMENT START | PDD.04.04 | Operational Configuration Management

- kind: `doc_id`
- id: `PDD.04.04`
- title: `Operational Configuration Management`
- path: `02_Product_Design/PDD.04.04_Operational_Configuration_Management.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `557`

---
doc_id: PDD.04.04
title: Operational Configuration Management
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "configuration", "validation", "governance"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.04_Operational_Configuration_Management.md
  - rel: related
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
---

# PDD.04.04 - Operational Configuration Management

## Maturity
**Core / Evolving**

## Purpose
This document defines how OI Survey should handle staged setup, validation, thresholds, lock state, and confidence in configuration truth.

## Surveyor Need
Surveyors need confidence that:
- the active setup is understood
- staged changes are visible before they are applied
- thresholds and templates are not hidden or inconsistent
- they can tell what is safe to change during live operations
- configuration truth and mission-time evidence do not silently diverge

## Product Role
Operational configuration management is broader than a single tool or modal. It is the capability that governs:
- staged vs live change
- validation and review
- thresholds and health definitions
- templates and reusable setup patterns
- lock state and authority controls
- configuration traceability

## Current Direction
The older `Configuration Manager` concept remains important, but its exact product boundary is still evolving. The capability should be documented now even if the final product surface naming changes later.

## Design Rules
- Separate staged setup from live operational state.
- Make validation legible before action, not only after failure.
- Expose what a change affects, especially where survey truth or downstream consumers may be impacted.
- Keep configuration ownership compatible with specialized subsystems such as Hydrosens.

## Summary Statement
> Operational configuration management should help survey teams trust that setup, thresholds, validation, and applied runtime state remain understandable, reviewable, and safe to change within the realities of mission execution.

### DOCUMENT END | PDD.04.04

### DOCUMENT START | PDD.04.05 | Online Log and Traceability Service

- kind: `doc_id`
- id: `PDD.04.05`
- title: `Online Log and Traceability Service`
- path: `02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `916`

---
doc_id: PDD.04.05
title: Online Log and Traceability Service
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "traceability", "logging", "service"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.05 - Online Log and Traceability Service

## Maturity
**Specialized / Active**

## Purpose
Online Log is the traceability layer of OI Survey. It replaces legacy spreadsheet-based logging with a structured, semi-automated event database that captures the operational narrative of survey and vessel activity.

## Product Role In OI Survey
Within the OI Survey ecosystem, Online Log:
- captures automated events from operational systems
- captures user actions from the Foundational App and related OI Survey workflows
- supports low-friction manual annotation by surveyors and supervisors
- provides a synchronized source of operational truth across vessels, payloads, and missions
- supports DPR generation, reporting workflows, compliance, billing support, and auditability

## Surveyor Need
Survey teams need a record they can trust for:
- handovers
- incident understanding
- defensible reporting
- client transparency
- reconstructing what happened and why

## Service Boundaries
Online Log should be understood as a shared service, not only a panel or window.

| Capability | Operational Value |
| --- | --- |
| **Automated event capture** | Reduces manual burden and improves completeness. |
| **User action traceability** | Preserves accountability for mission-time intervention. |
| **Manual annotations** | Allows contextual human judgment to remain part of the record. |
| **Cross-mission consistency** | Supports fleet-level, vessel-level, and mission-level reporting continuity. |
| **Export and reporting support** | Enables downstream DPR and related workflows. |

## Relationship To OI Survey Core
- Mission Deck and related surfaces should feed Online Log through both system-generated and user-generated events.
- Specialized subsystems such as Hydrosens should also contribute traceable workflow events.
- Online Log should remain the backbone for later automation, analytics, and multi-mission operational understanding.

For Hydrosens specifically, Online Log should capture events such as:
- cast acquired
- profile reviewed or cleaned
- profile approved
- profile exported
- profile distributed or applied to downstream systems
- explicit degraded-operation acceptance or override where environmental profile validity remains under question

## Research Implications
The senior surveyor workshop reinforces traceability as an operational need rather than an administrative add-on. The strongest signals are:
- event logging must support live operational understanding and later reporting
- handover quality depends on one trustworthy narrative rather than scattered notes and system records
- file-transfer state, user actions, and mission events should contribute to the same defensible timeline

This strengthens the treatment of Online Log as a shared service backbone for OI Survey.

## Summary Statement
> Online Log should be treated as the traceability backbone of OI Survey: a structured operational record that binds together automation, intervention, annotation, reporting, and confidence in what happened across survey work.

### DOCUMENT END | PDD.04.05

### DOCUMENT START | PDD.04.06 | Hydrosens Environmental Profile Management

- kind: `doc_id`
- id: `PDD.04.06`
- title: `Hydrosens Environmental Profile Management`
- path: `02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `1152`

---
doc_id: PDD.04.06
title: Hydrosens Environmental Profile Management
version: 0.1.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "hydrosens", "svp", "environmental-profiles"]
created: 2026-04-06
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md
  - rel: related
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: related
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.04.06 - Hydrosens Environmental Profile Management

## Maturity
**Specialized / Active**

## Purpose
Hydrosens is the OI Survey subsystem responsible for the lifecycle of sound velocity profiles and related environmental data. It replaces EIVA SVP Manager in Ocean Infinity operations and should be treated as a first-class part of the broader survey experience.

Hydrosens should be treated specifically as a **specialized environmental readiness subsystem**, not as a normal mission-time `Systems` pane and not merely as an evidence-monitoring surface under `Data Monitor`.

## Surveyor Need
Survey teams need a trustworthy way to:
- acquire environmental profile data
- review and clean profiles
- prepare survey-ready SVPs
- understand profile provenance and quality
- distribute approved profiles to downstream systems with confidence

## Operational Scope
Hydrosens covers:
- acquisition from connected hydrographic and environmental sensors
- logging of raw and processed profile data
- profile review, cleaning, comparison, resampling, extension, and preparation
- approval of survey-ready profiles
- export and distribution to downstream survey and navigation systems
- future automation and remote-control potential through extensible interfaces

## Why It Matters To OI Survey
Sound velocity and environmental profile truth are not peripheral concerns. They directly affect:
- survey accuracy
- system confidence
- readiness decisions
- downstream deliverable confidence
- the surveyor's trust in the mission setup

## Relationship To The Broader Experience
- **Mission Deck** should expose the operational consequence of profile readiness without trying to absorb the full Hydrosens workflow.
- **Mission Overview** should be the primary mission-level place where environmental readiness is surfaced.
- **Systems** should show `SVP` dependency meaning for affected acoustic systems without treating Hydrosens as a generic system pane.
- **Online Log** should capture profile acquisition, review, approval, export, and distribution events.
- **Operational Configuration Management** should remain compatible with Hydrosens where thresholds, profiles, or distribution choices affect mission truth.

## Placement In The Experience
The preferred product placement is:
- **primary home:** specialized subsystem
- **mission-time presence:** environmental readiness summary and consequence in Mission Overview
- **system-level presence:** `SVP` dependency and applied-profile meaning in affected acoustic systems
- **traceability presence:** lifecycle events in Online Log
- **cross-mission presence:** future aggregated environmental risk summaries in Multi-Mission Context

Hydrosens should therefore not be treated as:
- a standard `Systems` inventory item
- the default place for line-time intervention
- a capability absorbed into `Data Monitor`, except where observational or comparison views overlap

## Product Direction
Hydrosens should be documented under its current product/module identity while also representing the longer-lived capability of environmental profile management.

## Research Implications
The senior surveyor workshop adds strong support for keeping environmental and geodetic readiness visible in the broader OI Survey model. The workshop material repeatedly points to the need for:
- trustworthy SVP and reference-data preparation
- explicit visibility of profile readiness and validity
- operational continuity between specialist profile workflows and mission-time confidence

This reinforces Hydrosens as a specialized but connected subsystem rather than a hidden utility.

## Summary Statement
> Hydrosens should remain a distinct but fully connected part of OI Survey: the specialized environmental readiness subsystem that turns raw environmental acquisition into validated, survey-ready profile truth that can be distributed and trusted downstream.

### DOCUMENT END | PDD.04.06

### DOCUMENT START | PDD.05 | Operational State and Configuration Model

- kind: `doc_id`
- id: `PDD.05`
- title: `Operational State and Configuration Model`
- path: `02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `841`

---
doc_id: PDD.05
title: Operational State and Configuration Model
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "state", "configuration", "operations"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
  - rel: related
    href: 02_Product_Design/PDD.04.04_Operational_Configuration_Management.md
---

# PDD.05 - Operational State and Configuration Model

## Maturity
**Core / Evolving**

## Purpose
This document defines the key states that matter across mission execution, configuration management, evidence interpretation, and environmental profile distribution.

## Mission Lifecycle States
- **Preparation**: setup, validation, calibration, and readiness work before live acquisition.
- **Active Acquisition**: mission-time operation, evidence interpretation, and live intervention.
- **Degraded Operation**: survey continues or pauses under degraded confidence, dependencies, or evidence quality.
- **Review / Handover**: mission narrative, state understanding, and follow-on work are consolidated.

## Configuration States
- **Baseline**: known configuration starting point.
- **Staged**: proposed but not yet applied.
- **Applied**: accepted as the active operational setup.
- **Locked**: prevented from change due to authority or operational safety.
- **Divergent**: observed runtime behavior no longer matches expected configuration truth.

## Evidence States
- **Nominal**: evidence supports current understanding.
- **Watch**: evidence suggests closer attention is needed.
- **Invalidating**: evidence undermines confidence in readiness or quality.
- **Detached Review**: evidence requires deeper inspection outside the main control surface.

## Environmental Profile States
- **Acquired**: profile captured from source systems.
- **Prepared**: reviewed and processed but not yet approved.
- **Survey-Ready**: accepted for operational use.
- **Distributed**: exported or delivered to downstream systems.
- **Stale / Questioned**: no longer trusted without revalidation.

Environmental profile state should be treated as a **first-class operational state**, not merely as a background dependency. It should affect:
- mission-level environmental readiness
- affected-system readiness and dependency state
- traceability and handover confidence

## Environmental Readiness Expectations
The product should make environmental readiness legible at mission level by answering:
- how fresh the currently relevant profile is
- whether the active profile is trusted
- whether a newer cast is pending review
- whether an approved profile has been distributed or applied to affected systems
- what operational consequence follows if profile truth is stale, missing, or questioned

## Traceability Expectations
Every significant shift between these states should be traceable through Online Log or equivalent trace events, with enough context to support handover, reporting, and audit.

## Summary Statement
> OI Survey should make operational state visible across missions, systems, evidence, configuration, and environmental profiles so that survey teams can tell not only what is happening, but what is trustworthy right now.

### DOCUMENT END | PDD.05

### DOCUMENT START | PDD.06 | Roles, Authority and Operational Modes

- kind: `doc_id`
- id: `PDD.06`
- title: `Roles, Authority and Operational Modes`
- path: `02_Product_Design/PDD.06_Roles_Authority_and_Operational_Modes.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `944`

---
doc_id: PDD.06
title: Roles, Authority and Operational Modes
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "roles", "authority", "operations"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.06_Roles_Authority_and_Operational_Modes.md
  - rel: related
    href: 01_UX_Research/UXR.01_Roles_and_Responsibilities.md
  - rel: related
    href: 01_UX_Research/UXR.05_Role-Based_Insights.md
  - rel: related
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
---

# PDD.06 - Roles, Authority and Operational Modes

## Purpose
This document defines who acts, supervises, validates, annotates, and configures across the OI Survey ecosystem.

## Roles

| Role | Primary Product Relationship |
| --- | --- |
| **Survey Operator** | Uses Multi-Mission Context and Mission Deck to supervise active operations and intervene during mission time. |
| **Senior Surveyor** | Validates setup, supports problem-solving, interprets quality implications, and often owns higher-consequence configuration or environmental decisions. |
| **PEC** | Needs operational awareness, coordination context, and confidence in the status narrative rather than direct low-level control. |
| **Data Processor** | Relies on traceability, completeness, and downstream clarity for validation and reporting work. |
| **IT / Support** | Supports platform reliability, infrastructure confidence, and system integrity. |

## Surface-Level Authority Model

| Product Element | Primary Actors | Typical Authority |
| --- | --- | --- |
| **Multi-Mission Context** | Operator, Senior, PEC | Awareness, prioritization, mission focus selection. |
| **Mission Deck** | Operator, Senior | Mission-time supervision and intervention. |
| **Detached Evidence Surfaces** | Operator, Senior, Data Processor | Interpretation and monitoring, usually with limited direct control. |
| **Operational Configuration Management** | Senior, Operator, IT | Staged changes, thresholds, validation, locks, and templates depending on authority. |
| **Online Log** | Operator, Senior, PEC, Data Processor | Annotation, review, filtering, and operational reconstruction. |
| **Hydrosens** | Senior, Operator, specialist users | Profile acquisition, QC, approval, and distribution depending on role and authority. |

## Operational Modes
- **Preparation**: setup and validation dominate.
- **Active Acquisition**: intervention authority and runtime clarity matter most.
- **Degraded Mode**: escalation, interpretation, and consequence management become more important.
- **Review / Handover**: narrative quality, validation, and completeness matter most.

## Design Requirements
- The product should make authority boundaries visible.
- The product should support collaboration without erasing accountability.
- The same role may need different levels of access across missions or workflows.
- Traceability should preserve both system events and human judgment.

## Research Implications
The senior surveyor workshop sharpens the importance of:
- visible lock state and permission boundaries during live work
- safe multi-user participation without overlapping interference
- clear accountability for configuration, intervention, and annotation

This supports keeping authority, permission, and collaboration concerns explicit in the product model rather than treating them as background admin behavior.

## Summary Statement
> OI Survey should make roles and authority legible at the moment of work so that survey teams can collaborate safely without losing clarity about who can act, who can validate, and who remains accountable.

### DOCUMENT END | PDD.06

### DOCUMENT START | PDD.07 | Design Bets, Gaps and Future Directions

- kind: `doc_id`
- id: `PDD.07`
- title: `Design Bets, Gaps and Future Directions`
- path: `02_Product_Design/PDD.07_Design_Bets_Gaps_and_Future_Directions.md`
- section_id: `02PD`
- section_title: `Product Design`
- canonical_role: `canonical_doc`
- estimated_tokens: `2228`

---
doc_id: PDD.07
title: Design Bets, Gaps and Future Directions
version: 0.2.0
status: draft
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["design", "future", "gaps", "bets"]
created: 2025-11-09
last_updated: 2026-04-06
review_after: 2026-07-01
links:
  - rel: section
    href: 02_Product_Design
  - rel: source
    href: 02_Product_Design/PDD.07_Design_Bets_Gaps_and_Future_Directions.md
---

# PDD.07 - Design Bets, Gaps and Future Directions

## Maturity
**Draft / Emerging**

## Purpose
This document preserves unresolved product questions, active design bets, prototype gaps, and future-facing concepts without confusing them with core product truth.

It is also the canonical place to hold **promoted but unresolved architecture and interaction-model questions** that matter enough to preserve, but are not yet ready to become settled product truth or formal decision records.

## Active Design Bets
- Stronger mission-level surface clarity is an important organizing direction and should continue to be reinforced.
- Safe multi-mission operations remain strategically important and should continue to be refined rather than discarded.
- Detached evidence surfaces remain important even if their final product shape is not yet fixed.
- Operational configuration management is a necessary capability, even if its final UI boundary is still evolving.
- `Data Monitor` is a useful package-level framing for evidence and QC capabilities, even though its final product boundary is still evolving.

## Current Gaps
- Prototype coverage is strongest in acquisition-layer system experiences and does not yet represent the full OI Survey product.
- Cross-mission maturity is still evolving, but it should continue to be shaped in parallel with mission-level surface development.
- Collaboration, some role-specific workflows, and some cross-mission behaviors remain underdefined.
- Exact product boundaries between `Data Monitor`, detached evidence, and other evidence/QC capabilities still need refinement.
- Exact product boundaries between core surfaces, specialized subsystems, and shared services still need refinement.

## Active Architecture Questions
The following items are important enough to preserve canonically, but should not yet be treated as settled architecture. They exist to improve product memory and decision hygiene until stronger evidence or decisions are available.

### Topic: Mission-Time Decision Model
**Why it matters operationally**  
Surveyors and senior surveyors need more than status visibility. They need a trustworthy decision contract for whether work is safe to run, continue with risk, pause, or escalate.

**Current gap**  
The current architecture describes awareness, readiness, and consequence, but it does not yet define an explicit safe-to-run / continue-with-risk / pause / escalate model for mission-time use.

**Directionally true today**  
Mission Overview should likely be the primary place where this mission-time decision logic becomes legible.

**Unknowns / decisions not yet made**  
How many operational states should exist, who can move between them, and how strongly they should affect Mission Deck, Systems, and Online Log behavior.

**Evidence needed to close it**  
Senior surveyor validation of real degraded-operation decision patterns, acceptance thresholds, and escalation behavior.

**Priority / impact**  
High. This is central to product fit and operational trust.

### Topic: Spatial and Line-Context Integration
**Why it matters operationally**  
Survey work is often interpreted through line progress, KP/progress, deviation, and spatial context rather than through systems alone.

**Current gap**  
The docs acknowledge navigation and spatial truth, but the role of line, KP/progress, deviation, and survey-area context is still underdefined inside mission-time surfaces.

**Directionally true today**  
Mission Overview and Multi-Mission Context both need a stronger spatial/line-context layer, even if Qinsy remains an explicit external dependency.

**Unknowns / decisions not yet made**  
Which spatial signals should be shown directly in OI Survey, which should remain dependency acknowledgements, and how they should appear across mission-level and cross-mission surfaces.

**Evidence needed to close it**  
Examples of line-time supervisory workflows, navigation-heavy exception handling, and how surveyors actually combine spatial and system confidence signals.

**Priority / impact**  
High. This changes whether the product feels operationally credible or merely system-aware.

### Topic: Multi-Mission Context Mandatory Signal Set
**Why it matters operationally**  
Cross-mission work is only safe if each mission is compressed into a reliable set of signals that survive aggregation without hiding critical context.

**Current gap**  
Multi-Mission Context is directionally defined, but its mandatory information contract is still too generic for safe supervisory use.

**Directionally true today**  
It should likely recombine a subset of the most important mission-level signals rather than invent a separate cross-mission status model.

**Unknowns / decisions not yet made**  
Which fields are mandatory in the compressed mission view: mission phase, active risk, environmental readiness, key degraded dependency, unresolved note state, reason this mission needs attention now, or other signals.

**Evidence needed to close it**  
Cross-mission triage examples, senior-surveyor review of compressed mission states, and validation of what can be safely omitted.

**Priority / impact**  
High. This directly affects safe multi-mission fit.

### Topic: Cross-Surface Resolution Loop
**Why it matters operationally**  
Operational trust comes from the full loop: issue recognition, deeper diagnosis, specialist action, recorded outcome, and updated mission confidence.

**Current gap**  
The architecture defines the main surfaces, but not yet the explicit interaction pattern that links Mission Overview, Systems, Data Monitor, Hydrosens, and Online Log into one closed-loop operational flow.

**Directionally true today**  
Mission Overview should likely surface the issue, specialist or deeper surfaces should resolve it, and Online Log should preserve the accepted outcome while state flows back into mission-level surfaces.

**Unknowns / decisions not yet made**  
Which loops are generic across all issue types, which require subsystem-specific variants, and how much of the loop should be standardized in the product model.

**Evidence needed to close it**  
Concrete incident and recovery walkthroughs across systems, evidence, environmental workflows, and handover scenarios.

**Priority / impact**  
High. This is central to interaction-model coherence.

### Topic: Degraded-Operation Governance and Sign-Off
**Why it matters operationally**  
Real operations often continue under controlled degradation rather than under clean nominal conditions. Accountability for that choice matters.

**Current gap**  
The current docs define roles and permissions broadly, but do not yet define who can accept degraded conditions, how that choice is surfaced, or how it is logged and reviewed.

**Directionally true today**  
This likely needs explicit linkage between Mission Overview, role/authority rules, and Online Log.

**Unknowns / decisions not yet made**  
Who can accept degraded operation, when a supervisor or senior surveyor sign-off is required, how overrides expire, and how accepted risk should remain visible afterward.

**Evidence needed to close it**  
Senior surveyor and supervisory role validation on degraded-mode authority, exception handling, and audit expectations.

**Priority / impact**  
High. This is necessary for operational trust, governance, and defensible traceability.

## Future Directions Worth Preserving
- richer cross-mission supervision patterns
- broader evidence detachment and comparison workflows
- clearer consolidation of evidence and QC capabilities under the `Data Monitor` product direction
- deeper integration between Online Log and operational automation
- expanded environmental workflow automation through Hydrosens
- clearer product treatment of external dependencies such as Qinsy over time

## Rule For Use
Items in this document should inform research and design iteration, but should not override the more mature design truth captured in `PDD.00` through `PDD.06`.

Questions captured under `Active Architecture Questions` are promoted unresolved items. They should not be treated as settled truth until they are either:
- resolved into updates to more mature canonical docs
- promoted into a formal `DCR.*` decision record
- or supported by further evidence in `sources/`

## Summary Statement
> PDD.07 exists to preserve promising directions and acknowledged gaps without allowing unresolved ideas to silently become the default product model.

### DOCUMENT END | PDD.07

## SECTION END | 02PD

## SECTION START | 03DC | Decisions

- section_id: `03DC`
- title: `Decisions`
- base_path: `03_Decisions`
- tags: [decisions, product, design, governance]
- document_count: `3`

### DOCUMENT START | DCR.0001 | Multi-Mission Context Naming

- kind: `decision_id`
- id: `DCR.0001`
- title: `Multi-Mission Context Naming`
- path: `03_Decisions/DCR.0001_Multi-Mission_Context_Naming.md`
- section_id: `03DC`
- section_title: `Decisions`
- canonical_role: `decision_record`
- estimated_tokens: `432`

---
decision_id: DCR.0001
title: Multi-Mission Context Naming
status: accepted
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["decision", "naming", "product-design", "multi-mission"]
created: 2026-04-06
last_updated: 2026-04-08
links:
  - rel: evidence
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
  - rel: affected
    href: 02_Product_Design/PDD.04.01_Multi-Mission_Context.md
---

# DCR.0001 - Multi-Mission Context Naming

## Question
What should replace the older `Triage Hub` concept in the OI Survey product model?

## Decision
Use `Multi-Mission Context` as the canonical product term.

## Why
The updated term better reflects the surveyor's actual job: maintaining awareness across assigned missions, understanding which mission needs attention now, and shifting focus safely without reducing the concept to a single screen or card grid.

## Evidence
- Product design refactor in `02_Product_Design`
- Senior surveyor workshop synthesis in `UXR.08`
- Current multi-mission positioning in product foundation and design docs

## Implications
- `Triage Hub` should remain a historical term only where needed for traceability.
- Product and design documentation should use `Multi-Mission Context` as the canonical term.
- Future decisions about layout or interaction should not reintroduce the older name by default.

## Alternatives Considered
- Keep `Triage Hub`
- Use `Mission Overview`

## Product Naming Note
Use `OI Survey` as the primary full product name in product and UI copy. `OIS` remains approved shorthand, not a competing visible product title.

## Follow-Up
- Validate the terminology with a broader stakeholder group as the product language matures.

### DOCUMENT END | DCR.0001

### DOCUMENT START | DCR.0002 | Product Surface Model

- kind: `decision_id`
- id: `DCR.0002`
- title: `Product Surface Model`
- path: `03_Decisions/DCR.0002_Product_Surface_Model.md`
- section_id: `03DC`
- section_title: `Decisions`
- canonical_role: `decision_record`
- estimated_tokens: `919`

---
decision_id: DCR.0002
title: Product Surface Model
status: accepted
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["decision", "product-model", "naming", "architecture"]
created: 2026-04-13
last_updated: 2026-04-13
links:
  - rel: evidence
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: evidence
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: evidence
    href: 02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md
  - rel: affected
    href: 00_Product_Foundation/PFD.01_Product_Vision.md
  - rel: affected
    href: 00_Product_Foundation/PFD.03_Product_Architecture_Overview.md
  - rel: affected
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
---

# DCR.0002 - Product Surface Model

## Question
How should OI Survey's near-term product structure be described so the documentation reflects the current direction without collapsing the product into one flat application model?

## Decision
Use a **product surface model** in which OI Survey is described first as a **unified operational ecosystem**, and structurally as a set of connected operational surfaces, shared services, and specialist subsystems.

Within that model:
- `Mission Deck` is the mission-time container/package element
- `Mission Overview` is the default primary decision surface
- `Systems` is the deep operational/control surface
- `Data Monitor` is the package-level evidence/QC capability family
- `Multi-Mission Context` remains a parallel cross-mission awareness surface
- `Online Log` remains the traceability backbone and shared service

## Why
This model reflects the current product direction more accurately than describing OI Survey as one flat application shell or reducing it to a mere software package.

It also matches observed prototype direction more closely:
- Mission Overview already exists as the default overview surface inside Mission Deck
- Systems already exists as the deeper operational workspace
- Online Log is already first-class
- Multi-Mission Context remains distinct
- Mission Overview and Multi-Mission Context are being shaped together as related layers of the same attention model
- evidence and QC capabilities exist in multiple forms that are better grouped under a package-level direction than forced into one early rigid module

## Evidence
- `02_Product_Design/PDD.01_OIS_Product_Topology.md`
- `02_Product_Design/PDD.04.02_Mission_Deck.md`
- `02_Product_Design/PDD.04.03_Detached_Evidence_Surfaces.md`
- current `sm-poseidon` prototype naming and workspace structure

## Implications
- Product and design documentation should describe OI Survey as a unified operational ecosystem.
- Mission Deck should no longer be described as one flat cockpit.
- Mission Overview should be treated as the default mission-time decision surface.
- Systems should be treated as the deep operational/control surface.
- Data Monitor can be used as a package-level capability term without forcing Detached Evidence Surfaces to be renamed or discarded.
- Multi-Mission Context remains strategically important and should continue evolving in parallel with mission-level surfaces rather than being treated as a distant later-stage capability.

## Alternatives Considered
- Keep describing OI Survey as a unified application.
- Treat Multi-Mission Context as the primary default organizing model.
- Rename Detached Evidence Surfaces directly to Data Monitor.

## Follow-Up
- Align Product Foundation and Product Design language to this model.
- Preserve older terminology only where needed for traceability.
- Keep validating the product boundary of Data Monitor as evidence and QC capabilities mature.

### DOCUMENT END | DCR.0002

### DOCUMENT START | DCR.0003 | Hydrosens Placement Model

- kind: `decision_id`
- id: `DCR.0003`
- title: `Hydrosens Placement Model`
- path: `03_Decisions/DCR.0003_Hydrosens_Placement_Model.md`
- section_id: `03DC`
- section_title: `Decisions`
- canonical_role: `decision_record`
- estimated_tokens: `826`

---
decision_id: DCR.0003
title: Hydrosens Placement Model
status: accepted
visibility: internal
owners: ["pedro.baptista@oceaninfinity.com"]
tags: ["decision", "hydrosens", "svp", "product-model", "architecture"]
created: 2026-04-14
last_updated: 2026-04-14
links:
  - rel: evidence
    href: 01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md
  - rel: affected
    href: 02_Product_Design/PDD.01_OIS_Product_Topology.md
  - rel: affected
    href: 02_Product_Design/PDD.04.02_Mission_Deck.md
  - rel: affected
    href: 02_Product_Design/PDD.04.05_Online_Log_and_Traceability_Service.md
  - rel: affected
    href: 02_Product_Design/PDD.04.06_Hydrosens_Environmental_Profile_Management.md
  - rel: affected
    href: 02_Product_Design/PDD.05_Operational_State_and_Configuration_Model.md
---

# DCR.0003 - Hydrosens Placement Model

## Question
Where should Hydrosens fit inside the OI Survey product architecture and experience model?

## Decision
Treat `Hydrosens` as a **specialized environmental readiness subsystem**.

Within that model:
- Hydrosens owns the full SVP workflow: acquire, inspect, clean, compare, prepare, approve, export, distribute
- Mission-time surfaces expose the **operational consequence** of environmental profile readiness
- `Mission Overview` is the primary mission-level place where environmental readiness is surfaced
- affected acoustic systems in `Systems` show `SVP` dependency state and operational consequence
- `Online Log` records Hydrosens lifecycle events
- `Multi-Mission Context` may later aggregate cross-mission environmental risk summaries, but does not own the specialist workflow

## Why
This model best matches senior surveyor operating logic.

SVP management is not a normal line-time system pane. It is a readiness-governance workflow with mission-time consequences. Surveyors need to know whether environmental profile truth is affecting the mission now, but the full Hydrosens workflow should remain a specialist subsystem rather than being flattened into `Systems` or absorbed into `Data Monitor`.

## Evidence
- `01_UX_Research/UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md`
- current Hydrosens and environmental readiness positioning in `02_Product_Design`
- prototype signals showing SVP age and dependency meaning in mission and sensor surfaces

## Implications
- Hydrosens should not be treated as a generic `Systems` pane.
- Hydrosens should not be positioned merely as an evidence-monitoring capability under `Data Monitor`.
- Mission Overview should surface environmental readiness at mission level.
- Systems should show `SVP` dependency and applied-profile meaning for affected acoustic systems.
- Online Log should capture profile acquisition, review, approval, export, and distribution events.

## Alternatives Considered
- Treat Hydrosens as a normal system pane inside `Systems`
- Treat Hydrosens as part of `Data Monitor`
- Hide Hydrosens behind mission-time dependency states without a visible subsystem identity

## Follow-Up
- Keep `Hydrosens` visible as the current product/module identity for the SVP manager.
- Refine environmental readiness as a reusable mission-level concept.
- Validate how Multi-Mission Context should summarize cross-mission environmental risk without absorbing the Hydrosens workflow.

### DOCUMENT END | DCR.0003

## SECTION END | 03DC
