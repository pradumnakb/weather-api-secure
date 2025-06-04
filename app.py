from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your real API key
API_KEY = "ae9f49f2f7fdef520c93207a617a69b9"  

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        })

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

