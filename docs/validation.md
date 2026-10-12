# Validation record

Version 0.4.0, 12 October 2026. This release adds five country cards and scoped ATS troubleshooting. The [0.3.0 record](validation-v0.3.0.md) and [0.2.0 record](validation-v0.2.0.md), including earlier adverse observations, remain historical evidence.

## Focused behaviour checks

**Nine fresh-context executions, nine distinct fictional cases, GX-37 to GX-45.** Each met its prewritten criteria under developer assessment; no critical failure was observed. See the [assessment](../evals/v0.4.0/assessment.md), [run index](../evals/v0.4.0/runs.json) and [protocol](../evals/protocol.md).

The tasks cover US federal length/details, Belfast CV and jurisdiction, Canadian Workday qualification/language correction, an Australian APS pitch through PageUp, NZ referees and Recruitee extraction, a Workable correction with an interview active, SuccessFactors missing fields, Greenhouse/Ashby mechanism distinctions, and Personio inferred attributes. Some responses were verbose and used formal completion labels; these observations are retained in the assessment.

All runs preserve raw prompts/responses, exact wrappers and complete runtime snapshots. The snapshot inventory digest is `170dda31dd23c5b93c2d1b46199a97d7a3fc0f1133afe15e8709c7e8d45645dd`. The runtime remained unchanged during execution. Model/sampling metadata is unknown, and complete tool transcripts are not archived. Agents shared a filesystem but were instructed to read only the request, skill and relevant references. No independent contamination or human adjudication claim is made.

No baseline/control condition was repeated in this release. These observations do not establish superiority, human usability, live ATS compatibility, fairness or hiring uplift. Six of the fourteen vendor cards were not directly exercised. All five new countries were exercised once; legal and recognition coverage remains narrow.

## Deterministic checks

**27 unit tests passed, no skips**, covering the unchanged preflight, evaluation-recording and research-record helpers. See [raw output](../evals/v0.4.0/unit-tests.txt) and [environment](../evals/v0.4.0/environment.json). The skill-creator frontmatter check passed.

The [research check](../evals/v0.4.0/research-check.json) validates the structure of 46 claim records and their links into 49 authored cases. The [repository check](../evals/v0.4.0/repository-check.json) checks 38 runtime files, digests, metadata, local links and Python syntax. The [record integrity check](../evals/v0.4.0/integrity-check.json) verifies the nine saved executions. These checks do not grade evidence truth or live product behaviour.

## Research boundaries

The release adds 30 scoped source records, for 46 total, and 13 fictional scenarios, for 49 total. Only nine new cases were executed. Across the 0.3.0 and 0.4.0 catalogue runs, 14 distinct cases have recorded executions, not all 49. Earlier pre-catalogue trials remain separately documented.

Fourteen product cards include retrieval-limited Lever and older-release Taleo coverage. Australian AHRC full-page retrieval was unavailable. Product-specific limits and correction behaviour need current verification before consequential use. See the [coverage map](../research/ats-coverage.md), [search log](../research/search-log.md) and [implementation status](../research/implementation-status.md).

No participant research, real CV, employer contact, live application, purchase, assistive-technology session or hiring outcome was involved. Further work should target these information gaps rather than inflate synthetic test counts.
