from fastapi import APIRouter, HTTPException

from app.schemas.profile import UserProfileCreate, UserProfileRead


router = APIRouter()

_profiles: dict[int, UserProfileRead] = {}
_profile_id = 1


@router.post("/", response_model=UserProfileRead)
def create_profile(payload: UserProfileCreate) -> UserProfileRead:
    global _profile_id
    profile = UserProfileRead(id=_profile_id, **payload.model_dump())
    _profiles[_profile_id] = profile
    _profile_id += 1
    return profile


@router.get("/{profile_id}", response_model=UserProfileRead)
def get_profile(profile_id: int) -> UserProfileRead:
    profile = _profiles.get(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
