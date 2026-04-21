# 02 Product Design
version: 0.2.0  
last_updated: 2026-04-06

This section describes how OI Survey should work for remote survey operations. It is written for both human readers and AI agents, and is organized around surveyor needs rather than a flat list of screens.

The current product-design framing treats OI Survey as a unified operational ecosystem expressed through connected operational surfaces. Within that model, Mission Deck remains the active mission-time container, with Mission Overview as the default decision surface and Systems as the deeper operational/control surface, while Multi-Mission Context evolves in parallel from the same attention model.

## Documentation Model
The Product Design section is layered so that mature concepts, evolving concepts, specialized subsystems, and shared services can live together without being treated as equally fixed.

### Layers
- **Foundational Design**: principles, product topology, information model, and interaction framework.
- **Core Product Surfaces**: the primary surveyor-facing operational surfaces.
- **Specialized Operational Subsystems**: deep domain workflows that remain part of the OI Survey experience.
- **Shared Services**: cross-cutting services that support traceability, reporting, and operational continuity.
- **Design Bets and Gaps**: unresolved questions, emerging concepts, and future-facing opportunities.

### Maturity Labels
- **Core**: stable product concepts that should guide design and implementation decisions.
- **Core / Evolving**: important concepts whose role is clear but whose exact product shape is still developing.
- **Specialized / Active**: domain-specific subsystems or services that are active parts of the experience.
- **Draft / Emerging**: concepts that should be preserved, but not overcommitted.

## Files (PDD.*)
- **PDD.00 - Design Principles and Documentation Model**  
  [`PDD.00_Design_Principles_and_Documentation_Model.md`](./PDD.00_Design_Principles_and_Documentation_Model.md)  
  *Surveyor-centered design principles, documentation purpose, and maturity model.*

- **PDD.01 - OIS Product Topology**  
  [`PDD.01_OIS_Product_Topology.md`](./PDD.01_OIS_Product_Topology.md)  
  *The overall OI Survey ecosystem, including core surfaces, specialized subsystems, and shared services.*

- **PDD.02 - Operational Information Model**  
  [`PDD.02_Operational_Information_Model.md`](./PDD.02_Operational_Information_Model.md)  
  *Operational objects, relationships, and information semantics that support survey work.*

- **PDD.03 - Interaction Framework and Surface Grammar**  
  [`PDD.03_Interaction_Framework_and_Surface_Grammar.md`](./PDD.03_Interaction_Framework_and_Surface_Grammar.md)  
  *Shared interaction rules across cross-mission, mission-context, detached, and service surfaces.*

### Core Product Surfaces
- **PDD.04.01 - Multi-Mission Context**  
  [`PDD.04.01_Multi-Mission_Context.md`](./PDD.04.01_Multi-Mission_Context.md)  
  *Cross-mission awareness, prioritization, and safe attention management.*

- **PDD.04.02 - Mission Deck**  
  [`PDD.04.02_Mission_Deck.md`](./PDD.04.02_Mission_Deck.md)  
  *Primary mission-time workspace for supervision, intervention, and system-level coordination.*

- **PDD.04.03 - Detached Evidence Surfaces**  
  [`PDD.04.03_Detached_Evidence_Surfaces.md`](./PDD.04.03_Detached_Evidence_Surfaces.md)  
  *Evidence-first views for datagrams, imagery, cameras, and QC overlays when interpretation needs to detach from control.*

- **PDD.04.04 - Operational Configuration Management**  
  [`PDD.04.04_Operational_Configuration_Management.md`](./PDD.04.04_Operational_Configuration_Management.md)  
  *How staged setup, validation, thresholds, and lock state should be managed across OI Survey.*

### Shared Services
- **PDD.04.05 - Online Log and Traceability Service**  
  [`PDD.04.05_Online_Log_and_Traceability_Service.md`](./PDD.04.05_Online_Log_and_Traceability_Service.md)  
  *The operational traceability service that captures mission narrative, interventions, and reporting evidence.*

### Specialized Operational Subsystems
- **PDD.04.06 - Hydrosens Environmental Profile Management**  
  [`PDD.04.06_Hydrosens_Environmental_Profile_Management.md`](./PDD.04.06_Hydrosens_Environmental_Profile_Management.md)  
  *SVP acquisition, QC, preparation, export, and distribution as part of the broader OI Survey experience.*

### State, Roles, and Futures
- **PDD.05 - Operational State and Configuration Model**  
  [`PDD.05_Operational_State_and_Configuration_Model.md`](./PDD.05_Operational_State_and_Configuration_Model.md)  
  *Mission state, configuration state, evidence state, and environmental distribution state across the lifecycle.*

- **PDD.06 - Roles, Authority and Operational Modes**  
  [`PDD.06_Roles_Authority_and_Operational_Modes.md`](./PDD.06_Roles_Authority_and_Operational_Modes.md)  
  *Who acts, supervises, validates, annotates, and configures across the OI Survey ecosystem.*

- **PDD.07 - Design Bets, Gaps and Future Directions**  
  [`PDD.07_Design_Bets_Gaps_and_Future_Directions.md`](./PDD.07_Design_Bets_Gaps_and_Future_Directions.md)  
  *Active bets, prototype gaps, promoted unresolved architecture questions, and future-facing ideas worth preserving.*

## Navigation
- Upstream: **UX Research** -> [`../01_UX_Research/README.md`](../01_UX_Research/README.md)

## Agent Hints
- `doc_id` pattern: `PDD.<NN>` or `PDD.04.<NN>`.
- Read `PDD.00` and `PDD.01` first when the question is about product shape or scope.
- Read `PDD.03` when the question is about shared interaction rules or surface behavior.
- Read `PDD.04.*` when the question is about a specific surface, service, or subsystem.
- Read `PDD.07` when the question is about unresolved architecture, product-fit gaps, or future-facing design questions that are important but not yet settled.
- Treat this folder as product-design truth, not a 1:1 reflection of the current prototype.
- Preserve heading structure and keep tables intact for retrieval.
