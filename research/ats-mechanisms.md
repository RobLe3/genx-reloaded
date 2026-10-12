# ATS mechanisms, checked 12 October 2026

The [0.3.0 matrix](ats-mechanisms-v0.3.0.md) is preserved. The current [fourteen-product coverage map](ats-coverage.md) identifies sources, useful distinctions and limits. No employer environment was accessed.

| Layer | Documented examples | What a candidate can check | What cannot be inferred |
| --- | --- | --- | --- |
| Origin and transmission | SmartRecruiters partner API, Workable LinkedIn origin, Teamtailor Mailbox | Selected file, source form, destination and receipt | Email/referral/job-board use bypasses screening |
| File extraction | Greenhouse, Recruitee, Personio | Text, layout, contact identity and populated data | An attached file parsed correctly |
| Structured profile | Workday reuse, SAP custom-field limitation, iCIMS profile steps | Dates, qualifications, languages and job-specific submission | Profile completion is application completion |
| Eligibility rules | Greenhouse, Oracle Recruiting, Workable | Actual question and truthful response | A particular quick rejection had this cause |
| Matching and review assistance | Greenhouse Talent Matching, Ashby criteria, configured Workday skills features | Evidence clarity and the employer's disclosure | Universal score, threshold, deployment or fairness |
| Human review and workflow | Configured statuses, tasks and notifications | Outstanding tasks and explicit feedback | Status text proves a human read the CV |
| Corrections and privacy | Workable update/withdrawal, PageUp employer support | State-specific correction route and current notice | Profile edits propagate or withdrawal is harmless |

Sources: GX-C03 to GX-C05 and GX-C29 to GX-C46 in [claims.json](claims.json). Product-specific claims are bounded by their recorded source scope. Proposed candidate actions are practical inferences, not measured hiring remedies. An optional AI control for one feature does not disable all processing, and a vendor's product description is not independent validation.
