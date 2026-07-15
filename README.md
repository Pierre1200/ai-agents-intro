# AI Agents in Python

## Description
A local, multi-agent AI system that generates complete Markdown study guides for any programming topic — explanation, key concepts, example, practice exercise, common mistakes, review comments, and summary — using Google ADK, LiteLLM, and a locally-hosted Qwen3 model via Ollama. Everything runs offline, for free, on consumer hardware.

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com) (local model runtime)
- ~5GB free disk space for the `qwen3:8b` model
- macOS, Linux, or Windows

## Setup

### 1. Clone and enter the repo
```bash
git clone <your-repo-url>
cd ai-agents-intro
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama
Installed via Homebrew on macOS:
```bash
brew install ollama
```
(See [ollama.com/download](https://ollama.com/download) for other platforms.)

### 5. Start the Ollama server
```bash
ollama serve
```
⚠️ Keep this running in a dedicated terminal — it's a server process, not a one-off command. Run the next steps in a separate terminal tab/window.

### 6. Pull the model
```bash
ollama pull qwen3:8b
```

### 7. Test the model directly (before running the project)
```bash
ollama run qwen3:8b
```
Type a prompt, confirm it answers, then exit with `/bye`.

## Configuration

Copy `.env.example` to `.env` and adjust if needed:
```bash
cp .env.example .env
```

Relevant variables (see `.env.example`):
```
OLLAMA_API_BASE=http://localhost:11434
MODEL_NAME=ollama_chat/qwen3:8b
```

**Model provider**: this project uses **Qwen3 8B**, served locally through **Ollama**, connected via **LiteLLM** (`ollama_chat/qwen3:8b`) as the connector between Google ADK and the model runtime. No API key is required for this default configuration. Qwen3 was chosen over alternatives like Nous Hermes because it ships directly in Ollama's official library with native tool-calling support, and fits within the unified memory constraints of a 16GB Apple Silicon machine (Mac M4). To use a different provider (Gemini, OpenAI, Claude, etc.), swap `MODEL_NAME` and add the relevant API key to `.env` — no agent code changes are required, since LiteLLM abstracts the provider.

## How to Run

```bash
python main.py "Python decorators"
```

The pipeline runs in 4 steps, printing progress for each:
```
[1/4] Running Explainer Agent for: Python decorators
[2/4] Running Practice Designer Agent
[3/4] Running Reviewer Agent
[4/4] Validating and saving
```

The final guide is saved to `output/<topic-slug>_full_guide.md`.

## Example Input
```bash
python main.py "Python decorators"
```

## Example Output
Excerpt from `output/python-decorators_full_guide.md`:
```markdown
# Topic: Python decorators

## Simple Explanation  
Les décorateurs en Python sont des outils qui permettent d'ajouter ou modifier
le comportement d'une fonction sans la changer directement...

## Key Concepts  
1. **@decorator** : Syntaxe pour appliquer un décorateur à une fonction.
...

## Practice Exercise
### Task
Créez un décorateur qui enregistre le nom de la fonction et ses arguments
avant son exécution...

