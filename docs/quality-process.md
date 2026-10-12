# Quality process

The aim is a useful, humane and accurate skill with inspectable limits. "Perfect" is not a testable claim about every candidate, model, ATS, or labour market.

## What to check

| Layer | Check | What it can establish |
| --- | --- | --- |
| Runtime structure | Repository validator and skill frontmatter validation | Files, links, metadata, syntax and inventory are consistent |
| Deterministic helper | Synthetic PDF, DOCX and text tests | Observed behaviour for those fixtures |
| Agent behaviour | Fresh-context task trials using raw prompts | Whether a particular execution follows the workflow |
| Source quality | Primary source, date, scope, limitations, contradictory findings | A claim is traceable to appropriate evidence |
| Human usefulness | Feedback from consenting users | Actual usability, tone and usefulness in that setting |
| Hiring effectiveness | Suitable controlled research | Effects within the tested population and intervention |

The first four have initial coverage. Human usefulness and hiring effectiveness remain unestablished.

## Refine from an observed problem

1. Preserve the accepted version and the failed output.
2. Identify a concrete defect, a missing fact, a capability limitation, or a preference change.
3. Remove private details and construct a fictional reproduction if reusable learning is appropriate.
4. Change the smallest relevant instruction or helper behaviour.
5. Run the affected checks. Give an evaluation agent the skill and raw request without the diagnosis or desired answer.
6. Record the actual result, including failures, skips, unresolved issues, and scope limits.
7. Update version, manifest, change notes and documentation when the runtime changes.
8. Publish only with maintainer authorization.

Do not tune a benchmark's criteria after seeing the answer and then call it a pass under the original rules. A revised criterion or prompt needs its own record.

## Stop conditions

Stop when the requested scope is satisfactory and another pass has little expected value. Continue for a concrete defect or a required gate. Missing evidence is a reason for a bounded result, not an excuse to invent a finding or run endless cosmetic rewrites.

The skill's own [quality reference](../skills/genx-reloaded/references/quality-and-completion.md) applies the same principle to candidate deliverables.

## Next useful evaluation work

- Human feedback across occupations, countries, vocational routes, nonlinear careers and energy levels.
- Generated document accessibility and visual checks in multiple hosts.
- Behaviour on scanned CVs, very long histories and conflicting sources.
- Broader multilingual and model coverage.
- Evaluation of specific interventions without attributing uncontrolled outcomes to the skill.

These are research needs, not promises that current tests already cover them.
