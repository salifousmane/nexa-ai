from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.connection import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True
    )

    profession = Column(String(150))

    education_level = Column(String(150))

    experience_level = Column(String(100))

    goal = Column(Text)

    available_hours = Column(Integer)

    preferred_language = Column(
        String(20),
        default="fr"
    )

    user = relationship(
        "User",
        back_populates="profile"
    )