import tkinter as tk


def calculate():
    try:
        operation = operation_var.get().lower()
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "addition":
            result = num1 + num2
        elif operation == "subtraction":
            result = num1 - num2
        elif operation == "multiplication":
            result = num1 * num2
        elif operation == "division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"

        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state=tk.DISABLED)

        ask_to_try_again()

    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Invalid input")
        output_text.config(state=tk.DISABLED)


def ask_to_try_again():
    try_again_prompt.config(state=tk.NORMAL)
    try_again_prompt.delete(1.0, tk.END)
    try_again_prompt.insert(tk.END, "Do you want to try again? (Y/N)")
    try_again_prompt.config(state=tk.DISABLED)

    button_yes.config(state=tk.NORMAL)
    button_no.config(state=tk.NORMAL)


def try_again(option):
    if option.lower() == "y":
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "CALCULATOR.")
        output_text.config(state=tk.DISABLED)
        try_again_prompt.config(state=tk.NORMAL)
        try_again_prompt.delete(1.0, tk.END)
        try_again_prompt.config(state=tk.DISABLED)
        button_yes.config(state=tk.DISABLED)
        button_no.config(state=tk.DISABLED)
    elif option.lower() == "n":
        root.destroy()


root = tk.Tk()
root.title("Mini Calculator")

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

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, columnspan=2)

output_text = tk.Text(root, height=2, width=30)
output_text.grid(row=4, columnspan=2)
output_text.insert(tk.END, "Can't add the calculator interface.")
output_text.config(state=tk.DISABLED)

try_again_prompt = tk.Text(root, height=1, width=30)
try_again_prompt.grid(row=5, columnspan=2)
try_again_prompt.config(state=tk.DISABLED)

button_yes = tk.Button(root, text="Yes", command=lambda: try_again("Y"), state=tk.DISABLED)
button_yes.grid(row=6, column=0)

button_no = tk.Button(root, text="No", command=lambda: try_again("N"), state=tk.DISABLED)
button_no.grid(row=6, column=1)

root.mainloop()
