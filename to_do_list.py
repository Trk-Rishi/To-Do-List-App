## 1. Show the Task
## 2. Add Task
## 3. Delete Task
## 4. Save and Exit
import time

tasks = []
file_name = "ToDoTaskList.txt"

def get_tasks():
    with open(file_name, "r") as f:
        data = f.read()
        print("Sure, here's the tasks ...")
        print(data)
        time.sleep(1.5)


def save_task(task:str):
    with open(file_name, "a") as f:
        f.write(f"{task}\n")
        print("Task Successfully Added...")

save_task("1. Say Hello")
get_tasks()

save_task("2. Say Wssup")
get_tasks()

def clear_list():
    with open(file_name,"w") as f:
        f.write("")
        print("List Cleared Successfully")

clear_list()
get_tasks()