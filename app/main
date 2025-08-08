from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup_ip():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP address is required"}), 400

    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    if data.get("status") != "success":
        return jsonify({"error": "Failed to retrieve data"}), 500

    result = {
        "ip": ip,
        "country": data.get("country"),
        "region": data.get("regionName"),
        "city": data.get("city"),
        "lat": data.get("lat"),
        "lon": data.get("lon"),
        "isp": data.get("isp")
    }

    return jsonify(result)
