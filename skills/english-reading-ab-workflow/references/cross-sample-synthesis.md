# Cross-sample synthesis reference

Use this reference only for the `Cross-sample synthesis` mode of `english-reading-ab-workflow`.

## Preconditions

The user must explicitly specify the comparison scope. Each included item must be a completed `-comparison.md` with matching `-baseline.md` and `-skilled.md`, workflow metadata, a source identifier, `## 7. Improvement candidates`, and `## 8. Recommendation`.

Exclude and report files that are incomplete, duplicated by article ID, inconsistent with their paired source identifier, or outside the explicit scope. Do not read unlisted comparisons to search for stronger evidence.

## Synthesis artifact

Save one report as `reports/ab-synthesis/ABS-YYYYMMDD-NNN.md`. Begin with hidden metadata that records:

- `synthesis_id`, `workflow_skill`, `workflow_skill_version`, `companion_skill_versions`, `generated_at`, and `status`;
- requested comparison paths; included and excluded article IDs; and the regression report identifier.

Use this outline:

1. **Executive conclusion**
2. **Scope and input ledger** — requested, included, excluded, and why
3. **Sample diversity map** — article ID, text type, relevant difficulty, candidate labels
4. **Candidate normalization** — original wording and normalized mechanism
5. **Evidence matrix** — candidate × article ID, concrete skilled gain, baseline advantage, boundary/risk
6. **Status decisions** — Article-specific, Candidate, Validated pattern, or Non-findings
7. **Recommended action**
8. **Authorization boundary** — no automatic skill, version, or article modification

## Status rules

| Status | Required evidence |
|---|---|
| `Article-specific` | One text only, or a mechanism tied to that text's unique facts. |
| `Candidate — needs more samples` | Plausible mechanism but fewer than three distinct IDs, insufficient diversity, or conflicting evidence. |
| `Validated pattern — eligible for proposed update` | At least three distinct IDs; concrete evidence in each comparison; meaningful topic, structure, or learning-difficulty differences; gain beyond formatting; and an explicit boundary/risk. |
| `Non-findings` | A suspected pattern lacks support, conflicts across samples, or cannot be normalized honestly. |

Distinct IDs are necessary but insufficient. Explain why the samples are not merely duplicates by topic or form. Never count more headings, more words, or a newer companion version as evidence of improvement.

## Safety and authority boundary

A synthesis evaluates evidence. It can propose a separate skill-update document, but cannot edit a companion skill, change a version, regenerate a reading, or rewrite a comparison. Those actions require their own user authorization.
