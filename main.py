import os
import sys
from datetime import datetime
import json

class Task:
    def __init__(self, description: str, id: int):
        self.id = id
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
        self.updatedAt = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }


class TodoApp():
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.id_count = 1
        self.total_tasks = 0
        self.tasks = {}
        self.init_app()

    def init_app(self):
        if not os.path.exists(self.filename):
            data = {
                "id_count": self.id_count,
                "total_tasks": self.total_tasks,
                "tasks": self.tasks
            }
            with open(self.filename, "w") as db:
                json.dump(data, db, indent=2)
                return
        
        with open(self.filename, "r") as db:
            data = json.load(db)
            self.id_count = data.get("id_count")
            self.total_tasks = data.get("total_tasks")
            self.tasks = data.get("tasks")

    def add_task(self, title: str):
        task = Task(title, id=self.id_count)
        self.id_count += 1
        self.total_tasks += 1
        self.tasks[task.id] = task.to_dict()
        self.save_tasks()
        print(f"Task added successfully (ID: {task.id})")

    def update_task(self, task_id: int, new_title: str):
        task = self.get_task(task_id)
        if not task:
            print(f"Task {task_id} does not exist")
        else:
            task["description"] = new_title
            self.save_tasks()
            print(f"Task updated successfully (ID: {task_id})")

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            print(f"Task {task_id} does not exist")
        else:
            self.tasks.pop(task_id)
            self.total_tasks -= 1
            self.save_tasks()
            print(f"Task deleted successfully (ID: {task_id})")

    def list_tasks(self, filter=None):
        if not filter:
            for tasks in self.tasks.values():
                print(tasks["description"], tasks["status"])
        
        match filter:
            case 'todo':
                for tasks in self.tasks.values():
                    if tasks["status"] == 'todo':
                        print(tasks["description"], tasks["status"])
            case 'done':
                for tasks in self.tasks.values():
                    if tasks["status"] == 'done':
                        print(tasks["description"], tasks["status"])
            case 'in-progress':
                for tasks in self.tasks.values():
                    if tasks["status"] == 'in-progres':
                        print(tasks["description"], tasks["status"])
            case _:
                print("Invalid Argument.\nUse todo, done or in-progress")

    def save_tasks(self):
        data = {
                "id_count": self.id_count,
                "total_tasks": self.total_tasks,
                "tasks": self.tasks
            }
        with open(self.filename, "w") as db:
            json.dump(data, db, indent=2)

    def get_task(self, task_id: int):
        return self.tasks.get(task_id)

def main():
    if len(sys.argv) < 2:
        print("Invalid!\nUsage: python main.py <command> [arg]")
        return
    
    app = TodoApp()

    match sys.argv[1]:
        case 'add':
            if len(sys.argv) != 3:
                print("Invalid!\nUsage: python main.py add \"task title\"")
                return
            app.add_task(sys.argv[2])
        case 'update':
           if len(sys.argv) != 4:
                print("Invalid!\nUsage: python main.py update task_id \"task title\"")
                return
           app.update_task(sys.argv[2], sys.argv[3])
        case 'delete':
           if len(sys.argv) != 3:
                print("Invalid!\nUsage: python main.py delete task_id")
                return
           app.delete_task(sys.argv[2])
        case 'mark-in-progress':
            print("Task marked in progress")
        case 'mark-done':
            print("Task marked as done")
        case 'list':
            if len(sys.argv) > 3:
                print("Invalid!\nUsage: python main.py list [optional arg]")
                return
            try:
                app.list_tasks(sys.argv[2])
            except IndexError:
                app.list_tasks()

        case _:
            print("Invalid command")


if __name__ == "__main__":
    main()