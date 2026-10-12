# Validation record

Version 0.4.2, 12 October 2026. **A local DOCX privacy-review false-negative was fixed. No substantive assistant advantage over no-skill or 0.4.1 was established.** The entry skill is unchanged. See the [correction report](docx-comment-check.md) for the development observations, frozen comparison, adverse details and release decision.

## Changed behaviour and local checks

The helper now detects stored Word comments and comment anchors, without copying comment contents or authors into findings or body extraction. It recognises standard and content-type-declared parts, applies bounded XML inspection, and fails honestly on malformed, oversized or missing declared parts. The existing layout reference explains deletion on a submission copy and rechecking; no additional runtime module was added.

Two synthetic commented excerpts changed from `no_local_flags` under released code to `review_needed`; a clean excerpt remained unflagged. Body extraction hashes matched, and the helper preserved source bytes. This is local verification, not a Word UI, complete metadata audit or ATS test. The [helper comparison](../evals/docx-review-2026-10-12/helper-comparison.json) records those observations.

The full unit suite passed **33 tests, no skips**, including six added helper tests. The helper subset has 21 tests. [Released-code failures](../evals/docx-review-2026-10-12/released-helper-tests.txt) preserve the original omission and the newly specified reporting contract; the [release suite](../evals/docx-review-2026-10-12/unit-tests.txt) records the final result. Repository, research and frontmatter checks also passed. Their scope is structure and consistency, not candidate or hiring effectiveness.

## Fair comparison and attribution

Six development executions inspected three diverse requests with no GenX runtime and 0.4.1. Nine reserved executions then compared no-skill, 0.4.1 and the frozen candidate: two repetitions on a fresh commented excerpt and one clean neighbouring case per condition. All had the same raw material, host model configuration, ordinary document tools and permitted browsing. Exact model identity/sampling remain unknown.

The condition-label-blinded assessor found nine substantive pairwise ties across three sets. Candidate/no-skill and candidate/0.4.1 each had three ties, no wins and no losses. No critical factual, application-disclosure or false-certification failure was observed. Copy/recheck wording omissions and thumbnail-layout overstatement remain recorded; original actions were not independently verified. The developer accepted the ties and refined its initial action-verification judgment. This is agent assessment, not independent human review or measured user correction effort.

All fifteen raw task outputs, exact runtime snapshots, criteria, blinding map and adjudication remain in the [run index](../evals/docx-review-2026-10-12/runs.json). One post-output provenance receipt and one reviewer execution are counted separately. The runtime inventory digest is `b8bcba926fa9b0920db632bd3c5eae586abf3bd6a289159e5bc2dfe1440c111d`, identical to the frozen candidate. The original 0.5.0 proposal and its failed gain gate remain unchanged.

## Historical records and remaining limits

The catalogue contains 73 authored cases and the research register 49 claims. Thirty-eight distinct catalogue cases have recorded task executions across the preserved series; none of these counts is a reliability or acceptance rate. The new cases are now exposed material, not future unseen holdouts.

The [0.4.1 record](validation-v0.4.1.md), [application-gain study](application-gains.md), [historical-version comparison](skill-comparison.md), and earlier [0.4.0](validation-v0.4.0.md), [0.3.0](validation-v0.3.0.md) and [0.2.0](validation-v0.2.0.md) records retain prior negative findings and coverage limits.

Small synthetic excerpts and instructed read boundaries limit generalisation. The helper is not a complete metadata/privacy inspector; style inheritance, other package information and visual output still need separate review. Resolved-thread status was generated as OOXML, not exercised in Word. No real candidate data, human usability measurement, employer contact, external upload, live ATS or hiring outcome was involved.

New generated input packages remain outside Git; generator, hashes and observations are retained. Previously withheld GX-64 attachments were neither available for inspection nor republished. Their publication still requires the document-level permission described in the [historical publication note](../evals/gains-2026-10-12/publication-note.md). Consented real CV/vacancy pairs and authorised ATS environments remain the dependencies for stronger outcome evidence.
