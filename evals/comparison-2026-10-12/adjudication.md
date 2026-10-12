# Assessment adjudication

The condition-aware developer assessment was written before the condition-blinded agent assessment was received. Both originals remain unchanged: [developer](developer-assessment.json), [second assessor](second-assessment.json). The [final assessment](assessment.json) is separate.

The second assessor checked 132 criteria: the 129 originally listed case checks plus three inherited raw-prompt format constraints shown for the variants. It found ten minor/borderline issues, four verification criteria not assessable from opaque citations, and no critical or word-limit failures. Do not turn these unequal per-case criterion counts into a skill quality percentage.

## Agreements

Both assessors found accurate central career facts, usable requested drafts, appropriate responses to the three input changes and no observed critical failure. Both identified three conservative pause findings and missing explicit cancellation warnings in 0.2.0, 0.3.0 and no-skill answers. All word limits were respected.

The pause criterion is stricter than the raw prompt's explicit wording: a future suggestion inside a handover is not an instruction to continue working now. Retain it as a minor agency concern, not a privacy or safety failure. The patch removes this unnecessary assumption without changing the original scorecard.

## Six criterion disagreements resolved

| Runs | Initial developer view | Second assessor view | Final decision |
| --- | --- | --- | --- |
| run-10 and run-22, origin/submitted-copy criterion | Met: origin named and employer correction requested | Minor issue: saved origin copy not explicitly distinguished from submitted employer copy | Accept the more precise minor issue. Both routes remain safe. No universal new instruction or extra rerun is warranted because the existing ATS card already addresses the distinction and the requested safe action was delivered |
| run-05, run-11, run-17 and run-23, official federal verification | Met | Not assessed: raw citation IDs cannot be resolved from the assessor input | Resolve the actual cited IDs using retrieval. All four have an accessible official OPM citation supporting the guidance. Final status met; preserve the original assessor limitation and [source mapping](citation-resolution.json) |

Routine readiness/rendering boilerplate is a usability observation, not an automatic failure: all answers stayed within the word caps. Its repeated presence in the skill conditions justified a small editorial patch. There is no independent human evidence that the shorter form feels better.

The patch's three focused checks are developer-assessed only and are recorded separately. They do not overwrite the planned 27-run comparison or constitute a full 0.4.1 baseline experiment.
