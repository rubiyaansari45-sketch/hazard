import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from config import APP_CONFIG
from alert.alert_manager import build_alert

load_dotenv()

app = Flask(__name__)
app.config.update(APP_CONFIG)

def assess_habitation(data):
    # Demo scoring model. Replace with a trained/validated model for production use.
    hazard = float(data.get("hazard_score", 0))
    population = int(data.get("population", 0))
    capacity = int(data.get("carrying_capacity", 0))
    vulnerability = float(data.get("vulnerability_score", 0))
    distance = float(data.get("safe_distance_km", 0))

    hazard = max(0, min(hazard, 100))
    vulnerability = max(0, min(vulnerability, 100))

    overload_pct = 0
    if capacity > 0:
        overload_pct = max(0, ((population - capacity) / capacity) * 100)

    # Weighted demo risk score
    risk_score = (hazard * 0.50) + (vulnerability * 0.30) + (min(overload_pct, 100) * 0.20)

    if risk_score >= 75 or hazard >= 85:
        zone = "RED"
    elif risk_score >= 50 or hazard >= 65:
        zone = "AMBER"
    else:
        zone = "GREEN"

    relocation = (
        "IMMEDIATE"
        if zone == "RED" and (vulnerability >= 60 or overload_pct > 20)
        else "PRIORITY"
        if zone in ("RED", "AMBER")
        else "MONITOR"
    )

    alert = build_alert(
        zone=zone,
        relocation=relocation,
        hazard_score=round(hazard, 1),
        overload_pct=round(overload_pct, 1),
        safe_distance_km=round(distance, 1)
    )

    return {
        "zone": zone,
        "risk_score": round(risk_score, 1),
        "population": population,
        "carrying_capacity": capacity,
        "overload_percentage": round(overload_pct, 1),
        "vulnerability_score": round(vulnerability, 1),
        "relocation_need": relocation,
        "safe_distance_km": round(distance, 1),
        "alert": alert
    }

@app.route("/")
def index():
    return render_template("index.html", app_name=APP_CONFIG["APP_NAME"])

@app.route("/api/assess", methods=["POST"])
def api_assess():
    data = request.get_json(silent=True) or {}
    try:
        result = assess_habitation(data)
        return jsonify({"success": True, "result": result})
    except (TypeError, ValueError) as exc:
        return jsonify({"success": False, "error": f"Invalid input: {exc}"}), 400

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": APP_CONFIG["APP_NAME"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
