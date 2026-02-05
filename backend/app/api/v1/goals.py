from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.goal import GoalCreate, GoalRead
from app.services import goal_service


router = APIRouter()


@router.post("/", response_model=GoalRead)
def create_goal(
    payload: GoalCreate,
    db: Session = Depends(get_db),
) -> GoalRead:
    return goal_service.create_goal(db, payload)


@router.get("/{goal_id}", response_model=GoalRead)
def get_goal(
    goal_id: int,
    db: Session = Depends(get_db),
) -> GoalRead:
    goal = goal_service.get_goal(db, goal_id)
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal


@router.get("/", response_model=list[GoalRead])
def list_goals(db: Session = Depends(get_db)) -> list[GoalRead]:
    return goal_service.list_goals(db)
