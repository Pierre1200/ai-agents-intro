from __future__ import annotations


class ExplainerAgent:
    """Generates a short explanation for a learning topic."""

    def explain(self, topic: str, summary: str) -> str:
        return f"## {topic}\n\n{summary.strip()}"
