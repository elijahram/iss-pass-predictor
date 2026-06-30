import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.n2yo.com/rest/v1/satellite"


def get_iss_passes():

    while True:

        try:
            satellite_choice = int(
                input(
                    "Would you like to select a preset satellite or choose your own satellite ID?\nPress 1 : ISS\nPress 2 : Hubble Space Telescope\nPress 3 : James Webb Space Telescope\nPress 4 : Enter your own NORAD ID\nPress 5 : Exit\n"
                )
            )
        except ValueError:
            print("This is not a valid input. Please try again.")
            continue

        satellites = {
            1: {"id": 25544},
            2: {"id": 20580},
            3: {"id": 50463},
        }

        if satellite_choice == 4:
            sat_id = input(
                "Please enter the NORAD ID of the satellite you wish to track: "
            )
            sat = {"id": sat_id}
        elif satellite_choice == 5:
            break
        elif satellite_choice in satellites:
            sat = satellites[satellite_choice]
        else:
            print("This is not a valid input. Please try again.")
            continue

        try:
            location_choice = int(
                input(
                    "Please select the location you would like to know the satellite passes over.\nPress 1 : Los Angeles, CA\nPress 2 : New York City, NY\nPress 3 : London, UK\nPress 4 : Enter your own coordinates\nPress 5 : Exit\n"
                )
            )
        except ValueError:
            print("This is not a valid input. Please try again.")
            continue

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
        elif location_choice in locations:
            loc = locations[location_choice]
        else:
            print("This is not a valid input. Please try again.")
            continue

        url = f"{BASE_URL}/positions/{sat['id']}/{loc['lat']}/{loc['lon']}/{loc['alt']}/{1}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if "positions" not in data:
            print("No data returned. Please check your inputs.")
            continue

        info = data["info"]
        pos = data["positions"][0]
        time = datetime.fromtimestamp(data["positions"][0]["timestamp"])

        print(f"""
        Satellite: {info['satname']}
        Latitude:   {pos['satlatitude']}°
        Longitude:  {pos['satlongitude']}°
        Altitude:   {pos['sataltitude']} km
        Azimuth:    {pos['azimuth']}°
        Elevation:  {pos['elevation']}°
        Time:       {time}
        """)


get_iss_passes()
