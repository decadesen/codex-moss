from fastapi import APIRouter

from app.api.v1 import goals, memories, profiles


api_router = APIRouter()
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(memories.router, prefix="/memories", tags=["memories"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"])
