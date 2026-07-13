from __future__ import annotations


def validate_topic_item(item: dict) -> bool:
    required_keys = {"topic", "summary", "examples"}
    return required_keys.issubset(item.keys()) and isinstance(item["examples"], list)
