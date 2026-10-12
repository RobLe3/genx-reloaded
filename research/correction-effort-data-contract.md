# Correction-effort data contract

This contract turns the participant protocol into a repeatable measurement workflow. Version 1 covers the twelve-person baseline, six-to-eight-person candidate pilot and 36-to-120-person confirmatory comparison. Discovery notes remain qualitative and private.

The study record stays in encrypted private storage. Use coded participant, output, task and reviewer IDs. Keep the condition key separate until both reviews and any severity adjudication are complete. Do not include names, contact details, document text, quotations, consent records or free-text participant history.

## Record shape

The root records the study identity, phase, date, freeze and blinding checks, the optional accessibility time exception, six regression results and the output rows. Each output records:

- coded output, participant, packet and task-family IDs;
- condition and counterbalanced order;
- elapsed seconds, completion status, deliverable completion and blocking-question count;
- optional 1-to-7 effort, representation and disclosure-control responses;
- two distinct coded reviewers; and
- distinct correction-action IDs with both blinded severity ratings and the adjudicated severity.

Allowed severities are `critical`, `consequential`, `minor` and `preference`. The primary outcome counts adjudicated consequential actions. A packet is usable without critical or consequential correction only when the requested deliverable is complete and neither severity is present.

The validator requires one output per condition for each participant, different packets and task families within a participant, valid sample bounds and two reviewers. Confirmatory records also require a frozen protocol, balanced task-family assignment and counterbalanced condition order.

## Commands

```bash
python scripts/correction_effort.py validate private/correction-effort/baseline.json
python scripts/correction_effort.py analyse private/correction-effort/baseline.json
python scripts/correction_effort.py power private/correction-effort/pilot.json \
  --iterations 5000 --seed 20261012
python scripts/correction_effort.py analyse private/correction-effort/confirmatory.json
```

Validation errors identify array positions rather than private identifiers. Analysis output is aggregate. Store redirected output in the private study directory until the publication review is complete.

## Frozen confirmatory calculation

For each participant, calculate candidate-minus-control differences in adjudicated consequential corrections. Report the paired mean reduction against no runtime and released 0.4.2. Use one-sided normal tests on the participant-paired differences, Holm-adjust the two p-values and report Bonferroni simultaneous one-sided 95% upper bounds.

The primary gate passes when both comparisons have a mean reduction of at least 0.5 action per task, adjusted `p < 0.05`, and a simultaneous upper bound below zero. The aggregate release gate also applies the zero-correction-rate, critical-error, time and regression requirements from the protocol.

The pilot power command resamples complete participant blocks. This preserves the two paired contrasts, their within-participant relationship and the task assignments observed in the pilot. It searches from 36 through 120 completers and selects the first size reaching 80% estimated power for the complete primary gate. Obtain a quantitative-methods review before confirmatory recruitment; record any approved method change before collecting confirmatory data.

## Synthetic rehearsal

The unit suite generates balanced fictional baseline, pilot and confirmatory records. It verifies a passing gate, blocking critical and time results, malformed reviews, repeated packets, sample-size simulation and identifier-safe error output. These fixtures contain no participant data.
