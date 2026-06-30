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
Learned about REST API's (Representational State Transfer Application Programming Interface) and made a get request to n2yo's satellites API. Here we were able to use a NORAD ID in order to track information about specific satallites, where we formatted the json response into legible information for the user. Translated the timestamp into something more readable using datetime