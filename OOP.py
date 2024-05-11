#1. Get user's name and dream job input.
#2. Initialize a counter variable 'count' to 0.

#3. When a button is clicked:
#    a. Increment 'count'.
#    b. If 'count' is 1:
#        - Show user's name and dream job.
#
#4. Load and play the music file.

#5. Create a button in the main window:
#    - Text: "CLICK FOR USERNAME AND USER DREAM JOB"
#    - When clicked, execute the click function.



import tkinter as tk
from tkinter import Button
import pygame



user_name = input("What is your name? ")
user_dream_job = input("What is your dream job? ")
count = 0


def click():
    global count
    count += 1
    print(count)
    if count == 1:
        show_user_info()

def show_user_info():
    root = tk.Toplevel()
    root.title("Personal Information")
    root.geometry("300x150")

    user_name_and_dream_job = f"Name: {user_name}\nDream Job: {user_dream_job}"
    label = tk.Label(root, text=user_name_and_dream_job, width=600, height=300,
                     bg="black", fg="yellow")
    label.pack()


pygame.init()
pygame.mixer.music.load('Com_Eng_Song_Sound.mp3')  # Update with correct file path
pygame.mixer.music.play()

window = tk.Tk()

button = Button(window,
                text="CLICK FOR USERNAME AND USER DREAM JOB",
                command=click,
                font=("Comic Sans", 50),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=tk.ACTIVE)
button.pack()


window.mainloop()
