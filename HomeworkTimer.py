from datetime import datetime
import time
from datetime import timedelta
import keyboard
import sys
from win10toast import ToastNotifier
import json

timerRunning = False
start = None
end = None
currentDuration = timedelta()


jsonFilePath = "data.json"



def log_data(duration, description, date):
    my_data = open("my_data.txt", "a")
    
    my_data.write(f"\nDate: {date}, Duration: {duration}, Description: {description}")

    my_data.close()

def update_timer():
    global timerRunning, end, start, currentDuration
    if timerRunning:
        end = datetime.now()
        # Format the datetime object as a string with both date and time
        formatted_datetime = start.strftime("%Y-%m-%d %H:%M")
        log_data((end-start), "2test", formatted_datetime)
        currentDuration = (end-start)
        toaster = ToastNotifier()
        toaster.show_toast("Timer has ended.", f"Session duration: {currentDuration}")
    else:
        start = datetime.now()
        toaster = ToastNotifier()
        toaster.show_toast("Timer has started.", "Happy working.")
    timerRunning = not timerRunning
  
def ToastTotalDuration(dur):
    #prints total duration
    toaster = ToastNotifier()
    toaster.show_toast("Total Duration: ", str(dur))

def parseJsonDuration(dur):
    hours, minutes, seconds = map(float, dur.split(":"))
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def updateJson():
    global currentDuration
    with open(jsonFilePath, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    sumDuration = 0

    for key in jsonData:
        if key == "duration":
            oldTotalDuration = parseJsonDuration(jsonData["duration"])
            sumDuration = currentDuration + oldTotalDuration
            jsonData["duration"] = str(sumDuration)
            ToastTotalDuration(sumDuration)

    with open(jsonFilePath, 'w') as jsonFile:
        json.dump(jsonData, jsonFile, indent=2)

    


#toast notification indicating timer has started
    #toast notification indicating timer has stopped
        # in notification, displays "press 1, 2, or 3 for homework, research, lecture" and wait for user input to close notification   

def closeProgram():
    toaster = ToastNotifier()
    toaster.show_toast("Program has closed.", f"Hotkeys should be off.")
    sys.exit()

keyboard.add_hotkey('ctrl+alt+a', update_timer)
keyboard.add_hotkey('ctrl+alt+q', closeProgram)
keyboard.add_hotkey('ctrl+alt+i', updateJson)
keyboard.wait()


