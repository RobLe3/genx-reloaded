# SmartRecruiters

Checked 12 October 2026. Scope: official integration/API documentation, not a tested candidate UI.

**Documented:** [Application API](https://developers.smartrecruiters.com/docs/application-api-1) supports application collection on employer sites or job boards, including job-specific questions and privacy information. [Parse a resume](https://developers.smartrecruiters.com/reference/candidatesresumeparse) distinguishes unparseable documents, such as images, from resumes missing required parse information.

**Help the candidate:** Identify whether the error arose on a partner surface, the employer's page, or a SmartRecruiters page. For an unreadable-file error, inspect selectable text and supply an accepted text-based document. For incomplete data, inspect essential contact and profile information rather than adding keywords. Review questions and the employer notice at the actual point of application. Verify a job-specific receipt.

**If blocked:** Ask the employer/portal's documented support route to check the submitted application and attachment. Candidate-editability mentioned in API documentation is not proof that a particular UI exposes the same control at every stage.

**Avoid:** Asking applicants to call authenticated APIs, requesting developer credentials, or treating API error names as confirmed causes without seeing the actual error. No universal scoring threshold, consumer-facing file limit or fairness result was established here.
