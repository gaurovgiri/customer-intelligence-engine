"""Application entrypoint for the Customer Intelligence Engine API."""

from fastapi import FastAPI
from app.api.router import router


app = FastAPI(
    title="Customer Intelligence Engine",
    version="1.0.0",
    description=(
        "API for customer chat, intent classification, and personalized "
        "recommendations powered by ML and LLM providers."
    ),
)

app.include_router(router)


@app.get("/")
def root():
    """Return basic API information for the root endpoint."""
    return {
        "message": "Welcome to the Customer Intelligence Engine API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    """Return a simple liveness response for monitoring."""
    return {"status": "ok"}
