from fastapi import FastAPI
from api.routes import router as api_router
from infrastructure.databases.db import init_db

app = FastAPI(title="Eat Today API")

app.include_router(api_router, prefix="/api", tags=["api"])

@app.get("/")
async def root():
    return {"message": "Welcome to Eat Today API"}

@app.on_event("startup")
async def startup_event():
    init_db()