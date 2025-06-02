import tkinter as tk
from tkinter import messagebox,filedialog

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Select Error", "Please select a task to delete.")
def save_task():
    tasks = task_listbox.get(0, tk.END)
    if not tasks:
        messagebox.showinfo("No Tasks", "There are no tasks to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")


def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        task_listbox.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())


window=tk.Tk()

window.title("To do list")
window.geometry("500x500")

task_entry=tk.Entry(window,width=20,font=("Arial",23))
task_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(window, text="Save Tasks", width=20, command=save_task)
save_button.pack(pady=5)

load_button = tk.Button(window, text="Load Tasks", width=20, command=load_tasks)
load_button.pack(pady=5)

task_listbox = tk.Listbox(window, width=30, height=10, font=('Arial', 12))
task_listbox.pack(pady=20)
window.mainloop()
