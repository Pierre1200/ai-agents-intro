from __future__ import annotations


class ReviewerAgent:
    """Applies a minimal quality check on generated content."""

    def review(self, content: str) -> str:
        cleaned = content.strip()
        if not cleaned:
            raise ValueError("Generated content is empty.")
        return cleaned + "\n"
