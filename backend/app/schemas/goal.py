from datetime import date

from pydantic import BaseModel


class GoalBase(BaseModel):
    title: str
    description: str | None = None
    due_date: date | None = None
    status: str = "active"
    progress: float = 0.0


class GoalCreate(GoalBase):
    pass


class GoalRead(GoalBase):
    id: int

    class Config:
        from_attributes = True
