# Project-series contract

Read this reference before generating or revising a full numbered companion for the English-Reading-Companion project. It does not apply to general companion requests, focused answers, or A/B evaluation artifacts. Authorization comes from the user's request and the applicable project AGENTS.md; this reference grants none. Reuse this reference at save time without rereading unchanged material.

## Before generation or revision

- Resolve the authoritative source from the user's request and existing project files. Read the complete target source. Save newly supplied source text under `content/sources/` before generating the companion; preserve its wording and uncertain text.
- Reuse an existing article ID and filename. For a new article, determine the next unused HONY ID from the established sequence and derive a lowercase English slug from the title or content. New HONY IDs begin at `HONY-001`; preserve existing names and follow any newer user naming rule. If no source title is supplied, label it untitled rather than inventing an original title.
- Resolve the target path and whether it already exists before writing. Check numbering and target existence by filename only; do not read neighboring articles to infer conventions.
- Never overwrite an existing companion file unless the user's existing explicit authorization covers that target; otherwise save a separate draft or ask if the overwrite is necessary. Ask only when source identity, numbering conflicts, or the overwrite target cannot be resolved reliably; missing filename components alone do not require confirmation.

## Before saving and handing off

- In project-series mode, save the completed analysis as `content/readings/HONY-NNN-english-slug.md` using the source file's HONY ID and slug; do not leave the result only in chat. Existing pure-numeric files retain their historical names.
- Save new project-series analyses with `status: "draft"` without an extra approval step. Follow the applicable project status rules for revisions; do not promote a draft to final without the required explicit authorization.
- Begin the file with a hidden metadata comment (HTML) containing `article_id`, `source_title`, `companion_title`, `skill`, `skill_version`, `generated_at`, `regression_report`, and `status`. Store `skill: "english-reading-companion"` and `skill_version: "2.8.6"`; metadata must reflect the actual skill version and actual validation, without inventing a regression report.
- Verify the file exists, its naming and Markdown structure are valid, required metadata and version agree, and the Original Text reproduces the authoritative source's wording, punctuation, and paragraph breaks. Apply the entrypoint's full content quality gate. Reuse checks already passed for unchanged content.
- Only after direct artifact checks pass and applicable project authorization covers the private save, follow the entrypoint's conditional 得到大脑 delivery step. Revision of a local companion does not authorize updating, overwriting, or creating a replacement for an existing external note.
- Include the skill name and version in the concise handoff, link the verified local artifact, and report local-save and external-delivery results separately. If external delivery is pending or unsuccessful, do not describe overall delivery as complete.
