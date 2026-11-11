"""Health and safe error handling tests."""

from fastapi.testclient import TestClient

from app.core.config import Settings
from app.core.exceptions import AppError
from app.main import create_app


def make_app():
    return create_app(Settings(_env_file=None, app_env="test"))


def test_health() -> None:
    with TestClient(make_app()) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "screenshot-action-inbox"}


def test_custom_error() -> None:
    app = make_app()

    @app.get("/test-error")
    def fail():
        raise AppError("not_ready", "Please try later.", 409)

    with TestClient(app) as client:
        response = client.get("/test-error")
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "not_ready", "message": "Please try later."}}


def test_unexpected_error_hides_details() -> None:
    app = make_app()

    @app.get("/test-crash")
    def crash():
        raise RuntimeError("private detail")

    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/test-crash")
    assert response.status_code == 500
    assert "private detail" not in response.text
    assert response.json()["error"]["code"] == "internal_error"
