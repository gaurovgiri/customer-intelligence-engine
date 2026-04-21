from fastapi import FastAPI
from app.api.router import router


app = FastAPI(
    title="Customer Intelligence Engine",
    version="1.0.0"
)

app.include_router(router)



@app.get("/health")
def health():
    return {"status": "ok"}