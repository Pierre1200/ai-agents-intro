from pathlib import Path

def save_markdown_file(file_path: str, content: str) -> str:
    path = Path(file_path)
    # Ensure the parent directory exists.
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return f"Error creating directory {path.parent}: {e}"
    # Write the Markdown content.
    try:
        path.write_text(content)
    except Exception as e:
        return f"Error writing to file {path}: {e}"
    # Return a useful message or the saved path.
    return f"Markdown file saved to {path}"