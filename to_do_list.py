import json
import os
import sys

TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read tasks file, starting with empty list.")
            return []
    else:
        return []


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError:
        print("Error: Could not save tasks to file.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task.get('done') else "[ ]"
        print(f"{idx}. {status} {task.get('description')}")


def add_task(tasks, description):
    if not description.strip():
        print("Error: Task description cannot be empty.")
        return
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f'Task added: "{description}"')


def delete_task(tasks, task_number):
    if not task_number.isdigit():
        print("Error: Task number must be a positive integer.")
        return
    idx = int(task_number) - 1
    if 0 <= idx < len(tasks):
        task = tasks.pop(idx)
        save_tasks(tasks)
        print(f'Task deleted: "{task.get("description")}"')
    else:
        print("Error: Task number does not exist.")


def mark_done(tasks, task_number):
    if not task_number.isdigit():
        print("Error: Task number must be a positive integer.")
        return
    idx = int(task_number) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['done'] = True
        save_tasks(tasks)
        print(f'Task marked as done: "{tasks[idx].get("description")}"')
    else:
        print("Error: Task number does not exist.")


def print_help():
    help_text = """
To-Do List Application - Commands:
  add "task description"    Add a new task
  delete TASK_NUMBER         Delete a task by its number
  done TASK_NUMBER           Mark a task as done by its number
  list                      List all tasks
  help                      Show this help message
"""
    print(help_text)


def main():
    tasks = load_tasks()

    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            return
        description = " ".join(sys.argv[2:])
        add_task(tasks, description)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: Missing task number to delete.")
            return
        delete_task(tasks, sys.argv[2])
    elif command == 'done':
        if len(sys.argv) < 3:
            print("Error: Missing task number to mark as done.")
            return
        mark_done(tasks, sys.argv[2])
    elif command == 'list':
        list_tasks(tasks)
    elif command == 'help':
        print_help()
    else:
        print(f"Error: Unknown command '{command}'.")
        print_help()



main()
