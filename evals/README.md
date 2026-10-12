# Agent task trials

For version 0.4.1 use the [evaluation protocol](protocol.md), [68-case catalogue](catalogue/cases.json), and the [current validation record](../docs/validation.md). See the [matched version comparison](../docs/skill-comparison.md), [frozen protocol](comparison-2026-10-12/protocol.md) and [run index](comparison-2026-10-12/runs.json). The earlier trials below remain historical evidence. New runs preserve exact instruction snapshots and raw artifacts. Their integrity checks do not grade behavioural quality.

These are qualitative behavioural checks with fictional candidates. They do not measure interview probability, human wellbeing, universal model reliability, or real ATS acceptance.

## Prospective application-gain study

The [new report](../docs/application-gains.md), [frozen protocol](gains-2026-10-12/protocol.json) and [35-run index](gains-2026-10-12/runs.json) preserve 33 planned executions and two adaptive follow-ups. Twelve condition-blinded pair judgments were ties. Actual DOCX artifacts and rendered pages were inspected locally; [attachment publication is restricted](gains-2026-10-12/publication-note.md), with hashes and findings preserved. The 0.5.0 candidate was not promoted; released 0.4.1 remains unchanged. Cases GX-60 to GX-68 are now exposed evaluation material, not unseen holdouts for future tuning.

## Method

Give a fresh-context agent the skill path and one raw prompt from `prompts/`. Do not provide the diagnosis, expected answer, prior output, or evaluation commentary. Ask it to produce the requested candidate-facing response. Keep candidate data fictional and perform no live applications.

Inspect factual fidelity, instruction following, optional support, privacy, historical value, role mapping, and whether claims about tools or checks match actions. Preserve raw responses, adverse observations, and any follow-up changes. The developer who made the changes assessed these trials. The October comparison additionally has a condition-blinded agent assessment and explicit adjudication; neither is an independent human study.

## Recorded tasks

| Prompt | Focus | Record |
| --- | --- | --- |
| [Conflicting records](prompts/conflicting-records.md) | Explicit correction, disputed percentage, old training evidence, introductory learning, embedded instructions | [Response](results/conflicting-records.md) |
| [German career change](prompts/german-career-change.md) | Mixed languages, private break, qualification translation, real language gap, desired responsibility | [Initial](results/german-career-change-initial.md), [rerun](results/german-career-change-rerun.md) |
| [Low energy and accessibility](prompts/low-energy-accessibility.md) | One question, unsuitable nostalgia prompts, disclosure control, no evidence lecture | [Response](results/low-energy-accessibility.md) |

See [validation](../docs/validation.md) for the assessment and remaining limits. Earlier baseline trials have summaries only and are not counted as new raw-output records.

## Useful future cases

These have not been run as a systematic suite: a scanned CV, an unavailable job URL, a public-sector complete-history form, a regulated-role license requirement, a long academic CV, a source conflict about employment dates, a request to hide a gap, and behaviour across different models. Keep new prompt material separate from assessor notes.
