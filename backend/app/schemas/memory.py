from pydantic import BaseModel


class MemoryBase(BaseModel):
    type: str
    content: str
    source: str
    confidence: float = 0.8
    tags: list[str] = []


class MemoryCreate(MemoryBase):
    pass


class MemoryRead(MemoryBase):
    id: int

    class Config:
        from_attributes = True
