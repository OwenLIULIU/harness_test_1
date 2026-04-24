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


@app.route("/cal")
def cal():
    """Query: a, b — returns a + b + 2."""
    a_raw, b_raw = request.args.get("a"), request.args.get("b")
    if a_raw is None or b_raw is None:
        return jsonify({"error": "a and b are required"}), 400
    try:
        a, b = float(a_raw), float(b_raw)
    except ValueError:
        return jsonify({"error": "invalid a or b"}), 400
    return jsonify({"result": a + b + 2})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
