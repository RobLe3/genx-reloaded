# GenX Reloaded

**Your experience still counts. Make it visible.**

ATS-aware CV and career support for people with a long career and plenty left to offer. Recover the strengths you have stopped noticing, translate historical knowledge into present relevance, and produce a focused, truthful application.

## Why this exists

GenX Reloaded began after watching 60 Minutes Australia’s report [*How AI is causing an unemployment crisis among middle aged job seekers*](https://www.youtube.com/watch?v=DA_IhG1ZFl4). The report prompted a practical response: help experienced jobseekers make decades of relevant knowledge visible in modern recruitment while preserving truthful dates, qualifications and contribution.

**Version 0.4.2, research preview.** Supports eight markets and scoped troubleshooting for 14 ATS products. The current release includes an offline Word check for retained reviewer comments, including resolved threads. The next measurement phase focuses on candidate correction effort, completion time and control over the finished application, using consenting participants and a predeclared comparison with both released 0.4.2 and a capable general assistant.

[Why](#why-this-exists) · [Start here](#quick-start) · [Podcast](#listen-to-the-podcast) · [Install](docs/installation.md) · [Examples](examples/README.md) · [Evidence](skills/genx-reloaded/references/evidence.md) · [Validation](docs/validation.md) · [Correction-effort study](research/correction-effort-study.md) · [Research roadmap](docs/research-roadmap.md) · [Changes](CHANGELOG.md)

## Listen to the podcast

[![Listen to How GenX Reloaded Outsmarts ATS Filters](assets/GenX_Reloaded_Podcast_Player.svg)](https://roblemumin.com/api/documents/57/audio)

*About 21 minutes · Opens in your browser’s audio player.*

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
| "I need to stop and continue later" | A short, user-controlled handover that leaves unnecessary private history out |
| "My application form has the wrong data" | Surface/vendor-specific diagnosis, a small repair and a safe correction request |
| "Adapt this to US, UK, Canada, Australia or NZ" | Local conventions, public-service requirements and qualification/referee safeguards |
| "Should I apply or learn something first?" | A practical requirement and opportunity check, with a bounded next step |

Try: "Use $genx-reloaded for an Australian APS application through PageUp. Draft the requested pitch and check the submission requirements." Or: "Workable received an old LinkedIn cover letter and I already have an interview. Help me correct it safely."

The full [workflow](docs/workflow.md) adapts to the request. It never makes a motivational exercise a prerequisite for practical help.

## Verified capabilities and current measurement

| Capability | Practical result | Verification |
| --- | --- | --- |
| Optional confidence and strengths support | Practical help remains available immediately, including low-energy and one-question routes | Fictional interaction scenarios and focused regressions |
| Historical-to-current experience translation | Relevant older evidence stays visible with its original period and truthful modern relevance | Worked examples, requirement maps and recorded application tasks |
| Conflicting-source handling | Candidate corrections take priority while titles, dates, credentials and contribution remain consistent | Urgent-rewrite and multi-source development cases |
| Complete application drafting | CV copy, supporting statements, form fields and screening answers remain separate and ready to paste | Bounded application tasks with exact runtime snapshots |
| Offline document preflight | PDF, DOCX, TXT and Markdown extraction plus structural review flags, including retained Word comments | 21 synthetic helper tests and preserved source checks |
| Market and application routing | Eight country cards distinguish commercial, academic and public-service requirements | Dated primary-source records and market-specific scenarios |
| ATS troubleshooting | Fourteen product cards route upload, autofill, screening and correction issues by documented surface | [Product coverage map](research/ats-coverage.md) and current source records |
| Reproducible improvement work | Every meaningful mutation can be compared with released 0.4.2 and a capable general assistant | 77 authored scenarios, immutable runtime snapshots and raw evaluation records |
| Participant measurement | Coded records preserve blinding, task balance, correction severity and candidate effort while private material stays outside Git | Reviewer calibration, aggregate analysis, pilot-based sample-size simulation and an ephemeral workflow rehearsal |

The repository keeps product guidance, executable checks and measurement records separate. The current release includes the verified local Word-comment correction and the complete automated repository suite.

The [candidate correction-effort study](research/correction-effort-study.md) is the next release path. It begins with consenting participants, identifies recurring application work, tests the smallest relevant repair and promotes version 0.5.0 when the candidate produces a clear measured reduction in consequential corrections against both controls. Its coded measurement workflow now includes reviewer calibration, balance checks, blinded-review controls, aggregate analysis, pilot-based sample-size selection and an ephemeral rehearsal.

Detailed methods, comparison records and result histories remain available in the [validation record](docs/validation.md), [evaluation archive](evals/README.md) and [research implementation status](research/implementation-status.md).

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
| [Country and ATS examples](examples/market-and-ats.md), [ATS coverage](research/ats-coverage.md) | Local application requirements and product-specific troubleshooting |
| [Evidence register](skills/genx-reloaded/references/evidence.md) | Sources, dates, study scope and limitations |
| [Layout and checks](skills/genx-reloaded/references/layout-and-checks.md) | Document defaults and the offline helper |
| [Quality and completion](skills/genx-reloaded/references/quality-and-completion.md) | Acceptance criteria, focused repairs and stop conditions |
| [Low-effort routes](skills/genx-reloaded/references/accessibility-and-resume.md), [opportunities](skills/genx-reloaded/references/opportunities-and-learning.md), [interviews](skills/genx-reloaded/references/interview-and-outreach.md) | Optional support beyond the CV |
| [Research implementation](research/README.md), [status](research/implementation-status.md) | Source records, study preparation and remaining roadmap gates |
| [Design](docs/design.md), [examples](examples/README.md), [evaluations](evals/README.md) | Project rationale and inspectable behaviour |
| [manifest.json](manifest.json) | Runtime inventory and SHA-256 file digests |

One entry skill loads relevant references as needed. Research records, tests, evaluation answers, and project documentation stay outside the installable runtime.

## Local document check

The helper requires Python 3.9 or later. PDF extraction also needs `pypdf`; DOCX extraction uses the standard library. It does not use a network.

```bash
python skills/genx-reloaded/scripts/cv_preflight.py /path/to/cv.pdf --require "Your Name" --require "Actual Employer"
```

It reports extraction and structural concerns, including retained Word comments. Comment text and authors stay out of its findings and extracted body text. `review_needed` is a completed inspection with observations; `no_local_flags` is not an ATS or privacy certificate. Word style inheritance, other metadata, visual reading order, scanned text, and many PDF appearance issues still require other checks. The JSON report can contain requested personal strings and file paths, so keep it private along with the CV.

## Validate the source

```bash
python -m pip install -r requirements-test.txt
python scripts/validate_repository.py
python scripts/validate_research.py
python -m unittest discover -s tests -v
```

The dependency file records the versions used for this preview. A skipped test is not a pass. Local checks are documented; no hosted CI result is claimed.

## Privacy, honesty and scope

Keep real CVs, contact details, application records, private explanations, and extracted text outside this repository. The agent may use your supplied facts, but it must not publish them as reusable knowledge. See [SECURITY.md](SECURITY.md).

The skill does not fabricate qualifications, disguise dates, insert hidden keywords, manipulate a hiring model, diagnose the reason for a rejection, or submit applications without authorization. It does not promise to remove discrimination. Support is warm and practical, with room for anger and humour, and no blame directed at another generation.

## Contribute and improve

Bring a concrete use case, a synthetic reproduction, or a well-scoped primary source. Change the smallest relevant part, repeat the affected check and record the result completely. See [CONTRIBUTING.md](CONTRIBUTING.md) and [quality process](docs/quality-process.md).

The [research roadmap](docs/research-roadmap.md) sets out twelve workstreams, evidence standards, candidate studies, accessibility priorities, and a staged implementation backlog. It is a plan for future investigation, with verified starting points and explicit completion gates. A copy-ready GitHub description is available in [repository-description.txt](docs/repository-description.txt).

The [implementation status](research/implementation-status.md) separates additions delivered through 0.4.0 from research that still needs participants, access to employer systems, or further primary methods. See the [six occupation translations](examples/occupation-translations.md) and [evaluation protocol](evals/protocol.md) for concrete starting points.

The documentation approach draws on the inspectable validation and bounded claims in [cc-blender-skill](https://github.com/RobLe3/cc-blender-skill) and [YNM](https://github.com/RobLe3/ynm-skill). Neither project is a runtime dependency, and their evaluation results do not transfer to this skill.

## License and maintainer

Maintained by [RobLe3](https://github.com/RobLe3). No distribution license has been selected. Public visibility does not imply an open-source license. Source links in the evidence register remain subject to their respective owners' terms.
