from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.coach import CoachSummary
from app.services.coach_service import build_coach_summary


router = APIRouter()


@router.get("/summary", response_model=CoachSummary)
def get_coach_summary(db: Session = Depends(get_db)) -> CoachSummary:
    return build_coach_summary(db)
