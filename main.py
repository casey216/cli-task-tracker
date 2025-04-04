import os

def main(*args, **kwargs):

    # create database file
    filename = "tasks.json"
    if not os.path.exists(filename):
        with open(filename, "w") as db:
            pass