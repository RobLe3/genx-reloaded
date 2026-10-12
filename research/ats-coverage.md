# ATS coverage and insights, 0.4.0

Checked 12 October 2026. **Fourteen scoped product cards, not an exhaustive ATS directory.** This bounded expansion follows the requested international and vendor-specific support. Sources are official documentation; no employer tenant, real application or commercial scanner was used. Read [mechanisms](ats-mechanisms.md), [claim records](claims.json) and [search log](search-log.md) for provenance and limits.

| Product | Inspected scope | Candidate-relevant insight | Main uncertainty |
| --- | --- | --- | --- |
| Greenhouse | Parsing, Talent Matching, auto-reject | An attached file, AI category and question-triggered rejection are different events | Employer feature settings |
| Workday | Administrator training, external applications and Candidate Home | Reused fields and configured skills features need separate checks | Training versus tenant release/configuration |
| iCIMS | Candidate portal guide | Profile/talent-pool completion may precede an actual job application | Employer's enabled dashboard options |
| Oracle Fusion Recruiting | Partner import and disqualification questions | Parser arrangements can vary; eligibility answers can be decisive | Enabled package and rules |
| Oracle Taleo Enterprise | 23D application-flow blocks | General profile, text resume and job attachments can be distinct | Older version, current tenant unverified |
| SAP SuccessFactors | Public KBA on missing fields | Blank custom fields need not indicate a malformed CV | Current release and field configuration |
| SmartRecruiters | Application and parse APIs | The visible job board may not be the downstream application system | Candidate UI differs from developer API |
| Workable | Candidate import/update help, auto-disqualification | Check saved job-board files; withdrawal can cancel active invitations | Review state and origin surface |
| Ashby | AI-Assisted Application Review | Employer criteria and notice settings matter; human and AI scores differ | Enabled feature and actual criteria |
| Recruitee | Parsing troubleshooting | Combined dossiers can cause the wrong contact to be extracted | Route and document dependence |
| Teamtailor | Mailbox ingestion | Email can enter the ATS and be parsed | Whether this mailbox route was used |
| Personio | Textkernel-based CV parsing | Derived attributes may need correction; employer controls are not applicant controls | Deployment, accuracy and downstream use |
| PageUp | Applicant FAQ | Employer-specific recovery and support are central | Parser/ranking not established |
| Lever | Official search extracts; direct help retrieval failed | Use the real form and keep claims conditional | Full current specification unavailable |

The executable workflow is in [ATS troubleshooting](../skills/genx-reloaded/references/ats-troubleshooting.md); all product cards are linked from [SKILL.md](../skills/genx-reloaded/SKILL.md). A card's existence is not evidence of a passed live test.

## What changes the advice

1. **Submission state matters.** Repairing a draft is different from withdrawing a submitted application with an interview attached. Preserve the existing application when a correction route is available.
2. **Data can differ between surfaces.** A saved job-board file, parsed profile and job-specific attachment are separate things to check. Do not assume updates propagate backwards.
3. **Formatting is only one mechanism.** Eligibility questions, configured review criteria, incomplete submissions and account failures cannot all be repaired by adding keywords.
4. **A vendor's capability is not an employer's configuration.** Look for the actual notice, field and error. Absence of a visible score does not establish absence of automation; presence of automation does not establish a rejection cause.
5. **Older experience should remain attributable.** Clear role boundaries and dates make depth easier to understand without fabricating recency or replacing a person's identity.

These are practical inferences from documented mechanisms. Their effects on interviews or bias have not been measured.

## Multiple sources, different purposes

Combine official candidate help, administrator specifications, integration documentation, employer instructions, observed errors, and the existing regulator/study evidence. Do not flatten them into one authority ranking: API documentation can explain integration but cannot prove a button exists in a candidate UI; a regulator audit can identify governance risks but cannot diagnose one application. Community reports remain leads until corroborated.

## Expansion and refresh rules

For an uncovered product, first identify the candidate's concrete issue and current surface. Potential follow-ups include Avature, Bullhorn, Jobvite, BambooHR, Pinpoint, JobAdder and separate assessment/matching providers. These names are a backlog, **not researched coverage or market-share claims**. Build a new card only after inspecting the relevant current primary material, recording scope and failed retrieval, and adding a realistic scenario. Do not assume assessment vendors are the ATS.

Recheck when documentation changes, a candidate reports contradictory behaviour, a live screen differs, or before consequential advice about withdrawal, limits, AI controls or rights. Without fresh access, keep cached dates visible and actions reversible. The skill can help with an unknown system without inventing its internals.
