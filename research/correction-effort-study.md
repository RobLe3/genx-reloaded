# Candidate correction-effort study

## Decision this study supports

This programme determines whether a focused GenX Reloaded candidate reduces the work a candidate must do before an application is accurate, complete and ready to submit. It compares the candidate with both a capable general assistant and released 0.4.2.

The machine-readable protocol is in [`correction-effort-study.json`](correction-effort-study.json). Repository validation checks its fixed structure and thresholds. Participant records, contact details, consent records, private documents and session recordings never belong in Git.

## Launch gate

Before recruitment, create `private/correction-effort/operations.json` in the ignored private directory. It must name the study owner, private encrypted storage location, access list, participant contact route, recruitment source, withdrawal contact, compensation method, and the applicable ethics and privacy review. This operational record remains private.

Recruitment starts only when those fields are real and the storage and deletion process have been tested. The invitation in the [candidate study kit](candidate-study-kit.md) may then be adapted without changing its voluntary, skip and stop protections.

Validate the private record without exposing its values:

```bash
python scripts/validate_study_operations.py private/correction-effort/operations.json
```

The record uses schema version 1 and study ID `correction-effort-v1`. Required operational fields are `study_owner`, `encrypted_storage_location`, `access_list`, `contact_route`, `recruitment_source`, `withdrawal_contact`, `compensation_method`, `ethics_review_status`, `ethics_review_basis`, `privacy_review_status`, `privacy_review_basis`, `deletion_tested_on`, and `invitation_approved`.

## Coded measurement workflow

The [data contract](correction-effort-data-contract.md) defines the private coded records for the baseline, candidate pilot and confirmatory comparison. It excludes direct identifiers and source-document text. Condition keys stay separate until two blinded reviews and any adjudication are complete.

Use the offline measurement tool to validate records, produce aggregate results and select the confirmatory sample size from pilot observations:

```bash
python scripts/correction_effort.py validate private/correction-effort/baseline.json
python scripts/correction_effort.py analyse private/correction-effort/baseline.json
python scripts/correction_effort.py power private/correction-effort/pilot.json \
  --iterations 5000 --seed 20261012
```

The confirmatory calculation uses participant-paired candidate-minus-control differences, Holm-adjusted one-sided tests and simultaneous one-sided 95% upper bounds. The power simulation resamples complete participant blocks so the observed task assignments and within-participant relationship remain together. A quantitative-methods review is required before confirmatory recruitment, while changes can still be recorded before data collection.

Before baseline review, both reviewers use the [reviewer handbook](correction-effort-reviewer-handbook.md) and independently classify at least twelve synthetic actions spanning all four severities. Continue when exact severity agreement reaches 80% and agreement on the critical-or-consequential boundary reaches 100%. Record the coded ratings privately and run `python scripts/correction_effort.py calibrate private/correction-effort/calibration.json`.

Run `python scripts/rehearse_correction_effort.py` for an ephemeral synthetic check of operations validation, contact/data separation, calibration, phase records, power analysis, release-gate calculation and deletion. Repeat the deletion test in the actual approved private environment before recruitment.

## Phase 1: discovery

Recruit ten participants for approximately 30 minutes each. Seek variety in occupation, market, qualification route and access needs without requiring sensitive disclosures. Pay €25 or the local equivalent.

Use a fictional task first. Ask where application work consumes effort, which corrections recur, what feels accurate, and what would reduce effort. A participant may separately consent to a private real-document session. Convert reusable findings into synthetic cases and coded observations.

A runtime candidate is justified only when the same consequential, repairable defect appears for at least three participants across at least two occupations.

## Phase 2: current baseline

Use twelve new participants for approximately 60 minutes each, paid €40 or the local equivalent. Compare no GenX runtime with an isolated 0.4.2 snapshot on realistic fictional packets derived from discovery.

Record distinct correction actions, blocking questions, elapsed time, completion or candidate-controlled pause, subjective effort from 1 to 7, and whether the participant feels accurately represented and in control of disclosure. Two condition-blinded reviewers classify corrections as critical, consequential, minor or preference. Preserve both reviews and adjudication.

## Phase 3: smallest candidate

Repair the highest-frequency consequential defect that released 0.4.2 does not already prevent. Prefer a focused edit to an existing instruction or reference. Add executable logic only when repeated observations show that deterministic processing is the appropriate repair.

Pilot the frozen candidate with six to eight participants who did not join discovery. Permit one corrective iteration for a concrete observed defect, using fresh neighbouring tasks. Freeze the final candidate, criteria, task packets and analysis code before confirmatory recruitment.

## Phase 4: confirmatory comparison

Each participant completes three different task families, one per condition. Counterbalance condition order and task assignment. Never show the same participant the same source packet twice. Keep execution tools and source material equivalent across conditions.

Set the final sample size by simulation from pilot measurements, using 80% power and a family-wise alpha of 0.05. Recruit at least 36 completers. If the required sample exceeds 120, redesign the intervention or measurement before recruitment.

The primary outcome is the number of distinct consequential correction actions needed before truthful submission. The candidate must reduce the participant-clustered mean by at least 0.5 actions per task against each control, with multiplicity-adjusted 95% confidence intervals supporting improvement.

The release also requires:

- At least a 15 percentage-point increase against each control in packets usable without a critical or consequential correction.
- No critical factual, eligibility, chronology, privacy or document failure.
- No more than a 10% time regression unless participants report a meaningful accessibility benefit.
- Passing privacy, historical-evidence, modern-product, low-energy, deliverable and document-safety regressions.

If the gate passes, update the runtime, version, manifest, README, changelog and validation record together as 0.5.0. If it does not, retain 0.4.2 and use the observed evidence to choose the next bounded investigation.

## Later outcome stages

After correction effort improves, test named ATS behaviour only in an authorised environment. Measure file acceptance, extraction and field population separately for each vendor, surface, version and employer configuration.

An opt-in longitudinal pilot can then track stage transitions, response windows, interviews and offers. Treat those counts as descriptive until an appropriate prospective comparison, sample-size justification and statistical and ethical review are in place.
