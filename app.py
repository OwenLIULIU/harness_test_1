from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

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


def _fibonacci(n: int) -> int:
    """0-based: F(0)=0, F(1)=1. Returns 0 for n < 0 (matches Go Fibonacci)."""
    if n < 0:
        return 0
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@app.route("/fibonacci")
def fibonacci():
    n_raw = request.args.get("n", "0")
    try:
        n = int(n_raw)
    except ValueError:
        return jsonify({"error": "query parameter n must be an integer"}), 400
    return jsonify({"n": n, "value": _fibonacci(n)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
