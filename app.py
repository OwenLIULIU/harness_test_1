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

@app.route('/cal')
def cal():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
    except (TypeError, ValueError):
        return jsonify({"error": "a and b must be integers"}), 400
    return jsonify({"result": a + b + 2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
