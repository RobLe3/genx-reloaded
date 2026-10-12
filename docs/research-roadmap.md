# GenX Reloaded research roadmap

**Status:** proposed programme, not completed research. **Prepared:** 12 October 2026. **Baseline:** version 0.2.0, commit `fe331d402a4bfdd5c296e34e3296ed68a6b68f39`.

**Implementation update:** version 0.3.0 delivers the first repository and runtime additions. See the [task-by-task status](../research/implementation-status.md) for completed artifacts and remaining research gates. The programme below is preserved as the original plan; it is not retroactively labelled complete.

## Purpose and decisions

Help someone recognise the value of their experience, make a truthful and relevant application, and choose a manageable next step. Gen X is the starting audience and the voice of the project. Age, gender, occupation, educational background, disability, and confidence level must not become eligibility requirements.

The research should answer five practical questions:

1. What support helps a person feel understood and regain useful agency?
2. Which application changes improve clarity, factual accuracy, accessibility, and relevance?
3. What do different hiring mechanisms actually do, and which candidate responses are justified?
4. Where do advice and language need to change for the person, occupation, and country?
5. How can we demonstrate benefits and detect harm without promising interviews or collecting unnecessary personal data?

The skill can have backbone: "You are allowed to be furious. Your experience did not expire. Let's make it visible." Research must preserve that emotional permission while checking what people actually find helpful. A rejection is not a diagnosis of the candidate, an employer, an algorithm, or another generation. Support should not require someone to prove that their frustration is justified.

Do not turn every research finding into more instructions. Add a rule only when it improves a real decision or prevents a demonstrated failure. Put specialist knowledge in optional references and keep the entry workflow short.

## What we already know about this project

The [validation record](validation.md) reports 15 synthetic document-checker tests and four fresh-context agent executions across three fictional requests. It preserves the initial German scenario's usability failures and a focused rerun. The runtime already separates extraction from hiring decisions, preserves useful older achievements, offers optional encouragement, and prohibits invented credentials or results.

These checks establish a small behavioural and technical baseline. They do not establish human usability, accessible operation, reliable behaviour across models, live ATS compatibility, or improved hiring outcomes. Earlier scenario snapshots and model settings were not captured comprehensively. The [evidence register](../skills/genx-reloaded/references/evidence.md) is a curated starting point, not a systematic review.

The first work should improve research provenance, candidate involvement, and coverage beyond the existing IT and bilingual examples. A newer ICO report identified during this planning pass also makes an evidence refresh worthwhile. This document identifies research starting points; it does not claim to have completed the review proposed below.

## Priority and sequence

| Priority | Work | Why it comes here | Decision it should unlock |
| --- | --- | --- | --- |
| P0 | Reproducible evaluation and claim register | We need to know what changed and why we believe it | Whether a proposed improvement is supported and testable |
| P0 | Candidate discovery, emotional support, accessibility | The skill must help people in the state in which they arrive | Which routes, wording, and interaction defaults to retain |
| P0 | ATS mechanisms and age-bias evidence | Confident myths can waste effort or damage applications | Which advice is justified, conditional, uncertain, or obsolete |
| P1 | Historical experience, CV interventions, occupation coverage | This is the core practical value | How to preserve experience while making relevance obvious |
| P1 | Country and language guidance | A universal CV rule can be wrong in a particular market | What must be localised and when to check an official source |
| P1 | Interviews, opportunity choice, privacy and portability | A polished CV is only part of the journey | What the end-to-end workflow should include on request |
| P2 | Broader languages, hosts, and prospective outcome studies | Expansion is useful after the core is credible | Which claims and supported environments can responsibly expand |

Privacy and factual accuracy apply from the first phase, even where their broader research workstream is scheduled later. Accessibility is part of the core, not a later premium feature. Priorities are sequencing decisions, not a ranking of people's needs.

## Research workstreams

### R01. Understand candidates' actual needs

**Questions.** Where do people get stuck: remembering achievements, choosing a direction, writing, operating application forms, explaining a break, or recovering after rejection? What feels patronising? How much effort can they spare? Does the GenX identity feel welcoming, useful, irrelevant, or exclusionary? Do metaphors such as "Botoxing" imply hiding age or appeal unevenly across genders?

