from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "DOC_MANIFEST.yml"
OUTPUT_PATH = REPO_ROOT / "CHATGPT_PROJECT_KNOWLEDGE.md"


@dataclass
class DocEntry:
    kind: str
    entry_id: str
    title: str
    path: str


@dataclass
class Section:
    section_id: str
    title: str
    base_path: str
    tags: str
    docs: list[DocEntry]


def parse_manifest(text: str) -> tuple[list[Section], list[DocEntry]]:
    lines = text.splitlines()
    sections: list[Section] = []
    root_docs: list[DocEntry] = []
    i = 0
    in_root_docs = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped == "root_docs:":
            in_root_docs = True
            i += 1
            continue

        if not in_root_docs and re.match(r"^  - section_id:", line):
            section_id = line.split(":", 1)[1].strip()
            section_title = lines[i + 1].split(":", 1)[1].strip()
            base_path = lines[i + 2].split(":", 1)[1].strip()
            tags = lines[i + 3].split(":", 1)[1].strip()
            i += 4
            docs: list[DocEntry] = []

            while i < len(lines):
                current = lines[i]
                if re.match(r"^  - section_id:", current) or current.strip() == "root_docs:":
                    break

                doc_match = re.match(r"^      - (doc_id|decision_id):\s*(.+)$", current)
                if doc_match:
                    kind = doc_match.group(1)
                    entry_id = doc_match.group(2).strip()
                    doc_title = lines[i + 1].split(":", 1)[1].strip()
                    path = lines[i + 2].split(":", 1)[1].strip()
                    docs.append(DocEntry(kind=kind, entry_id=entry_id, title=doc_title, path=path))
                    i += 3
                    continue

                i += 1

            sections.append(
                Section(
                    section_id=section_id,
                    title=section_title,
                    base_path=base_path,
                    tags=tags,
                    docs=docs,
                )
            )
            continue

        if in_root_docs:
            doc_match = re.match(r"^  - (doc_id|source_id):\s*(.+)$", line)
            if doc_match:
                kind = doc_match.group(1)
                entry_id = doc_match.group(2).strip()
                title = lines[i + 1].split(":", 1)[1].strip()
                path = lines[i + 2].split(":", 1)[1].strip()
                root_docs.append(DocEntry(kind=kind, entry_id=entry_id, title=title, path=path))
                i += 3
                continue

        i += 1

    return sections, root_docs


def clean_text(text: str) -> str:
    return text.replace("\ufeff", "").strip() + "\n"


def file_token_estimate(text: str) -> int:
    # Keep the estimate simple and deterministic for local generation.
    return round(len(text) / 4)


def build() -> None:
    manifest_text = clean_text(MANIFEST_PATH.read_text(encoding="utf-8"))
    sections, root_docs = parse_manifest(manifest_text)

    parts: list[str] = []
    parts.append("# SM Product Documentation: Project Knowledge Bundle")
    parts.append("")
    parts.append("This file is a retrieval-optimized merged export for ChatGPT Projects or GPT Knowledge.")
    parts.append("It preserves canonical document order, stable identifiers, source paths, and section boundaries.")
    parts.append("")
    parts.append("## Retrieval Notes")
    parts.append("")
    parts.append("- Prefer answers from canonical docs before `sources/` evidence docs.")
    parts.append("- Cite answers with `doc_id` or `decision_id`, document title, and repo path.")
    parts.append("- Treat each `DOCUMENT START` / `DOCUMENT END` block as the authoritative boundary for one source file.")
    parts.append("- The canonical reading order is Product Foundation -> UX Research -> Product Design -> Decisions.")
    parts.append("")
    parts.append("## Bundle Index")
    parts.append("")

    for section in sections:
        parts.append(
            f"- `{section.section_id}` | {section.title} | base_path: `{section.base_path}` | tags: {section.tags}"
        )
        for doc in section.docs:
            parts.append(f"  - `{doc.entry_id}` | {doc.title} | `{doc.path}`")

    if root_docs:
        parts.append("- `ROOT` | Repository-level docs")
        for doc in root_docs:
            parts.append(f"  - `{doc.entry_id}` | {doc.title} | `{doc.path}`")

    parts.append("")
    parts.append("## Repository-Level Documents")
    parts.append("")

    for doc in root_docs:
        doc_path = REPO_ROOT / doc.path
        doc_text = clean_text(doc_path.read_text(encoding="utf-8"))
        parts.append(f"### DOCUMENT START | {doc.entry_id} | {doc.title}")
        parts.append("")
        parts.append(f"- kind: `{doc.kind}`")
        parts.append(f"- id: `{doc.entry_id}`")
        parts.append(f"- title: `{doc.title}`")
        parts.append(f"- path: `{doc.path}`")
        parts.append(f"- canonical_role: `repository_context`")
        parts.append(f"- estimated_tokens: `{file_token_estimate(doc_text)}`")
        parts.append("")
        parts.append(doc_text)
        parts.append(f"### DOCUMENT END | {doc.entry_id}")
        parts.append("")

    for section in sections:
        parts.append(f"## SECTION START | {section.section_id} | {section.title}")
        parts.append("")
        parts.append(f"- section_id: `{section.section_id}`")
        parts.append(f"- title: `{section.title}`")
        parts.append(f"- base_path: `{section.base_path}`")
        parts.append(f"- tags: {section.tags}")
        parts.append(f"- document_count: `{len(section.docs)}`")
        parts.append("")

        for doc in section.docs:
            doc_path = REPO_ROOT / doc.path
            doc_text = clean_text(doc_path.read_text(encoding="utf-8"))
            canonical_role = "decision_record" if doc.kind == "decision_id" else "canonical_doc"
            parts.append(f"### DOCUMENT START | {doc.entry_id} | {doc.title}")
            parts.append("")
            parts.append(f"- kind: `{doc.kind}`")
            parts.append(f"- id: `{doc.entry_id}`")
            parts.append(f"- title: `{doc.title}`")
            parts.append(f"- path: `{doc.path}`")
            parts.append(f"- section_id: `{section.section_id}`")
            parts.append(f"- section_title: `{section.title}`")
            parts.append(f"- canonical_role: `{canonical_role}`")
            parts.append(f"- estimated_tokens: `{file_token_estimate(doc_text)}`")
            parts.append("")
            parts.append(doc_text)
            parts.append(f"### DOCUMENT END | {doc.entry_id}")
            parts.append("")

        parts.append(f"## SECTION END | {section.section_id}")
        parts.append("")

    output = "\n".join(parts).rstrip() + "\n"
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Characters: {len(output)}")
    print(f"Estimated tokens: {file_token_estimate(output)}")


if __name__ == "__main__":
    build()
