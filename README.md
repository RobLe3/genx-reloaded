# GenX Reloaded

**Your experience still counts. Make it visible.**

ATS-aware CV and career support for people with a long career and plenty left to offer. Recover the strengths you have stopped noticing, translate historical knowledge into present relevance, and produce a focused, truthful application.

**Version 0.2.0, research preview.** Usable skill and offline document checker, with synthetic tests and documented agent trials. Hiring effectiveness and human usability have not been established.

[Start here](#quick-start) · [Install](docs/installation.md) · [Examples](examples/README.md) · [Evidence](skills/genx-reloaded/references/evidence.md) · [Validation](docs/validation.md) · [Changes](CHANGELOG.md)

## What it feels like

> This process can be unfair and exhausting. A rejection does not erase what you know. Let's recover the strengths you may have stopped noticing, then make them visible.

A paper map, a difficult conversation, a repaired machine, or another technology transition can be a memory cue. Your own examples matter more than fitting a generational stereotype. The skill turns relevant memories into work examples and supported CV claims.

You can start with one question. You can skip the encouragement. You can say you have had enough for today.

## A 30-second example

**Before:** "Responsible for all IT and digital transformation."

**Confirmed facts:** Led six engineers through a network replacement at 11 sites. No measured savings were supplied.

**After:** "Led six engineers through a network replacement across 11 sites."

The useful result is specific scope and contribution. It does not acquire an invented cost saving or become an AI project. An older achievement can stay when it is the best evidence for the role.

All examples in this repository are fictional. They must never be copied as a real candidate's achievements.

## Quick start

Clone the repository:

```bash
git clone https://github.com/RobLe3/genx-reloaded.git
cd genx-reloaded
```

Ask an agent with local file access:

```text
Read skills/genx-reloaded/SKILL.md and use it to help me tailor my CV to this vacancy. Keep valuable older experience and do not invent facts.
```

In a host where the skill is installed and named invocation is supported:

```text
Use $genx-reloaded. I am exhausted by applications. Start with one small question.
```

Or:

```text
Use $genx-reloaded. Skip the pep talk. Rewrite the supplied CV for this role and flag genuine qualification gaps separately.
```

The runtime is the self-contained [skills/genx-reloaded](skills/genx-reloaded/SKILL.md) folder. It does not require a particular model provider, a scoring service, or a paid ATS checker. File rendering and automatic skill discovery depend on the host. See [installation and verification](docs/installation.md).

## Choose your route

| Need | What you receive |
| --- | --- |
| "I feel invisible" | Brief support, an optional strength prompt, one manageable next step |
| "Audit this CV" | Prioritised findings tied to actual passages |
| "Rewrite this for the job" | Usable CV copy, supported positioning, material gaps and review notes |
| "Make a submission file" | Requested document, factual review, visual and extraction checks where tools permit |
| "Explain ATS and age bias" | Sourced findings, distinct screening mechanisms, and their limits |
| "Help me through the process" | CV, requested supporting drafts, application review, interview stories and rejection debrief |

The full [workflow](docs/workflow.md) adapts to the request. It never makes a motivational exercise a prerequisite for practical help.

## What works, and what the evidence supports

| Capability | Evidence in this repository | Boundary |
| --- | --- | --- |
| Optional confidence and strengths coaching | Fictional low-energy scenarios | No human usability or clinical study |
| Historical-to-current experience translation | Worked examples and CV scenarios | No invented modern tool experience |
| Accurate handling of conflicting facts | Recorded urgent-rewrite scenario | Finite examples, not universal model reliability |
| Bilingual application support and private career breaks | German/English scenario, observed defects and focused rerun | Broader languages and markets remain untested |
| Offline PDF, DOCX, TXT and Markdown preflight | 15 synthetic tests | Local extraction, not live ATS behaviour |
| Bias and ATS knowledge | Dated source register with context and limitations | Curated research, not an exhaustive review |
| Repeatable repository checks | Manifest, links, metadata and Python syntax validator | Structural consistency, not hiring effectiveness |

Read the [validation record](docs/validation.md) for methods, adverse observations, exact scope, and remaining work. Do not infer a measured interview uplift from these checks.

## The journey

1. Recover confidence, if wanted.
2. Identify strengths and find work evidence.
3. Establish the target, market, requirements, and constraints.
4. Translate the career while preserving valuable historical knowledge.
5. Build a clear first page and accurate chronology.
6. Check facts, reading order, and requested file outputs.
7. Prepare the next application or interview step.
8. After rejection, allow disappointment and choose one useful next action.

## Knowledge and runtime structure

| Location | Purpose |
| --- | --- |
| [SKILL.md](skills/genx-reloaded/SKILL.md) | Entry point and end-to-end workflow |
| [Support and strengths](skills/genx-reloaded/references/support-and-strengths.md) | Voice, ten optional prompts, rejection support |
| [Working patterns](skills/genx-reloaded/references/working-patterns.md) | Evidence maps and truthful bullet patterns |
| [Application decisions](skills/genx-reloaded/references/application-decisions.md) | Language, qualifications, career breaks and changes of seniority |
| [Bias and ATS caveats](skills/genx-reloaded/references/bias-and-ats-caveats.md) | Screening mechanisms and reasonable responses |
| [Evidence register](skills/genx-reloaded/references/evidence.md) | Sources, dates, study scope and limitations |
| [Layout and checks](skills/genx-reloaded/references/layout-and-checks.md) | Document defaults and the offline helper |
| [Quality and completion](skills/genx-reloaded/references/quality-and-completion.md) | Acceptance criteria, focused repairs and stop conditions |
| [Design](docs/design.md), [examples](examples/README.md), [evaluations](evals/README.md) | Project rationale and inspectable behaviour |
| [manifest.json](manifest.json) | Runtime inventory and SHA-256 file digests |

One entry skill loads relevant references as needed. Research records, tests, evaluation answers, and project documentation stay outside the installable runtime.

## Local document check

The helper requires Python 3.9 or later. PDF extraction also needs `pypdf`; DOCX extraction uses the standard library. It does not use a network.

```bash
python skills/genx-reloaded/scripts/cv_preflight.py /path/to/cv.pdf --require "Your Name" --require "Actual Employer"
```

It reports extraction and structural concerns. `review_needed` is a completed inspection with observations; `no_local_flags` is not an ATS certificate. Word style inheritance, visual reading order, scanned text, and many PDF appearance issues still require other checks. The JSON report can contain personal strings and file paths, so keep it private along with the CV.

## Validate the source

```bash
python -m pip install -r requirements-test.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

The dependency file records the versions used for this preview. A skipped test is not a pass. Local checks are documented; no hosted CI result is claimed.

## Privacy, honesty and scope

Keep real CVs, contact details, application records, private explanations, and extracted text outside this repository. The agent may use your supplied facts, but it must not publish them as reusable knowledge. See [SECURITY.md](SECURITY.md).

The skill does not fabricate qualifications, disguise dates, insert hidden keywords, manipulate a hiring model, diagnose the reason for a rejection, or submit applications without authorization. It does not promise to remove discrimination. Support is warm and practical, with room for anger and humour, and no blame directed at another generation.

## Contribute and improve

Bring a concrete failure, a synthetic reproduction, or a well-scoped primary source. Preserve mixed findings and failed trials. Change the smallest relevant part, repeat the affected check, and stop when additional polishing has little information value. See [CONTRIBUTING.md](CONTRIBUTING.md) and [quality process](docs/quality-process.md).

The documentation approach draws on the inspectable validation and bounded claims in [cc-blender-skill](https://github.com/RobLe3/cc-blender-skill) and [YNM](https://github.com/RobLe3/ynm-skill). Neither project is a runtime dependency, and their evaluation results do not transfer to this skill.

## License and maintainer

Maintained by [RobLe3](https://github.com/RobLe3). No distribution license has been selected. Public visibility does not imply an open-source license. Source links in the evidence register remain subject to their respective owners' terms.
