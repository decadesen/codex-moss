from fastapi import APIRouter

from app.api.v1 import coach, context, goals, memories, profiles


api_router = APIRouter()
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(memories.router, prefix="/memories", tags=["memories"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"])
api_router.include_router(context.router, prefix="/context", tags=["context"])
api_router.include_router(coach.router, prefix="/coach", tags=["coach"])
