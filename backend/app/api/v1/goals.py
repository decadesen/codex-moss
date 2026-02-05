from fastapi import APIRouter, HTTPException

from app.schemas.goal import GoalCreate, GoalRead


router = APIRouter()

_goals: dict[int, GoalRead] = {}
_goal_id = 1


@router.post("/", response_model=GoalRead)
def create_goal(payload: GoalCreate) -> GoalRead:
    global _goal_id
    goal = GoalRead(id=_goal_id, **payload.model_dump())
    _goals[_goal_id] = goal
    _goal_id += 1
    return goal


@router.get("/{goal_id}", response_model=GoalRead)
def get_goal(goal_id: int) -> GoalRead:
    goal = _goals.get(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal
