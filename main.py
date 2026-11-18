"""Student Task Manager - console application.

Run with:  python main.py
"""
from task_manager import TaskManager

STORAGE_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
"""


def show_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_add(manager):
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added: {task}")


def handle_complete(manager):
    show_tasks(manager)
    raw = input("ID of the task to complete: ").strip()
    if not raw.isdigit():
        print("Error: please enter a numeric task ID.")
        return
    try:
        task = manager.complete_task(int(raw))
    except KeyError as error:
        print(f"Error: {error.args[0]}")
        return
    print(f"Completed: {task}")


def handle_delete(manager):
    print("Deleting tasks is coming soon.")


def main():
    manager = TaskManager(STORAGE_FILE)
    actions = {
        "1": handle_add,
        "2": show_tasks,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
            continue
        action(manager)


if __name__ == "__main__":
    main()
