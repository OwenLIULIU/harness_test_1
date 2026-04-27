from flask import Flask, request, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import os

sentry_dsn = os.environ.get("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/version')
def version():
    return jsonify({"commit": os.environ.get("COMMIT_SHA", "dev"), "built_at": "now"})

@app.route('/crash')
def crash():
    1 / 0
    return "This should not be reached"

@app.route('/cal')
def cal():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"result": a + b + 2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
