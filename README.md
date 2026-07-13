# AI Study Guide Generator

## Description
______ (une phrase : c'est quoi ce projet, en gros)

## Model Provider
- **Model**: qwen3:8b
- **Runtime**: Ollama (local)
- **Connector**: LiteLLM
- **Why this model**: contrainte matérielle : Mac M4, RAM unifiée 16 Go

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
Installed via Homebrew:
```bash
brew install ollama
```

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

### 8. Configure environment variables
Copy `.env.example` to `.env` and adjust if needed:
```bash
cp .env.example .env
```

## Usage
______ (à compléter plus tard, une fois main.py fonctionnel)

## Reflection
______ (à compléter en fin de projet — ex: pourquoi un modèle local plutôt qu'une API cloud pour ce projet ? quelles limites as-tu déjà rencontrées avec qwen3:8b ?)