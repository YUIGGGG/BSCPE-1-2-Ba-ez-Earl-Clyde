import tkinter as tk


def calculate():
    operation = operation_var.get().lower()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if operation == "addition" or operation == "add":
        result = num1 + num2
    elif operation == "subtraction" or operation == "subtract" or operation == "minus":
        result = num1 - num2
    elif operation == "multiplication" or operation == "multiply" or operation == "times":
        result = num1 * num2
    elif operation == "division" or operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    else:
        result = "Invalid operation entered."

    label_result.config(text="Result: " + str(result))


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
    button = tk.Button(button_frame, text=text, width=5, height=2)
    button.grid(row=row, column=col)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=4, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=5, columnspan=2)

root.mainloop()
