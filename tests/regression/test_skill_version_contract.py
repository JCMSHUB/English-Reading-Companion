from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


class SkillVersionContractTest(unittest.TestCase):
    def assert_common_contract(self, skill_name: str) -> str:
        skill_dir = SKILLS / skill_name
        version = (skill_dir / "VERSION").read_text(encoding="utf-8").strip()
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        agent_text = (skill_dir / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )

        self.assertRegex(version, SEMVER)
        self.assertIn(f"**Current version:** {version}", skill_text)
        self.assertIn(f"v{version}", agent_text)
        return version

    def test_companion_version_is_visible_and_recorded(self):
        version = self.assert_common_contract("english-reading-companion")
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn(f"> Skill: english-reading-companion v{version}", skill_text)
        self.assertIn(f'skill_version: "{version}"', skill_text)
        self.assertIn("hidden metadata comment", skill_text)
        self.assertNotIn("YAML frontmatter", skill_text)

    def test_full_article_companion_requires_local_artifact(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "save the completed analysis as `content/readings/HONY-NNN-english-slug.md`",
            skill_text,
        )
        self.assertIn("do not leave the result only in chat", skill_text)
        self.assertIn("`content/sources/`", skill_text)
        self.assertIn("Never overwrite an existing companion file", skill_text)
        self.assertIn("### 11. Save and hand off the artifact", skill_text)

    def test_full_article_companion_saves_same_artifact_to_getnote(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("### 12. Save the same artifact to 得到大脑", skill_text)
        reference = SKILLS / "english-reading-companion" / "references" / "getnote-delivery.md"
        self.assertIn("(references/getnote-delivery.md)", skill_text)
        delivery_text = reference.read_text(encoding="utf-8")
        self.assertNotIn("getnote save --content-file", skill_text)
        self.assertIn("Upload the exact saved Markdown file", delivery_text)
        self.assertIn("whose name is exactly `英语伴读`", delivery_text)
        self.assertIn("following returned pagination", delivery_text)
        self.assertIn("Do not hard-code, remember, or guess the ID", delivery_text)
        self.assertIn("getnote save --content-file <reading-path>", delivery_text)
        self.assertIn("--topic-id <topic-id>", delivery_text)
        self.assertIn("saved file's SHA-256", delivery_text)
        self.assertIn("data.note.note_id", delivery_text)
        self.assertIn("data.note.note_url", delivery_text)
        self.assertIn("keep the local artifact", delivery_text)

    def test_full_article_companion_quotes_the_authoritative_source(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("### 3. Show the source for side-by-side reading", skill_text)
        self.assertIn("## Original Text / 对照原文", skill_text)
        self.assertIn("Markdown blockquotes", skill_text)
        self.assertIn("one `>`-prefixed paragraph per source paragraph", skill_text)
        self.assertIn("Preserve its title, byline, spelling, punctuation, and paragraph breaks", skill_text)
        self.assertIn("single full-text display", skill_text)

    def test_companion_uses_scan_friendly_readability_patterns(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Reading Route / 阅读路线", skill_text)
        self.assertIn("under 35 Chinese characters", skill_text)
        self.assertIn("Do not put it in `details`, tabs, or a table", skill_text)
        self.assertIn("Meaning in context（语境含义）", skill_text)
        self.assertIn("Why it matters（值得注意）", skill_text)
        self.assertIn("Try it（可迁移用法）", skill_text)
        self.assertIn("one Simple English line plus 2–4 short Chinese or usage sentences", skill_text)

    def test_companion_uses_bounded_simple_english_and_english_replay(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")
        method_text = (
            SKILLS / "english-reading-companion" / "references" / "method.md"
        ).read_text(encoding="utf-8")

        self.assertIn("clearly simpler, accurate English sentence", skill_text)
        self.assertIn("omit it when simplification would distort", skill_text)
        self.assertIn("Chinese remains primary for precise context and tone", skill_text)
        self.assertIn("## English Replay / 用英语再走一遍", skill_text)
        self.assertIn("### Read once（先读一遍）", skill_text)
        self.assertIn("### Your Turn（轮到你说）", skill_text)
        self.assertIn("retell the article in **2–3 sentences**", skill_text)
        self.assertIn("2–3 target expressions", skill_text)
        self.assertIn("2–3 short sentence starters", skill_text)
        self.assertIn("article-specific content route", skill_text)
        self.assertIn("It replaces separate Takeaway and Reflection sections", skill_text)
        self.assertIn("do not create a parallel English analysis", skill_text)
        self.assertIn("what remains unresolved", skill_text)
        self.assertIn("## Simple English and English Replay", method_text)
        self.assertIn("The Read once paragraph is a comprehension bridge", method_text)

    def test_companion_targets_elementary_learners_and_both_reading_modes(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("elementary foundation in English", skill_text)
        self.assertIn("Close reading / 精读", skill_text)
        self.assertIn("Extensive reading / 泛读", skill_text)
        self.assertIn("without translating every sentence", skill_text)

    def test_companion_keeps_necessary_cultural_or_historical_gateway_terms(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "cultural, historical, or role-identity gateway term", skill_text
        )
        self.assertIn("minimal stable context needed to unlock the text", skill_text)
        self.assertIn("unsupported background history", skill_text)

    def test_companion_controls_density_inference_and_transfer_examples(self):
        skill_text = (
            SKILLS / "english-reading-companion" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("default to three", skill_text)
        self.assertIn("merge them or omit the lower-value section", skill_text)
        self.assertIn("textual fact, the author's interpretation", skill_text)
        self.assertIn("replacement, destiny, causation, compensation, or resolution", skill_text)
        self.assertIn("natural, no harder than the source point", skill_text)

    def test_companion_has_conditional_calibration_rules(self):
        skill_text = (SKILLS / "english-reading-companion" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        method_text = (
            SKILLS / "english-reading-companion" / "references" / "method.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Conditional calibration rules", skill_text)
        self.assertIn("Concentrated short texts", skill_text)
        self.assertIn("Sensitive autobiographical texts", skill_text)
        self.assertIn("Role-identity gateways", skill_text)
        self.assertIn("Structural anchors", skill_text)
        self.assertIn("author's interpretation", skill_text)
        self.assertIn("two to four anchors", skill_text)
        self.assertIn("## Conditional calibration patterns", method_text)
        self.assertIn("Textual fact", method_text)
        self.assertIn("Reader association", method_text)

    def test_companion_metadata_is_hidden_from_readers(self):
        required_fields = [
            "article_id:",
            "source_title:",
            "companion_title:",
            "skill:",
            "skill_version:",
            "generated_at:",
            "regression_report:",
            "status:",
        ]

        for path in sorted((ROOT / "content" / "readings").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if "workflow_skill:" in text:
                continue
            self.assertTrue(text.startswith("<!--\n"), str(path))
            self.assertIn("-->\n\n# ", text)
            self.assertNotIn("\n---\n", text)
            for field in required_fields:
                self.assertIn(field, text, f"{path}: {field}")

    def test_ab_workflow_displays_both_versions(self):
        version = self.assert_common_contract("english-reading-ab-workflow")
        skill_text = (
            SKILLS / "english-reading-ab-workflow" / "SKILL.md"
        ).read_text(encoding="utf-8")

        expected = (
            f"> Skills: english-reading-ab-workflow v{version}; "
            "english-reading-companion v<installed-version>"
        )
        self.assertIn(expected, skill_text)
        self.assertIn("read only its `VERSION` file before starting the baseline", skill_text)

    def test_ab_workflow_has_cross_sample_synthesis_contract(self):
        workflow_dir = SKILLS / "english-reading-ab-workflow"
        skill_text = (workflow_dir / "SKILL.md").read_text(encoding="utf-8")
        synthesis_text = (
            workflow_dir / "references" / "cross-sample-synthesis.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Cross-sample synthesis", skill_text)
        self.assertIn("explicitly provides comparison paths, article IDs", skill_text)
        self.assertIn("Do not default to scanning all `content/readings/`", skill_text)
        self.assertIn("Reject duplicate article IDs", skill_text)
        self.assertIn("fewer than three included articles", skill_text)
        self.assertIn("no skill, version, or existing article was modified", skill_text)
        self.assertIn("## Status rules", synthesis_text)
        self.assertIn("Distinct IDs are necessary but insufficient", synthesis_text)
        self.assertIn("cannot edit a companion skill", synthesis_text)

    def test_ab_workflow_isolates_and_evaluates_companion_output_mechanisms(self):
        workflow_dir = SKILLS / "english-reading-ab-workflow"
        skill_text = (workflow_dir / "SKILL.md").read_text(encoding="utf-8")
        baseline_text = (
            workflow_dir / "references" / "baseline-spec.md"
        ).read_text(encoding="utf-8")
        rubric_text = (
            workflow_dir / "references" / "comparison-rubric.md"
        ).read_text(encoding="utf-8")

        self.assertIn("English-to-English meaning bridge", skill_text)
        self.assertIn("observed scaffold usability", skill_text)
        self.assertIn("bundled-mechanism leakage", skill_text)
        self.assertIn("a required `Simple English` line", baseline_text)
        self.assertIn("a required `English Replay` close", baseline_text)
        self.assertIn("independent overlap as baseline evidence", baseline_text)
        self.assertIn("English-to-English meaning bridge", rubric_text)
        self.assertIn("Active output / recall support", rubric_text)
        self.assertIn("### Companion-mechanism checks", rubric_text)
        self.assertIn("not a retrospective failure", rubric_text)
        self.assertIn("not an automatic isolation failure", rubric_text)
        self.assertIn("do not claim improved retelling accuracy", rubric_text)

    def test_referenced_files_exist(self):
        expected = [
            SKILLS / "english-reading-companion" / "references" / "method.md",
            SKILLS / "english-reading-companion" / "references" / "getnote-delivery.md",
            SKILLS
            / "english-reading-ab-workflow"
            / "references"
            / "baseline-spec.md",
            SKILLS
            / "english-reading-ab-workflow"
            / "references"
            / "comparison-rubric.md",
        ]

        for path in expected:
            self.assertTrue(path.is_file(), str(path))


if __name__ == "__main__":
    unittest.main()
