# Code And Privacy Review

Review date: October 7, 2026. Scope: this distribution and the source artifacts selected from the supplied Theories collection and matching recovered Hub packages. This is an AI-assisted static review with targeted execution tests, not a malware certification or a full independent scientific audit.

## Findings And Disposition

| Finding | Consequence | Treatment in this edition |
|---|---|---|
| A2 source discovers a Hub and appends a ledger | Direct execution can modify an operational workspace | Source retained as `.py.txt`; supported wrapper uses a fresh private output tree and checks the sealed source hash |
| Legacy downloaders use HTTP requests; one downloader runs at import | Unexpected network access and unpinned inputs | Archived as non-executing text; excluded from supported entry points |
| C-series scripts and PowerShell wrapper assume fixed work areas | Non-portable paths and possible overwrites | Private paths redacted; source reference only, not claimed runnable |
| Conscious Physics notebooks include package installs, file writers, random masses/lags, and iterative replacement code | Misleading results and unintended environment/file changes if blindly run | Outputs removed; all code cells displayed as fenced text in Markdown cells; prototype status stated prominently |
| A2 embedded output hashes are generated before final JSON rewrites | Some historical embedded hashes are stale by construction | No historical numerical code rewrite; non-circular outer checksums added for final distribution bytes |
| RNSF runner executes at import and writes to an old fixed path | Surprise computation and non-portable output | Guarded runner, copied into fresh output folder; numerical routines unchanged |
| Historical reports contain stronger scientific claims than the evidence establishes | Numerical checks can be mistaken for derivation or discovery | New overview, evidence index, and claims boundary override release-level interpretation; historical claims remain identifiable as such |

## Checks Performed

The review enumerated Python imports and file/process/network-related calls, parsed Python sources, inspected the PowerShell launcher and notebook cells, and searched for common credential formats, credential assignments, private drive paths, email addresses, and employer/project identifiers. DOCX XML relationships, embedded-object indicators, PDF metadata/action dictionaries, and image metadata were inspected as well.

No unexplained upload endpoint, credential-harvesting routine, destructive shell command, obfuscated executable payload, or discovered credential was identified in the reviewed material. That is a scoped review result, not a guarantee that no defect or private content can exist.

The only supported process launches are explicit calls to the current Python interpreter with `shell=False`, for the reviewed numerical scripts. No Git hooks, GitHub Actions workflows, automatic installers, executable binaries, macros, or credentials are included as part of this distribution's execution design.

The integrity tests include negative controls for modified, missing, extra, duplicate-manifest, and path-traversal cases. Numeric comparisons reject non-finite values and meaningful numerical drift. Recorded rerun evidence is in `docs/verification/`.

## Privacy And Document Handling

Public exports omit private conversations, unrelated company work, local absolute source paths, contact details, old operational manifests, and two observational input files whose redistribution rights were not established. Original source files and backups were not edited.

DOCX author/company/custom metadata and comments were cleaned in copies. Namespace declarations and document structure were checked after rewriting. PDF page text and page counts were compared with source PDFs after metadata and annotation removal. In edition `2026.10.07.1`, three PDF title-page bylines were additionally sanitized: public author credit was standardized to Lou Thomas, personal affiliation locations were removed, and unfilled contact templates were removed. The affected PDFs were rendered and compared page by page; pixels outside the changed byline/contact regions and all other pages were unchanged. The repository source map records original and public hashes so a sanitized export is never misrepresented as byte-identical to its source.

The unfilled email templates in two archived RSI PDFs were removed. A damaged alternative animation was excluded; every frame of the retained animation was successfully decoded. Public author credit and research review history remain intentional disclosures. Image metadata and contact sheets were reviewed, but this was not an exhaustive OCR or steganography examination. The updated privacy review is recorded in `docs/verification/publication_privacy.json`.

DOCX layout could not be re-rendered because LibreOffice was unavailable. Their XML/structure checks are not visual acceptance. Existing PDFs are retained as reading copies where supplied; no claim is made that all editable manuscripts were newly typeset or visually reviewed page by page.

## Remaining Risk

Renaming historical text sources makes them executable again. Dependencies can contain vulnerabilities outside this review's scope. Copyright ownership, employer agreements, patent consequences, research novelty, and correctness of the physical reductions require appropriate human judgment. The package does not silently turn any of those into a passed gate.