**Method.** Begin with an exploratory set of approximately 8 to 12 voluntary interviews, then small iterative usability rounds of about 5 to 8 participants. These are planning ranges for qualitative discovery, not statistically representative samples or sufficient evidence for subgroup comparisons. Seek variation in occupation, employment status, language, application experience, access needs, and career length. Do not require disclosure of protected characteristics or a full CV. Include people who are time-poor, sceptical of coaching, or unfamiliar with AI.

Observe concrete tasks: start without a prepared CV; recover one accomplishment; tailor an existing CV; resume after an interruption; challenge an incorrect suggestion. Ask about feelings without leading people toward the intended brand story. Record dissent and requests to skip support. Recruitment, compensation, recordings, and any use of real documents need a separate, explicit consent process before a study begins.

**Deliverable and exit.** An anonymised needs map, consent materials, task scripts, and a ranked list of observed friction. Every proposed interaction change must point to an observation or be labelled a hypothesis. Do not publish participant quotations or details without specific permission.

### R02. Make emotional support useful and optional

**Questions.** Does encouragement help someone begin or feel understood? When does it delay useful work? Are a calm voice, dry humour, and a more defiant voice received differently? Which rejection responses reduce shame without making unsupported promises? Can someone stop comfortably and restart later?

**Method.** Review job-search intervention research, starting with the Liu, Huang and Wang meta-analysis in the source table. Investigate skill development, self-efficacy, goal setting, social support, and setback preparation. Follow its references to original interventions before adapting any exercise. Evidence for a facilitated programme does not establish the effect of an AI conversation or one pep talk.

Compare short, candidate-selected openings: immediate practical help; brief acknowledgement plus a small action; optional strengths exploration. Offer one memory cue first, with up to ten available if wanted. A paper map or direct conversation can prompt a memory, but is not evidence of a professional skill until the person supplies a relevant example. Never imply younger people cannot do those things. Allow "I don't know", "skip", fragments, anger, silence, and "enough for today".

**Deliverable and exit.** A tested voice guide and support patterns for initiation, overwhelm, rejection, and returning after a pause. Evaluate perceived respect, choice, pressure, usefulness, and effort. Someone requesting an urgent rewrite receives it without completing coaching. Do not claim clinical benefit or make positive mood a completion requirement.

### R03. Understand bias without inventing the cause of a rejection

**Questions.** What evidence concerns age, and how does it interact with gender, disability, names or perceived ethnicity, career gaps, class signals, foreign qualifications, and changes of seniority? Which findings concern employer behaviour, a particular model, a screening rule, or candidate expectations? Which mitigation strategies have actually been tested?

**Method.** Map field experiments, administrative studies, laboratory studies, model audits, regulator investigations, settlements, and candidate surveys separately. Extract country, occupation, period, age ranges, outcome, sample, design, and uncertainty. Distinguish an investigation from a finding, and a settlement from a trial judgment. Include null and mixed findings. Use age ranges from each study rather than relabelling all older-worker research as Gen X research.

For the skill itself, use fictional paired cases to check that equally supported experience receives equally serious help when irrelevant demographic cues vary. This tests the assistant's treatment of candidates, not discrimination in an employer's system. Do not infer protected characteristics from names or dates, rank people's employability by them, or reuse private candidate records for fairness testing.

**Deliverable and exit.** A bias evidence matrix and candidate-facing explanations with carefully bounded actions. Each mitigation recommendation needs intervention evidence or an explicit description as a practical option with uncertain hiring benefit. No claim that removing an age cue removes bias, and no claim about hostile motives of another generation.

### R04. Map actual hiring mechanisms and ATS variation

**Questions.** Which products extract fields, search resumes, match skills, rank applicants, apply employer-defined screening questions, schedule assessments, or simply store applications? What depends on configuration or a purchased feature? Can candidates correct parsed fields or request human review? What does an opt-out actually cover?

**Method.** Start with official documentation for systems encountered by participants. Greenhouse is a useful documented starting point. Add systems such as Lever, Workday, SAP SuccessFactors, Personio, or SmartRecruiters only where relevance and accessible evidence justify the effort. Record product, feature, documentation date, configuration, and what remains unknown. Distinguish vendor descriptions from independent validation. The existence of a capability does not show how frequently employers enable it.

