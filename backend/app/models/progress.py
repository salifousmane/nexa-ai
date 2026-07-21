from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    learning_path_id = Column(
        Integer,
        ForeignKey("learning_paths.id"),
        nullable=False
    )

    completion = Column(
        Float,
        default=0.0
    )

    current_step = Column(
        String(255),
        default=""
    )

    user = relationship("User")

    learning_path = relationship("LearningPath")