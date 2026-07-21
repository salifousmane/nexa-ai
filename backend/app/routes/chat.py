from fastapi import APIRouter

from app.schemas.ai_schema import (
    ChatRequest,
    ChatResponse
)

from app.services.openai_service import (
    generate_ai_response
)


router = APIRouter()


MENTOR_SYSTEM_PROMPT = """
Tu es Nexa Mentor.

Tu accompagnes les utilisateurs
dans leur évolution professionnelle
et leur apprentissage.

Tu expliques simplement,
tu encourages la progression
et tu proposes des actions concrètes.
"""


@router.post(
    "/",
    response_model=ChatResponse
)
def chat_with_mentor(
    request: ChatRequest
):

    response = generate_ai_response(
        MENTOR_SYSTEM_PROMPT,
        request.message
    )

    return {
        "response": response
    }