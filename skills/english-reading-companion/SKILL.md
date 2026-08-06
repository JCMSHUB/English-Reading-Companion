---
name: english-reading-companion
description: "Analyze English stories and short essays with the user's English Reading Companion method: understand the story first, then examine high-value language, authorial thinking, and non-literal meaning in Beyond the Words. Use when the user submits an English article, story, essay, speech, or excerpt and asks for 英语伴读, 伴读解析, 精读, reading companion, story/language/thinking analysis, Beyond the Words, or a continuation of the numbered English Reading Companion series. Also use when reviewing or revising an earlier companion analysis to match this method."
---

# English Reading Companion

**Current version:** 1.0.1
**Release:** 2026-08-06 · REG-20260806-002

Apply the user's stable reading method. Build English intuition rather than produce a translation or grammar lecture.

## Version visibility

- Read `VERSION` before producing any analysis and require it to match the version declared above.
- Begin every user-visible analysis with this exact line immediately after any YAML frontmatter and title:

  `> Skill: english-reading-companion v1.0.1`

- For every full-article companion, save the completed analysis as `content/readings/NNN-english-slug.md`; do not leave the result only in chat. Do this before sending the final handoff.
- Before generating, confirm the source text is available under `content/sources/`, and identify its three-digit article ID, lowercase English slug, and source title. If any is missing or ambiguous, stop and ask the user instead of inventing a filename or silently skipping the save.
- Save new analyses with `status: "draft"`. Never overwrite an existing companion file without the user's explicit confirmation.
- Set `skill: "english-reading-companion"` and `skill_version: "1.0.1"` in the saved file's YAML frontmatter.
- Include the same skill name and version in the concise chat handoff that links or summarizes a saved artifact.
- Stop and report a version mismatch instead of guessing which version is active.

## Core objective

Help the reader understand English as English across four connected layers:

1. **Story** — what happens, how the narrative moves, and where it turns.
2. **Language** — how meaning is packaged in chunks, collocations, idioms, syntax, and natural phrasing.
3. **Thinking** — what viewpoint, value, assumption, or way of seeing the world shapes the writing.
4. **Beyond the Words** — what the words mean in context beyond their literal surface.

Treat the four layers as a reasoning sequence, not four independent labels.

## Operating principles

- Understand the whole story before analyzing individual sentences.
- Explain meaning in context before discussing grammar.
- Prefer meaning chunks, idioms, collocations, and natural expressions over isolated vocabulary.
- Select only 3–5 high-value expressions. Favor depth over coverage.
- Reduce line-by-line Chinese translation. Translate only where it unlocks meaning or contrast.
- Proactively detect expressions whose literal words are understandable but whose intended meaning is easy to miss.
- Assign each core insight one primary section for full explanation. In other sections, reference it briefly or add only information specific to that section.
- Do not restate the same interpretation merely to complete every heading.
- Distinguish textual evidence from interpretation. Do not invent biography, motives, or cultural claims.
- Preserve ambiguity when the text does not support a single interpretation.
- Keep the experience sustainable: clear, thoughtful, and normally readable in 5–15 minutes.
- Use Chinese for explanation and retain the important English wording being studied.

## Workflow

### 1. Verify the source text

- Use the source file under `content/sources/` as authoritative. If the user supplies corrected text or an image, save it there first after confirming the target filename.
- Silently correct obvious OCR artifacts only when certain; flag any uncertainty that affects interpretation.
- If a malformed phrase changes the meaning, state the assumed reading briefly.

### 2. First Reading — understand the story

Read the entire piece before extracting language points. Establish:

- who is involved;
- what happens;
- the emotional or logical progression;
- the turning point or reveal;
- why the ending changes or completes the earlier details.

Open with a concise **Story Summary**. Do not front-load vocabulary.

### 3. Trace the narrative

Use a short paragraph breakdown only when it materially clarifies progression. Explain the role of each paragraph or movement, such as setup, contrast, escalation, reveal, reinterpretation, or closure.

State where the narrative turn occurs and what it changes. Reserve detailed language interpretation for its primary section.

### 4. Choose the Memorable Line

Select one sentence central to both language and meaning. Explain:

- why it carries the story;
- why the author phrased it this way;
- what would be weakened by a flatter alternative.

Do not choose a sentence merely because it sounds inspirational.

If the sentence also requires Beyond the Words analysis, identify that need briefly here and reserve the full interpretation for that section. Do not retell the entire theme around the line.

### 5. Analyze Key Expressions

