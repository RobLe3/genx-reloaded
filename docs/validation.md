# Validation record

Version 0.4.1, 12 October 2026. This patch follows a matched historical-version comparison. **Useful fictional outputs are demonstrated; human confidence, live ATS acceptance and hiring benefit are not.** Read the [comparison report](skill-comparison.md) for task-level results and limits. Historical records remain available for [0.4.0](validation-v0.4.0.md), [0.3.0](validation-v0.3.0.md) and [0.2.0](validation-v0.2.0.md).

## Matched comparison and repair

Six new requests across 0.2.0, 0.3.0, 0.4.0 and no loaded skill produced 24 fresh-context answers. Three one-fact variants under 0.4.0 brought the planned comparison to 27 executions and nine distinct cases. The runtime remained frozen during these runs. See the [protocol](../evals/comparison-2026-10-12/protocol.md), [run index](../evals/comparison-2026-10-12/runs.json), [final assessment](../evals/comparison-2026-10-12/assessment.json) and [adjudication](../evals/comparison-2026-10-12/adjudication.md).

All planned answers met word limits, and none exhibited a critical failure in the saved output. Ten minor or borderline criterion issues remain: three unagreed future tasks in skill handovers, three omitted withdrawal-cancellation explanations, and four partial saved-origin/submitted-copy distinctions. All conditions gave a safe employer correction route; only 0.4.0 explicitly named the cancellation risk. A strong no-skill condition prevents claims of general skill superiority.

The developer assessed all outputs before receiving a fresh, condition-blinded agent assessment. Six criterion disagreements were adjudicated explicitly. Actual federal citation identities were retrieved to resolve four provenance questions. This is additional agent review, not an independent human study. Exact model/sampling metadata and full tool transcripts are unavailable.

Version 0.4.1 changes three instruction files to remove unagreed next tasks from pause-only handovers and omit routine check boilerplate from short text. Three focused executions met their written checks: the same pause request, the same rewrite, and a neighbouring explicit verification request. The [repair assessment](../evals/comparison-2026-10-12/repair-assessment.json) preserves outputs and the snapshot digest `2acc46bc65cc3fca8bb6b8cfc6af6061efa16a96f758fdccdb1a0e65236f6f80`. These three runs do not repeat the whole four-condition experiment.

## Structural and artifact checks

Repository structure, links, runtime manifest, frontmatter, research-record structure and recorded artifact integrity were checked for this patch. See [repository check](../evals/comparison-2026-10-12/repository-check.json), [research check](../evals/comparison-2026-10-12/research-check.json), [frontmatter check](../evals/comparison-2026-10-12/frontmatter-check.txt) and [integrity check](../evals/comparison-2026-10-12/integrity-check.json).

No executable helper changed. The 27 passing helper unit tests belong to the preserved [0.4.0 run](../evals/v0.4.0/unit-tests.txt); they are not represented as rerun for 0.4.1. The current catalogue has 59 authored cases. Across the 0.3.0, 0.4.0 and this comparison, 24 distinct catalogue cases have recorded executions. Case count is not pass count, and most catalogue cases have not run.

## Remaining boundaries

The no-skill assistant inherited the same host instructions and skill-catalogue metadata but was instructed not to load a runtime. Agents shared a filesystem; read boundaries were instructed, not enforced. Prompts contain explicit guardrails, actual browsing differs, and each condition has one answer per task. These conditions support qualitative observations, not causal estimates or general reliability rates.

All candidate records are fictional. The evaluation harness saves those fictional records deliberately; it does not test real-user retention controls. No participant study, real CV, external message, live application, withdrawal, purchase, assistive-technology session or hiring outcome is part of this record. Eight market cards and fourteen ATS cards remain bounded research coverage, not universal compatibility. The best next evidence is consented human usability, relevant document checks and authorised ATS-surface investigation.
