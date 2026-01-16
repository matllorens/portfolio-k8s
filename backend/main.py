import os
import socket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (para que el frontend pueda pegarle al backend sin drama)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = os.getenv("API_PREFIX") or "/api"

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"status": "ready"}

@app.get(f"{API_PREFIX}/projects")
def projects():
    return {
        "pod": socket.gethostname(),
        "projects": [
            {
                "id": 1,
                "title": "Kubernetes Portfolio",
                "stack": ["Kubernetes", "Nginx", "FastAPI"],
                "link": "https://example.com",
            }
        ],
    }

@app.get(f"{API_PREFIX}/cv")
def cv():
    # Por ahora devolvemos una URL fija. Luego lo reemplazamos por Spaces URL firmada.
    return {"pod": socket.gethostname(), "url": "/cv.pdf"}
