from __future__ import annotations

from typing import Iterable


class PracticeDesignerAgent:
    """Builds simple practice prompts for a topic."""

    def design(self, topic: str, examples: Iterable[str]) -> str:
        lines = [f"- Practice: explain '{topic}' in your own words."]
        for example in examples:
            lines.append(f"- Example to revisit: {example}")
        return "\n".join(lines)
