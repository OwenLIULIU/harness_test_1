"""HTTP tests for app routes."""

from unittest.mock import patch

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_cal_v2_default(client):
    r = client.get("/cal?a=1&b=2")
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 5.0
    assert data["api_version"] == 2
    assert data["a"] == 1.0
    assert data["b"] == 2.0


def test_cal_v1_legacy(client):
    r = client.get("/v1/cal?a=1&b=2")
    assert r.status_code == 200
    data = r.get_json()
    assert data["result"] == 4.0
    assert data["api_version"] == 1


def test_cal_missing_params(client):
    r = client.get("/cal?a=1")
    assert r.status_code == 400
    assert "error" in r.get_json()


def test_cal_invalid_number(client):
    r = client.get("/cal?a=x&b=2")
    assert r.status_code == 400


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_sentry_test_1_missing_dsn(client, monkeypatch):
    monkeypatch.delenv("SENTRY_DSN", raising=False)
    r = client.get("/sentry_test_1")
    assert r.status_code == 503
    assert "error" in r.get_json()


@patch("sentry_sdk.flush")
@patch("sentry_sdk.capture_message")
def test_sentry_test_1_sends_event(mock_capture, mock_flush, client, monkeypatch):
    monkeypatch.setenv("SENTRY_DSN", "https://key@o4500000000000000.ingest.sentry.io/1")
    r = client.get("/sentry_test_1")
    assert r.status_code == 200
    assert r.get_json()["ok"] is True
    mock_capture.assert_called_once()
    args, kwargs = mock_capture.call_args
    assert args[0] == "sentry_test_1: event from GET /sentry_test_1"
    assert kwargs.get("level") == "error"
    mock_flush.assert_called_once()
