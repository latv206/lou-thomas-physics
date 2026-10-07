# A2 FINAL DETECTIVE REPORT
Run: A2_FINAL_DETECTIVE_HARDENING_20260707_075631 · 2026-07-07 · claude-physics
Task: CLAUDE_CODE_A2_FINAL_DETECTIVE_ORGANIZE_AND_HARDEN_TASK_FINAL.txt (sha 2c72912c…44122f)

## Classification: FINAL_PASS

Final authoritative artifacts:
- A2_MANUSCRIPT_FINAL.tex — sha256 f8d1e2c3f03c0fd0d815732a51bd59a36c6929344ba94a2f49dd6413e6e39cbf
- A2_MANUSCRIPT_FINAL.pdf — 10 pages — sha256 8ec9410a06004270461fd8ab779f6e5158d1a9a66d33e84c9826b154c8ce45e5
- Source package BIH_VI_A2_FINAL_MANUSCRIPT_DELIVERABLE.zip — sha256
  4d118ccdcc5f2d91cb9794a9fcc3b183a853d1e48dba70352c974281ff4d8931 (hash-gate MATCH)

## Source package verification
Internal SHA256SUMS: 24/24 entries verified, 0 failures. Detective cross-check beyond the task:
the seven locked/reference inputs in the package are BYTE-IDENTICAL to the canonical accepted
data lock (A2_FINAL_DATA_LOCK_20260706_160748) — the upstream theory pass altered no locked
content.

## Hardening applied (allowed edits only, in A2_MANUSCRIPT_FINAL.tex)
1. Section 7 nomenclature block ADDED (hard envelope, K grid label + K_Sigma note, sealed G-S
   criteria, claim-bearing/non-claim-bearing rows, folded disposition — required meanings verbatim).
2. Section 8 contract-boundary sentence ADDED verbatim in the introduction boundaries paragraph.
3. Section 9 literature-scope note ADDED verbatim (LaTeX math adaptation of eta_H only) in Scope.
4. Reference [5] (Arroja–Tanaka) was in the bibliography but uncited — now cited at the
   boundary-terms mention in the instrument section (allowed edit: add real citations).
No other prose changes; locked files untouched (fatal hash rule verified after hardening AND after
compile, 7/7 unchanged).

## Compile (fresh, local — the FINAL_PASS basis)
Lou authorized a minimal toolchain install (durable artifact LOU_APPROVAL_tex_install_20260707.md).
MiKTeX 25.12 installed via winget; pdflatex x2 with -interaction=nonstopmode -enable-installer on
the hardened source: clean both passes — 0 undefined control sequences, 0 emergency stops, 0 fatal
errors, 0 unresolved references/citations, 0 rerun warnings; complete 10-page PDF with %%EOF
trailer. Full record: A2_MANUSCRIPT_FINAL_COMPILE_LOG.txt.

## Audits (all PASS)
- Numeric-literal drift (sec 11): PASS — approved rounded intervals
  [0.02230,0.03822]/[0.05507,0.05906]; 13 gates; hard grid 0.010:0.005:0.060; provisional
  {0.072,0.090,0.119}; counts match locked state (42/22/11/11/0/14/0) where stated.
- Forbidden-claim audit (sec 12): PASS — every occurrence of a forbidden term is a negation or
  the mandated "not a physical cliff" sentence; zero assertive forbidden claims. C4/C5/C6 appear
  only in the explicit non-use disclaimer.
- Citation status (sec 10): RESOLVED — 8 cited = 8 defined (thebibliography, no .bib needed),
  0 undefined, 0 uncited, 0 CITATION-TODO / THEORY-PASS-TODO markers. All eight references are
  real, correctly attributed publications.
- PDF inclusion audit (sec 14): PASS on the FRESH locally compiled PDF — allowed claim verbatim
  (×2), all four locked tables fully rendered (22 claim rows; 13 gates w/ values; family summary;
  all 14 G-FLAT rows flat_limit/False), "diagnostic/report-only" and the folded sentence verbatim,
  AND the hardening content rendered (nomenclature block, contract-boundary sentence,
  literature-scope note, [5] cited in body). Landscape-table text extraction partially truncates
  but rendered pages show full content (extraction limitation, non-failure per sec 14).
- Post-pass hash audit (sec 15): 7/7 locked inputs UNCHANGED (pre = post) across locked_inputs/,
  locked/, and manuscript_work/locked/.

## Historical note (SUPERSEDED stage — recorded for audit-trail completeness)
The first emission of this run (2026-07-07 08:02) was classified REVIEW_CANDIDATE_NOT_FINAL for
exactly one reason: no LaTeX toolchain existed on this host at that time, so the mandatory fresh
compile could not run (task section 13 cap). That state was SUPERSEDED the same morning: Lou
authorized the toolchain install, the fresh pdflatex x2 succeeded cleanly, and the classification
was upgraded to FINAL_PASS (ledger 2026-07-07T08:14:54). The earlier
_REVIEW_CANDIDATE_NOT_FINAL.zip remains on disk as the append-only record of that stage and is
superseded by the FINAL_PASS re-emit zip.

## Stale/superseded source inventory (marked in A2_FINAL_DETECTIVE_INVENTORY.csv, files untouched)
A2_MANUSCRIPT_THEORY_PASS_DRAFT.* (superseded by FINAL_DRAFT), embedded task files
CLAUDE_CODE_A2_MANUSCRIPT_FINALIZE_PROMPT.txt / CLAUDE_CODE_FINAL_MANUSCRIPT_TASK.txt (stale per
this task's supersession note; not executed), TeX build artifacts (.aux/.log/.out/.fls/.fdb_latexmk).
