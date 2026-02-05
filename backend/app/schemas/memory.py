from pydantic import BaseModel, Field


class MemoryBase(BaseModel):
    type: str
    content: str
    source: str
    confidence: float = 0.8
    importance: float = 0.5
    tags: list[str] = Field(default_factory=list)


class MemoryCreate(MemoryBase):
    pass


class MemoryRead(MemoryBase):
    id: int
    access_count: int = 0

    class Config:
        from_attributes = True
