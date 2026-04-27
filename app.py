from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

# Harness demo app; trivial edit to verify CI workflow triggers on push.

# These would be injected at build time
COMMIT_SHA = os.environ.get("COMMIT_SHA", "unknown")
START_TIME = time.time()

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

@app.route('/cal')
def cal():
    """GET /cal?a=&b= — return result = a + b + 2.

    Required by workspace issue OWE-27 (product spec); intentionally updates the prior a + b + 1 behavior.
    """
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return jsonify({"error": "missing required query parameters: a, b"}), 400
    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return jsonify({"error": "a and b must be valid numbers"}), 400
    return jsonify({"a": a, "b": b, "result": a + b + 2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
