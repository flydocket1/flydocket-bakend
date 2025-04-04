
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/api/scrape", methods=["GET"])
def scrape_flights():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    date = request.args.get("date", datetime.date.today().isoformat())

    # Simulated response (replace this with actual scraping logic)
    flights = [
        {
            "airline": "IndiGo",
            "flight_number": "6E123",
            "departure": "10:00",
            "arrival": "12:30",
            "duration": "2h 30m",
            "price": "₹4500",
            "booking_url": "https://www.makemytrip.com/flights/"
        },
        {
            "airline": "Air India",
            "flight_number": "AI202",
            "departure": "14:00",
            "arrival": "16:45",
            "duration": "2h 45m",
            "price": "₹5100",
            "booking_url": "https://www.goibibo.com/flights/"
        }
    ]

    return jsonify({"flights": flights})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
