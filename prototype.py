import time
from quotes import Motivation
tasks = []
selection = 0
pomodoros = 0
motivate = Motivation()
tasks = []


def add_task():
    task = input("What do you want to work on>?")
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
        main()
    else:
        print("No task entered. Please try again.")
        add_task()


def start_task():
    if not tasks:
        print("No tasks available. Please add a task first.")
        main()

    print("Current tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    selection = int(input("\nSelect a task to start the Pomodoro Timer:"))
    print(f"\nWorking on: {tasks[selection - 1]}")
    pomodoros = int(input("\nHow many Pomodoros do you want to assign for this task? (25-minute work, 5-minute break loops): "))
    print("\nStarting the Pomodoro Timer for 25 minutes...")
    for _ in range(pomodoros):
        start_timer()
    print("\nAll Pomodoros completed for this task!")
    main()


def start_timer():
    for i in range(25, 0, -1):
        print(motivate.get_motivation())
        print(f"{i} minutes remaining...")
        time.sleep(60)
    print("\nTime's up! Take a 5-minute break.")
    for i in range(5, 0, -1):
        print(f"{i} minutes remaining for break...")
        time.sleep(60)
    print("\nBreak's over! Back to work.")
        
    
def main():
    print("\nWelcome to the Pomodoro Timer!")
    print("1. Add Task")
    print("2. Start Task")
    print("3. Exit")
    choice = input("\nPlease select (1-3): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        start_task()
    elif choice == '3':
        print("\nExiting the Pomodoro Timer. Goodbye!")
        exit()
    else:
        print("\nInvalid choice. Please select from 1-3")
        main()


if __name__ == "__main__":
    main()
