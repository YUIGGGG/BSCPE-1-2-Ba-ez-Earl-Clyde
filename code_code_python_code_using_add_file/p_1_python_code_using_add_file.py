import tkinter as tk

def even_numbers(number):
    return number % 2 == 0

def read_numbers():
    even_numbers_list = []
    odd_numbers_list = []
    with open("numbers_from_p_1.txt", "r") as the_integers:
        for line in the_integers:
            number = int(line.strip())
            if even_numbers(number):
                even_numbers_list.append(number)
            else:
                odd_numbers_list.append(number)
    return even_numbers_list, odd_numbers_list

def display_even_numbers():
    even_numbers_list, _ = read_numbers()
    even_str = "\n".join(map(str, even_numbers_list))
    even_label.config(text=even_str)

def display_odd_numbers():
    _, odd_numbers_list = read_numbers()
    odd_str = "\n".join(map(str, odd_numbers_list))
    odd_label.config(text=odd_str)

window = tk.Tk()
window.title("Even and Odd Numbers")
window.geometry("400x300")

even_button = tk.Button(window, text="Even Numbers", command=display_even_numbers)
even_button.pack(pady=10)

even_label = tk.Label(window, text="", bg="lightblue", width=30, height=10)
even_label.pack(pady=5)

odd_button = tk.Button(window, text="Odd Numbers", command=display_odd_numbers)
odd_button.pack(pady=10)

odd_label = tk.Label(window, text="", bg="lightpink", width=30, height=10)
odd_label.pack(pady=5)

window.mainloop()
