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
        print(data)
        print("Sure, here's the tasks ...")
        time.sleep(1.5)
get_tasks()

def save_task(task):
    with open(file_name, "w") as f:
        f.write(f"{task}\n")
        print("Task Successfully Added...")

save_task("I'm the Coder !!!")
get_tasks()

save_task("Testing 1 2 3")
get_tasks()

save_task("Is this on top ???")
get_tasks()
