# ISS Pass Predictor🛰️

A CLI tool that calls a real public API to fetch the next ISS pass times over any location on Earth. User enters a city or lat/lon, and the tool returns a clean table showing when the ISS will fly overhead. API key is needed.


## How it Works
A user will type in the lat/lon coordinates or city name that they would like to know when the ISS makes a pass over. A call is then made to the N2YO API, which gives the International Space Station's current location, and returns Unix timestamps. This is then converted to readable dates and times and displayed in a table for the user to see.


## How to Run
```bash
git clone https://github.com/YOUR-USERNAME/iss-period-predictor
cd iss-period-predictor
python predictor.py
```


## What I Learned
Made a GET request to n2yo's REST API. I had to create an API key on their website, and store it in a .env file which was added to my .gitignore file. I use a NORAD ID in order to track information about specific satellites, where I then formatted the json response into legible information for the user. Translated the timestamp into something more readable using datetime otherwise it would just be a long integer that has no meaning to normal users.