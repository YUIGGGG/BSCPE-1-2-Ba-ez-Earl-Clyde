import tkinter as tk


def calculate():
    try:
        operation = operation_var.get().lower()
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "addition":
            result_of_addition = num1 + num2
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Result: " + str(result_of_addition))
            output_text.config(state=tk.DISABLED)

        elif operation == "subtraction":
            result_of_subtraction = num1 - num2
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Result: " + str(result_of_subtraction))
            output_text.config(state=tk.DISABLED)

        elif operation == "multiplication":
            result_of_multiplication = num1 * num2
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Result: " + str(result_of_multiplication))
            output_text.config(state=tk.DISABLED)

        elif operation == "division":
            result_of_division = num1 / num2
            output_text.config(state=tk.NORMAL)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Result: " + str(result_of_division))
            output_text.config(state=tk.DISABLED)

    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Invalid input. Please enter valid numbers.")
        output_text.config(state=tk.DISABLED)

    except ZeroDivisionError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Division by zero!")
        output_text.config(state=tk.DISABLED)


def update_number(number):
    current_text = entry_operation.get()
    entry_operation.delete(0, tk.END)
    entry_operation.insert(tk.END, current_text + number)


root = tk.Tk()
root.title("Calculator")

operation_var = tk.StringVar()

label_operation = tk.Label(root, text="Operation:")
label_operation.grid(row=0, column=0)

entry_operation = tk.Entry(root, textvariable=operation_var)
entry_operation.grid(row=0, column=1)

label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=1, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=2, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1)

button_frame = tk.Frame(root)
button_frame.grid(row=3, columnspan=2)

buttons = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("0", 3, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, width=5, height=2, command=lambda t=text: update_number(t))
    button.grid(row=row, column=col)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=4, columnspan=2)

output_text = tk.Text(root, height=4, width=20)
output_text.grid(row=6, columnspan=2)
output_text.insert(tk.END, "Disclaimer: The buttons are not working on Number 1 and Number 2.")
output_text.config(state=tk.DISABLED)

root.mainloop()
