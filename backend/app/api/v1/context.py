from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.context import ContextPayload, ContextResponse
from app.services.context_service import build_context


router = APIRouter()


@router.post("/", response_model=ContextResponse)
def create_context(
    payload: ContextPayload,
    db: Session = Depends(get_db),
) -> ContextResponse:
    return build_context(db, payload)
