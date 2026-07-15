# ==============================
# 📚 Python Intensive Course
# ==============================

# ==============================
# 🔄 Project 3: To-Do List Manager
# ==============================

import os
from datetime import datetime

# file to store text
TASK_FILE = "task.txt"

# load task from file
def load_task():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                # Fixed: changed variable 'task' to 'task_name' to avoid conflict
                task_name, time, priority = line.strip().split("||")
                tasks.append({"task": task_name.strip(), "time": time.strip(), "priority": int(priority.strip())})
    return tasks

# save tasks to file
def save_task(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            # Fixed: Changed inner double quotes to single quotes
            file.write(f"{t['task']} || {t['time']} || {t['priority']} \n")

# add task
def add_task(tasks):
    task_name = input("Enter task: ")
    priority = int(input("Enter priority (1=High, 2=Medium, 3=Low): "))
    time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    # Fixed: Appending to 'tasks' list instead of 'task' string
    tasks.append({"task": task_name, "time": time, "priority": int(priority)})
    save_task(tasks)
    print("✅ Task added")

def view_task(tasks):
    if not tasks:
        print("No tasks available")
        return
    else:
        sorted_task = sorted(tasks, key=lambda x: x['priority'])  # sorted by priority
        print("\n Your tasks 📰")
        for i, t in enumerate(sorted_task, 1):
            print(f" {i}. {t['task']} (Priority: {t['priority']}, Added: {t['time']})")

def delete_task(tasks):
    view_task(tasks)
    try:
        choice = int(input("Enter task no to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_task(tasks) #need to save again
            print(f" {removed['task']} is deleted 👌")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")

def main():
    tasks = load_task()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add task\n2. View tasks\n3. Delete task\n4. Exit\n")
        choice = input("Enter an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye")
            break  # Stops the while loop to exit cleanly
        else:
            print("Invalid choice. Try again")

# Fixed: Changed "main" to "__main__"
if __name__ == "__main__":
    main()