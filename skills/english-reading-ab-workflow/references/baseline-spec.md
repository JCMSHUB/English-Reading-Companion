# Historical Baseline Specification

Use this contract to reproduce a capable pre-skill English companion analysis. The purpose is a fair control, not a deliberately inferior answer.

## Allowed structure

Adapt naturally to the article. Typical sections are:

1. Article summary / 文章大意
2. Key vocabulary and expressions / 重点词汇与表达
3. One difficult sentence, when needed
4. Theme or main idea / 主题
5. A memorable sentence / 值得记住的句子

Do not force every section. Prefer a coherent general analysis over a fixed template.

## Expected behavior

- Explain the story accurately.
- Select useful vocabulary, phrases, or grammar points as a general English tutor would.
- Explain an obviously difficult sentence if it blocks comprehension.
- State the main theme or lesson.
- Use Chinese explanation while retaining important English wording.
- Keep the output useful and reasonably concise.

## Isolation boundary

The baseline must not deliberately apply or reproduce these companion-specific mechanisms:

- the four-layer Story / Language / Thinking / Beyond the Words reasoning sequence;
- mandatory proactive non-literal diagnostics;
- the companion's fixed 3–5 expression prioritization rule;
- mandatory narrative-turn tracing;
- a required `Simple English` line attached to selected expressions as a fixed bundle;
- a required `English Replay` close with a three-sentence model, target expressions, sentence starters, and a content route;
- any other mandatory companion-specific closing module, including the historical One-sentence Takeaway plus 30-second Reflection;
- the companion quality gate;
- companion reference examples or terminology.

Natural overlap is allowed when the text makes a point obvious. For example, a general analysis may correctly explain an idiom, use a naturally simple English paraphrase, notice irony, or ask a small reflection or retelling question. Treat that independent overlap as baseline evidence; do not suppress valid insights merely to exaggerate the skilled result. Leakage means reproducing the companion's recognizable bundled mechanism or consulting its instructions, not independently making one similar move.

## Baseline quality checks

- Is the story summary correct?
- Are explanations useful rather than padded?
- Are claims grounded in the source?
- Are any simple paraphrases or output prompts independently motivated rather than copied as a companion-specific bundle?
- Would this be a plausible competent response before the specialized skill existed?
- Was it finalized before the skilled branch began?
