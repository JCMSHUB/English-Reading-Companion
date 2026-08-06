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
        self.assertIn("### 10. Save and hand off the artifact", skill_text)

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
