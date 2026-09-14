---
name: english-reading-companion
description: "Use the established English Reading Companion method for elementary learners when the user requests 英语伴读, asks for close or extensive reading with this method, continues its numbered series, or revises an existing companion. Ordinary translation, isolated language questions, and skill-file audits do not trigger this skill by themselves."
---

# English Reading Companion

**Current version:** 2.8.4
**Release:** 2026-09-14 · Instruction-only update; validation recorded in the project CHANGELOG.md entry for 2.8.4.

Apply the user's stable reading method. Build English intuition rather than produce a translation or grammar lecture.

## Delivery scope

- Use **project-series mode** only when generating a full numbered companion for the `English-Reading-Companion` project. Resolve this from the requested target project and its applicable `AGENTS.md`, not merely from a folder name or an English article. In this mode, use the project's source, naming, local-save, and private-archive contract below; the project's recorded authorization governs external delivery.
- For general companion requests outside that project, use the user's supplied text, image, or requested source directly and deliver in chat or the requested format. Do not require `content/sources/`, a HONY ID, local saving, or private archiving. Focused answers and A/B evaluation artifacts are not project-series deliverables.

- The full output structure, four-layer coverage, expression count, and full quality gate apply only to a full companion, including an A/B skilled branch. For a focused follow-up within this method, apply only the relevant explanation and checks; do not add a full template or Replay. An A/B baseline follows its independent baseline contract and does not apply this skill.

## Version visibility

- Read `VERSION` before producing any analysis and require it to match the version declared above.
- Begin every user-visible analysis with this exact line immediately after the title:

  `> Skill: english-reading-companion v2.8.4`

- In project-series mode, save the completed analysis as `content/readings/HONY-NNN-english-slug.md`; do not leave the result only in chat. Then follow the conditional external-delivery step 12 before the final handoff. Existing pure-numeric files retain their historical names.
- For a project-series companion, resolve the source from the user's request and existing project files. Save newly supplied source text under `content/sources/` before generating the companion. Reuse an existing article ID and filename; for a new article, determine the next unused HONY ID from the established sequence and derive a lowercase English slug from the title or content. New HONY IDs begin at `HONY-001`; preserve existing names and follow any newer user naming rule. If no source title is supplied, label it untitled rather than inventing an original title. Ask only when source identity, numbering conflicts, or the overwrite target cannot be resolved reliably; missing filename components alone do not require confirmation.
- Save new project-series analyses with `status: "draft"` without an extra approval step. Never overwrite an existing companion file unless the user's existing explicit authorization covers that target; otherwise save a separate draft or ask if the overwrite is necessary.
- Store `skill: "english-reading-companion"` and `skill_version: "2.8.4"` in the saved file's hidden metadata comment.
- Include the same skill name and version in the concise chat handoff that links or summarizes a saved artifact.
- Stop and report a version mismatch instead of guessing which version is active.

## Core objective and learner scope

Serve learners with an elementary foundation in English. Use the original text as the center of the learning experience, so the learner gradually reads more independently rather than relying on a full translation or a grammar lecture.

Build both reading modes through the same companion:

- **Close reading / 精读** — notice how selected sentences, expressions, structure, and context create meaning.
- **Extensive reading / 泛读** — follow the main idea, story movement, and key details without translating every sentence.

Help the reader understand English as English across four connected layers:

1. **Story** — what happens, how the narrative moves, and where it turns.
2. **Language** — how meaning is packaged in chunks, collocations, idioms, syntax, and natural phrasing.
3. **Thinking** — what viewpoint, value, assumption, or way of seeing the world shapes the writing.
4. **Beyond the Words** — what the words mean in context beyond their literal surface.

Treat the four layers as a reasoning sequence, not four independent labels.

## Operating principles

