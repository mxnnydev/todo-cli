
# TODO CLI 📝
# A simple command-line to-do list manager built with Python. Allows users to add, view, and remove tasks directly from the terminal.

import os
from get_time import get_time_of_day 
from core.todo_functions import create, delete, edit, view


# init program
def init_program():
    print("👋 Welcome to the To-Do List Manager!")
    print("🧾 You can add, view, and remove your tasks with ease.")
    start_program = input("\nDo you want to start the To-Do List Manager? (yes/no): ").strip().lower()
    return start_program

def todo_menu(name="User"):
    # Shows options and calls create/delete/edit/view
    print(f"\nHello Good {get_time_of_day().capitalize()} {name}, what would you like to do?")
    # shows options and calls create/delete/edit/view
    print("c - Create 📝")
    print("d - Delete 🗑️")
    print("e - Edit ✏️")
    print("v - View 📋")

    menu_option = input("Select an option: ").strip().lower()

    while menu_option not in ['c', 'd', 'e', 'v']:
        # Invalid input print message
        print("Invalid option. Please select 'c', 'd', 'e' or 'v'.")
        # Show options again
        menu_option = input("Select an option: ").strip().lower()

    # Call the appropriate function based on the user's choice
    match menu_option:
        case 'c':
            create()
        case 'd':
            delete()
        case 'e':
            edit()
        case 'v':
            view()


# Main function to start the program
def main():
    begin = init_program() 

    # Check if the user wants to start the program
    if begin.lower() in ['yes', 'y']:
        print("\nStarting To-Do List Manager...")
        name = input("Please enter your name: ").strip().title() or "User"
        todo_menu(name)
    elif begin.lower() not in ['no', 'n']:
        print("\nSee you later 👋\n")

# Only run main() if this file is executed directly
if __name__ == '__main__':
    main()