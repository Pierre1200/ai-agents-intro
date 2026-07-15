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

## Example Output

Command:
````bash
python main.py "Python decorators"
````

Output:
````markdown
## Explanation  
En Python, un **décorateur** est une fonction qui permet d'ajouter des fonctionnalités à une autre fonction sans la modifier directement. Il s'agit d'une forme de "sucre syntaxique" qui permet d'envelopper une fonction existante avec du code supplémentaire (comme le logging, la validation, ou la gestion des erreurs). Un décorateur est défini avec la syntaxe `@decorator` juste avant la définition de la fonction qu'il modifie.

## Key Concepts  
- **Fonction première classe** : Les fonctions peuvent être passées en paramètres, retournées ou assignées à des variables.  
- **Décorateur** : Une fonction qui prend une autre fonction en entrée et retourne une nouvelle fonction modifiée.  
- **`*args` et `**kwargs`** : Permettent de gérer un nombre variable d'arguments lors de l'appel des fonctions.  
- **Syntaxe `@decorator`** : Simplifie l'application d'un décorateur à une fonction.  

## Example  
```python
def log_message(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_message
def saluer(nom):
    print(f"Bonjour, {nom}!")

saluer("Alice")
```

**Sortie :**  
````
Appel de saluer avec arguments: ('Alice',), {}
Bonjour, Alice!
````
````