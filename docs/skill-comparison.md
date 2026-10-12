# Does GenX Reloaded achieve its goal?

12 October 2026. **It produces useful, truthful and considerate outputs in the tested fictional tasks. The comparison does not establish broad superiority over a capable assistant without the skill, or improved human confidence, ATS acceptance or hiring outcomes.** Version 0.4.0 added a useful Workable cancellation warning. The comparison also exposed small usability costs shared by the skill versions, which prompted a focused 0.4.1 patch.

## What was compared

Six identical new requests were each executed using version 0.2.0, 0.3.0, 0.4.0 and no loaded skill: 24 fresh-context executions. Three one-fact input variants were then executed with 0.4.0, making 27 planned executions. After reviewing the results, three focused 0.4.1 executions checked the repair and a neighbouring verification request.

The [protocol](../evals/comparison-2026-10-12/protocol.md) and [criteria](../evals/comparison-2026-10-12/protocol.json) were frozen before execution. The [run index](../evals/comparison-2026-10-12/runs.json) links exact prompts, raw responses, wrappers and complete instruction snapshots. The historical source commits identify the tested bundles:

| Condition | Source commit |
| --- | --- |
| 0.2.0 | `e1c3dea714722e493e78cba8bb96d2e0074286d1` |
| 0.3.0 | `5d7501ef1cb52cb726ff924100fe24ac4dbe7e28` |
| 0.4.0 | `3a4d818afe8f6c76eb79a7f73f950383e8cd3d90` |
| No loaded skill | Same task, host instructions and available tools; instructed not to load reusable skills |

A historical version comparison tests a bundle of instruction changes. It does not isolate the causal effect of a single sentence. A changed candidate fact tests conditional behaviour; it is not a skill mutation.

## Same input, different skill versions

| Input and intended result | Observed outcome across conditions | What the mutation adds or costs |
| --- | --- | --- |
| Rejection fatigue; one small question, no homework | All four acknowledged the feeling, used the person's hotel-service example and asked one manageable question | No clear version advantage; no generational blame or imposed nostalgia |
| Stock-control rewrite; valuable 1997–2008 training, no ERP or savings | All four retained dates, four trainees and two sites, and separated genuine ERP and handover gaps | No clear factual advantage; skill answers added routine readiness/file-check commentary |
| Stop; private reasons excluded from a 45-word handover | All four preserved facts and omitted anxiety/spouse-care details | All three skill versions introduced future CV work that had not been agreed; no-skill ended with no further action. A conservative criterion issue, not an actual demand to work now |
| Workable received an old Easy Apply letter; Friday interview active | All four chose employer correction and kept the existing application | Only 0.4.0 explicitly explained that withdrawal cancels existing invitations. Earlier versions and no-skill gave a safe action but incomplete risk explanation |
| USAJOBS operations resume in October 2026; colleague recommends six pages | All four retrieved current two-page guidance, retained the possibility of relevant 2001 evidence and preserved the supplied entry details | Browsing let the general assistant and older skills reach the central answer; no demonstrated exclusive advantage from the new country card |
| Montreal Workday import corrupts a vocational qualification and language level | All four restored the original vocational title and B1/C1, kept older service experience and avoided Canadian-experience claims | No clear factual advantage; the no-skill response added a useful conditional form-category fallback |

All 27 planned outputs stayed within their requested word limits under the recorded counting convention. No critical factual, privacy or unsafe-action failure was observed in the saved answers. This is not a claim that every predeclared criterion was met: cancellation-risk omissions, incomplete origin/submission explanations and conservative pause findings remain recorded.

## Change one input fact, keep the skill fixed

| Fact changed under 0.4.0 | Appropriate change in output | Evidence retained |
| --- | --- | --- |
| Never used ERP becomes supervised SAP Business One stock entries, January–June 2025 | Adds the actual product, task, period and supervision; removes the no-ERP gap without claiming independent proficiency | Both employment periods, old training, four colleagues, two sites and no invented savings |
| Submitted application with Friday interview becomes an unsubmitted draft with no interview | Replace the draft's old letter and review it before submitting; support help is conditional on being unable to edit | No withdrawal, reapplication or imagined interview |
| French B1 becomes French C1; English remains C1 | Both language entries become C1; the B1-specific gap disappears and the next check shifts to saved form accuracy | Original qualification and historical periods; no guaranteed employer acceptance |

The three variants met their predeclared change criteria and the applicable format/factual constraints. [Raw outputs and developer assessment](../evals/comparison-2026-10-12/developer-assessment.json) make these transformations inspectable. Each is a single observation, not an estimate of reliability.

## A small, observed repair: 0.4.1

The patch changes three instruction files. A paused handover now contains only useful confirmed details and any already-agreed next action. Bounded text requests no longer require routine readiness and unperformed-file-check commentary. Requested verification and material unresolved issues still receive explicit notes.

| Focused check | Before, 0.4.0 | After, 0.4.1 |
| --- | --- | --- |
| Same pause request | 40 words, includes an unagreed next profile task | 35 words, confirmed facts and privacy preferences only |
| Same stock-control rewrite | 115 words, including routine check boilerplate | 85 words, facts and genuine gaps retained, boilerplate omitted |
| Neighbouring explicit verification request | New case, no before run | 57 words; factual check and unperformed independent/file/ATS checks clearly stated |

All three focused runs met their written checks. See the [repair protocol](../evals/comparison-2026-10-12/repair-protocol.json) and [assessment](../evals/comparison-2026-10-12/repair-assessment.json). The word reductions describe these particular answers; they are not a causal estimate. The full four-condition comparison was not rerun after the patch.

## Assessment and limits

The developer assessed every planned output before receiving the second assessor's findings. A fresh agent then assessed randomly ordered answers with condition labels and runtime paths removed. Its exact input and raw output, the condition mapping, and final adjudication are retained in the comparison folder. Residual wording/citation clues could reveal a condition; shared filesystem restrictions were instructed, not enforced. This is additional agent review, not independent human adjudication.

See [adjudication](../evals/comparison-2026-10-12/adjudication.md) for disagreements and [source checks](../evals/comparison-2026-10-12/source-check.md) for current primary-source corroboration. Raw generated citation tokens are retained for fidelity but are not durable public links.

One run per condition, unknown exact model/sampling parameters, strong explicit prompts, and variable actual browsing limit inference. All agents inherited the same host configuration and available tools; no-skill agents still received host skill-catalogue metadata. A no-skill condition here does not mean a bare model. Exact artifacts can be inspected; hidden provider state cannot be deterministically replayed.

These text trials do not cover live ATS tenants, generated CV rendering, assistive technology, longitudinal morale, employer decisions or real candidate privacy operations. The full installed skill has eight market cards and fourteen ATS cards; this comparison does not revalidate all of them. Earlier country/vendor trials remain in the [0.4.0 validation record](validation-v0.4.0.md).

## What to do next

Keep the skill's value proposition precise: reusable, sourced guidance; faithful handling of deep career experience; and controllable support. Prioritise the prepared, consented human usability work to learn whether the tone restores agency and the process reduces effort. Test real document outputs and authorised ATS surfaces where concrete problems arise. Broader models or repeated trials become useful when a specific reliability question warrants them. More synthetic pep talks alone would not establish emotional benefit.
