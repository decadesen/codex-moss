from pydantic import BaseModel, Field


class ContextPayload(BaseModel):
    query: str | None = None
    memory_type: str | None = None
    tags: list[str] = Field(default_factory=list)
    limit: int = Field(default=5, ge=1, le=20)
    summary_size: int = Field(default=3, ge=1, le=10)


class ContextSource(BaseModel):
    id: int
    type: str
    content: str
    confidence: float
    importance: float
    tags: list[str]
    score: float
    reasons: list[str] = Field(default_factory=list)


class ContextResponse(BaseModel):
    summary: str
    sources: list[ContextSource]
