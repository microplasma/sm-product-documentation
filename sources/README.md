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
