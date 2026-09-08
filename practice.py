# a = int(input("enter a number"))
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# area = int(input("enter area of circle"))
# print("area of circle ",3.14*area*area)

# length = int(input("enter length of reactangle"))
# breath = int(input("enter brath of reactangle"))
# area = length * breath 
# print(area)

# cube = int(input("enter a number"))
# cube1 = cube**3
# print(cube1)

# marks = int(input("enter a marks"))
# marks = (marks/500)*100
# print("percentage=",marks)


# Celsius = float(input("enter a Celsius temperature"))
# Fahrenheit =( 9/5)*Celsius+32
# print(Fahrenheit)

import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "users.json"

# File create if not exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f)

def signup():
    users = load_users()

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Warning", "Fill all fields")
        return

    if username in users:
        messagebox.showerror("Error", "Username already exists")
        return

    users[username] = password
    save_users(users)

    messagebox.showinfo("Success", "Account Created Successfully")

def login():
    users = load_users()

    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        open_home(username)
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

def open_home(username):
    home = tk.Toplevel(root)
    home.title("Home")
    home.geometry("400x300")

    tk.Label(home, text=f"Welcome {username}", font=("Arial",18)).pack(pady=40)

    tk.Button(
        home,
        text="Logout",
        command=home.destroy,
        bg="red",
        fg="white",
        width=15
    ).pack()

root = tk.Tk()
root.title("Social Media App")
root.geometry("400x450")

tk.Label(root,text="SOCIAL APP",font=("Arial",20,"bold")).pack(pady=20)

tk.Label(root,text="Username").pack()

username_entry=tk.Entry(root,width=30)
username_entry.pack(pady=5)

tk.Label(root,text="Password").pack()

password_entry=tk.Entry(root,show="*",width=30)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Sign Up",
    command=signup,
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="Login",
    command=login,
    bg="blue",
    fg="white",
    width=20
).pack()

root.mainloop()