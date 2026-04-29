"""HTTP tests for app routes."""

from unittest.mock import patch

import pytest

import app as app_module
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


def test_sentry_test_1_skips_sentry_without_dsn(client, monkeypatch):
    monkeypatch.setattr(app_module, "sentry_dsn", None)
    r = client.get("/sentry_test_1")
    assert r.status_code == 200
    data = r.get_json()
    assert data["ok"] is True
    assert data["sent"] is False
    assert "reason" in data


def test_sentry_test_1_sends_with_dsn(client, monkeypatch):
    monkeypatch.setattr(app_module, "sentry_dsn", "https://example@o1.ingest.sentry.io/1")
    with patch("sentry_sdk.capture_message") as cap_m, patch("sentry_sdk.flush"):
        r = client.get("/sentry_test_1")
    assert r.status_code == 200
    data = r.get_json()
    assert data["ok"] is True
    assert data["sent"] is True
    assert "event_id" in data
    assert cap_m.call_count == 1
