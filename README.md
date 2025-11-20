# 🗣️ My Voice Assistant - Python Project

A smart **online** voice assistant built using Python.  
Supports speech recognition, text-to-speech, to-do list, notes, Wikipedia search, weather updates, jokes, and more!

## ✨ Features
- Greeting based on time
- Tell time, date & day
- Add/View/Delete Tasks & Notes (saved permanently)
- Search Wikipedia by voice
- Get live weather (any city across the world)
- Tell jokes
- Fully modular code (easy to understand & extend)

## 🛠️ Technologies Used
- `speech_recognition` + Microphone
- `win32com` (Windows TTS)
- `wikipedia` API
- `open-meteo` (free weather API - no key needed)
- File handling for persistent data

## 🚀 How to Run
1. Clone this repo
2. `pip install -r requirements.txt`
3. Run: `python main.py`
4. Wait for "Listening..." to come and then start speaking

## 📁 Project Structure (Modular Design)
- `main.py` → The brain (while loop + command routing)
- `modules/` → Separated logic (audio, skills, etc.)
- `data/` → Stores your tasks & notes (ignored in GitHub)

Made with ❤️ for my Python Major Project  
Feel free to work and improve!

Contact me if any errors faced, or doubts in the project: https://discord.gg/s4qsdWS5S2