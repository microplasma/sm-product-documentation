# PRD_PROMPT_TEMPLATE
version: 0.2.0
last_updated: 2026-04-06

## Purpose
This template defines how to ask an LLM to generate a **Product Requirements Document (PRD)** for the **SM Product System**, using the curated knowledge stored in this repository.

Use this as a helper prompt when engaging a large language model or custom GPT.
Once the PRD is generated, you can follow with the **Implementation Plan Extension** below.

---

## Context Overview (for the model)

The repository is organized into four layers:

| Layer | Folder | Description |
|-------|--------|-------------|
| **Canonical Docs** | `00_Product_Foundation/`, `01_UX_Research/`, `02_Product_Design/` | The promoted source of truth for vision, research, and product design. |
| **Decisions** | `03_Decisions/` | Accepted or proposed product and design decisions linked to evidence and affected docs. |
| **Source Artifacts** | `sources/` | Raw or lightly structured evidence from workshops, external platforms, exports, and recordings. |
| **Helper Material** | `bits/` | Supporting templates, prompts, and helper content. Not canonical product truth. |

When generating a PRD:
- prioritize `00`, `01`, `02`, and accepted records in `03_Decisions/`
- use `sources/` only when a source package has already been promoted or explicitly referenced by canonical docs
- treat draft or evolving concepts carefully and avoid turning them into confirmed commitments unless supported by the canonical documentation

Each canonical document contains a `doc_id` prefix (for example `PFD.02`, `UXR.04`, `PDD.04.03`).
Decision records use `decision_id` values such as `DCR.0001`.

> Use `DOC_MANIFEST.yml` to locate canonical documents and relationships.

---

## Primary Prompt - Generate the Product Requirements Document (PRD)

**System / Role Instruction**

> You are a **Senior Product Manager** with strong UX and engineering collaboration experience.
> You are responsible for writing a **Product Requirements Document (PRD)** for the SM Product System based on the curated repository documentation.
> Your output must be **clear, structured, concise, and traceable**, and it must distinguish between confirmed product direction and evolving design areas.

**Task**

Using the provided document summaries, excerpts, decision records, and manifest references:

1. **Synthesize** a Product Requirements Document (PRD) that captures the current promoted product intent.
2. **Reference source IDs** wherever a source is used:
   - `doc_id` for canonical docs
   - `decision_id` for decision records
3. Assign **requirement IDs** (`REQ-001`, `REQ-002`, etc.) to each confirmed core requirement.
4. Distinguish between:
   - confirmed requirements
   - evolving or open design areas
5. Produce the PRD in **Markdown**, using the structure below.

---

### Required PRD Structure

```text
# Product Requirements Document (PRD)

## 1. Overview
- Product Name
- Document Owner
- Version and Date
- References (`doc_id`, `decision_id`)

## 2. Purpose and Background
- Summary of product vision and strategy (PFD.01, PFD.02)
- Architectural and operating context (PFD.03, PFD.04)
- Relevant accepted decisions

## 3. Problem Definition
- Key user pain points and operational realities (UXR.04, UXR.06, UXR.08)
- Workflow and role context (UXR.02, UXR.05)
- Constraints, dependencies, and opportunities

## 4. Objectives and Success Metrics
- Product objectives mapped to pillars and workflows
- Experience, operational, and quality metrics

## 5. Users, Roles, and Context of Use
- Primary roles and responsibilities
- Operational modes and authority boundaries
- Multi-mission and mission-time context

## 6. Confirmed Functional Requirements
For each requirement:
- Requirement ID: REQ-###
- Name
- Description
- Rationale / Source (`doc_id`, `decision_id`)
- Acceptance Criteria
- Dependencies or Constraints

Include subsections for:
- Product Topology and Interaction Model (PDD.01-PDD.03)
- Core Product Surfaces (PDD.04.01-PDD.04.06)
- Operational State and Roles (PDD.05, PDD.06)

## 7. Evolving or Open Areas
- Design bets, draft concepts, and unresolved questions (PDD.07)
- Research or evidence gaps
- Areas that should not yet be treated as committed scope

## 8. Non-Functional Requirements
- Performance, reliability, safety, traceability, and usability expectations
- Consistency and evidence-traceability expectations

## 9. Dependencies and Risks
- System dependencies
- External tools or operational dependencies
- Open risks and validation needs

## 10. Delivery Considerations
- Suggested milestones or sequencing
- Owner teams or roles
- Notes for implementation planning

## 11. Appendix
- Source table (`doc_id` or `decision_id`, title, path)
```

---

### Output Requirements
- Output must be in **Markdown**.
- Keep the PRD under **3,000 words** unless otherwise requested.
- Maintain clarity, concision, and traceability.
- Use numbered sections and `###` subheadings where helpful.
- Tag every confirmed requirement with both a `REQ-###` and at least one supporting source ID.
- Do not turn raw source artifacts into requirements unless they have already been promoted into canonical documentation or accepted decisions.

---

### Optional Enhancements
You may ask the model to:
- Generate a **Requirements Traceability Matrix (RTM)** (`REQ-ID -> source ID -> section`)
- Suggest **success metrics** aligned with the strategy and research
- Produce a **summary table** mapping pain points to product capabilities
- Produce a **decision coverage table** showing which accepted decisions materially shape the PRD

---

## Follow-Up Prompt - Generate Implementation Plan

Once the PRD is complete, provide it to the same or another model with the following instruction:

> **You are a Technical Program Manager.**
> Using the PRD below, generate a detailed **Implementation Plan** for the confirmed scope.
> Break down the plan into:
> - **Epics and modules** (linked to `REQ-###`)
> - **Engineering and design deliverables**
> - **Dependencies and sequencing**
> - **Validation and testing plan**
> - **Open technical and product questions**
> - **Explicit assumptions for evolving or unresolved areas**
>
> Maintain traceability to both `REQ-###` and the underlying `doc_id` or `decision_id`.
> Do not treat items from the PRD's evolving/open areas section as committed delivery scope unless explicitly promoted.

---

## Example Workflow

1. Copy excerpts or summaries from relevant canonical docs, for example:
   - `PFD.01_Product_Vision.md`
   - `UXR.04_Pain_Points_and_Opportunities.md`
   - `UXR.08_Senior_Surveyor_Workshop_Feature_Themes.md`
   - `PDD.04.02_Mission_Deck.md`
   - `PDD.04.06_Hydrosens_Environmental_Profile_Management.md`
2. Add any relevant accepted decisions, for example:
   - `DCR.0001_Multi-Mission_Context_Naming.md`
3. Paste them after this prompt under a section titled **Context Inputs**.
4. Run this prompt in ChatGPT or your chosen LLM.
5. Save the output as `PRD_SM_Product_System.md`.
6. Use the PRD to generate an implementation plan via the follow-up prompt.

---

## Notes
- Keep this file in `bits/Prompts/` as a helper artifact.
- When the documentation evolves, update `DOC_MANIFEST.yml` and refresh this prompt if the repository model changes.
- Recommended output checkpoint: `PRD v0.1 -> Implementation Plan v0.1 -> Engineering Spec v0.1`

---
