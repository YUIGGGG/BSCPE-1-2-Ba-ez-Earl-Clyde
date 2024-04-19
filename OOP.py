import tkinter as tk
from tkinter import Button, Label, ACTIVE
from playsound import playsound

def get_user_info():
    user_name = input("What is your name? ")
    user_dream_job = input("What is your dream job? ")
    return user_name, user_dream_job

def show_user_info():
    global user_name, user_dream_job
    root = tk.Toplevel()
    root.title("Personal Information")
    root.geometry("300x150")

    user_name_and_dream_job = f"Name: {user_name}\nDream Job: {user_dream_job}"
    label = tk.Label(root, text=user_name_and_dream_job, width=300, height=150,
                     bg="black", fg="yellow")
    label.pack()

def click():
    global count
    count += 1
    print(count)
    if count == 1:
        show_user_info()

def play_sound():
    playsound(r'com_eng_song.mp3')

count = 0
user_name, user_dream_job = get_user_info()

window = tk.Tk()
button = Button(window,
                text="CLICK FOR USERNAME AND USER DREAM JOB",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE)
button.pack()

play_sound()  # Play the sound
window.mainloop()
