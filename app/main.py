"""Application entrypoint for the Customer Intelligence Engine API."""

from fastapi import FastAPI
from app.api.router import router


app = FastAPI(
    title="Customer Intelligence Engine",
    version="1.0.0"
)

app.include_router(router)



@app.get("/health")
def health():
    """Return a simple liveness response for monitoring."""
    return {"status": "ok"}