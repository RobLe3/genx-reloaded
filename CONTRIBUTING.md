# Contributing

Contribute usable evidence, clearer instructions, accessible workflows, and reproducible local checks.

## Research contributions

For each source, include:

1. Title, author or organisation, and primary URL.
2. Publication or revision date, date checked, and version if relevant.
3. Evidence type: experiment, observation, audit, enforcement allegation/settlement/judgment, vendor documentation, or advice.
4. Population, sample, geography, product version, or other important context.
5. The finding and the exact practical implication it supports.
6. Limitations, conflicting results, and what it does not establish.
7. Sections inspected and any access limitations.

Use short paraphrases and links. Do not copy complete third-party documents. Include null, mixed, and contrary findings. A study showing bias is not automatically evidence that a proposed CV edit fixes it.

Do not turn a vendor claim into independent validation, a settlement into an admission, or a hypothetical scenario into an observed incident.

## Skill changes

Preserve the optional support opening, skip path for urgent tasks, factual boundaries, and user control over personal disclosures. Test with a relevant synthetic request. Give an evaluation agent the raw task and skill, not the expected answer.

Keep detailed references outside SKILL.md. Avoid adding user CVs, secrets, personal experiences, or real application responses to the repository.

## Code changes

Run the synthetic preflight tests and report failures and skips. Test a changed failure mode with a meaningful fixture. Do not create tests that merely restate the implementation.

Keep the helper offline. Do not add telemetry, model calls, external uploads, or live applications as part of testing.

## Version and release preparation

Use `VERSION` as the repository's release identifier. Update `manifest.json`, README, CHANGELOG and the validation record together. Recompute the runtime SHA-256 inventory after a runtime edit; do not change hashes merely to conceal an unexpected file modification.

For this preview series, use a patch increment for focused corrections and a minor increment for new workflow capabilities or changed invocation. Do not call a version stable solely because structural checks pass. Broader use and evaluation must support stronger claims.

Run `python scripts/validate_repository.py` and `python -m unittest discover -s tests -v`. Re-run agent scenarios only for a concrete affected behaviour. Preserve adverse results and separate raw prompts from assessor notes. Do not include candidate data or unrelated local files in commits.

For research updates, also run `python scripts/validate_research.py`. Follow the [research record contract](research/record-contract.md) and [evaluation protocol](evals/protocol.md). Keep human-study consent and observations outside Git. Record catalogue cases separately from actual executions and preserve exact tested runtime snapshots.

The [correction-effort study](research/correction-effort-study.md) fixes the participant sequence and release thresholds for the next runtime candidate. Before recruitment, create the private operations record and validate it with `python scripts/validate_study_operations.py private/correction-effort/operations.json`. Never commit that record, participant contacts, consent records, session notes, recordings or real application documents.

## Distribution

The maintainer has not selected a distribution license. Public visibility does not grant an open-source license. Resolve licensing before redistributing the material under new terms or accepting contributions whose terms are incompatible with the maintainer's eventual choice.
