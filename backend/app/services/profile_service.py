from sqlalchemy.orm import Session

from app.models.profile import UserProfile
from app.schemas.profile import UserProfileCreate


def create_profile(db: Session, payload: UserProfileCreate) -> UserProfile:
    profile = UserProfile(**payload.model_dump())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def get_profile(db: Session, profile_id: int) -> UserProfile | None:
    return db.get(UserProfile, profile_id)


def list_profiles(db: Session) -> list[UserProfile]:
    return db.query(UserProfile).order_by(UserProfile.id.desc()).all()
