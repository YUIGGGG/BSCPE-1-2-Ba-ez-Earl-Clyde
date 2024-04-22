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

highest_student, highest_gwa = get_student_with_highest_gwa()
print("Student with the highest GWA is:", highest_student)
print("GWA:", highest_gwa)
