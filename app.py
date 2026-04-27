from flask import Flask, jsonify, request
import os
import time

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
