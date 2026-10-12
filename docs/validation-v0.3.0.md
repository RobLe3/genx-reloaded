# Validation record

Version 0.3.0, 12 October 2026. This release implements the first research-roadmap additions and records finite checks. The [0.2.0 record](validation-v0.2.0.md) and its initial failures remain historical evidence.

## Deterministic checks

**27 synthetic unit tests passed, no skips.** See [raw output](../evals/v0.3.0/unit-tests.txt) and [environment](../evals/v0.3.0/environment.json).

| Area | Cases | What was checked |
| --- | --- | --- |
| Existing document preflight | 15 | Extraction, phrase boundaries, DOCX observations, source preservation and output aliases |
| Evaluation recording | 8 | Raw artifact round trip, unknown metadata, no-skill control, tampering, unsafe paths, symlinks, overwrite refusal and blank outputs |
| Research records | 4 | Valid records, missing provenance/dates, unknown cases, duplicate claims and invalid roots |

The helpers ran locally on the recorded Linux/Python environment. No hosted CI, live ATS, OCR, visual document or accessibility result is claimed. The source-truth and behaviour assessments remain separate from data validation.

## Fresh agent executions

**Eight executions, five distinct fictional cases:** two 0.2.0 baseline runs, five 0.3.0 candidate runs, and one general-assistant comparison without the skill. See the [run index](../evals/v0.3.0/runs.json), [assessment](../evals/v0.3.0/assessment.md), and [protocol](../evals/protocol.md).

| Candidate task | Observation |
| --- | --- |
| Retail to stockroom coordinator | Retained older evidence and periods, kept ERP as a preferred gap, suggested bounded introductory learning |
| Stop and resume with low energy | Produced a short note without questions/tables and omitted private health/family reasons |
| Swiss references and AI question | Drafted approval-before-contact wording; distinguished Swiss scope from assumed EU rights |
| Suspicious opportunity | Prioritised protecting money and identity with no transaction or unapproved contact |
| German paragraph and English CV | Put the language explanation inside the paragraph; preserved qualification, B2 and neutral break |

No critical failure was observed in these five candidate responses under developer assessment. Both baseline responses also met the inspected task criteria. The general-assistant answer was useful but omitted one employment period under the catalogue's date-retention criterion. These single executions do not establish that 0.3.0 is more effective than 0.2.0 or a competent general assistant.

The candidate/control rubric existed before execution. The baseline assessment is retrospective because its two runs began before the formal catalogue/rubric was saved. No independent human adjudication occurred. Exact provider model and sampling settings are unavailable. All skill conditions have complete runtime snapshots and artifact hashes; no-skill comparison is explicitly marked. Integrity verification checks the saved records, not the correctness of their answers.

## Research and structure

The release adds 16 structured claim records and 36 authored fictional scenarios. Only five distinct catalogue cases were executed, not all 36. The record validator checks schema-like field requirements and case links; it does not validate source truth. The [search log](../research/search-log.md) records retrieval scope and failures, including missing original intervention methods and unavailable Lever documentation.

Repository validation checks 18 runtime files and their digests, version/metadata consistency, local Markdown targets and Python syntax. The skill-creator frontmatter check also passed. See [repository check](../evals/v0.3.0/repository-check.json) and [research check](../evals/v0.3.0/research-check.json). The candidate runtime inventory digest is `23b116683e5d41d72c807901621b25650a67103c487e0c71edea391dc0e9210b`, using the evaluation snapshot algorithm. This differs from a digest of manifest.json because its path base and encoding contract differ.

## Remaining limits

Human usability, emotional effects, assistive-technology operation, hiring outcomes, employer configurations, further languages/countries and cross-model behaviour remain unestablished. The country cards are limited starting points, not a comprehensive legal review. Study materials are prepared but no participants were recruited. No real CV, application, employer contact or purchase was involved.

See [implementation status](../research/implementation-status.md) for every roadmap task's delivered artifacts and outstanding research gate. Further work should resolve those actual gaps rather than repeat successful synthetic checks without a concrete reason.