Use synthetic documents for local extraction tests. Employer-side tests require an authorised test environment and must identify the exact configuration. Never submit fake applications to real vacancies as an informal experiment. Treat employer screening questions, document parsing, semantic matching, assessments, and human decisions as different mechanisms. Investigate semantic matching as well as exact wording, including risks of keyword stuffing.

**Deliverable and exit.** A versioned mechanism matrix and a short decision guide. Every practical ATS claim identifies its source and scope. The skill explains what it can check locally and what remains unknown. No universal pass score, universal rejection percentage, or claim that extraction success predicts selection.

### R05. Test which CV changes help readers and preserve evidence

**Questions.** How should a first page communicate fit? When should older achievements remain prominent? How much chronology is useful? Do page count, headings, bullet structure, terminology, and ordering work differently by occupation or market? Does a functional layout obscure evidence that a hybrid chronology preserves? What does "quick to scan" mean in a real task?

**Method.** Build fictional before-and-after examples with an explicit fact ledger. Compare limited changes while holding underlying qualifications constant. Ask reviewers to locate relevant evidence, identify gaps, and explain their confidence. Where practical, hide which variant the project prefers and counterbalance presentation order. A small preference study is not evidence of interview uplift.

Research dated advice about photographs, graduation dates, early roles, and career length in its jurisdiction. Separate optional omission from misleading chronology and mandatory form responses. Do not make a blanket 10- or 15-year deletion rule. Examine common claims about seconds spent reading and automated rejection rates rather than repeating them. Check the exact source, method, and whether the claim generalises.

**Deliverable and exit.** A library of annotated transformations across occupations, with supported facts, trade-offs, and local context. A reviewer can find the core qualification and the candidate's contribution with less confusion. No transformation invents a metric, promotes participation to ownership, or upgrades historical tools into current experience. Qualitative evidence remains valid when no measurement exists.

### R06. Translate deep experience across occupations

**Questions.** Which historical knowledge remains directly useful? Which capabilities transfer but need a new example or current training? How do we help a specialist change sector or move from leadership to an individual contributor role? How can informal, voluntary, or caring experience be discussed without inventing employment or demanding private disclosure?

**Method.** Use ESCO and O*NET as vocabulary and task-mapping aids, alongside current role descriptions and candidate confirmation. Do not infer that someone has every skill associated with their title. Preserve distinctions between a capability, a tool, domain knowledge, a credential, and recent hands-on practice. Treat taxonomy equivalence as a research question, not an automatic translation.

Build examples for skilled trades, manufacturing, logistics, retail and hospitality, administration, care, education, creative work, public service, and technical roles. Research contribution evidence beyond revenue and team size: reliability, fault diagnosis, handovers, customer resolution, process continuity, and knowledge transfer. Make each claim depend on the person's facts. A caring role does not automatically confer a regulated professional qualification.

**Deliverable and exit.** Occupation examples and an evidence-to-language method covering direct evidence, transferable evidence, recency gaps, and missing qualifications. A candidate can reject a proposed interpretation. Valuable older expertise survives when relevant; gaps remain visible without turning the person into a list of deficiencies.

### R07. Make low-energy and accessible use a core route

**Questions.** Can the workflow be used with fatigue, executive-function difficulties, limited typing, a screen reader, voice input, mobile access, or limited bandwidth? Can someone resume without retelling a painful history? Are exported documents usable as well as visually neat?

**Method.** Use W3C cognitive accessibility guidance as a starting point and separately identify applicable WCAG requirements for any interface the project actually controls. Test concise steps, predictable choices, plain language, answer fragments, explicit confirmation of facts, and a short user-controlled resume note. Avoid inferring a diagnosis from behaviour.

Combine actual assistive-technology checks with voluntary user testing. For documents, inspect semantic headings, reading order, selectable text, contrast, meaningful links, and available PDF tagging support. Test OCR and non-Latin text only if those capabilities are provided, and expose extraction uncertainty. Check whether tables are necessary before using them in candidate deliverables. Do not describe a document or host as accessible solely because text extraction succeeded.

