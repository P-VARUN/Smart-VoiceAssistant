import win32com.client                                  # import library to this file
import speech_recognition as sr                         # import library and rename it as sr(shortform to make it easy to use)
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")      # Starts the speaker
speaker.Rate = 0.8                                      # Speed: -10 to 10
speaker.Volume = 100                                    # speaker volume
speaker.Voice = speaker.GetVoices().Item(1)             # Change voice 0->male 1->female

r=sr.Recognizer()                                       # Initialize the voice recognizer

def speak(text):
    print(f"Assistant: {text}")
    speaker.Speak("")
    speaker.Speak(text)                                       # This NEVER locks audio
    time.sleep(0.8)                                           # Small delay for next mic access

def takespeech():

    try:                                                      # Tries this code, if something goes wrong..
        with sr.Microphone() as source:                       # Opens microphone
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)              # Improves accuracy
            r.dynamic_energy_threshold = True                             # keep True usually; set False if it misbehaves after calibration
            r.energy_threshold = r.energy_threshold                       # leave calibrated value (or set numeric e.g. 400)
            r.pause_threshold = 1.8                                       # wait this many seconds of silence before considering phrase complete
            r.phrase_threshold = 0.3                                      # minimum seconds of speaking to consider as phrase (default ~0.3)          
            audio = r.listen(source, timeout=6, phrase_time_limit=None)  # starts recording and stores the listened audio in "audio" variable

        print("Recognizing...")
        uservoice = r.recognize_google(audio, language='en-in')   # Uses google's speech recognition to convert audio to text
        print(f"You: {uservoice}\n")
    except Exception as e:                                        # Except handle the error safely
        print("Say that again please...")
        return "None"
    return uservoice.lower()                                      # Converts the text to lower case and returns it