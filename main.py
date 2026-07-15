import asyncio
import sys

from google.adk.runners import InMemoryRunner
from google.genai import types

from agents.explainer_agent import explainer_agent

APP_NAME = "study_guide_generator"
USER_ID = "local_user"


async def run_explainer(topic: str) -> str:
    runner = InMemoryRunner(agent=explainer_agent, app_name=APP_NAME)

    session = await runner.session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=topic)],
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
    if len(sys.argv) < 2:
        print('Usage: python main.py "<topic>"')
        sys.exit(1)

    topic = sys.argv[1]

    result = asyncio.run(run_explainer(topic))
    print(result)


if __name__ == "__main__":
    main()