**Deliverable and exit.** An accessibility checklist tied to supported hosts and formats, an explicit list of untested combinations, and demonstrated low-effort routes. Someone can obtain a useful result with one question at a time, skip nonessential questions, and pause without losing their work. Manual checks and user observations remain distinct from conformance claims.

### R08. Localise language, qualifications, and official guidance

**Questions.** Which recommendations change by application country, working language, occupation, or employer? How should non-equivalent qualifications be named? What is customary versus required? What official options exist for correction, accommodation, human review, data access, or discrimination concerns?

**Method.** Prioritise German- and English-language applications, building on the existing scenario, then decide further expansion from observed demand. Treat Germany, Austria, and Switzerland as separate jurisdictions. Treat UK and US guidance separately too; further regional distinctions may be necessary. Country of residence, target employer location, and language are different inputs.

Create small country modules with official sources, last-checked dates, scope, and unresolved questions. Investigate photos, birth dates, education dates, qualification recognition, language proficiency, career-break wording, references, forms, and requested documents. Verify laws and regulatory dates at the time of use. Separate rules in force from proposed amendments, guidance, and employer custom. Do not extrapolate an EU rule to Switzerland or treat a national rule as worldwide advice.

**Deliverable and exit.** Maintained country cards and bilingual examples. A qualification retains its accurate original meaning, with an explanation where useful. Private health or family context is not disclosed without the candidate choosing it. Unknown rules trigger an official-source check or a clear limitation, not a guess. Legal escalation information points to appropriate official help without promising an outcome.

### R09. Connect the CV to the rest of the job search

**Questions.** What helps with referrals, applications, interviews, work samples, negotiation, and rejection? How can someone explain "overqualification" or a change of seniority without apologising for experience? Which activities are feasible for people without an extensive network or spare time?

**Method.** Research networking evidence with attention to platform and occupational context. The weak-ties study in the source table is a starting point for questions, not a justification for mass messaging. Explore low-pressure reconnection drafts, professional associations, community routes, and direct applications. No outreach is sent without authorization.

Develop interview stories from the same confirmed fact ledger as the CV. Examine skills demonstrations that are bounded, relevant, and not unpaid consulting projects. Keep confidential employer material out of examples. Research negotiation and role expectations without defaulting to an age-related pay cut, a lower-status role, or the assumption that every candidate wants management. After rejection, distinguish explicit feedback from speculation and offer rest as a legitimate option.

**Deliverable and exit.** Optional application, interview, and follow-up modules that reuse confirmed evidence and reflect the person's constraints. A candidate can choose a sustainable weekly effort rather than an application-volume target. The workflow remains useful to someone with no referral, portfolio, or social-media presence.

### R10. Help people choose worthwhile opportunities and learning

**Questions.** How can someone distinguish required qualifications from preferred ones, identify a realistic stretch, and avoid needless self-rejection? When would a small learning project help, and when is another certificate a costly distraction? What signals justify checking whether a vacancy or recruiter is legitimate?

**Method.** Compare real role requirements across relevant occupations without republishing restricted job data or assuming all listed preferences are hard filters. Separate regulated requirements and explicit employer constraints from ambiguous wording. Build a decision aid using direct evidence, transferable evidence, gaps, practical constraints, and the candidate's preferences. It must not turn into a pseudo-scientific employability score.

Use official consumer-protection guidance for scam awareness and verify local relevance. Examine upfront fees, requests to move money, sensitive-data requests, employer identity, and communication channels. One suspicious cue warrants checking; it does not always establish fraud. Silence after an application does not establish a fake vacancy. Recommend training only after identifying a specific gap, with time, cost, alternatives, and no assumption that a course equals production experience.

**Deliverable and exit.** A short opportunity check and a targeted learning decision aid. Recommendations respect financial urgency, working hours, location, accessibility, and the person's chosen direction. No guarantees about employers, paid courses, or application outcomes.

### R11. Protect private history and work across realistic environments

**Questions.** What information is genuinely needed? What can stay on the person's device? How do model, host, tools, and file formats affect quality, cost, and effort? Can someone continue with plain text or a smaller model when export tools are unavailable?

