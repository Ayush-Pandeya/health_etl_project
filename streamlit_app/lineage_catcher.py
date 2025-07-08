from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)
LOG_DIR = os.path.join(os.path.dirname(__file__), "lineage_logs")
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/lineage", methods=["POST"])
def receive_lineage():
    event = request.json
    if not event:
        return jsonify({"error": "No JSON payload received"}), 400

    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%f")
    filename = f"lineage_event_{timestamp}.json"
    filepath = os.path.join(LOG_DIR, filename)

    with open(filepath, "w") as f:
        json.dump(event, f, indent=2)

    print(f" Lineage event saved: {filename}")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5001)
