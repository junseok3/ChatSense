# Backend

## Run (dev)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# GET http://localhost:8000/health
# POST http://localhost:8000/predict  body: { "text": "i'm happy" }
```
