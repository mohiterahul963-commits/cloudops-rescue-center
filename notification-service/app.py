from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "CloudOps Notification Service is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/notify")
def notify():
    return jsonify({
        "message": "Notification processed successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)