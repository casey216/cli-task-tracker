import os
import sys
from datetime import datetime

class Task:
    _id_counter = 1

    def __init__(self, description):
        self.id = Task._id_counter
        Task._id_counter =+ 1
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()

def main():

    # create database file
    filename = "tasks.json"
    if not os.path.exists(filename):
        with open(filename, "w") as db:
            pass

    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [arg]")
        return
    
    match sys.argv[1]:
        case 'add':
            pass
        case 'update':
            pass
        case 'delete':
            pass
        case 'mark-in-progress':
            pass
        case 'mark-done':
            pass
        case 'list':
            pass
        case _:
            pass


if __name__ == "__main__":
    main()