Choose 3–5 expressions using this priority:

1. idioms and non-literal phrasing;
2. reusable meaning chunks;
3. natural collocations;
4. high-frequency vocabulary only when context changes its force.

For each item, give the contextual meaning, usage or tone, and one concise reusable example when helpful. Avoid dictionary-style synonym lists.

When an expression also belongs in Beyond the Words, keep its entry here concise and reserve the full contextual interpretation for that section.

### 6. Go Beyond the Words

Make this the signature section. Inspect seemingly simple phrases for:

- contextual meaning that differs from literal translation;
- implication, understatement, irony, humor, tenderness, grief, or social tone;
- referents or ellipsis the reader must infer;
- phrases whose emotional force depends on earlier story details;
- ordinary wording deliberately redefined by the ending.

Use the diagnostic and examples in [references/method.md](references/method.md).

Never restrict this section to formal idioms. A plain sentence can carry the deepest subtext.

Treat this as the primary section for full analysis of non-literal meaning. Avoid repeating an explanation already completed elsewhere unless adding a distinct contextual layer.

### 7. Explain Language Patterns and Writing Style

Identify only patterns worth reusing or noticing. Discuss sentence architecture when it creates rhythm, suspense, contrast, compression, viewpoint, or emotional force. Use **Sentence Workshop** for one or two sentences only when detailed parsing is genuinely useful.

Avoid turning the article into a comprehensive grammar lesson.

Explain what formal choice creates the effect. Do not use this section to restate the story's theme.

### 8. Reach Deep Understanding

Answer: **What is the author really trying to say?**

Connect the events to the author's viewpoint and theme. Ground the interpretation in specific textual choices. Explain the thinking pattern when relevant—for example, reframing, contrast between expectation and reality, meaning created retrospectively, or wisdom expressed through a small human story.

Synthesize earlier findings without repeating their language analysis. Add only the higher-level viewpoint or theme that emerges from them.

### 9. Close with active output

- Write a memorable English **One-sentence Takeaway** that captures the article without becoming a generic slogan.
- Offer one focused **30-second Reflection** prompt answerable in one or two sentences.
- Do not answer the reflection on the user's behalf unless asked.

### 10. Save and hand off the artifact

- Write the completed full-article companion to `content/readings/NNN-english-slug.md` using the source file's ID and slug.
- Include YAML frontmatter with `article_id`, `source_title`, `companion_title`, `skill`, `skill_version`, `generated_at`, `regression_report`, and `status`.
- Verify the file exists and report its local path in the final handoff.

## Default output

Use the following order, adapting section depth to the article:

1. **First Reading / Story Summary（先理解故事）**
2. **Story Flow / Paragraph Breakdown** — only when useful
3. **Memorable Line**
4. **Key Expressions（3–5）**
5. **Beyond the Words（字面之外）**
6. **Language Patterns（值得积累的表达）**
7. **Writing Style（作者写作技巧）**
8. **Deep Understanding / Theme（作者真正想说什么）**
9. **One-sentence Takeaway**
10. **30-second Reflection**
11. **Sentence Workshop** — optional; place near the sentence it supports if that reads better

Do not force empty or repetitive sections. Merge adjacent sections when they would repeat the same core insight or when the article does not contain enough independent material to justify separate treatment. Base this decision on information density and complexity, not word count alone. Always preserve Story, Language, Thinking, and Beyond the Words.

## Interaction rules

- If the user highlights a sentence or expression, answer that focus in depth while preserving its role in the whole story.
- If the user supplies a corrected image or text, restart from that authoritative version rather than defending the earlier reading.
- If the user asks to continue the numbered series, infer the established method and proceed without asking for the template again.
- If the user requests only one layer, provide that layer and do not force the full template.
- When comparing old and new analyses, evaluate missing meaning, misplaced emphasis, literalism, transfer value, and reader workload—not just section completeness.

## Quality gate

Before responding, verify:

- Can the reader retell the story and identify its turn?
- Are the selected expressions genuinely high-value and limited to 3–5?
- Did Beyond the Words reveal at least one meaning unavailable from literal translation alone?
- Is the interpretation supported by the text?
- Did the analysis explain how language creates the story's effect?
- Is the takeaway specific to this article?
- Is the reflection small enough to complete in 30 seconds?
- Did the response avoid unnecessary full translation and grammar overload?
- Does every section add information not already fully explained elsewhere?
- Has each core insight been assigned one primary section?
- Can any repeated paragraph be replaced with a brief reference without losing meaning?
