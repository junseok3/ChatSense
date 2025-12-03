# backend/app/main.py
from pathlib import Path
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .model import EmojiModel


BASE_DIR = Path(__file__).resolve().parent.parent   # .../backend
INDEX_DIR = BASE_DIR / "indexes"                    # .../backend/indexes
ASSETS_DIR = INDEX_DIR / "assets"                   # .../backend/indexes/assets

app = FastAPI(title="ChatSense Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/assets", StaticFiles(directory=str(ASSETS_DIR)), name="assets")


model = EmojiModel(base=str(INDEX_DIR))


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: dict = Body(...)):
    text = payload.get("text", "")
    return {"predictions": model.predict(text)}
