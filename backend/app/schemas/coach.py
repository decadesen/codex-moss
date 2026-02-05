from pydantic import BaseModel, Field


class CoachSummary(BaseModel):
    focus: str
    observations: list[str] = Field(default_factory=list)
    suggested_actions: list[str] = Field(default_factory=list)
    related_memories: list[str] = Field(default_factory=list)
