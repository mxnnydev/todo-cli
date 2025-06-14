from datetime import datetime
from time import sleep
import os

def get_time_of_day():
    hour = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"
    

# clear the terminal in smooth transition ~ AVOID Flickering
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[H\033[J", end='')  # ANSI for smooth clearing



if __name__ == '__main__':
    while True:
        curr_time = datetime.now().strftime("%I:%M:%S%p")
        print(f"Welcome current time: {curr_time}")
        clear_screen()
        sleep(1)