from fastapi import APIRouter

from app.schemas.ai_schema import (
    DiagnosticRequest,
    DiagnosticResponse
)

from app.services.diagnostic_service import (
    create_diagnostic
)


router = APIRouter()


@router.post(
    "/generate",
    response_model=DiagnosticResponse
)
def generate_diagnostic(
    request: DiagnosticRequest
):

    result = create_diagnostic(
        request.model_dump()
    )

    return result