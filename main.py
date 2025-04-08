import os
import sys
from datetime import datetime
import json

class Task:
    _id_counter = 1

    def __init__(self, description):
        self.id = Task._id_counter
        Task._id_counter =+ 1
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()


class TodoApp():
    def __init__(self, filename = "tasks.json"):
        self.filename = filename
        self.init_app()

    def init_app(self):
        if not os.path.exists(self.filename):
            data = {
                "id_count": 1,
                "total_tasks": 0,
                "tasks": {}
            }
            with open(self.filename, "w") as db:
                json.dump(data, db, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [arg]")
        return
    
    app = TodoApp()

    match sys.argv[1]:
        case 'add':
            print("Task added")
        case 'update':
           print("Task updated")
        case 'delete':
           print("Task deleted")
        case 'mark-in-progress':
            print("Task marked in progress")
        case 'mark-done':
            print("Task marked as done")
        case 'list':
            print("Task listed")
        case _:
            print("Invalid command")


if __name__ == "__main__":
    main()