from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


def create_application() -> FastAPI:
    application = FastAPI(
        title="MOSS Backend",
        version="0.1.0",
        description="Core API for the MOSS personal AI assistant.",
        docs_url="/docs" if settings.env != "production" else None,
        redoc_url="/redoc" if settings.env != "production" else None,
    )
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()
