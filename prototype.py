import time  # Import time module for sleep functionality
from quotes import Motivation  # Import Motivation class from quotes.py
tasks = []  # Initialize an empty list to hold tasks
selection = 0  # Initialize selection to zero
pomodoros = 0  # Initialize pomodoros to zero
motivate = Motivation()  # Create an instance of Motivation class
tasks = []  # Initialize an empty list to hold tasks


def add_task():  # Function to add a task
    task = input("What do you want to work on>?")  # Prompt user for a task
    if task:  # Check if the task is not empty
        tasks.append(task)  # Add the task to the tasks list
        print(f"Task '{task}' added.")
        main()  # Return to the main menu
    else:
        print("No task entered. Please try again.")
        add_task()  # If no task entered, prompt again


def start_task():  # Function to start a task
    if not tasks:  # Check if there are no tasks available
        print("No tasks available. Please add a task first.")
        main()  # Return to the main menu if no tasks are available

    print("Current tasks:")
    for i, task in enumerate(tasks, start=1):  # Enumerate through tasks to display them
        print(f"{i}. {task}")  # Print each task with its index
    
    selection = int(input("\nSelect a task to start the Pomodoro Timer:"))  # Prompt user to select a task
    print(f"\nWorking on: {tasks[selection - 1]}")  # Display the selected task
    pomodoros = int(input("\nHow many Pomodoros do you want to assign for this task? (25-minute work, 5-minute break loops): "))  # Prompt user for number of Pomodoros
    print("\nStarting the Pomodoro Timer for 25 minutes...")  # Notify user that the timer is starting
    for _ in range(pomodoros):  # Loop through the number of Pomodoros
        start_timer()  # Call the start_timer function for each Pomodoro
    print("\nAll Pomodoros completed for this task!")
    main()  # Return to the main menu after completing all Pomodoros


def start_timer():  # Function to start the Pomodoro timer
    for i in range(25, 0, -1):  # Loop for 25 minutes countdown
        print(motivate.get_motivation())  # Print a motivational quote using the Motivation class
        print(f"{i} minutes remaining...")  # Print remaining time
        time.sleep(60)  # Sleep for 60 seconds (1 minute)
    print("\nTime's up! Take a 5-minute break.")
    for i in range(5, 0, -1):  # Loop for 5 minutes countdown for break
        print(f"{i} minutes remaining for break...")
        time.sleep(60) 
    print("\nBreak's over! Back to work.")
        
    
def main():  # Main function to display the menu and handle user input
    print("\nWelcome to the Pomodoro Timer!")
    print("1. Add Task")
    print("2. Start Task")
    print("3. Exit")
    choice = input("\nPlease select (1-3): ")  # Prompt user for menu choice
    if choice == '1':
        add_task()  # Call the add_task function if user selects option 1
    elif choice == '2':
        start_task()  # Call the start_task function if user selects option 2
    elif choice == '3':
        print("\nExiting the Pomodoro Timer. Goodbye!")
        exit()  # Exit the program if user selects option 3
    else:
        print("\nInvalid choice. Please select from 1-3")
        main()  # Return to the main menu for invalid input


if __name__ == "__main__":
    main()  # Check if the script is being run directly
