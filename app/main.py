from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "🌍 IP Location API is live!"

@app.route('/location')
def get_location():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({'error': 'IP address is required'}), 400

    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
