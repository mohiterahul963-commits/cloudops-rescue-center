from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


incidents = [
    {
        "id": "INC001",
        "title": "Website Down",
        "severity": "HIGH",
        "status": "OPEN"
    },
    {
        "id": "INC002",
        "title": "Database Error",
        "severity": "MEDIUM",
        "status": "OPEN"
    }
]

NOTIFICATION_SERVICE_URL = "http://notification-service:5001/notify"

@app.route("/")
def home():
    return "CloudOps Incident API is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)


@app.route("/incidents", methods=["POST"])
def create_incident():

    data = request.form

    incident = {
        "id": data["id"],
        "title": data["title"],
        "severity": data["severity"],
        "status": "OPEN"
    }

    incidents.append(incident)

    notification_response = requests.get(NOTIFICATION_SERVICE_URL)

    return jsonify({
        "message": "Incident created successfully",
        "incident": incident,
        "notification": notification_response.json()
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)