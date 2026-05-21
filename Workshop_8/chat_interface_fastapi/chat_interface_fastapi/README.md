# CHAT Interface — FastAPI + Ollama

Cette application expose un modèle Ollama dans une interface web FastAPI.

## Prérequis

- Python 3.10+
- Ollama installé et lancé
- Un modèle téléchargé, par exemple :

```bash
ollama pull gemma3:1b
```

## Installation

```bash
cd chat_interface_fastapi
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Puis ouvrir :

```text
http://127.0.0.1:8000
```

## Variables d'environnement optionnelles

Changer le modèle :

```bash
set MODEL_NAME=gemma3:1b
```

Sur Linux/macOS :

```bash
export MODEL_NAME=gemma3:1b
```

Changer l'URL Ollama :

```bash
set OLLAMA_API_URL=http://localhost:11434
```

## Endpoint API

```http
POST /api/chat
Content-Type: application/json

{
  "message": "Explique FastAPI simplement."
}
```
