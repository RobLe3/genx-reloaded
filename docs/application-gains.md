# Prospective application-gain comparison

12 October 2026. **The proposed expansion did not demonstrate a substantive advantage over the no-skill condition. The study retained 0.4.1.** All 35 execution records are available, including the unpromoted candidate. This result is useful evidence against adding redundant instructions; it is not proof that the skill has no value in other settings.

Later update, 12 October 2026: [0.4.2 fixes a separate local Word-comment check](docx-comment-check.md). It does not promote this proposal or change this study's failed gate.

## What was tested

The candidate added an application-preparation reference and two entry-point instructions. It made requested outputs and fields explicit, separated real eligibility gaps from hidden evidence, checked overlapping experience periods, and reviewed the final application packet. See the [proposed reference](../evals/gains-2026-10-12/proposal/application-readiness.md), [entry-point diff](../evals/gains-2026-10-12/proposal/entrypoint.diff) and [frozen candidate](../evals/gains-2026-10-12/candidate-freeze.json). The provisional 0.5.0 label in snapshots was never released.

The [protocol](../evals/gains-2026-10-12/protocol.json) and [nine cases](../evals/gains-2026-10-12/cases.json) were written before these executions. Three development cases ran with 0.4.1 and no GenX runtime, followed by three candidate checks. Six reserved cases then ran twice per condition, producing 24 reserved answers. Both conditions could use ordinary document/PDF skills, browsing and the same host capabilities. This avoids crediting GenX Reloaded merely for having access to a document tool.

The primary endpoint was consequential correction work before the requested application could be used. A substantive win required avoiding a consequential omission or error without introducing a comparable problem. Extra caveats, optional dates and cosmetic preferences alone were ties. The predeclared project gate required wins in both repetitions of at least three of six families, no critical failure and no substantive loss. This was a release decision rule, not a statistical significance test.

## Results

| Reserved task | Concrete behaviour observed | Result across two repetitions |
| --- | --- | --- |
| NZ reporting duration, GX-63 | Both calculated five non-overlapping Power BI years and two management years, excluded learning and mentoring, and produced 60-word profiles | Two ties |
| UK maintenance DOCX, GX-64 | Both produced legible one-page files below 1 MB with correct dates, useful older evidence, Excel and truthful handover wording | Two ties |
| AU quality documentation, GX-65 | Both retained the 2003 evidence, covered the four essentials and distinguished coordination from ownership and awareness training from certification | Two ties |
| AU PageUp draft correction, GX-66 | Both corrected the actual job draft, supplied a supported statement and preserved the account with a confirmation check | Two ties |
| CA inventory screening, GX-67 | Both answered No to the missing management requirement and labelled sandbox learning accurately; candidate bullets retained more role/date context | Two ties |
| UK anonymous packet, GX-68 | Both supplied all three bounded fields, removed identifying details and retained useful historical examples | Two ties |

The condition-blinded assessor recorded **12 ties, no substantive wins or losses, and no critical failures**. Across 60 criterion ratings per condition, the candidate received 58 pass and 2 partial ratings; the no-skill condition received 52 pass and 8 partial ratings. These checklist totals are not ATS scores or acceptance probabilities. The six-rating difference did not meet the more meaningful correction-work endpoint. The release gate failed: zero qualifying families against the required three.

The remaining partials were explicit desirable-SAP wording, optional date/context details, one omitted alternative next step, and an additional mandatory-task check that both PageUp conditions omitted. Known field defects were still addressed. No invented missing field was assumed. One baseline CV opening included obvious contact placeholders when no identity had been supplied; the assessor recorded the necessary completion/removal but did not treat a top-of-CV template as a falsely finished file. All four actual DOCX packages and rendered pages were inspected locally. The fictional invalid email requires replacement in both conditions, and both flagged it.

See the [raw blinded assessment](../evals/gains-2026-10-12/blind-review/assessment.json), [label mapping](../evals/gains-2026-10-12/blinding-map.json) and [decoded results and maintainer decision](../evals/gains-2026-10-12/assessment.json). The maintainer accepted all twelve tie judgments. Literal criterion coverage and substantive usability were kept separate rather than relaxing the gate after seeing the results.

## Why the candidate was not promoted

The dated inventory bullets looked like a possible benefit. Two additional, explicitly adaptive executions used the released 0.4.1 on that known case. Both already retained the roles and dates while meeting the factual and screening requirements. The [follow-up protocol](../evals/gains-2026-10-12/attribution-protocol.json) and [assessment](../evals/gains-2026-10-12/attribution-assessment.json) preserve this result. These follow-ups are not new reserved cases or an isolated causal ablation.

The longer module therefore had no demonstrated incremental value sufficient to justify shipping it. It remains an experimental artifact. No second corrective candidate was produced because the review found no consequential candidate defect needing a repair. The original gate and all negative observations remain intact. The installed instructions were verified against the unchanged 0.4.1 source.

## Evidence and limits

The [run index](../evals/gains-2026-10-12/runs.json) contains 33 planned executions and two adaptive follow-ups. Every run has its raw request, complete saved response, exact wrapper and runtime snapshot where applicable. [Integrity checks](../evals/gains-2026-10-12/integrity-check.json) cover the 35 records and 15 document-evidence files. The reviewer received shuffled A/B pairs and inspected the actual documents. Exact reviewer instructions, pair copies and output are archived; the mapping locates the corresponding execution records. Generated attachment bytes are withheld after automatic approval review; their hashes and local findings are preserved. See the [publication boundary](../evals/gains-2026-10-12/publication-note.md). Raw assessor pair inputs are archived as text with historical paths.

This is a small synthetic evaluation using one available host model with unknown exact model and sampling metadata. Author-created reserved cases were frozen, but were not independently secret. The same developer designed the candidate and knew the task families. Host instructions and catalogue descriptions were still visible in the no-GenX condition; agent read boundaries were instructed rather than filesystem-enforced. Wording could reveal conditions to the label-blinded assessor. Full execution tool transcripts and human adjudication are unavailable. Source retrieval was not controlled, and the assessor did not independently verify the PageUp citation tokens.

There were no real CVs, employer contacts, submissions, withdrawals, participant measurements or live ATS tests. A correct No on a mandatory requirement can prevent a dishonest application while reducing its chance of progressing; this is not an optimisation failure to hide. No result here establishes interview uplift, ATS acceptance or reduced age discrimination.

## The next informative step

Use consented, anonymised CV/vacancy pairs whose important evidence is not already neatly enumerated in the request. Have candidate and recruiting reviewers assess factual corrections, effort, clarity and usefulness without condition labels. Separately, use an authorised ATS test environment to measure extraction and field handling. Keep those intermediate outcomes distinct from a prospective hiring-outcome study. The [research note](../research/writing-and-application-evidence.md) and [candidate study kit](../research/candidate-study-kit.md) define the evidence boundary.

More synthetic repetitions of these already successful tasks would not establish higher acceptance rates. New runtime work should start with a concrete failure or new evidence, rather than a requirement to produce a winning benchmark.
