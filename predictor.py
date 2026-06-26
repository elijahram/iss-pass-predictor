import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.n2yo.com/rest/v1/satellite/"


def get_iss_passes():

    while True:

        satellite_choice = input(
            "Would you like to select a preset satellite or choose your own satellite ID?\nPress 1 : ISS\nPress 2 : Hubble Space Telescope\nPress 3 : James Webb Space Telescope\nPress 4 : Enter your own NORAD ID\nPress 5 : Exit\n"
        )

        satellites = {
            1: {"name": "ISS", "id": 25544},
            2: {"name": "Hubble Space Telescope", "id": 20580},
            3: {"name": "James Webb Space Telescope", "id": 50463},
        }

        if satellite_choice == 4:
            sat_id = input(
                "Please enter the NORAD ID of the satellite you wish to track: "
            )
            sat = {"id": sat_id}
        elif satellite_choice == 5:
            break
        else:
            sat = satellites[satellite_choice]

        location_choice = input(
            "Please select the location you would like to know the satellite passes over.\nPress 1 : Los Angeles, CA\nPress 2 : New York City, NY\n Press 3 : London, UK\nPress 4 : Enter your own coordinates\nPress 5 : Exit\n"
        )

        locations = {
            1: {"name": "Hawthorne, CA", "lat": 34.0522, "lon": -118.2437, "alt": 0},
            2: {"name": "New York, NY", "lat": 40.7128, "lon": -74.0060, "alt": 0},
            3: {"name": "London, UK", "lat": 51.5074, "lon": -0.1278, "alt": 0},
        }

        if location_choice == 4:
            lon = float(input("Enter the longitude coordinate : "))
            lat = float(input("Enter the latitude coordinate: "))
            alt = float(
                input("Enter altitude above sea level in meters (enter 0 if unknown): ")
            )
            loc = {"lon": lon, "lat": lat, "alt": alt}
        elif location_choice == 5:
            break
        else:
            loc = locations[location_choice]

        url = f"{BASE_URL}/positions/{sat['id']}/{loc['lat']}/{loc['lon']}/{loc['alt']}/{10}&apiKey={API_KEY}"
        response = requests.get(url)
        return response.json()


get_iss_passes()
