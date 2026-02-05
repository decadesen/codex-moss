from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.memory import MemoryCreate, MemoryRead
from app.services import memory_service


router = APIRouter()


@router.post("/", response_model=MemoryRead)
def create_memory(
    payload: MemoryCreate,
    db: Session = Depends(get_db),
) -> MemoryRead:
    return memory_service.create_memory(db, payload)


@router.get("/{memory_id}", response_model=MemoryRead)
def get_memory(
    memory_id: int,
    db: Session = Depends(get_db),
) -> MemoryRead:
    memory = memory_service.get_memory(db, memory_id)
    if memory is None:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memory


@router.get("/", response_model=list[MemoryRead])
def list_memories(db: Session = Depends(get_db)) -> list[MemoryRead]:
    return memory_service.list_memories(db)


@router.get("/search/", response_model=list[MemoryRead])
def search_memories(
    query: str | None = None,
    memory_type: str | None = None,
    tags: str | None = None,
    limit: int = 5,
    db: Session = Depends(get_db),
) -> list[MemoryRead]:
    parsed_tags = [tag.strip() for tag in tags.split(",")] if tags else None
    return memory_service.retrieve_memories(
        db,
        query=query,
        memory_type=memory_type,
        tags=parsed_tags,
        limit=limit,
    )
