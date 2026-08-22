---
name: english-reading-ab-workflow
description: "Run a controlled English Reading A/B workflow: compare baseline and skilled analyses for one source text, or synthesize evidence from an explicitly specified set of completed comparison reports. Use when the user asks for 双轨伴读, 英语伴读 A/B, baseline versus skill, cross-sample synthesis, or to evaluate and improve the English Reading Companion skill from evidence."
---

# English Reading A/B Workflow

**Current version:** 1.2.0
**Release:** 2026-08-22 · REG-20260822-002

Produce either a reproducible comparison from one authoritative source text, or a reproducible synthesis from an explicitly specified set of completed comparison reports. Do not conflate the two modes.

## Version visibility

- Read this skill's `VERSION` and require it to match the version declared above.
- Locate the installed `english-reading-companion` package and read only its `VERSION` file before starting the baseline. Do not read its `SKILL.md` or method references until the skilled branch begins.
- Begin the user-visible workflow response with:

  `> Skills: english-reading-ab-workflow v1.2.0; english-reading-companion v<installed-version>`

- Record both versions in every comparison or synthesis artifact. Record `workflow_skill` and `workflow_skill_version` in all workflow artifacts; record `skill` and `skill_version` in the skilled artifact.
- Stop and report the blocker when either version is missing, malformed, or inconsistent. Never infer a version from memory.

## Mode selection

Use **Single-article comparison** when the user supplies one authoritative source text or asks for baseline/skilled/comparison outputs. Use **Cross-sample synthesis** only when the user explicitly asks to aggregate completed comparison reports and explicitly provides comparison paths, article IDs, or an approved directory range. Do not default to scanning all `content/readings/`.

## Single-article comparison

### Required outputs

Create exactly these files unless the user requests different names:

1. `<number>-<slug>-baseline.md`
2. `<number>-<slug>-skilled.md`
3. `<number>-<slug>-comparison.md`

Use the article number when supplied; otherwise omit `<number>-`. Derive a short lowercase hyphenated slug from the English title. Preserve leading zeroes such as `009`.

Save all three as user-facing artifacts and return a separate download link for each. Keep temporary processing outside the deliverables.

### Execution contract

### 1. Normalize the shared input

- Treat the user's latest text or image as authoritative.
- Extract title, author/source, article number, and body.
- Correct obvious OCR artifacts only when certain.
- Record any meaning-changing uncertainty identically in both analyses.
- Freeze this normalized source before either branch begins. Do not silently use different source text between branches.

### 2. Run the baseline branch

Generate the baseline first using [references/baseline-spec.md](references/baseline-spec.md).

During this branch:

- Do not invoke, quote, imitate, or consult the English Reading Companion skill.
- Do not use its fixed Story / Language / Thinking / Beyond the Words framework.
- Do not intentionally make the baseline weak or incorrect.
- Reproduce the user's earlier general companion style: competent natural analysis centered on story comprehension, selected vocabulary or expressions, theme, and a memorable sentence.
- Let article difficulty determine whether a difficult sentence receives extra explanation.
- Judge the baseline on correctness, not on whether it resembles the skilled version.

Write and finalize the baseline file before starting the skilled branch. Do not revise it after seeing the skilled output.

### 3. Run the skilled branch

Locate and apply the installed skill whose frontmatter name is `english-reading-companion`.

- Follow that skill and its referenced method files faithfully.
- Confirm its `SKILL.md` version declaration matches the `VERSION` value read before the baseline.
- Use the same normalized source as the baseline.
- Generate a complete standalone analysis; do not mention the baseline or the comparison experiment.
- Write and finalize the skilled file before comparing.

If the companion skill cannot be located, stop after preserving any completed baseline and report the blocker. Do not fabricate a skilled result from memory.

### 4. Run the comparison branch

Read both finalized analyses and apply [references/comparison-rubric.md](references/comparison-rubric.md).

The comparison must:

- compare actual passages and omissions from the two outputs;
- distinguish content gains from formatting gains;
- identify what the skill discovered that the baseline missed;
- identify anything the baseline did more clearly, efficiently, or naturally;
- measure reader workload qualitatively;
- evaluate any English-to-English meaning bridge and active-output support required by the installed companion, without treating extra English or extra prompts as automatic gains;
- distinguish observed scaffold usability from unmeasured learner outcomes such as retelling accuracy, transfer, or delayed recall;
- produce evidence-based skill improvement candidates;
- separate one-article observations from recurring-pattern candidates.

Never claim improvement merely because the skilled document is longer or has more headings.

### 5. Verify the artifact set

Before delivery, confirm:

- all three files exist and are valid UTF-8 Markdown;
- filenames share the same number and slug;
- displayed and recorded skill versions match the corresponding `VERSION` files;
- both analyses use the same source text;
- the baseline contains no companion-only fixed framework or bundled-mechanism leakage;
- the skilled file is understandable without the comparison report;
- the comparison cites concrete differences from both files;
- no recommendation was silently applied to the companion skill.

### Iteration policy

Treat the comparison report as evaluation evidence, not automatic authorization to update the English Reading Companion skill.

Classify recommendations:

- **Article-specific** — useful only for the current text; do not propose a skill change.
- **Candidate** — plausible general improvement requiring more samples.
- **Validated pattern** — repeated across at least three sufficiently different articles or explicitly confirmed by the user; suitable for a proposed skill update.

Do not edit or update `english-reading-companion` unless the user separately authorizes that change after reviewing the evidence.

### Default interaction

- If the user supplies a complete article, proceed without asking for template choices.
- If the article number is missing, omit it rather than blocking.
- If the title is missing, use a short content-derived slug and label the title as untitled.
- If the user asks only to test the workflow, still create the three files.
- Keep chat delivery concise: list the three artifacts and summarize only the most important comparison finding.

## Cross-sample synthesis

Read [references/cross-sample-synthesis.md](references/cross-sample-synthesis.md) before starting this mode.

### Required output

Create one independent Markdown artifact under `reports/ab-synthesis/` named `ABS-YYYYMMDD-NNN.md`. It is an evaluation artifact, not a full companion and not a replacement for any single-article comparison.

### Input and isolation contract

- Use only the comparison files in the user's explicit scope. Record every requested, included, and excluded path.
- Verify that every included comparison has matching baseline and skilled artifacts, workflow metadata, a source identifier, `## 7. Improvement candidates`, and `## 8. Recommendation`.
- Reject duplicate article IDs, inconsistent source identifiers within one artifact set, missing required comparison sections, or a request to mark a pattern validated from fewer than three included articles. Report concrete exclusions; do not silently use partial evidence to upgrade a status.
- Never revise a frozen baseline, skilled, or comparison file during synthesis.

### Synthesis decision rules

- Normalize differently worded candidates only when their mechanism, expected benefit, and boundary genuinely match. Preserve the original candidate wording and source article IDs in the evidence matrix.
- Mark a pattern `Validated pattern — eligible for proposed update` only when at least three distinct article IDs provide concrete comparison evidence and the report explains meaningful sample differences in topic, structure, or learning difficulty. Length, headings, or repeated versions alone are not diversity evidence.
- Keep article-specific, insufficient, conflicting, or overgeneralized observations under `Article-specific`, `Candidate — needs more samples`, or `Non-findings` as appropriate.
- A synthesis may recommend a separately reviewable skill-update proposal. It must state that no skill, version, or existing article was modified by the synthesis.

### Delivery

Return the synthesis artifact link and a concise account of included/excluded samples, status decisions, and next recommended action. Do not claim a companion-skill update merely because a pattern became eligible for a proposal.
