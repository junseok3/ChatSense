from fastapi import FastAPI, Body
from .model import EmojiModel

app = FastAPI(title="ChatSense Backend", version="0.1.0")
model = EmojiModel()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(text: str = Body(..., embed=True)):

    preds = model.predict(text)
    return {"predictions": preds}