## Review Comments
**Recommandation** : approuvé.
```

## Project Structure
```
ai-agents-intro/
├── agents/
│   ├── explainer_agent.py          # Explains the topic + key concepts + example + common mistakes + summary
│   ├── practice_designer_agent.py  # Designs a practice exercise from the explanation
│   └── reviewer_agent.py           # Reviews the draft guide and gives feedback
├── tools/
│   ├── file_writer.py              # Deterministic: saves Markdown to disk
│   └── validation.py               # Deterministic: checks required sections are present
├── output/                         # Generated study guides land here
├── data/
│   └── topic_examples.json         # Sample topics for quick testing
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── main.py                         # Orchestrates the full sequential pipeline
```

## Agents

| Agent | File | Responsibility |
|---|---|---|
| **Explainer Agent** | `agents/explainer_agent.py` | Receives a topic and produces the Simple Explanation, Key Concepts, Example, Common Mistakes, and Final Summary sections. It is the only agent with general knowledge of the topic. |
| **Practice Designer Agent** | `agents/practice_designer_agent.py` | Receives the topic + the explanation already produced, and designs a short (10-20 min) practice exercise with expected input/output and hints. Explicitly instructed not to re-explain the topic or give away the full solution. |
| **Reviewer Agent** | `agents/reviewer_agent.py` | Receives the full draft (explanation + exercise) and produces specific, actionable review comments plus an approve/revise recommendation. Does not regenerate content — critique only. |

## Tools

| Tool | File | Responsibility |
|---|---|---|
| **`save_markdown_file()`** | `tools/file_writer.py` | Deterministic. Writes Markdown content to a given path, creating parent directories as needed, with error handling for filesystem failures. |
| **`validate_required_sections()`** | `tools/validation.py` | Deterministic. Checks that all 8 required Markdown headers are present in the final guide and reports which ones are missing, if any. |

## Self-Validation Checklist

- [x] Project structure matches the required layout (Task 0)
- [x] Local model environment set up and documented (Task 1)
- [x] Explainer Agent created, tested with 2+ topics (Task 2)
- [x] `save_markdown_file()` tool created and tested independently (Task 3)
- [x] `validate_required_sections()` tool created and tested independently (Task 4)
- [x] Practice Designer Agent created, uses previous agent's output (Task 5)
- [x] Reviewer Agent created, reviews without rewriting (Task 6)
- [x] Full sequential workflow built in `main.py` (Task 7)
- [x] Basic error handling: empty topic, unreachable model, file errors, validation failures (Task 8)
- [x] README completed with all required sections (Task 9)

## Reflection

**1. What is the difference between a direct LLM call and an AI agent?**
A direct LLM call sends a prompt and returns text — a single, stateless, non-deterministic transformation. An AI agent wraps a model with a defined role, explicit instructions, and (optionally) tools and orchestration logic, so it behaves as a component in a larger, structured system rather than a one-off text generator.

**2. What role does each agent have in your system?**
The Explainer Agent generates the core educational content (explanation, key concepts, example, common mistakes, summary). The Practice Designer Agent builds a small exercise from that explanation without repeating it. The Reviewer Agent critiques the assembled draft and gives actionable feedback, without producing new content itself.

**3. What role does each tool have in your system?**
`save_markdown_file()` handles all file I/O deterministically — same input always produces the same file on disk, with clear errors on failure. `validate_required_sections()` deterministically checks that the LLM-generated content respects the required structure, catching cases where an agent's output drifts from the expected format.

**4. What was the most difficult part of the project?**
Debugging a loop bug in `main.py`: the ADK `Runner` streams multiple `events` per agent turn, and Qwen3 (a reasoning model) emits its internal "thinking" as a separate event before the actual answer. The initial loop captured whichever text arrived last without distinguishing reasoning from the final response, silently returning the model's internal monologue instead of the structured Markdown output. Fixing it required inspecting each event's `thought` attribute directly rather than trusting a naive "last event wins" assumption.

**5. What limitation did you observe when using your selected model?**
Qwen3 8B "thinks out loud" before answering (visible via `thought=True` events), which adds latency and required explicit filtering logic to separate reasoning from the actual deliverable — a behavior that isn't obvious from the model's name alone and would trip up anyone assuming a plain one-shot text response.

## Known Limitations
- Runs best with `qwen3:8b`; larger models (14B+) are constrained by the 16GB unified memory on Apple Silicon and were not extensively tested.
- No persistent memory between runs — each topic is generated independently, no history of past guides is used as context.
- The Reviewer Agent's feedback is not automatically applied — it's included in the output for a human to act on, not looped back into the agents.
- Validation checks section *presence*, not content quality or factual accuracy.
- Tested primarily on programming topics in French/English; behavior on other languages or non-programming topics is untested.