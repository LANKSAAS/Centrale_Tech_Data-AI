from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CHAT Interface")

BASE_DIR = os.path.dirname(__file__)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:1b")

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "Tu es un assistant pédagogique. Réponds clairement, simplement et étape par étape."
)


def call_ollama(message: str) -> str:
    """Appelle Ollama via l'endpoint /api/chat."""
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
        "stream": False,
    }

    response = requests.post(
        f"{OLLAMA_API_URL}/api/chat",
        json=payload,
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "resultat": None,
            "prompt": "",
            "model_name": MODEL_NAME,
            "error": None,
        },
    )


@app.post("/", response_class=HTMLResponse)
async def ask(request: Request, prompt: str = Form("")):
    prompt = (prompt or "").strip()
    resultat = None
    error = None

    if prompt:
        try:
            resultat = call_ollama(prompt)
        except requests.exceptions.ConnectionError:
            error = "Impossible de contacter Ollama. Vérifie que Ollama est lancé sur http://localhost:11434."
        except requests.exceptions.HTTPError as exc:
            error = f"Erreur HTTP Ollama : {exc}"
        except Exception as exc:
            error = f"Erreur : {exc}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "resultat": resultat,
            "prompt": prompt,
            "model_name": MODEL_NAME,
            "error": error,
        },
    )


@app.post("/api/chat")
async def api_chat(payload: dict):
    """Endpoint API utilisable par une interface JavaScript."""
    message = (payload.get("message") or "").strip()
    if not message:
        return JSONResponse({"error": "Le champ 'message' est obligatoire."}, status_code=400)

    try:
        answer = call_ollama(message)
        return {"model": MODEL_NAME, "response": answer}
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
