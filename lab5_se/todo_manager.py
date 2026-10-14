"""Simple to-do list and task manager."""
import json
import re
import secrets
import subprocess  # nosec B404 - used without a shell, arguments validated
from datetime import datetime

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium"):
    """Add a task and return its id."""
    task_id = len(tasks) + 1
    tasks[task_id] = {"title": title, "priority": priority, "done": False,
                      "created": datetime.now().isoformat()}
    return task_id


def complete_task(task_id):
    """Mark a task as done. Return True if it exists, else False."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True
    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return titles of pending tasks, highest priority first."""
    pending = [task for task in tasks.values() if not task["done"]]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword):
    """Return the id of the first task whose title contains keyword.

    Returns None if no task matches.
    """
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks_saved.json"):
    """Save all tasks to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file)


def load_tasks(file_name="tasks_saved.json"):
    """Load tasks from a JSON file and return them as a dict."""
    with open(file_name, "r", encoding="utf-8") as file:
        return {int(key): value for key, value in json.load(file).items()}


def export_json(file_name="tasks.json"):
    """Export all tasks to a human-readable JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def remind_by_email(address):
    """Email the exported task file to the given address."""
    # Helper kept for the lab: not called by the demo
    if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", address):
        raise ValueError("Invalid email address")
    with open("tasks.json", "r", encoding="utf-8") as file:
        subprocess.run(  # nosec B603 B607 - no shell, address validated above
            ["mail", "-s", "Pending tasks", address],
            stdin=file, check=True)


def main():
    """Run a short demonstration of the task manager."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")
    complete_task(2)
    complete_task(99)
    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))  # returns None silently
    suggestion = secrets.choice(pending_tasks())
    print("Try this next:", suggestion)
    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
