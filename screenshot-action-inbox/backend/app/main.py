"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import Settings, get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings if settings is not None else get_settings()
    setup_logging(settings)
    app = FastAPI(title="Screenshot Action Inbox API", version="0.1.0")
    app.state.settings = settings
    register_exception_handlers(app)
    app.include_router(health_router)
    return app


app = create_app()
