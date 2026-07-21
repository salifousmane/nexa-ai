from pydantic import BaseModel
from typing import Optional


class ProfileCreate(BaseModel):
    profession: Optional[str] = None
    education_level: Optional[str] = None
    experience_level: Optional[str] = None
    goal: Optional[str] = None
    available_hours: Optional[int] = None
    preferred_language: Optional[str] = "fr"


class ProfileResponse(ProfileCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True