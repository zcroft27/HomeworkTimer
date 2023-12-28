from datetime import datetime
from datetime import timedelta
from win10toast import ToastNotifier
import keyboard, sys, json, easygui


timerRunning = False
start = timedelta()
end = timedelta()
CurrentSessionDuration = timedelta()
session_type = easygui.choicebox

jsonFilePath = "data.json"



def log_data(duration, description, date):
    my_data = open("my_data.txt", "a")
    
    my_data.write(f"\nDate: {date}, Duration: {duration}, Description: {description}")

    my_data.close()

def update_timer():
    global timerRunning, end, start, CurrentSessionDuration, session_type
    if timerRunning:
        end = datetime.now()
        # Format the datetime object as a string with both date and time
        formatted_datetime = start.strftime("%Y-%m-%d %H:%M")
        CurrentSessionDuration = (end-start)
        log_data(CurrentSessionDuration, session_type, formatted_datetime)
        updateJson()
    else:
        session_type = prompt_for_session_type()
        start = datetime.now()
        toaster = ToastNotifier()
        toaster.show_toast("Timer has started.", f"Task: {session_type}.")
    timerRunning = not timerRunning


def prompt_for_session_type():
    global session_type
    # Prompt user for session type
    session_type = easygui.choicebox(
        msg="Select session type",
        title="Session Type",
        choices=["Programming", "Research", "Lecture"]
    )
    return session_type


def ToastTotalDuration(tdur, sdur):
    #prints total duration and session duration
    toaster = ToastNotifier()
    toaster.show_toast(f"Total Duration: {str(tdur)}", f"Session duration: {str(sdur)}")

def parseJsonDuration(dur):
    hours, minutes, seconds = map(float, dur.split(":"))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def updateJson():
    global CurrentSessionDuration
    with open(jsonFilePath, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    sumDuration = 0

    for key in jsonData:
        if key == "Fundamentals 2":
            for innerKey in jsonData[key]:
                if innerKey == "Total duration":
                    oldTotalDuration = parseJsonDuration(jsonData[key][innerKey])
                    sumDuration = CurrentSessionDuration + oldTotalDuration
                    jsonData[key]["Total duration"] = str(sumDuration)
                    ToastTotalDuration(sumDuration, CurrentSessionDuration)
                elif innerKey == "Programming duration" and session_type == "Programming":
                    oldProgrammingDuration = parseJsonDuration(jsonData[key][innerKey])
                    sumProgrammingDuration = CurrentSessionDuration + oldProgrammingDuration
                    jsonData[key]["Programming duration"] = str(sumProgrammingDuration)
                elif innerKey == "Lecture duration" and session_type == "Lecture":
                    oldLectureDuration = parseJsonDuration(jsonData[key][innerKey])
                    sumLectureDuration = CurrentSessionDuration + oldLectureDuration
                    jsonData[key]["Lecture duration"] = str(sumLectureDuration)
                elif innerKey == "Researching duration" and session_type == "Research":
                    oldResearchingDuration = parseJsonDuration(jsonData[key][innerKey])
                    sumResearchingDuration = CurrentSessionDuration + oldResearchingDuration
                    jsonData[key]["Researching duration"] = str(sumResearchingDuration)


                

    with open(jsonFilePath, 'w') as jsonFile:
        json.dump(jsonData, jsonFile, indent=2)

    
def closeProgram():
    toaster = ToastNotifier()
    toaster.show_toast("Program has closed.", f"Hotkeys should be off.")
    sys.exit()

keyboard.add_hotkey('ctrl+alt+a', update_timer)
keyboard.add_hotkey('ctrl+alt+q', closeProgram)
keyboard.wait()


