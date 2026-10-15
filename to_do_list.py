## 1. Show the Task
## 2. Add Task
## 3. Delete Task
## 4. Save and Exit
import time
import datetime
import os

tasks = []
file_name = "ToDoTaskList.txt"

def get_tasks():
    try:
        with open(file_name, "r") as f:
            data = f.read()
            print("Sure, here's the tasks ...")
            print(data)
            print()
            time.sleep(1.5)
    except FileNotFoundError:
        print("No such To-Do List exists")


def save_task(task:str):
    with open(file_name, "a") as f:
        f.write(f"{task}\n")
        print("Add a time to complete this task by...")
        date = input("Set Task Time ---> \ne.g.(15/10/2026 18:50)\nEnter: ")
        time_ = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")
        print("Task Successfully Added...")
        print("Date Set:",time_.strftime("%A, %d %B %Y, %I:%M %p"))
        time.sleep(1)
        print()

def clear_list():
    with open(file_name,"w") as f:
        f.write("")
        print("List Cleared Successfully")
        time.sleep(1)
        print()

def delete_list():
    omega = input("Type 'CONFIRM' to delete the list: ")
    if omega == "CONFIRM":
        os.remove(file_name)
    else:
        print("Authorisation Failed")
        print("Input did not match the correct code!!!")

save_task("1. Hi Guys")
