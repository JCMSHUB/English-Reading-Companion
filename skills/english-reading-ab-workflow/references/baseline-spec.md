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
- mandatory One-sentence Takeaway plus 30-second Reflection;
- the companion quality gate;
- companion reference examples or terminology.

Natural overlap is allowed when the text makes a point obvious. For example, a general analysis may correctly explain an idiom or notice irony. Do not suppress valid insights merely to exaggerate the skilled result.

## Baseline quality checks

- Is the story summary correct?
- Are explanations useful rather than padded?
- Are claims grounded in the source?
- Would this be a plausible competent response before the specialized skill existed?
- Was it finalized before the skilled branch began?