- Understand the whole story before analyzing individual sentences.
- Calibrate explanations for an elementary learner: establish the main meaning first, use plain Chinese, and introduce terminology only when it helps the learner read the source independently.
- Make each analysis point serve one of two outcomes: deeper understanding of this text or a reusable reading habit for the next text.
- Explain meaning in context before discussing grammar.
- Prefer meaning chunks, idioms, collocations, and natural expressions over isolated vocabulary.
- For a full companion, select only 3–5 high-value expressions. Favor depth over coverage.
- When a cultural, historical, or role-identity term is necessary to understand the article's situation or stakes, include one such gateway term among the 3–5. Give only the minimal stable context needed to unlock the text; do not force one into articles that do not need it, and do not turn it into unsupported background history.
- Reduce line-by-line Chinese translation. Translate only where it unlocks meaning or contrast.
- Use Chinese to secure accurate contextual understanding. Add short Simple English only as a bridge from the source expression to English meaning, not as a parallel translation of the full analysis.
- Proactively detect expressions whose literal words are understandable but whose intended meaning is easy to miss.
- Assign each core insight one primary section for full explanation. In other sections, reference it briefly or add only information specific to that section.
- Do not restate the same interpretation merely to complete every heading.
- Distinguish textual evidence from interpretation. Do not invent biography, motives, or cultural claims.
- Preserve ambiguity when the text does not support a single interpretation.
- In historical, medical, death, trauma, or fate-like material, label the boundary between textual fact, the author's interpretation, and a reader's possible association when that boundary is needed to prevent overreach. Do not turn an interpretation or association into a diagnosis, a universal lesson, a factual background claim, or a claim of replacement, destiny, causation, compensation, or resolution unless the text supports it.
- Keep the experience sustainable: clear, thoughtful, and normally readable in 5–15 minutes.
- Use Chinese for explanation and retain the important English wording being studied.
- Use short labels and short paragraphs to make scanning easy; do not use tables for the main analysis, because they read poorly on narrow screens.

## Conditional calibration rules

Apply these rules only when their trigger condition materially changes understanding. They refine the four-layer method; they do not add mandatory sections.

1. **Concentrated short texts** — When a short text's key value is concentrated in a final reversal, irony, one non-literal phrase, or a repeated sentence pattern, use a core path: retain the story, decisive contextual explanation, needed language, theme, and active output; merge or omit any Story Flow or Writing Style section that would repeat the same evidence. Do not compress away the explanation that makes the reversal readable.
2. **Sensitive autobiographical texts** — When trauma, death, illness, body experience, strong symbolism, or fate-like framing invites overreach, distinguish textual fact from the author's interpretation and from a possible reader association in one or two natural sentences. Do not add a warning formula to low-risk texts or use the boundary to avoid explaining the text's actual emotional meaning.
3. **Role-identity gateways** — When a profession, family role, community, or institutional identity unlocks later actions, objects, relationships, or expectations, treat it as a high-priority gateway term. Give only the minimal stable context the text requires; do not turn every role word into background instruction.
4. **Structural anchors** — When repeated time markers, milestones, direct address, short-sentence runs, dashes, ellipses, or modal changes carry the narrative or emotional turn, identify two to four anchors before detailed language analysis. Do not force an anchor map onto a straightforward linear text or replace story comprehension with sentence-by-sentence parsing.

## Workflow

Source verification applies to the requested analysis. Steps 2–10 describe a full companion; focused follow-ups use only the relevant parts. Steps 11–12 apply only to project-series delivery.

### 1. Verify the source text

- In project-series mode, use the source file under `content/sources/` as authoritative. If the user supplies corrected text or an image, resolve the target from the current request and naming rules, then save the authorized correction there first. Ask only if the source identity or overwrite target remains unclear or the required overwrite is not authorized. Outside this mode, use the user's latest supplied or requested source without requiring a project file.
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

Immediately after it, add one quoted **Reading Route / 阅读路线** sentence that tells the reader what to read next: the source text, then the story or language focus, and finally the deeper meaning. Keep it specific to the article and under 35 Chinese characters where possible.

### 3. Show the source for side-by-side reading

- After **First Reading / Story Summary** and before any detailed analysis, add `## Original Text / 对照原文`.
- Reproduce the authoritative English source in Markdown blockquotes, one `>`-prefixed paragraph per source paragraph. Preserve its title, byline, spelling, punctuation, and paragraph breaks; do not translate, summarize, correct uncertain text, or insert analysis inside this section.
- Use a blockquote heading for the source title when it is not already clear from the companion title. Keep author or source credit as a separate quoted line when present.
- Treat this section as the single full-text display. Quote shorter excerpts elsewhere only when necessary for the analysis, so that duplication does not overwhelm the reading experience.
- Keep the original text directly visible. Do not put it in `details`, tabs, or a table unless the user explicitly asks, because those formats are less reliable across Markdown readers and make comparison less immediate.

### 4. Trace the narrative

Use a short paragraph breakdown only when it materially clarifies progression. Explain the role of each paragraph or movement, such as setup, contrast, escalation, reveal, reinterpretation, or closure.

State where the narrative turn occurs and what it changes. Reserve detailed language interpretation for its primary section.

