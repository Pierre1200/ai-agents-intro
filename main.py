from __future__ import annotations

import json
from pathlib import Path

from agents.explainer_agent import ExplainerAgent
from agents.practice_designer_agent import PracticeDesignerAgent
from agents.reviewer_agent import ReviewerAgent
from tools.file_writer import FileWriter
from tools.validation import validate_topic_item


def build_study_guide(data_path: str = "data/topic_examples.json") -> str:
    records = json.loads(Path(data_path).read_text(encoding="utf-8"))

    explainer = ExplainerAgent()
    practice = PracticeDesignerAgent()
    reviewer = ReviewerAgent()

    sections: list[str] = ["# Study Guide\n"]
    for item in records:
        if not validate_topic_item(item):
            continue
        sections.append(explainer.explain(item["topic"], item["summary"]))
        sections.append("\n### Practice\n")
        sections.append(practice.design(item["topic"], item["examples"]))
        sections.append("\n")

    return reviewer.review("\n".join(sections))


def main() -> None:
    content = build_study_guide()
    writer = FileWriter()
    writer.write_text("output/study_guide.md", content)
    print("Study guide generated: output/study_guide.md")


if __name__ == "__main__":
    main()
