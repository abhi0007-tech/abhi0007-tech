"""Liveness endpoint; does not require database or external services."""

from fastapi import APIRouter, Request

from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check(request: Request) -> HealthResponse:
    return HealthResponse(status="ok", service=request.app.state.settings.app_name)
