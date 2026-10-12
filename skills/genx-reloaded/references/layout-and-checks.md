# Layout and checks

Use these as conservative design defaults. They are not universal ATS requirements.

## Structure

- Prefer one main text column, recognisable section headings, and a clear employer/title/date relationship.
- Use reverse chronology for experience, with accurately labelled project or earlier-career sections where helpful.
- Put name and contact details in the main document body. Avoid placing essential content only in headers, footers, icons, text boxes, images, or a QR code.
- Keep headings such as Experience, Projects, Skills, Education, and Qualifications appropriate to the application language.
- Use restrained emphasis, adequate white space, and readable text. A practical starting point is 10.5-12 point body type, adjusted for the actual font and rendering.
- Treat two pages as a useful commercial-CV starting target, not a law. Do not remove essential evidence or shrink text merely to comply.
- Avoid skill bars, star ratings, and decorative charts for core qualifications. Describe level and use instead.
- Follow the employer's stated format and size requirements. Keep editable source files. Export a text-based PDF if appropriate; provide DOCX when requested.
- Do not state that PDF, DOCX, tables, or colour are universally accepted or rejected.

## Market and role differences

- Ask or infer the market from the task; do not impose US conventions globally.
- For German applications, distinguish a chronological, tabular style from implementing the whole document as a complex Word table.
- Treat photos and personal details according to candidate preference and current market requirements. Do not infer a legal requirement from a local custom.
- Preserve vocational qualifications and titles faithfully; do not convert them into unsupported academic equivalencies.
- Preserve licenses, current registration, security-clearance status, and expiration information when relevant. Verify legal or regulated-role assertions against current official sources.
- Academic, public-sector, regulated, and complete-history applications may legitimately need more detail than a short commercial CV.
- Keep health, disability, family, and career-break disclosures under the person's control.

## Use the local preflight script

Run from this skill's directory or use the script's absolute path:

```bash
python scripts/cv_preflight.py /absolute/path/cv.docx --require "Candidate Name" --require "Actual Employer" --report /scratch/cv-check.json --text-out /scratch/cv-text.txt
```

Use actual writable scratch paths. Do not overwrite the CV or store candidate text inside the skill directory.

The script:

- Extracts body text from DOCX, text from PDF using pypdf, or reads UTF-8 TXT/Markdown.
- Checks supplied expected strings after case, Unicode, dash, and whitespace normalisation, with alphanumeric boundaries so SQL does not match NoSQL.
- Flags little or no extractable text, and sparse PDF pages, for inspection.
- Reports DOCX tables, columns, text boxes, header/footer-only email or expected text, hidden text, tracked changes, and stored comments or comment markers as review observations. Comment text and authors stay out of extraction and findings.
- Excludes directly hidden runs and deleted/moved-from text from the DOCX extraction. Flags hidden settings in styles, but does not resolve full Word style inheritance.
- Protects the source against output paths that alias it, including symbolic and hard links.
- Writes a JSON report, with full extracted text only when --text-out is supplied. The report includes the input path and requested strings; handle it as candidate data too.
- Does not use a network, evaluate merit, infer age, rank candidates, OCR scans, inspect all PDF visual features, or emulate a vendor's ATS.

Exit code 0 means inspection completed, even if the result is review_needed. Exit code 1 means inspection failed; exit code 2 indicates CLI usage errors. Inspect the JSON status and findings, not just the exit code.

## Manual checks still required

1. Compare the CV's names, employers, titles, dates, quantities, qualifications, and scope against the source.
2. Render DOCX/PDF with the applicable artifact skill and inspect every page for legibility, clipping, broken sections, and awkward page breaks.
3. Read the extracted text from beginning to end. Confirm chronology and associations, not merely that each word is present.
4. Verify essential facts survived export. Review and delete private Word comments from a submission copy, preserving the original. Hiding markup or resolving a thread does not delete it. Recheck the saved copy; this helper is not a complete metadata/privacy inspector. Microsoft documents [comment resolution versus deletion](https://support.microsoft.com/en-gb/word/mark-comments-as-done) and [Document Inspector](https://support.microsoft.com/en-gb/office/collab-files/remove-hidden-data-and-personal-information-by-inspecting-documents-presentations-or-workbooks?nochrome=true), checked 12 October 2026. Document Inspector availability varies by host.
5. Check links locally for correct targets. Check live destinations when authorised and relevant, without uploading private CV content.
6. For a real application, review any populated form fields and all mandatory questions before submission.

Passing these checks means the local document was inspected. It does not certify the employer's extraction, matching, or hiring decision.
