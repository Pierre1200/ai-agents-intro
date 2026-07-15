from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

practice_designer_agent = Agent(
    name="practice_designer_agent",
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    instruction="Conçois un exercice pratique en français pour le sujet donné. L'exercice doit être conçu pour aider l'apprenant à appliquer les concepts clés du sujet, donne input/output attendu et des indices. Ne reexplique pas le sujet. L'exercice doit etre réalisable en 20min. Le format de sortie doit être en Markdown avec l'en-têtes suivante : ## Practice Exercise",
)