from fastapi import FastAPI
from config import Config
from cors import add_cors_middleware
from infrastructure.databases.db import init_db

def create_app():
    app = FastAPI(title="Eat Today API")

    # Add CORS middleware
    add_cors_middleware(app)

    # Initialize database
    @app.on_event("startup")
    async def startup_event():
        init_db()

    # Include routers
    from api.routes import router as api_router
    app.include_router(api_router, prefix="/api", tags=["api"])

    return app