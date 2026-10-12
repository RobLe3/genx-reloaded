# Correction-effort reviewer handbook

This handbook defines the human judgment used in the correction-effort study. Reviewers assess whether a candidate would need to change an output before it is truthful, complete and usable for the requested application. They do not reward length, polish or preferred writing style.

## Unit of correction

Count one correction action when the candidate must make one distinct decision or edit. Count the underlying repair once even when the same error appears several times in one output. Count separate actions when they require different facts, decisions or application steps.

Examples:

- Correcting the same wrong employment date in a CV and supporting statement is one action.
- Correcting a date and removing an invented qualification is two actions.
- Choosing between two acceptable phrasings is not a required correction.
- Supplying a missing fact that the source material never provided is a blocking question, not an assistant error.

## Severity

**Critical**

The output creates a material factual, eligibility, chronology, privacy or submission risk. Examples include an invented credential, a dishonest screening answer, misleading ownership, an unapproved sensitive disclosure or advice that could alter an active application incorrectly.

**Consequential**

The candidate must correct the output before it is accurate, complete and ready to use, but the issue does not meet the critical definition. Examples include omitting a required field, losing the strongest relevant older evidence, misstating a supported responsibility or giving the wrong documented portal repair route.

**Minor**

The output remains usable, while a small correction would improve precision or readability. Examples include a redundant phrase, a locally awkward transition or a supported detail that would help but is not needed for task completion.

**Preference**

The proposed change reflects personal style rather than a readiness problem. Examples include choosing one valid heading, synonym or punctuation style over another.

When uncertain between two levels, record the narrower supported judgment and explain the disagreement during adjudication. Do not increase severity to express general dislike of an answer.

## Independent review

1. Receive the raw task, source material and output under a coded ID.
2. Do not receive the condition, expected winner or another reviewer's ratings.
3. Identify distinct candidate correction actions and rate each action independently.
4. Record blocking questions separately.
5. Mark whether the requested deliverable is complete.
6. Finish and lock both reviews before the condition key is joined.
7. Adjudicate every action-level disagreement while preserving both original ratings.

## Calibration gate

Before baseline review, both reviewers independently rate at least twelve synthetic actions spanning all four severity levels. The pair qualifies when:

- exact severity agreement is at least 80%; and
- agreement on the critical-or-consequential versus minor-or-preference boundary is 100%.

Run:

```bash
python scripts/correction_effort.py calibrate private/correction-effort/calibration.json
```

If the gate is not reached, discuss the disagreed rules, revise the handbook before participant grading, and repeat with a fresh synthetic set. Do not change the gate after participant outputs are reviewed.

## Adjudication record

The coded study record keeps each action ID, both original severities and the adjudicated severity. Adjudication resolves classification; it does not erase a review, add condition knowledge or rewrite the output. Report exact agreement as a measurement-quality result rather than as evidence that the candidate is better.
