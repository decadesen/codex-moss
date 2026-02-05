from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.profile import UserProfileCreate, UserProfileRead
from app.services import profile_service


router = APIRouter()


@router.post("/", response_model=UserProfileRead)
def create_profile(
    payload: UserProfileCreate,
    db: Session = Depends(get_db),
) -> UserProfileRead:
    return profile_service.create_profile(db, payload)


@router.get("/{profile_id}", response_model=UserProfileRead)
def get_profile(
    profile_id: int,
    db: Session = Depends(get_db),
) -> UserProfileRead:
    profile = profile_service.get_profile(db, profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/", response_model=list[UserProfileRead])
def list_profiles(db: Session = Depends(get_db)) -> list[UserProfileRead]:
    return profile_service.list_profiles(db)
