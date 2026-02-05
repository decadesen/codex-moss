from sqlalchemy.orm import Session

from app.schemas.context import ContextPayload, ContextResponse, ContextSource
from app.services.memory_service import retrieve_memories_with_scores


def build_context(db: Session, payload: ContextPayload) -> ContextResponse:
    memories = retrieve_memories_with_scores(
        db,
        query=payload.query,
        memory_type=payload.memory_type,
        tags=payload.tags,
        limit=payload.limit,
    )
    sources = [
        ContextSource(
            id=memory.id,
            type=memory.type,
            content=memory.content,
            confidence=memory.confidence,
            importance=memory.importance,
            tags=memory.tags or [],
            score=score,
            reasons=reasons,
        )
        for memory, score, reasons in memories
    ]
    summary_lines = [
        f"{source.type}: {source.content}" for source in sources[: payload.summary_size]
    ]
    summary = "\n".join(summary_lines) if summary_lines else "暂无可用记忆上下文。"
    return ContextResponse(summary=summary, sources=sources)
