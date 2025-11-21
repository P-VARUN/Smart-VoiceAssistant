from modules.audio import speak, takespeech
from modules.core_skills import greetings, tell_time, tell_date, tell_day, tell_joke
from modules.data_skills import add_task, show_task, remove_task, add_notes, show_notes, remove_notes
from modules.web_skills import search_wikipedia, get_weather
from modules.chatbot import chatbot
import re
import time; time.sleep(0.8)

greetings()
speak("How can I help you today?")

while True:
    uservoice = takespeech()
    #-------------------------------------------MATHEMATICAL CALCULATIONS
    nums=re.findall(r"\d+", uservoice)
    #-------------------------------------------TIME AND DATE AND DAY
    if "time" in uservoice:
        tell_time()
    elif "date" in uservoice:
        tell_date()
    elif "day" in uservoice:
        tell_day()
    #-------------------------------------------JOKES
    elif "joke" in uservoice:
        tell_joke()
    #-------------------------------------------FOR TO DO LIST(TASKS)
    elif any(word in uservoice for word in ["add task", "add new task", "add a task", "add a new task", "add to task", "add this to task"]):
        remove_list=["add task", "add new task", "add a task", "add a new task", "add to task", "add this to task"]
        for phrase in remove_list:
            task=uservoice.replace(phrase, "")
        task=task.strip()
        if (task!=""):
            add_task(task)
        else:
            speak("What task do you want to add?")
            task=takespeech()
            if (task!="none"):
                add_task(task)
    #Task showing--------------------
    elif any(word in uservoice for word in ["show task", "show tasks", "view task", "view tasks"]):
        show_task()
    #Task removing-------------------
    elif any(word in uservoice for word in ["remove task", "remove tasks", "delete task", "delete tasks", "clear task", "clear tasks"]):
        remove_task()
    #-------------------------------------------NOTES
    elif any(word in uservoice for word in ["add note", "add new note", "add a note", "add a new note" , "add to note", "add this to note"]):
        remove_list=["add note", "add new note", "add a note", "add a new note", "add to note", "add this to note"]
        for phrase in remove_list:
            note=uservoice.replace(phrase, "")
        note=note.strip()
        if (note!=""):
            add_notes(note)
        else:
            speak("What note do you want to add?")
            note=takespeech()
            if (note!=""):
                add_notes(note)
    #Notes showing-----------------
    elif any(word in uservoice for word in ["show note", "show notes", "view note", "view notes"]):
        view_notes()
    #Notes removing----------------
    elif any(word in uservoice for word in ["remove note", "remove notes", "delete note", "delete notes", "clear note", "clear notes"]):
        remove_notes()
    #-------------------------------------------WIKIPEDIA
    elif any(word in uservoice for word in ["search", "wikipedia", "google it"]):
        query = uservoice
        for remove_word in ["search", "wikipedia", "google it"]:
            query = query.replace(remove_word, "")
        search_wikipedia(query)
    #-------------------------------------------WEATHER
    elif "weather" in uservoice:
        city = uservoice
        junk_words = ["weather", "in", "the", "what", "is", "check", "temperature", "for", "please", "me", "tell"]
        for word in junk_words:
            city = city.replace(word, "")
        city = city.strip()
        print(f"Searching for city: '{city}'")
        if city == "":
            get_weather("Delhi")
        else:
            get_weather(city)
    #-------------------------------------------SIMPLE MATH5
    elif len(nums) >=2:
        a, b = int(nums[0]),int(nums[1])
        if any(sign in uservoice for sign in["add", "addition", "sum", "+"]):
            speak(a+b)
        elif any(sign in uservoice for sign in["minus", "subtraction", "difference","-"]):
            speak(a-b)
        elif any(sign in uservoice for sign in["x", "multiply", "product"]):
            speak(a*b)
        elif any(sign in uservoice for sign in["/", "divided", "division"]):
            if b!=0:
                speak(a/b)
            else:
                speak("Cannot divide by 0")
        else:
            pass
    #-------------------------------------------CHATBOT
    else:
        chatbot(uservoice)