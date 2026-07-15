import asyncio
import sys
import re

from google.adk.runners import InMemoryRunner
from google.genai import types
from agents.practice_designer_agent import practice_designer_agent
from agents.explainer_agent import explainer_agent
from tools.file_writer import save_markdown_file
from agents.reviewer_agent import reviewer_agent
from tools.validation import validate_required_sections

APP_NAME = "study_guide_generator"
USER_ID = "local_user"


def slugify(topic: str) -> str:
    slug = topic.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


async def run_agent(agent, message_text):
    runner = InMemoryRunner(agent=agent, app_name=APP_NAME)

    session = await runner.session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=message_text)],
    )

    final_text = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session.id,
        new_message=user_message,
    ):
        if not event.content or not event.content.parts:
            continue
        for part in event.content.parts:
            is_thought = getattr(part, "thought", None)
            if not is_thought and part.text:
                final_text = part.text

    return final_text


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print('Usage: python main.py "<topic>"')
        sys.exit(1)

    topic = sys.argv[1]

    try:
        print(f"[1/4] Running Explainer Agent for: {topic}")
        explanation = asyncio.run(run_agent(explainer_agent, topic))
    except Exception as e:
        print(f"❌ Could not reach the local model. Is 'ollama serve' running? Details: {e}")
        sys.exit(1)

    print("[2/4] Running Practice Designer Agent")
    practice_input = f"Topic: {topic}\n\nExplanation:\n{explanation}"
    practice_exercise = asyncio.run(run_agent(practice_designer_agent, practice_input))

    draft = f"# Topic: {topic}\n\n{explanation}\n\n{practice_exercise}"

    print("[3/4] Running Reviewer Agent")
    review_comments = asyncio.run(run_agent(reviewer_agent, draft))

    final_markdown = f"{draft}\n\n## Review Comments\n{review_comments}"

    print("[4/4] Validating and saving")
    validation = validate_required_sections(final_markdown)
    if not validation["valid"]:
        print(f"⚠️ Missing sections: {validation['missing_sections']}")

    save_markdown_file(f"output/{slugify(topic)}_full_guide.md", final_markdown)


if __name__ == "__main__":
    main()