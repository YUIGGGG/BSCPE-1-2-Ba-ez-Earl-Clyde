import tkinter as tk

def double_numbers():
    with open("numbers_to_double_and_triple.txt", "r") as the_square_and_cube:
        with open("double.txt", "w") as double_output:
            for line in the_square_and_cube:
                number = int(line.strip())
                squared_number = number ** 2
                double_output.write(f"{squared_number}\n")
            print("Doubled numbers are written to double.txt")

def triple_numbers():
    with open("numbers_to_double_and_triple.txt", "r") as the_square_and_cube:
        with open("triple.txt", "w") as triple_output:
            for line in the_square_and_cube:
                number = int(line.strip())
                cubed_number = number ** 3
                triple_output.write(f"{cubed_number}\n")
            print("Tripled numbers are written to triple.txt")

def display_doubled_numbers():
    result_text.delete(1.0, tk.END)  # Clear previous text
    with open("double.txt", "r") as double_file:
        for line in double_file:
            result_text.insert(tk.END, line.strip() + "\n")

def display_tripled_numbers():
    result_text.delete(1.0, tk.END)  # Clear previous text
    with open("triple.txt", "r") as triple_file:
        for line in triple_file:
            result_text.insert(tk.END, line.strip() + "\n")

window = tk.Tk()
window.title("Number Operations")

double_button = tk.Button(window, text="Double Numbers", command=double_numbers)
double_button.pack(pady=5)

triple_button = tk.Button(window, text="Triple Numbers", command=triple_numbers)
triple_button.pack(pady=5)

display_double_button = tk.Button(window, text="Display Doubled Numbers", command=display_doubled_numbers)
display_double_button.pack(pady=5)

display_triple_button = tk.Button(window, text="Display Tripled Numbers", command=display_tripled_numbers)
display_triple_button.pack(pady=5)

result_text = tk.Text(window, height=10, width=30)
result_text.pack(pady=10)

window.mainloop()
