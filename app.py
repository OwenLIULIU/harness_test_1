from flask import Flask, jsonify, request
import os
import time
import uuid
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_dsn = os.environ.get("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

app = Flask(__name__)

# These would be injected at build time
COMMIT_SHA = os.environ.get("COMMIT_SHA", "unknown")
START_TIME = time.time()


def _parse_cal_query_params():
    """Parse a and b from the query string, or return (None, (response, status)) on error."""
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return None, (jsonify({"error": "missing required query parameters: a, b"}), 400)
    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return None, (jsonify({"error": "a and b must be valid numbers"}), 400)
    return (a, b), None

@app.route('/')
def hello():
    return "Harness Automation Demo is running!"

@app.route('/health')
def health():
    return jsonify({"status": "ok", "timestamp": time.time()})

@app.route('/version')
def version():
    return jsonify({
        "commit": COMMIT_SHA,
        "env": "local-factory",
        "up_since": START_TIME
    })

@app.route('/crash')
def crash():
    """Trigger a division by zero to test Sentry exception tracking."""
    try:
        1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return jsonify({"error": "division by zero caught and reported"}), 500
    return "This should not be reached"

@app.route("/sentry_test_1")
def sentry_test_1():
    """
    Each request sends a Sentry error event with a unique fingerprint so a new
    Sentry issue is created per API call (grouping is not merged with prior runs).
    """
    if not os.environ.get("SENTRY_DSN"):
        return jsonify(
            {"error": "SENTRY_DSN is not set; configure it to report to Sentry."}
        ), 503
    with sentry_sdk.new_scope() as scope:
        scope.fingerprint = ["sentry_test_1", str(uuid.uuid4())]
        sentry_sdk.capture_message(
            "sentry_test_1: event from GET /sentry_test_1",
            level="error",
        )
    sentry_sdk.flush(timeout=2.0)
    return jsonify({"ok": True, "message": "Sentry event sent"})

@app.route("/v1/cal")
def cal_v1():
    """Legacy contract: result = a + b + 1. Current default is GET /cal (v2, a + b + 2)."""
    parsed, err = _parse_cal_query_params()
    if err is not None:
        return err
    a, b = parsed
    return jsonify(
        {
            "a": a,
            "b": b,
            "result": a + b + 1,
            "api_version": 1,
        }
    )


@app.route("/cal")
def cal():
    """Default /cal: result = a + b + 2 (OWE-27). Legacy clients: GET /v1/cal."""
    parsed, err = _parse_cal_query_params()
    if err is not None:
        return err
    a, b = parsed
    return jsonify(
        {
            "a": a,
            "b": b,
            "result": a + b + 2,
            "api_version": 2,
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
