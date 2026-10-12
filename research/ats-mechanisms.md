# ATS mechanisms, checked 12 October 2026

This matrix documents capabilities, not deployment prevalence or candidate outcomes. No employer-side environment was accessed. Product statements are vendor documentation, not independent fairness validation.

| Product / feature | Documented mechanism | Candidate implication | Boundary |
| --- | --- | --- | --- |
| Greenhouse Recruiting, parsing | Extracts fields; some layouts can produce partial extraction | Inspect actual populated fields and correct errors where possible | Failure can require manual entry; it is not itself a rejection decision |
| Greenhouse Talent Matching | Compares related terms with configured criteria and places candidates in categories | Describe genuine skills and context accurately | The feature does not itself advance or reject candidates; more terms need not improve the category |
| Greenhouse Talent Matching, optional opt-out | Employer-enabled alternative review flow | Inspect the actual notice and available control | Do not promise this is enabled for every application or covers other tools |
| Greenhouse auto-reject | Configured answers to application questions can trigger rejection | Answer accurately and clarify ambiguous requirements | CV editing cannot supply a missing qualification |
| Lever parsing | Official help article reached only a loading/CSS-error shell | Follow actual form instructions and verify fields | Behaviour and limits remain unverified here |
| Workday, SAP SuccessFactors, Personio, SmartRecruiters | Not researched in this release | Consult current official documentation when relevant | No feature or compatibility claim |

Sources and exact feature scope: GX-C03, GX-C04 and GX-C05 in [claims.json](claims.json). Lever attempted URL: https://help.lever.co/s/article/Understanding-Resume-Parsing, no substantive content retrieved.

Keep independent assessments and human review as additional stages whose use is employer-specific. Do not infer an employer's configuration from its application-page brand. If a candidate asks "was it the ATS?", distinguish the response actually received from unobserved mechanisms.