**Method.** Threat-model CV uploads, hidden document text, malicious vacancy instructions, prompt injection, generated reports, logs, and repository publication. Maintain a clear boundary between reusable skill knowledge and an individual career record. Consent to help with a CV is not consent to publish it, train a model on it, or add it to research data. Research consent must be separate, revocable where applicable, and clear about retention and access.

Evaluate supported host/model combinations explicitly, recording versions and available tools. Include a text-only route, interruptions, limited context, and local execution where feasible. Document how private session notes can be resumed, exported, or deleted without pretending the skill controls a host's retention policy. Do not upload a document to a third-party ATS checker by default. Never commit real applicant records or private logs to this repository.

**Deliverable and exit.** A data-flow inventory, retention guidance, security scenarios, and a portability matrix. Unsupported export or browsing capabilities are explained accurately. Private details do not enter reusable examples. The smallest useful workflow remains available without requiring a commercial scoring service.

### R12. Establish credible evaluation and maintenance

**Questions.** Compared with the current skill and a competent general assistant, what improves? Which users or tasks receive worse help? How stable is behaviour across models and repeated runs? Which claims become stale fastest?

**Method.** Use the evaluation ladder below. Record exact skill commit, case version, model identifier when available, host, tool access, date, prompts, outputs, and assessment method. Mark unavailable metadata as unknown. Separate development cases from held-out evaluation cases. Preserve initial failures and reruns, with an explanation of what changed. Use an additional reviewer where feasible; label single-maintainer judgments honestly.

Build a source update process with a named maintainer and change log. Prioritise refresh when official product behaviour changes, a regulation changes, users report a contradiction, or a source is corrected. Record a suggested review cadence rather than pretending a calendar alone makes advice current. No monitoring automation is enabled by this plan.

**Deliverable and exit.** A reproducible evaluation protocol, complete run records, failure taxonomy, and maintenance checklist. Release notes describe observed improvements and known limitations. Finite successful tests are never described as universal safety, fairness, or hiring effectiveness.

## Research and evidence protocol

For each workstream, write the question before collecting sources. Log databases or sites, exact queries, languages, dates, inclusion criteria, exclusions, and inaccessible full texts. Search primary studies, official documentation, and regulators first. Practitioner advice can contribute practical hypotheses, but must be labelled as such. Seek contradictory evidence deliberately. Use a scoping review unless the work actually meets a predeclared systematic-review protocol.

Every claim record should include:

| Field | Required content |
| --- | --- |
| Identity | Stable claim ID, workstream, precise statement and intended decision |
| Source | URL or DOI, author or organisation, publication/version date, date checked |
| Evidence type | Experiment, observational study, synthesis, official rule, vendor documentation, practice guidance, or user observation |
| Scope | Country, occupation, sample or population, feature/configuration, and outcome measured |
| Findings | Direction, uncertainty, mixed results, and what was actually observed |
| Limits | Confounding, missing data, conflicts of interest, access limitations, and transfer assumptions |
| Action | Candidate implication, plausible downside, alternatives, and whether mitigation was tested |
| Maintenance | Status, review trigger, reviewer, linked tests, and superseded claims |

Keep claim confidence separate from source prestige. An official vendor page is strong evidence of documented product behaviour and weak evidence of impartial fairness. A controlled hiring experiment can establish an effect in its setting without establishing the cause of one person's rejection. A candidate interview can reveal a real usability problem without estimating its population prevalence.

Use plain statuses such as **supported within stated scope**, **promising but untested here**, **mixed**, **outdated**, and **unknown**. Do not aggregate unrelated claims into a numerical evidence score. Never turn a useful emotional phrase into an empirical assertion merely because it appears in the same reference file.

## Verified starting points and retrieval limits

These sources were inspected during the planning pass on 12 October 2026. They seed the work; their presence does not mean all underlying studies or linked documents were reviewed.

