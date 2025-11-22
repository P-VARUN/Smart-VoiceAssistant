from modules.audio import speak, takespeech
import webbrowser
import wikipedia

def chatbot(text):
    text = text.lower()
    if "your name" in text:
        speak("I am just a simple voice assistant, I dont have any name.")
    elif "your age" in text:
        speak("I am a software program, so I don't have age. I only get updated.")
    elif "what can you do" in text:
        speak("I can add notes; Save your tasks; Tell you day, date, time, weather, and jokes.")
    elif "who are you" in text:
        speak("I am voice based program in python, created by a Engineering Student.")
    elif "created you" in text:
        speak("I am created by an Engineeing student.")
        speak("Do you want to know more about him, or ask any question about the project?")
        response = takespeech()
        if any(word in response for word in ["yes","ok","sure","yeah"]):
            invite_url = "https://discord.gg/s4qsdWS5S2"
            speak("Opening Discord invite.")
            webbrowser.open_new_tab(invite_url)
        else:
            pass
    elif any(word in text for word in ["contact admin", "contact creator", "contact host", "contact your creator"]):
        speak("fulfilling your request...")
        webbrowser.open_new_tab("https://discord.gg/s4qsdWS5S2")
    elif any(start in text for start in ["language is used", "language are you created"]):
        speak("I am prepared by using PYTHON programming language.")
        speak("Do you want to know more about python language.")
        response = takespeech()
        if "ok" in response or "yes" in response:
            result = wikipedia.summary("Python (programming language)", sentences=2)
            speak(result)
        else:
            pass
    elif "bye" in text:
        speak("Happy to talk to you, Meet you again.")
        exit()
    elif any(start in text for start in ["hi", "hello", "whatsup!"]):
        speak("Hello , whats in your mind?")
    elif "thank you" in text or "thanks" in text:
        speak("Your welcome!")
    elif "open youtube" in text:
        speak("opening youtube...")
        webbrowser.open_new_tab("https://www.youtube.com/")
    else:
        speak("Sorry I did not hear that.")