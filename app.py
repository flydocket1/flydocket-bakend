
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

from scraper import scrape_sample_flights

app = Flask(__name__)
CORS(app)

@app.route("/api/scrape", methods=["GET"])
def scrape_flights():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    date = request.args.get("date", datetime.date.today().isoformat())

    flights = scrape_sample_flights(origin, destination, date)
    return jsonify({"flights": flights})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
