import tkinter as tk
import openpyxl

def get_student_with_highest_gwa():
    file_name = "gwa_of_the_students"  # Specify the file name here
    highest_gwa = 0
    highest_gwa_student = ""

    # Open the Excel file
    wb = openpyxl.load_workbook(file_name + ".xlsx", read_only=True)
    sheet = wb.active

    # Iterate over each row in the Excel sheet
    for row in sheet.iter_rows(values_only=True):
        if len(row) < 2:
            continue  # Skip rows with insufficient data
        student, gwa, *_ = row  # Extract only the first two values and ignore the rest

        # Check if the GWA value is numeric
        try:
            gwa = float(gwa)
        except ValueError:
            # Skip rows with non-numeric GWA values
            continue

        if gwa > highest_gwa:
            highest_gwa = gwa
            highest_gwa_student = student

    # Close the workbook
    wb.close()

    return highest_gwa_student, highest_gwa

def display_highest_gwa():
    highest_student, highest_gwa = get_student_with_highest_gwa()
    highest_gwa_str.set(f"Student with the highest GWA:\n{highest_student}\nGWA: {highest_gwa}")

window = tk.Tk()
window.title("Highest GWA")
window.geometry("300x200")

highest_gwa_str = tk.StringVar()
highest_gwa_label = tk.Label(window, textvariable=highest_gwa_str, font=("Helvetica", 12), wraplength=250)
highest_gwa_label.pack(pady=20)

refresh_button = tk.Button(window, text="Refresh", command=display_highest_gwa)
refresh_button.pack()

display_highest_gwa()  # Initially display the highest GWA
window.mainloop()
