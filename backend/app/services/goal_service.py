from sqlalchemy.orm import Session

from app.models.goal import Goal
from app.schemas.goal import GoalCreate


def create_goal(db: Session, payload: GoalCreate) -> Goal:
    goal = Goal(**payload.model_dump())
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal


def get_goal(db: Session, goal_id: int) -> Goal | None:
    return db.get(Goal, goal_id)


def list_goals(db: Session) -> list[Goal]:
    return db.query(Goal).order_by(Goal.id.desc()).all()
