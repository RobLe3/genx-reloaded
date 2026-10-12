# Validation record

Version 0.2.0, 12 October 2026. This record separates deterministic checks, qualitative agent behaviour, and untested real-world outcomes.

## Deterministic helper checks

**15 synthetic Python unittest cases passed with no skips.** See the [raw test output](../evals/results/preflight-tests.txt) and [environment](../evals/results/environment.json).

| Area | Cases exercised |
| --- | --- |
| Extraction and matching | Unicode/case/dash normalisation, missing text, whole-word boundaries, sparse PDF page |
| DOCX structure | Tables, direct hidden text, tracked changes, header-only contact, hidden style settings, explicit columns |
| File integrity | Source preserved; input/output and output/output aliases rejected, including hard links |
| CLI and outputs | JSON/text outputs, malformed document, non-file input, invalid blank expected phrase |

The tests use synthetic documents. They do not compare the helper with a deployed ATS. Style-inherited visibility, PDF visual appearance, OCR, multilingual typography, and adversarial resource exhaustion are not fully implemented or verified.

Runtime requirements: Python 3.9+; `pypdf` for PDF extraction. Recorded test environment: Linux, Python 3.12.14, pypdf 6.10.0, python-docx 1.2.0, reportlab 4.4.9 and PyYAML 6.0.3. Other runtime versions and operating systems have not been systematically qualified.

## Repository and skill structure

The skill-creator frontmatter validator passed. The project validator checks the runtime inventory and SHA-256 digests, version agreement, metadata, local Markdown links and Python syntax. See its [recorded output](../evals/results/repository-check.json).

These are structural checks. They do not establish successful automatic activation, compatibility with every agent host, correct live URLs, document accessibility, or hiring effectiveness.

## Current agent trials

Four fresh-context executions covered three fictional requests. Each agent received the skill and raw request without the expected answer or the developer's diagnosis. The developer reviewed the outputs; this was not independent adjudication. Exact model and sampling identifiers were not captured, so this is not a controlled cross-model benchmark. [Run records and input/output hashes](../evals/runs.json) preserve the available provenance.

| Task | Observed behaviour | Assessment |
| --- | --- | --- |
| Conflicting records, urgent rewrite | Used six employees after an explicit correction; omitted disputed percentages; retained older training evidence; kept introductory learning distinct; ignored instructions embedded in the CV | No material factual or task-completion defect observed in this response |
| Low energy and accessibility | Used the person's customer-conversation example, asked one question and allowed stopping; no generational-motive claim or imposed disability narrative | Desired narrow support behaviour observed |
| German/English career change, initial | Preserved qualification, B2, confidential clients, neutral break and desired hands-on direction; explained the mixed languages outside the letter; called file checks pending for text-only work | Two usability defects retained in the record |
| German/English career change, rerun | Put the language explanation inside the letter; marked rendering and extraction outside scope; retained factual and disclosure boundaries | Both targeted corrections observed in a fresh context |

The exact snapshots of the first three development trials were not archived. The recorded prompts, responses and corrections support inspection of those observations, not perfect reproduction of an earlier model execution. The rerun used the final behavioural instructions; UI metadata was regenerated afterward.

## Earlier baseline checks

The 0.1.0 baseline had eight synthetic helper tests and two fresh-context qualitative trials. Their raw responses were not preserved in this repository; the following are retained summaries, not additional current-version test results.

- **Discouraged user:** brief empathy, one memory prompt, permission to stop, no lecture or hostile-motive endorsement.
- **Urgent manufacturing CV:** retained old training evidence and dates, flagged an expired mandatory credential, preserved course/proposal status, and skipped coaching.

## Unestablished outcomes

- Human usefulness, accessibility and emotional impact across occupations and backgrounds.
- Interview, offer or other hiring uplift.
- Performance against live employer parsers, matching systems or screening rules.
- Reliable activation, equal behaviour across models, and broad multilingual quality.
- Exhaustive knowledge of selection bias or a way to remove it through CV editing.

No trial submitted an application or involved a real candidate's private data. Publish new evidence with its methods and limits, and preserve failed results.
