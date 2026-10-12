# Installation and verification

## Portable use

Clone the repository and ask a file-capable agent to read `skills/genx-reloaded/SKILL.md`. Supply a CV or career notes, and a vacancy if tailoring is wanted. The agent follows the entry point and reads only relevant references.

The core workflow is text. It has no Python, network, or external account requirement. Current research verification needs browsing; final PDF or Word production needs suitable host tools. When these are unavailable, the skill should provide useful text and name the missing check.

## Install into a skill-capable host

Copy the complete `skills/genx-reloaded` directory into the skill directory supported by your host. Keep its name `genx-reloaded`, and preserve `references`, `scripts`, `assets`, and `agents` underneath it. Do not copy evaluation answers into the runtime.

Before replacing an existing installation, preserve your local changes and compare versions. Avoid installing both the earlier `genx-ats-cv` copy and `genx-reloaded` as competing implicit skills. The earlier name is historical; no automatic alias is implemented.

Hosts use different discovery locations and refresh mechanisms. Follow the host's current instructions; this repository does not claim that every assistant can install a GitHub URL directly. `agents/openai.yaml` is optional host metadata, while `SKILL.md` is the portable entry point.

Where named invocation is supported, ask:

```text
Use $genx-reloaded. Here is my CV and the job description. Give me a focused rewrite, keep useful older evidence, and separate missing qualifications from wording problems.
```

If named invocation is not recognized, use the explicit entry-point path. Do not assume the skill loaded merely because the model produced a CV.

## Verify the checkout

From the repository root:

```bash
python -m pip install -r requirements-test.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

The repository validator checks declared runtime files and hashes, frontmatter and metadata agreement, local Markdown link targets, version agreement, and Python syntax. It does not test the agent's behaviour or contact websites.

The helper's runtime requirement is Python 3.9+. The recorded development run used Python 3.12.14 on Linux. Other Python versions, operating systems, models, and host integrations have not all been exercised.

## Smoke request

```text
Use the skill. Fictional example: I led six technicians through a network replacement at 11 sites in 2014. I want a network delivery role. Write one truthful CV bullet and tell me whether the date makes it irrelevant. Do not invent savings or call it a cloud migration.
```

Check that the result preserves the six technicians, 11 sites, and historical scope, and does not invent a financial outcome. This smoke check is illustrative, not a measured activation benchmark.

## Keep candidate files separate

Use a private working location for CVs, local reports, application records, and handovers. Do not write them under the runtime folder or commit them to the repository. The helper rejects outputs inside its own skill directory; it cannot enforce privacy across every folder on your computer.