| Source | Research use | Scope and caution |
| --- | --- | --- |
| [ICO, Recruitment rewired, 2026](https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/) | R03, R04, R08, R11: automated decisions, human involvement, transparency and monitoring | Executive summary inspected. Voluntary engagement with over 30 employers from March 2025 to January 2026, explicitly not an audit or investigation. Keep separate from the 2024 provider audit already in the evidence register. |
| [Liu, Huang and Wang, Effectiveness of job search interventions, 2014](https://research.monash.edu/en/publications/effectiveness-of-job-search-interventions-a-meta-analytic-review/) | R02, R09: practical skills, motivation and support | Institutional abstract inspected, describing 47 experimental or quasi-experimental interventions. Retrieve full methods and original studies before claiming that any component causes an effect. Results do not validate this skill or AI coaching. DOI: 10.1037/a0035923. |
| [W3C, Making Content Usable for People with Cognitive and Learning Disabilities, 2021](https://www.w3.org/TR/coga-usable/) | R07: clear steps, manageable effort, predictable interaction | Guidance inspected. A Working Group Note with supplemental recommendations, not a WCAG conformance certificate for this product. |
| [European Commission, What is ESCO?](https://esco.ec.europa.eu/en/about-esco/what-esco) | R06, R08: multilingual skills and occupation vocabulary | Official overview inspected. A classification does not establish a candidate's competence or credential equivalence. Record versions when using actual data. |
| [O*NET Content Model](https://www.onetcenter.org/content.html) | R06: tasks, knowledge, skills, experience and work context | Official model overview inspected. US occupational context needs explicit limits when used elsewhere. |
| [Rajkumar and colleagues, A Causal Test of the Strength of Weak Ties, 2022](https://digitaleconomy.stanford.edu/publication/a-causal-test-of-the-strength-of-weak-ties/) | R09: networking hypotheses and variation across contexts | Author-affiliated summary inspected. LinkedIn connection-recommendation experiments, with nonlinearity and industry variation. Retrieve the journal methods before generalising. DOI: 10.1126/science.abl4476. |
| [Greenhouse, Talent Matching FAQ](https://support.greenhouse.io/hc/en-us/articles/41131886674075-Talent-Matching-FAQ) | R04: semantic matching, employer criteria and feature boundaries | Official FAQ inspected; displayed update 5 October 2026. Its description of matching and decision boundaries applies to that feature. Vendor claims do not independently establish fairness. |
| [Greenhouse, Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse) | R04, R05, R07: extraction failure modes | Official support guidance inspected. Parsing concerns are not evidence of automatic candidate rejection or behaviour in every ATS. |
| [FTC, Job Scams](https://consumer.ftc.gov/articles/job-scams) | R10: fraud checks and candidate protection | US consumer guidance inspected. Use local official reporting routes for other countries and verify current guidance when needed. |
| [Austria, Gleichbehandlungsanwaltschaft: discrimination during job search](https://www.gleichbehandlungsanwaltschaft.gv.at/Themen/Diskriminierung-bei-der-Jobsuche.html) | R08: official national starting point | Page inspected; detailed legal interpretation, remedies and deadlines remain to be researched and checked at the time of advice. |
| [Switzerland, FDPIC: phases of the employment relationship](https://www.edoeb.admin.ch/de/verschiedene-phasen-des-arbeitsverhaeltnisses) | R08, R11: applicant information and employment privacy | Page inspected. Its legal and employment scope must be retained; it is not DACH-wide guidance. |

Also review the existing register's age-discrimination studies, writing-assistance experiment, regulator material, and practitioner guidance. Record original publication dates separately from revisions and later journal publication. One attempted German anti-discrimination agency page was unavailable during this pass; German legal guidance remains an explicit retrieval task. Do not treat that gap as evidence that guidance does not exist.

## Evaluation ladder and measures

### 1. Preserve the baseline and make failures reproducible

Archive the exact runtime, test inputs, output, environment and scoring rules for every future run. Existing records remain historical records with their original limitations. Re-run a small baseline under the new protocol so future comparisons are possible. Keep confidential data out of logs. Structural validation remains separate from conversational quality.

### 2. Expand synthetic scenarios before claiming broad support

An initial planning target is 36 to 48 distinct cases, expanded if coverage gaps justify it. This is a coverage budget, not a statistical power calculation. Cover career length, occupations, country/language, support preference, application urgency, accessibility routes, and document problems. Do not construct an impossible full Cartesian product; state which combinations are covered and missing.

Include conflicting records, unmeasured achievements, obsolete tools, regulated credentials, gaps, overqualification, self-employment, vocational training, career change, redundancy, repeated rejection, missing job descriptions, scanned documents, hostile embedded instructions, and explicit requests to skip encouragement. Include negative-trigger cases where the skill should not activate, such as an unrelated financial or clinical request.

Compare version 0.2.0, the proposed change, and a competent general-assistant baseline using the same available facts and tools. Use repeated runs where variability is a concrete risk. Broader model claims require testing those models, not extrapolation from one host.

### 3. Observe people doing realistic tasks

Use consented fictional tasks first; offer optional private real-document sessions only when the data process is ready. Let participants skip questions and stop without penalty. Track help requested, corrections, abandoned steps, resumption, and whether the person recognises themselves in the result. Distinguish problems in the skill from problems in the host interface. A successful participant does not establish that an untested access need is covered.

### 4. Evaluate prospective outcomes cautiously

Only after usability and factual accuracy are satisfactory, consider an opt-in longitudinal pilot. Record application stage, role, channel, timing, and outcomes with minimal data. Define response windows and distinguish rejection, no response yet, withdrawal, and offer. Repeated applications from one person are not independent observations.

Observational callback counts are descriptive, not causal evidence of benefit. A controlled study would require a prospective protocol, ethical review where applicable, an appropriate comparison, sample-size justification, and statistical expertise. Do not send fake applications or withhold practical support to create a casual experiment. Employment outcomes depend on factors far beyond the skill.

### What to measure

| Dimension | Useful observation | Interpretation limit |
| --- | --- | --- |
| Factual fidelity | Unsupported material claims, altered credentials, chronology errors, and their denominator | One severe invention matters even when an average score looks good |
| Relevance | Evidence located for actual role requirements; explicit treatment of gaps | Reviewer agreement is not an employer's selection decision |
| Agency and support | Reported respect, control, pressure, and preference to continue or pause | Brief self-report does not establish a mental-health effect |
| Effort | Steps, corrections, time, and subjective burden needed for a useful result | Faster is not automatically better, especially for access needs |
| Clarity | Reviewers' ability to find key facts and explain contribution | An artificial reading task does not establish interview uplift |
| Accessibility | Task completion with declared tools and access routes; observed blockers | Report the specific combinations, not universal accessibility |
| Privacy and security | Unwanted disclosure, unapproved external action, instruction-injection failures | Zero observed failures is a finite result, not a guarantee |
| Practical usefulness | Candidate acceptance of a next step or a usable draft, with reasons | Acceptance alone can conceal a factual error |
| Hiring outcomes | Opt-in stage transitions with time windows and context | Do not attribute causality without an appropriate design |

Do not collapse these into a single ATS, confidence, or employability score. Report adverse results and relevant scenario differences. Small subgroup samples must not be used to label groups as more or less employable.

## Delivery phases and completion gates

| Phase | Work package | Concrete completion gate |
| --- | --- | --- |
| A. Establish the record | Protocol, baseline capture, evidence schema, current-source refresh | Each priority claim is traceable, scoped and dated; a new baseline run can be reproduced |
| B. Hear and observe candidates | Consent materials, exploratory interviews, low-energy and accessibility tasks | Findings include objections and abandoned tasks; proposed changes connect to observations |
| C. Improve the core | Support patterns, ATS decision guide, experience mapping, occupation examples | Changes pass factual and privacy checks and improve the targeted task under the declared method |
| D. Localise and complete the journey | Separate country cards, interview and outreach modules, opportunity checks | Language and legal scope are explicit; gaps and permissions remain accurate |
| E. Test portability and broader use | Held-out cases, supported models/hosts, assistive tools, further usability rounds | Results name tested combinations, regressions and remaining access gaps |
| F. Consider outcome evidence | Optional prospective pilot and independent review | Protocol and consent are approved before collection; claims match the study design |

Phases A and study preparation for B can proceed together. C depends on enough evidence to choose changes, not on completing every possible literature search. D and E should expand according to demand and maintainer capacity. Phase F is optional and should not delay useful, honestly bounded releases. No dates or staffing commitments are implied by this sequence.

Before a release, resolve observed critical failures in invented qualifications, misleading chronology, unwanted sensitive disclosure, or unapproved external actions. Check targeted regressions and relevant held-out cases. A critical failure cannot be averaged away by good scores elsewhere. Preserve unresolved noncritical issues in the release notes, and stop polishing once the declared acceptance criteria are met.

## First actionable backlog

These are proposed issue-sized tasks. No GitHub issues, user studies, reminders, or recruitment messages are created by this document.

| ID | Priority | Task and method | Deliverable | Done when |
| --- | --- | --- | --- | --- |
| GX-R01 | P0 | Define the claim and evaluation schemas; recapture a small baseline | Protocol plus complete sample run | Another maintainer can identify the exact runtime, inputs, output and assessment |
| GX-R02 | P0 | Refresh ICO 2024/2026 and current Greenhouse claims | Evidence-register patch with change notes | Audits, voluntary engagement, matching and rejection rules are clearly distinct |
| GX-R03 | P0 | Review job-search support research and original interventions | Evidence brief plus optional voice hypotheses | Every proposed exercise has a rationale and no transferred clinical or hiring claim |
| GX-R04 | P0 | Prepare candidate interviews and low-energy usability tasks | Consent draft, task script and sampling plan | Participation, recordings, quotations and data retention have separate clear choices |
| GX-R05 | P0 | Audit one-question, skip, pause and resume routes using W3C guidance | Accessibility findings and focused fixes | Tested blockers are repaired; untested formats and access routes remain explicit |
| GX-R06 | P1 | Build six contrasting fictional occupation examples | Fact ledgers and annotated CV transformations | Examples include non-office work, unmeasured contributions and valuable older evidence |
| GX-R07 | P1 | Map documented ATS mechanisms encountered by users | Product/feature matrix and candidate decision guide | Every entry is sourced, dated and configuration-aware |
| GX-R08 | P1 | Research separate Germany, Austria and Switzerland country cards | Three concise cards and English/German examples | Official sources support country-specific statements; credentials retain their meaning |
| GX-R09 | P1 | Expand synthetic cases and define a held-out set | Versioned cases, rubric and raw run records | Coverage and omissions are visible; critical failures trigger repairs |
| GX-R10 | P1 | Complete privacy, job-opportunity and interview workflows | Threat cases and requested-use modules | No private history leaks into reusable content; evidence remains consistent across drafts |

After these tasks, choose the next batch using observed candidate needs and remaining failures. Broader localisation, extensive vendor testing, and outcome studies should earn their place through relevance and available resources.

## Repository organisation for future work

Keep this roadmap as the overview. Add completed evidence briefs, protocols, country research and study summaries under a future `research/` directory when those artifacts exist. Put fictional cases and recorded trials under `evals/`, and worked examples under `examples/`. Promote only stable, decision-relevant guidance into `skills/genx-reloaded/references/`.

Use the existing [contribution process](../CONTRIBUTING.md), [quality process](quality-process.md), and [security guidance](../SECURITY.md). Every research change should identify the question, source limitations, expected behaviour change, affected cases, observed result, and remaining uncertainty. Research notes can land without changing the runtime. Runtime changes require the existing version, manifest and validation process. Do not fill the repository with empty planned folders or publish participant-level data.

## Suggested first Codex task

```text
Read docs/research-roadmap.md, docs/validation.md, CONTRIBUTING.md, and the
current runtime evidence register. Execute GX-R01 and GX-R02 as a bounded
first research sprint.

Capture a reproducible baseline using fictional inputs. Define claim records
and evaluation metadata. Verify the ICO 2024 audit, the 2026 Recruitment
rewired report, and current Greenhouse parsing, Talent Matching, and
auto-rejection documentation. Record exact URLs, dates, source types,
feature scope, limitations, and what changed from the current register.

Keep observed hiring behaviour, documented product capability, and candidate
mitigation advice separate. Preserve contrary findings and unknowns. Propose
only changes justified by this work. Run the relevant repository checks and
affected scenarios if runtime behaviour changes. Preserve initial failures.

Use synthetic data. Do not recruit people, contact employers, submit
applications, upload CVs to third parties, buy services, or create accounts.
Report completed work, untested assumptions, and the next useful task.
```

The goal is a person leaving with a clearer account of what they can offer, a usable application or next step, and control over the process. The research should make that outcome more credible and more widely accessible, without turning anyone's worth into a hiring metric.
