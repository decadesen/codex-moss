from pydantic import BaseModel


class UserProfileBase(BaseModel):
    display_name: str
    bio: str | None = None
    timezone: str = "UTC"


class UserProfileCreate(UserProfileBase):
    pass


class UserProfileRead(UserProfileBase):
    id: int

    class Config:
        from_attributes = True
