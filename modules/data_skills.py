from modules.audio import speak
from datetime import datetime

def add_task(task):
    with open("data/todo_list.txt", "a") as f:
        f.write(task + "\n")
    speak("Task added successfully.")

def show_task():
    try:
        with open("data/todo_list.txt", "r") as f:
            tasks = f.readlines()
        if tasks:
            speak("Here are your tasks")
            for i, task in enumerate(tasks,1):
                speak(f"Task {i}: {task.strip()}")
            else:
                speak("These are only added tasks")
        else:
            speak("Your todo list is empty")
    except:
        speak("No tasks found")

def remove_task():
    try:
        with open("data/todo_list.txt", "w") as f:
            pass
        speak("All tasks removed")
    except:
        speak("No tasks found")

def add_notes(notes):
    speak("What note do you want me to save?")
    note=takespeech()
    with open("data/notes.txt", "a") as f:
        timestamp=datetime.now().strftime("%Y-%m-%d, %A, %H:%M")
        f.write(f"[{timestamp}] {note}\n\t")
    speak("Note saved")

def show_notes():
    try:
        with open("data/notes.txt", "r") as f:
            notes = f.readlines()
        if notes:
            speak("Here is your notes")
            print(notes + "\n\n")
        else:
            speak("No notes avaliable.")
    except:
        speak("No notes yet saved!")

def remove_notes():
    try:
        with open("data/notes.txt", "w") as f:
            pass
        speak("All notes removed")
    except:
        speak("No notes avaliable")