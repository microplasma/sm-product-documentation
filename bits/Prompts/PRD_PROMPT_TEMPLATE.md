# PRD_PROMPT_TEMPLATE
version: 0.1.0  
last_updated: 2025-11-09  

## Purpose
This template defines how to ask an LLM to generate a **Product Requirements Document (PRD)** for the **SM Product System**, based on the structured documentation stored in this repository.

Use this as your master prompt when engaging a large language model or custom GPT.  
Once the PRD is generated, you can follow with the **Implementation Plan Extension** below.

---

## 🧩 Context Overview (for the model)

The repository is organized into three structured sections:

| Section | Folder | Description |
|----------|---------|-------------|
| **Product Foundation** | `00_Product_Foundation/` | Defines vision, strategy, architecture, and product pillars. |
| **UX Research** | `01_UX_Research/` | Summarizes user research, roles, workflows, pain points, and environmental context. |
| **Product Design** | `02_Product_Design/` | Describes the product experience architecture, UX framework, key features, and roadmap. |

Each document contains a `doc_id` prefix (e.g., `PFD.02`, `UXR.04`, `PDD.04.03`) and may include front matter metadata for versioning, tags, and ownership.

> Agents can refer to `DOC_MANIFEST.yml` to locate document paths and relationships.

---

## 🎯 Primary Prompt — Generate the Product Requirements Document (PRD)

**System / Role Instruction**

> You are a **Senior Product Manager** with strong UX and engineering collaboration experience.  
> You are responsible for writing a **Product Requirements Document (PRD)** for the SM Product System based on the provided repository documentation.  
> Your output must be **clear, structured, and traceable** — suitable for both design and engineering review.

**Task**

Using the provided document summaries, excerpts, and manifest references:

1. **Synthesize** a Product Requirements Document (PRD) that captures the full product intent.  
2. **Reference document IDs** (`doc_id`) wherever a source is used (e.g., *Derived from UXR.04*).  
3. Assign **requirement IDs** (`REQ-001`, `REQ-002`, etc.) to each core requirement.
4. Produce the PRD in **Markdown**, using the structure below.

---

### 🧱 Required PRD Structure

```
# Product Requirements Document (PRD)
## 1. Overview
- Product Name
- Document Owner
- Version, Date, and References (doc_ids)

## 2. Purpose & Background
- Summary of product vision and strategy (PFD.01, PFD.02)
- Architectural context and constraints (PFD.03)
- Product pillars (PFD.04)

## 3. Problem Definition
- Key user pain points (UXR.04)
- Context of use (UXR.06)
- Operational limitations and opportunities

## 4. Objectives & Success Metrics
- Product objectives mapped to pillars
- Key performance and experience metrics

## 5. Target Users & Roles
- Primary roles (UXR.01)
- Workflows and responsibilities (UXR.02)
- Role-based insights (UXR.05)

## 6. Functional Requirements
List all major functions and behaviors.
For each:
- Requirement ID: REQ-###
- Name and Description
- Rationale / Source doc_id
- Acceptance Criteria
- Dependencies or Constraints

Include subsections for:
- Core System Functions (PDD.01–PDD.03)
- Feature Workspaces (PDD.04.01–PDD.04.05)
- Data & Configuration (PDD.05)
- Roles & Modes (PDD.06)

## 7. Non-Functional Requirements
- Performance, reliability, safety, traceability
- Design and UX consistency expectations

## 8. Dependencies & Risks
- System dependencies and open items (PDD.07)
- Research or data gaps

## 9. Timeline & Ownership
- Next development milestones
- Owner teams or roles

## 10. Appendix
- Source Documents Table (doc_id, title, path)
```

---

### 📋 Output Requirements
- Output must be in **Markdown**.
- Keep the PRD under **3,000 words**.
- Maintain clarity, concision, and traceability.
- Use numbered sections and `###` subheadings.
- Tag every requirement with both a `REQ-###` and a `doc_id` source.

---

### 🧠 Optional Enhancements
You may ask the model to:
- Generate a **Requirements Traceability Matrix (RTM)** (REQ-ID → doc_id → section).
- Suggest **success metrics** aligned with the strategy.
- Produce a **summary table** mapping user pain points to product features.

---

## 🔜 Follow-Up Prompt — Generate Implementation Plan

Once the PRD is complete, provide it to the same or another model with the following instruction:

> **You are a Technical Program Manager.**  
> Using the PRD below, generate a detailed **Implementation Plan** that defines how the product will be developed.  
> Break down the plan into:
> - **Epics and Modules** (linked to `REQ-###`)  
> - **Engineering Deliverables** (APIs, services, UI components)  
> - **Dependencies and Sequencing**  
> - **Testing and Validation Plan**  
> - **Open Technical Questions**  
>  
> Output as a structured Markdown document, maintaining traceability to both `REQ-###` and `doc_id`.

---

## 🧩 Example Workflow

1. Copy excerpts or summaries from:
   - `PFD.01_Product_Vision.md`
   - `UXR.04_Pain_Points_and_Opportunities.md`
   - `PDD.04.03_Stream_Viewer.md`
2. Paste them after this prompt under a section titled **"Context Inputs"**.
3. Run this prompt in ChatGPT or your chosen LLM.
4. Save the output as `PRD_SM_Product_System.md`.
5. Use the PRD to generate an implementation plan via the follow-up prompt.

---

## 🧭 Notes
- Keep this file in the root of the repository.
- When the documentation evolves, update `DOC_MANIFEST.yml` and re-run this prompt for a refreshed PRD.
- Recommended output checkpoint: PRD v0.1 → Implementation Plan v0.1 → Engineering Spec v0.1

---
