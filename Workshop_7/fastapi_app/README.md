FastAPI local assistant

Prerequisites
- Python 3.10+
- pip install fastapi uvicorn transformers torch

Quick start
1. From repository root run:
```bash
pip install -r requirements.txt  # optional if you create one
uvicorn Workshop_7.fastapi_app.main:app --reload --host 0.0.0.0 --port 8000
```
2. Open http://localhost:8000 in your browser.

App structure
- `main.py`: FastAPI app, mounts `/static`, renders templates, loads the model from `assets/gemma-3-1b-it`.
- `templates/index.html`: single-page form + result display.
- `static/style.css`: styles copied from previous app.
- `assets/`: expected model directory (not committed here).

Notes
- The app detects CUDA and sets device automatically; change `device` in `main.py` to force CPU/GPU.
- If the model directory is large, keep it out of Git and point `MODEL_PATH` to an external location.
- To deploy without `--reload` remove the flag and run behind a process manager.

If you want, I can add a `requirements.txt` and a one-line systemd/service example.
