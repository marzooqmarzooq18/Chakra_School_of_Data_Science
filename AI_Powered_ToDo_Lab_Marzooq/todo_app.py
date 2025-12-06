import json
import os
import logging

# ---------- Setup Logging ----------
logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TASK_FILE = "tasks.json"


# ---------- Helper Functions ----------
def load_tasks():
    """Load tasks from JSON file, return empty list if file missing or corrupted."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        logging.error("Failed to load tasks. Returning empty list.")
        return []


def save_tasks(tasks):
    """Save the task list to JSON file."""
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")


# ---------- Core Features ----------
def add_task():
    """Add a new task."""
    task_name = input("Enter new task: ").strip()
    if not task_name:
        print("Task name cannot be empty!")
        return

    tasks = load_tasks()
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    save_tasks(tasks)

    logging.info(f"Task added: {task_name}")
    print(f"Task '{task_name}' added successfully.")


def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print(" No tasks found.")
        return

    print("\n--- TO-DO LIST ---")
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["completed"] else "⏳ Pending"
        print(f"{i}. {t['task']} — {status}")
    print("------------------")


def mark_complete():
    """Mark a task as completed."""
    tasks = load_tasks()
    if not tasks:
        print(" No tasks to mark.")
        return

    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            logging.info(f"Task marked complete: {tasks[num - 1]['task']}")
            print(" Task marked as complete.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")


def delete_task():
    """Delete a selected task."""
    tasks = load_tasks()
    if not tasks:
        print(" No tasks to delete.")
        return

    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            logging.info(f"Task deleted: {removed['task']}")
            print(f" Task '{removed['task']}' deleted.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")


def search_task():
    """Search tasks by keyword."""
    tasks = load_tasks()
    keyword = input("Enter keyword to search: ").strip().lower()

    found = [t for t in tasks if keyword in t["task"].lower()]
    if not found:
        print(" No matching tasks found.")
    else:
        print("\n--- SEARCH RESULTS ---")
        for i, t in enumerate(found, start=1):
            status = " Done" if t["completed"] else "⏳ Pending"
            print(f"{i}. {t['task']} — {status}")
        print("----------------------")


# ---------- Menu System ----------
def show_menu():
    print("""
========= TO-DO MANAGER =========
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Search Task
6. Exit
=================================
""")


def main():
    """Main program loop."""
    print("Welcome to AI-Powered To-Do Manager!")
    while True:
        show_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            print("👋 Goodbye! Your tasks are saved.")
            logging.info("Application closed by user.")
            break
        else:
            print("⚠️ Invalid choice. Please select 1–6.")


if __name__ == "__main__":
    main()
