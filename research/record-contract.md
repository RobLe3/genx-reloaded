# Research record contract, version 1

`claims.json` contains `schema_version`, `checked_on`, `review_kind` and `claims`. Each claim has a unique `id`, `workstream`, `statement`, `source_url`, `source_title`, `publisher`, `publication_date`, `checked_on`, `evidence_type`, `scope`, `inspection`, `limitations`, `candidate_action`, `mitigation_tested`, `status`, `review_trigger`, `reviewer` and `related_cases`.

Dates are ISO calendar dates where known. `publication_date` may be a year, year-month, or null when not established; never fill an unknown with the retrieval date. `evidence_type` distinguishes study, synthesis, official guidance, law, vendor documentation, and retrieval lead. `status` is supported-within-scope, promising-untested-here, mixed, outdated, or unknown. `mitigation_tested` describes the specific intervention or says it was not tested; it is not a general source-quality score. Case IDs reference the scenario catalogue, not evidence of execution.

`python scripts/validate_research.py` checks required fields, status/type values, dates, URLs, unique identifiers and case references. It does not decide whether a source is true or whether a candidate-facing recommendation follows from it. A human or agent must inspect the source and state the inference.

The [evaluation protocol](../evals/protocol.md) defines the separate run record. Research evidence, fictional scenario design, recorded executions and human studies must never share a single pass count.
