#!/usr/bin/env python3
"""
Todo CLI App
Usage:
    python todo.py add "task description"
    python todo.py list
    python todo.py done <task_id>
    python todo.py remove <task_id>
    python todo.py clear
"""
import sys
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []
    
def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")

def add_task(text):
    tasks = load_tasks()
    task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "text": text,
        "done": False,
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {task['text']}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Use: python todo.py add \"task\"")
        return
    for t in tasks:
        status = "✔" if t["done"] else " "
        print(f"[{status}] {t['id']:>3} - {t['text']} (created: {t['created_at']})")

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            save_tasks(tasks)
            print(f"Marked #{task_id} done.")
            return
    print(f"Task #{task_id} not found.")

def remove_task(task_id):
    tasks = load_tasks()
    new = [t for t in tasks if t['id'] != task_id]
    if len(new) == len(tasks):
        print(f"Task #{task_id} not found.")
    else:
        save_tasks([])
        print(f"Removed task #{task_id}.")

def clear_all():
    save_tasks([])
    print("Cleared all tasks.")

def help_msg():
    print(__doc__)

def main(argv):
    if len(argv) < 2:
        help_msg()
        return
    cmd = argv[1].lower()
    if cmd == "add" and len(argv) >= 3:
        add_task(" ".join(argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(argv) == 3 and argv[2].isdigit():
        mark_done(int(argv[2]))
    elif cmd == "remove" and len(argv) == 3 and argv[2].isdigit():
        remove_task(int(argv[2]))
    elif cmd == "clear":
        clear_all()
    else:
        help_msg()

if __name__ == "__main__":
    main(sys.argv)
