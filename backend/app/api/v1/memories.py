from fastapi import APIRouter, HTTPException

from app.schemas.memory import MemoryCreate, MemoryRead


router = APIRouter()

_memories: dict[int, MemoryRead] = {}
_memory_id = 1


@router.post("/", response_model=MemoryRead)
def create_memory(payload: MemoryCreate) -> MemoryRead:
    global _memory_id
    memory = MemoryRead(id=_memory_id, **payload.model_dump())
    _memories[_memory_id] = memory
    _memory_id += 1
    return memory


@router.get("/{memory_id}", response_model=MemoryRead)
def get_memory(memory_id: int) -> MemoryRead:
    memory = _memories.get(memory_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
    return memory
