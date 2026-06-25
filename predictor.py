import requests
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.n2yo.com/rest/v1/satellite/"

def get_iss_passes(lat, lon, alt=0, seconds=10):
    url = f"{BASE_URL}/positions/25544/{lat}/{lon}/{alt}/{seconds}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()

print(get_iss_passes(34.0522, -118.2437))