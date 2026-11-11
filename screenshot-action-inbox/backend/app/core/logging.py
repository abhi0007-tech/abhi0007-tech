"""Application logging without sensitive request bodies."""

import logging

from app.core.config import Settings


def setup_logging(settings: Settings) -> None:
    """Configure logging when the hosting process has no handlers yet."""
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger("app").setLevel(settings.log_level)
