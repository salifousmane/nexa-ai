from fastapi import APIRouter

from app.schemas.ai_schema import (
    LearningPathResponse
)

from app.services.path_service import (
    generate_learning_path
)


router = APIRouter()


@router.post(
    "/generate",
    response_model=LearningPathResponse
)
def create_path(
    diagnostic: dict
):

    result = generate_learning_path(
        diagnostic
    )

    return result