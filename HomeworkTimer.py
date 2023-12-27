from datetime import datetime
import time
from datetime import timedelta
import keyboard
import sys
from win10toast import ToastNotifier

timerRunning = False
start = None
end = None
totalDuration = timedelta()

def log_data(duration, description, date):
    my_data = open("my_data.txt", "a")
    
    my_data.write(f"\nDate: {date}, Duration: {duration}, Description: {description}")

    my_data.close()

def update_timer():
    global timerRunning, end, start, totalDuration
    if timerRunning:
        end = datetime.now()
        # Format the datetime object as a string with both date and time
        formatted_datetime = start.strftime("%Y-%m-%d %H:%M")
        log_data((end-start), "2test", formatted_datetime)
        totalDuration += (end-start)
    else:
        start = datetime.now()
    timerRunning = not timerRunning
  
def printTotalDuration():
    #prints total duration
    print(totalDuration)

keyboard.add_hotkey('ctrl+alt+a', update_timer)
keyboard.add_hotkey('ctrl+alt+q', sys.exit)
keyboard.add_hotkey('ctrl+alt+y', printTotalDuration)
keyboard.wait()


