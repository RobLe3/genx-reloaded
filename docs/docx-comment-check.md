# A local Word comment check, 0.4.2

12 October 2026. **The offline checker now flags retained Word comments without putting their text or authors into its findings.** Previously, it returned `no_local_flags` on two synthetic excerpts containing private drafting comments, including a resolved thread. This is a verified local helper correction, not a demonstrated improvement in assistant advice or hiring outcomes.

## What led to the change

Three development requests covered untidy retail notes with a corrected title, overlapping management/training periods, and a Word audit. Each ran in fresh contexts with no GenX runtime and released 0.4.1. The writing answers retained the relevant older evidence, respected the corrections and counted formal management accurately. Both document agents found the private comment using ordinary tools. These observations did not justify another writing module.

The released helper inspected visible body text, styles and headers/footers, but not stored comment parts. It missed the comment even though the agent could find it separately. [Microsoft's inspector guidance](https://support.microsoft.com/en-gb/office/collab-files/remove-hidden-data-and-personal-information-by-inspecting-documents-presentations-or-workbooks?nochrome=true) distinguishes visible content from retained review information. Its [Word for the web guidance](https://support.microsoft.com/en-gb/word/mark-comments-as-done) confirms that resolving a thread does not delete it. Both were inspected on 12 October 2026; no live Word workflow was tested.

The patch changes the helper and its existing layout reference, not the entry point. It counts stored comments and anchors, recognises standard and content-type-declared comment parts, includes them in the XML size check, and reports a review observation. It does not delete anything or treat comment text as application evidence. It explicitly remains incomplete as a metadata/privacy audit.

## Verified helper result

| Synthetic input | Released 0.4.1 | 0.4.2 candidate |
| --- | --- | --- |
| Ordinary private reviewer comment | No local flags | Comment review flag |
| Retained comment with resolved-thread metadata | No local flags | Comment review flag |
| Clean career excerpt | No local flags | No local flags |

Body extraction hashes were identical before and after; comment text and authors were absent from extraction and findings, and source bytes were preserved during the local checks. Six added tests cover stored/alternate parts, dangling anchors, empty parts, malformed XML, excessive size and missing declared parts. The full suite passed 33 tests with no skips. The same 21 helper tests against released code recorded six assertion failures and one missing-field error, including the newly specified reporting contract. Those counts are not candidate outcome measures. See the [helper comparison](../evals/docx-review-2026-10-12/helper-comparison.json) and [test records](../evals/docx-review-2026-10-12/unit-tests.txt).

## Three-condition assistant result

Before reserved execution, the candidate, criteria and fixture generator were frozen. A fresh commented excerpt ran twice per condition; a clean neighbouring excerpt ran once. All conditions received the same source, request, inherited host model and ordinary tools. The controls were no GenX runtime and exact released 0.4.1. Nine reserved executions followed six development executions.

A fresh condition-label-blinded agent found **nine pairwise ties across three sets**, including three candidate/no-skill ties and three candidate/0.4.1 ties. Every condition identified the retained comment in both repetitions. No critical factual, application-disclosure or false-certification failure was observed. Copy/recheck omissions in controls and an overly broad thumbnail-layout statement remain in the assessment; a post-output receipt established that the latter used Quick Look, not full page rendering. Original execution actions were not independently verified. The developer accepted the tie judgments and retained those limitations.

The [protocol](../evals/docx-review-2026-10-12/protocol.json), [run index](../evals/docx-review-2026-10-12/runs.json), [blinded review](../evals/docx-review-2026-10-12/blind-review/assessment.json) and [adjudication](../evals/docx-review-2026-10-12/assessment.json) preserve the evidence. One diagnostic provenance receipt and one assessor execution are separate from the fifteen jobseeker-task executions.

## Release decision and limits

Ship the narrow correction as 0.4.2 because a reproducible helper defect was fixed without changing extraction on these inputs. Do not attribute an assistant advantage to it. The rejected 0.5.0 expansion stays experimental; its original failed gate is unchanged.

The records are synthetic, small and author-created. Exact model identity/sampling and complete tool transcripts are unavailable. Read boundaries were instructed, not filesystem-enforced, and prose can reveal conditions. Generated input packages stay outside Git; their generator, hashes and package findings are available, but exact ZIP bytes vary when regenerated. No prior withheld attachment was accessed or republished. No real CV, human study, employer contact, external upload, live ATS or hiring outcome was involved. Actual correction effort and privacy benefit remain unmeasured. More realistic work requires consented CV/vacancy pairs; parser claims require an authorised ATS environment.
