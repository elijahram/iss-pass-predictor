import requests
from datetime import datetime

URL = "http://api.open-notify.org/iss-now.json"

def get_iss_passes(lat, lon, n=5):
    params = {
        "lat": lat,
        "lon": lon,
        "n": n      # number of passes to return
    }
    response = requests.get(URL, params=params)
    print(response.json())

get_iss_passes(34.0522, -118.2437)