from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    instruction="Explique la programmation en français de manière simple et claire. Tu va recevoir un sujet et produire une courte explication, une liste de concepts clés, et un exemple de code. Ce sera produit en format Markdown et les headers markdown suivants : ## Simple Explanation, ## Key Concepts, ## Example, ajoute aussi une section '## Common Mistakes' (erreurs courantes sur ce sujet) "
    "et une section '## Final Summary' (résumé court en 2-3 phrases). ",
)