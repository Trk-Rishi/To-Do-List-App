## 1. Show the Task
## 2. Add Task
## 3. Delete Task
## 4. Save and Exit
import time
import datetime
import tkinter as tk
from tkinter import messagebox
import os

file_name = "ToDoTaskList.txt"

# def get_tasks():
#     try:
#         with open(file_name, "r") as f:
#             data = f.read()
#             print("Sure, here's the tasks ...")
#             print()
#             print(data)
#             print()
#             time.sleep(1.5)
#     except FileNotFoundError:
#         print("No such To-Do List exists")


# def save_task(task:str):
#     with open(file_name, "a") as f:
#         print("Add a time to complete this task by...")
#         date = input("Set Task Time ---> \ne.g.(15/10/2026 18:50)\nEnter: ")
#         time_ = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")
#         print("Task Successfully Added...")
#         print("Date Set:",time_.strftime("%A, %d %B %Y, %I:%M %p"))
#         f.write(f"{task} ---> {time_.strftime("%A, %d %B %Y, %I:%M %p")}\n")
#         time.sleep(1)
#         print()

# def clear_list():
#     with open(file_name,"w") as f:
#         f.write("")
#         print("List Cleared Successfully")
#         time.sleep(1)
#         print()

# def delete_list():
#     omega = input("Type 'CONFIRM' to delete the list: ")
#     if omega == "CONFIRM":
#         os.remove(file_name)
#     else:
#         print("Authorisation Failed")
#         print("Input did not match the correct code!!!")

def show_tasks():
    task_list.delete(0,tk.END)

    try:
        with open(file_name,"r") as f:
            data = f.readlines()

        for task in data:
            task_list.insert(tk.END, task.strip())

    except FileNotFoundError:
        pass

def delete_tasks():
    answer = messagebox.askyesno("CONFIRM","Are you sure you want to delete the list ?")
    if answer:
        try:
            os.remove(file_name)
            show_tasks()
            messagebox.showinfo("{Success}","List Deleted Successfully")
            root.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error","No List Exists")



def clear_tasks():
    with open(file_name,"w") as f:
        f.write("")
    show_tasks()
    messagebox.showinfo("Success","List Cleared Successfully")

def add_task():
    task = task_entry.get()
    date = date_entry.get()

    if task == "" or date == "":
        messagebox.showwarning("Warning", "Incomplete task and deadline !!!")
        return

    try:
        time_ = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")

        with open(file_name,"a") as f:
            f.write(f"{task} ---> {time_.strftime("%A, %d %B %Y, %I:%M %p")}\n")

        messagebox.showinfo("Success", "Task Added Successfully !!!!")

        task_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

        show_tasks()

    except ValueError:
        messagebox.showerror("Invalid Date","Enter date as DD/MM/YYYY HH:MM")


def toggle_numbering():
    numbering = tk.BooleanVar(value=False)

    def update_numbering():
        task_list.delete(0, tk.END)

        try:
            with open(file_name, "r") as f:
                data = f.readlines()

            for i , task in enumerate(data , start=1):
                if check.get():
                    task_list.insert(tk.END, f"{i}.  {task.strip()}")

                else:
                    task_list.insert(tk.END , task.strip())
        except FileNotFoundError:
            pass
    check = tk.BooleanVar(value=False)

    numbering_button = tk.Checkbutton(list_frame,text="Numbering",variable=check,command=update_numbering)
    numbering_button.pack(side=tk.LEFT, padx=5)
        


def mark_completed():
    try:
        selected = task_list.curselection()[0]

        with open(file_name,"r",encoding="utf-8") as f:
            data = f.readlines()

        if not data[selected].rstrip().endswith("[✓]"):
            data[selected] = data[selected].rstrip("\n") + "[✓]\n"

            with open(file_name,"w",encoding="utf-8") as f:
                f.writelines(data)

        task_list.delete(selected)
        task_list.insert(selected, data[selected].strip())

    except IndexError:
        messagebox.showwarning("Warning.","Select a task first !!!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")



title = tk.Label(root, text="MY TO-DO LIST", font=("Arial", 18))
title.pack(pady=10)

task_label = tk.Label(root, text="Enter Task:")
task_label.pack()

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

date_label = tk.Label(
    root,
    text="Deadline (DD/MM/YYYY HH:MM):"
)
date_label.pack()

date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=5)

add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task
)
add_button.pack(pady=5)

# show_button = tk.Button(
#     root,
#     text="Show Tasks",
#     command=show_tasks
# )
# show_button.pack(pady=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

task_list = tk.Listbox(list_frame, width=60, height=12)
task_list.pack(side=tk.LEFT)

toggle_numbering()


complete_button = tk.Button(root,text="Mark task as completed",command=mark_completed)
complete_button.pack(pady=3)

clear_button = tk.Button(
    root,
    text="Clear List",
    command=clear_tasks
)
clear_button.pack(pady=3)

delete_button = tk.Button(
    root,
    text="Delete List",
    command=delete_tasks
)
delete_button.pack(pady=3)

root.mainloop()

##hello ..
#testing...

##helllooo testingg again....

