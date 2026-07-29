---
name: english-reading-ab-workflow
description: "Run a controlled three-output English Reading A/B workflow from one English source text: create a historical-style baseline analysis without applying the English Reading Companion method, create a skilled analysis that explicitly applies the installed English Reading Companion skill, and create a comparison report with evidence-based improvement candidates. Use when the user asks for 双轨伴读, 英语伴读 A/B, baseline versus skill, three English reading Markdown files, or wants to evaluate and iteratively improve the English Reading Companion skill from new articles."
---

# English Reading A/B Workflow

Produce a reproducible comparison from one authoritative source text. Generate three downloadable Markdown artifacts, not merely three chat sections.

## Required outputs

Create exactly these files unless the user requests different names:

1. `<number>-<slug>-baseline.md`
2. `<number>-<slug>-skilled.md`
3. `<number>-<slug>-comparison.md`

Use the article number when supplied; otherwise omit `<number>-`. Derive a short lowercase hyphenated slug from the English title. Preserve leading zeroes such as `009`.

Save all three as user-facing artifacts and return a separate download link for each. Keep temporary processing outside the deliverables.

## Execution contract

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
- produce evidence-based skill improvement candidates;
- separate one-article observations from recurring-pattern candidates.

Never claim improvement merely because the skilled document is longer or has more headings.

### 5. Verify the artifact set

Before delivery, confirm:

- all three files exist and are valid UTF-8 Markdown;
- filenames share the same number and slug;
- both analyses use the same source text;
- the baseline contains no companion-only fixed framework leakage;
- the skilled file is understandable without the comparison report;
- the comparison cites concrete differences from both files;
- no recommendation was silently applied to the companion skill.

## Iteration policy

Treat the comparison report as evaluation evidence, not automatic authorization to update the English Reading Companion skill.

Classify recommendations:

- **Article-specific** — useful only for the current text; do not propose a skill change.
- **Candidate** — plausible general improvement requiring more samples.
- **Validated pattern** — repeated across at least three sufficiently different articles or explicitly confirmed by the user; suitable for a proposed skill update.

Do not edit or update `english-reading-companion` unless the user separately authorizes that change after reviewing the evidence.

## Default interaction

- If the user supplies a complete article, proceed without asking for template choices.
- If the article number is missing, omit it rather than blocking.
- If the title is missing, use a short content-derived slug and label the title as untitled.
- If the user asks only to test the workflow, still create the three files.
- Keep chat delivery concise: list the three artifacts and summarize only the most important comparison finding.
