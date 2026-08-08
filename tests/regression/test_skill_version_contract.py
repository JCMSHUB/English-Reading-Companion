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
            "save the completed analysis as `content/readings/NNN-english-slug.md`",
            skill_text,
        )
        self.assertIn("do not leave the result only in chat", skill_text)
        self.assertIn("`content/sources/`", skill_text)
        self.assertIn("Never overwrite an existing companion file", skill_text)
        self.assertIn("### 11. Save and hand off the artifact", skill_text)

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
        self.assertIn("Keep the whole entry to 2–4 short sentences", skill_text)

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

    def test_referenced_files_exist(self):
        expected = [
            SKILLS / "english-reading-companion" / "references" / "method.md",
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
