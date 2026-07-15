REQUIRED_SECTIONS = [
    "Topic",
    "Explanation",
    "Key Concepts",
    "Example",
    "Practice Exercise",
    "Common Mistakes",
    "Review Comments",
    "Final Summary",
]


def validate_required_sections(markdown: str) -> dict:
    missing = []

    for section in REQUIRED_SECTIONS:
        if section not in markdown:
            missing.append(section)

    return {
        "valid": len(missing) == 0,
        "missing_sections": missing,
    }