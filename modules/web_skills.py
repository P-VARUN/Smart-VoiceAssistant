import wikipedia
import requests
from modules.audio import speak

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query ,sentences=2)
        speak("According to wikipedia")
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except:
        speak("Sorry, I could'nt find any result in wikipedia on your requested data.")

def get_weather(city_name):
    speak(f"Checking weather for {city_name}...")
    try:
        #----------------------------------------------------------STEP 1: Find the city's coordinates (Latitude & Longitude)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url).json()
        if "results" in geo_response:
            result = geo_response["results"][0]
            lat = result["latitude"]
            lon = result["longitude"]
        else:
            speak("Sorry, I couldn't find that city.")
            return
        #----------------------------------------------------------STEP 2: Get the weather using those coordinates
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m"
        }
        response = requests.get(url, params=params).json()
        current_temp = response["current"]["temperature_2m"]
        speak(f"The current temperature in {city_name} is {current_temp} degrees celsius")
    except Exception as e:
        print(e)
        speak("Sorry, Server is busy , can't get weather now!")