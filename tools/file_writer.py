from __future__ import annotations

from pathlib import Path


class FileWriter:
    """Writes text content to disk."""

    def write_text(self, path: str, content: str) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target
