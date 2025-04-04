
import requests
from bs4 import BeautifulSoup

def scrape_sample_flights(origin, destination, date):
    # For now, we'll use a static HTML source (or this can be changed to a real open website)
    url = "https://example.com/flights"  # This URL would be replaced with a real endpoint if allowed

    # Simulate parsing from an HTML page
    html = '''
    <html>
        <body>
            <div class="flight">
                <span class="airline">Test Airways</span>
                <span class="flight-number">TA101</span>
                <span class="departure">08:00</span>
                <span class="arrival">10:30</span>
                <span class="duration">2h 30m</span>
                <span class="price">₹4000</span>
            </div>
            <div class="flight">
                <span class="airline">Demo Airlines</span>
                <span class="flight-number">DA202</span>
                <span class="departure">13:00</span>
                <span class="arrival">15:45</span>
                <span class="duration">2h 45m</span>
                <span class="price">₹5200</span>
            </div>
        </body>
    </html>
    '''

    soup = BeautifulSoup(html, "html.parser")
    flights = []

    for div in soup.find_all("div", class_="flight"):
        flights.append({
            "airline": div.find("span", class_="airline").text,
            "flight_number": div.find("span", class_="flight-number").text,
            "departure": div.find("span", class_="departure").text,
            "arrival": div.find("span", class_="arrival").text,
            "duration": div.find("span", class_="duration").text,
            "price": div.find("span", class_="price").text,
            "booking_url": "https://www.example.com/book"
        })

    return flights
