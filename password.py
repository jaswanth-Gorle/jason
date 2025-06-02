import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_variable.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

def copy_to_clipboard():
    password = password_variable.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
window= tk.Tk()

tk.Label(window,text="password Generator",font=("Arial",16,"bold")).pack(pady=10)

tk.Label(window,text="password length",font=("Arial",12)).pack()
length_entry = tk.Entry(window, font=("Arial", 12), justify='center')
length_entry.pack(pady=5)
tk.Button(window,text="Generate password",font=("Arial",12),command=generate_password).pack(pady=10)
password_variable = tk.StringVar()
tk.Entry(window, textvariable=password_variable, font=("Arial", 12), justify='center', state='readonly').pack(pady=5)

tk.Button(window, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard).pack(pady=10)
window.mainloop()