### 5. Choose the Memorable Line

Select one sentence central to both language and meaning. Explain:

- why it carries the story;
- why the author phrased it this way;
- what would be weakened by a flatter alternative.

Do not choose a sentence merely because it sounds inspirational.

If the sentence also requires Beyond the Words analysis, identify that need briefly here and reserve the full interpretation for that section. Do not retell the entire theme around the line.

### 6. Analyze Key Expressions

Choose 3–5 expressions using this priority. For a single-paragraph, joke-like, or emotionally concentrated text, default to three; add a fourth or fifth only when it unlocks distinct understanding or transfer value:

1. a cultural, historical, or role-identity gateway term when it materially unlocks the article;
2. idioms and non-literal phrasing;
3. reusable meaning chunks;
4. natural collocations;
5. high-frequency vocabulary only when context changes its force.

For each item, use this compact scan-friendly sequence: **Simple English**, **Meaning in context（语境含义）**, **Why it matters（值得注意）**, and **Try it（可迁移用法）**. Add **Simple English** only when one clearly simpler, accurate English sentence can preserve the expression's core meaning and any important limit; omit it when simplification would distort tone, uncertainty, duration, or implication. Chinese remains primary for precise context and tone. Add **Try it** only when its example is natural, no harder than the source point, and useful to an elementary learner; otherwise omit it and keep the item as a comprehension point. Keep the explanatory entry compact: one Simple English line plus 2–4 short Chinese or usage sentences. Avoid dictionary-style synonym lists.

When an expression also belongs in Beyond the Words, keep its entry here concise and reserve the full contextual interpretation for that section. A role-identity gateway belongs among the 3–5 expressions only when it unlocks the article's situation or stakes.

### 7. Go Beyond the Words

Make this the signature section. Inspect seemingly simple phrases for:

- contextual meaning that differs from literal translation;
- implication, understatement, irony, humor, tenderness, grief, or social tone;
- referents or ellipsis the reader must infer;
- phrases whose emotional force depends on earlier story details;
- ordinary wording deliberately redefined by the ending.

Consult the relevant sections of [references/method.md](references/method.md) when contextual meaning is difficult to determine, explanations overlap across sections, or interpretation depth needs calibration. Do not reread it when the available context is sufficient.

Never restrict this section to formal idioms. A plain sentence can carry the deepest subtext.

Treat this as the primary section for full analysis of non-literal meaning. Avoid repeating an explanation already completed elsewhere unless adding a distinct contextual layer.

### 8. Explain Language Patterns and Writing Style

Identify only patterns worth reusing or noticing. Discuss sentence architecture when it creates rhythm, suspense, contrast, compression, viewpoint, or emotional force. For structurally fragmented text, identify the selected anchors and their combined movement before parsing any one sentence. Use **Sentence Workshop** for one or two sentences only when detailed parsing is genuinely useful. When Story Flow and Writing Style would rely on the same evidence without adding a distinct learning layer, merge them or omit the lower-value section.

Avoid turning the article into a comprehensive grammar lesson.

Explain what formal choice creates the effect. Do not use this section to restate the story's theme.

### 9. Reach Deep Understanding

Answer: **What is the author really trying to say?**

Connect the events to the author's viewpoint and theme. Ground the interpretation in specific textual choices. Explain the thinking pattern when relevant—for example, reframing, contrast between expectation and reality, meaning created retrospectively, or wisdom expressed through a small human story.

Synthesize earlier findings without repeating their language analysis. Add only the higher-level viewpoint or theme that emerges from them.

### 10. Close with English Replay

Use `## English Replay / 用英语再走一遍` as the default active-output close for a full companion. It replaces separate Takeaway and Reflection sections rather than stacking after them.

- Under `### Read once（先读一遍）`, write three short Simple English sentences that retrace the story, its turn, and its core meaning. Keep them easier than the source and grounded in the text; do not create a parallel English analysis.
- Under `### Your Turn（轮到你说）`, ask the learner to read the three sentences once, look away, and retell the article in **2–3 sentences**.
- Offer 2–3 target expressions from the companion, 2–3 short sentence starters, and one article-specific content route that says which story movements to cover. These are optional supports, not a model answer the learner must copy.
- Keep the task small. A specific takeaway may be folded into the final Read once sentence, and a reflection may be folded into the content route, but do not add separate default sections for them.
- For sensitive material, preserve the distinction between what happened, how the author understood it, and what remains unresolved. Do not let the simplified retelling turn a temporary emotional shift into a diagnosis, cure, causal claim, or complete resolution.

