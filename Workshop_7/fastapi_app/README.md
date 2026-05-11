Assistant local FastAPI

Prérequis
- Python 3.10+
- `pip install fastapi uvicorn transformers torch`

Démarrage rapide
1. Depuis la racine du dépôt, lancez :
```bash
pip install -r requirements.txt  # optionnel si vous créez ce fichier
uvicorn Workshop_7.fastapi_app.main:app --reload --host 0.0.0.0 --port 8000
```
2. Ouvrez http://localhost:8000 dans votre navigateur.

Structure de l'application
- `main.py` : application FastAPI, montage de `/static`, rendu des templates et chargement du modèle depuis `assets/gemma-3-1b-it`.
- `templates/index.html` : page unique avec formulaire et affichage du résultat.
- `static/style.css` : styles copiés depuis l'ancienne application.
- `assets/` : dossier attendu pour le modèle, non versionné ici.

Remarques
- L'application détecte CUDA et choisit le device automatiquement. Modifiez `device` dans `main.py` pour forcer CPU ou GPU.
- Si le dossier du modèle est volumineux, gardez-le hors de Git et pointez `MODEL_PATH` vers un emplacement externe.
- Pour un déploiement sans `--reload`, retirez l'option et exécutez l'application derrière un gestionnaire de processus.

Si vous voulez, je peux aussi ajouter un `requirements.txt` et un exemple de service système.
