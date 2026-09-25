from flask import Flask, render_template
import requests

app = Flask(__name__)

INCIDENT_API_URL = "http://127.0.0.1:5000/incidents"


@app.route("/")
def home():
    response = requests.get(INCIDENT_API_URL)
    incidents = response.json()

    return render_template("index.html", incidents=incidents)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)