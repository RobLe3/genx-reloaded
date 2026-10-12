# Focused assessment, 0.4.0

12 October 2026. Maintainer/developer assessment, not independent adjudication. The checks in GX-37 to GX-45 were written before execution. Nine fresh-context agents received the skill path and their fictional request, without the checks, diagnosis or expected answer. The complete wrapper, raw prompt, response, file hashes and runtime snapshot are preserved per run. The skill snapshot was unchanged during these executions.

| Case | Observed result | Assessment against written checks |
| --- | --- | --- |
| GX-37, US federal resume | Rejected six-page folklore, used two-page guidance, kept 24 hours/week and supplied month/year dates, allowed relevant 2004 evidence and asked for missing identifiers | Met |
| GX-38, Belfast | Delivered three-sentence profile, omitted unnecessary personal/referee details, distinguished Northern Ireland from Great Britain and used current official routes | Met |
| GX-39, Montreal/Workday | Restored German vocational qualification and B1/C1, rejected invented degree/fluency, checked bilingual duties and preserved older overseas experience | Met |
| GX-40, Australia/PageUp | Delivered a 92-word pitch from both employment periods, no invented APS service/results; checklist separated pitch, CV, form and receipt | Met |
| GX-41, NZ/Recruitee | Followed two-referee request with agreed alternatives; explained possible combined-PDF contact extraction; drafted correction without current-employer contact or duplicate application | Met |
| GX-42, Workable/LinkedIn | Preserved active interview, recognised withdrawal cancellation, drafted employer correction and distinguished saved-origin files | Met |
| GX-43, SuccessFactors | Explained scoped custom/date limitations, suggested manual correction/support and retained vocational diploma rather than a degree | Met |
| GX-44, Greenhouse/Ashby | Separated Talent Matching and rule-based rejection, treated licence issue as plausible not proven, rejected checker/opt-out guarantees and duplicate-route tactics | Met |
| GX-45, Personio/Canada | Preserved name and dates, scoped inferred attributes to documented capability, identified employer-owned subcontractor setting and drafted neutral process question | Met |

No critical failure was observed in these nine answers. This is a finite qualitative result, not a measured reliability rate or superiority result. No comparison condition was run in this release. Previous baseline/control trials remain in the 0.3.0 record.

## Review notes and limits

- Raw response whitespace is preserved, including a Markdown hard break and terminal blank lines. The staged whitespace check reports these three artifact locations; non-artifact changes pass that check. Answers were not normalised merely to silence it.
- Responses were sometimes longer than the user's brevity request, particularly the US and Canada answers. Useful details and questions were retained; this is a polish limitation, not evidence that extra detail helps candidates.
- Text-only responses sometimes repeated a formal completion label. No unnecessary document test was claimed. A more conversational ending may be preferable in future human usability work.
- US missing job identifiers were clearly marked as draft placeholders rather than invented. Workable's email draft instructs the person to attach the corrected letter before using its attachment wording. Neither response was claimed to be submission-ready without those steps.
- Agents retrieved official sources as needed. Raw responses preserve host citation markers; those markers alone are not portable source archives. The reusable cards and research records retain ordinary source URLs. Complete tool transcripts were not archived.
- Exact provider model, sampling settings and execution start times are unavailable. Record timestamps reflect artifact capture. All agents ran in one host environment and were instructed not to inspect the other repository material, but there was no filesystem isolation or independent contamination audit.
- These are advice/drafting trials. No live upload, parser, employer rule, account change, withdrawal, submission, outreach, legal case or interview outcome was tested.
- Every new country was exercised once. Several vendor cards were not directly exercised: iCIMS, Oracle Fusion Recruiting, Taleo, SmartRecruiters, Teamtailor and Lever. No broad product compatibility claim follows. Catalogue GX-46 to GX-49 remains unexecuted.

The 49-case catalogue is not a list of 49 passed tests. Together with the distinct 0.3.0 cases, 14 catalogue cases now have recorded executions; this release adds nine single runs. Keep historical failures and scope unchanged.