### 11. Save and hand off the artifact

The file and metadata requirements in this step apply to project-series mode. For general companion requests, hand off in the requested format; do not impose the project directory or HONY naming scheme.

- Write the completed new HONY companion to `content/readings/HONY-NNN-english-slug.md` using the source file's `HONY-NNN` ID and slug. Do not rename existing pure-numeric artifacts.
- Begin the file with an HTML comment containing `article_id`, `source_title`, `companion_title`, `skill`, `skill_version`, `generated_at`, `regression_report`, and `status`. This preserves local validation metadata without presenting engineering fields to the reader.
- Verify the file exists and passes the direct artifact checks before any external save.

### 12. Save the same artifact to 得到大脑

Only when this is a full project-series companion under `content/readings/`, the local file has passed direct artifact checks, and the applicable project authorization covers this private save, read [references/getnote-delivery.md](references/getnote-delivery.md) and complete delivery before the final handoff. Do not read this reference for general companion requests, focused one-layer answers, or A/B evaluation artifacts. Report the actual local-save and 得到大脑 delivery results separately.

## Default output

Use the following order, adapting section depth to the article:

1. **First Reading / Story Summary（先理解故事）**
2. **Reading Route / 阅读路线** — one short quoted sentence
3. **Original Text / 对照原文** — quote the complete source text, preserving paragraph breaks
4. **Story Flow / Paragraph Breakdown** — only when useful
5. **Memorable Line**
6. **Key Expressions（3–5）**
7. **Beyond the Words（字面之外）**
8. **Language Patterns（值得积累的表达）**
9. **Writing Style（作者写作技巧）**
10. **Deep Understanding / Theme（作者真正想说什么）**
11. **English Replay / 用英语再走一遍** — three-sentence `Read once` plus a supported 2–3-sentence `Your Turn`
12. **Sentence Workshop** — optional; place near the sentence it supports if that reads better

Do not force empty or repetitive sections. Merge adjacent sections when they would repeat the same core insight or when the article does not contain enough independent material to justify separate treatment. Base this decision on information density and complexity, not word count alone. For a full companion, preserve Story, Language, Thinking, and Beyond the Words as reading dimensions; do not invent an insight to fill a section. Focused answers need only their relevant dimensions.

## Interaction rules

- If the user highlights a sentence or expression, answer that focus in depth while preserving its role in the whole story.
- If the user supplies a corrected image or text, restart from that authoritative version rather than defending the earlier reading.
- If the user asks to continue the numbered series, infer the established method and proceed without asking for the template again.
- If the user requests only one layer, provide that layer and do not force the full template.
- When comparing old and new analyses, evaluate missing meaning, misplaced emphasis, literalism, transfer value, and reader workload—not just section completeness.

## Quality gate

Before delivering a full companion, verify the applicable items below. For a focused answer, check only source accuracy, the requested explanation, and any relevant interpretation or language constraints; do not require the full expression count, Reading Route, four-layer output, or English Replay.

- Can the reader retell the story and identify its turn?
- Are the selected expressions genuinely high-value and limited to 3–5, with three as the default for a very short or concentrated text?
- When the article depends on a cultural, historical, or role-identity gateway term, did the selection include one with only the minimal context needed?
- Did the analysis check for contextual meaning that literal reading could miss, explain it when supported, and avoid forcing a hidden meaning when the text provides none?
- Is the interpretation supported by the text?
- For sensitive or fate-like material, did the analysis keep textual fact, implication, and reader association distinct?
- Did the analysis explain how language creates the story's effect?
- Is each Simple English line clearly easier than the source expression, accurate in context, and omitted when it would erase an important limit or tone?
- Does English Replay use three short, text-grounded sentences and ask for only a 2–3-sentence retelling?
- Are its target expressions, sentence starters, and content route specific and light enough to support recall without becoming a second lesson or a model answer?
- For sensitive material, does the Replay preserve what remains unresolved rather than converting a moment of change into complete resolution?
- Did the response avoid unnecessary full translation and grammar overload?
- Is each core insight fully explained only once, with other sections adding unique information or a necessary brief reference, and repetition that adds no information removed?
- Does the Reading Route give a useful next step without repeating the summary?
- Does every Key Expressions entry use the compact Simple English, Meaning, and Why it matters sequence when accurate simplification is possible, and use Try it only when the example is natural and level-appropriate?
