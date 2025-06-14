
# TODO CLI 📝
# A simple command-line to-do list manager built with Python. Allows users to add, view, and remove tasks directly from the terminal.

import os
from get_time import get_time_of_day 


# init program
def init_program():
    print("Welcome to the To-Do List Manager!")
    print("You can add, view, and remove tasks.")
    start_program = input("\nDo you want to start the To-Do List Manager? (yes/no): ").strip().lower()
    return start_program

def todo_menu(name="Emmanuel"):
    # shows options and calls create/delete/edit/view
    print(f"Good {get_time_of_day()} Welcome Emmanuel 👋\n\nWhat would you like to get done:\nc - create\nd - delete\ne - edit\nv - view\n\n")



def main():
    begin = init_program() # start inital program

    # check weather to begin program or no
    if begin.lower() in ['yes', 'y']:
        pass
    elif begin.lower() not in ['no', 'n']:
        print("\nSee you later 👋\n")

# Only run main() if this file is executed directly
if __name__ == '__main__':
    # main()
    todo_menu()