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
