"""Validated configuration loaded from environment variables and .env."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BACKEND_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "screenshot-action-inbox"
    app_env: Literal["development", "test", "production"] = "development"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    data_dir: Path = Path("./data")
    max_upload_bytes: int = Field(default=10 * 1024 * 1024, gt=0)


@lru_cache
def get_settings() -> Settings:
    """Read settings once per process. Clear cache in tests if needed."""
    return Settings()
