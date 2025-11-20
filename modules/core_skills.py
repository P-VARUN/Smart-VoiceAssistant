import datetime
import pyjokes
from modules.audio import speak

def tell_time():
    time=datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def tell_date():
    date=datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def tell_day():
    day=datetime.datetime.now().strftime("%A")
    speak(f"Today is {day}")

def greetings():
    hour=datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
    elif 17 <= hour < 21:
        speak("Good evening!")
    else:
        speak("Hello! It's a great night yet!")

def tell_joke():
    joke=pyjokes.get_joke()
    speak(joke)