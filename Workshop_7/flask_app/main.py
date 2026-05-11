from flask import Flask, render_template, request
from transformers import pipeline
import torch
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "assets", "gemma-3-1b-it")
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

print(f"Chargement du modèle depuis {MODEL_PATH} sur {device}...")
pipe = pipeline(
    "text-generation",
    model=MODEL_PATH,
    device=device,
    torch_dtype=torch_dtype,
)
print("Modèle prêt !")


@app.route("/", methods=["GET", "POST"])
def index():
    resultat = None
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            messages = [{"role": "user", "content": prompt}]
            output = pipe(messages, max_new_tokens=300)
            resultat = output[0]["generated_text"][-1]["content"]
    return render_template("index.html", resultat=resultat)


if __name__ == "__main__":
    app.run(debug=True)
