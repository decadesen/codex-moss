from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.db.session import Base, engine
from app.models import goal, memory, profile


def create_application() -> FastAPI:
    application = FastAPI(
        title="MOSS Backend",
        version="0.1.0",
        description="Core API for the MOSS personal AI assistant.",
        docs_url="/docs" if settings.env != "production" else None,
        redoc_url="/redoc" if settings.env != "production" else None,
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
