import random
import tkinter as tk

def get_random_quote():
    return random.choice(quote_lines)

def display_quote():
    quote_label.config(text=get_random_quote())

def close_window():
    window.destroy()

def get_another_quote():
    display_quote()
    choice_label.config(text="")

def handle_choice(choice):
    if choice == "Yes":
        get_another_quote()
    elif choice == "No":
        close_window()

with open("the_line_of_p3.txt", "r") as the_lines:
    quote_lines = the_lines.readlines()

window = tk.Tk()
window.title("Random Quote Generator")

quote_label = tk.Label(window, text="", wraplength=300)
quote_label.pack(pady=10)

get_quote_button = tk.Button(window, text="Get Another Quote", command=display_quote)
get_quote_button.pack(pady=5)

choice_label = tk.Label(window, text="Do you want another quote line? (Yes/No):")
choice_label.pack(pady=5)

yes_button = tk.Button(window, text="Yes", command=lambda: handle_choice("Yes"))
yes_button.pack(pady=5)

no_button = tk.Button(window, text="No", command=lambda: handle_choice("No"))
no_button.pack(pady=5)

display_quote()  # Display initial quote

window.mainloop()
