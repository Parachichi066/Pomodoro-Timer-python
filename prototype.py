import time
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

def start_timer():
    if not tasks:
        print("No tasks available. Please add a task first.")
        main()

    print("Current tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    pomodoros = int(input("How many Pomodoros do you want to complete? (default is 1): "))


    print("Starting the Pomodoro Timer for 25 minutes...")
    for i in range(25, 0, -1):
        print(f"{i} minutes remaining...", end='\r')
        time.sleep(60)
        # Insert quote function here
    print("\nTime's up! Take a 5-minute break.")
    for i in range(5, 0, -1):
        print(f"{i} minutes remaining for break...", end='\r')
        time.sleep(60)
    
    
def main():
    print("Welcome to the Pomodoro Timer!")
    print("1. Add Task")
    print("2. Start Timer")
    print("3. Exit")
    choice = input("\nPlease select (1-3): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        start_timer()
    elif choice == '3':
        print("Exiting the Pomodoro Timer. Goodbye!")
        exit()
    else:
        print("Please select from 1-3")
        main()