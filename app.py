from flask import Flask, jsonify, request
import os
import time

from calculator import add

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


@app.route("/cal")
def cal():
    """Query: /cal?a=...&b=... — returns a + b + 2."""
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"error": "query parameters a and b are required"}), 400
    return jsonify({"result": add(a, b) + 2})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
