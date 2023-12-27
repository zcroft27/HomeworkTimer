from datetime import datetime
import time
from datetime import timedelta
import keyboard
import sys

timerRunning = False
start = None
end = None


def main():
    #TODO
    return 1


def log_data(duration, description, date):
    my_data = open("my_data.txt", "a")
    
    my_data.write(f"\nDate: {date}, Duration: {duration}, Description: {description}")

    my_data.close()

def update_timer():
    global timerRunning, end, start
    if timerRunning:
        end = datetime.now()
        # Format the datetime object as a string with both date and time
        formatted_datetime = start.strftime("%Y-%m-%d %H:%M")
        log_data((end-start), "2test", formatted_datetime)
    else:
        start = datetime.now()
    timerRunning = not timerRunning
  
# get current time
    # while loop until hotkey is pressed again
    # get end end time 
    # find difference in times
    # prompt user to write description of session
    # write to file


keyboard.add_hotkey('ctrl+alt+a', update_timer)
keyboard.add_hotkey('ctrl+alt+q', sys.exit)
keyboard.wait()


