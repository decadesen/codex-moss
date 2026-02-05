from __future__ import annotations

import math
from datetime import datetime, timezone

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models.memory import Memory
from app.schemas.memory import MemoryCreate


def create_memory(db: Session, payload: MemoryCreate) -> Memory:
    memory = Memory(**payload.model_dump())
    db.add(memory)
    db.commit()
    db.refresh(memory)
    return memory


def get_memory(db: Session, memory_id: int) -> Memory | None:
    return db.get(Memory, memory_id)


def list_memories(db: Session) -> list[Memory]:
    return db.query(Memory).order_by(Memory.id.desc()).all()


def _recency_score(last_accessed: datetime | None, created_at: datetime | None) -> float:
    reference = last_accessed or created_at
    if reference is None:
        return 0.3
    now = datetime.now(timezone.utc)
    delta_days = max((now - reference).days, 0)
    return math.exp(-delta_days / 30)


def _score_memory(
    memory: Memory,
    *,
    query: str | None,
    memory_type: str | None,
    tags: list[str] | None,
) -> tuple[float, list[str]]:
    reasons: list[str] = []
    if query and query.lower() in memory.content.lower():
        reasons.append("匹配关键词")
    if memory_type and memory.type == memory_type:
        reasons.append("类型匹配")
    if tags:
        matched = [tag for tag in tags if tag in (memory.tags or [])]
        if matched:
            reasons.append(f"标签匹配: {', '.join(matched)}")
    recency = _recency_score(memory.last_accessed, memory.created_at)
    score = (
        memory.confidence * 0.5
        + memory.importance * 0.3
        + recency * 0.2
    )
    if recency > 0.6:
        reasons.append("近期访问")
    return score, reasons


def retrieve_memories_with_scores(
    db: Session,
    *,
    query: str | None = None,
    memory_type: str | None = None,
    tags: list[str] | None = None,
    limit: int = 5,
) -> list[tuple[Memory, float, list[str]]]:
    statement = select(Memory)
    if query:
        statement = statement.where(
            or_(
                Memory.content.ilike(f"%{query}%"),
                Memory.type.ilike(f"%{query}%"),
            )
        )
    if memory_type:
        statement = statement.where(Memory.type == memory_type)
    if tags:
        statement = statement.where(Memory.tags.contains(tags))
    memories = db.execute(statement).scalars().all()
    scored = [
        (memory, *_score_memory(memory, query=query, memory_type=memory_type, tags=tags))
        for memory in memories
    ]
    scored.sort(key=lambda item: (item[1], item[0].id), reverse=True)
    top = scored[:limit]
    now = datetime.now(timezone.utc)
    for memory, _, _ in top:
        memory.last_accessed = now
        memory.access_count = (memory.access_count or 0) + 1
    if top:
        db.commit()
    return top


def retrieve_memories(
    db: Session,
    *,
    query: str | None = None,
    memory_type: str | None = None,
    tags: list[str] | None = None,
    limit: int = 5,
) -> list[Memory]:
    scored = retrieve_memories_with_scores(
        db,
        query=query,
        memory_type=memory_type,
        tags=tags,
        limit=limit,
    )
    return [memory for memory, _, _ in scored]
